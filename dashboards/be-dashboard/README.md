# Basic Engineering Notes Dashboard + Quiz

A small multi-page Flask site, built the same way as the EVS dashboard: two
illustrated notebooks (Circuits, and Machines), a syllabus dashboard with an
expandable topic/subtopic tree, and a custom MCQ quiz module with 100
questions spanning multiple Bloom's-Taxonomy levels.

## Run it

```bash
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000**.

## Pages

- **`/`** — Dashboard: the full syllabus, one card per topic. Click a topic's
  title to open it. Click "subtopics covered" to expand it in place — you'll
  see a one-line summary of each subtopic and a link to jump straight to it
  in the notebook.
- **`/topic/<num>`** — A topic's notebook inside a shared layout: a sticky
  top nav and matching bottom nav with **☰ Dashboard**, **📝 Quiz**, **←
  Prev**, **Next →**. Buttons grey out at the first/last topic.
- **`/quiz`** — Quiz setup: tick whole topics or expand into individual
  subtopics, see how many questions are available from your selection,
  choose exactly how many you want, and toggle **"Allow going back to
  previous questions"** on or off.
- **`/quiz/start`** (POST) — Runs the quiz: one question at a time, a
  clickable palette, Prev/Next, a live timer, and a **🚩 Flag for review**
  toggle per question. **Every question's four options are reshuffled fresh
  on every attempt.** Submitting shows a full post-mortem: overall score, an
  accuracy bar chart **by topic**, a second chart **by subtopic**, a
  time-analysis panel, and a filterable full review (All / Correct / Wrong /
  Skipped, plus an independent "🚩 Flagged only" toggle).
- **`/download/<file>`** — Serves the original self-contained standalone
  HTML file for that topic.

## Structure

```
be-dashboard/
├── app.py                     Routes, TOPICS syllabus data, quiz bank loading/sampling
├── diagrams.py                All circuit/wave/machine diagrams, drawn from one symbol library (run it to preview PNGs)
├── build_expand.py            Adds key-terms boxes, extra content, diagrams and glossary to the topic pages (re-runnable)
├── expand_data1.py / expand_data2.py   The terms and extra teaching content it inserts (edit these to add more)
├── _orig/                     Pristine base copies of the topic pages that build_expand.py starts from
├── build_quiz_bank.py         Regenerates data/quiz_bank.json from source (re-run after editing it)
├── requirements.txt
├── data/
│   └── quiz_bank.json          100 MCQs (5 per subtopic × 20 subtopics),
│                                  {topic: {subtopic_id: {label, questions[]}}}
├── templates/
│   ├── base.html               Shared top/bottom nav bar, wraps every topic page
│   ├── dashboard.html          Syllabus cards with expandable topic → subtopic tree
│   ├── topic1.html             Topic 1 — DC & AC Circuits (extends base.html)
│   ├── topic2.html             Topic 2 — Electrical Machines (extends base.html)
│   ├── quiz_setup.html         Topic/subtopic picker + custom question-count control
│   └── quiz_run.html           The quiz itself + full post-quiz analytics
└── notes/
    ├── topic1.html              Standalone copy of Topic 1 (used by /download)
    └── topic2.html              Standalone copy of Topic 2 (used by /download)
```

## How the quiz bank is structured

`data/quiz_bank.json` looks like:

```json
{
  "1": {
    "a1": {
      "label": "Ohm's Law & Circuit Elements",
      "questions": [
        {"level": "Remember", "q": "...", "options": ["...","...","...","..."], "answer": 0},
        {"level": "Understand", ...},
        {"level": "Apply", ...},
        {"level": "Analyze", ...},
        {"level": "Evaluate", ...}
      ]
    },
    "a2": { ... }
  },
  "2": { ... }
}
```

`answer` is a 0-based index into `options` **as stored** — the per-attempt
shuffle happens at request time in `quiz_start()` in `app.py`, so the file
on disk always stays in original, unshuffled order. Every subtopic has
exactly one question at each of five Bloom's levels: Remember, Understand,
Apply, Analyze, Evaluate.

## Adding a third topic later

1. Drop a standalone `topic3.html` into `notes/` (used for `/download`).
2. Turn it into a template: copy its `<style>` block and content into a new
   `templates/topic3.html` that extends `base.html` (use `templates/topic2.html`
   as a pattern).
3. Add one entry (num `3`) to the `TOPICS` dict at the top of `app.py`, with
   its `title`, `desc`, `accent` colours, and a `topics` list (id/label/summary
   matching the `id="..."` anchors in that topic's `<h3>` tags).
4. Add a `"3": {...}` block to `data/quiz_bank.json` (or extend
   `build_quiz_bank.py` and re-run it) with the same `{subtopic_id: {label,
   questions}}` shape.

Dashboard, routing, prev/next nav, and the quiz picker all pick it up
automatically — nothing else needs to change.


## Notebook depth

Every subtopic opens with a **Key terms** box (vocabulary you might be asked to define), followed by the definition, derivation, worked examples and extra material drawn from the lecture slides. Each topic page ends with an **A–Z Glossary** of all its terms. To add more terms or content, edit `expand_data1.py` / `expand_data2.py` and run `python build_expand.py`.
