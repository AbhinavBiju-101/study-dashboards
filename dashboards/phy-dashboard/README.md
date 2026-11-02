# QM Illustrated Notes (BAPHY105, Modules 1-5)

Flask study dashboard: illustrated notes for all five modules of BAPHY105 (wave-particle duality, maths foundations, postulates
with Schrödinger equations, particle in a box with degeneracy and tunnelling, elements of quantum computing), plus an
exam-recap page and a quiz.

## Run
```
python -m venv venv && source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py                                        # open http://127.0.0.1:5000
```

## Routes
`/` dashboard · `/module/1|2|3|4|5` notes · `/recap` exam recap · `/quiz` setup · `POST /quiz/start`

## Data (built by scripts, not retyped)
- `python scripts/build_syllabus.py` builds `data/syllabus.json` from `scripts/syllabus_spec.py`.
- Quiz bank pipeline: `python scripts/parse_md_bank.py` parses `data/source/Physics_MCQ_Bank_Modules_2-4.md` (183 questions) into
  `data/source/mcq_bank.json`, The new-topics bank (337 questions, Modules 1, 3 s5, 4 s3.3-5, 5) is `data/source/Physics_MCQ_Bank_New_Topics_Set1.md`, with its JSON in `data/source/mcq_bank_new_topics.json`. `python scripts/build_quiz_bank.py` merges every `*.json`/`*.csv` in `data/source/`, drops exact
  duplicates and writes `data/quiz_bank.json`. Bloom's level, option text and the keyed answer are copied exactly as in the bank.
- The bank's 31 sections are mapped to the notes' subtopics in `SECTION_MAP` (top of `parse_md_bank.py`; a few sections are split
  per question). Edit the map and re-run the two scripts if you want a different assignment.
- The bank has no explanations, so the quiz review shows none.
- The bank covers Modules 2 to 4 only. Modules 1 and 5 (and the newer Module 3 §5, Module 4 §3.3, §4, §5 topics) have notes but no quiz questions; the dashboard hides the Quiz pill where there are none. Drop a new JSON/CSV in `data/source/` and re-run `build_quiz_bank.py` to add questions.
- Module 1's decks are scans: they were read by OCR plus the slide images. Module 1 extras (photoelectric effect, Davisson-Germer, uncertainty principle) are in your decks but not in the syllabus line; they are marked "extra".
- **The exam-recap page is still a labelled placeholder**: the recap file and model paper were not supplied.

## Verify
`python scripts/verify.py` (every route, every dashboard anchor, duplicate ids, real-bank integrity, quiz sampling/shuffle/answer remap, bank builder)
and `python tests/check_examples.py` (independent numeric check of the worked examples).
Both use Flask's test client. Separately, the new pages (Modules 1 and 5, Module 4 sections 3.3 to 5) were opened in headless Chromium and their figures checked by screenshot. The quiz screens were tested through the test client only, not clicked through in a browser.
