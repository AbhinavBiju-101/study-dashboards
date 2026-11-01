"""Builds data/syllabus.json from scripts/syllabus_spec.py."""
import json, pathlib
from syllabus_spec import MODULES
out = []
for m in MODULES:
    mm = {k: v for k, v in m.items() if k != "topics"}
    mm["topics"] = []
    for t in m["topics"]:
        tt = dict(id=t["id"], title=t["title"], summary=t["summary"], excluded=(len(t["subs"]) == 0), subtopics=[])
        for sid, title, summ in t["subs"]:
            tt["subtopics"].append(dict(id=sid, title=title, summary=summ))
        mm["topics"].append(tt)
    out.append(mm)
p = pathlib.Path(__file__).resolve().parent.parent / "data" / "syllabus.json"
p.write_text(json.dumps(dict(modules=out), indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote", p, "modules:", len(out), "subtopics:", sum(len(t["subtopics"]) for m in out for t in m["topics"]))
