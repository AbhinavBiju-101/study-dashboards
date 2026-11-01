# EVS Notes Dashboard + Quiz

A small multi-page Flask site: four illustrated EVS weekly notebooks, a
syllabus dashboard with an expandable topic/subtopic tree, and a fully
custom MCQ quiz module built from a 180-question bank.

## Run it

```bash
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000**.

## Pages

- **`/`** — Dashboard: the full syllabus, one card per week. Click a week's
  title to open it. Click a topic row to expand it in place — you'll see a
  one-line summary of that topic, a link to open it in the notebook, and (if
  the notes had subheadings) a list of subtopics, each with its own summary
  and its own direct link.
- **`/week/<num>`** — A week's notebook inside a shared layout: a sticky top
  nav and matching bottom nav with **☰ Dashboard**, **📝 Quiz**, **← Prev**,
  **Next →**. Buttons grey out at the first/last week.
- **`/quiz`** — Quiz setup: tick whole weeks or expand into individual
  topics, see how many questions are available from your selection, choose
  exactly how many you want (fully custom count, clamped to what's
  available), and toggle **"Allow going back to previous questions"**
  (backtracking) on or off.
- **`/quiz/start`** (POST) — Runs the quiz: one question at a time, a
  clickable palette to jump between questions, Prev/Next, a live timer, and
  a **🚩 Flag for review** toggle on every question (flagged questions get a
  small flag marker in the palette). If backtracking was turned off at
  setup, the Previous button and any already-passed palette slots are
  locked — you can only move forward.
  **Every question's four options are reshuffled fresh on every attempt**
  (and the correct-answer index is remapped accordingly), so the same
  question never has a predictable answer position twice in a row.
  Submitting shows a full post-mortem: overall score, an **accuracy bar
  chart by week** (surfaces your weakest week at a glance), a second bar
  chart **by topic** (more granular drill-down), a time-analysis panel
  (average / fastest / slowest question, full per-question time bars), and
  a **filterable full review** — All / Correct / Wrong / Skipped, plus an
  independent "🚩 Flagged only" toggle that ANDs with whichever correctness
  filter is active. From there you can reshuffle the same topic set (same
  backtracking setting too) for another attempt, change topics, or head
  back to the dashboard.
- **`/download/<file>`** — Serves the original self-contained standalone
  HTML file for that week — handy for offline reading or sharing one file.

## Structure

```
evs-dashboard/
├── app.py                     Routes, WEEKS syllabus data, quiz bank loading/sampling
├── requirements.txt
├── data/
│   └── quiz_bank.json          360 MCQs (10 per topic × 36 topics — two independent
│                                  5-question sets merged), {week: {topic_id: {label, questions[]}}}
├── templates/
│   ├── base.html               Shared top/bottom nav bar, wraps every week page
│   ├── dashboard.html          Syllabus cards with expandable topic → subtopic tree
│   ├── week1.html .. week4.html   Each week's content, extends base.html
│   ├── quiz_setup.html         Week/topic picker + custom question-count control
│   └── quiz_run.html           The quiz itself + full post-quiz analytics
└── notes/
    ├── week1.html .. week4.html   Original standalone files (used by /download)
```

## How the quiz bank is structured

`data/quiz_bank.json` looks like:

```json
{
  "1": {
    "s1": {
      "label": "Environmental science, studies & engineering",
      "questions": [
        {"level": "Remember", "q": "...", "options": ["...","...","...","..."], "answer": 1},
        ...
      ]
    },
    "s2": { ... }
  },
  "2": { ... }
}
```

`answer` is a 0-based index into `options` **as stored** — the per-attempt
shuffle happens at request time in `quiz_start()` in `app.py`, so the file
on disk always stays in original, unshuffled order.

## Adding a fifth week later

1. Drop the original standalone `week5.html` into `notes/` (used for `/download`).
2. Turn it into a template: copy its `<style>` block and `<body>` content into
   a new `templates/week5.html` that extends `base.html` (use `templates/week4.html`
   as a pattern).
3. Add one entry (num `5`) to the `WEEKS` dict at the top of `app.py`, with its
   `title`, `desc`, `accent` colours, and a `topics` list (id/label/summary/
   subtopics matching the `id="..."` anchors in that week's `<section>`/`<h3>` tags).
4. Add a `"5": {...}` block to `data/quiz_bank.json` with the same
   `{topic_id: {label, questions}}` shape, 5 questions per topic.

Dashboard, routing, prev/next nav, and the quiz picker all pick it up
automatically — nothing else needs to change.

## Weeks 5 and 6 (added)

- Week 5: climate change, carbon sequestration, environmental health monitoring (111 questions).
- Week 6: solar, hydro and wind, ocean thermal and geothermal, biomass, hydrogen, environmental acts and EIA (356 questions).
- Same format as weeks 1-4: `notes/week5.html` and `notes/week6.html` are standalone pages; `templates/week5.html` and `templates/week6.html` are the same content inside the dashboard layout. Diagrams are inline vector SVG; equations are MathML (no internet needed).
- `notes/week5.pdf` and `notes/week6.pdf` are optional print versions (`/download/week5.pdf`).
- Quiz bank topic ids are `s1..s11` (week 5) and `s1..s34` (week 6), one per MCQ subsection, with both question sets merged and duplicates removed.
