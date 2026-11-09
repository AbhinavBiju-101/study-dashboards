"""Builds all five module pages (Flask templates), standalone downloads, the combined
all_modules.html, data/syllabus.json and the PDF.   Run:  python build_modules.py [--pdf]"""
import json, os, re, sys, shutil
from sections import *
import expand_data1, expand_data2
import content_m1x, content_m2, content_m3, content_m4, content_m5

HERE = os.path.dirname(os.path.abspath(__file__))
BASE, TPL, NOTES, DATA = (os.path.join(HERE, d) for d in ("_base", "templates", "notes", "data"))
for d in (NOTES, DATA):
    os.makedirs(d, exist_ok=True)
bio_src = "/mnt/user-data/uploads/bio_inspired_design_notes.html"
if not os.path.exists(os.path.join(BASE, "bio_inspired_design_notes.html")) and os.path.exists(bio_src):
    shutil.copy(bio_src, os.path.join(BASE, "bio_inspired_design_notes.html"))

old = json.load(open(os.path.join(BASE, "old_topics.json"), encoding="utf-8"))
OLD = {t["id"]: t for k in old for t in old[k]["topics"]}
circ = open(os.path.join(BASE, "m1_circuits.html"), encoding="utf-8").read()
mach = open(os.path.join(BASE, "m1_machines.html"), encoding="utf-8").read()
STYLE = re.search(r"<style>.*?</style>", circ, re.S).group(0)
EXTRA_CSS = """
<style>
  .bio .s{stroke:#333;fill:none;stroke-width:1.5}.bio .a{fill:#e8f0fc}.bio .b{fill:#e6f4ec}.bio .c{fill:#fdf0e3}.bio .d{fill:#f3ecfb}
  .bio svg text{font:12.5px sans-serif;fill:#1d2330}.bio figure{margin:16px 0;text-align:center}.bio figcaption,.bio .note{color:#5b6475;font-size:.92rem}
  .bio table{display:block;overflow-x:auto}.bio .box .t{font-weight:700}
  .cover{text-align:center;padding:90px 20px}.cover h1{font-size:2.4rem;margin:0 0 10px}.module{margin-top:30px}
  @media print{
    body{background:#fff}.backtop,nav.site-nav{display:none!important}.wrap{max-width:none;padding:0}
    header.hero{box-shadow:none;border-radius:0!important;margin:0!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
    .module{break-before:page}h2.part{break-before:page}h2.part:first-of-type{break-before:auto}
    .box,.diagram,table,tr,.foreshadow,h3.topic,h4.sub{break-inside:avoid}h3.topic{break-after:avoid}
    *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
    nav.toc{box-shadow:none;margin:12px 0}
  }
</style>
"""

PREFIX = lambda i: i[0].upper() + i[1:] + ". "
def cut(s, a, b):
    i = s.index(a)
    return s[i:s.index(b, i)] if b else s[i:]

circuits_body = cut(circ, '<h2 class="part" id="parta">', '<h2 class="part" id="glossary">')
machines_body = cut(mach, '<h2 class="part" id="partc">', '<h2 class="part" id="glossary">')
mach_checks = re.findall(r"<li>(.*?)</li>", cut(mach, '<ul class="checklist">', "</ul>"), re.S)
MARKS = {"parta": "Circuits", "partb": "Circuits", "partc": "Machines"}
for k, v in MARKS.items():
    circuits_body = re.sub(rf'(<h2 class="part" id="{k}">[^<]*)<span class="marks">[^<]*</span>', rf'\1<span class="marks">{v}</span>', circuits_body)
    machines_body = re.sub(rf'(<h2 class="part" id="{k}">[^<]*)<span class="marks">[^<]*</span>', rf'\1<span class="marks">{v}</span>', machines_body)
circuits_body = circuits_body.replace("Topic 2 (Electrical Machines)", "Part C (Electrical Machines)")

X = {s["id"]: s for s in content_m1x.SECTIONS}
part = lambda i, t, m: f'\n<h2 class="part" id="{i}">{t} <span class="marks">{m}</span></h2>\n'

# ------------------------------------------------------------------ module definitions
MODS = []
m1_secs = [x for x in X.values()]
m1_body = (circuits_body + render_section(X["b6"]) + machines_body + "".join(render_section(X[i]) for i in ("c7", "c8", "c9", "c10"))
           + part("partd", "Part D — Power Electronics &amp; Electric Drives", "concepts") + "".join(render_section(X[i]) for i in ("d1", "d2"))
           + part("parte", "Part E — Electrical Safety &amp; Earthing", "safety") + "".join(render_section(X[i]) for i in ("e1", "e2")))
m1_toc = [(i, PREFIX(i) + OLD[i]["label"], OLD[i]["summary"]) for i in
          ("a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "b1", "b2", "b3", "b4", "b5")] + [("b6", X["b6"]["title"], X["b6"]["summary"])] \
         + [(i, PREFIX(i) + OLD[i]["label"], OLD[i]["summary"]) for i in ("c1", "c2", "c3", "c4", "c5", "c6")] \
         + [(i, X[i]["title"], X[i]["summary"]) for i in ("c7", "c8", "c9", "c10", "d1", "d2", "e1", "e2")]
m1_terms = list(expand_data1.TERMS1.values()) + list(expand_data2.TERMS2.values()) + [X[i]["terms"] for i in X]
m1_checks = mach_checks + ["Explain why a single-phase induction motor is not self-starting and compare the five starting methods.", "Describe a BLDC motor's six-step commutation and a stepper motor's step angle/speed relations.",
                           "State how an alternator differs from a DC generator and compute its speed for a given frequency.", "Describe the four converter families, PWM and why switching converters are efficient.", "Explain V/f control in a VFD and the fan-law energy saving.",
                           "Explain the principle of earthing and why the earth wire protects a person; list the effects of current levels and the five preventive measures.", "Compute the energy used and cost for a set of appliances."]
MODS.append(dict(num=1, title="Principles of Electrical Engineering: Circuits &amp; Power Conversion", short="Circuits & Power Conversion",
                 desc="DC and AC circuits, network theorems, AC power, electrical machines (DC, induction, BLDC, stepper, transformer, alternator), power electronics, drives, and electrical safety & earthing.",
                 accent="#3949ab", dk="#1e2a4a", body=m1_body, toc=m1_toc, terms=m1_terms, checks=m1_checks, intro=""))

def simple(num, title, short, desc, accent, dk, mod, intro=""):
    S = mod.SECTIONS
    body = "".join(render_section(s) if s["terms"] else f'\n<h3 class="topic" id="{s["id"]}">{s["title"]}</h3>' + s["body"] for s in S)
    return dict(num=num, title=title, short=short, desc=desc, accent=accent, dk=dk, body=body, toc=[(s["id"], s["title"], s["summary"]) for s in S],
                terms=[s["terms"] for s in S if s["terms"]], checks=mod.CHECKLIST, intro=intro)

MODS.append(simple(2, "Foundations of Electronics &amp; Communication Systems", "Electronics & Communication", "PN, Zener, BJT and MOSFET; rectifiers and voltage regulators; op-amps; the EM spectrum; communication systems, cellular, satellite and radar.", "#0f766e", "#134e4a", content_m2))
MODS.append(simple(3, "Engineering Graphics &amp; CAD", "Engineering Graphics & CAD", "BIS standards, orthographic projection (first/third angle), projection of solids, isometric and perspective, freehand sketching, building drawing, CAD — plus the CAT-1 question patterns.", "#b45309", "#78350f", content_m3))
MODS.append(simple(4, "Manufacturing, Energy Conversion &amp; Mechanical Automation", "Manufacturing & Automation", "Casting, forming, joining, machining, CNC and 3-D printing; IC engines, power plants, refrigeration, fuel cells; mechanisms, mechanical components, robotics and pneumatic/hydraulic actuators.", "#be123c", "#881337", content_m4))
m5 = simple(5, "Bio-Inspired Design in Engineering", "Bio-Inspired Design", "Biomimicry and its core ideas, case studies (Velcro, self-healing, termite-mound ventilation, insect-inspired drones and soft robots, neural networks).", "#15803d", "#14532d", content_m5,
            intro=content_m5.NOTE + content_m5.INTRO)
m5["body"] = m5["intro"] + m5["body"]
MODS.append(m5)

# ------------------------------------------------------------------ page assembly
def module_content(m, combined=False):
    sfx = f"-{m['num']}" if combined else ""
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t, _ in m["toc"])
    if m["terms"]:
        toc += f'<li><a href="#glossary{sfx}">Glossary (A–Z)</a></li>'
    toc += f'<li><a href="#selftest{sfx}">Self-test checklist</a></li>'
    gl = glossary_html(m["terms"]) if m["terms"] else ""
    out = (f'<header class="hero" style="border-radius:12px;margin-top:24px;"><h1>Module {m["num"]} — {m["title"]}</h1><p>{m["desc"]}</p></header>'
           f'<nav class="toc"><h2>Subtopics in this module</h2><ol>{toc}</ol></nav>' + m["body"] + gl + checklist_html(m["checks"]))
    if combined:
        out = out.replace('id="glossary"', f'id="glossary{sfx}"').replace('id="selftest"', f'id="selftest{sfx}"')
    return out

def raw(s):
    return "{% raw %}" + s + "{% endraw %}"

for m in MODS:
    n = m["num"]
    page = ('{% extends "base.html" %}\n{% block title %}Basic Engineering — Module ' + str(n) + '{% endblock %}\n{% block extra_style %}\n' + STYLE + EXTRA_CSS + '{% endblock %}\n{% block content %}\n'
            '<div class="wrap">\n' + raw(module_content(m)) + '\n</div>\n<a href="#top" class="backtop">↑</a>\n{% endblock %}\n')
    open(os.path.join(TPL, f"topic{n}.html"), "w", encoding="utf-8").write(page)
    stand = (f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Basic Engineering — Module {n}</title>{STYLE}{EXTRA_CSS}</head>'
             f'<body><div class="wrap">{module_content(m)}</div></body></html>')
    open(os.path.join(NOTES, f"topic{n}.html"), "w", encoding="utf-8").write(stand)

cover = ('<div class="cover"><h1>Basic Engineering — Illustrated Notes</h1><p style="font-size:1.1rem;color:#4a5568">BAEEE101 · all five modules</p><ol style="display:inline-block;text-align:left;font-size:1.05rem;line-height:1.9">'
         + "".join(f'<li><a href="#module-{m["num"]}">Module {m["num"]} — {m["short"]}</a></li>' for m in MODS) + '</ol></div>')
combined = (f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Basic Engineering — Illustrated Notes (all modules)</title>{STYLE}{EXTRA_CSS}</head><body><div class="wrap">{cover}'
            + "".join(f'<section class="module" id="module-{m["num"]}">{module_content(m, True)}</section>' for m in MODS) + "</div></body></html>")
open(os.path.join(NOTES, "all_modules.html"), "w", encoding="utf-8").write(combined)

# ------------------------------------------------------------------ syllabus data for the dashboard
syl = {"modules": [dict(num=m["num"], title=re.sub(r"&amp;", "&", m["title"]), desc=m["desc"], accent=m["accent"], accent_dk=m["dk"], download_file=f"topic{m['num']}.html",
                         topics=[dict(id=i, label=re.sub(r"&amp;", "&", re.sub(r"^[A-Z]\d+\.\s*", "", t)), summary=re.sub(r"&amp;", "&", sm), subtopics=[]) for i, t, sm in m["toc"]]) for m in MODS]}
json.dump(syl, open(os.path.join(DATA, "syllabus.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("modules:", [(m["num"], len(m["toc"])) for m in MODS], "| combined bytes:", len(combined))

if "--pdf" in sys.argv:
    from playwright.sync_api import sync_playwright
    out = os.path.join(HERE, "Basic_Engineering_Illustrated_Notes.pdf")
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        pg.goto("file://" + os.path.join(NOTES, "all_modules.html"))
        pg.wait_for_timeout(1500)
        pg.pdf(path=out, format="A4", print_background=True, margin={"top": "14mm", "bottom": "16mm", "left": "12mm", "right": "12mm"}, display_header_footer=True,
               header_template="<span></span>", footer_template='<div style="font-size:8px;width:100%;text-align:center;color:#666">BAEEE101 Basic Engineering — <span class="pageNumber"></span> / <span class="totalPages"></span></div>')
        br.close()
    print("pdf:", os.path.getsize(out) // 1024, "KB")
