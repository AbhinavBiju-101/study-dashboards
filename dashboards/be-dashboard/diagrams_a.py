"""Diagrams for Module 1 additions (machines, power electronics, safety) and Module 2 (electronics)."""
import math
from diagrams import *
from diagrams import _g, _frame, _label, _polar, _DIR

LIGHT = "#eef0f4"


# ------------------------------------------------------------ extra primitives
def rect(x, y, w, h, fill="none", stroke=INK, sw=2, rx=0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def box(x, y, w, h, label, fill=LIGHT, stroke=INK, size=13, c=INK, weight=None):
    lines = label.split("\n")
    out = rect(x, y, w, h, fill, stroke, 1.8, 6)
    y0 = y + h / 2 - (len(lines) - 1) * 8 + 4.5
    for i, l in enumerate(lines):
        out += text(x + w / 2, y0 + i * 16, l, "middle", c, size, weight)
    return out


def pfill(pts, fill, stroke=INK, sw=1.6):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'


def gnd(x, y):
    return line(x, y, x, y + 8) + line(x - 10, y + 8, x + 10, y + 8) + line(x - 6, y + 13, x + 6, y + 13) + line(x - 2, y + 18, x + 2, y + 18)


def _lbl(out, mx, my, label, side, off=20):
    if label:
        out += _label(mx, my, label, side, off)
    return out


def diode(x1, y1, x2, y2, label=None, side="top"):
    L, ang, mx, my, ux, uy = _frame(x1, y1, x2, y2)
    inner = (f'<line x1="{-L/2:.1f}" y1="0" x2="-10" y2="0"/><line x1="10" y1="0" x2="{L/2:.1f}" y2="0"/>'
             f'<polygon points="-10,-11 -10,11 10,0" fill="{INK}"/><line x1="10" y1="-11" x2="10" y2="11"/>')
    return _lbl(_g(mx, my, ang, inner), mx, my, label, side, 22)


def zener(x1, y1, x2, y2, label=None, side="right"):
    L, ang, mx, my, ux, uy = _frame(x1, y1, x2, y2)
    inner = (f'<line x1="{-L/2:.1f}" y1="0" x2="-10" y2="0"/><line x1="10" y1="0" x2="{L/2:.1f}" y2="0"/>'
             f'<polygon points="-10,-11 -10,11 10,0" fill="{INK}"/><path d="M16,-15 L10,-11 L10,11 L4,15"/>')
    return _lbl(_g(mx, my, ang, inner), mx, my, label, side, 24)


def cap(x1, y1, x2, y2, label=None, side="right"):
    L, ang, mx, my, ux, uy = _frame(x1, y1, x2, y2)
    inner = (f'<line x1="{-L/2:.1f}" y1="0" x2="-5" y2="0"/><line x1="5" y1="0" x2="{L/2:.1f}" y2="0"/>'
             '<line x1="-5" y1="-13" x2="-5" y2="13" stroke-width="3"/><line x1="5" y1="-13" x2="5" y2="13" stroke-width="3"/>')
    return _lbl(_g(mx, my, ang, inner), mx, my, label, side, 20)


def switch(x1, y1, x2, y2, label=None, side="right"):
    L, ang, mx, my, ux, uy = _frame(x1, y1, x2, y2)
    inner = (f'<line x1="{-L/2:.1f}" y1="0" x2="-12" y2="0"/><line x1="12" y1="0" x2="{L/2:.1f}" y2="0"/>'
             '<line x1="-12" y1="0" x2="9" y2="-15"/><circle cx="-12" cy="0" r="2.5" fill="#1b1f24"/><circle cx="12" cy="0" r="2.5" fill="#1b1f24"/>')
    return _lbl(_g(mx, my, ang, inner), mx, my, label, side, 20)


def opamp(cx, cy):
    b = pfill([(cx - 40, cy - 45), (cx - 40, cy + 45), (cx + 50, cy)], "#fff", INK, 2)
    b += text(cx - 31, cy - 17, "−", "middle", INK, 16, "bold") + text(cx - 31, cy + 27, "+", "middle", INK, 16, "bold")
    return b


def person(x, gy, c=INK):
    b = f'<circle cx="{x}" cy="{gy-74}" r="10" fill="none" stroke="{c}" stroke-width="2"/>'
    b += line(x, gy - 64, x, gy - 30, c, 2.4) + line(x, gy - 30, x - 9, gy, c, 2.4) + line(x, gy - 30, x + 9, gy, c, 2.4)
    return b


def bjt(cx, cy, kind="npn"):
    s = -1 if kind == "npn" else 1   # collector side: npn top (-1), pnp bottom (+1)
    b = line(cx - 45, cy, cx, cy) + line(cx, cy - 20, cx, cy + 20, INK, 4)
    b += line(cx, cy + s * 8, cx + 30, cy + s * 30) + line(cx + 30, cy + s * 30, cx + 30, cy + s * 50)   # collector
    b += line(cx, cy - s * 8, cx + 30, cy - s * 30) + line(cx + 30, cy - s * 30, cx + 30, cy - s * 50)   # emitter
    ex, ey = 30, -s * 22
    n = math.hypot(ex, ey)
    ux, uy = ex / n, ey / n
    if kind == "npn":
        b += head(cx + 0.86 * 30, cy - s * 8 + 0.86 * ey, ux, uy, INK, 10)
    else:
        b += head(cx + 0.2 * 30, cy - s * 8 + 0.2 * ey, -ux, -uy, INK, 10)
    return b


# ------------------------------------------------------------ Module 1 additions
def d_cap_start():
    b = line(110, 40, 410, 40) + line(110, 170, 410, 170) + acsrc(110, 170, 110, 40, "1-φ supply", "left")
    b += ind(270, 40, 270, 170, "Main winding", "left")
    b += line(410, 40, 410, 50) + cap(410, 50, 410, 82, "Cₛ (starting capacitor)", "right")
    b += switch(410, 82, 410, 112, "centrifugal switch", "right") + ind(410, 112, 410, 170, None)
    b += text(422, 150, "Aux. winding", "start", INK, 13)
    b += f'<circle cx="340" cy="105" r="26" fill="#f7f8fb" stroke="{INK}" stroke-width="2"/>' + text(340, 109, "Rotor", "middle", INK, 13, "bold")
    b += dot(270, 40) + dot(410, 40) + dot(270, 170) + dot(410, 170)
    return wrap(svg(640, 200, b), "Capacitor-start motor: the auxiliary winding (90° from the main winding in space) is fed through a capacitor, so its current leads the main winding's and the two together make a rotating field. A centrifugal switch cuts the auxiliary branch out at about 70–80% of synchronous speed.")


def _bldc_snap(cx, cy, mode, a, b_):
    ax = {"U": (0, -1), "V": (-math.cos(math.radians(30)), 0.5), "W": (math.cos(math.radians(30)), 0.5)}
    v = (ax[b_][0] - ax[a][0], ax[b_][1] - ax[a][1])
    n = math.hypot(*v)
    v = (v[0] / n, v[1] / n)
    s = f'<circle cx="{cx}" cy="{cy}" r="52" fill="#f7f8fb" stroke="{INK}" stroke-width="2"/>'
    for k, (p, pos) in enumerate((("U", (0, -1)), ("V", ax["V"]), ("W", ax["W"]))):
        x, y = cx + pos[0] * 52, cy + pos[1] * 52
        on = p in (a, b_)
        s += rect(x - 9, y - 9, 18, 18, "#f5d0cb" if p == a else ("#cfe3f7" if on else "#fff"), RED if p == a else (BLUE if on else INK), 2, 3)
        s += text(cx + pos[0] * 72, cy + pos[1] * 72 + 5, p, "middle", INK, 14, "bold")
    s += arrow(cx - v[0] * 26, cy - v[1] * 26, cx + v[0] * 38, cy + v[1] * 38, GREEN, 3, 11)
    s += f'<circle cx="{cx}" cy="{cy}" r="13" fill="{BLUE}" stroke="{INK}" stroke-width="1.5"/>'
    s += f'<circle cx="{cx + v[0]*7:.1f}" cy="{cy + v[1]*7:.1f}" r="6" fill="{RED}"/>'
    s += text(cx, cy + 96, f"Mode {mode}: {a} → {b_}", "middle", INK, 13, "bold")
    return s


def d_bldc():
    modes = [(1, "U", "W"), (2, "U", "V"), (3, "W", "V"), (4, "W", "U"), (5, "V", "U"), (6, "V", "W")]
    b = ""
    for i, (m, a, c) in enumerate(modes):
        b += _bldc_snap(100 + (i % 3) * 210, 100 + (i // 3) * 205, m, a, c)
    b += text(330, 12, "red coil = current enters, blue coil = current leaves, green arrow = resultant stator flux, red/blue disc = permanent-magnet rotor (red = N)", "middle", GREY, 11)
    return wrap(svg(660, 420, b), "Six-step commutation of a three-coil BLDC motor. Each step energises two coils, the stator flux jumps 60°, and the permanent-magnet rotor follows. Six steps = one electrical revolution.")


def d_stepper():
    b = ""
    steps = [("A  +", 0, -90), ("B  +", 90, 0), ("A  −", 180, 90), ("B  −", 270, 180)]
    pos = {"A": (0, -1), "B": (1, 0), "A′": (0, 1), "B′": (-1, 0)}
    names = ["A", "B", "A′", "B′"]
    for i, (lab, th, ang) in enumerate(steps):
        cx, cy = 90 + i * 170, 100
        b += f'<circle cx="{cx}" cy="{cy}" r="55" fill="#f7f8fb" stroke="{INK}" stroke-width="2"/>'
        for n in names:
            x, y = cx + pos[n][0] * 55, cy + pos[n][1] * 55
            on = (i == names.index(n))
            b += rect(x - 10, y - 10, 20, 20, "#f5d0cb" if on else "#fff", RED if on else INK, 2, 3)
            b += text(cx + pos[n][0] * 75, cy + pos[n][1] * 75 + 5, n, "middle", INK, 13, "bold")
        dx, dy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        b += f'<circle cx="{cx}" cy="{cy}" r="16" fill="#fff" stroke="{INK}" stroke-width="2"/>'
        b += arrow(cx - dx * 4, cy - dy * 4, cx + dx * 34, cy + dy * 34, PURP, 3, 11)
        b += text(cx, cy + 100, f"θ = {th}°", "middle", INK, 13, "bold") + text(cx, cy + 118, f"phase {lab} on", "middle", GREY, 12)
    return wrap(svg(700, 235, b), "A 2-phase, 2-pole permanent-magnet stepper: the rotor (arrow = its north pole) snaps to whichever stator pole is energised. Switching A → B → A′ → B′ turns it 90° per pulse.")


def d_alternator():
    cx, cy = 230, 150
    b = f'<circle cx="{cx}" cy="{cy}" r="120" fill="none" stroke="#9aa3b2" stroke-width="22"/>'
    cols = [RED, AMBER, BLUE]
    for k in range(12):
        x, y = _polar(cx, cy, 113, k * 30)
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{cols[k % 3]}" stroke="{INK}" stroke-width="1"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="82" fill="#fff" stroke="{INK}" stroke-width="1.5" stroke-dasharray="4,3"/>'
    b += rect(cx - 26, cy - 78, 52, 50, "#d7dce5", INK, 2) + text(cx, cy - 46, "N", "middle", RED, 20, "bold")
    b += rect(cx - 26, cy + 28, 52, 50, "#d7dce5", INK, 2) + text(cx, cy + 62, "S", "middle", BLUE, 20, "bold")
    b += rect(cx - 18, cy - 28, 36, 56, "#f1c9a5", "#b46b2d", 1.6) + text(cx, cy + 4, "field", "middle", INK, 12)
    b += arc_arrow(cx, cy, 46, -40, 40, PURP, 3)
    b += text(cx + 150, 40, "Stator (stationary):", "start", INK, 13, "bold") + text(cx + 150, 58, "3-phase armature winding", "start", INK, 13)
    b += text(cx + 150, 78, "(A red, B amber, C blue)", "start", GREY, 12)
    b += line(cx + 145, 52, cx + 100, 90, GREY, 1.2)
    b += text(cx + 150, 150, "Rotor (rotating):", "start", INK, 13, "bold") + text(cx + 150, 168, "DC field winding", "start", INK, 13) + text(cx + 150, 186, "via slip rings", "start", GREY, 12)
    b += line(cx + 145, 160, cx + 30, 150, GREY, 1.2)
    b += text(cx + 150, 250, "Prime mover turns the rotor", "start", PURP, 13, "bold")
    return wrap(svg(680, 290, b), "Alternator (synchronous generator): unlike a DC machine, the armature is stationary and the field rotates, so the output is taken straight from the stator terminals without brushes.")


def d_pe_block():
    b = box(10, 30, 150, 64, "Electrical energy\nsource (AC or DC)") + box(240, 30, 170, 64, "Power electronic\nconverter circuit") + box(490, 30, 140, 64, "Electrical\nload")
    b += arrow(160, 62, 238, 62, INK, 2) + arrow(410, 62, 488, 62, INK, 2)
    b += text(325, 20, "i, v", "middle", GREY, 12, None, True)
    b += box(490, 150, 140, 54, "Sensing unit\n(sensor)") + arrow(560, 94, 560, 148, INK, 2)
    b += box(240, 150, 170, 54, "Control circuit") + arrow(490, 177, 412, 177, INK, 2)
    b += arrow(325, 148, 325, 96, INK, 2) + text(335, 126, "control signals", "start", GREY, 12, None, True)
    b += arrow(325, 245, 325, 206, INK, 2) + text(325, 262, "Reference value", "middle", INK, 13)
    return wrap(svg(650, 275, b), "A power-electronic system: the converter shapes energy from the source for the load, while sensor and control circuit close a feedback loop around it.")


def d_converters():
    b = ""
    def ico(x, y, kind, c=PURP):
        s = line(x, y, x + 56, y, GREY, 1)
        if kind == "ac":
            s += poly(sine_pts(x, y, 56, 12, 0, 360, 0, 60), c, 2)
        elif kind == "dc":
            s += line(x, y - 12, x + 56, y - 12, c, 2.4)
        elif kind == "dc_low":
            s += line(x, y - 6, x + 56, y - 6, c, 2.4)
        elif kind == "acs":
            s += poly(sine_pts(x, y, 56, 6, 0, 360, 0, 60), c, 2)
        return s
    cells = [("Rectifier", "AC → DC", "ac", "dc", 20, 20), ("Inverter", "DC → AC", "dc", "ac", 380, 20),
             ("DC–DC converter (chopper)", "DC → DC (other level)", "dc", "dc_low", 20, 130), ("AC regulator / cycloconverter", "AC → AC (other V or f)", "ac", "acs", 380, 130)]
    for name, sub, i, o, x, y in cells:
        b += rect(x, y, 340, 98, "#fbfbfa", INK, 1.5, 8)
        b += text(x + 170, y + 22, name, "middle", INK, 14, "bold") + text(x + 170, y + 40, sub, "middle", GREY, 12)
        b += ico(x + 20, y + 76, i) + arrow(x + 90, y + 66, x + 120, y + 66, INK, 2, 8)
        b += box(x + 125, y + 50, 90, 32, "converter", "#f3effc", PURP, 12) + arrow(x + 218, y + 66, x + 248, y + 66, INK, 2, 8) + ico(x + 262, y + 76, o)
    return wrap(svg(740, 245, b), "The four basic converter families of power electronics, named by what goes in and what comes out.")


def d_drive_block():
    b = box(10, 40, 100, 56, "Power\nsource", "#cfe0f5") + box(160, 40, 110, 56, "Power\nconverter", "#d4e8d0") + box(320, 40, 90, 56, "Motor", "#2b2f3a", INK, 13, "#fff") + box(460, 40, 90, 56, "Load", "#e0c98a")
    b += arrow(110, 68, 158, 68, INK, 2) + arrow(270, 68, 318, 68, INK, 2) + arrow(410, 68, 458, 68, INK, 2)
    b += box(390, 150, 110, 52, "Sensing\nunit", "#d4dff0") + dot(435, 68, 4) + arrow(435, 68, 435, 148, INK, 2, 9)
    b += box(160, 150, 110, 52, "Control\nunit", "#e8cdb8") + arrow(388, 176, 272, 176, INK, 2) + arrow(215, 150, 215, 98, INK, 2)
    b += arrow(215, 240, 215, 204, INK, 2) + text(215, 256, "Input command (reference)", "middle", INK, 13)
    return wrap(svg(580, 270, b), "Block diagram of an electric drive: the control unit compares the command with sensed motor/load quantities and tells the converter what to deliver to the motor.")


def _panel_earth(x0, earthed):
    b = ""
    sx = x0 + 45
    b += text(x0 + 190, 20, "With earthing" if earthed else "Without earthing", "middle", INK, 14, "bold")
    b += rect(x0 + 10, 214, 360, 14, "#e8dcc8", "#b9a888", 1.2) + text(x0 + 360, 242, "earth", "end", GREY, 12)
    b += acsrc(sx, 150, sx, 70, None) + line(sx, 70, x0 + 150, 70, RED, 2.5) + line(sx, 150, x0 + 150, 150, INK, 2.5)
    b += line(sx, 150, sx, 214, INK, 2) + dot(sx, 150, 4)
    b += rect(x0 + 150, 45, 120, 115, "#f3f4f7", INK, 2.5) + text(x0 + 210, 38, "metal-cased appliance", "middle", GREY, 12)
    b += line(x0 + 150, 70, x0 + 205, 70, RED, 2.5) + line(x0 + 205, 70, x0 + 205, 84, RED, 2.5) + line(x0 + 150, 150, x0 + 205, 150, INK, 2.5) + line(x0 + 205, 150, x0 + 205, 138, INK, 2.5)
    b += rect(x0 + 180, 84, 50, 54, "#fff", INK, 1.5) + text(x0 + 205, 116, "load", "middle", INK, 12)
    b += line(x0 + 170, 70, x0 + 170, 45, RED, 2.2, "4,3") + dot(x0 + 170, 70, 3.5, RED) + text(x0 + 165, 62, "fault", "end", RED, 12, "bold")
    px = x0 + 335
    b += person(px, 214) + line(px, 172, x0 + 270, 118, INK, 2.4)
    if earthed:
        b += line(x0 + 235, 160, x0 + 235, 214, GREEN, 3) + text(x0 + 243, 192, "earth wire", "start", GREEN, 12, "bold")
        b += arrow(x0 + 235, 168, x0 + 235, 204, RED, 2.5, 9) + arrow(x0 + 232, 221, sx + 6, 221, RED, 2.5, 9)
        b += text(px + 2, 78, "≈ no current", "middle", GREEN, 12, "bold") + text(px + 2, 94, "→ safe", "middle", GREEN, 12, "bold")
        b += text(x0 + 224, 185, "big fault current:", "end", RED, 12) + text(x0 + 224, 200, "fuse / MCB trips", "end", RED, 12)
    else:
        b += arrow(x0 + 282, 128, x0 + 326, 160, RED, 2.5, 9) + arrow(px - 2, 176, px - 2, 204, RED, 2.5, 9) + arrow(px - 6, 221, sx + 6, 221, RED, 2.5, 9)
        b += text(px + 15, 78, "current flows", "middle", RED, 12, "bold") + text(px + 15, 94, "through the person", "middle", RED, 12, "bold")
    return b


def d_earthing():
    b = _panel_earth(0, False) + _panel_earth(400, True)
    return wrap(svg(780, 255, b), "A live wire touches the metal body. Left: the body becomes live and the person offers the only path to earth. Right: a low-resistance earth wire carries the fault current instead, and the protective device disconnects the supply.")


def d_current_zones():
    zones = [("1 mA", "tingling", "#f6e58d", INK), ("2–9 mA", "small shock", "#f2c94c", INK), ("10–24 mA", "muscles lock —\ncan't let go", "#f2994a", INK),
             ("25–74 mA", "breathing muscles\nparalysed,\nburns", "#eb5757", "#fff"), ("75–300 mA", "ventricular\nfibrillation,\nusually fatal", "#b32d2d", "#fff"), ("> 300 mA", "death almost\ncertain; severe\nburns", "#5c1a1a", "#fff")]
    b = text(350, 20, "AC current through the body  →  increasing severity", "middle", INK, 13, "bold")
    for i, (a, t, fill, tc) in enumerate(zones):
        x = 10 + i * 115
        b += rect(x, 36, 112, 112, fill, INK, 1.2, 4) + text(x + 56, 62, a, "middle", tc, 14, "bold")
        for k, l in enumerate(t.split("\n")):
            b += text(x + 56, 92 + k * 16, l, "middle", tc, 12)
    return wrap(svg(710, 165, b), "Effect of AC current on the human body (bands are not to scale). Currents of only tens of milliamperes through the chest are dangerous — far below what a fuse is designed to notice.")


# ------------------------------------------------------------ Module 2
def d_pn_junction():
    b = ""
    L, J1, J2, R = 60, 290, 390, 620
    b += rect(L, 40, J1 - L, 110, "#fde8e8", INK, 1.5) + rect(J1, 40, J2 - J1, 110, "#ececec", INK, 1.5) + rect(J2, 40, R - J2, 110, "#e3ecff", INK, 1.5)
    for r in range(3):
        for c in range(5):
            b += f'<circle cx="{L + 28 + c * 40}" cy="{65 + r * 38}" r="6" fill="#fff" stroke="{RED}" stroke-width="1.8"/>'
            b += f'<circle cx="{J2 + 28 + c * 40}" cy="{65 + r * 38}" r="6" fill="{BLUE}"/>'
        for c in range(2):
            b += text(J1 + 18 + c * 24, 71 + r * 38, "⊖", "middle", RED, 18) + text(J2 - 18 - c * 24, 71 + r * 38, "⊕", "middle", BLUE, 18)
    b += line(340, 40, 340, 150, INK, 1.5, "4,3")
    b += text((L + J1) / 2, 30, "P-type", "middle", RED, 14, "bold") + text((J2 + R) / 2, 30, "N-type", "middle", BLUE, 14, "bold") + text(340, 30, "depletion region", "middle", INK, 13, "bold")
    b += text(L, 168, "○ holes (majority)", "start", RED, 12) + text(R, 168, "● electrons (majority)", "end", BLUE, 12)
    b += arrow(380, 172, 300, 172, PURP, 2.5, 9) + text(340, 190, "built-in E-field (N → P)", "middle", PURP, 12, "bold")
    b += line(L, 270, R, 270, INK, 1.2) + line(L, 215, L, 270, INK, 1.2) + text(L + 6, 212, "potential", "start", INK, 12)
    b += f'<path d="M{L},268 L{J1 - 6},268 C{J1+40},268 {J1+30},232 340,232 C{J2-30},232 {J2-40},232 {J2+6},232 L{R},232" fill="none" stroke="{PURP}" stroke-width="2.6"/>'
    b += text(340, 292, "barrier V₀ ≈ 0.7 V (Si), 0.3 V (Ge)", "middle", PURP, 13, "bold")
    return wrap(svg(680, 305, b), "A PN junction at equilibrium: diffusion leaves fixed negative ions on the P side and fixed positive ions on the N side. The resulting field (and potential barrier) stops further diffusion.")


def d_pn_bias():
    def panel(x0, fwd):
        b = text(x0 + 150, 18, "Forward bias" if fwd else "Reverse bias", "middle", INK, 14, "bold")
        dw = 24 if fwd else 70
        L, R = x0 + 20, x0 + 280
        J = (L + R) / 2
        b += rect(L, 36, J - dw / 2 - L, 64, "#fde8e8", INK, 1.5) + rect(J - dw / 2, 36, dw, 64, "#ececec", INK, 1.5) + rect(J + dw / 2, 36, R - J - dw / 2, 64, "#e3ecff", INK, 1.5)
        b += text((L + J) / 2 - dw / 4, 74, "P", "middle", RED, 20, "bold") + text((R + J) / 2 + dw / 4, 74, "N", "middle", BLUE, 20, "bold")
        b += text(J, 114, "depletion layer " + ("narrow" if fwd else "wide"), "middle", GREY, 12)
        b += line(L, 68, L - 14, 68) + line(L - 14, 68, L - 14, 170) + line(R, 68, R + 14, 68) + line(R + 14, 68, R + 14, 170) + line(L - 14, 170, R + 14, 170)
        bx = (L + R) / 2
        if fwd:
            b += line(bx - 8, 154, bx - 8, 186, INK, 4) + line(bx + 8, 160, bx + 8, 180, INK, 4)
        else:
            b += line(bx - 8, 160, bx - 8, 180, INK, 4) + line(bx + 8, 154, bx + 8, 186, INK, 4)
        if fwd:
            b += text(bx - 22, 160, "+", "end", INK, 15, "bold") + text(bx + 22, 160, "−", "start", INK, 15, "bold")
            b += arrow(x0 + 60, 195, x0 + 240, 195, GREEN, 2.5, 10) + text(bx, 214, "large current", "middle", GREEN, 13, "bold")
        else:
            b += text(bx - 22, 160, "−", "end", INK, 15, "bold") + text(bx + 22, 160, "+", "start", INK, 15, "bold")
            b += text(bx, 214, "almost no current (leakage)", "middle", RED, 13, "bold")
        return b
    b = panel(0, True) + panel(340, False)
    return wrap(svg(660, 228, b), "Forward bias (+ on P) pushes carriers toward the junction and shrinks the depletion layer, so current flows. Reverse bias (+ on N) pulls carriers away and widens the layer, so only a tiny leakage current flows.")


def d_diode_vi():
    ox, oy = 280, 210
    b = line(60, oy, 540, oy, INK, 1.5) + line(ox, 20, ox, 300, INK, 1.5)
    b += text(545, oy + 5, "V", "start", INK, 13, None, True) + text(ox + 8, 20, "I (mA)", "start", INK, 13, None, True)
    def fwd(v0):
        pts = []
        for i in range(0, 151):
            v = i / 150 * (v0 + 0.12)
            ima = 6 * math.exp((v - v0) / 0.04)
            y = oy - min(ima * 3.2, 175)
            pts.append((ox + v * 250, y))
            if ima * 3.2 > 175:
                break
        return pts
    b += poly(fwd(0.7), PURP, 2.8) + poly(fwd(0.3), AMBER, 2.4, "6,3")
    b += poly([(ox, oy), (ox - 160, oy + 6), (ox - 175, oy + 8), (ox - 177, oy + 60), (ox - 178, oy + 85)], PURP, 2.8)
    b += line(ox + 0.7 * 250, oy, ox + 0.7 * 250, oy + 8) + text(ox + 0.7 * 250, oy + 24, "0.7 V (Si)", "middle", PURP, 12, "bold")
    b += line(ox + 0.3 * 250, oy, ox + 0.3 * 250, oy + 8) + text(ox + 0.3 * 250 - 6, oy + 24, "0.3 V (Ge)", "middle", AMBER, 12, "bold")
    b += text(ox - 12, 50, "forward conduction", "end", GREEN, 13, "bold") + text(ox - 12, 66, "(above the knee voltage)", "end", GREY, 12)
    b += text(ox - 150, oy - 14, "reverse leakage", "middle", RED, 12, "bold") + text(ox - 150, oy - 28, "(nA–µA, magnified)", "middle", GREY, 11)
    b += text(ox - 150, oy + 106, "reverse breakdown", "middle", RED, 12, "bold")
    b += text(300, 338, "schematic — reverse current drawn magnified, forward and reverse scales differ", "middle", GREY, 11, None, True)
    return wrap(svg(580, 350, b), "V–I characteristic of a junction diode: almost nothing flows until the forward knee (≈ 0.7 V for silicon, 0.3 V for germanium); in reverse only a tiny leakage flows until breakdown.")


def d_zener_vi():
    ox, oy = 300, 170
    b = line(60, oy, 540, oy, INK, 1.5) + line(ox, 30, ox, 310, INK, 1.5)
    b += text(545, oy + 5, "V", "start", INK, 13, None, True) + text(ox + 8, 30, "I", "start", INK, 13, None, True)
    b += poly([(ox, oy), (ox + 40, oy - 2), (ox + 60, oy - 12), (ox + 75, oy - 60), (ox + 85, oy - 120)], PURP, 2.8)
    b += poly([(ox, oy), (ox - 120, oy + 4), (ox - 150, oy + 6), (ox - 158, oy + 30), (ox - 162, oy + 130)], BLUE, 2.8)
    b += line(ox - 158, oy, ox - 158, oy + 8) + text(ox - 158, oy - 12, "−V_Z", "middle", BLUE, 13, "bold")
    b += line(ox - 158, oy + 30, ox, oy + 30, GREY, 1, "3,3") + text(ox - 80, oy + 24, "I_Z(min)", "middle", GREY, 11)
    b += line(ox - 162, oy + 130, ox, oy + 130, GREY, 1, "3,3") + text(ox - 80, oy + 146, "I_Z(max) — power limit", "middle", GREY, 11)
    b += rect(ox - 175, oy + 30, 34, 100, "none", GREEN, 1.4, 3, "4,3") + text(ox - 190, oy + 82, "regulating", "end", GREEN, 12, "bold") + text(ox - 190, oy + 98, "region", "end", GREEN, 12, "bold")
    b += text(ox + 95, oy - 100, "forward: acts as a", "start", PURP, 12) + text(ox + 95, oy - 84, "normal diode", "start", PURP, 12)
    b += text(ox - 20, 318, "voltage stays ≈ V_Z while current varies widely", "middle", INK, 12, None, True)
    return wrap(svg(580, 335, b), "Zener diode V–I curve: forward it behaves like an ordinary diode; in reverse the voltage is pinned near V_Z over a wide range of current, which is what makes it a voltage reference.")


def d_zener_reg():
    T, B = 60, 195
    b = line(80, B, 400, B) + vsrc(80, B, 80, T, "V_in", "left")
    b += res(80, T, 260, T, "R_s") + line(260, T, 400, T) + dot(260, T) + dot(260, B)
    b += zener(260, B, 260, T, "D_Z", "left") + res(400, T, 400, B, "R_L", "right")
    b += dot(400, T) + dot(400, B)
    b += arrow(92, T - 12, 128, T - 12, RED, 2, 8) + text(110, T - 18, "I_S", "middle", RED, 13, "bold")
    b += arrow(282, 105, 282, 140, RED, 2, 8) + text(296, 126, "I_Z", "start", RED, 13, "bold")
    b += arrow(376, 105, 376, 140, RED, 2, 8) + text(366, 126, "I_L", "end", RED, 13, "bold")
    b += text(330, 30, "V_out = V_Z", "middle", GREEN, 14, "bold")
    return wrap(svg(540, 230, b), "Zener shunt regulator: the series resistor R_s drops the excess voltage, the reverse-biased Zener holds the output near V_Z, and R_L is in parallel with the Zener. I_S = I_Z + I_L.")


def d_bjt():
    b = bjt(130, 120, "npn") + bjt(450, 120, "pnp")
    # NPN labels and currents
    b += text(163, 58, "C", "start", INK, 14, "bold") + text(163, 192, "E", "start", INK, 14, "bold") + text(70, 126, "B", "end", INK, 14, "bold")
    b += arrow(190, 52, 190, 84, RED, 2, 8) + text(198, 72, "I_C", "start", RED, 13, "bold")
    b += arrow(190, 158, 190, 190, RED, 2, 8) + text(198, 178, "I_E", "start", RED, 13, "bold")
    b += arrow(44, 106, 76, 106, RED, 2, 8) + text(60, 98, "I_B", "middle", RED, 13, "bold")
    b += text(130, 24, "NPN", "middle", INK, 15, "bold") + text(130, 225, "arrow points OUT (n-type emitter)", "middle", GREY, 12)
    # PNP: emitter top, collector bottom
    b += text(483, 58, "E", "start", INK, 14, "bold") + text(483, 192, "C", "start", INK, 14, "bold") + text(390, 126, "B", "end", INK, 14, "bold")
    b += arrow(510, 52, 510, 84, RED, 2, 8) + text(518, 72, "I_E", "start", RED, 13, "bold")
    b += arrow(510, 158, 510, 190, RED, 2, 8) + text(518, 178, "I_C", "start", RED, 13, "bold")
    b += arrow(396, 106, 364, 106, RED, 2, 8) + text(380, 98, "I_B", "middle", RED, 13, "bold")
    b += text(450, 24, "PNP", "middle", INK, 15, "bold") + text(450, 225, "arrow points IN (p-type emitter)", "middle", GREY, 12)
    b += text(290, 262, "I_E = I_B + I_C   (both types)", "middle", INK, 14, "bold")
    return wrap(svg(580, 275, b), "BJT symbols with conventional current directions. The emitter arrow always shows the direction of conventional emitter current: out of an NPN, into a PNP.")


def d_bjt_curves():
    ox, oy = 70, 220
    b = line(ox, oy, 460, oy, INK, 1.5) + line(ox, oy, ox, 20, INK, 1.5)
    b += text(465, oy + 5, "V_CE (V)", "start", INK, 13) + text(ox, 14, "I_C (mA)", "middle", INK, 13)
    b += rect(ox, 20, 38, 200, "#f6e9ff", "none", 0) + text(ox + 19, 40, "sat.", "middle", PURP, 11, "bold")
    for ib, sat in ((80, 8), (60, 6), (40, 4), (20, 2)):
        pts = [(ox + v * 7, oy - (sat * 22) * (1 - math.exp(-v / 0.6)) - 0.35 * v * (sat / 4) * 1.4 * (v > 0)) for v in [i * 0.4 for i in range(0, 52)]]
        b += poly(pts, PURP, 2.4) + text(ox + 20 * 7 + 8, pts[-1][1] + 4, f"I_B = {ib} µA", "start", INK, 11)
    b += line(ox, oy - 1, ox + 20 * 7, oy - 1, BLUE, 3) + text(ox + 20 * 7 + 8, oy - 1, "I_B = 0  (cut-off)", "start", BLUE, 11, "bold")
    b += text(ox + 80, oy - 20, "ACTIVE region: I_C ≈ β·I_B", "start", GREEN, 12, "bold")
    b += text(ox + 8, oy + 18, "0.2 V", "middle", GREY, 11)
    return wrap(svg(560, 250, b), "Common-emitter output characteristics (β = 100): each curve is one base current. Left edge = saturation (switch ON), flat middle = active region (amplifier), I_B = 0 = cut-off (switch OFF).")


def d_mosfet():
    b = rect(110, 120, 400, 100, "#f7e5c8", INK, 2) + text(310, 200, "P-type substrate (body)", "middle", INK, 13)
    b += rect(135, 120, 80, 36, "#c5d3f5", INK, 1.6) + rect(405, 120, 80, 36, "#c5d3f5", INK, 1.6) + text(175, 143, "N⁺", "middle", BLUE, 14, "bold") + text(445, 143, "N⁺", "middle", BLUE, 14, "bold")
    b += rect(135, 100, 350, 20, "#e2e4ea", INK, 1.2) + text(310, 114, "SiO₂ insulating layer", "middle", GREY, 11)
    b += rect(215, 78, 190, 22, "#b9c0cc", INK, 1.6) + text(310, 94, "gate metal", "middle", INK, 11, "bold")
    b += rect(150, 86, 50, 34, "#b9c0cc", INK, 1.4) + rect(420, 86, 50, 34, "#b9c0cc", INK, 1.4)
    b += rect(215, 120, 190, 8, "#7aa7ff", "none", 0, 0)
    b += text(310, 172, "induced N-channel (blue strip) when V_GS > V_T", "middle", BLUE, 12, "bold") + line(310, 160, 310, 129, BLUE, 1.2)
    b += line(175, 86, 175, 40) + line(445, 86, 445, 40) + line(310, 78, 310, 40)
    b += text(175, 30, "Source (S)", "middle", INK, 14, "bold") + text(310, 30, "Gate (G)", "middle", INK, 14, "bold") + text(445, 30, "Drain (D)", "middle", INK, 14, "bold")
    b += arrow(185, 62, 295, 62, GREEN, 2, 8) + text(240, 56, "+V_GS", "middle", GREEN, 12, "bold")
    b += arrow(460, 52, 330, 52, RED, 0.01, 1) if False else ""
    b += text(540, 150, "electrons flow", "start", PURP, 12) + text(540, 166, "S → D through the", "start", PURP, 12) + text(540, 182, "channel when V_DS > 0", "start", PURP, 12)
    return wrap(svg(680, 240, b), "N-channel enhancement MOSFET: the gate is insulated by SiO₂, so no gate current flows. A positive gate voltage above the threshold pulls electrons under the oxide and forms the channel between N⁺ source and drain.")


def d_mosfet_curves():
    ox, oy = 70, 230
    sx, sy = 38, 20
    b = line(ox, oy, 480, oy, INK, 1.5) + line(ox, oy, ox, 20, INK, 1.5)
    b += text(480, oy + 34, "V_DS (V) →", "end", INK, 13) + text(ox, 14, "I_D (mA)", "middle", INK, 13)
    k, vt = 0.5, 2
    bd = [(ox + v * sx, oy - min(k * v * v, 9.6) * sy) for v in [i * 0.05 for i in range(0, 81)] if k * v * v <= 9.6]
    b += poly(bd, GREY, 1.6, "5,4") + text(ox + 4.2 * sx, oy - 9.5 * sy, "boundary: V_DS = V_GS − V_T", "start", GREY, 11)
    for vgs in (3, 4, 5, 6):
        vp = vgs - vt
        pts = []
        for i in range(0, 201):
            v = i * 0.05
            if v <= vp:
                idd = k * (2 * vp * v - v * v)
            else:
                idd = k * vp * vp
            pts.append((ox + v * sx, oy - idd * sy))
        b += poly(pts, PURP, 2.4) + text(ox + 10 * sx + 6, pts[-1][1] + 4, f"V_GS = {vgs} V", "start", INK, 11)
    b += line(ox, oy - 1, ox + 10 * sx, oy - 1, BLUE, 3) + text(ox + 5 * sx, oy + 18, "V_GS < V_T (2 V): cut-off (I_D ≈ 0)", "middle", BLUE, 11, "bold")
    b += text(ox + 1.0 * sx, 110, "ohmic", "middle", GREEN, 12, "bold") + text(ox + 1.0 * sx, 126, "(triode)", "middle", GREEN, 12, "bold")
    b += text(ox + 7 * sx, 150, "saturation", "middle", GREEN, 12, "bold")
    return wrap(svg(620, 262, b), "MOSFET output characteristics (V_T = 2 V): below V_T nothing flows (cut-off); for small V_DS the device acts like a voltage-controlled resistor (ohmic); beyond V_DS = V_GS − V_T the current flattens (saturation).")


def _wave_pair(x0, y_in, y_out, w=300, A=40, cycles=2, out="half"):
    deg = 360 * cycles
    b = line(x0, y_in, x0 + w + 10, y_in, GREY, 1) + line(x0, y_out, x0 + w + 10, y_out, GREY, 1)
    pts = sine_pts(x0, y_in, w, A, 0, deg, 0, 240)
    b += poly(pts, "#9aa3b2", 2, "5,3") + text(x0 - 6, y_in - A + 4, "v_in", "end", INK, 12, None, True)
    if out == "half":
        op = [(x, y_out - max(0, y_in - y)) for x, y in pts]
    else:
        op = [(x, y_out - abs(y_in - y)) for x, y in pts]
    b += poly(op, PURP, 2.8) + text(x0 - 6, y_out - A + 4, "v_out", "end", INK, 12, None, True)
    return b


def d_halfwave():
    b = line(150, 160, 310, 160) + acsrc(150, 160, 150, 50, "v = V_m sin ωt", "left")
    b += line(150, 50, 185, 50) + diode(185, 50, 265, 50, "D") + line(265, 50, 310, 50) + res(310, 50, 310, 160, "R_L", "right")
    b += _wave_pair(470, 70, 190, 280, 40, 2, "half")
    b += text(610, 18, "input and output waveforms", "middle", GREY, 12)
    return wrap(svg(780, 235, b), "Half-wave rectifier: the diode conducts only on positive half-cycles, so the load sees pulses with an average of V_m/π and the ripple is at the supply frequency.")


def d_fullwave_ct():
    b = acsrc(45, 175, 45, 65, "v₁", "left") + line(45, 65, 105, 65) + line(45, 175, 105, 175)
    b += ind(105, 65, 105, 175, None) + line(125, 78, 125, 162, INK, 2) + line(131, 78, 131, 162, INK, 2)
    b += ind(185, 50, 185, 120, None) + ind(185, 120, 185, 190, None)
    b += text(176, 44, "A", "end", INK, 13, "bold") + text(176, 200, "B", "end", INK, 13, "bold")
    b += line(185, 50, 225, 50) + diode(225, 50, 285, 50, "D₁") + line(285, 50, 330, 50) + line(330, 50, 330, 190)
    b += line(185, 190, 225, 190) + diode(225, 190, 285, 190, "D₂", "bottom") + line(285, 190, 330, 190)
    b += line(330, 120, 400, 120) + res(400, 120, 400, 190, "R_L", "right") + gnd(400, 190) + dot(330, 120, 4)
    b += line(185, 120, 158, 120) + line(158, 120, 158, 205) + gnd(158, 205) + dot(185, 120, 3.5)
    b += text(200, 112, "C (centre tap)", "start", GREY, 12)
    b += _wave_pair(520, 70, 195, 280, 40, 2, "full")
    return wrap(svg(840, 250, b), "Centre-tapped full-wave rectifier: D₁ conducts when A is positive, D₂ when B is positive; each takes half the secondary, so the load current always flows the same way and the ripple frequency is 2f.")


def d_bridge():
    cx, cy = 300, 130
    Lf, Tp, Rt, Bt = (cx - 85, cy), (cx, cy - 65), (cx + 85, cy), (cx, cy + 65)
    b = diode(*Tp, *Rt, "D₁", "right") + diode(*Bt, *Rt, "D₂", "right") + diode(*Lf, *Tp, "D₃", "left") + diode(*Lf, *Bt, "D₄", "left")
    b += res(Lf[0], cy, Rt[0], cy, "R_L", "top")
    b += line(cx, cy - 65, cx, cy - 92) + line(cx, cy - 92, cx - 160, cy - 92) + line(cx, cy + 65, cx, cy + 92) + line(cx, cy + 92, cx - 160, cy + 92)
    b += acsrc(cx - 160, cy + 92, cx - 160, cy - 92, "v", "left")
    for p in (Lf, Tp, Rt, Bt):
        b += dot(*p, 4)
    b += text(Rt[0] + 10, cy - 8, "+", "start", GREEN, 18, "bold") + text(Lf[0] - 10, cy - 8, "−", "end", GREEN, 18, "bold")
    b += _wave_pair(560, 75, 200, 260, 40, 2, "full")
    return wrap(svg(860, 262, b), "Bridge rectifier: when the top input is positive, current runs through D₁, the load (right to left) and D₄; on the other half-cycle through D₂, the same load direction, and D₃. Two diodes conduct at a time, so about 1.4 V is lost.")


def _opamp_core(cx=330, cy=120):
    return opamp(cx, cy) + line(cx + 50, cy, cx + 100, cy) + dot(cx + 50, cy, 0.1)


def d_opamp_inv():
    cx, cy = 330, 120
    b = opamp(cx, cy)
    b += dot(100, 98, 4) + text(92, 94, "v_i", "end", INK, 14, "bold") + res(100, 98, 235, 98, "R₁") + line(235, 98, cx - 40, 98) + dot(235, 98, 4)
    b += line(235, 98, 235, 48) + res(235, 48, 400, 48, "R_f") + line(400, 48, 400, cy) + line(cx + 50, cy, 440, cy) + dot(400, cy, 4) + dot(440, cy, 4) + text(450, cy + 4, "v_o", "start", INK, 14, "bold")
    b += line(cx - 40, cy + 22, 250, cy + 22) + line(250, cy + 22, 250, cy + 40) + gnd(250, cy + 40)
    b += line(180, 160, 232, 103, GREEN, 1.2) + text(228, 176, "inverting node ≈ 0 V", "end", GREEN, 12, "bold") + text(228, 192, "(virtual earth)", "end", GREEN, 12)
    b += text(330, 226, "A_v = v_o / v_i = − R_f / R₁", "middle", INK, 15, "bold")
    return wrap(svg(520, 245, b), "Inverting amplifier: negative feedback through R_f forces the inverting input to ≈ 0 V (virtual earth), so the current v_i/R₁ must flow through R_f. Output = −(R_f/R₁) × input.")


def d_opamp_noninv():
    cx, cy = 330, 120
    b = pfill([(cx - 40, cy - 45), (cx - 40, cy + 45), (cx + 50, cy)], "#fff", INK, 2)
    b += text(cx - 31, cy - 17, "+", "middle", INK, 16, "bold") + text(cx - 31, cy + 27, "−", "middle", INK, 16, "bold")
    b += dot(100, cy - 22, 4) + text(92, cy - 18, "v_i", "end", INK, 14, "bold") + line(100, cy - 22, cx - 40, cy - 22)
    b += line(cx - 40, cy + 22, 260, cy + 22) + dot(260, cy + 22, 4) + res(260, cy + 22, 260, 205, "R₁", "right") + gnd(260, 205)
    b += line(260, cy + 22, 225, cy + 22) + line(225, cy + 22, 225, 250) + res(225, 250, 400, 250, "R_f", "bottom") + line(400, 250, 400, cy)
    b += line(cx + 50, cy, 440, cy) + dot(400, cy, 4) + dot(440, cy, 4) + text(450, cy + 4, "v_o", "start", INK, 14, "bold")
    b += text(330, 305, "A_v = v_o / v_i = 1 + R_f / R₁", "middle", INK, 15, "bold")
    return wrap(svg(520, 322, b), "Non-inverting amplifier: the input drives the + terminal; R_f and R₁ form a divider that feeds back a fraction of v_o to the − terminal. Gain is always ≥ 1 and the output is in phase with the input.")


def d_opamp_sum():
    cx, cy = 360, 118
    b = opamp(cx, cy)
    ys = (50, 96, 142)
    for y, n, r in zip(ys, ("v_A", "v_B", "v_C"), ("R_A", "R_B", "R_C")):
        b += dot(70, y, 4) + text(62, y + 4, n, "end", INK, 13, "bold") + res(70, y, 210, y, r, "top")
    b += line(210, 50, 210, 142) + line(210, 96, cx - 40, 96) + dot(210, 96, 4)
    b += line(210, 50, 210, 14) + res(210, 14, 430, 14, "R_f", "top") + line(430, 14, 430, cy) + line(cx + 50, cy, 480, cy) + dot(430, cy, 4) + dot(480, cy, 4) + text(490, cy + 4, "v_o", "start", INK, 14, "bold")
    b += line(cx - 40, cy + 22, 285, cy + 22) + line(285, cy + 22, 285, cy + 45) + gnd(285, cy + 45)
    b += text(300, 222, "v_o = − R_f ( v_A/R_A + v_B/R_B + v_C/R_C )", "middle", INK, 14, "bold")
    return wrap(svg(560, 262, f'<g transform="translate(0,22)">{b}</g>'), "Summing amplifier: all input currents add at the virtual-earth node and flow through R_f, so the output is the (negative) weighted sum. With R_A = R_B = R_C = R_f it is simply −(v_A + v_B + v_C).")


def d_comm_block():
    names = ["Information\nsource", "Input\ntransducer", "Transmitter", "Channel", "Receiver", "Output\ntransducer", "Destination"]
    b = ""
    for i, n in enumerate(names):
        x = 10 + i * 118
        b += box(x, 70, 100, 56, n, "#fde8f2" if n == "Channel" else LIGHT, "#d6307a" if n == "Channel" else INK)
        if i < 6:
            b += arrow(x + 100, 98, x + 118, 98, INK, 2, 8)
    b += box(354, 170, 100, 40, "Noise", "#fff", "#d6307a") + arrow(404, 170, 404, 128, "#d6307a", 2.2, 9)
    b += text(60, 54, "message", "middle", GREY, 12, None, True) + text(178, 54, "electrical signal", "middle", GREY, 12, None, True)
    b += text(650, 54, "electrical signal", "middle", GREY, 12, None, True) + text(768, 54, "message", "middle", GREY, 12, None, True)
    return wrap(svg(830, 225, b), "Block diagram of a communication system: the message is converted to an electrical signal, shaped by the transmitter, sent over a channel that adds noise, then recovered by the receiver and converted back.")


def d_em_spectrum():
    bands = [("Radio", "#b7c7e8", "> 1 m", "broadcast,\nmobile, Wi-Fi"), ("Microwave", "#c5b7e8", "1 m – 1 mm", "ovens, radar,\nsatellite"), ("Infrared", "#e8b7b7", "1 mm – 700 nm", "remotes, thermal\nimaging"),
             ("Visible", None, "700 – 400 nm", "human vision"), ("Ultraviolet", "#d9b7e8", "400 – 10 nm", "sterilising,\nsunburn"), ("X-rays", "#b7e8d9", "10 nm – 0.01 nm", "medical\nimaging"), ("Gamma", "#e8e0b7", "< 0.01 nm", "radioactive\nsources")]
    b = ('<defs><linearGradient id="visg" x1="0" x2="1"><stop offset="0" stop-color="#e03b3b"/><stop offset="0.25" stop-color="#f2c94c"/>'
         '<stop offset="0.5" stop-color="#5fc26a"/><stop offset="0.75" stop-color="#4a8fe0"/><stop offset="1" stop-color="#8a4fd0"/></linearGradient></defs>')
    for i, (n, col, wl, use) in enumerate(bands):
        x = 10 + i * 122
        b += rect(x, 50, 118, 44, col or "url(#visg)", INK, 1.4, 4) + text(x + 59, 78, n, "middle", "#fff" if n == "Visible" else INK, 14, "bold")
        b += text(x + 59, 114, wl, "middle", INK, 12, "bold")
        for k, l in enumerate(use.split("\n")):
            b += text(x + 59, 134 + k * 15, l, "middle", GREY, 12)
    b += arrow(20, 28, 840, 28, INK, 2, 10) + text(430, 20, "frequency and photon energy increase  →", "middle", INK, 12, "bold")
    b += arrow(840, 180, 20, 180, INK, 2, 10) + text(430, 200, "←  wavelength increases", "middle", INK, 12, "bold")
    return wrap(svg(864, 215, b), "The electromagnetic spectrum. All of it travels at c = 3 × 10⁸ m/s in vacuum; c = fλ links frequency and wavelength.")


def _hex(cx, cy, s, fill, label, sw=1.5, stroke=INK):
    pts = [(cx + s * math.cos(math.radians(60 * k - 30)), cy + s * math.sin(math.radians(60 * k - 30))) for k in range(6)]
    return pfill(pts, fill, stroke, sw) + text(cx, cy + 5, label, "middle", INK, 14, "bold")


def d_cellular():
    cols = ["#f9c5c5", "#f9e0a8", "#d5f0b4", "#b4f0d9", "#b8d4f5", "#d5c4f5", "#f5c4e6"]
    s = 28
    b = ""
    for row in range(5):
        for col in range(8):
            q = col - (row - (row & 1)) // 2
            idx = (q + 5 * row) % 7
            x = 40 + s * math.sqrt(3) * (col + 0.5 * (row % 2))
            y = 40 + s * 1.5 * row
            hi = idx == 0
            b += _hex(x, y, s - 1, cols[idx], str(idx + 1), 3 if hi else 1.2, RED if hi else INK)
            if hi:
                b += dot(x, y - 14, 3, RED)
    b += text(520, 60, "Cells with the same number reuse", "start", INK, 13, "bold") + text(520, 78, "the same frequency set.", "start", INK, 13, "bold")
    b += text(520, 108, "Red outlines = co-channel cells,", "start", RED, 13) + text(520, 126, "kept far apart so they don't", "start", RED, 13) + text(520, 144, "interfere.", "start", RED, 13)
    b += text(520, 176, "Each hexagon = one cell served", "start", GREY, 12) + text(520, 192, "by its own base station.", "start", GREY, 12)
    b += text(520, 222, "Cluster of N = 7 cells uses all", "start", GREY, 12) + text(520, 238, "the available channels once.", "start", GREY, 12)
    return wrap(svg(740, 270, b), "Cellular layout with frequency reuse, cluster size N = 7: the service area is tiled by hexagonal cells, and each of the 7 frequency groups is reused in a distant cell.")


def d_satellite():
    b = f'<circle cx="420" cy="500" r="300" fill="#dcecf7" stroke="{INK}" stroke-width="2"/>'
    for x in (220, 620):
        y = 500 - math.sqrt(300 ** 2 - (x - 420) ** 2)
        b += line(x, y, x, y - 28, INK, 3) + line(x - 10, y - 28, x + 10, y - 28, INK, 3) + line(x - 5, y - 36, x + 5, y - 36, INK, 3)
    ys = 500 - math.sqrt(300 ** 2 - 200 ** 2)
    b += rect(395, 60, 50, 34, "#d9dde6", INK, 2) + rect(340, 70, 48, 14, "#9db7e8", INK, 1.5) + rect(452, 70, 48, 14, "#9db7e8", INK, 1.5) + text(420, 50, "Satellite (transponder)", "middle", INK, 13, "bold")
    b += arrow(222, ys - 40, 396, 90, RED, 2.8, 12) + arrow(444, 90, 618, ys - 40, BLUE, 2.8, 12)
    b += text(250, 150, "Uplink", "end", RED, 14, "bold") + text(250, 167, "5.9–6.4 GHz", "end", RED, 13) + text(590, 150, "Downlink", "start", BLUE, 14, "bold") + text(590, 167, "3.7–4.2 GHz", "start", BLUE, 13)
    b += text(205, ys - 2, "Transmitting earth station", "end", INK, 12) + text(635, ys - 2, "Receiving earth station", "start", INK, 12)
    b += text(420, 290, "Earth", "middle", GREY, 13, "bold")
    return wrap(svg(840, 330, b), "Satellite link: the ground station sends the uplink at a higher frequency; the satellite amplifies it, shifts it down in frequency and returns it as the downlink.")


def d_transponder():
    items = ["Input\nfilter", "6 GHz\namplifier", "Mixer", "4 GHz\namplifier", "Input\nmux", "TWT\namplifier", "Output\nmux"]
    b = text(50, 40, "Uplink", "middle", RED, 13, "bold") + text(50, 56, "5.9–6.4 GHz", "middle", RED, 12)
    xs = [110, 215, 320, 410, 540, 650, 760]
    for i, (x, n) in enumerate(zip(xs, items)):
        if n == "Mixer":
            b += f'<circle cx="{x+30}" cy="80" r="26" fill="#fff" stroke="{INK}" stroke-width="2"/>' + text(x + 30, 87, "×", "middle", INK, 22, "bold")
        else:
            b += box(x, 52, 82 if i not in (4, 5, 6) else 84, 56, n, "#fff7cc" if i >= 4 else LIGHT)
    b += rect(530, 40, 322, 80, "none", AMBER, 2.4, 10, "6,3") + text(690, 36, "Transponder", "middle", AMBER, 12, "bold")
    b += arrow(80, 80, 108, 80, INK, 2, 8) + arrow(192, 80, 213, 80, INK, 2, 8) + arrow(297, 80, 322, 80, INK, 2, 8)
    b += arrow(376, 80, 408, 80, INK, 2, 8) + arrow(492, 80, 538, 80, INK, 2, 8) + arrow(624, 80, 648, 80, INK, 2, 8) + arrow(734, 80, 758, 80, INK, 2, 8) + arrow(844, 80, 874, 80, INK, 2, 8)
    b += box(300, 150, 100, 40, "2.2 GHz local\noscillator", "#fff", INK, 11) + arrow(350, 150, 350, 108, INK, 2, 8)
    b += text(900, 40, "Downlink", "middle", BLUE, 13, "bold") + text(900, 56, "3.7–4.2 GHz", "middle", BLUE, 12)
    return wrap(svg(960, 200, b), "Satellite transponder chain (C-band): the 6 GHz uplink is filtered, amplified, mixed with a 2.2 GHz oscillator to shift it down to about 4 GHz, amplified again by a travelling-wave-tube amplifier and sent back down.")


def d_radar():
    b = line(0, 220, 600, 220, "#b9a888", 3)
    b += line(70, 220, 70, 170, INK, 4) + f'<path d="M40,150 Q70,115 100,150" fill="none" stroke="{INK}" stroke-width="4"/>' + line(70, 135, 70, 170, INK, 2)
    b += text(70, 245, "Radar (Tx + Rx)", "middle", INK, 13, "bold")
    for r in (40, 75, 110):
        b += f'<path d="M{70 + r*math.cos(math.radians(-35)):.1f},{135 + r*math.sin(math.radians(-35)):.1f} A{r},{r} 0 0 1 {70 + r*math.cos(math.radians(25)):.1f},{135 + r*math.sin(math.radians(25)):.1f}" fill="none" stroke="{RED}" stroke-width="2" opacity="{1 - r/160:.2f}"/>'
    jet = [(470, 80), (520, 84), (540, 76), (520, 72), (500, 50), (488, 50), (498, 72), (462, 70), (452, 56), (444, 56), (448, 74)]
    b += pfill([(430, 92), (520, 88), (545, 98), (520, 108), (430, 100)], "#9aa3b2", INK, 1.8) + pfill([(470, 88), (490, 56), (500, 56), (492, 88)], "#9aa3b2", INK, 1.5) + pfill([(470, 104), (490, 130), (500, 130), (492, 104)], "#9aa3b2", INK, 1.5)
    b += text(485, 150, "Target", "middle", INK, 13, "bold")
    b += arrow(180, 110, 425, 96, RED, 2.5, 10) + text(300, 88, "transmitted pulse", "middle", RED, 12, "bold")
    b += arrow(425, 112, 180, 128, BLUE, 2.5, 10, "6,3") + text(300, 144, "echo (reflected)", "middle", BLUE, 12, "bold")
    b += arrow(80, 190, 430, 190, INK, 1.5, 8) + arrow(430, 190, 80, 190, INK, 1.5, 8) + text(255, 184, "range R = c·t / 2", "middle", INK, 13, "bold")
    return wrap(svg(600, 262, b), "Pulse radar: a short pulse goes out, reflects off the target and returns after time t; since it travelled out and back, the range is R = ct/2.")


MODULE1_EXTRA = [d_cap_start, d_bldc, d_stepper, d_alternator, d_pe_block, d_converters, d_drive_block, d_earthing, d_current_zones]
MODULE2 = [d_pn_junction, d_pn_bias, d_diode_vi, d_zener_vi, d_zener_reg, d_bjt, d_bjt_curves, d_mosfet, d_mosfet_curves,
           d_halfwave, d_fullwave_ct, d_bridge, d_opamp_inv, d_opamp_noninv, d_opamp_sum, d_comm_block, d_em_spectrum,
           d_cellular, d_satellite, d_transponder, d_radar]

if __name__ == "__main__":
    import os, sys
    from playwright.sync_api import sync_playwright
    os.makedirs("_dga", exist_ok=True)
    fns = MODULE1_EXTRA + MODULE2
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 980, "height": 400})
        for f in fns:
            pg.set_content(f'<body style="margin:0;background:#fff;font-family:Arial"><div style="width:960px;padding:6px;text-align:center">{f()}</div></body>')
            pg.screenshot(path=f"_dga/{f.__name__}.png", full_page=True)
        br.close()
    print(len(fns))
