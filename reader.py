"""CommonReader (experimental): one reader for every notes dashboard.

Each dashboard is built differently (EVS has weeks, BE has modules, PHY has module/topic/subtopic pages, BAMAT101 serves
converted PDF sections ...).  CommonReader does not need to know any of that.  It does what a person would do:
open the dashboard, follow its notes-page links (the `note_pattern` already in subjects.py), and read the headings.
From those it builds ONE normalised course outline:

    Course  { slug, code, title, accent, blurb, stats{...}, modules[ Module ] }
    Module  { id, title, url, summary, words, minutes, topics[ Topic ] }          <- one notes page
    Topic   { id, title, url, summary, words, minutes, subtopics[ Topic ] }       <- h2 sections, with h3/h4 nested

so the same "common dashboard" template renders any subject, and a new subject only needs an entry in subjects.py.
The sub-apps are read in-process through Flask's test client (no network, no changes to the dashboards).
"""
import re
import threading
from html.parser import HTMLParser

from search import clean_tex

SKIP = {"script", "style", "svg", "noscript", "template", "nav", "footer", "button", "form", "select", "option"}
HEADINGS = {"h1": 1, "h2": 2, "h3": 3, "h4": 4}
WPM = 200  # reading speed used for "x min read"


def _clean(text):
    return re.sub(r"\s+", " ", clean_tex(text)).strip()


def _first_sentence(text, limit=170):
    text = text.strip()
    if not text:
        return ""
    m = re.match(r"(.{40,%d}?[.!?])(\s|$)" % limit, text)
    out = m.group(1) if m else text[:limit]
    return out + ("…" if not m and len(text) > limit else "")


class _Outline(HTMLParser):
    """Collects headings (level, anchor, text) and the words/snippet that follow each one."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items = []          # {level, anchor, title, text:[...]}
        self.page_title = ""
        self._skip = 0
        self._anchor = None
        self._h = None           # [level, anchor, parts]
        self._cur = None

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self._skip += 1
            return
        if self._skip:
            return
        a = dict(attrs)
        if tag in HEADINGS:
            self._h = [HEADINGS[tag], a.get("id") or self._anchor, []]
            return
        if a.get("id"):
            self._anchor = a["id"]
        if self._h:
            self._h[2].append(" ")

    def handle_endtag(self, tag):
        if tag in SKIP:
            self._skip = max(0, self._skip - 1)
            return
        if self._skip:
            return
        if self._h and tag in HEADINGS and HEADINGS[tag] == self._h[0]:
            title = _clean("".join(self._h[2]))
            if title:
                if self._h[0] == 1 and not self.page_title:
                    self.page_title = title
                if self._h[0] > 1:
                    self._cur = {"level": self._h[0], "anchor": self._h[1], "title": title, "text": []}
                    self.items.append(self._cur)
                else:
                    self._cur = None
            self._h = None
        elif self._h:
            self._h[2].append(" ")

    def handle_data(self, data):
        if self._skip:
            return
        if self._h:
            self._h[2].append(data)
        elif self._cur is not None:
            self._cur["text"].append(data)
        elif not self.items:
            self.intro = getattr(self, "intro", []) + [data]


def _natural(path):
    return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", path)]


class CommonReader:
    def __init__(self, apps, subjects, bank_counts=None):
        self._apps, self._subjects = apps, {s["slug"]: s for s in subjects}
        self._order = [s["slug"] for s in subjects]
        self._counts = bank_counts or (lambda: {})
        self._cache, self._lock = {}, threading.Lock()

    # ---- public ----
    def slugs(self):
        return list(self._order)

    def course(self, slug):
        if slug not in self._apps:
            return None
        with self._lock:
            if slug not in self._cache:
                self._cache[slug] = self._read(slug)
        return self._cache[slug]

    def library(self):
        return [self.course(s) for s in self._order if s in self._apps]

    # ---- reading one dashboard ----
    def _read(self, slug):
        subj = self._subjects[slug]
        client = self._apps[slug].test_client()
        hdr = {"X-Hub-Index": "1"}
        home = client.get("/", headers=hdr).get_data(as_text=True)
        pattern = re.compile(subj["note_pattern"])
        paths = sorted({h for h in re.findall(r'href="([^"#?]+)', home) if pattern.fullmatch(h)}, key=_natural)
        modules = []
        for n, path in enumerate(paths, 1):
            resp = client.get(path, headers=hdr)
            if resp.status_code != 200 or "html" not in resp.mimetype:
                continue
            modules.append(self._module(slug, n, path, resp.get_data(as_text=True)))
        sections = sum(len(m["topics"]) for m in modules)
        words = sum(m["words"] for m in modules)
        return {
            "slug": slug, "code": subj["code"], "title": subj["title"], "blurb": subj["blurb"], "accent": subj["accent"],
            "unit": subj.get("unit", "modules"), "url": f"/{slug}/",
            "quiz_url": f"/{slug}/quiz", "questions": self._counts().get(slug, 0),
            "practice": subj.get("practice", "questions"),
            "stats": {"modules": len(modules), "sections": sections,
                      "subsections": sum(len(t["subtopics"]) for m in modules for t in m["topics"]),
                      "words": words, "minutes": max(1, round(words / WPM))},
            "modules": modules,
        }

    def _module(self, slug, n, path, html):
        p = _Outline()
        p.feed(html)
        p.close()
        items = p.items
        # a heading that shows up many times on a page is a box label ("Worked Example"), not a section
        freq = {}
        for it in items:
            freq[it["title"].lower()] = freq.get(it["title"].lower(), 0) + 1
        items = [it for it in items if len(it["title"]) > 2 and freq[it["title"].lower()] < 4]
        for it in items:
            it["text"] = _clean(" ".join(it["text"]))
            it["words"] = len(it["text"].split())
        top = min((it["level"] for it in items), default=2)
        topics, cur = [], None
        for it in items:
            node = {"id": it["anchor"] or f"s{len(topics) + 1}", "title": it["title"], "summary": _first_sentence(it["text"]),
                    "url": f"/{slug}{path}" + (f"#{it['anchor']}" if it["anchor"] else ""), "words": it["words"],
                    "minutes": max(1, round(it["words"] / WPM)), "subtopics": []}
            if it["level"] <= top or cur is None:
                topics.append(node)
                cur = node
            else:
                cur["subtopics"].append(node)
                cur["words"] += node["words"]
                cur["minutes"] = max(1, round(cur["words"] / WPM))
        words = sum(t["words"] for t in topics) or len(_clean(re.sub(r"<[^>]+>", " ", html)).split())
        title = p.page_title or f"Part {n}"
        intro = _first_sentence(_clean(" ".join(getattr(p, "intro", []))), 200)
        return {"id": f"m{n}", "title": title, "url": f"/{slug}{path}", "summary": intro or (topics[0]["summary"] if topics else ""),
                "words": words, "minutes": max(1, round(words / WPM)), "topics": topics}
