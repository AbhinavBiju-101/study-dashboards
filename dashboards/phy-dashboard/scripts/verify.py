"""Verification: run every route with Flask's test client, check anchors and ids, and exercise the quiz.
Run from the project root:  python scripts/verify.py"""
import sys, re, json, pathlib, random
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import app as appmod
from html.parser import HTMLParser

client = appmod.app.test_client()
fails = []
def check(name, cond, extra=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  " + extra) if extra and not cond else ""))
    if not cond: fails.append(name)

class Collect(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids = []; self.hrefs = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d: self.ids.append(d["id"])
        if tag == "a" and d.get("href"): self.hrefs.append(d["href"])

def parse(url):
    r = client.get(url); c = Collect(); c.feed(r.get_data(as_text=True)); return r, c

# 1. every route returns 200
pages = {}
for u in ["/", "/module/1", "/module/2", "/module/3", "/module/4", "/module/5", "/recap", "/quiz", "/module/2?x=1"]:
    r, c = parse(u); pages[u] = c
    check(f"GET {u} -> 200", r.status_code == 200)
check("GET /module/9 -> 404", client.get("/module/9").status_code == 404)
check("POST /quiz/start works", client.post("/quiz/start", data={}).status_code == 200)

# 2. duplicate ids on each page
for u in ["/module/1", "/module/2", "/module/3", "/module/4", "/module/5"]:
    ids = pages[u].ids; dup = {i for i in ids if ids.count(i) > 1}
    check(f"no duplicate ids on {u}", not dup, str(dup))

# 3. every dashboard anchor exists on its target page
syl = json.loads((ROOT / "data" / "syllabus.json").read_text(encoding="utf-8"))["modules"]
n_checked = 0
for href in pages["/"].hrefs:
    m = re.match(r"^/module/(\d+)#(.+)$", href)
    if m:
        n_checked += 1
        check(f"anchor {href} exists", m.group(2) in pages[f"/module/{m.group(1)}"].ids)
check("dashboard has anchor links", n_checked > 50, f"only {n_checked}")
# every syllabus id is an anchor on its module page
for mod in syl:
    ids = pages[f"/module/{mod['n']}"].ids
    for t in mod["topics"]:
        check(f"topic id {t['id']} in page", t["id"] in ids)
        for s in t["subtopics"]:
            check(f"subtopic id {s['id']} in page", s["id"] in ids)
# anchors used by the recap page
for href in pages["/recap"].hrefs:
    m = re.match(r"^/module/(\d+)#(.+)$", href)
    if m: check(f"recap anchor {href} exists", m.group(2) in pages[f"/module/{m.group(1)}"].ids)
# quiz links on the dashboard point to real ids
subs = {s["id"] for mod in syl for t in mod["topics"] for s in t["subtopics"]}
for href in pages["/"].hrefs:
    m = re.match(r"^/quiz\?sub=(.+)$", href)
    if m: check(f"quiz link {href} valid", m.group(1) in subs)

# 4. nav: prev/next on each module page
for n, (p, nx) in {1: (None, 2), 2: (1, 3), 3: (2, 4), 4: (3, 5), 5: (4, None)}.items():
    h = pages[f"/module/{n}"].hrefs
    check(f"module {n} next link", (f"/module/{nx}" in h) if nx else ("/recap" in h))
    check(f"module {n} prev link", (f"/module/{p}" in h) if p else ("/" in h))

# 5. quiz machinery with a throw-away test bank (NOT shipped; the real bank is empty)
test_bank = {"status": "ok", "questions": [
    {"id": f"t{i}", "module": 2, "topic": "m2-1", "subtopic": "m2-1-3" if i % 2 else "m2-1-4", "bloom": "Understand" if i % 3 else "Apply",
     "question": f"Test question {i}?", "options": ["A", "B", "C", "D"], "answer": i % 4, "explanation": "x"} for i in range(12)]}
orig = appmod.quiz_bank
appmod.quiz_bank = lambda: test_bank
r = client.get("/quiz"); check("quiz setup renders with bank", r.status_code == 200 and "Test" not in r.get_data(as_text=True) or r.status_code == 200)
r = client.post("/quiz/start", data={"sub": ["m2-1-3", "m2-1-4"], "bloom": ["Understand", "Apply"], "count": "8", "allow_back": "on"})
html = r.get_data(as_text=True)
check("quiz start 200", r.status_code == 200)
m = re.search(r"var Q = (\[.*?\]);\s*var ALLOW_BACK", html, re.S)
check("quiz data embedded", bool(m))
Q = json.loads(m.group(1))
check("8 questions sampled", len(Q) == 8)
ok = True
for q in Q:
    src = next(x for x in test_bank["questions"] if x["id"] == q["id"])
    ok &= q["options"][q["answer"]] == src["options"][src["answer"]] and sorted(q["options"]) == sorted(src["options"])
check("answer index remapped correctly after shuffle", ok)
orders = set()
for _ in range(30):
    rr = client.post("/quiz/start", data={"sub": ["m2-1-3"], "count": "1"})
    mm = re.search(r"var Q = (\[.*?\]);\s*var ALLOW_BACK", rr.get_data(as_text=True), re.S)
    q = json.loads(mm.group(1))[0]; orders.add(tuple(q["options"]))
check("options really shuffle between attempts", len(orders) > 1)
r = client.post("/quiz/start", data={"sub": ["m2-1-3"], "count": "500"})
check("count capped by availability", len(json.loads(re.search(r"var Q = (\[.*?\]);\s*var ALLOW_BACK", r.get_data(as_text=True), re.S).group(1))) == 6)
r = client.post("/quiz/start", data={"sub": ["m2-1-3"], "count": "3"})
check("allow_back off -> ALLOW_BACK false", "var ALLOW_BACK = false" in r.get_data(as_text=True))
check("quiz runner has palette, flag, timer, submit", all(k in html for k in ["palette", "flag", "timer", "submit"]))
appmod.quiz_bank = orig

# 6. the real bank
bank_real = json.loads((ROOT / "data" / "quiz_bank.json").read_text(encoding="utf-8"))
RQ = bank_real["questions"]
check("real bank is non-empty", len(RQ) > 0, f"{len(RQ)} questions")
check("every real question has 4 options and a valid answer index", all(len(q["options"]) == 4 and 0 <= q["answer"] < 4 for q in RQ))
check("every real question maps to a real subtopic", all(q["subtopic"] in subs for q in RQ))
check("Bloom's level present on every real question", all(q["bloom"] in {"Remember","Understand","Apply","Analyze","Evaluate","Create"} for q in RQ))
check("no exact duplicates in real bank", len({(q["question"].lower(), tuple(sorted(o.lower() for o in q["options"]))) for q in RQ}) == len(RQ))
r = client.post("/quiz/start", data={"count": "10", "allow_back": "on"})
mm = re.search(r"var Q = (\[.*?\]);\s*var ALLOW_BACK", r.get_data(as_text=True), re.S)
RS = json.loads(mm.group(1)) if mm else []
check("real quiz starts and embeds 10 questions", r.status_code == 200 and len(RS) == 10)
src_by_q = {q["question"]: q for q in RQ}
check("real quiz: remapped answer still points at the keyed option", all(q["options"][q["answer"]] == src_by_q[q["question"]]["options"][src_by_q[q["question"]]["answer"]] for q in RS))
r = client.get("/quiz"); check("setup page shows real counts", "Module 2" in r.get_data(as_text=True) and ">85<" in r.get_data(as_text=True))

# 7. bank builder merge/duplicates on TEMP folders (never touches data/source or the real bank)
import subprocess, tempfile, os
with tempfile.TemporaryDirectory() as td:
    tsrc = pathlib.Path(td) / "src"; tsrc.mkdir(); tout = pathlib.Path(td) / "out.json"
    a = [{"module": 2, "topic": "m2-1", "subtopic": "m2-1-3", "bloom": "Apply", "question": "Q?", "options": ["x", "y"], "answer": "y"}]
    (tsrc / "a.json").write_text(json.dumps(a)); (tsrc / "b.json").write_text(json.dumps(a + [dict(a[0], question="Q2?")]))
    env = dict(os.environ, QM_SRC=str(tsrc), QM_OUT=str(tout))
    out = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_quiz_bank.py")], capture_output=True, text=True, env=env).stdout
    d = json.loads(tout.read_text(encoding="utf-8"))
    check("bank builder merges and drops exact duplicates", len(d["questions"]) == 2 and "duplicates_dropped=1" in out, out)
    check("bank builder preserves Bloom level", d["questions"][0]["bloom"] == "Apply")

print("\nFAILED:" if fails else "\nALL CHECKS PASSED", fails or "")
sys.exit(1 if fails else 0)
