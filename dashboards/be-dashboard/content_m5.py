"""Module 5 is built from the user's own bio-inspired design notes (uploaded HTML),
converted to this site's box/heading styles. Expand later with the video transcripts."""
import os, re, html
from sections import *

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_base", "bio_inspired_design_notes.html")


def _convert(h):
    # box headers: <b class="t">Label</b> -> span.label ; 'fs' boxes become foreshadow notes
    h = re.sub(r'<div class="box fs"><b class="t">.*?</b>', '<div class="foreshadow">', h, flags=re.S)
    h = re.sub(r'<div class="box (def|why|mis|ex)"><b class="t">(.*?)</b>', r'<div class="box \1"><span class="label">\2</span>', h, flags=re.S)
    h = re.sub(r'<h3>(.*?)</h3>', r'<h4 class="sub">\1</h4>', h, flags=re.S)
    return h


def load():
    s = open(SRC, encoding="utf-8").read()
    body = s[s.index("<body"):]
    parts = re.split(r'(?=<h2[ >])', body)
    intro, secs, check = "", [], []
    for p in parts:
        m = re.match(r'<h2(?: id="s(\d)")?>(.*?)</h2>', p, re.S)
        if not m:
            continue
        title = re.sub(r"^\d+\.\s*", "", m.group(2)).strip()
        content = p[m.end():]
        content = re.split(r'</main>|<script', content)[0]
        if m.group(1) is None and title.startswith("Roadmap"):
            intro = _convert(content)
        elif m.group(1) is None:   # self-test checklist
            check = [html.unescape(x).replace("☐", "").strip() for x in re.findall(r"<li>(.*?)</li>", content, re.S)]
        else:
            secs.append((int(m.group(1)), title, _convert(content)))
    out = []
    for n, title, content in secs:
        summ = {1: "Definition, what does and does not count, Rawling's spectrum (biomimetics–biomimicry–bionics), history and the four primitive design forms.",
                2: "Animal and plant examples: kingfisher beak, boxfish, tadpole, snake, ear bones, beehive, burdock (Velcro) and skin (self-healing).",
                3: "How termite mounds ventilate, the stack-effect pressure Δp = gh(ρout − ρin), and how green buildings copy it.",
                4: "Reading an insect as a design: head, antenna, wings, abdomen; flapping-wing physics and the Reynolds number.",
                5: "Insect intelligence, swarms, soft robots and micro-robots.",
                6: "Biological neuron to artificial neuron; activation functions, network shapes and training.",
                7: "Summary tables for revision."}.get(n, "")
        out.append(sec(f"i{n}", f"I{n}. {title}", summ, [], f'<div class="bio">{content}</div>'))
    return intro, out, check


INTRO, SECTIONS, CHECKLIST = load()
NOTE = M("These notes are the ones you prepared from the Module 5 videos, restyled to match the rest of the site. When you send the full transcripts I will expand each section.", "Status")
