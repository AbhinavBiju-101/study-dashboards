# Study Dashboards

Parent site that lists every study dashboard and routes to it. All dashboards are mounted
inside **one** Render web service (Render exposes one port per service, so 4000/4001/4002/4005
can't be hosted side by side).

| Subject | Local port (standalone) | URL on the hub |
|---|---|---|
| EVS | 4000 | `/evs/` |
| Basic Engineering | 4001 | `/be/` |
| BAENG101 | 4002 | `/baeng101/` |
| BAPHY105 (QM) | 4005 | `/phy/` |

```
app.py            hub routes + APIs, mounts each dashboard (DispatcherMiddleware)
subjects.py       the registry: one entry per subject (card text, colour, notes-page pattern)
banks.py          normalises the 4 quiz banks for the mixed quiz
search.py         full-text index over every dashboard's notes
templates/ static/  hub pages (light theme), favicon, client JS
dashboards/<slug>-dashboard/  your Flask projects, unchanged (evs-dashboard, be-dashboard, ...)
render.yaml       Render blueprint
```

## Hub pages
| Page | What it does |
|---|---|
| `/` Home | Streak, quizzes, accuracy, quick-start actions, per-subject progress, recent activity |
| `/subjects` | Subject cards with jump-links to every week/topic/module |
| `/quiz` Mixed quiz | Pick any subjects/topics/Bloom levels, balanced sampling, retry missed, presets (`?preset=quick`, `?preset=weak`) |
| `/progress` | Accuracy by subject and Bloom level, weak areas, trend, 16-week heatmap, history, export/import/clear |
| `/search` | Full-text search across all notes; each hit deep-links to its section |

Progress comes from the mixed quiz **and** from each dashboard's own quiz: a one-line guarded
`hubRecord(...)` call in each dashboard's quiz-result code reports to the hub (a no-op when a dashboard runs standalone).
Section labels match between the two, so results merge on the Progress page.

## Run locally
With Docker: `docker build -t study-dashboards . && docker run -p 3000:10000 -e SECRET_KEY=dev study-dashboards` then open http://127.0.0.1:3000.

Without Docker:
```
pip install -r requirements.txt
python app.py          # http://127.0.0.1:3000
```
Each dashboard can still be run on its own (`cd dashboards/evs-dashboard && python app.py`).

## Deploy to Render
1. Push this folder to a GitHub repo.
2. Render -> New -> **Blueprint** -> pick the repo (it reads `render.yaml` and builds the `Dockerfile`).
   Or New -> Web Service -> Language: Docker. Render supplies `$PORT`; the container honours it.
3. `SECRET_KEY` is generated for you. Free instances sleep after idle, so the first load can take ~30-60 s.

## Add a subject later
Put the Flask project in `dashboards/<slug>-dashboard/` (must expose `app` in `app.py`, use `url_for` for links),
add one entry to `subjects.py`. It is mounted and gets a card automatically.

## Notes
- Everything shares one domain, so browser `localStorage` is shared. Current keys don't collide (`b101`, `qm_*`).
  New dashboards should prefix their keys.
- Dashboards get a small "All subjects" pill (bottom-left) when served through the hub; standalone runs don't.
- The old nested copy `evs-dashboard/evs-dashboard/` from the zip was older and was left out.

## Supabase later (quiz outcomes)
All reads and writes go through `static/hub-store.js` (`read`, `record`, `clear`, import/export), so moving to Supabase
means changing that one file: `record()` posts the attempt (`subject, mode, secs, rows`) to a `/api/results` endpoint
backed by Supabase (`SUPABASE_URL` / `SUPABASE_KEY` as Render env vars) and `read()` loads it back. Nothing else changes.
Until then, history lives in each browser, so use Progress -> Export backup to move it between devices.

## Quiz marking & clearing answers
- Every quiz (dashboards and the mixed quiz) has a **Clear answer** control (click a chosen option again to deselect; skipped = unanswered).
- Before starting, a **marking scheme** panel sets marks for correct / incorrect / unanswered (default +2 / −1 / 0). It is saved in the browser (`hub.marking`) and shown on result screens and the Progress history. BAMAT101 (self-graded) is exempt.
- Marking is injected by the hub, so it only appears when dashboards are served through the hub.

## Accounts (optional, Google sign-in via Supabase)
The app is anonymous by default (data in localStorage). To enable accounts you **do** need a free Supabase project (it provides Google OAuth + Postgres):
1. Create a project at supabase.com. In *SQL editor*, run `supabase/schema.sql` (tables + row-level security).
2. *Authentication → Providers → Google*: enable it with a Google Cloud OAuth client (Web). Put Supabase's callback URL in Google's "Authorized redirect URIs".
3. *Authentication → URL configuration*: set Site URL to your Render URL and add it to Redirect URLs.
4. On Render set env vars `SUPABASE_URL` and `SUPABASE_ANON_KEY` (the public anon key; safe in the browser because RLS limits each user to their own rows).
Without these, the Account page says sign-in isn't configured and nothing else changes. Free-tier Supabase projects pause after inactivity.

## Common reader (experimental)
`reader.py` → `CommonReader` reads each dashboard's notes pages in-process (via the test client, using `note_pattern` in `subjects.py`) and builds one normalised outline: course → modules → topics → subtopics, with reading time. Views: `/c` (library), `/c/<slug>` (common dashboard), `/api/common/<slug>.json`. A new subject needs only a `subjects.py` entry. Quality depends on each dashboard's headings; repeated box labels are filtered.
