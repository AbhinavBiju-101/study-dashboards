"""Full-text search over every dashboard's notes.

At first use each dashboard's pages are rendered in-process (no HTTP), split into sections at
every heading, and kept in memory.  A hit links straight to the heading's anchor.
"""
import html
import re
import threading
from html.parser import HTMLParser

SKIP = {"script", "style", "svg", "noscript", "template", "nav", "footer"}
HEADINGS = {"h1", "h2", "h3", "h4"}
WORD = re.compile(r"[\w'’-]+", re.U)


class _SectionParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.sections, self.page_title = [], ""
        self._skip = 0
        self._anchor = None
        self._cur = None
        self._h = None  # (level, anchor, [text])

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self._skip += 1
            return
        if self._skip:
            return
        a = dict(attrs)
        if a.get("id"):
            self._anchor = a["id"]
        if tag in HEADINGS:
            self._flush()
            self._h = (tag, self._anchor, [])
        elif self._h:
            self._h[2].append(" ")  # "<span>5.5</span>Hadamard" -> "5.5 Hadamard"

    def handle_endtag(self, tag):
        if tag in SKIP:
            self._skip = max(0, self._skip - 1)
            return
        if self._skip:
            return
        if self._h and tag != self._h[0]:
            self._h[2].append(" ")
        if self._h and tag == self._h[0]:
            title = re.sub(r"\s+", " ", "".join(self._h[2])).strip()
            if title:
                if not self.page_title and tag == "h1":
                    self.page_title = title
                self._cur = {"heading": title, "anchor": self._h[1], "text": []}
            self._h = None

    def handle_data(self, data):
        if self._skip:
            return
        if self._h:
            self._h[2].append(data)
        elif self._cur is not None:
            self._cur["text"].append(data)

    def _flush(self):
        if self._cur is not None:
            self._cur["text"] = re.sub(r"\s+", " ", " ".join(self._cur["text"])).strip()
            self.sections.append(self._cur)
            self._cur = None

    def close(self):
        super().close()
        self._flush()


class NoteIndex:
    def __init__(self, apps, subjects):
        self._apps, self._subjects = apps, {s["slug"]: s for s in subjects}
        self._lock = threading.Lock()
        self.docs, self.pages, self.ready = [], {}, False

    def ensure(self):
        if self.ready:
            return
        with self._lock:
            if not self.ready:
                self._build()
                self.ready = True

    def _build(self):
        docs, pages = [], {}
        for slug, app in self._apps.items():
            client = app.test_client()
            hdr = {"X-Hub-Index": "1"}
            home = client.get("/", headers=hdr).get_data(as_text=True)
            pattern = re.compile(self._subjects[slug]["note_pattern"])
            paths = sorted({h for h in re.findall(r'href="([^"#?]+)', home) if pattern.fullmatch(h)},
                           key=lambda p: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", p)])
            pages[slug] = []
            for path in paths:
                resp = client.get(path, headers=hdr)
                if resp.status_code != 200 or "html" not in resp.mimetype:
                    continue
                p = _SectionParser()
                p.feed(resp.get_data(as_text=True))
                p.close()
                title = p.page_title or path
                pages[slug].append({"url": f"/{slug}{path}", "title": title})
                for sec in p.sections:
                    url = f"/{slug}{path}" + (f"#{sec['anchor']}" if sec["anchor"] else "")
                    docs.append({"subject": slug, "page": title, "heading": sec["heading"], "url": url, "text": sec["text"],
                                 "h_l": sec["heading"].lower(), "t_l": sec["text"].lower()})
        self.docs, self.pages = docs, pages

    def search(self, query, subject=None, limit=40):
        self.ensure()
        toks = [t for t in WORD.findall(query.lower()) if len(t) > 1][:8]
        if not toks:
            return {"total": 0, "results": []}
        phrase = " ".join(toks)
        scored = []
        for d in self.docs:
            if subject and d["subject"] != subject:
                continue
            score = 0
            for t in toks:
                in_h, c = t in d["h_l"], d["t_l"].count(t)
                if not in_h and not c:
                    break
                score += (8 if in_h else 0) + min(c, 6)
            else:
                if len(toks) > 1:
                    score += 12 if phrase in d["h_l"] else (5 if phrase in d["t_l"] else 0)
                scored.append((score, d))
        scored.sort(key=lambda x: -x[0])
        rx = re.compile("|".join(re.escape(t) for t in sorted(toks, key=len, reverse=True)), re.I)
        results = []
        for score, d in scored[:limit]:
            s = self._subjects[d["subject"]]
            results.append({"subject": d["subject"], "code": s["code"], "accent": s["accent"], "page": d["page"],
                            "heading": d["heading"], "url": d["url"], "snippet": self._snippet(d["text"], rx),
                            "heading_html": self._mark(d["heading"], rx)})
        return {"total": len(scored), "results": results}

    @staticmethod
    def _mark(text, rx):
        out, pos = [], 0
        for m in rx.finditer(text):
            out.append(html.escape(text[pos:m.start()]))
            out.append("<mark>" + html.escape(m.group(0)) + "</mark>")
            pos = m.end()
        out.append(html.escape(text[pos:]))
        return "".join(out)

    def _snippet(self, text, rx, width=240):
        m = rx.search(text)
        if not m:
            return html.escape(text[:width]) + ("…" if len(text) > width else "")
        start = max(0, m.start() - 70)
        if start:
            start = text.rfind(" ", 0, start) + 1 or start
        frag = text[start:start + width]
        return ("…" if start else "") + self._mark(frag, rx) + ("…" if start + width < len(text) else "")
