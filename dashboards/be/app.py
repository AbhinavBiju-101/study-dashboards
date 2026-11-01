"""
Basic Engineering Notes Dashboard
---------------------------------
Multi-page Flask site for the illustrated Circuits & Machines notebooks.

Routes:
  GET  /                  dashboard: full syllabus, expandable topic -> subtopic tree
  GET  /topic/<int:num>   a topic's notebook, with prev/next/back-to-dashboard nav
  GET  /download/<file>   original self-contained standalone HTML (offline copy)
  GET  /quiz               quiz setup: pick topics/subtopics + question count
  POST /quiz/start         run a freshly-shuffled quiz built from the selection

Run:
    pip install -r requirements.txt
    python app.py
    open http://127.0.0.1:4001
"""

import json
import os

import random
from flask import Flask, abort, flash, redirect, render_template, request, send_from_directory, url_for

app = Flask(__name__)
app.secret_key = "be-dashboard-local-dev-key"  # only used for flash messages; local tool, not public-facing

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_DIR = os.path.join(BASE_DIR, "notes")  # original standalone files, for download
DATA_DIR = os.path.join(BASE_DIR, "data")

# Quiz question bank: {"1": {"s1": {"label": ..., "questions": [...]}, ...}, "2": {...}}
# Each question: level (Bloom's Taxonomy), q (stem), options (4, bank order), answer (0-based index).
with open(os.path.join(DATA_DIR, "quiz_bank.json"), encoding="utf-8") as f:
    QUIZ_BANK = json.load(f)

# One entry per topic. `topics` here means "subtopics" in the dashboard's own language —
# kept as the key name "topics" purely so dashboard.html (adapted from a working template)
# doesn't need restructuring. Each subtopic has an id (anchor on the topic page), a label,
# a one-line summary, and an (empty, for this syllabus) list of finer subtopics.
TOPICS = {
    1: {
        "num": 1,
        "title": "DC & AC Circuits",
        "desc": "Ohm's Law, Kirchhoff's Laws, network theorems (node/mesh/Thevenin/Norton/superposition/max power), then AC fundamentals: RMS/phasors/impedance, series RL-RC-RLC, and power factor.",
        "accent": "#3949ab",
        "accent_dk": "#1e2a4a",
        "download_file": "topic1.html",
        "topics": [
            {"id": "a1", "label": "Ohm's Law & Circuit Elements", "summary": "V=IR links voltage, current and resistance for a single resistor — the atomic building block every other law in this topic is built from.", "subtopics": []},
            {"id": "a2", "label": "Kirchhoff's Laws (KCL, KVL)", "summary": "KCL: current into a node equals current out (conservation of charge). KVL: voltage rises equal drops around any closed loop (conservation of energy).", "subtopics": []},
            {"id": "a3", "label": "Series, Parallel & Dividers", "summary": "Series resistors share one current and simply add; parallel resistors share one voltage and add as reciprocals. The voltage- and current-divider shortcuts follow directly.", "subtopics": []},
            {"id": "a4", "label": "Node-Voltage Analysis", "summary": "Pick a reference node, assign unknown voltages to the rest, write one KCL equation per unknown node, and solve — best for circuits rich in parallel branches.", "subtopics": []},
            {"id": "a5", "label": "Mesh-Current Analysis", "summary": "Assign a circulating current to each loop and write one KVL equation per loop; a shared branch carries the difference of its two mesh currents.", "subtopics": []},
            {"id": "a6", "label": "Source Transformation", "summary": "A voltage source with series R is externally indistinguishable from a current source I=V/R with the same R in parallel — a useful circuit-simplifying swap.", "subtopics": []},
            {"id": "a7", "label": "Thevenin's & Norton's Theorem", "summary": "Any linear network, seen from two terminals, collapses to one source (V_th or I_N) plus one resistance (R_th) — found from the open-circuit voltage and the source-killed resistance.", "subtopics": []},
            {"id": "a8", "label": "Maximum Power Transfer Theorem", "summary": "A Thevenin source delivers maximum power to a load when R_L=R_th — derived by differentiating load power with respect to R_L and setting it to zero.", "subtopics": []},
            {"id": "a9", "label": "Superposition Theorem", "summary": "In a linear circuit with several independent sources, the total response is the sum of each source's individual contribution, with all other sources killed in turn.", "subtopics": []},
            {"id": "b1", "label": "Generating an AC Waveform", "summary": "A coil rotating at constant speed in a uniform field produces v(t)=V_m sin(ωt) — the rotating-coil picture behind every AC quantity that follows.", "subtopics": []},
            {"id": "b2", "label": "RMS, Average, Form Factor & Peak Factor", "summary": "RMS (V_m/√2) and half-cycle average (2V_m/π) are both derived by integration; their ratio gives the form factor, and V_m/V_rms gives the peak factor.", "subtopics": []},
            {"id": "b3", "label": "Phasors & Impedance", "summary": "A phasor freezes a sinusoid's magnitude and phase as a complex number; impedance Z=R+jX generalises resistance so KVL/KCL algebra keeps working unchanged for AC.", "subtopics": []},
            {"id": "b4", "label": "Series RL, RC, RLC Circuits", "summary": "Impedance triangles for RL (lagging), RC (leading) and RLC (either, or resonant when X_L=X_C) circuits, with |Z|, phase angle and current computed directly.", "subtopics": []},
            {"id": "b5", "label": "Power & Power Factor in AC Circuits", "summary": "Real power P=VIcosφ, reactive power Q=VIsinφ and apparent power S=VI form a right triangle (S²=P²+Q²); power factor cosφ=P/S governs how much current is needed for a given useful watt.", "subtopics": []},
        ],
    },
    2: {
        "num": 2,
        "title": "Electrical Machines",
        "desc": "DC motor construction, working principle and back-EMF, shunt/series/compound types, transformer construction and EMF equation, and the three-phase induction motor's rotating field.",
        "accent": "#7c3aed",
        "accent_dk": "#4b3480",
        "download_file": "topic2.html",
        "topics": [
            {"id": "c1", "label": "DC Motor: Construction", "summary": "Every part explained — yoke, poles and pole shoes, armature core/winding (lap vs wave), commutator, brushes — with material, purpose and why the iron is laminated.", "subtopics": []},
            {"id": "c2", "label": "DC Motor: Working Principle & Back EMF", "summary": "Fleming's Left-Hand Rule gives force direction (F=BIL); the moving conductor also generates a back-EMF (V=E_b+I_aR_a), which is why a starter is needed. Includes the DC generator principle (8 loop positions, commutation).", "subtopics": []},
            {"id": "c3", "label": "Types of DC Motors", "summary": "Separately excited, shunt, series and short/long-shunt compound — circuit equations, characteristics and applications — plus DC generator types and their uses.", "subtopics": []},
            {"id": "c4", "label": "Transformer: Construction", "summary": "Working principle (mutual induction), laminated core, core-type vs shell-type windings, ideal-transformer ratios, losses and applications.", "subtopics": []},
            {"id": "c5", "label": "Transformer: EMF Equation", "summary": "Faraday's law on a sinusoidal flux gives E=4.44fΦ_mN — the same √2 conversion from B2's RMS derivation reappears here as the constant 4.44.", "subtopics": []},
            {"id": "c6", "label": "Three-Phase Induction Motor", "summary": "Stator construction, why three phases make a rotating field (N_s=120f/P), slip, squirrel-cage vs wound rotor (full comparison table) and applications.", "subtopics": []},
        ],
    },
}
TOTAL_WEEKS = len(TOPICS)

_VALID_DOWNLOADS = {w["download_file"] for w in TOPICS.values()}


@app.route("/")
def dashboard():
    """Full syllabus: one card per topic, each expandable into subtopics."""
    weeks = [TOPICS[n] for n in sorted(TOPICS)]
    return render_template("dashboard.html", weeks=weeks, total=TOTAL_WEEKS)


@app.route("/topic/<int:num>")
def topic_page(num):
    """Render one topic's notebook inside the shared nav layout."""
    if num not in TOPICS:
        abort(404)
    w = TOPICS[num]
    return render_template(
        f"topic{num}.html",
        current=num,
        total=TOTAL_WEEKS,
        prev_num=num - 1 if num > 1 else None,
        next_num=num + 1 if num < TOTAL_WEEKS else None,
        accent=w["accent"],
    )


@app.route("/download/<path:filename>")
def download(filename):
    """Serve the original self-contained standalone HTML file for offline use."""
    if filename not in _VALID_DOWNLOADS:
        abort(404)
    return send_from_directory(NOTES_DIR, filename, as_attachment=True)


def _quiz_topic_picker():
    """Build {topic_num: [{id, label, count}, ...]} straight from the question bank,
    in subtopic order, for rendering the quiz setup page's checkboxes."""
    picker = {}
    for wnum_str in sorted(QUIZ_BANK, key=int):
        wnum = int(wnum_str)
        topics = []
        for tid in sorted(QUIZ_BANK[wnum_str], key=lambda t: int(t[1:])):
            entry = QUIZ_BANK[wnum_str][tid]
            topics.append({"id": tid, "label": entry["label"], "count": len(entry["questions"])})
        picker[wnum] = topics
    return picker


@app.route("/quiz")
def quiz_setup():
    """Quiz setup: pick topics/subtopics and how many questions, fully custom."""
    picker = _quiz_topic_picker()
    weeks = [
        {
            "num": n,
            "title": TOPICS[n]["title"],
            "accent": TOPICS[n]["accent"],
            "accent_dk": TOPICS[n]["accent_dk"],
            "topics": picker[n],
            "total_available": sum(t["count"] for t in picker[n]),
        }
        for n in sorted(TOPICS)
    ]
    grand_total = sum(w["total_available"] for w in weeks)
    return render_template("quiz_setup.html", weeks=weeks, grand_total=grand_total)


@app.route("/quiz/start", methods=["POST"])
def quiz_start():
    """Build a randomised, per-attempt-shuffled question set from the selected subtopics."""
    selected = request.form.getlist("topics")  # e.g. ["1:a1", "1:a7", "2:c6"]
    backtracking = request.form.get("backtracking") == "on"
    try:
        requested_count = int(request.form.get("count", 10))
    except ValueError:
        requested_count = 10

    pool = []
    for token in selected:
        if ":" not in token:
            continue
        wnum_str, tid = token.split(":", 1)
        if wnum_str not in QUIZ_BANK or tid not in QUIZ_BANK[wnum_str]:
            continue
        topic_label = QUIZ_BANK[wnum_str][tid]["label"]
        for i, q in enumerate(QUIZ_BANK[wnum_str][tid]["questions"]):
            pool.append({
                "key": f"{wnum_str}-{tid}-{i}",
                "week": int(wnum_str),
                "topic_id": tid,
                "topic_label": topic_label,
                "level": q["level"],
                "q": q["q"],
                "options": q["options"],
                "answer": q["answer"],
            })

    if not pool:
        flash("Pick at least one subtopic before starting the quiz.")
        return redirect(url_for("quiz_setup"))

    count = max(1, min(requested_count, len(pool)))
    chosen = random.sample(pool, count)

    # Per-attempt shuffle: randomise each question's option order (and remap the
    # correct index) so the same question never has a predictable answer position.
    quiz_questions = []
    for q in chosen:
        order = list(range(len(q["options"])))
        random.shuffle(order)
        shuffled_options = [q["options"][i] for i in order]
        new_answer = order.index(q["answer"])
        quiz_questions.append({
            "key": q["key"],
            "week": q["week"],
            "topic_id": q["topic_id"],
            "topic_label": q["topic_label"],
            "level": q["level"],
            "q": q["q"],
            "options": shuffled_options,
            "answer": new_answer,
        })

    week_titles = {n: TOPICS[n]["title"] for n in TOPICS}

    return render_template(
        "quiz_run.html",
        questions=quiz_questions,
        pool_size=len(pool),
        requested_count=requested_count,
        selected_topics=selected,
        backtracking=backtracking,
        week_titles=week_titles,
    )


if __name__ == "__main__":
    app.run(debug=True, port=4001)
