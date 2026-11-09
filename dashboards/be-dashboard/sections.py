"""Tiny helpers so each module's content can be written compactly but rendered with the
same box styles (definition / why / misconception / example / foreshadow / terms)."""
import re


def _box(cls, label, t):
    return f'\n<div class="box {cls}"><span class="label">{label}</span>{t}</div>\n'


def D(t, label="Definition"): return _box("def", label, t)
def W(t, label="Why this is true"): return _box("why", label, t)
def M(t, label="Fixing a common misconception"): return _box("mis", label, t)
def E(t, label="Worked example"): return _box("ex", label, t)
def F(t): return f'\n<div class="foreshadow">{t}</div>\n'
def H(t): return f'\n<h4 class="sub">{t}</h4>\n'
def FM(t): return f'\n<div class="formula">{t}</div>\n'
def P(t): return f"\n<p>{t}</p>\n"


def UL(items): return "\n<ul>\n" + "\n".join(f"<li>{i}</li>" for i in items) + "\n</ul>\n"
def OL(items): return "\n<ol>\n" + "\n".join(f"<li>{i}</li>" for i in items) + "\n</ol>\n"


def T(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f"\n<table>\n<tr>{h}</tr>\n{r}\n</table>\n"


def terms_box(items):
    lis = "\n".join(f"<li><b>{t}</b> — {d}</li>" for t, d in items)
    return f'\n<div class="box terms"><span class="label">Key terms — know these words</span>\n<ul>\n{lis}\n</ul>\n</div>\n'


def sec(id, title, summary, terms, body):
    return {"id": id, "title": title, "summary": summary, "terms": terms, "body": body}


def render_section(s):
    return f'\n<h3 class="topic" id="{s["id"]}">{s["title"]}</h3>' + terms_box(s["terms"]) + s["body"]


def strip_tags(s):
    return re.sub(r"<.*?>", "", s).lower()


def glossary_html(term_lists):
    seen, rows = set(), []
    for items in term_lists:
        for t, d in items:
            k = strip_tags(t)
            if k in seen:
                continue
            seen.add(k)
            rows.append((k, t, d))
    rows.sort()
    body = "\n".join(f"<tr><td>{t}</td><td>{d}</td></tr>" for _, t, d in rows)
    return (f'\n<h2 class="part" id="glossary">Glossary (A–Z) <span class="marks">{len(rows)} terms</span></h2>\n'
            '<p>Every key term from the boxes above in one alphabetical list — skim this the night before the exam.</p>\n'
            f'<table class="gloss">\n<tr><th>Term</th><th>Meaning</th></tr>\n{body}\n</table>\n')


def checklist_html(items):
    lis = "\n".join(f"  <li>{i}</li>" for i in items)
    return ('\n<h2 class="part" id="selftest">Self-Test Checklist</h2>\n'
            '<p>Can you do each of these <em>right now</em>, without looking back? If not, that is the section to re-read.</p>\n'
            f'<ul class="checklist">\n{lis}\n</ul>\n')
