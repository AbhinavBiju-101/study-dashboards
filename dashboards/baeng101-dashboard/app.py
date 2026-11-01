"""BAENG101 Modules 3 & 4: Flask dashboard, illustrated notes and quiz.
Run: pip install -r requirements.txt && python app.py  ->  http://127.0.0.1:4002
Routes: /  dashboard | /module/<3|4> notes | /quiz setup | POST /quiz/start"""
import json, os, random
from flask import Flask, abort, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = "baeng101-local-dev-key"
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
MODS = json.load(open(os.path.join(D, "syllabus.json"), encoding="utf-8"))
BANK = json.load(open(os.path.join(D, "quiz_bank.json"), encoding="utf-8"))
LEVELS = ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"]
PAGES = {m["num"]: m for m in MODS if m["page"]}

@app.route("/")
def dashboard():
    total = sum(len(b["questions"]) for b in BANK.values())
    return render_template("dashboard.html", mods=MODS, total_q=total, total_s=len(BANK))

@app.route("/module/<int:num>")
def module(num):
    if num not in PAGES: abort(404)
    m = PAGES[num]
    return render_template(f"module{num}.html", accent=m["accent"], accent_dk=m["accent_dk"], current=num,
                           prev_num=num - 1 if num - 1 in PAGES else None, next_num=num + 1 if num + 1 in PAGES else None)

@app.route("/quiz")
def quiz_setup():
    picks = set(request.args.getlist("pick"))
    for m in MODS:
        m["total"] = sum(s["count"] for t in m["topics"] for s in t["subtopics"])
        for t in m["topics"]:
            for s in t["subtopics"]:
                lv = {l: 0 for l in LEVELS}
                for q in BANK[s["id"]]["questions"]: lv[q["level"]] = lv.get(q["level"], 0) + 1
                s["lv"] = lv
    return render_template("quiz_setup.html", mods=MODS, levels=LEVELS, picks=picks,
                           grand_total=sum(m["total"] for m in MODS))

@app.route("/quiz/start", methods=["POST"])
def quiz_start():
    subs = request.form.getlist("subs"); levels = set(request.form.getlist("levels")) or set(LEVELS)
    back = request.form.get("backtracking") == "on"
    try: want = int(request.form.get("count", 10))
    except ValueError: want = 10
    pool = [dict(sid=sid, **q, module=BANK[sid]["module"], topic=BANK[sid]["topic"], sub=BANK[sid]["label"])
            for sid in subs if sid in BANK for q in BANK[sid]["questions"] if q["level"] in levels]
    if not pool:
        flash("Pick at least one subtopic (and one level) before starting the quiz.")
        return redirect(url_for("quiz_setup"))
    chosen = random.sample(pool, max(1, min(want, len(pool))))
    out = []
    for q in chosen:  # shuffle options per attempt and remap the answer index
        order = random.sample(range(len(q["options"])), len(q["options"]))
        out.append({"sid": q["sid"], "module": q["module"], "topic": q["topic"], "sub": q["sub"], "level": q["level"],
                    "q": q["q"], "options": [q["options"][i] for i in order], "answer": order.index(q["answer"])})
    return render_template("quiz_run.html", questions=out, pool_size=len(pool), requested=want, backtracking=back)

if __name__ == "__main__":
    app.run(debug=True, port=4002)
