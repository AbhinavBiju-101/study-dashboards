"""Build data/problems.json from data/problems_src/bank_m*.txt

Source format (plain text; math is LaTeX inside \\( \\) and \\[ \\]):

    ### TOPIC F | 1 | Functions of Two Variables and Partial Derivatives
    #### F1 | Remember | 4 | 19
    Q:
    Problem text, as printed in the Practice Problem Bank.
    (a) sub-parts stay on their own lines.
    A:
    The worked answer from the Answer Key.

TOPIC line:  prefix | module number | topic title
Problem line: id | Bloom level | page of the problem in the PDF | page of its answer in the PDF
Usage: python tools/build_problems.py [--check]      (--check = validate only, write nothing)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "problems_src"
OUT = ROOT / "data" / "problems.json"
LEVELS = ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"]
EXPECTED = {"F": 7, "TD": 7, "J": 7, "TE": 7, "MM": 6, "LM": 7, "DI": 6, "DP": 6, "TI": 6, "G": 6, "D": 6, "Dv": 6,
            "C": 6, "P": 6, "L": 6, "Gr": 6, "S": 6, "St": 6, "Gs": 6, "O": 6, "PI": 7, "VP": 7, "CE": 8, "CL": 6,
            "AP": 7, "FP": 8, "PQ": 7, "ZP": 7, "XP": 7, "CK": 7, "LG": 8, "SV": 7}


def parse(path):
    topics, topic, prob, mode, errs = [], None, None, None, []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("### TOPIC "):
            parts = [p.strip() for p in line[len("### TOPIC "):].split("|")]
            if len(parts) != 3 or not parts[1].isdigit():
                errs.append(f"{path.name}:{n}: bad TOPIC line"); continue
            topic = {"prefix": parts[0], "module": int(parts[1]), "title": parts[2], "problems": []}
            topics.append(topic); prob = mode = None
        elif line.startswith("#### "):
            parts = [p.strip() for p in line[5:].split("|")]
            if topic is None or len(parts) != 4 or parts[1] not in LEVELS or not (parts[2].isdigit() and parts[3].isdigit()):
                errs.append(f"{path.name}:{n}: bad problem line: {line[:60]}"); continue
            prob = {"id": parts[0], "level": parts[1], "q_page": int(parts[2]), "a_page": int(parts[3]), "q": [], "a": []}
            topic["problems"].append(prob); mode = None
        elif line.strip() == "Q:" and prob is not None: mode = "q"
        elif line.strip() == "A:" and prob is not None: mode = "a"
        elif prob is not None and mode: prob[mode].append(line)
    for t in topics:
        for p in t["problems"]:
            for k in ("q", "a"):
                p[k] = "\n".join(p[k]).strip()
                if not p[k]: errs.append(f"{p['id']}: empty {k.upper()}")
            if not re.fullmatch(re.escape(t["prefix"]) + r"\d+", p["id"]): errs.append(f"{p['id']}: id does not match topic prefix {t['prefix']}")
    return topics, errs


def main():
    check = "--check" in sys.argv
    topics, errs = [], []
    for f in sorted(SRC.glob("bank_m*.txt")):
        t, e = parse(f); topics += t; errs += e
    seen = {}
    for t in topics:
        n = len(t["problems"])
        if t["prefix"] in EXPECTED and n != EXPECTED[t["prefix"]]:
            errs.append(f"topic {t['prefix']}: {n} problems, expected {EXPECTED[t['prefix']]}")
        for p in t["problems"]:
            if p["id"] in seen: errs.append(f"duplicate id {p['id']}")
            seen[p["id"]] = 1
    total = sum(len(t["problems"]) for t in topics)
    print(f"{len(topics)} topics, {total} problems" + (" (expected 211 across 32 topics)" if total != 211 or len(topics) != 32 else ""))
    for e in errs: print("ERROR", e)
    if errs: sys.exit(1)
    if not check:
        OUT.write_text(json.dumps(sorted(topics, key=lambda t: (t["module"], list(EXPECTED).index(t["prefix"]) if t["prefix"] in EXPECTED else 99)), ensure_ascii=False, indent=1), encoding="utf-8")
        print("wrote", OUT)


if __name__ == "__main__":
    main()
