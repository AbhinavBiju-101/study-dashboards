"""Study Dashboards: a parent site that lists every study dashboard, adds cross-subject features
(search, mixed quiz, progress) and mounts each dashboard under its own URL prefix
(/evs, /be, /baeng101, /phy) inside ONE web service.

Why one service?  Render gives each web service a single public port, so the dashboards that ran
on 4000/4001/4002/4005 locally are mounted side by side here.  Their own code still runs standalone.

Local:   python app.py            -> http://127.0.0.1:3000
Render:  gunicorn app:app
"""
import importlib.util
import json
import os
import re
import sys
import threading
from pathlib import Path

from flask import Flask, jsonify, redirect, render_template, request, send_from_directory
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from banks import build_bank
from search import NoteIndex
from subjects import SUBJECTS

ROOT = Path(__file__).resolve().parent
SECRET = os.environ.get("SECRET_KEY", "dev-only-change-me")

# Small additions made to every dashboard page when served through the hub (standalone runs are unaffected).
HUB_PILL = (
    '<a id="hub-home-pill" href="/" title="Back to all subjects" '
    'style="position:fixed;left:12px;bottom:12px;z-index:2147483000;display:flex;align-items:center;gap:6px;'
    'padding:7px 12px;border-radius:999px;background:#fff;color:#1c2420;border:1px solid #d9d3c2;'
    'font:600 12px/1 system-ui,sans-serif;text-decoration:none;box-shadow:0 2px 8px rgba(0,0,0,.15)">'
    '<span aria-hidden="true">&#8962;</span> All subjects</a>'
)
FAVICON = '<link rel="icon" type="image/svg+xml" href="/static/favicon.svg"><link rel="alternate icon" href="/favicon.ico">'
_BODY_END = re.compile(r"</body\s*>", re.I)
_HEAD_END = re.compile(r"</head\s*>", re.I)
_HAS_ICON = re.compile(r'rel=["\']?(?:shortcut )?icon', re.I)


def load_subapp(slug):
    """Import dashboards/<slug>-dashboard/app.py under a unique module name and return its Flask app."""
    path = ROOT / "dashboards" / f"{slug}-dashboard" / "app.py"
    spec = importlib.util.spec_from_file_location(f"dash_{slug}", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    sub = mod.app

    # One origin now hosts every dashboard: keep their cookies/secrets apart.
    sub.secret_key = f"{SECRET}:{slug}"
    sub.config["SESSION_COOKIE_NAME"] = f"session_{slug}"
    sub.config["SESSION_COOKIE_PATH"] = f"/{slug}"

    @sub.after_request
    def decorate(resp):
        if (request.headers.get("X-Hub-Index") or resp.mimetype != "text/html" or resp.direct_passthrough
                or resp.status_code != 200 or "attachment" in resp.headers.get("Content-Disposition", "")):
            return resp
        page = resp.get_data(as_text=True)
        if "hub-home-pill" in page:
            return resp
        if not _HAS_ICON.search(page):
            page = _HEAD_END.sub(lambda m: FAVICON + m.group(0), page, count=1)
        tail = HUB_PILL
        if request.path == "/quiz/start" or "hubRecord(" in page:  # quiz result screens call hubRecord() to save progress here
            tail += ('<script src="/static/hub-store.js"></script>'
                     f'<script src="/static/hub-record.js" data-slug="{slug}"></script>')
        resp.set_data(_BODY_END.sub(lambda m: tail + m.group(0), page, count=1))
        return resp

    return sub


hub = Flask(__name__)
hub.config["TEMPLATES_AUTO_RELOAD"] = bool(os.environ.get("HUB_DEBUG"))

SUBAPPS = {}
for _s in SUBJECTS:
    SUBAPPS[_s["slug"]] = load_subapp(_s["slug"])

INDEX = NoteIndex(SUBAPPS, SUBJECTS)
threading.Thread(target=INDEX.ensure, daemon=True).start()  # warm the search index in the background

_bank_cache = {}


def bank():
    if "b" not in _bank_cache:
        _bank_cache["b"] = build_bank(SUBJECTS)
    return _bank_cache["b"]


def subject_cards():
    INDEX.ensure()
    counts = {s["slug"]: 0 for s in SUBJECTS}
    for q in bank()["questions"]:
        counts[q["s"]] += 1
    cards = []
    for s in SUBJECTS:
        c = dict(s)
        c["questions"] = counts[s["slug"]]
        c["pages"] = INDEX.pages.get(s["slug"], [])
        c["units"] = len(c["pages"])
        cards.append(c)
    return cards


@hub.context_processor
def shared():
    public = {s["slug"]: {"code": s["code"], "title": s["title"], "accent": s["accent"]} for s in SUBJECTS}
    return {"subjects_json": json.dumps(public), "nav": [
        ("home", "/", "Home"), ("subjects", "/subjects", "Subjects"), ("quiz", "/quiz", "Mixed quiz"),
        ("progress", "/progress", "Progress"), ("search", "/search", "Search")]}


def page(template, active, **ctx):
    return render_template(template, active=active, **ctx)


@hub.route("/")
def home():
    cards = subject_cards()
    return page("home.html", "home", subjects=cards, total_q=sum(c["questions"] for c in cards))


@hub.route("/subjects")
def subjects():
    return page("subjects.html", "subjects", subjects=subject_cards())


@hub.route("/quiz")
def quiz():
    return page("quiz.html", "quiz")


@hub.route("/progress")
def progress():
    return page("progress.html", "progress")


@hub.route("/search")
def search():
    return page("search.html", "search", q=request.args.get("q", ""), subject=request.args.get("subject", ""))


@hub.route("/api/bank")
def api_bank():
    resp = jsonify(bank())
    resp.headers["Cache-Control"] = "public, max-age=300"
    return resp


@hub.route("/api/search")
def api_search():
    q = request.args.get("q", "").strip()[:100]
    subject = request.args.get("subject") or None
    if subject and subject not in SUBAPPS:
        subject = None
    return jsonify(INDEX.search(q, subject))


@hub.route("/healthz")
def healthz():
    return "ok"


@hub.route("/favicon.ico")
def favicon_ico():
    return send_from_directory(hub.static_folder, "favicon.ico", mimetype="image/x-icon")


@hub.errorhandler(404)
def not_found(_):
    return page("404.html", "", ), 404


def _make_redirect(slug):
    # /evs -> /evs/ so relative navigation and the dispatcher both behave.
    hub.add_url_rule(f"/{slug}", endpoint=f"redir_{slug}", view_func=lambda: redirect(f"/{slug}/", 308))


for _slug in SUBAPPS:
    _make_redirect(_slug)

# Dispatcher strips the prefix and sets SCRIPT_NAME, so every url_for() in the dashboards keeps working.
app = DispatcherMiddleware(hub, {f"/{slug}": sub for slug, sub in SUBAPPS.items()})

if __name__ == "__main__":
    from werkzeug.serving import run_simple

    run_simple("127.0.0.1", int(os.environ.get("PORT", 3000)), app, use_reloader=False, threaded=True)
