"""Diagrams for Module 3 (Engineering Graphics) and Module 4 (Manufacturing, Energy, Automation)."""
import math
from diagrams import *
from diagrams import _g, _frame, _label, _polar
from diagrams_a import rect, box, pfill, gnd, LIGHT


def dashed(x1, y1, x2, y2, c=GREY, w=1.2):
    return line(x1, y1, x2, y2, c, w, "5,3")


def chain(x1, y1, x2, y2, c=INK, w=1.4):
    return line(x1, y1, x2, y2, c, w, "14,3,2,3")


def dimh(x1, x2, y, label, ext_from=None, size=12, c=INK):
    """horizontal dimension line with arrowheads and label above"""
    b = arrow(x1 + 14, y, x1, y, c, 1.3, 7) + arrow(x2 - 14, y, x2, y, c, 1.3, 7) + line(x1, y, x2, y, c, 1.3)
    if ext_from is not None:
        b += line(x1, y - 4, x1, ext_from, c, 0.9) + line(x2, y - 4, x2, ext_from, c, 0.9)
    return b + text((x1 + x2) / 2, y - 4, label, "middle", c, size)


def dimv(y1, y2, x, label, ext_from=None, size=12, c=INK):
    b = line(x, y1, x, y2, c, 1.3) + arrow(x, y1 + 14, x, y1, c, 1.3, 7) + arrow(x, y2 - 14, x, y2, c, 1.3, 7)
    if ext_from is not None:
        b += line(x - 4, y1, ext_from, y1, c, 0.9) + line(x - 4, y2, ext_from, y2, c, 0.9)
    t = text(x - 5, (y1 + y2) / 2, label, "middle", c, size)
    return b + t.replace("<text ", f'<text transform="rotate(-90 {x-5:.1f} {(y1+y2)/2:.1f})" ')


# ===================================================================== MODULE 3
def d_sheet_sizes():
    s = 500 / 1189
    x0, y0 = 40, 30
    W, H = 1189 * s, 841 * s
    b = rect(x0, y0, W, H, "#f4f7ff", INK, 2.2)
    w1 = 594 * s
    b += line(x0 + w1, y0, x0 + w1, y0 + H, INK, 1.6)
    b += text(x0 + w1 / 2, y0 + H / 2, "A1", "middle", INK, 26, "bold") + text(x0 + w1 / 2, y0 + H / 2 + 20, "594 × 841", "middle", GREY, 12)
    rx = x0 + w1
    h2 = 420 * s
    b += line(rx, y0 + h2, x0 + W, y0 + h2, INK, 1.6) + text(rx + (W - w1) / 2, y0 + h2 / 2 + 8, "A2", "middle", INK, 22, "bold") + text(rx + (W - w1) / 2, y0 + h2 / 2 + 26, "420 × 594", "middle", GREY, 12)
    w3 = 297 * s
    b += line(rx + w3, y0 + h2, rx + w3, y0 + H, INK, 1.6)
    b += text(rx + w3 / 2, y0 + h2 + (H - h2) / 2 + 8, "A3", "middle", INK, 20, "bold") + text(rx + w3 / 2, y0 + h2 + (H - h2) / 2 + 24, "297 × 420", "middle", GREY, 11)
    xm = rx + w3
    hm = y0 + h2 + (H - h2) / 2
    b += line(xm, hm, x0 + W, hm, INK, 1.6)
    for k, yy in enumerate((y0 + h2 + (hm - y0 - h2) / 2, hm + (y0 + H - hm) / 2)):
        b += text(xm + (x0 + W - xm) / 2, yy + 2, "A4", "middle", INK, 16, "bold") + text(xm + (x0 + W - xm) / 2, yy + 16, "210 × 297", "middle", GREY, 10)
    b += text(x0 + 25, y0 + H - 14, "A0", "start", INK, 28, "bold") + text(x0 + 25, y0 + H + 18, "841 × 1189", "start", GREY, 12) if False else ""
    b += text(x0 + 20, y0 + 28, "A0 = 841 × 1189", "start", BLUE, 14, "bold")
    b += dimh(x0, x0 + W, y0 + H + 22, "1189") + dimv(y0, y0 + H, x0 - 16, "841")
    b += text(x0 + W / 2, y0 + H + 46, "all dimensions in mm — each size is half the one before; sides are in the ratio 1 : √2", "middle", GREY, 12, None, True)
    return wrap(svg(600, y0 + H + 62, b), "BIS drawing-sheet sizes (A-series). A0 has an area of 1 m²; folding a sheet across its longer side gives the next size.")


def d_title_block():
    s = 3.0
    x0, y0 = 44, 24
    W, H = 185 * s, 65 * s
    b = rect(x0, y0, W, H, "#fff", INK, 2.4)
    rw = 55 * s
    xr = x0 + W - rw
    b += line(xr, y0, xr, y0 + H) + line(x0, y0 + 45 * s, xr, y0 + 45 * s)
    b += line(xr, y0 + 10 * s, x0 + W, y0 + 10 * s) + line(xr, y0 + 45 * s, x0 + W, y0 + 45 * s)
    for k in range(5):
        b += line(xr, y0 + (10 + 7 * (k + 1)) * s, x0 + W, y0 + (10 + 7 * (k + 1)) * s, INK, 1)
    b += line(xr + 20 * s, y0, xr + 20 * s, y0 + 45 * s) + line(xr + 45 * s, y0, xr + 45 * s, y0 + 45 * s)
    b += text(xr + 32.5 * s, y0 + 6.5 * s, "NAME", "middle", INK, 11) + text(xr + 50 * s, y0 + 6.5 * s, "DATE", "middle", INK, 10)
    for k, n in enumerate(("DESIGNED", "DRAWN", "CHECKED", "STANDARD", "APPROVED")):
        b += text(xr + 2, y0 + (10 + 7 * k + 4.8) * s, n, "start", INK, 10)
    b += text(x0 + 8, y0 + 22, "NAME OF THE FIRM", "start", INK, 14, "bold")
    b += line(x0 + 25 * s, y0 + 45 * s, x0 + 25 * s, y0 + H, INK, 1.4)
    b += text(x0 + 6, y0 + 45 * s + 18, "SCALE", "start", INK, 11) + text(x0 + 25 * s + 8, y0 + 45 * s + 18, "TITLE", "start", INK, 11)
    b += pfill([(x0 + 10, y0 + 56 * s), (x0 + 10, y0 + 62 * s), (x0 + 30, y0 + 63 * s), (x0 + 30, y0 + 55 * s)], "#fff", INK, 1.2)
    b += f'<circle cx="{x0 + 48}" cy="{y0 + 59 * s}" r="9" fill="none" stroke="{INK}" stroke-width="1.2"/><circle cx="{x0 + 48}" cy="{y0 + 59 * s}" r="4" fill="none" stroke="{INK}" stroke-width="1.2"/>'
    b += text(xr + 4, y0 + 45 * s + 16, "DRAWING NO.", "start", INK, 11) + text(x0 + W - 6, y0 + H - 7, "SHEET 3 OF 12", "end", INK, 9)
    b += dimh(x0, x0 + W, y0 - 6, "185") + dimh(xr, xr + 20 * s, y0 + H + 22, "20") + dimh(xr + 20 * s, xr + 45 * s, y0 + H + 22, "25") + dimh(xr + 45 * s, x0 + W, y0 + H + 22, "10")
    b += dimv(y0, y0 + H, x0 - 10, "65")
    return wrap(svg(640, y0 + H + 40, b), "Title block (drawn in the bottom right corner of the sheet): it identifies the drawing, its owner, scale and projection symbol, and records who designed, drew, checked and approved it.")


def d_line_types():
    rows = [("A", "Continuous thick", "visible outlines and edges", "solid", 3.2), ("B", "Continuous thin", "dimension, extension, projection, leader lines; hatching", "solid", 1.2),
            ("C", "Continuous thin freehand", "limits of partial / interrupted views", "free", 1.2), ("D", "Thin with zig-zags", "long break lines", "zig", 1.2),
            ("E", "Dashed thick", "permissible surface treatment", "dash", 3), ("F", "Dashed thin", "hidden outlines and edges", "dashthin", 1.4),
            ("G", "Chain thin (long-dash dot)", "centre lines, lines of symmetry, pitch circles", "chain", 1.4), ("H", "Chain thin, thick at ends", "cutting planes", "cut", 1.4),
            ("J", "Chain thick", "surfaces with a special requirement", "chaink", 3), ("K", "Chain thin double-dash", "adjacent parts, alternate/extreme positions", "dd", 1.4)]
    b = text(20, 18, "Type", "start", GREY, 12, "bold") + text(70, 18, "Sample", "start", GREY, 12, "bold") + text(260, 18, "Name", "start", GREY, 12, "bold") + text(450, 18, "Typical use", "start", GREY, 12, "bold")
    for i, (k, n, u, kind, w) in enumerate(rows):
        y = 44 + i * 30
        b += text(24, y + 4, k, "start", INK, 15, "bold")
        x1, x2 = 70, 235
        if kind == "solid":
            b += line(x1, y, x2, y, INK, w)
        elif kind == "free":
            b += f'<path d="M{x1},{y} q10,-6 20,0 t20,0 t20,0 t20,0 t20,0 t20,0 t20,0 t20,0" fill="none" stroke="{INK}" stroke-width="{w}"/>'
        elif kind == "zig":
            b += line(x1, y, 130, y, INK, w) + poly([(130, y), (138, y - 9), (146, y + 9), (154, y)], INK, w) + line(154, y, x2, y, INK, w)
        elif kind in ("dash", "dashthin"):
            b += line(x1, y, x2, y, INK, w, "12,6")
        elif kind in ("chain", "chaink"):
            b += line(x1, y, x2, y, INK, w, "20,4,3,4")
        elif kind == "cut":
            b += line(x1, y, x1 + 22, y, INK, 3) + line(x1 + 22, y, x2 - 22, y, INK, 1.2, "16,4,3,4") + line(x2 - 22, y, x2, y, INK, 3)
        elif kind == "dd":
            b += line(x1, y, x2, y, INK, w, "18,4,3,4,3,4")
        b += text(260, y + 4, n, "start", INK, 13) + text(450, y + 4, u, "start", GREY, 12)
    b += text(20, 44 + 10 * 30 + 6, "Pencil grades: thick lines HB, thin lines 2H.  (Types A–K as in the lecture table, after N.D. Bhatt.)", "start", GREY, 12, None, True)
    return wrap(svg(760, 44 + 10 * 30 + 20, b), "BIS line types used in engineering drawing. In orthographic views the commonest are A (visible), F (hidden), G (centre lines), B (dimensions) and H (cutting planes).")


def d_dim_elements():
    x0, y0, w, h = 170, 90, 240, 120
    b = rect(x0, y0, w, h, "#f7f9fc", INK, 3)
    cx, cy = x0 + 70, y0 + 60
    b += f'<circle cx="{cx}" cy="{cy}" r="22" fill="none" stroke="{INK}" stroke-width="3"/>'
    b += chain(cx - 32, cy, cx + 32, cy) + chain(cx, cy - 32, cx, cy + 32)
    yt = 50
    b += line(x0, y0 - 3, x0, yt - 6, INK, 1) + line(x0 + w, y0 - 3, x0 + w, yt - 6, INK, 1)
    b += arrow(x0 + 18, yt, x0, yt, INK, 1.3, 8) + arrow(x0 + w - 18, yt, x0 + w, yt, INK, 1.3, 8) + line(x0 + 18, yt, x0 + w - 18, yt, INK, 1.3) + text(x0 + w / 2, yt - 5, "80", "middle", INK, 14, "bold")
    xr = x0 + w + 40
    b += line(x0 + w + 3, y0, xr + 6, y0, INK, 1) + line(x0 + w + 3, y0 + h, xr + 6, y0 + h, INK, 1)
    b += arrow(xr, y0 + 18, xr, y0, INK, 1.3, 8) + arrow(xr, y0 + h - 18, xr, y0 + h, INK, 1.3, 8) + line(xr, y0 + 18, xr, y0 + h - 18, INK, 1.3)
    b += text(xr - 6, y0 + h / 2 + 5, "50", "middle", INK, 14, "bold").replace("<text ", f'<text transform="rotate(-90 {xr-6} {y0+h/2})" ')
    b += line(cx + 16, cy + 16, cx + 70, cy + 52, INK, 1.2) + arrow(cx + 36, cy + 33, cx + 16, cy + 16, INK, 1.2, 8) + line(cx + 70, cy + 52, cx + 110, cy + 52, INK, 1.2)
    b += text(cx + 74, cy + 47, "Ø20", "start", INK, 14, "bold")
    # callouts: text right-aligned at x=140, leaders start just right of the text
    b += text(140, 54, "dimension line", "end", BLUE, 12, "bold") + line(146, 51, x0 + 30, yt, BLUE, 1)
    b += text(140, 86, "extension line", "end", RED, 12, "bold") + line(146, 83, x0 - 1, 80, RED, 1)
    b += text(140, 205, "outline (thick)", "end", GREEN, 12, "bold") + line(146, 202, x0 + 2, y0 + h - 20, GREEN, 1)
    b += text(xr + 24, 62, "arrowhead", "start", PURP, 12, "bold") + line(xr + 20, 66, xr + 4, y0 + 6, PURP, 1)
    b += text(xr + 24, 178, "dimension figure", "start", INK, 12, "bold") + line(xr + 20, 172, xr - 2, 150, INK, 1)
    b += text(cx + 74, cy + 90, "leader line", "start", AMBER, 12, "bold") + line(cx + 72, cy + 82, cx + 56, cy + 56, AMBER, 1)
    b += text(cx, y0 + 108, "centre lines", "middle", GREY, 11)
    return wrap(svg(660, 250, b), "Elements of dimensioning: extension (projection) lines start just clear of the outline and run slightly past the dimension line; the dimension line ends in arrowheads; figures read from the bottom or the right; diameters carry Ø and use a leader.")


def d_dim_systems():
    b = text(150, 20, "Chain (continuous) dimensioning", "middle", INK, 13, "bold") + text(520, 20, "Parallel (progressive) dimensioning", "middle", INK, 13, "bold")
    for k, x in enumerate((150, 520)):
        b += rect(x - 120, 70, 240, 36, "#f7f9fc", INK, 2.4)
        for hx in (-80, -30, 20, 70):
            b += f'<circle cx="{x + hx + 10}" cy="88" r="7" fill="none" stroke="{INK}" stroke-width="2"/>'
    xs = [150 - 70, 150 - 20, 150 + 30, 150 + 80]
    for i in range(3):
        b += dimh(xs[i], xs[i + 1], 140, "50", ext_from=100, size=11)
    b += text(150, 170, "each error adds to the next", "middle", RED, 12, "bold") + text(150, 186, "(tolerances accumulate along the chain)", "middle", GREY, 11)
    xs2 = [520 - 70, 520 - 20, 520 + 30, 520 + 80]
    for i, yy in zip(range(1, 4), (124, 146, 168)):
        b += dimh(xs2[0], xs2[i], yy, str(50 * i), ext_from=100, size=11)
    b += text(520, 196, "all measured from one datum", "middle", GREEN, 12, "bold") + text(520, 212, "(error cannot accumulate)", "middle", GREY, 11)
    b += dot(xs2[0], 100, 4, GREEN) + text(xs2[0] - 10, 112, "datum", "end", GREEN, 11, "bold")
    return wrap(svg(680, 225, b), "Why parallel dimensioning is preferred for inspection: every feature is positioned from the same datum surface, so one hole's error does not shift the others.")


def d_quadrants():
    cx, cy = 300, 170
    b = line(cx, 20, cx, 320, INK, 2.2) + line(80, cy, 520, cy, INK, 2.2)
    b += text(cx + 8, 32, "VP (vertical plane)", "start", BLUE, 13, "bold") + text(500, cy - 8, "HP (horizontal plane)", "end", BLUE, 13, "bold")
    b += text(cx - 150, 50, "I", "middle", GREY, 26, "bold") + text(cx + 150, 50, "II", "middle", GREY, 26, "bold") + text(cx + 150, 310, "III", "middle", GREY, 26, "bold") + text(cx - 150, 310, "IV", "middle", GREY, 26, "bold")
    b += text(cx - 150, 72, "above HP, in front of VP", "middle", GREY, 11) + text(cx + 150, 72, "above HP, behind VP", "middle", GREY, 11)
    b += text(cx + 150, 288, "below HP, behind VP", "middle", GREY, 11) + text(cx - 150, 288, "below HP, in front of VP", "middle", GREY, 11)
    b += rect(cx - 130, cy - 90, 60, 60, "#e8f0fc", BLUE, 2.2) + text(cx - 100, cy - 54, "object", "middle", BLUE, 12, "bold") + text(cx - 100, cy - 12, "FIRST ANGLE (I)", "middle", BLUE, 12, "bold")
    b += rect(cx + 70, cy + 30, 60, 60, "#fdf0e3", AMBER, 2.2) + text(cx + 100, cy + 66, "object", "middle", AMBER, 12, "bold") + text(cx + 100, cy + 22, "THIRD ANGLE (III)", "middle", AMBER, 12, "bold")
    b += f'<circle cx="60" cy="{cy - 60}" r="10" fill="none" stroke="{INK}" stroke-width="2"/><circle cx="60" cy="{cy - 60}" r="3" fill="{INK}"/>' + text(60, cy - 78, "observer", "middle", INK, 12)
    b += arrow(78, cy - 60, cx - 135, cy - 60, GREY, 1.5, 8)
    b += text(cx, 340, "Side view of the planes (looking from the left). Observer is on the left in both systems.", "middle", GREY, 12, None, True)
    return wrap(svg(600, 352, b), "The four quadrants. First angle: the object lies between the observer and the vertical plane (the plane is behind the object and treated as opaque). Third angle: the plane lies between the observer and the object (transparent).")


def _view_box(x, y, w, h, label, fill="#f2f6ff"):
    return rect(x, y, w, h, fill, INK, 1.6) + text(x + w / 2, y + h / 2 + 4, label, "middle", INK, 13, "bold")


def d_first_third():
    b = ""
    for k, (ox, title) in enumerate(((20, "FIRST ANGLE projection (BIS)"), (390, "THIRD ANGLE projection"))):
        b += text(ox + 150, 18, title, "middle", INK, 14, "bold")
        if k == 0:
            b += _view_box(ox + 20, 40, 120, 80, "Front view") + _view_box(ox + 170, 40, 80, 80, "Left side\nview".split("\n")[0], "#fdf0e3") + _view_box(ox + 20, 150, 120, 80, "Top view", "#e6f4ec")
            b += text(ox + 210, 140, "(LSV is drawn on the RIGHT of FV)", "middle", GREY, 10)
            b += text(ox + 80, 250, "top view BELOW front view", "middle", GREY, 11)
        else:
            b += _view_box(ox + 20, 40, 120, 80, "Top view", "#e6f4ec") + _view_box(ox + 20, 150, 120, 80, "Front view") + _view_box(ox + 170, 150, 80, 80, "Right side\nview".split("\n")[0], "#fdf0e3")
            b += text(ox + 80, 250, "top view ABOVE front view", "middle", GREY, 11)
            b += text(ox - 0, 252, "", "middle")
    b += text(150, 275, "", "middle")
    # symbols
    def sym(x, y, third):
        s = ""
        tr = [(x, y + 18), (x + 40, y + 4), (x + 40, y + 36), (x, y + 22 + 12)]
        tr = [(x, y + 12), (x + 46, y + 2), (x + 46, y + 46), (x, y + 36)]
        circ = f'<circle cx="{x + 90}" cy="{y + 24}" r="20" fill="none" stroke="{INK}" stroke-width="1.6"/><circle cx="{x + 90}" cy="{y + 24}" r="9" fill="none" stroke="{INK}" stroke-width="1.6"/>' + chain(x + 62, y + 24, x + 118, y + 24, INK, 1) + chain(x + 90, y + 0, x + 90, y + 48, INK, 1)
        fv = pfill(tr, "none", INK, 1.6)
        if third:
            fv = pfill([(x + 118 + 20, y + 12), (x + 118 + 66, y + 2), (x + 118 + 66, y + 46), (x + 118 + 20, y + 36)][::-1], "none", INK, 1.6)
            fv = pfill([(x + 138, y + 2), (x + 138, y + 46), (x + 184, y + 36), (x + 184, y + 12)], "none", INK, 1.6)
            return circ + fv
        c2 = f'<circle cx="{x + 138}" cy="{y + 24}" r="20" fill="none" stroke="{INK}" stroke-width="1.6"/><circle cx="{x + 138}" cy="{y + 24}" r="9" fill="none" stroke="{INK}" stroke-width="1.6"/>' + chain(x + 110, y + 24, x + 166, y + 24, INK, 1) + chain(x + 138, y, x + 138, y + 48, INK, 1)
        return fv + text(x + 23, y + 70, "F.V.", "middle", INK, 11) + c2 + text(x + 138, y + 70, "L.H.S.V.", "middle", INK, 11)
    b += text(150, 290, "Symbol (put in the title block):", "middle", GREY, 12) + sym(60, 300, False)
    b += text(520, 290, "Symbol:", "middle", GREY, 12)
    ox = 400
    circ = f'<circle cx="{ox + 40}" cy="324" r="20" fill="none" stroke="{INK}" stroke-width="1.6"/><circle cx="{ox + 40}" cy="324" r="9" fill="none" stroke="{INK}" stroke-width="1.6"/>' + chain(ox + 12, 324, ox + 68, 324, INK, 1) + chain(ox + 40, 300, ox + 40, 348, INK, 1)
    b += circ + pfill([(ox + 100, 302), (ox + 100, 346), (ox + 146, 336), (ox + 146, 312)], "none", INK, 1.6)
    b += text(ox + 40, 370, "L.H.S.V.", "middle", INK, 11) + text(ox + 123, 370, "F.V.", "middle", INK, 11)
    return wrap(svg(740, 380, b), "Layout of views and the identifying symbol. First angle (BIS standard in India): front view on top, top view BELOW it, left-side view to the RIGHT of it. Third angle (USA and others): top view ABOVE, right-side view to the right.")


def d_step_views():
    s = 2.0
    ox, oy = 70, 40
    W, D, Hh, h1, xs = 60, 40, 40, 20, 30
    fx, fy = ox, oy
    b = ""
    # FV
    pts = [(0, Hh), (W, Hh), (W, 0), (xs, 0), (xs, Hh - h1), (0, Hh - h1)]
    b += pfill([(fx + x * s, fy + y * s) for x, y in pts], "#f2f6ff", INK, 2.6) + text(fx + W * s / 2, fy - 8, "FRONT VIEW", "middle", INK, 12, "bold")
    # TV
    tx, ty = ox, oy + Hh * s + 50
    b += rect(tx, ty, W * s, D * s, "#f2f6ff", INK, 2.6) + line(tx + xs * s, ty, tx + xs * s, ty + D * s, INK, 2.6) + text(tx + W * s / 2, ty + D * s + 18, "TOP VIEW", "middle", INK, 12, "bold")
    # LSV (to the right of FV)
    lx, ly = ox + W * s + 50, oy
    b += rect(lx, ly, D * s, Hh * s, "#f2f6ff", INK, 2.6) + line(lx, ly + (Hh - h1) * s, lx + D * s, ly + (Hh - h1) * s, INK, 2.6) + text(lx + D * s / 2, ly - 8, "LEFT SIDE VIEW", "middle", INK, 12, "bold")
    for x in (0, xs, W):
        b += dashed(fx + x * s, fy + Hh * s + 2, tx + x * s, ty - 2, GREY, 1)
    for y in (0, Hh - h1, Hh):
        b += dashed(fx + W * s + 2, fy + y * s, lx - 2, ly + y * s, GREY, 1)
    b += dimh(fx, fx + W * s, fy + Hh * s + 22, "60", size=11) + dimv(fy, fy + Hh * s, fx - 22, "40", size=11) + dimv(fy + (Hh - h1) * s, fy + Hh * s, fx - 8 if False else fx - 40, "20", size=11)
    b += dimh(fx, fx + xs * s, fy + Hh * s + 40 - 18 if False else ty - 12, "30", size=11) if False else ""
    b += dimv(ty, ty + D * s, tx + W * s + 22, "40", size=11)
    b += text(lx + D * s / 2, ly + Hh * s + 18, "first-angle arrangement", "middle", GREY, 11, None, True)
    return wrap(svg(520, 280, b), "Three views of a stepped block (first angle). The step appears as the L-shaped outline in the front view, as an edge in the top view and as a horizontal line in the left-side view. No hidden lines are needed because every edge is visible from the viewing side.")


def d_solids():
    s = 1.0
    b = ""
    cells = [("Square pyramid", 95, "pyr"), ("Hexagonal prism", 225, "hex"), ("Cone", 355, "cone"), ("Cylinder", 485, "cyl")]
    xy = 150
    b += line(30, xy, 570, xy, INK, 1.4) + text(34, xy - 4, "X", "start", GREY, 12) + text(566, xy - 4, "Y", "end", GREY, 12) + text(566, xy + 14, "HP", "end", GREY, 11) + text(566, xy - 14, "VP", "end", GREY, 11)
    for name, cx, kind in cells:
        b += text(cx, 16, name, "middle", INK, 13, "bold")
        if kind == "pyr":
            a, h = 50, 70
            b += pfill([(cx - a / 2, xy), (cx + a / 2, xy), (cx, xy - h)], "#e8f0fc", INK, 2.4)
            tv = [(cx - a / 2, xy + 12), (cx + a / 2, xy + 12), (cx + a / 2, xy + 12 + a), (cx - a / 2, xy + 12 + a)]
            b += pfill(tv, "#e8f0fc", INK, 2.4) + line(tv[0][0], tv[0][1], tv[2][0], tv[2][1], INK, 1.8) + line(tv[1][0], tv[1][1], tv[3][0], tv[3][1], INK, 1.8)
        elif kind == "hex":
            a, h = 25, 65
            b += rect(cx - a, xy - h, 2 * a, h, "#e8f0fc", INK, 2.4) + line(cx - a / 2, xy - h, cx - a / 2, xy, INK, 2) + line(cx + a / 2, xy - h, cx + a / 2, xy, INK, 2)
            dd = a * math.sqrt(3) / 2
            hexp = [(cx - a, xy + 12 + dd), (cx - a / 2, xy + 12), (cx + a / 2, xy + 12), (cx + a, xy + 12 + dd), (cx + a / 2, xy + 12 + 2 * dd), (cx - a / 2, xy + 12 + 2 * dd)]
            b += pfill(hexp, "#e8f0fc", INK, 2.4)
        elif kind == "cone":
            r, h = 30, 70
            b += pfill([(cx - r, xy), (cx + r, xy), (cx, xy - h)], "#e8f0fc", INK, 2.4)
            b += f'<circle cx="{cx}" cy="{xy + 12 + r}" r="{r}" fill="#e8f0fc" stroke="{INK}" stroke-width="2.4"/>' + dot(cx, xy + 12 + r, 2.5)
        else:
            r, h = 25, 65
            b += rect(cx - r, xy - h, 2 * r, h, "#e8f0fc", INK, 2.4) + chain(cx, xy - h - 8, cx, xy + 6, GREY, 1)
            b += f'<circle cx="{cx}" cy="{xy + 12 + r}" r="{r}" fill="#e8f0fc" stroke="{INK}" stroke-width="2.4"/>' + chain(cx - r - 6, xy + 12 + r, cx + r + 6, xy + 12 + r, GREY, 1) + chain(cx, xy + 6, cx, xy + 12 + 2 * r + 6, GREY, 1)
    b += text(10, 60, "FV", "start", INK, 12, "bold") + text(10, 186, "TV", "start", INK, 12, "bold")
    b += text(300, 262, "all four: axis ⟂ HP, resting on the base on HP (simple position)", "middle", GREY, 12, None, True)
    return wrap(svg(600, 274, b), "Front and top views of regular solids in simple position. The pyramid is from the CAT-1 key (base 50, axis 70, a base side parallel to VP); the hexagonal prism has side 25, height 65, base edge parallel to VP.")


def d_iso_scale():
    A = (50, 210)
    k = 4.2
    b = line(A[0], A[1], 330, A[1], INK, 1.6)
    b += line(A[0], A[1], A[0] + 260 * math.cos(math.radians(45)), A[1] - 260 * math.sin(math.radians(45)), BLUE, 2) + line(A[0], A[1], A[0] + 300 * math.cos(math.radians(30)), A[1] - 300 * math.sin(math.radians(30)), RED, 2)
    b += text(A[0] + 96, A[1] - 12, "30°", "start", RED, 12, "bold") + text(A[0] + 70, A[1] - 52, "45°", "start", BLUE, 12, "bold")
    b += f'<path d="M{A[0]+60},{A[1]} A60,60 0 0 0 {A[0]+60*math.cos(math.radians(30)):.1f},{A[1]-60*math.sin(math.radians(30)):.1f}" fill="none" stroke="{RED}" stroke-width="1.4"/>'
    b += f'<path d="M{A[0]+80},{A[1]} A80,80 0 0 0 {A[0]+80*math.cos(math.radians(45)):.1f},{A[1]-80*math.sin(math.radians(45)):.1f}" fill="none" stroke="{BLUE}" stroke-width="1.4"/>'
    for t in (10, 20, 30, 40, 50):
        L = t * k
        px, py = A[0] + L * math.cos(math.radians(45)), A[1] - L * math.sin(math.radians(45))
        qx, qy = px, A[1] - (px - A[0]) * math.tan(math.radians(30))
        b += line(px, py, qx, qy, GREY, 1, "3,3") + dot(px, py, 3.5, BLUE) + dot(qx, qy, 3.5, RED)
        b += text(px - 6, py - 4, str(t), "end", BLUE, 11, "bold") + text(qx + 8, qy + 14, f"{t*0.8165:.1f}", "start", RED, 10)
    b += text(250, 40, "TRUE LENGTHS (mm) — on the 45° line", "start", BLUE, 12, "bold") + text(210, 236, "ISOMETRIC LENGTHS — on the 30° line", "middle", RED, 12, "bold")
    b += text(400, 100, "isometric length ÷ true length", "start", INK, 13, "bold") + text(400, 120, "= cos 45° / cos 30° = 0.816", "start", INK, 13, "bold") + text(400, 140, "(≈ 9/11 in the lecture)", "start", GREY, 12)
    return wrap(svg(680, 250, b), "Constructing the isometric scale: mark true lengths on the 45° line, drop verticals onto the 30° line, and read the shortened (isometric) lengths there. Every length along an isometric axis is multiplied by about 0.816.")


def _iso(ox, oy, s):
    c, sn = math.cos(math.radians(30)), math.sin(math.radians(30))
    def P(x, y, z):
        return (ox + (x - y) * c * s, oy - (x + y) * sn * s - z * s)
    return P


def d_iso_axes_cube():
    P = _iso(190, 250, 1.8)
    a = 60
    fx = lambda *pts: [P(*p) for p in pts]
    b = pfill(fx((0, 0, a), (a, 0, a), (a, a, a), (0, a, a)), "#f3f4f7", INK, 2.2)
    b += pfill(fx((0, 0, 0), (a, 0, 0), (a, 0, a), (0, 0, a)), "#dfe4ee", INK, 2.2)
    b += pfill(fx((0, 0, 0), (0, a, 0), (0, a, a), (0, 0, a)), "#c9d2e3", INK, 2.2)
    o = P(0, 0, 0)
    for (x, y, z), lab, anc in (((1.7 * a, 0, 0), "x axis", "start"), ((0, 1.7 * a, 0), "y axis", "end"), ((0, 0, 1.75 * a), "z axis (vertical)", "middle")):
        e = P(x, y, z)
        b += arrow(o[0], o[1], e[0], e[1], RED, 2, 9) + text(e[0] + (8 if anc == "start" else (-8 if anc == "end" else 0)), e[1] + (4 if anc != "middle" else -8), lab, anc, RED, 12, "bold")
    b += text(o[0], o[1] + 30, "120° between each pair of axes", "middle", INK, 12, "bold") + text(o[0] - 70, o[1] - 4, "30°", "end", INK, 12) + text(o[0] + 70, o[1] - 4, "30°", "start", INK, 12)
    b += line(o[0] - 120, o[1], o[0] + 120, o[1], GREY, 1, "4,3")
    tx = 400
    b += text(tx, 90, "Isometric axes: one vertical, two at 30°", "start", INK, 13, "bold") + text(tx, 108, "to the horizontal.", "start", INK, 13, "bold")
    b += text(tx, 138, "Lines parallel to an axis = isometric lines", "start", GREY, 12) + text(tx, 154, "(true length in an isometric DRAWING,", "start", GREY, 12) + text(tx, 170, "×0.816 in an isometric PROJECTION).", "start", GREY, 12)
    b += text(tx, 198, "Other lines = non-isometric lines: locate their", "start", GREY, 12) + text(tx, 214, "end points, then join (never measure directly).", "start", GREY, 12)
    return wrap(svg(780, 290, b), "Isometric axes drawn on a cube. All three faces are foreshortened equally, which is why it is called ‘iso-metric’ (equal measure).")


def d_iso_step():
    s = 2.4
    P = _iso(230, 270, s)
    quad = lambda *pts: [P(*p) for p in pts]
    b = pfill(quad((0, 0, 0), (0, 40, 0), (0, 40, 20), (0, 0, 20)), "#c9d2e3", INK, 2.2)
    b += pfill(quad((0, 0, 0), (30, 0, 0), (30, 0, 20), (0, 0, 20)), "#dfe4ee", INK, 2.2)
    b += pfill(quad((0, 0, 20), (30, 0, 20), (30, 40, 20), (0, 40, 20)), "#f3f4f7", INK, 2.2)
    b += pfill(quad((30, 0, 20), (30, 40, 20), (30, 40, 40), (30, 0, 40)), "#c9d2e3", INK, 2.2)
    b += pfill(quad((30, 0, 0), (60, 0, 0), (60, 0, 40), (30, 0, 40)), "#dfe4ee", INK, 2.2)
    b += pfill(quad((30, 0, 40), (60, 0, 40), (60, 40, 40), (30, 40, 40)), "#f3f4f7", INK, 2.2)
    p0, p1 = P(0, 0, 0), P(60, 0, 0)
    b += text((p0[0] + p1[0]) / 2 + 14, (p0[1] + p1[1]) / 2 + 22, "60", "middle", INK, 13, "bold")
    q1 = P(0, 40, 0)
    b += text((p0[0] + q1[0]) / 2 - 14, (p0[1] + q1[1]) / 2 + 20, "40", "middle", INK, 13, "bold")
    r0, r1 = P(60, 0, 0), P(60, 0, 40)
    b += text(r0[0] + 16, (r0[1] + r1[1]) / 2, "40", "start", INK, 13, "bold")
    t0, t1 = P(0, 40, 0), P(0, 40, 20)
    b += text(t0[0] - 10, (t0[1] + t1[1]) / 2 + 4, "20", "end", INK, 13, "bold")
    return wrap(svg(520, 300, b), "Isometric view of the same stepped block (axes at 30°, true lengths). Compare it with the three orthographic views: the step, the riser face and the top surfaces are all visible in one picture.")


def _ell(cx, cy, R, th0=0, th1=360, n=100):
    c, sn = math.cos(math.radians(30)), math.sin(math.radians(30))
    pts = []
    for i in range(n + 1):
        t = math.radians(th0 + (th1 - th0) * i / n)
        a, b_ = R * math.cos(t), R * math.sin(t)
        pts.append((cx + (a - b_) * c, cy - (a + b_) * sn))
    return pts


def d_iso_cylinder():
    s = 2.2
    R = 25 * s
    H = 60 * s
    cx, cyb = 470, 300
    cyt = cyb - H
    c = math.cos(math.radians(30))
    b = ""
    for cy in (cyt, cyb):   # bounding rhombi
        rh = [(cx, cy - R), (cx + 2 * R * c, cy), (cx, cy + R), (cx - 2 * R * c, cy)]
        b += pfill(rh, "none", GREY, 1.1).replace('stroke-linejoin="round"', 'stroke-dasharray="4,3"')
    b += line(cx - 1.2247 * R, cyb, cx - 1.2247 * R, cyt, INK, 2.6) + line(cx + 1.2247 * R, cyb, cx + 1.2247 * R, cyt, INK, 2.6)
    b += poly(_ell(cx, cyb, R, 45, 225 + 90), INK, 2.6) if False else ""
    front = [p for p in _ell(cx, cyb, R, 0, 360, 200) if p[1] >= cyb - 0.001]
    # lower (front) half of bottom ellipse = points with y >= cyb
    lower = [p for p in _ell(cx, cyb, R, 0, 360, 360) if p[1] >= cyb - 0.01]
    lower.sort(key=lambda p: p[0])
    b += poly(lower, INK, 2.6)
    b += poly(_ell(cx, cyt, R, 0, 360, 200), INK, 2.6) + f'<path d="M0,0" />'
    b += chain(cx, cyt - R, cx, cyb + R, GREY, 1)
    b += dot(cx, cyt, 3) + dot(cx, cyb, 3)
    b += dimv(cyt, cyb, cx + 1.2247 * R + 45, "60", size=13)
    b += text(cx, cyt - R - 28, "Ø50", "middle", INK, 14, "bold") + line(cx - 1.2247 * R, cyt - R - 12, cx + 1.2247 * R, cyt - R - 12, INK, 1, "2,2") if False else ""
    b += text(20, 70, "Four-centre method, isometric DRAWING (true lengths):", "start", INK, 13, "bold")
    b += text(20, 92, "1. rhombus of side = diameter (50 mm) on the 30° axes", "start", GREY, 12) + text(20, 110, "2. ellipse inside it: major axis ≈ 1.22 × 50 = 61 mm,", "start", GREY, 12)
    b += text(20, 126, "    minor axis ≈ 0.71 × 50 = 35 mm", "start", GREY, 12) + text(20, 144, "3. repeat at the top, raised by the 60 mm height", "start", GREY, 12) + text(20, 162, "4. join the two ellipses with vertical tangents", "start", GREY, 12)
    return wrap(svg(720, 340, b), "Isometric view of a vertical cylinder (Ø50 × 60), as asked in CAT-1 Q4: two identical ellipses joined by vertical tangents; only the lower half of the bottom ellipse is visible.")


def d_freehand():
    b = text(80, 20, "vertical: top → bottom", "middle", INK, 12, "bold") + line(60, 40, 60, 150, INK, 2.4) + arrow(100, 50, 100, 140, BLUE, 3, 12) + dot(60, 40, 4) + dot(60, 150, 4)
    b += text(230, 20, "horizontal: left → right", "middle", INK, 12, "bold") + line(160, 100, 310, 100, INK, 2.4) + arrow(170, 70, 300, 70, BLUE, 3, 12) + dot(160, 100, 4) + dot(310, 100, 4)
    b += text(450, 20, "inclined", "middle", INK, 12, "bold") + line(380, 150, 470, 40, INK, 2.4) + arrow(510, 60, 420, 100, BLUE, 2, 9) if False else text(430, 20, "inclined (↗ or ↙)", "middle", INK, 12, "bold") + line(380, 150, 470, 45, INK, 2.4) + dot(380, 150, 4) + dot(470, 45, 4)
    cx, cy, r = 620, 100, 46
    b += text(cx, 20, "circle", "middle", INK, 12, "bold")
    b += chain(cx - r - 10, cy, cx + r + 10, cy, GREY, 1) + chain(cx, cy - r - 10, cx, cy + r + 10, GREY, 1) + chain(cx - 38, cy - 38, cx + 38, cy + 38, GREY, 1) + chain(cx - 38, cy + 38, cx + 38, cy - 38, GREY, 1)
    for a in range(0, 360, 45):
        b += dot(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)), 3, RED)
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2.2"/>'
    b += text(cx, 178, "radius marks on centre lines", "middle", GREY, 11) + text(cx, 192, "+ diagonals, then sweep through", "middle", GREY, 11)
    b += text(60, 190, "eye on the END point; mark both end points first", "start", RED, 12, "bold")
    return wrap(svg(720, 205, b), "Freehand sketching technique from the lecture: always mark the end points, look at the end point (not the pencil tip), and build circles and ellipses from centre lines with radius marks.")


def d_persp_terms():
    gy = 230
    b = line(30, gy, 570, gy, INK, 2.4) + text(560, gy + 18, "GP (ground plane)", "end", GREY, 12, "bold")
    b += line(300, 40, 300, gy, BLUE, 2.4) + text(306, 52, "PP (picture plane)", "start", BLUE, 12, "bold") + dot(300, gy, 4) + text(292, gy + 18, "GL", "end", BLUE, 12, "bold")
    sx, sy = 90, 100
    b += dashed(30, sy, 570, sy, AMBER, 1.4) + text(570, sy - 6, "HL — horizon line (eye level)", "end", AMBER, 12, "bold")
    b += f'<circle cx="{sx}" cy="{sy}" r="9" fill="#fff" stroke="{INK}" stroke-width="2"/>' + dot(sx, sy, 3.5) + text(sx, sy - 18, "S (station point)", "middle", INK, 12, "bold")
    b += line(sx, sy, 300, sy, GREEN, 1.6) + dot(300, sy, 4, GREEN) + text(306, sy + 18, "C (centre of vision)", "start", GREEN, 12, "bold") + text(195, sy - 8, "axis of vision ⟂ PP", "middle", GREEN, 11)
    b += rect(380, 150, 70, 80, "#e8f0fc", INK, 2.4) + text(415, 195, "object", "middle", BLUE, 13, "bold")
    for (ox, oy) in ((380, 150), (380, 230)):
        t = (300 - sx) / (ox - sx)
        py = sy + t * (oy - sy)
        b += line(sx, sy, ox, oy, RED, 1.4) + dot(300, py, 4.5, RED)
    b += text(30, 44, "each visual ray from S to the object cuts the PP", "start", RED, 11) + text(30, 58, "at a perspective point (red dots)", "start", RED, 11)
    b += dimh(sx, 300, gy + 36, "distance of S in front of PP", size=11) + dimh(300, 380, gy + 36, "behind PP", size=11)
    b += dimv(sy, gy, 40, "S above GP", size=11)
    return wrap(svg(600, 290, b), "Side view of the perspective set-up (visual-ray method): the observer at S looks through the transparent picture plane PP at an object standing on the ground plane GP; where each visual ray cuts the PP is a point of the perspective image.")


def d_floorplan():
    s = 40
    ox, oy = 50, 40
    b = ""
    def wall(x1, y1, x2, y2, w=4):
        return line(ox + x1 * s, oy + y1 * s, ox + x2 * s, oy + y2 * s, INK, w)
    # outer walls
    b += rect(ox, oy, 6.8 * s, 6.0 * s, "#fbfcff", INK, 5)
    # inner walls
    b += wall(3.6, 0, 3.6, 3.6, 3) + wall(0, 3.6, 6.8, 3.6, 3) + wall(3.6, 3.6, 3.6, 6.0, 3) + wall(5.2, 3.6, 5.2, 6.0, 3)
    # doors (gap + swing)
    def door(cx, cy, w, orient):
        gap = ""
        if orient == "h":
            gap = line(ox + cx * s, oy + cy * s, ox + (cx + w) * s, oy + cy * s, "#fbfcff", 6)
            gap += line(ox + cx * s, oy + cy * s, ox + cx * s, oy + (cy + w) * s, INK, 1.6)
            gap += f'<path d="M{ox + cx*s},{oy + (cy + w)*s} A{w*s},{w*s} 0 0 0 {ox + (cx + w)*s},{oy + cy*s}" fill="none" stroke="{INK}" stroke-width="1.2"/>'
        else:
            gap = line(ox + cx * s, oy + cy * s, ox + cx * s, oy + (cy + w) * s, "#fbfcff", 6)
            gap += line(ox + cx * s, oy + cy * s, ox + (cx + w) * s, oy + cy * s, INK, 1.6)
            gap += f'<path d="M{ox + (cx + w)*s},{oy + cy*s} A{w*s},{w*s} 0 0 1 {ox + cx*s},{oy + (cy + w)*s}" fill="none" stroke="{INK}" stroke-width="1.2"/>'
        return gap
    b += door(3.6, 1.2, 0.9, "v") + door(1.4, 3.6, 0.9, "h") + door(5.2, 4.3, 0.8, "v") + door(4.0, 3.6, 0.8, "h") + door(3.6, 4.4, 0.8, "v")
    # windows (double line gaps in outer wall)
    def win(x1, y1, x2, y2):
        return line(ox + x1 * s, oy + y1 * s, ox + x2 * s, oy + y2 * s, "#fbfcff", 6) + line(ox + x1 * s, oy + y1 * s - 2 * (y1 == y2), ox + x2 * s, oy + y2 * s - 2 * (y1 == y2), BLUE, 1.4) + line(ox + x1 * s, oy + y1 * s + 2 * (y1 == y2), ox + x2 * s, oy + y2 * s + 2 * (y1 == y2), BLUE, 1.4)
    b += win(1.0, 0, 2.6, 0) + win(4.4, 0, 6.0, 0) + win(0, 4.4, 0, 5.4).replace("y1=\"", "y1=\"") 
    b += text(ox + 1.8 * s, oy + 1.8 * s, "LIVING", "middle", INK, 13, "bold") + text(ox + 1.8 * s, oy + 1.8 * s + 16, "3.6 × 3.6 m", "middle", GREY, 11)
    b += text(ox + 5.2 * s, oy + 1.8 * s, "BEDROOM", "middle", INK, 13, "bold") + text(ox + 5.2 * s, oy + 1.8 * s + 16, "3.2 × 3.6 m", "middle", GREY, 11)
    b += text(ox + 1.8 * s, oy + 4.8 * s, "KITCHEN", "middle", INK, 13, "bold") + text(ox + 1.8 * s, oy + 4.8 * s + 16, "3.6 × 2.4 m", "middle", GREY, 11)
    b += text(ox + 4.4 * s, oy + 5.5 * s, "PASSAGE", "middle", INK, 10, "bold") + text(ox + 6.0 * s, oy + 5.4 * s, "BATH", "middle", INK, 11, "bold") + text(ox + 6.0 * s, oy + 5.4 * s + 13, "1.6×2.4", "middle", GREY, 10)
    b += dimh(ox, ox + 3.6 * s, oy - 16, "3600", size=11) + dimh(ox + 3.6 * s, ox + 6.8 * s, oy - 16, "3200", size=11) + dimv(oy, oy + 3.6 * s, ox - 22, "3600", size=11) + dimv(oy + 3.6 * s, oy + 6 * s, ox - 22, "2400", size=11)
    b += text(ox + 3.4 * s, oy + 6 * s + 24, "walls: external 230 mm (thick), partitions 115 mm (thin)", "middle", GREY, 11, None, True)
    return wrap(svg(420, 350, b), "A simple one-bedroom residential plan: external walls thick, partition walls thinner, door swings as quarter-circles, windows as double lines in the wall. Dimensions in mm as in a real plan; room sizes meet the usual minimum-area rules.")


# ===================================================================== MODULE 4
def d_sand_mould():
    b = rect(40, 50, 260, 90, "#f1e7d6", INK, 2) + rect(40, 140, 260, 90, "#e6d8bf", INK, 2)
    b += text(124, 66, "COPE (upper box)", "start", INK, 12, "bold") + text(50, 222, "DRAG (lower box)", "start", INK, 12, "bold") + dashed(30, 140, 310, 140, RED, 1.6) + text(316, 144, "parting line", "start", RED, 12, "bold")
    b += rect(120, 120, 130, 40, "#fff", INK, 1.8) + text(185, 144, "mould cavity", "middle", INK, 12, "bold")
    b += rect(224, 80, 30, 40, "#fff", INK, 1.6) + text(239, 76, "riser", "middle", INK, 11, "bold")
    b += pfill([(60, 50), (110, 50), (104, 72), (66, 72)], "#fff", INK, 1.6) + text(85, 44, "pouring basin", "middle", INK, 11, "bold")
    b += rect(80, 72, 16, 68, "#fff", INK, 1.6) + text(118, 96, "sprue", "start", INK, 11, "bold") + line(114, 92, 97, 92, GREY, 1)
    b += rect(80, 140, 16, 14, "#fff", INK, 1.6) + rect(96, 142, 24, 10, "#fff", INK, 1.6) + text(105, 182, "runner & gate", "middle", INK, 11, "bold") + line(105, 168, 100, 154, GREY, 1)
    b += arrow(85, 14, 85, 46, RED, 2, 9) + text(96, 22, "molten metal", "start", RED, 11, "bold") if False else arrow(85, 8, 85, 40, RED, 2, 9) + text(96, 14, "molten metal", "start", RED, 11, "bold")
    b += text(420, 60, "Steps:", "start", INK, 13, "bold")
    for i, t in enumerate(("1 pattern making (with allowances)", "2 mould making (sand packed round pattern)", "3 core setting, closing the mould", "4 melting & pouring", "5 solidification & cooling", "6 shake-out, fettling (cut gates/risers), inspection")):
        b += text(420, 80 + i * 20, t, "start", GREY, 12)
    return wrap(svg(760, 250, b), "Sand-casting mould (cross-section): metal runs down the sprue, along the runner and gate into the cavity; the riser feeds extra molten metal as the casting shrinks.")


def d_pattern_allowances():
    b = ""
    def shape(x, y, w, h, taper=0, stroke=INK, dash=None, sw=2.2, fill="none"):
        pts = [(x - taper, y + h), (x + taper, y), (x + w - taper, y), (x + w + taper, y + h)]
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<polygon points="{" ".join(f"{a:.1f},{b_:.1f}" for a, b_ in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
    cx, cy = 200, 40
    b += shape(cx + 20, cy + 20, 200, 120, 0, INK, None, 3) + shape(cx + 10, cy + 10, 220, 140, 0, GREY, "3,3", 2.2) + shape(cx, cy, 240, 160, 4, BLUE, "14,3,2,3", 2.2)
    b += line(cx - 20, cy + 6 + 160 / 2, cx + 244, cy + 6 + 160 / 2, "#aaa", 1.2, "8,3") if False else ""
    b += text(30, 70, "component", "start", INK, 13, "bold") + text(30, 86, "(full line)", "start", GREY, 11) + line(110, 72, cx + 24, 78, INK, 1)
    b += text(30, 120, "casting size = component", "start", GREY, 13, "bold") + text(30, 136, "+ machining allowance (dotted)", "start", GREY, 11) + line(190, 124, cx + 12, 124, GREY, 1)
    b += text(30, 170, "pattern size = casting", "start", BLUE, 13, "bold") + text(30, 186, "+ shrinkage (chain-dotted)", "start", BLUE, 11) + line(180, 172, cx + 2, 172, BLUE, 1)
    b += text(cx + 120, cy + 188, "draft: vertical faces ⟂ parting line are tapered", "middle", RED, 12, "bold") + line(cx + 120, cy + 172, cx + 238, cy + 150, RED, 1)
    return wrap(svg(520, 250, b), "Pattern allowances (CAT-1 Q5): the pattern is made larger than the finished component — for shrinkage on cooling and extra stock to machine off — and its vertical faces are tapered (draft) so it can be withdrawn from the sand without damaging the mould.")


def d_cnc_loop():
    b = box(10, 40, 100, 56, "Part program\n(G / M codes)") + box(150, 40, 100, 56, "Machine control\nunit (MCU)") + box(290, 40, 100, 56, "Drive\namplifier") + box(430, 40, 100, 56, "Servo\nmotor")
    b += box(570, 40, 100, 56, "Ball screw\n+ table / spindle", "#fff7cc")
    for x in (110, 250, 390, 530):
        b += arrow(x, 68, x + 40, 68, INK, 2, 9)
    b += box(430, 150, 100, 46, "Encoder /\nfeedback", "#e6f4ec") + line(620, 96, 620, 173, GREY, 2) + arrow(620, 173, 532, 173, GREY, 2, 9) + arrow(430, 173, 200, 173, GREEN, 2, 9) + line(200, 173, 200, 98, GREEN, 2) + arrow(200, 120, 200, 98, GREEN, 2, 9)
    b += text(315, 216, "position / speed feedback (closed loop)", "middle", GREEN, 12, "bold")
    return wrap(svg(690, 230, b), "A CNC axis: the controller turns the program into commands, the drive and servo motor move the table through a ball screw, and an encoder reports the real position back so the controller can correct any error.")


def d_fdm():
    b = rect(110, 230, 240, 18, "#d9dde6", INK, 2) + text(230, 244, "build platform (heated bed)", "middle", INK, 11, "bold")
    for i in range(8):
        b += rect(150, 218 - i * 7, 160, 7, "#9ab8ef" if i % 2 else "#b8cdf5", INK, 1)
    b += text(330, 190, "printed part, built", "start", GREY, 11) + text(330, 204, "layer by layer", "start", GREY, 11)
    b += rect(205, 110, 50, 34, "#f2c94c", INK, 2) + text(230, 131, "heater", "middle", INK, 11, "bold") + pfill([(213, 144), (247, 144), (237, 160), (223, 160)], "#cfd4dd", INK, 2) + text(262, 156, "nozzle", "start", INK, 11, "bold")
    b += line(230, 48, 230, 110, RED, 3) + text(240, 78, "filament", "start", RED, 12, "bold")
    b += f'<circle cx="230" cy="26" r="22" fill="#fff" stroke="{INK}" stroke-width="2"/>' + text(230, 30, "spool", "middle", INK, 11)
    b += arrow(150, 104, 190, 104, BLUE, 2, 9) + arrow(270, 104, 310, 104, BLUE, 2, 9) + text(340, 108, "nozzle moves in X–Y", "start", BLUE, 12, "bold")
    b += arrow(60, 190, 60, 226, PURP, 2, 9) + text(10, 262, "platform lowers", "start", PURP, 11, "bold") + text(10, 276, "one layer in Z", "start", PURP, 11, "bold")
    return wrap(svg(540, 290, b), "FDM / FFF 3D printing: a heated nozzle melts thermoplastic filament and deposits it in a path; after each layer the platform moves down (or the nozzle up) by the layer height.")


def _piston_panel(ox, title, th_deg, arrow_dir, valves, gas, spark=False):
    r, l = 18, 72
    yc = 190
    th = math.radians(th_deg)
    pin_y = yc - r * math.cos(th) - math.sqrt(l * l - (r * math.sin(th)) ** 2)
    cx = ox + 60
    b = text(cx, 14, title, "middle", INK, 13, "bold") + '<g transform="translate(0,36)">'
    top, bottom = 38, 150
    crown = pin_y - 8
    if gas:
        b += rect(cx - 32, top, 64, crown - top, gas, "none", 0)
    b += line(cx - 34, top, cx - 34, bottom, INK, 3) + line(cx + 34, top, cx + 34, bottom, INK, 3) + line(cx - 34, top, cx + 34, top, INK, 4)
    b += rect(cx - 32, crown, 64, 16, "#c9d2e3", INK, 2) + line(cx, crown + 16, cx + r * math.sin(th), yc - r * math.cos(th), INK, 4)
    b += f'<circle cx="{cx}" cy="{yc}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="2"/>' + dot(cx + r * math.sin(th), yc - r * math.cos(th), 4, RED) + dot(cx, yc, 2.5)
    b += arc_arrow(cx, yc, r + 9, -150, -60, PURP, 2)
    for side, kind in (("L", valves[0]), ("R", valves[1])):
        vx = cx - 18 if side == "L" else cx + 18
        lift = 9 if kind == "open" else 0
        b += line(vx, top - 18 - lift, vx, top - lift + 2, INK, 3) + line(vx - 7, top - lift + 2, vx + 7, top - lift + 2, INK, 3)
        b += text(vx, top - 24 - lift, "IN" if side == "L" else "EX", "middle", GREEN if kind == "open" else GREY, 10, "bold")
    if spark:
        b += pfill([(cx - 3, top + 2), (cx + 4, top + 12), (cx - 1, top + 12), (cx + 5, top + 26), (cx - 6, top + 14), (cx - 1, top + 14)], "#f2c94c", "#b8860b", 1)
    ay = crown + 8
    if arrow_dir == "down":
        b += arrow(cx + 44, ay - 10, cx + 44, ay + 22, RED, 2.2, 9)
    else:
        b += arrow(cx + 44, ay + 22, cx + 44, ay - 10, RED, 2.2, 9)
    return b + "</g>"


def d_four_stroke():
    b = ""
    panels = [("1  Suction", 60, "down", ("open", "closed"), "#dbeafe", False), ("2  Compression", 300, "up", ("closed", "closed"), "#bfd3f5", False),
              ("3  Power", 60, "down", ("closed", "closed"), "#ffd9a8", True), ("4  Exhaust", 300, "up", ("closed", "open"), "#dcdcdc", False)]
    for i, (t, th, d, v, g, sp) in enumerate(panels):
        b += _piston_panel(10 + i * 150, t, th, d, v, g, sp)
    b += text(300, 288, "fuel-air in  →  squeezed  →  burns and expands (spark)  →  burnt gas out", "middle", GREY, 12, None, True)
    return wrap(svg(620, 300, b), "Four-stroke petrol (SI) engine: one power stroke every two crank revolutions (720°). Valves open only for suction (IN) and exhaust (EX); the shading shows fresh charge, compressed charge, burning gas and exhaust above the piston. Red arrow = piston direction.")


def d_rankine():
    b = box(30, 40, 120, 60, "Boiler\n(steam generator)", "#fde8d9") + pfill([(240, 40), (240, 100), (320, 85), (320, 55)], "#d4e8d0", INK, 2) + text(280, 74, "Turbine", "middle", INK, 12, "bold")
    b += f'<circle cx="400" cy="70" r="24" fill="#fff" stroke="{INK}" stroke-width="2"/>' + text(400, 75, "G", "middle", INK, 16, "bold") + line(320, 70, 376, 70, INK, 3)
    b += box(240, 170, 100, 50, "Condenser", "#d4dff0") + box(30, 170, 120, 50, "Feed pump", "#eee")
    b += arrow(150, 70, 238, 70, RED, 2.5, 10) + text(194, 56, "HP steam", "middle", RED, 11, "bold")
    b += arrow(280, 100, 280, 168, GREY, 2.5, 10) + text(288, 138, "exhaust steam", "start", GREY, 11, "bold")
    b += arrow(240, 195, 152, 195, BLUE, 2.5, 10) + text(196, 187, "water", "middle", BLUE, 11, "bold")
    b += arrow(90, 168, 90, 102, BLUE, 2.5, 10) + text(98, 140, "feed water", "start", BLUE, 11, "bold")
    b += arrow(60, 18, 60, 38, INK, 2, 9) + text(30, 12, "fuel + air", "start", INK, 11, "bold")
    b += arrow(345, 205, 395, 205, BLUE, 2, 9) + text(400, 209, "cooling water in/out", "start", BLUE, 11)
    b += text(440, 74, "→ electrical output", "start", GREEN, 12, "bold")
    return wrap(svg(640, 240, b), "Steam (Rankine-cycle) power plant: the boiler makes high-pressure steam, the turbine expands it to drive the generator, the condenser turns the exhaust back into water and the pump returns it to the boiler.")


def d_vcr():
    b = box(250, 30, 170, 50, "CONDENSER\n(rejects heat Q_H)", "#fde8d9") + box(250, 210, 170, 50, "EVAPORATOR\n(absorbs heat Q_L)", "#d4e8f5")
    b += f'<circle cx="530" cy="145" r="42" fill="#fff" stroke="{INK}" stroke-width="2.4"/>' + text(530, 141, "COMPRESSOR", "middle", INK, 9.5, "bold") + text(530, 156, "(work W in)", "middle", INK, 9.5)
    b += pfill([(100, 130), (140, 130), (100, 160), (140, 160)], "#fff", INK, 2.4) + text(86, 140, "EXPANSION", "end", INK, 10, "bold") + text(86, 154, "VALVE", "end", INK, 10, "bold")
    b += line(420, 55, 530, 55, RED, 2.6) + arrow(530, 55, 530, 101, RED, 2.6, 10) + text(540, 80, "2: hot HP vapour", "start", RED, 11, "bold")
    b += line(420, 235, 530, 235, BLUE, 2.6) + arrow(530, 235, 530, 189, BLUE, 2.6, 10) + text(540, 215, "1: LP vapour", "start", BLUE, 11, "bold")
    b += line(250, 55, 120, 55, AMBER, 2.6) + arrow(120, 55, 120, 128, AMBER, 2.6, 10) + text(112, 95, "3: HP liquid", "end", AMBER, 11, "bold")
    b += line(120, 162, 120, 235, "#5b8bd6", 2.6) + arrow(120, 235, 248, 235, "#5b8bd6", 2.6, 10) + text(185, 258, "4: cold mixture", "middle", "#5b8bd6", 11, "bold")
    b += text(335, 22, "Q_H → rejected to the surroundings", "middle", RED, 11, "bold")
    b += text(335, 284, "Q_L ← absorbed from the cold space", "middle", BLUE, 11, "bold")
    b += text(335, 150, "COP = Q_L / W", "middle", INK, 15, "bold")
    return wrap(svg(640, 296, b), "Vapour-compression refrigeration cycle: compressor raises pressure; the condenser rejects heat; the expansion valve drops pressure and temperature; the evaporator absorbs heat from the cold space.")


def d_fuel_cell():
    b = rect(110, 100, 90, 140, "#e8f0fc", INK, 2.4) + rect(200, 100, 100, 140, "#f6e9ff", INK, 2) + rect(300, 100, 90, 140, "#e6f4ec", INK, 2.4)
    b += text(155, 92, "ANODE", "middle", BLUE, 12, "bold") + text(250, 92, "ELECTROLYTE", "middle", PURP, 11, "bold") + text(345, 92, "CATHODE", "middle", GREEN, 12, "bold")
    b += arrow(20, 170, 106, 170, BLUE, 2.6, 10) + text(20, 158, "H₂ in", "start", BLUE, 13, "bold") + arrow(480, 170, 394, 170, GREEN, 2.6, 10) + text(480, 158, "O₂ (air) in", "end", GREEN, 13, "bold")
    b += text(155, 135, "H₂ → 2H⁺", "middle", BLUE, 11, "bold") + text(155, 150, "+ 2e⁻", "middle", BLUE, 11, "bold")
    b += text(345, 130, "½O₂ + 2H⁺", "middle", GREEN, 11, "bold") + text(345, 145, "+ 2e⁻ → H₂O", "middle", GREEN, 11, "bold")
    b += arrow(214, 200, 286, 200, PURP, 2.4, 9) + text(250, 220, "H⁺ ions", "middle", PURP, 11, "bold")
    b += line(155, 100, 155, 44, RED, 2.4) + line(155, 44, 345, 44, RED, 2.4) + line(345, 44, 345, 100, RED, 2.4)
    b += rect(230, 32, 40, 24, "#fff", INK, 2) + text(250, 48, "load", "middle", INK, 11, "bold") + arrow(168, 44, 226, 44, RED, 2.2, 9) + text(190, 36, "e⁻ flow", "middle", RED, 11, "bold")
    b += arrow(345, 242, 345, 272, GREEN, 2.4, 9) + text(354, 266, "water + heat out", "start", GREEN, 12, "bold")
    return wrap(svg(520, 285, b), "Hydrogen PEM fuel cell: hydrogen splits at the anode, protons cross the membrane, electrons take the external circuit (the useful current) and all meet oxygen at the cathode to make water.")


def d_fourbar():
    O2, O4 = (130, 230), (330, 230)
    r, cpl, rk = 50, 150, 110
    th = math.radians(75)
    A = (O2[0] + r * math.cos(th), O2[1] - r * math.sin(th))
    dx, dy = O4[0] - A[0], O4[1] - A[1]
    d = math.hypot(dx, dy)
    aa = (cpl ** 2 - rk ** 2 + d ** 2) / (2 * d)
    h = math.sqrt(max(cpl ** 2 - aa ** 2, 0))
    xm, ym = A[0] + aa * dx / d, A[1] + aa * dy / d
    B = (xm + h * dy / d, ym - h * dx / d)
    if B[1] > A[1] + 10 or B[0] < A[0] - 5:
        B = (xm - h * dy / d, ym + h * dx / d)
    b = line(O2[0], O2[1], O4[0], O4[1], INK, 5)
    for p in (O2, O4):
        b += pfill([(p[0], p[1]), (p[0] - 14, p[1] + 20), (p[0] + 14, p[1] + 20)], "#e0e3ea", INK, 1.6) + line(p[0] - 20, p[1] + 20, p[0] + 20, p[1] + 20, INK, 2.4)
    b += line(O2[0], O2[1], A[0], A[1], RED, 5) + line(A[0], A[1], B[0], B[1], BLUE, 5) + line(O4[0], O4[1], B[0], B[1], GREEN, 5)
    for p in (O2, O4, A, B):
        b += f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="7" fill="#fff" stroke="{INK}" stroke-width="2.4"/>'
    b += text(230, 252, "link 1: frame (fixed) = 200", "middle", INK, 12, "bold") + text(O2[0] - 14, (O2[1] + A[1]) / 2, "link 2: crank = 50", "end", RED, 12, "bold")
    b += text((A[0] + B[0]) / 2 - 4, (A[1] + B[1]) / 2 - 14, "link 3: coupler = 150", "end", BLUE, 12, "bold") + text(O4[0] + 16, (O4[1] + B[1]) / 2, "link 4: rocker = 110", "start", GREEN, 12, "bold")
    b += text(O2[0], O2[1] + 40, "O₂", "middle", GREY, 11) + text(O4[0], O4[1] + 40, "O₄", "middle", GREY, 11) + text(A[0] + 12, A[1] - 8, "A", "start", GREY, 11) + text(B[0] + 4, B[1] - 12, "B", "middle", GREY, 11)
    b += text(480, 70, "Grashof's law: s + l ≤ p + q", "start", INK, 14, "bold") + text(480, 92, "s = 50, l = 200, p, q = 150, 110", "start", GREY, 12)
    b += text(480, 112, "50 + 200 = 250 ≤ 150 + 110 = 260  ✓", "start", GREEN, 12, "bold") + text(480, 134, "shortest link (crank) is next to the frame", "start", GREY, 12) + text(480, 152, "⇒ CRANK-ROCKER (crank turns fully,", "start", GREY, 12) + text(480, 168, "rocker only swings)", "start", GREY, 12)
    return wrap(svg(720, 290, b), "A four-bar mechanism: four rigid links, four revolute pairs, one degree of freedom (3(n−1) − 2j = 3·3 − 2·4 = 1). With these lengths Grashof's condition holds and it is a crank-rocker.")


def d_hexapod():
    cx = 200
    bc, tc = (cx, 230), (cx, 90)
    brx, bry, trx, tr_y = 140, 36, 90, 24
    b = f'<ellipse cx="{bc[0]}" cy="{bc[1]}" rx="{brx}" ry="{bry}" fill="#e9edf5" stroke="{INK}" stroke-width="2.4"/>' + text(bc[0], bc[1] + 62, "fixed base", "middle", INK, 12, "bold")
    base_ang = [20, 100, 140, 220, 260, 340]
    top_ang = [40, 80, 160, 200, 280, 320]
    pts_b = [(bc[0] + brx * math.cos(math.radians(a)), bc[1] + bry * math.sin(math.radians(a))) for a in base_ang]
    pts_t = [(tc[0] + trx * math.cos(math.radians(a)), tc[1] + tr_y * math.sin(math.radians(a))) for a in top_ang]
    for pb, pt in zip(pts_b, pts_t):
        mx, my = pb[0] + (pt[0] - pb[0]) * 0.5, pb[1] + (pt[1] - pb[1]) * 0.5
        b += line(pb[0], pb[1], mx, my, INK, 5) + line(mx, my, pt[0], pt[1], "#7c8aa8", 3)
        b += f'<circle cx="{pb[0]:.1f}" cy="{pb[1]:.1f}" r="4" fill="#fff" stroke="{INK}" stroke-width="2"/><circle cx="{pt[0]:.1f}" cy="{pt[1]:.1f}" r="4" fill="#fff" stroke="{INK}" stroke-width="2"/>'
    b += f'<ellipse cx="{tc[0]}" cy="{tc[1]}" rx="{trx}" ry="{tr_y}" fill="#f3e9ff" stroke="{PURP}" stroke-width="2.4"/>' + text(tc[0], tc[1] + 5, "moving platform", "middle", PURP, 12, "bold")
    b += text(350, 100, "6 telescopic (linear)", "start", INK, 13, "bold") + text(350, 118, "actuators, each with a", "start", INK, 13, "bold") + text(350, 136, "universal/spherical joint", "start", INK, 13, "bold") + text(350, 154, "at both ends.", "start", INK, 13, "bold")
    b += text(350, 184, "Changing the six lengths moves", "start", GREY, 12) + text(350, 200, "the platform in all 6 degrees of", "start", GREY, 12) + text(350, 216, "freedom (3 translations + 3 rotations).", "start", GREY, 12)
    return wrap(svg(620, 300, b), "Hexapod (Stewart platform): a parallel mechanism in which six variable-length legs connect a fixed base to a moving platform — used in flight simulators, machine-tool positioning tables and precision alignment.")


def d_hydraulic():
    b = rect(60, 100, 90, 120, "#cfe2f7", INK, 2.4) + rect(150, 190, 200, 30, "#cfe2f7", INK, 2.4) + rect(350, 70, 190, 150, "#cfe2f7", INK, 2.4)
    b += rect(70, 100, 70, 14, "#9aa3b2", INK, 2) + line(105, 60, 105, 100, INK, 5) + arrow(105, 18, 105, 56, RED, 3, 12) + text(120, 36, "F₁", "start", RED, 16, "bold")
    b += rect(372, 70, 146, 14, "#9aa3b2", INK, 2) + line(445, 50, 445, 70, INK, 5) + arrow(445, 46, 445, 8, GREEN, 3, 12) + text(462, 30, "F₂", "start", GREEN, 16, "bold")
    b += text(300, 150, "incompressible fluid —", "middle", BLUE, 12, "bold") + text(300, 166, "same pressure p everywhere", "middle", BLUE, 12, "bold")
    b += text(105, 244, "small piston, area A₁", "middle", INK, 12, "bold") + text(445, 244, "large piston, area A₂", "middle", INK, 12, "bold")
    b += text(105, 268, "p = F₁ / A₁", "middle", INK, 14, "bold") + text(445, 268, "F₂ = p·A₂ = F₁ (A₂ / A₁)", "middle", INK, 14, "bold")
    b += text(300, 296, "force is multiplied by A₂/A₁, but the large piston moves only A₁/A₂ as far", "middle", GREY, 12, None, True)
    return wrap(svg(600, 308, b), "Pascal's law in a hydraulic press: pressure applied to a confined liquid is transmitted equally in all directions, so a small force on a small piston balances a large force on a large piston.")


def d_robot_arm():
    O = (110, 250)
    L1, L2 = 150, 110
    t1, t2 = math.radians(40), math.radians(45)
    J = (O[0] + L1 * math.cos(t1), O[1] - L1 * math.sin(t1))
    E = (J[0] + L2 * math.cos(t1 + t2), J[1] - L2 * math.sin(t1 + t2))
    b = rect(70, 250, 80, 20, "#cfd4dd", INK, 2) + rect(95, 232, 30, 18, "#9aa3b2", INK, 2)
    b += line(O[0], O[1], O[0] + 240, O[1], GREY, 1, "4,3") + line(O[0], O[1], J[0], J[1], BLUE, 9) + line(J[0], J[1], E[0], E[1], GREEN, 7)
    b += dashed(J[0], J[1], J[0] + 90 * math.cos(t1), J[1] - 90 * math.sin(t1), GREY, 1.2)
    b += f'<path d="M{O[0]+60},{O[1]} A60,60 0 0 0 {O[0]+60*math.cos(t1):.1f},{O[1]-60*math.sin(t1):.1f}" fill="none" stroke="{RED}" stroke-width="2"/>' + text(O[0] + 74, O[1] - 18, "θ₁", "start", RED, 14, "bold")
    b += f'<path d="M{J[0]+50*math.cos(t1):.1f},{J[1]-50*math.sin(t1):.1f} A50,50 0 0 0 {J[0]+50*math.cos(t1+t2):.1f},{J[1]-50*math.sin(t1+t2):.1f}" fill="none" stroke="{RED}" stroke-width="2"/>' + text(J[0] + 56, J[1] - 40, "θ₂", "start", RED, 14, "bold")
    for p in (O, J):
        b += f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="9" fill="#fff" stroke="{INK}" stroke-width="2.6"/>'
    ex, ey = E[0] + 14 * math.cos(t1 + t2), E[1] - 14 * math.sin(t1 + t2)
    b += line(E[0], E[1], ex - 6 * math.sin(t1 + t2), ey - 6 * math.cos(t1 + t2), INK, 3) + line(E[0], E[1], ex + 6 * math.sin(t1 + t2), ey + 6 * math.cos(t1 + t2), INK, 3)
    b += text((O[0] + J[0]) / 2 - 10, (O[1] + J[1]) / 2 - 12, "L₁", "end", BLUE, 14, "bold") + text((J[0] + E[0]) / 2 + 12, (J[1] + E[1]) / 2 - 10, "L₂", "start", GREEN, 14, "bold")
    b += text(E[0] + 20, E[1] - 12, "end effector (x, y)", "start", INK, 12, "bold") + text(O[0] + 4, O[1] + 40, "base (fixed)", "middle", GREY, 12)
    b += text(330, 230, "x = L₁cosθ₁ + L₂cos(θ₁+θ₂)", "start", INK, 13, "bold") + text(330, 250, "y = L₁sinθ₁ + L₂sin(θ₁+θ₂)", "start", INK, 13, "bold")
    return wrap(svg(620, 305, b), "A two-link planar manipulator (two revolute joints, 2 degrees of freedom): the joint angles θ₁, θ₂ fix the position of the end effector — forward kinematics.")


MODULE3 = [d_sheet_sizes, d_title_block, d_line_types, d_dim_elements, d_dim_systems, d_quadrants, d_first_third, d_step_views, d_solids, d_iso_scale, d_iso_axes_cube, d_iso_step, d_iso_cylinder, d_freehand, d_persp_terms, d_floorplan]
MODULE4 = [d_sand_mould, d_pattern_allowances, d_cnc_loop, d_fdm, d_four_stroke, d_rankine, d_vcr, d_fuel_cell, d_fourbar, d_hexapod, d_hydraulic, d_robot_arm]

if __name__ == "__main__":
    import os
    from playwright.sync_api import sync_playwright
    os.makedirs("_dgb", exist_ok=True)
    fns = MODULE3 + MODULE4
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 980, "height": 400})
        for f in fns:
            pg.set_content(f'<body style="margin:0;background:#fff;font-family:Arial"><div style="width:960px;padding:6px;text-align:center">{f()}</div></body>')
            pg.screenshot(path=f"_dgb/{f.__name__}.png", full_page=True)
        br.close()
    print(len(fns))
