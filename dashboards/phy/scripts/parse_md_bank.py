"""Parses data/source/Physics_MCQ_Bank_Modules_2-4.md into data/source/mcq_bank.json (parsed with code, nothing retyped).

Expected markdown (as in the supplied bank):
    ### 2.5 Inner Product            <- section header: <module>.<n> <title>
    **Q3 (Apply).** question text    <- Bloom's level in brackets
    * A. option ... * D. option
    **Answer: B**
Each bank section is mapped to a subtopic of the notes (SECTION_MAP below; per-question overrides where a bank
section spans several subtopics). Bloom's level, option order and the answer letter are copied exactly as given.
The bank has no explanations, so none are added."""
import re, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "source" / "Physics_MCQ_Bank_Modules_2-4.md"
OUT = ROOT / "data" / "source" / "mcq_bank.json"

# bank section -> default subtopic id; overrides: {question number: subtopic id}
SECTION_MAP = {
 "2.1": ("m2-1-1", {2: "m2-1-4"}),
 "2.2": ("m2-1-3", {1: "m2-1-4", 3: "m2-1-2", 6: "m2-1-2"}),
 "2.3": ("m2-2-1", {}),
 "2.4": ("m2-2-2", {2: "m2-3-1", 4: "m2-3-1"}),
 "2.5": ("m2-3-2", {}),
 "2.6": ("m2-3-3", {}),
 "2.7": ("m2-3-4", {}),
 "2.8": ("m2-4-1", {3: "m2-4-2", 4: "m2-4-2", 6: "m2-4-2"}),
 "2.9": ("m2-4-2", {}),
 "2.10": ("m2-4-3", {}),
 "2.11": ("m2-4-5", {1: "m2-4-4", 2: "m2-4-4", 6: "m2-4-4"}),
 "2.12": ("m2-5-1", {}),
 "2.13": ("m2-6-1", {3: "m2-6-2", 5: "m2-6-2", 4: "m2-7-2"}),
 "2.14": ("m2-7-2", {1: "m2-7-1", 3: "m2-7-1"}),
 "3.1": ("m3-1-1", {2: "m3-1-2", 4: "m3-1-2"}),
 "3.2": ("m3-1-2", {2: "m3-1-4"}),
 "3.3": ("m3-1-4", {4: "m3-3-1", 5: "m3-3-1"}),
 "3.4": ("m3-2-2", {2: "m3-2-1", 5: "m3-2-3", 8: "m3-2-3", 6: "m3-2-4"}),
 "3.5": ("m3-4-1", {}),
 "3.6": ("m3-4-3", {1: "m3-4-2", 2: "m3-4-2"}),
 "3.7": ("m3-4-4", {}),
 "3.8": ("m3-4-5", {}),
 "3.9": ("m3-4-6", {4: "m3-4-5"}),
 "4.1": ("m4-1-1", {}),
 "4.2": ("m4-1-3", {1: "m4-1-2"}),
 "4.3": ("m4-1-4", {2: "m4-2-1", 4: "m4-2-1"}),
 "4.4": ("m4-1-5", {}),
 "4.5": ("m4-2-2", {3: "m4-2-1"}),
 "4.6": ("m4-2-3", {4: "m4-2-4", 5: "m4-2-4"}),
 "4.7": ("m4-2-1", {3: "m4-2-4"}),
 "4.8": ("m4-1-4", {2: "m4-2-5", 4: "m4-2-1"}),
}

def clean(s):
    s = re.sub(r"\\([_*\[\]()#<>.!-])", r"\1", s)     # markdown escapes such as S\_z
    return s.strip()

def parse(text):
    qs, sec, cur = [], None, None
    for line in text.splitlines():
        m = re.match(r"^### (\d+\.\d+) (.*)", line)
        if m: sec = m.group(1); continue
        m = re.match(r"^\*\*Q(\d+) \((\w+)\)\.\*\* (.*)", line)
        if m:
            cur = dict(section=sec, qnum=int(m.group(1)), bloom=m.group(2), question=clean(m.group(3)), options=[], answer_letter=None)
            qs.append(cur); continue
        m = re.match(r"^\* ([A-D])\. (.*)", line)
        if m and cur is not None:
            cur["options"].append(clean(m.group(2))); continue
        m = re.match(r"^\*\*Answer: ([A-D])\*\*\s*$", line)
        if m and cur is not None:
            cur["answer_letter"] = m.group(1)
    return qs

def main():
    qs = parse(SRC.read_text(encoding="utf-8"))
    out, problems = [], []
    for q in qs:
        sub_default, over = SECTION_MAP[q["section"]]
        sub = over.get(q["qnum"], sub_default)
        if len(q["options"]) != 4 or q["answer_letter"] is None:
            problems.append((q["section"], q["qnum"])); continue
        out.append(dict(module=int(q["section"].split(".")[0]), topic=sub.rsplit("-", 1)[0], subtopic=sub,
                        bloom=q["bloom"], question=q["question"], options=q["options"],
                        answer="ABCD".index(q["answer_letter"]), source=f"bank {q['section']} Q{q['qnum']}"))
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"parsed {len(qs)} questions, wrote {len(out)}, problems: {problems}")

if __name__ == "__main__":
    main()
