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
app.py            hub + mounts each dashboard (DispatcherMiddleware)
subjects.py       the registry: one entry per subject (card text, colour)
templates/ static/  landing page
dashboards/<slug>-dashboard/  your Flask projects, unchanged (evs-dashboard, be-dashboard, ...)
render.yaml       Render blueprint
```

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
Today quiz results live only in the browser. When ready, add a `POST /api/results` endpoint in `app.py`
(Supabase client + `SUPABASE_URL` / `SUPABASE_KEY` as Render env vars) and have each dashboard's results screen
post `{subject, subtopic, level, correct, time}` to it. A hub-level progress view can then read it back.
