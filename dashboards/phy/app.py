"""QM Illustrated Notes: Flask study dashboard (Modules 2-4 of BAPHY105)."""
import json, math, random, pathlib
from flask import Flask, render_template, request, abort, jsonify

BASE = pathlib.Path(__file__).resolve().parent
app = Flask(__name__)


def load_json(name):
    with open(BASE / "data" / name, encoding="utf-8") as f:
        return json.load(f)


def syllabus():
    return load_json("syllabus.json")["modules"]


def quiz_bank():
    try:
        return load_json("quiz_bank.json")
    except FileNotFoundError:
        return {"status": "missing", "questions": []}


@app.context_processor
def inject():
    return dict(modules=syllabus())


# ---------- diagram helpers (computed, so the curves match the formulas in the text) ----------
def wave_svg(n, kind="psi", w=300, h=120):
    """Polyline for psi_n or |psi_n|^2 of the 1D box, in units where L = 1 and A = sqrt(2)."""
    pts = []
    N = 120
    for i in range(N + 1):
        x = i / N
        s = math.sin(n * math.pi * x)
        y = s if kind == "psi" else s * s
        if kind == "psi":
            py = h / 2 - y * (h / 2 - 12)
        else:
            py = h - 10 - y * (h - 26)
        pts.append(f"{10 + x * (w - 20):.1f},{py:.1f}")
    return " ".join(pts)


app.jinja_env.globals["wave_svg"] = wave_svg

# ---------- tunnelling helpers (computed so the figure and the numbers come from the same equations) ----------
_H = 6.626e-34; _HB = _H / (2 * math.pi); _ME = 9.109e-31; _EV = 1.602e-19


def tunnel_T(E_eV, V0_eV, L_nm):
    """Rectangular barrier, electron, E < V0. Returns kappa, k1 (1/m), exact T, the slide-12 formula and e^(-2 kappa L)."""
    L = L_nm * 1e-9
    kap = math.sqrt(2 * _ME * (V0_eV - E_eV) * _EV) / _HB
    k1 = math.sqrt(2 * _ME * E_eV * _EV) / _HB
    exact = 1 / (1 + V0_eV ** 2 * math.sinh(kap * L) ** 2 / (4 * E_eV * (V0_eV - E_eV)))
    s12 = 16 * (E_eV / V0_eV) * (1 - E_eV / V0_eV) * math.exp(-2 * kap * L)
    return dict(kappa=kap, k1=k1, exact=exact, s12=s12, approx=math.exp(-2 * kap * L), s7=16 / (4 + (kap / k1) ** 2) * math.exp(-2 * kap * L))


def _solve(M, b):
    n = len(b); A = [row[:] + [b[i]] for i, row in enumerate(M)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(A[r][c])); A[c], A[piv] = A[piv], A[c]
        for r in range(n):
            if r != c:
                f = A[r][c] / A[c][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [A[i][n] / A[i][i] for i in range(n)]


def barrier_wave(E=2.0, V0=5.0, L=1.0, w=620, h=210):
    """Solve the three-region barrier problem in units hbar^2/2m = 1 (k = sqrt(E), kappa = sqrt(V0-E)) with unit incident amplitude.
    Returns an SVG polyline for Re(psi), plus R and T."""
    k = math.sqrt(E); kap = math.sqrt(V0 - E); eL = math.exp(kap * L); ikL = complex(math.cos(k * L), math.sin(k * L))
    # unknowns B, C, D, F:  1+B = C+D ;  ik(1-B) = kap(C-D) ;  C e^{kL}+D e^{-kL} = F e^{ikL} ;  kap(C e^{kL}-D e^{-kL}) = ik F e^{ikL}
    M = [[-1, 1, 1, 0], [1j * k, kap, -kap, 0], [0, eL, 1 / eL, -ikL], [0, kap * eL, -kap / eL, -1j * k * ikL]]
    b = [1, 1j * k, 0, 0]
    B, C, D, F = _solve([[complex(x) for x in r] for r in M], [complex(x) for x in b])
    R = abs(B) ** 2; T = abs(F) ** 2
    span = 4.5; x0, x1 = -span, L + span
    def psi(x):
        if x < 0: return complex(math.cos(k * x), math.sin(k * x)) + B * complex(math.cos(k * x), -math.sin(k * x))
        if x <= L: return C * math.exp(kap * x) + D * math.exp(-kap * x)
        return F * complex(math.cos(k * x), math.sin(k * x))
    N = 600; pts = []
    for i in range(N + 1):
        x = x0 + (x1 - x0) * i / N
        X = 15 + (x - x0) / (x1 - x0) * (w - 30); Y = h / 2 - psi(x).real * 40
        pts.append(f"{X:.1f},{Y:.1f}")
    X0 = 15 + (0 - x0) / (x1 - x0) * (w - 30); X1 = 15 + (L - x0) / (x1 - x0) * (w - 30)
    return dict(pts=" ".join(pts), R=R, T=T, x_left=X0, x_right=X1, k=k, kappa=kap)


app.jinja_env.globals["tunnel_T"] = tunnel_T
app.jinja_env.globals["barrier_wave"] = barrier_wave

# ---- Module 1 computed figures ----
_K = 1.381e-23; _C = 2.998e8

def _planck_lam(lam_nm, T):
    lam = lam_nm * 1e-9
    x = _H * _C / (lam * _K * T)
    return 8 * math.pi * _H * _C / lam ** 5 / math.expm1(x) if x < 600 else 0.0

def _rj_lam(lam_nm, T):
    lam = lam_nm * 1e-9
    return 8 * math.pi * _K * T / lam ** 4

def planck_plot(temps=(3000, 4000, 5000), rj_T=5000, w=560, h=300):
    """SVG of Planck spectra and the Rayleigh-Jeans curve for rj_T, wavelength 100-3000 nm."""
    lmin, lmax = 100.0, 3000.0
    ymax = max(_planck_lam(l, max(temps)) for l in range(100, 3000, 10)) * 1.15
    ox, oy, pw, ph = 50, 20, w - 70, h - 60
    def pt(l, v):
        return "%.1f,%.1f" % (ox + (l - lmin) / (lmax - lmin) * pw, oy + ph - min(v / ymax, 1.0) * ph)
    out = ['<svg viewBox="0 0 %d %d" width="%d" role="img" aria-label="Blackbody spectra and Rayleigh-Jeans curve">' % (w, h, w)]
    out.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#555"/><line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#555"/>' % (ox, oy, ox, oy + ph, ox, oy + ph, ox + pw, oy + ph))
    out.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="#fde68a" fill-opacity=".35"/>' % (ox + (400 - lmin) / (lmax - lmin) * pw, oy, 300 / (lmax - lmin) * pw, ph))
    cols = ["#0f766e", "#6d28d9", "#c0392b"]
    for i, T in enumerate(temps):
        pts = " ".join(pt(l, _planck_lam(l, T)) for l in range(100, 3001, 20))
        out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2"/>' % (pts, cols[i % 3]))
        lp = 2.898e-3 / T * 1e9
        out.append('<text x="%.1f" y="%.1f" font-size="12" fill="%s">%d K</text>' % (ox + (lp - lmin) / (lmax - lmin) * pw + 6, oy + ph - min(_planck_lam(lp, T) / ymax, 1) * ph + 4, cols[i % 3], T))
    pts = " ".join(pt(l, _rj_lam(l, rj_T)) for l in range(100, 3001, 20))
    out.append('<polyline points="%s" fill="none" stroke="#333" stroke-dasharray="6 4" stroke-width="1.8"/>' % pts)
    out.append('<text x="%d" y="%d" font-size="12">Rayleigh-Jeans, %d K (classical)</text>' % (ox + 12, oy + 14, rj_T))
    out.append('<text x="%d" y="%d" font-size="12">wavelength (nm)</text><text x="%d" y="%d" font-size="11">100</text><text x="%d" y="%d" font-size="11">1000</text><text x="%d" y="%d" font-size="11">2000</text><text x="%d" y="%d" font-size="11">3000</text>' % (ox + pw // 2 - 40, h - 8, ox - 6, h - 30, ox + (900 / 2900) * pw - 10, h - 30, ox + (1900 / 2900) * pw - 10, h - 30, ox + pw - 22, h - 30))
    out.append('<text x="%d" y="%d" font-size="11" transform="rotate(-90 14 %d)">spectral radiance (relative)</text></svg>' % (14, oy + ph - 20, oy + ph - 20))
    return "".join(out)

def wavepacket(n=15, spread=0.6, w=560, h=160, carrier=12.0):
    """Polyline of a Gaussian-weighted sum of cosines (a wave packet) plus its envelope."""
    xs = [i * 0.02 - 6 for i in range(0, 601)]
    ks = [carrier + spread * (j - n // 2) * 0.2 for j in range(n)]
    ws = [math.exp(-((k - carrier) / (spread * 0.9)) ** 2) for k in ks]
    def y(x): return sum(wt * math.cos(k * x) for wt, k in zip(ws, ks))
    ys = [y(x) for x in xs]; m = max(abs(v) for v in ys)
    pts = " ".join("%.1f,%.1f" % (10 + (x + 6) / 12 * (w - 20), h / 2 - v / m * (h / 2 - 12)) for x, v in zip(xs, ys))
    env = [sum(ws) * math.exp(-((x * spread * 0.2 * 0.9) ** 2) * 0.0) for x in xs]
    return '<svg viewBox="0 0 %d %d" width="%d" role="img" aria-label="Wave packet"><line x1="10" y1="%d" x2="%d" y2="%d" stroke="#bbb"/><polyline points="%s" fill="none" stroke="#6d28d9" stroke-width="1.6"/></svg>' % (w, h, w, h // 2, w - 10, h // 2, pts)

app.jinja_env.globals["planck_plot"] = planck_plot
app.jinja_env.globals["wavepacket"] = wavepacket



# ---------- pages ----------
@app.route("/")
def dashboard():
    mods = syllabus()
    n_topics = sum(len(m["topics"]) for m in mods)
    n_subs = sum(len(t["subtopics"]) for m in mods for t in m["topics"])
    return render_template("index.html", page="dash", n_topics=n_topics, n_subs=n_subs, counts=_tree(quiz_bank()),
                           n_questions=len(quiz_bank()["questions"]))


@app.route("/module/<int:n>")
def module(n):
    mods = syllabus()
    cur = next((m for m in mods if m["n"] == n), None)
    if cur is None:
        abort(404)
    i = mods.index(cur)
    prev_m = mods[i - 1] if i > 0 else None
    next_m = mods[i + 1] if i < len(mods) - 1 else None
    return render_template(f"module{n}.html", page="mod", n=n, cur=cur, prev_m=prev_m, next_m=next_m)


@app.route("/recap")
def recap():
    return render_template("recap.html", page="recap")


# ---------- quiz ----------
def _tree(bank):
    counts = {}
    for q in bank["questions"]:
        for key in (q["module"], q["topic"], q["subtopic"]):
            counts[key] = counts.get(key, 0) + 1
    return counts


@app.route("/quiz")
def quiz_setup():
    bank = quiz_bank()
    blooms = sorted({q.get("bloom", "Unspecified") for q in bank["questions"]})
    return render_template("quiz_setup.html", page="quiz", bank_status=bank.get("status", "ok"),
                           bank_note=bank.get("note", ""), total=len(bank["questions"]),
                           counts=_tree(bank), blooms=blooms,
                           questions_meta=[dict(id=q["id"], module=q["module"], topic=q["topic"],
                                                subtopic=q["subtopic"], bloom=q.get("bloom", "Unspecified"))
                                           for q in bank["questions"]])


@app.route("/quiz/start", methods=["POST"])
def quiz_start():
    bank = quiz_bank()
    subs = set(request.form.getlist("sub"))          # subtopic ids ticked on the setup page
    blooms = set(request.form.getlist("bloom"))
    allow_back = request.form.get("allow_back") == "on"
    pool = [q for q in bank["questions"]
            if (not subs or q["subtopic"] in subs) and (not blooms or q.get("bloom", "Unspecified") in blooms)]
    try:
        want = int(request.form.get("count", "10"))
    except ValueError:
        want = 10
    want = max(1, min(want, len(pool))) if pool else 0
    chosen = random.sample(pool, want) if want else []
    out = []
    for q in chosen:
        order = list(range(len(q["options"])))
        random.shuffle(order)                        # new option order for this attempt
        out.append(dict(id=q["id"], module=q["module"], topic=q["topic"], subtopic=q["subtopic"],
                        bloom=q.get("bloom", "Unspecified"), question=q["question"],
                        options=[q["options"][j] for j in order],
                        answer=order.index(q["answer"]),   # answer index remapped to the shuffled order
                        explanation=q.get("explanation", "")))
    return render_template("quiz_run.html", page="quiz", questions=out, allow_back=allow_back,
                           empty=(len(out) == 0))


if __name__ == "__main__":
    app.run(port=4005, debug=True)
