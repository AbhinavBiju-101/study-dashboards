"""Applies Key-terms boxes, extra teaching content, diagrams and an A-Z glossary to the
topic templates, then regenerates the standalone notes/ copies.

Always starts from the pristine originals in _orig/ so it can be re-run safely.
"""
import math, os, re, shutil
from expand_data1 import TERMS1, EXTRA1
from expand_data2 import TERMS2, EXTRA2

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "templates")
ORIG = os.path.join(HERE, "_orig")
NOTES = os.path.join(HERE, "notes")

os.makedirs(ORIG, exist_ok=True)
for n in ("topic1.html", "topic2.html"):
    src = os.path.join(ORIG, n)
    if not os.path.exists(src):
        shutil.copy(os.path.join(TPL, n), src)

EXTRA_CSS = """
  .terms{background:#fff9e6;border-color:#f0dfa0;}
  .terms .label{color:#8a6d00;}
  .terms ul{list-style:none;margin:0;padding:0;}
  .terms li{padding:5px 0;border-bottom:1px dotted #ecdca2;font-size:.94rem;}
  .terms li:last-child{border-bottom:none;}
  .terms li b{color:#5c4700;}
  ol,ul{padding-left:22px;}
  .gloss td:first-child{font-weight:600;white-space:nowrap;vertical-align:top;}
"""

# ---------- diagrams ----------
def path(points):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in points)

def resonance_svg():
    Q = 4.0
    pts = []
    for i in range(0, 121):
        x = 0.4 + i * 0.01
        val = 1 / math.sqrt(1 + Q * Q * (x - 1 / x) ** 2)
        px = 50 + (x - 0.4) / 1.2 * 340
        py = 170 - val * 130
        pts.append((px, py))
    f0x = 50 + (1.0 - 0.4) / 1.2 * 340
    return f'''<div class="diagram">
<svg viewBox="0 0 430 210" xmlns="http://www.w3.org/2000/svg">
  <line x1="50" y1="170" x2="400" y2="170" stroke="#1b1f24"/><line x1="50" y1="170" x2="50" y2="20" stroke="#1b1f24"/>
  <path d="{path(pts)}" fill="none" stroke="#7c3aed" stroke-width="2.5"/>
  <line x1="{f0x:.1f}" y1="170" x2="{f0x:.1f}" y2="40" stroke="#c0392b" stroke-dasharray="4,3"/>
  <text x="{f0x:.1f}" y="188" font-size="12" text-anchor="middle" fill="#c0392b">f₀ = 1/(2π√LC)</text>
  <text x="{f0x+6:.1f}" y="36" font-size="12" fill="#c0392b">I_max = V/R (Z = R)</text>
  <text x="120" y="120" font-size="12" fill="#1e468c">capacitive</text><text x="120" y="134" font-size="11" fill="#1e468c">(I leads V)</text>
  <text x="320" y="120" font-size="12" fill="#166e3c">inductive</text><text x="320" y="134" font-size="11" fill="#166e3c">(I lags V)</text>
  <text x="225" y="205" font-size="12" text-anchor="middle">frequency f →</text>
  <text x="14" y="100" font-size="12" transform="rotate(-90 14 100)">current I</text>
</svg>
<p class="caption">Current in a series RLC circuit versus frequency: a sharp peak at resonance where X<sub>L</sub> = X<sub>C</sub>; the higher the Q, the narrower the peak.</p>
</div>'''

def generator_svg():
    w, x0, ymid, amp = 390, 30, 100, 60
    ac, dc = [], []
    for i in range(0, 401):
        t = i / 400 * 2  # two cycles
        x = x0 + t / 2 * w
        s = math.sin(2 * math.pi * t)
        ac.append((x, ymid - amp * s))
        dc.append((x, ymid - amp * abs(s)))
    return f'''<div class="diagram">
<svg viewBox="0 0 440 200" xmlns="http://www.w3.org/2000/svg">
  <line x1="30" y1="100" x2="425" y2="100" stroke="#1b1f24"/><line x1="30" y1="25" x2="30" y2="175" stroke="#1b1f24"/>
  <path d="{path(ac)}" fill="none" stroke="#9aa3b2" stroke-width="2" stroke-dasharray="5,3"/>
  <path d="{path(dc)}" fill="none" stroke="#7c3aed" stroke-width="2.6"/>
  <text x="330" y="22" font-size="12" fill="#9aa3b2">- - EMF in the loop (AC)</text>
  <text x="330" y="38" font-size="12" fill="#7c3aed">—— at the brushes (after commutator)</text>
  <text x="225" y="192" font-size="12" text-anchor="middle">time (two revolutions of the loop) →</text>
</svg>
<p class="caption">A single-loop generator. The loop's EMF alternates every half-turn; the commutator swaps the connections at each zero crossing so the load sees a one-directional, pulsating output.</p>
</div>'''

def threephase_svg():
    w, x0, ymid, amp = 340, 40, 100, 60
    cols = [("Phase A", "#c0392b", 0), ("Phase B", "#d4a017", 120), ("Phase C", "#1e468c", 240)]
    body = ""
    for name, col, lag in cols:
        pts = []
        for i in range(0, 361):
            x = x0 + i / 360 * w
            y = ymid - amp * math.sin(math.radians(i - lag))
            pts.append((x, y))
        body += f'<path d="{path(pts)}" fill="none" stroke="{col}" stroke-width="2.4"/>'
    ticks = ""
    for ang in (0, 90, 180, 270, 360):
        x = x0 + ang / 360 * w
        ticks += f'<line x1="{x:.1f}" y1="97" x2="{x:.1f}" y2="103" stroke="#1b1f24"/><text x="{x:.1f}" y="116" font-size="10" text-anchor="middle">{ang}°</text>'
    return f'''<div class="diagram">
<svg viewBox="0 0 470 200" xmlns="http://www.w3.org/2000/svg">
  <line x1="40" y1="100" x2="395" y2="100" stroke="#1b1f24"/><line x1="40" y1="30" x2="40" y2="170" stroke="#1b1f24"/>
  {body}{ticks}
  <text x="405" y="60" font-size="12" fill="#c0392b">Phase A</text>
  <text x="405" y="80" font-size="12" fill="#d4a017">Phase B (lags 120°)</text>
  <text x="405" y="100" font-size="12" fill="#1e468c">Phase C (lags 240°)</text>
  <text x="217" y="192" font-size="12" text-anchor="middle">ωt →</text>
</svg>
<p class="caption">Three balanced currents 120° apart. At any instant they sum to zero, and fed into three windings placed 120° apart in space they create the rotating field.</p>
</div>'''

import diagrams as D
SVGS = {"@@RESONANCE_SVG@@": D.d_resonance(), "@@GENERATOR_SVG@@": D.d_generator(), "@@THREEPHASE_SVG@@": D.d_threephase()}

# ---------- helpers ----------
def terms_box(items):
    lis = "\n".join(f"<li><b>{t}</b> — {d}</li>" for t, d in items)
    return f'\n<div class="box terms"><span class="label">Key terms — know these words</span>\n<ul>\n{lis}\n</ul>\n</div>\n'

def strip_tags(s):
    return re.sub(r"<.*?>", "", s).lower()

def glossary_html(terms_dict):
    seen, rows = set(), []
    for items in terms_dict.values():
        for t, d in items:
            k = strip_tags(t)
            if k in seen:
                continue
            seen.add(k)
            rows.append((k, t, d))
    rows.sort()
    body = "\n".join(f"<tr><td>{t}</td><td>{d}</td></tr>" for _, t, d in rows)
    return f'''
<h2 class="part" id="glossary">Glossary (A–Z) <span class="marks">{len(rows)} terms</span></h2>
<p>Every key term from the boxes above in one alphabetical list — skim this the night before the exam.</p>
<table class="gloss">
<tr><th>Term</th><th>Meaning</th></tr>
{body}
</table>
'''

ORDER = {
    "topic1.html": D.TOPIC1[:13] + [D.d_resonance] + D.TOPIC1[13:],
    "topic2.html": [D.TOPIC2[0], D.TOPIC2[1], D.d_generator, D.TOPIC2[2], D.TOPIC2[3], D.TOPIC2[4], D.d_threephase],
}


def apply(name, terms, extra, tail_marker, glossary_before, extra_checklist=None):
    s = open(os.path.join(ORIG, name), encoding="utf-8").read()
    # css
    s = s.replace("</style>", EXTRA_CSS + "</style>", 1)
    # extras first (so the heading anchors are still simple), then terms
    for sid, html in extra.items():
        for k, v in SVGS.items():
            html = html.replace(k, v)
        m = re.search(rf'<h3 class="topic" id="{sid}">', s)
        assert m, f"missing section {sid}"
        rest = s[m.end():]
        nxt = re.search(r'<h3 class="topic"|<h2 class="part"|' + re.escape(tail_marker), rest)
        assert nxt, f"no end for {sid}"
        pos = m.end() + nxt.start()
        s = s[:pos] + html + "\n" + s[pos:]
    for sid, items in terms.items():
        m = re.search(rf'(<h3 class="topic" id="{sid}">.*?</h3>)', s)
        assert m, f"missing heading {sid}"
        s = s[:m.end()] + terms_box(items) + s[m.end():]
    # glossary
    g = glossary_html(terms)
    idx = s.index(glossary_before)
    s = s[:idx] + g + "\n" + s[idx:]
    # toc entry
    if 'id="selftest"' in s and '<li><a href="#selftest">' in s:
        s = s.replace('<li><a href="#selftest">', '<li><a href="#glossary">Glossary (A–Z)</a></li>\n  <li><a href="#selftest">', 1)
    else:
        s = s.replace("</ol>\n</nav>", '  <li><a href="#glossary">Glossary (A–Z)</a></li>\n</ol>\n</nav>', 1)
    if extra_checklist:
        i = s.index('<ul class="checklist">')
        j = s.index("</ul>", i)
        s = s[:j] + extra_checklist + s[j:]
    # replace every diagram (base + inserted) with the redrawn versions, in page order
    order = ORDER[name]
    blocks = list(re.finditer(r'<div class="diagram">.*?</div>', s, re.S))
    assert len(blocks) == len(order), (name, len(blocks), len(order))
    for m, fn in reversed(list(zip(blocks, order))):
        s = s[:m.start()] + fn() + s[m.end():]
    open(os.path.join(TPL, name), "w", encoding="utf-8").write(s)
    return s

t1 = apply("topic1.html", TERMS1, EXTRA1,
           tail_marker='</div>\n<a href="#top"',
           glossary_before='</div>\n<a href="#top"')

extra_ck = """  <li>Name every part of a DC machine and say what each does, including why the iron is laminated.</li>
  <li>Explain how the same armature works as a motor and as a generator, and why the commutator is needed in both.</li>
  <li>Write the supply/terminal-voltage equation for shunt, series, and short/long-shunt compound machines.</li>
  <li>State the working principle of a transformer in your own words and explain why it fails on DC.</li>
  <li>Explain why a wound-rotor induction motor starts better than a squirrel-cage one, and what it costs.</li>
"""
t2 = apply("topic2.html", TERMS2, EXTRA2,
           tail_marker='<h2 class="part" id="selftest">',
           glossary_before='<h2 class="part" id="selftest">',
           extra_checklist=extra_ck)

# ---------- standalone notes/ copies ----------
def standalone(tpl_text, title):
    style = re.search(r"<style>.*?</style>", tpl_text, re.S).group(0)
    body = tpl_text.split("{% block content %}", 1)[1].rsplit("{% endblock %}", 1)[0]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{style}
</head>
<body>
{body}
</body>
</html>
'''

open(os.path.join(NOTES, "topic1.html"), "w", encoding="utf-8").write(standalone(t1, "Basic Engineering — Topic 1: DC &amp; AC Circuits"))
open(os.path.join(NOTES, "topic2.html"), "w", encoding="utf-8").write(standalone(t2, "Basic Engineering — Topic 2: Electrical Machines"))
print("expanded:", len(t1.splitlines()), "and", len(t2.splitlines()), "lines")
