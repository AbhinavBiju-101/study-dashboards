"""Normalise the four dashboards' quiz banks into one shape for the mixed quiz.

Section labels are built exactly like each dashboard's own quiz-result screen builds them
("W1 · topic", "T1 · topic", ...) so progress recorded from a dashboard quiz and from the
mixed quiz lands on the same row of the Progress page.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _read(slug, name):
    return json.loads((ROOT / "dashboards" / f"{slug}-dashboard" / "data" / name).read_text("utf-8"))


def _by_unit_bank(slug, prefix, unit_word, titles):
    """EVS / BE layout: {unit: {sid: {label, questions}}}."""
    sections, questions = [], []
    for unit, secs in _read(slug, "quiz_bank.json").items():
        for sid, sec in secs.items():
            label = f"{prefix}{unit} · {sec['label']}"
            sections.append({"id": f"{slug}:{unit}:{sid}", "group": f"{unit_word} {unit} · {titles.get(int(unit), '')}".strip(" ·"),
                             "label": label, "n": len(sec["questions"])})
            for q in sec["questions"]:
                questions.append((f"{slug}:{unit}:{sid}", q["level"], q["q"], q["options"], q["answer"]))
    return sections, questions


def _baeng():
    sections, questions = [], []
    for sid, sec in _read("baeng101", "quiz_bank.json").items():
        sections.append({"id": f"baeng101:{sid}", "group": sec["module"], "label": sec["label"], "n": len(sec["questions"])})
        for q in sec["questions"]:
            questions.append((f"baeng101:{sid}", q["level"], q["q"], q["options"], q["answer"]))
    return sections, questions


def _phy():
    syl = _read("phy", "syllabus.json")["modules"]
    mod_title = {m["n"]: m["title"] for m in syl}
    sub_title = {s["id"]: s["title"] for m in syl for t in m["topics"] for s in t["subtopics"]}
    top_title = {t["id"]: t["title"] for m in syl for t in m["topics"]}
    secs, questions = {}, []
    for q in _read("phy", "quiz_bank.json")["questions"]:
        sid = q.get("subtopic") or q["topic"]
        title = sub_title.get(sid) or top_title.get(q["topic"], sid)
        key = f"phy:{sid}"
        if key not in secs:
            secs[key] = {"id": key, "group": f"Module {q['module']} · {mod_title.get(int(q['module']), '')}",
                         "label": title, "n": 0}
        secs[key]["n"] += 1
        questions.append((key, q["bloom"], q["question"], q["options"], q["answer"]))
    return list(secs.values()), questions


def build_bank(subjects):
    """Return the JSON-serialisable payload for /api/bank."""
    evs = sys.modules.get("dash_evs")
    be = sys.modules.get("dash_be")
    evs_titles = {n: w["title"] for n, w in getattr(evs, "WEEKS", {}).items()}
    be_titles = {n: t["title"] for n, t in getattr(be, "TOPICS", {}).items()}
    loaders = {
        "evs": lambda: _by_unit_bank("evs", "W", "Week", evs_titles),
        "be": lambda: _by_unit_bank("be", "T", "Topic", be_titles),
        "baeng101": _baeng,
        "phy": _phy,
    }
    out_subjects, out_questions = [], []
    for s in subjects:
        if s["slug"] not in loaders:  # self-graded problem banks (e.g. bamat101) are not MCQ: kept out of the mixed quiz
            continue
        secs, qs = loaders[s["slug"]]()
        out_subjects.append({"slug": s["slug"], "code": s["code"], "title": s["title"], "accent": s["accent"], "sections": secs})
        for sec_id, level, q, options, answer in qs:
            out_questions.append({"s": s["slug"], "c": sec_id, "l": level, "q": q, "o": options, "a": answer})
    return {"subjects": out_subjects, "questions": out_questions}
