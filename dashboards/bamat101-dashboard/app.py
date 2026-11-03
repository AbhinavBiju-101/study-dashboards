"""BAMAT101 Notes Dashboard: syllabus tree, embedded PDF reader, figures and a self-graded practice quiz.
Run: pip install -r requirements.txt && python app.py  ->  http://127.0.0.1:4003
Routes: /  dashboard | /module/<1-6> notes | /read/<notes|bank>?page=N PDF reader | /pdf/<which> | /download/<which>
        /quiz setup | POST /quiz/start"""
import json
import random
import re
from pathlib import Path
from flask import Flask, abort, flash, redirect, render_template, request, send_from_directory, url_for
from markupsafe import Markup

app = Flask(__name__)
app.secret_key = "bamat101-local-dev-key"
BASE = Path(__file__).resolve().parent
PDFS = {"notes": "BAMAT101_Illustrated_Lesson_Notes_Complete.pdf", "bank": "BAMAT101_Practice_Problem_Bank.pdf"}
PDF_TITLES = {"notes": "Illustrated Lesson Notes", "bank": "Practice Problem Bank"}
LEVELS = ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"]


def _load(name, default):
    p = BASE / "data" / name
    return json.loads(p.read_text("utf-8")) if p.exists() else default


SYL = _load("syllabus.json", {"modules": []})
MODS = {m["num"]: m for m in SYL["modules"]}
TOTAL = len(MODS)
FIGS = json.loads((BASE / "static" / "figures" / "manifest.json").read_text("utf-8"))
TOPICS = _load("problems.json", [])   # [{prefix, module, title, problems:[{id, level, q, a, q_page, a_page}]}]


def _enrich():
    """Merge optional per-module trees (data/tree_*.json, written by the notes conversion) into the syllabus."""
    for f in sorted((BASE / "data").glob("tree_*.json")):
        for t in json.loads(f.read_text("utf-8")).get("topics", []):
            for m in MODS.values():
                for s in m["topics"]:
                    if s["id"] == t["id"]:
                        s["summary"] = t.get("summary", s["summary"]); s["subtopics"] = t.get("subtopics", [])
_enrich()


def _fragment(m):
    """Converted notes HTML for a module, if present (not run through Jinja; maths stays as LaTeX for KaTeX)."""
    parts = [(BASE / "notes_html" / f"{k}.html") for k in m["files"]]
    if not all(p.exists() for p in parts):
        return None
    html = "\n".join(p.read_text("utf-8") for p in parts)
    html = html.replace("@static/", url_for("static", filename=""))
    html = re.sub(r"@pdf/(notes|bank)/(\d+)", lambda x: url_for("read", which=x.group(1), page=int(x.group(2))), html)
    return Markup(html)


@app.route("/")
def dashboard():
    n_problems = sum(len(t["problems"]) for t in TOPICS)
    return render_template("dashboard.html", mods=[MODS[n] for n in sorted(MODS)], total=TOTAL, n_problems=n_problems)


@app.route("/module/<int:num>")
def module(num):
    if num not in MODS:
        abort(404)
    m = MODS[num]
    lo, hi = m["pages"]
    figs = [f for f in FIGS if lo <= f["page"] <= hi]
    return render_template("module.html", m=m, current=num, total=TOTAL, accent=m["accent"], figs=figs, body=_fragment(m),
                           prev_num=num - 1 if num > 1 else None, next_num=num + 1 if num < TOTAL else None)


@app.route("/read/<which>")
def read(which):
    if which not in PDFS:
        abort(404)
    page = max(1, request.args.get("page", 1, type=int))
    return render_template("read.html", which=which, title=PDF_TITLES[which], page=page, accent="#b7791f",
                           src=url_for("pdf_inline", which=which) + f"#page={page}&view=FitH")


@app.route("/pdf/<which>")
def pdf_inline(which):
    if which not in PDFS:
        abort(404)
    return send_from_directory(BASE / "notes", PDFS[which], as_attachment=False)


@app.route("/download/<which>")
def download(which):
    if which not in PDFS:
        abort(404)
    return send_from_directory(BASE / "notes", PDFS[which], as_attachment=True)


def _picker():
    out = {}
    for t in TOPICS:
        out.setdefault(t["module"], []).append({"prefix": t["prefix"], "title": t["title"], "count": len(t["problems"])})
    return out


@app.route("/quiz")
def quiz_setup():
    picker = _picker()
    mods = [{"num": n, "title": MODS[n]["title"], "accent": MODS[n]["accent"], "topics": picker.get(n, []),
             "total": sum(t["count"] for t in picker.get(n, []))} for n in sorted(MODS) if n in picker]
    return render_template("quiz_setup.html", mods=mods, levels=LEVELS, grand_total=sum(m["total"] for m in mods))


@app.route("/quiz/start", methods=["POST"])
def quiz_start():
    chosen = set(request.form.getlist("topics"))
    levels = set(request.form.getlist("levels")) or set(LEVELS)
    order = request.form.get("order", "random")
    try:
        want = int(request.form.get("count", 10))
    except ValueError:
        want = 10
    pool = []
    for t in TOPICS:
        if t["prefix"] in chosen:
            for p in t["problems"]:
                if p["level"] in levels:
                    pool.append({**p, "prefix": t["prefix"], "module": t["module"], "topic": t["title"],
                                 "label": f"M{t['module']} · {t['title']}"})
    if not pool:
        flash("Pick at least one topic (and one level) before starting.")
        return redirect(url_for("quiz_setup"))
    want = max(1, min(want, len(pool)))
    picked = random.sample(pool, want)
    if order == "syllabus":
        index = {p["id"]: i for i, p in enumerate(pool)}
        picked.sort(key=lambda p: index[p["id"]])
    return render_template("quiz_run.html", problems=picked, pool_size=len(pool), requested=want, accent="#b7791f")


if __name__ == "__main__":
    app.run(debug=True, port=4003)
