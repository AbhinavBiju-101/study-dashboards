"""Parses question-bank files from data/source/ into data/quiz_bank.json (no retyping).

Accepted inputs (drop them in data/source/):
  *.json  a list of objects (or {"questions":[...]}) with keys:
          module, topic, subtopic, bloom, question, options (list), answer (0-based index or the option text)
  *.csv   columns: module,topic,subtopic,bloom,question,option1..optionN,answer  (answer = 1-based number or option text)
Overlapping files are merged; exact duplicates (same question text + same option set) are dropped.
Bloom's level is copied as given. Nothing is invented: rows missing a question, options or an answer are reported and skipped.
"""
import csv, json, os, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path(os.environ.get("QM_SRC", ROOT / "data" / "source"))
OUT = pathlib.Path(os.environ.get("QM_OUT", ROOT / "data" / "quiz_bank.json"))


def norm_answer(ans, options, one_based):
    if isinstance(ans, str) and ans.strip() in options:
        return options.index(ans.strip())
    try:
        i = int(ans) - (1 if one_based else 0)
        return i if 0 <= i < len(options) else None
    except (TypeError, ValueError):
        return None


def rows_from_json(p):
    d = json.loads(p.read_text(encoding="utf-8"))
    d = d["questions"] if isinstance(d, dict) else d
    for r in d:
        opts = [str(o).strip() for o in r.get("options", [])]
        yield dict(module=r.get("module"), topic=r.get("topic"), subtopic=r.get("subtopic"), bloom=r.get("bloom"),
                   question=(r.get("question") or "").strip(), options=opts,
                   answer=norm_answer(r.get("answer"), opts, False), explanation=r.get("explanation", ""), source=r.get("source", ""), file=p.name)


def rows_from_csv(p):
    with p.open(encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            opts = [v.strip() for k, v in r.items() if k and k.lower().startswith("option") and v and v.strip()]
            yield dict(module=r.get("module"), topic=r.get("topic"), subtopic=r.get("subtopic"), bloom=r.get("bloom"),
                       question=(r.get("question") or "").strip(), options=opts,
                       answer=norm_answer(r.get("answer"), opts, True), explanation=r.get("explanation", ""), source=r.get("source", ""), file=p.name)


def main():
    files = sorted(SRC.glob("*.json")) + sorted(SRC.glob("*.csv")) if SRC.exists() else []
    seen, out, skipped, dupes = set(), [], 0, 0
    for p in files:
        for r in (rows_from_json(p) if p.suffix == ".json" else rows_from_csv(p)):
            if not r["question"] or len(r["options"]) < 2 or r["answer"] is None or not (r["module"] and r["topic"] and r["subtopic"]):
                skipped += 1
                print("skipped row from", r["file"], ":", r["question"][:60])
                continue
            key = (r["question"].lower(), tuple(sorted(o.lower() for o in r["options"])))
            if key in seen:
                dupes += 1
                continue
            seen.add(key)
            r["id"] = f"q{len(out) + 1:04d}"
            r["bloom"] = r["bloom"] or "Unspecified"
            r.pop("file")
            out.append(r)
    doc = dict(status="ok" if out else "missing",
               note="" if out else "No question-bank file was supplied with the request, so this bank is empty. Put the bank in data/source/ and run scripts/build_quiz_bank.py.",
               questions=out)
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"files={len(files)} kept={len(out)} duplicates_dropped={dupes} skipped={skipped}")


if __name__ == "__main__":
    main()
