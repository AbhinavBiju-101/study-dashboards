# BAMAT101 Notes Dashboard
Multivariable Calculus and Differential Equations (Modules 1-5 + summary).

    pip install -r requirements.txt
    python app.py     # http://127.0.0.1:4003

- `/` syllabus tree (every section links to its page in the PDF reader) · `/module/1..6` module page with the figures and the PDF reader
- `/read/notes?page=N`, `/read/bank?page=N` embedded PDF reader · `/download/notes|bank`
- `/quiz` self-graded practice: pick topics and Bloom levels, attempt, reveal the worked answer, rate yourself.
  The Practice Problem Bank is open-ended (not multiple choice), so answers are self-assessed.
- `data/syllabus.json` modules/sections; `data/problems.json` the problems (built from `data/problems_src/bank_m*.txt` with `python tools/build_problems.py`).
- `notes_html/*.html` + `data/tree_*.json` (optional): converted notes. When present they replace the PDF reader on module pages.
- Maths is rendered with KaTeX (vendored in `static/katex`).
