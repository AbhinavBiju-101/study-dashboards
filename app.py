"""Study Hub: a parent site that lists every study dashboard and mounts each one
under its own URL prefix (/evs, /be, /baeng101, /phy) inside ONE web service.

Why one service?  Render gives each web service a single public port, so the
dashboards that ran on 4000/4001/4002/4005 locally are mounted side by side here
instead.  The dashboards' own code is untouched and still runs standalone.

Local:   python app.py            -> http://127.0.0.1:3000
Render:  gunicorn app:app
"""
import importlib.util
import json
import os
import re
import sys
from pathlib import Path

from flask import Flask, redirect, render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from subjects import SUBJECTS

ROOT = Path(__file__).resolve().parent
SECRET = os.environ.get("SECRET_KEY", "dev-only-change-me")

# "Back to hub" pill injected into every dashboard page (hub only; standalone runs are unaffected).
HUB_PILL = (
    '<a id="hub-home-pill" href="/" title="Back to all subjects" '
    'style="position:fixed;left:12px;bottom:12px;z-index:2147483000;display:flex;align-items:center;gap:6px;'
    'padding:7px 12px;border-radius:999px;background:rgba(30,42,34,.88);color:#fff;font:600 12px/1 system-ui,sans-serif;'
    'text-decoration:none;box-shadow:0 2px 8px rgba(0,0,0,.25);backdrop-filter:blur(4px)">'
    '<span aria-hidden="true">&#8962;</span> All subjects</a>'
)
_BODY_END = re.compile(r"</body\s*>", re.I)


def count_questions(node):
    """Count MCQs in any of the quiz_bank.json layouts (nested dicts/lists of {options, answer})."""
    if isinstance(node, dict):
        if "options" in node and "answer" in node:
            return 1
        return sum(count_questions(v) for v in node.values())
    if isinstance(node, list):
        return sum(count_questions(v) for v in node)
    return 0


def load_subapp(slug):
    """Import dashboards/<slug>/app.py under a unique module name and return its Flask app."""
    path = ROOT / "dashboards" / slug / "app.py"
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
    def add_hub_pill(resp):
        if (resp.mimetype == "text/html" and not resp.direct_passthrough
                and resp.status_code == 200 and "attachment" not in resp.headers.get("Content-Disposition", "")):
            html = resp.get_data(as_text=True)
            if "hub-home-pill" not in html:
                html = _BODY_END.sub(lambda m: HUB_PILL + m.group(0), html, count=1)
                resp.set_data(html)
        return resp

    return sub


hub = Flask(__name__)


def subject_cards():
    cards = []
    for s in SUBJECTS:
        card = dict(s)
        try:
            bank = json.loads((ROOT / "dashboards" / s["slug"] / "data" / "quiz_bank.json").read_text("utf-8"))
            card["questions"] = count_questions(bank)
        except (OSError, ValueError):
            card["questions"] = 0
        cards.append(card)
    return cards


@hub.route("/")
def index():
    cards = subject_cards()
    return render_template("index.html", subjects=cards, total_q=sum(c["questions"] for c in cards))


@hub.route("/healthz")
def healthz():
    return "ok"


def _make_redirect(slug):
    # /evs -> /evs/ so relative navigation and the dispatcher both behave.
    hub.add_url_rule(f"/{slug}", endpoint=f"redir_{slug}", view_func=lambda: redirect(f"/{slug}/", 308))


mounts = {}
for s in SUBJECTS:
    mounts[f"/{s['slug']}"] = load_subapp(s["slug"])
    _make_redirect(s["slug"])

# Dispatcher strips the prefix and sets SCRIPT_NAME, so every url_for() in the dashboards keeps working.
app = DispatcherMiddleware(hub, mounts)

if __name__ == "__main__":
    from werkzeug.serving import run_simple

    run_simple("127.0.0.1", int(os.environ.get("PORT", 3000)), app, use_reloader=False, threaded=True)
