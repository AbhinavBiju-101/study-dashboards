"""All diagrams for the notes, drawn with one small symbol library so orientation,
sizes and label placement are consistent. Each function returns a <div class="diagram">.
Run `python diagrams.py` to write PNG previews to _diag/ for visual checking."""
import math, re

INK, RED, BLUE, GREEN, PURP, GREY, AMBER = "#1b1f24", "#c0392b", "#1e468c", "#166e3c", "#7c3aed", "#8a93a3", "#d4a017"


# ------------------------------------------------------------------ primitives
def svg(w, h, body):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" style="max-width:100%;height:auto" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI, Arial, sans-serif" '
            f'font-size="13" fill="{INK}">{body}</svg>')


def line(x1, y1, x2, y2, c=INK, w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{w}"{d} stroke-linecap="round"/>'


def text(x, y, s, anchor="middle", c=INK, size=13, weight=None, italic=False):
    wt = f' font-weight="{weight}"' if weight else ""
    it = ' font-style="italic"' if italic else ""
    s = re.sub(r"_(\w+)", r'<tspan baseline-shift="sub" font-size="75%">\1</tspan>', s)
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" fill="{c}" font-size="{size}"{wt}{it}>{s}</text>'


def dot(x, y, r=4, c=INK):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}"/>'


def head(x2, y2, ux, uy, c, size=9):
    nx, ny = -uy, ux
    bx, by = x2 - ux * size, y2 - uy * size
    pts = f"{x2:.1f},{y2:.1f} {bx + nx * size * .42:.1f},{by + ny * size * .42:.1f} {bx - nx * size * .42:.1f},{by - ny * size * .42:.1f}"
    return f'<polygon points="{pts}" fill="{c}"/>'


def arrow(x1, y1, x2, y2, c=RED, w=2, size=9, dash=None):
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    return line(x1, y1, x2 - ux * size * .8, y2 - uy * size * .8, c, w, dash) + head(x2, y2, ux, uy, c, size)


def arc_arrow(cx, cy, r, a1, a2, c=PURP, w=2):
    """clockwise arc from angle a1 to a2 (degrees, SVG orientation) with arrowhead."""
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    p2 = (cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2)))
    large = 1 if (a2 - a1) % 360 > 180 else 0
    ux, uy = -math.sin(math.radians(a2)), math.cos(math.radians(a2))
    return (f'<path d="M{p1[0]:.1f},{p1[1]:.1f} A{r},{r} 0 {large} 1 {p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{c}" stroke-width="{w}"/>'
            + head(p2[0], p2[1], ux, uy, c, 8))


def _frame(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    return L, math.degrees(math.atan2(dy, dx)), (x1 + x2) / 2, (y1 + y2) / 2, dx / L, dy / L


_DIR = {"top": (0, -1), "bottom": (0, 1), "left": (-1, 0), "right": (1, 0)}


def _label(mx, my, s, side, off, c=INK, weight=None):
    dx, dy = _DIR[side]
    x, y = mx + dx * off, my + dy * off
    anchor = {"left": "end", "right": "start"}.get(side, "middle")
    y += 4 if side in ("left", "right") else (4 if side == "bottom" else 0)
    return text(x, y, s, anchor, c, 13, weight)


def _g(mx, my, ang, inner, stroke=INK, fill="none"):
    return (f'<g transform="translate({mx:.1f},{my:.1f}) rotate({ang:.1f})" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="2" stroke-linejoin="round" stroke-linecap="round">{inner}</g>')


def _default_side(x1, y1, x2, y2):
    return "top" if abs(x2 - x1) >= abs(y2 - y1) else "right"


def res(x1, y1, x2, y2, label=None, side=None):
    L, ang, mx, my, ux, uy = _frame(x1, y1, x2, y2)
    b = 30
    pts = [(-b, 0)] + [(-b + 60 * (i + .5) / 6, -9 if i % 2 == 0 else 9) for i in range(6)] + [(b, 0)]
    inner = (f'<line x1="{-L/2:.1f}" y1="0" x2="{-b}" y2="0"/><line x1="{b}" y1="0" x2="{L/2:.1f}" y2="0"/>'
             f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}"/>')
    out = _g(mx, my, ang, inner)
    if label:
        s = side or _default_side(x1, y1, x2, y2)
        out += _label(mx, my, label, s, 18 if s in ("top", "bottom") else 20)
    return out


def ind(x1, y1, x2, y2, label=None, side=None):
    L, ang, mx, my, ux, uy = _frame(x1, y1, x2, y2)
    inner = (f'<line x1="{-L/2:.1f}" y1="0" x2="-28" y2="0"/><line x1="28" y1="0" x2="{L/2:.1f}" y2="0"/>'
             '<path d="M-28,0 a7,7 0 0 1 14,0 a7,7 0 0 1 14,0 a7,7 0 0 1 14,0 a7,7 0 0 1 14,0"/>')
    out = _g(mx, my, ang, inner)
    if label:
        s = side or _default_side(x1, y1, x2, y2)
        out += _label(mx, my, label, s, 22 if s in ("top", "bottom") else 20)
    return out


def vsrc(x1, y1, x2, y2, label=None, side=None, plus="end", signs=True):
    """DC battery from p1 to p2; the LONG plate (+) sits at the `plus` end."""
    L, ang, mx, my, ux, uy = _frame(x1, y1, x2, y2)
    lp, sp = (4, -4) if plus == "end" else (-4, 4)
    inner = (f'<line x1="{-L/2:.1f}" y1="0" x2="{min(lp, sp)}" y2="0"/><line x1="{max(lp, sp)}" y1="0" x2="{L/2:.1f}" y2="0"/>'
             f'<line x1="{lp}" y1="-15" x2="{lp}" y2="15" stroke-width="3.5"/><line x1="{sp}" y1="-8" x2="{sp}" y2="8" stroke-width="3.5"/>')
    out = _g(mx, my, ang, inner)
    s = side or ("left" if abs(y2 - y1) > abs(x2 - x1) else "top")
    if label:
        out += _label(mx, my, label, s, 24 if s in ("left", "right") else 24)
    if signs:
        ox, oy = _DIR[s]
        sgn_plus = 1 if plus == "end" else -1
        for k, ch in ((sgn_plus, "+"), (-sgn_plus, "−")):
            out += text(mx - ox * 15 + ux * 15 * k, my - oy * 15 + uy * 15 * k + 5, ch, "middle", INK, 14, "bold")
    return out


def isrc(x1, y1, x2, y2, label=None, side=None):
    L, ang, mx, my, ux, uy = _frame(x1, y1, x2, y2)
    inner = (f'<line x1="{-L/2:.1f}" y1="0" x2="-18" y2="0"/><line x1="18" y1="0" x2="{L/2:.1f}" y2="0"/>'
             '<circle cx="0" cy="0" r="18"/>')
    out = _g(mx, my, ang, inner)
    out += arrow(mx - ux * 10, my - uy * 10, mx + ux * 11, my + uy * 11, INK, 2, 8)
    if label:
        s = side or ("left" if abs(y2 - y1) > abs(x2 - x1) else "top")
        out += _label(mx, my, label, s, 30)
    return out


def acsrc(x1, y1, x2, y2, label=None, side=None):
    L, ang, mx, my, ux, uy = _frame(x1, y1, x2, y2)
    inner = (f'<line x1="{-L/2:.1f}" y1="0" x2="-18" y2="0"/><line x1="18" y1="0" x2="{L/2:.1f}" y2="0"/>'
             '<circle cx="0" cy="0" r="18"/>')
    out = _g(mx, my, ang, inner)
    out += (f'<path d="M{mx-10:.1f},{my:.1f} q5,-10 10,0 t10,0" fill="none" stroke="{INK}" stroke-width="2"/>')
    if label:
        s = side or ("left" if abs(y2 - y1) > abs(x2 - x1) else "top")
        out += _label(mx, my, label, s, 30)
    return out


def motor(cx, cy, r=22):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="2"/>'
            + text(cx, cy + 5, "M", "middle", INK, 15, "bold"))


def sine_pts(x0, ymid, w, amp, deg0=0, deg1=360, phase=0, n=240):
    pts = []
    for i in range(n + 1):
        a = deg0 + (deg1 - deg0) * i / n
        pts.append((x0 + (a - deg0) / (deg1 - deg0) * w, ymid - amp * math.sin(math.radians(a - phase))))
    return pts


def poly(pts, c=PURP, w=2.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linejoin="round"{d}/>'


def wrap(body_svg, caption):
    caption = re.sub(r"(\w)_(\w+)", r"\1<sub>\2</sub>", caption)
    return f'<div class="diagram">\n{body_svg}\n<p class="caption">{caption}</p>\n</div>'


# ------------------------------------------------------------------ Topic 1
def d_ohm():
    b = ""
    L, R, T, B = 110, 350, 45, 165
    b += line(L, T, R, T) + line(L, B, R, B)
    b += vsrc(L, B, L, T, "V = 12 V", "left")
    b += res(R, T, R, B, "R = 4 Ω", "right")
    b += arrow(190, T, 260, T, RED, 2.5) + text(225, T - 12, "I", "middle", RED, 15, "bold")
    return wrap(svg(480, 210, b), "A single-loop circuit: the source drives current I clockwise (leaving its + plate) through R. Ohm's law links V, I and R.")


def d_kcl_kvl():
    b = ""
    # KCL panel
    nx, ny = 150, 100
    b += line(40, 40, nx, ny) + line(40, 160, nx, ny) + line(nx, ny, 260, ny)
    b += dot(nx, ny, 5)
    b += arrow(72, 58, 118, 84, RED, 2.5) + arrow(72, 142, 118, 116, RED, 2.5) + arrow(175, ny, 235, ny, RED, 2.5)
    b += text(36, 34, "I₁", "end", RED, 14, "bold") + text(36, 174, "I₂", "end", RED, 14, "bold") + text(248, ny - 10, "I₃", "middle", RED, 14, "bold")
    b += text(150, 205, "KCL: I₁ + I₂ = I₃", "middle", INK, 14, "bold")
    # KVL panel
    x0 = 380
    b += line(x0 + 30, 40, x0 + 300, 40) + line(x0 + 30, 160, x0 + 300, 160)
    b += vsrc(x0 + 30, 160, x0 + 30, 40, "V", "left")
    b += res(x0 + 30, 40, x0 + 165, 40, "R₁") + res(x0 + 165, 40, x0 + 300, 40, "R₂")
    b += line(x0 + 300, 40, x0 + 300, 160)
    b += arc_arrow(x0 + 165, 100, 32, -60, 230, PURP, 2.5) + text(x0 + 165, 105, "loop", "middle", PURP, 13, None, True)
    b += text(x0 + 165, 205, "KVL: V = I·R₁ + I·R₂", "middle", INK, 14, "bold")
    return wrap(svg(720, 220, b), "Left: KCL at a node — the arrows into the dot balance the arrow out. Right: KVL round the dashed loop — the source's rise equals the two resistors' drops.")


def d_series_parallel():
    b = text(130, 24, "Series", "middle", INK, 15, "bold")
    b += res(20, 90, 130, 90, "R₁") + res(130, 90, 240, 90, "R₂") + dot(20, 90) + dot(240, 90)
    b += text(130, 140, "same current I through R₁ and R₂", "middle", GREY, 13)
    x = 360
    b += text(x + 130, 24, "Parallel", "middle", INK, 15, "bold")
    b += line(x, 60, x, 130) + line(x + 260, 60, x + 260, 130)
    b += res(x, 60, x + 260, 60, "R₁") + res(x, 130, x + 260, 130, "R₂", "bottom")
    b += line(x - 30, 95, x, 95) + line(x + 260, 95, x + 290, 95) + dot(x - 30, 95) + dot(x + 290, 95) + dot(x, 95) + dot(x + 260, 95)
    b += text(x + 130, 190, "same voltage V across R₁ and R₂", "middle", GREY, 13)
    return wrap(svg(680, 205, b), "Series elements share one current path end to end; parallel elements share both end nodes, so they share the same voltage.")


def d_node():
    b = ""
    gy, ty, ax, bx = 170, 60, 170, 350
    b += line(50, gy, bx, gy, INK, 3)
    b += isrc(70, gy, 70, ty, "6 A", "left")
    b += line(70, ty, ax, ty)
    b += res(ax, ty, bx, ty, "R₂ = 4 Ω")
    b += res(ax, ty, ax, gy, "R₁ = 4 Ω", "right") + res(bx, ty, bx, gy, "R₃ = 4 Ω", "right")
    b += dot(ax, ty, 5) + dot(bx, ty, 5)
    b += text(ax - 8, ty - 10, "A", "end", BLUE, 15, "bold") + text(bx + 10, ty - 10, "B", "start", BLUE, 15, "bold")
    b += text(200, gy + 26, "reference node (0 V)", "middle", GREY, 13)
    return wrap(svg(460, 205, b), "Two unknown nodes A and B. The 6 A source injects current into A; the bottom rail is the 0 V reference.")


def d_mesh():
    b = ""
    L, M, R, T, B = 110, 290, 500, 45, 195
    b += line(L, B, R, B)
    b += vsrc(L, B, L, T, "V₁ = 16 V", "left", plus="end")
    b += res(L, T, M, T, "R₁ = 4 Ω") + res(M, T, R, T, "R₂ = 6 Ω")
    b += res(M, T, M, B, "Rs = 2 Ω", "right")
    b += vsrc(R, T, R, B, "V₂ = 2 V", "right", plus="end")
    b += dot(M, T, 4) + dot(M, B, 4)
    b += arc_arrow(200, 120, 30, -60, 235, PURP, 2.5) + text(200, 126, "I₁", "middle", PURP, 15, "bold")
    b += arc_arrow(408, 120, 30, -60, 235, PURP, 2.5) + text(408, 126, "I₂", "middle", PURP, 15, "bold")
    return wrap(svg(610, 225, b), "Two-mesh circuit. Mesh 1 (left) holds V₁, R₁ and the shared branch Rs; mesh 2 (right) holds V₂, R₂ and the same Rs. Both mesh currents are drawn clockwise, and both sources push current clockwise.")


def d_source_transform():
    T, B = 70, 165
    b = text(150, 18, "Voltage-source form", "middle", INK, 14, "bold")
    b += line(85, B, 250, B) + vsrc(85, B, 85, T, "12 V", "left")
    b += res(85, T, 220, T, "4 Ω") + line(220, T, 250, T)
    b += dot(250, T, 5, RED) + dot(250, B, 5, RED) + text(262, T + 4, "a", "start", RED, 14, "bold") + text(262, B + 4, "b", "start", RED, 14, "bold")
    b += text(340, 120, "⇌", "middle", INK, 30)
    x = 400
    b += text(x + 150, 18, "Current-source form", "middle", INK, 14, "bold")
    b += line(x + 85, T, x + 250, T) + line(x + 85, B, x + 250, B)
    b += isrc(x + 85, B, x + 85, T, "3 A", "left")
    b += res(x + 185, T, x + 185, B, "4 Ω", "right")
    b += dot(x + 250, T, 5, RED) + dot(x + 250, B, 5, RED) + text(x + 262, T + 4, "a", "start", RED, 14, "bold") + text(x + 262, B + 4, "b", "start", RED, 14, "bold")
    return wrap(svg(700, 205, b), "12 V in series with 4 Ω looks, from terminals a–b, exactly like a 3 A source (12/4) in parallel with the same 4 Ω.")


def _thev_orig(x0):
    b = line(x0 + 50, 150, x0 + 200, 150)
    b += vsrc(x0 + 50, 150, x0 + 50, 45, "24 V", "left") + res(x0 + 50, 45, x0 + 180, 45, "6 Ω")
    b += line(x0 + 180, 45, x0 + 200, 45) + res(x0 + 180, 45, x0 + 180, 150, "12 Ω", "right")
    b += line(x0 + 180, 150, x0 + 220, 150) + line(x0 + 180, 45, x0 + 220, 45)
    return b


def d_thevenin():
    T, B = 75, 175
    b = text(170, 18, "Original network", "middle", INK, 14, "bold")
    b += line(90, B, 280, B) + vsrc(90, B, 90, T, "24 V", "left")
    b += res(90, T, 220, T, "6 Ω") + line(220, T, 280, T) + res(220, T, 220, B, "12 Ω", "right")
    b += dot(280, T, 5, RED) + dot(280, B, 5, RED) + text(292, T + 4, "a", "start", RED, 14, "bold") + text(292, B + 4, "b", "start", RED, 14, "bold")
    b += text(390, 128, "≡", "middle", INK, 34)
    b += text(590, 18, "Thevenin equivalent", "middle", INK, 14, "bold")
    b += line(500, B, 700, B) + vsrc(500, B, 500, T, "V_th = 16 V", "left")
    b += res(500, T, 660, T, "R_th = 4 Ω") + line(660, T, 700, T)
    b += dot(700, T, 5, RED) + dot(700, B, 5, RED) + text(712, T + 4, "a", "start", RED, 14, "bold") + text(712, B + 4, "b", "start", RED, 14, "bold")
    return wrap(svg(750, 210, b), "The 24 V / 6 Ω / 12 Ω network (load removed) collapses, as seen from a–b, to a 16 V source in series with 4 Ω.")


def d_maxpower():
    x0, y0, W, H = 60, 200, 380, 160
    b = line(x0, y0, x0 + W + 10, y0) + line(x0, y0, x0, y0 - H - 15)
    pts = []
    for i in range(0, 201):
        rl = 20 * i / 200
        p = 256 * rl / (4 + rl) ** 2
        pts.append((x0 + rl / 20 * W, y0 - p / 16 * H))
    b += poly(pts, PURP, 2.8)
    for rl in (0, 4, 8, 12, 16, 20):
        x = x0 + rl / 20 * W
        b += line(x, y0, x, y0 + 5) + text(x, y0 + 20, str(rl), "middle", GREY, 12)
    for p in (0, 4, 8, 12, 16):
        y = y0 - p / 16 * H
        b += line(x0 - 5, y, x0, y) + text(x0 - 9, y + 4, str(p), "end", GREY, 12)
    px = x0 + 4 / 20 * W
    b += line(px, y0, px, y0 - H, RED, 1.5, "4,3") + line(x0, y0 - H, px, y0 - H, RED, 1.5, "4,3") + dot(px, y0 - H, 5, RED)
    b += text(px + 12, y0 - H - 8, "P_max = 16 W at R_L = R_th = 4 Ω", "start", RED, 13, "bold")
    b += text(x0 + W / 2, y0 + 42, "load resistance R_L (Ω)", "middle", INK, 13)
    b += text(18, y0 - H / 2, "power P (W)", "middle", INK, 13).replace('<text ', '<text transform="rotate(-90 18 %.1f)" ' % (y0 - H / 2))
    return wrap(svg(520, 262, b), "Power delivered to R_L (V_th = 16 V, R_th = 4 Ω): it rises, peaks exactly at R_L = R_th, then falls — the calculus in the box above proves the peak sits there.")


def d_superposition():
    T, B = 80, 180
    b = text(170, 18, "V₁ alone (current source opened)", "middle", INK, 13, "bold")
    b += line(95, B, 250, B) + vsrc(95, B, 95, T, "24 V", "left")
    b += res(95, T, 250, T, "6 Ω") + res(250, T, 250, B, "12 Ω", "right")
    b += dot(250, T, 5, BLUE) + text(262, T - 8, "A", "start", BLUE, 14, "bold")
    b += text(170, 218, "V_A1 = 16 V", "middle", GREEN, 14, "bold")
    b += text(370, 130, "+", "middle", INK, 30)
    x = 420
    b += text(x + 170, 18, "2 A source alone (V₁ shorted)", "middle", INK, 13, "bold")
    b += line(x + 60, T, x + 250, T) + line(x + 60, B, x + 250, B)
    b += isrc(x + 60, B, x + 60, T, "2 A", "left")
    b += res(x + 150, T, x + 150, B, "6 Ω", "right") + res(x + 250, T, x + 250, B, "12 Ω", "right")
    b += dot(x + 150, T, 5, BLUE) + text(x + 140, T - 10, "A", "end", BLUE, 14, "bold")
    b += text(x + 170, 218, "V_A2 = 8 V", "middle", GREEN, 14, "bold")
    return wrap(svg(760, 235, b), "The network with a 2 A source added at node A. Left: only the 24 V source acts. Right: the 24 V source is replaced by a short, so 6 Ω and 12 Ω sit in parallel. Add the node voltages: 16 + 8 = 24 V.")


def d_sine():
    x0, ym, W, A = 60, 100, 360, 62
    b = line(x0, ym, x0 + W + 15, ym) + line(x0, ym - A - 20, x0, ym + A + 20)
    for a in (90, 180, 270, 360):
        x = x0 + a / 360 * W
        b += line(x, ym - A - 12, x, ym + A + 12, "#d5d9e0", 1, "3,3") + text(x, ym + A + 34, f"{a}°", "middle", GREY, 12)
    b += text(x0, ym + A + 34, "0°", "middle", GREY, 12)
    b += poly(sine_pts(x0, ym, W, A), PURP, 2.8)
    px = x0 + 90 / 360 * W
    b += dot(px, ym - A, 4.5, RED) + text(px + 8, ym - A - 6, "+V_m", "start", RED, 13, "bold")
    tx = x0 + 270 / 360 * W
    b += dot(tx, ym + A, 4.5, RED) + text(tx + 8, ym + A + 16, "−V_m", "start", RED, 13, "bold")
    b += text(x0 + W + 15, ym - 8, "ωt", "end", INK, 13, None, True) + text(x0 - 8, ym - A - 8, "v", "end", INK, 13, None, True)
    return wrap(svg(500, 230, b), "One full rotation of the coil (360°) traces one full sine cycle: positive peak at 90°, zero at 180°, negative peak at 270°.")


def d_rms():
    x0, ym, W, A = 50, 170, 250, 130
    b = line(x0, ym, x0 + W + 20, ym) + line(x0, ym, x0, ym - A - 20)
    b += poly(sine_pts(x0, ym, W, A, 0, 180), PURP, 2.8)
    lv = {"Vm": (100, RED), "rms": (70.7, BLUE), "avg": (63.7, GREEN)}
    for k, (v, c) in lv.items():
        y = ym - A * v / 100
        b += line(x0, y, x0 + W + 12, y, c, 1.6, "5,3")
    b += text(x0 + W + 18, ym - A + 4, "V_m = 100 V (peak)", "start", RED, 13, "bold")
    b += text(x0 + W + 18, ym - A * .707 - 5, "V_rms = 70.7 V", "start", BLUE, 13, "bold")
    b += text(x0 + W + 18, ym - A * .637 + 16, "V_avg = 63.7 V", "start", GREEN, 13, "bold")
    b += text(x0, ym + 18, "0°", "middle", GREY, 12) + text(x0 + W, ym + 18, "180°", "middle", GREY, 12)
    b += text(x0 + W / 2, ym + 38, "one half-cycle", "middle", GREY, 12)
    return wrap(svg(510, 235, b), "Three 'heights' of the same 100 V-peak sine wave (one half-cycle shown). RMS sits above the average because squaring weights the larger values more.")


def d_phasor():
    ox, oy = 60, 200
    b = line(ox, oy, 420, oy, INK, 1.5) + line(ox, oy, ox, 30, INK, 1.5)
    b += text(426, oy + 5, "Re", "start", GREY, 13) + text(ox - 6, 26, "Im", "end", GREY, 13)
    b += arrow(ox, oy, ox + 280, oy, RED, 3, 12)
    b += text(ox + 285, oy + 22, "I (reference, 0°)", "end", RED, 13, "bold")
    ang = math.radians(40)
    vx, vy = ox + 300 * math.cos(ang), oy - 300 * math.sin(ang)
    b += arrow(ox, oy, vx, vy, BLUE, 3, 12)
    b += text(vx + 8, vy + 4, "V (leads I by φ)", "start", BLUE, 13, "bold")
    r = 70
    b += f'<path d="M{ox + r},{oy} A{r},{r} 0 0 0 {ox + r * math.cos(ang):.1f},{oy - r * math.sin(ang):.1f}" fill="none" stroke="{PURP}" stroke-width="2"/>'
    b += text(ox + 92, oy - 22, "φ", "middle", PURP, 16, "bold")
    return wrap(svg(560, 240, b), "Phasor diagram of an inductive (RL) circuit: current is the reference; the voltage phasor sits ahead of it by the impedance angle φ.")


def d_rl():
    b = ""
    b += line(60, 160, 340, 160) + acsrc(60, 160, 60, 45, "V = 50 V", "left")
    b += res(60, 45, 200, 45, "R = 3 Ω") + ind(200, 45, 340, 45, "X_L = 4 Ω") + line(340, 45, 340, 160)
    b += arc_arrow(200, 105, 24, -60, 235, RED, 2) + text(200, 111, "I", "middle", RED, 14, "bold")
    b += text(200, 200, "Z = 3 + j4 Ω  →  |Z| = 5 Ω,  φ = 53.1°", "middle", INK, 13, "bold")
    # impedance triangle
    ox, oy, sx = 470, 170, 36
    P = (ox + 3 * sx, oy)
    Q = (ox + 3 * sx, oy - 4 * sx)
    b += text(ox + 90, 20, "Impedance triangle", "middle", INK, 14, "bold")
    b += line(ox, oy, P[0], P[1], INK, 2.5) + line(P[0], P[1], Q[0], Q[1], INK, 2.5) + line(ox, oy, Q[0], Q[1], PURP, 2.8)
    b += f'<rect x="{P[0]-10}" y="{P[1]-10}" width="10" height="10" fill="none" stroke="{INK}" stroke-width="1.4"/>'
    b += text((ox + P[0]) / 2, oy + 20, "R = 3 Ω", "middle", INK, 13, "bold")
    b += text(P[0] + 10, (oy + Q[1]) / 2 + 4, "X_L = 4 Ω", "start", INK, 13, "bold")
    b += text((ox + Q[0]) / 2 - 8, (oy + Q[1]) / 2 - 6, "Z = 5 Ω", "end", PURP, 13, "bold")
    b += f'<path d="M{ox+32},{oy} A32,32 0 0 0 {ox+32*math.cos(math.atan2(4,3)):.1f},{oy-32*math.sin(math.atan2(4,3)):.1f}" fill="none" stroke="{RED}" stroke-width="2"/>'
    b += text(ox + 47, oy - 10, "φ", "middle", RED, 14, "bold")
    return wrap(svg(720, 215, b), "Series RL circuit and its impedance triangle — a 3-4-5 right triangle: resistance and reactance are the legs, impedance the hypotenuse.")


def d_resonance():
    Q = 4.0
    pts = []
    for i in range(0, 121):
        x = 0.4 + i * 0.01
        val = 1 / math.sqrt(1 + Q * Q * (x - 1 / x) ** 2)
        pts.append((50 + (x - 0.4) / 1.2 * 340, 170 - val * 130))
    f0x = 50 + 0.6 / 1.2 * 340
    b = line(50, 170, 400, 170) + line(50, 170, 50, 20)
    b += poly(pts, PURP, 2.8)
    b += line(f0x, 170, f0x, 40, RED, 1.5, "4,3")
    b += text(f0x, 188, "f₀ = 1/(2π√LC)", "middle", RED, 13, "bold")
    b += text(f0x + 12, 28, "I_max = V/R  (Z = R)", "start", RED, 13, "bold")
    b += text(60, 80, "capacitive", "start", BLUE, 13, "bold") + text(60, 96, "(I leads V)", "start", BLUE, 12)
    b += text(392, 80, "inductive", "end", GREEN, 13, "bold") + text(392, 96, "(I lags V)", "end", GREEN, 12)
    b += text(225, 208, "frequency f →", "middle", INK, 13) + text(16, 100, "current I", "middle", INK, 13).replace('<text ', '<text transform="rotate(-90 16 100)" ')
    return wrap(svg(430, 215, b), "Current in a series RLC circuit versus frequency: a sharp peak at resonance, where X_L = X_C. The higher the Q, the narrower the peak.")


def d_power_triangle():
    ox, oy, sc = 60, 210, .46
    P = (ox + 300 * sc, oy)
    Q = (P[0], oy - 400 * sc)
    b = line(ox, oy, P[0], P[1], GREEN, 3) + line(P[0], P[1], Q[0], Q[1], BLUE, 3) + line(ox, oy, Q[0], Q[1], PURP, 3)
    b += f'<rect x="{P[0]-11}" y="{P[1]-11}" width="11" height="11" fill="none" stroke="{INK}" stroke-width="1.4"/>'
    b += text((ox + P[0]) / 2, oy + 22, "P = 300 W (real)", "middle", GREEN, 13, "bold")
    b += text(P[0] + 10, (oy + Q[1]) / 2 + 4, "Q = 400 VAR (reactive)", "start", BLUE, 13, "bold")
    b += text((ox + Q[0]) / 2 - 10, (oy + Q[1]) / 2 - 4, "S = 500 VA", "end", PURP, 13, "bold")
    a = math.atan2(400, 300)
    b += f'<path d="M{ox+38},{oy} A38,38 0 0 0 {ox+38*math.cos(a):.1f},{oy-38*math.sin(a):.1f}" fill="none" stroke="{RED}" stroke-width="2"/>'
    b += text(ox + 56, oy - 12, "φ", "middle", RED, 14, "bold") + text((ox + P[0]) / 2, oy + 40, "power factor cos φ = P/S = 0.6", "middle", RED, 12)
    return wrap(svg(430, 260, b), "The power triangle for the B4 circuit — the same 3-4-5 shape as the impedance triangle, because P, Q and S are I² times R, X and Z.")


# ------------------------------------------------------------------ Topic 2
def _polar(cx, cy, r, deg):
    return cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg))


def d_dc_machine():
    cx, cy = 300, 190
    b = ""
    # yoke
    b += f'<circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="#9aa3b2" stroke-width="16"/>'
    # poles + shoes + coils
    for sign, name, col in ((-1, "N", RED), (1, "S", BLUE)):
        ang = -90 if sign < 0 else 90
        # pole core
        x1 = cx - 24
        yA, yB = (cy - 142, cy - 86) if sign < 0 else (cy + 86, cy + 142)
        b += f'<rect x="{x1}" y="{yA}" width="48" height="{yB-yA}" fill="#d7dce5" stroke="{INK}" stroke-width="1.6"/>'
        # field coils
        for dx in (-38, 24):
            b += f'<rect x="{cx+dx}" y="{yA+8}" width="14" height="{yB-yA-14}" fill="#f1c9a5" stroke="#b46b2d" stroke-width="1.4"/>'
        # pole shoe (arc band)
        a1, a2 = ang - 38, ang + 38
        outer = [_polar(cx, cy, 88, a1 + (a2 - a1) * i / 20) for i in range(21)]
        inner = [_polar(cx, cy, 72, a2 - (a2 - a1) * i / 20) for i in range(21)]
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in outer + inner)
        b += f'<polygon points="{pts}" fill="#c3cad6" stroke="{INK}" stroke-width="1.6"/>'
        b += text(cx, (cy - 106 if sign < 0 else cy + 112), name, "middle", col, 22, "bold")
    # armature
    b += f'<circle cx="{cx}" cy="{cy}" r="64" fill="#eef0f4" stroke="{INK}" stroke-width="2"/>'
    for k in range(12):
        a = 15 + 30 * k
        x, y = _polar(cx, cy, 52, a)
        top = math.sin(math.radians(a)) < 0
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
        if top:
            b += line(x - 3.5, y - 3.5, x + 3.5, y + 3.5, INK, 1.5) + line(x - 3.5, y + 3.5, x + 3.5, y - 3.5, INK, 1.5)
        else:
            b += dot(x, y, 2)
    b += f'<circle cx="{cx}" cy="{cy}" r="12" fill="#fff" stroke="{PURP}" stroke-width="2.4"/>'
    # labels (left / right columns with leaders)
    def lab(s, tx, ty, lx, ly, anchor):
        return line(lx, ly, tx, ty, GREY, 1.2) + dot(tx, ty, 2.5, GREY) + text(lx + (-6 if anchor == "end" else 6), ly + 4, s, anchor, INK, 13, "bold")
    b += lab("Yoke", *_polar(cx, cy, 150, 200), 120, 80, "end")
    b += lab("Pole core", cx - 24, cy - 116, 120, 130, "end")
    b += lab("Pole shoe", *_polar(cx, cy, 80, 225), 120, 180, "end")
    b += lab("Field winding", cx + 31, cy + 112, 480, 330, "start")
    b += lab("Air gap", *_polar(cx, cy, 68, -60), 480, 90, "start")
    b += lab("Armature core", *_polar(cx, cy, 60, 20), 480, 150, "start")
    b += lab("Armature conductors", *_polar(cx, cy, 52, 75), 480, 210, "start")
    b += lab("Shaft", cx + 8, cy + 8, 480, 270, "start")
    b += text(300, 372, "× current into page (under N)     • current out of page (under S)", "middle", GREY, 12)
    return wrap(svg(640, 385, b), "Cross-section of a two-pole DC machine: the yoke carries flux between the N and S poles; conductors in the armature slots carry current straight along the shaft, in opposite directions under the two poles.")


def d_fleming():
    ox, oy = 300, 150
    b = arrow(ox, oy, ox, 50, GREEN, 3.5, 13) + text(ox, 34, "Force / Motion (thuMb)", "middle", GREEN, 14, "bold")
    b += arrow(ox, oy, 470, oy, BLUE, 3.5, 13) + text(476, oy + 5, "Field, N → S", "start", BLUE, 14, "bold") + text(476, oy + 22, "(First finger)", "start", BLUE, 12)
    dx, dy = -math.cos(math.radians(35)), math.sin(math.radians(35))
    ex, ey = ox + dx * 120, oy + dy * 120
    b += arrow(ox, oy, ex, ey, RED, 3.5, 13) + text(ex - 6, ey + 18, "Current (seCond finger)", "end", RED, 14, "bold")
    b += dot(ox, oy, 4)
    b += f'<rect x="{ox}" y="{oy-14}" width="14" height="14" fill="none" stroke="{GREY}" stroke-width="1.3"/>'
    b += text(ox + 40, 262, "three mutually perpendicular directions (current drawn coming toward you)", "middle", GREY, 12, None, True)
    return wrap(svg(640, 275, b), "Fleming's Left-Hand Rule (motors): thu<b>M</b>b = <b>M</b>otion/force, <b>F</b>irst finger = <b>F</b>ield, se<b>C</b>ond finger = <b>C</b>urrent.")


def _supply(x, ytop, ybot):
    return dot(x, ytop, 4) + dot(x, ybot, 4) + text(x - 8, ytop + 4, "+", "end", INK, 15, "bold") + text(x - 8, ybot + 4, "−", "end", INK, 15, "bold")


def d_motor_types():
    b = ""
    T, B = 60, 170
    # Shunt
    x = 0
    b += text(x + 115, 24, "Shunt", "middle", INK, 15, "bold") + _supply(x + 30, T, B)
    b += line(x + 30, T, x + 170, T) + line(x + 30, B, x + 170, B)
    b += ind(x + 85, T, x + 85, B, "field", "left") + dot(x + 85, T) + dot(x + 85, B)
    b += line(x + 170, T, x + 170, 88) + line(x + 170, 132, x + 170, B) + motor(x + 170, 110)
    b += text(x + 115, 208, "field ∥ armature", "middle", GREY, 12)
    # Series
    x = 240
    b += text(x + 115, 24, "Series", "middle", INK, 15, "bold") + _supply(x + 30, T, B)
    b += ind(x + 30, T, x + 140, T, "series field") + line(x + 140, T, x + 170, T)
    b += line(x + 30, B, x + 170, B) + line(x + 170, T, x + 170, 88) + line(x + 170, 132, x + 170, B) + motor(x + 170, 110)
    b += text(x + 115, 208, "field in series with armature", "middle", GREY, 12)
    # Compound (short shunt)
    x = 480
    b += text(x + 130, 24, "Compound (short shunt)", "middle", INK, 15, "bold") + _supply(x + 30, T, B)
    b += ind(x + 30, T, x + 110, T, "series", "top") + line(x + 110, T, x + 200, T)
    b += line(x + 30, B, x + 200, B)
    b += ind(x + 110, T, x + 110, B, "shunt", "left") + dot(x + 110, T) + dot(x + 110, B)
    b += line(x + 200, T, x + 200, 88) + line(x + 200, 132, x + 200, B) + motor(x + 200, 110)
    b += text(x + 130, 208, "series field in the supply line", "middle", GREY, 12)
    return wrap(svg(740, 228, b), "Three ways to connect the field winding: the coil symbol is the field, the circle marked M is the armature. Each connection gives a different speed/torque personality.")


def d_transformer():
    ox = 150
    b = ""
    # core
    b += f'<rect x="{ox}" y="20" width="260" height="180" fill="#cfd5df" stroke="{INK}" stroke-width="2"/>'
    b += f'<rect x="{ox+60}" y="80" width="140" height="60" fill="#fbfbfa" stroke="{INK}" stroke-width="2"/>'
    # windings
    def coil(cx, col):
        s = ""
        for k in range(7):
            y = 92 + k * 6
            s += f'<rect x="{cx-40}" y="{y}" width="80" height="4" rx="2" fill="{col}" stroke="none"/>'
        return s
    b += coil(ox + 30, "#c0392b") + coil(ox + 230, "#1e468c")
    # flux loop
    b += f'<rect x="{ox+30}" y="50" width="200" height="120" fill="none" stroke="{PURP}" stroke-width="2.4" stroke-dasharray="7,4"/>'
    b += head(ox + 140, 50, 1, 0, PURP, 11)
    b += text(ox + 130, 114, "Φ", "middle", PURP, 20, "bold")
    # labels
    b += text(ox - 20, 100, "Primary", "end", RED, 14, "bold") + text(ox - 20, 118, "N₁ turns", "end", RED, 13)
    b += text(ox + 292, 100, "Secondary", "start", BLUE, 14, "bold") + text(ox + 292, 118, "N₂ turns", "start", BLUE, 13)
    b += arrow(ox - 100, 40, ox - 30, 40, INK, 2) + text(ox - 105, 44, "V₁ in", "end", INK, 13)
    b += arrow(ox + 300, 160, ox + 360, 160, INK, 2) + text(ox + 366, 164, "V₂ out", "start", INK, 13)
    b += text(ox + 130, 216, "laminated silicon-steel core", "middle", GREY, 12)
    return wrap(svg(720, 235, b), "Core-type construction: the alternating flux Φ set up by the primary circulates round the core and links the secondary winding on the opposite limb.")


def d_generator():
    x0, ym, W, A = 50, 110, 390, 62
    b = line(x0, ym, x0 + W + 12, ym) + line(x0, ym - A - 20, x0, ym + A + 20)
    b += poly(sine_pts(x0, ym, W, A, 0, 720), GREY, 2, "6,4")
    b += poly([(p[0], ym - abs(ym - p[1])) for p in sine_pts(x0, ym, W, A, 0, 720)], PURP, 2.8)
    for k in range(5):
        x = x0 + k * W / 4
        b += text(x, ym + A + 40, f"{k*180}°", "middle", GREY, 12)
    b += line(x0 + 10, 16, x0 + 40, 16, GREY, 2, "6,4") + text(x0 + 46, 20, "EMF induced in the loop (alternating)", "start", GREY, 12)
    b += line(x0 + 10, 34, x0 + 40, 34, PURP, 2.8) + text(x0 + 46, 38, "voltage at the brushes after the commutator (one direction)", "start", PURP, 12)
    b += text(x0 + W / 2, ym + A + 62, "loop rotation (two revolutions)", "middle", INK, 12)
    return wrap(svg(470, 260, b), "A single-loop generator: the loop's EMF alternates every half-turn; the commutator swaps the brush connections at each zero crossing so the load sees a one-directional, pulsating output.")


def d_rotating():
    b = ""
    names = [("A", -90, "ωt = 90°", "A carries its maximum current"), ("B", 30, "ωt = 210°", "B carries its maximum current"), ("C", 150, "ωt = 330°", "C carries its maximum current")]
    for i, (n, ang, t, note) in enumerate(names):
        cx, cy, r = 110 + i * 230, 105, 62
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f7f8fb" stroke="{INK}" stroke-width="2.2"/>'
        for m, a2, _, _ in names:
            x, y = _polar(cx, cy, r, a2)
            xl, yl = _polar(cx, cy, r + 15, a2)
            act = (m == n)
            b += line(cx, cy, x, y, "#c8cdd8", 1.2, "3,3") + text(xl, yl + 5, m, "middle", PURP if act else GREY, 15 if act else 13, "bold")
        x, y = _polar(cx, cy, r - 6, ang)
        b += arrow(cx, cy, x, y, PURP, 3.5, 12)
        b += text(cx, 200, t, "middle", INK, 13, "bold") + text(cx, 218, "resultant field points along " + n, "middle", GREY, 12)
    return wrap(svg(690, 232, b), "Stator cross-section at three instants. Each winding's axis is drawn dashed (A, B, C, 120° apart). As each phase current peaks in turn, the resultant field (arrow) jumps from A to B to C — a rotation.")


def d_threephase():
    x0, ym, W, A = 50, 105, 360, 62
    b = line(x0, ym, x0 + W + 12, ym) + line(x0, ym - A - 22, x0, ym + A + 22)
    for lag, col in ((0, RED), (120, AMBER), (240, BLUE)):
        b += poly(sine_pts(x0, ym, W, A, 0, 360, lag), col, 2.6)
    for a in (0, 90, 180, 270, 360):
        x = x0 + a / 360 * W
        b += text(x, ym + A + 40, f"{a}°", "middle", GREY, 12)
    for a, lab, col in ((90, "A max", RED), (210, "B max", AMBER), (330, "C max", BLUE)):
        x = x0 + a / 360 * W
        b += line(x, ym - A - 14, x, ym + A + 14, col, 1.2, "3,3") + text(x, ym - A - 20, lab, "middle", col, 12, "bold")
    lx = x0 + W + 40
    for i, (t, col) in enumerate((("Phase A", RED), ("Phase B (lags 120°)", AMBER), ("Phase C (lags 240°)", BLUE))):
        b += line(lx, 60 + i * 22, lx + 22, 60 + i * 22, col, 3) + text(lx + 30, 64 + i * 22, t, "start", INK, 13)
    b += text(x0 + W / 2, ym + A + 64, "ωt →", "middle", INK, 13)
    return wrap(svg(620, 230, b), "Three balanced currents 120° apart. Each phase peaks in turn (A, then B, then C), and at any instant the three sum to zero.")


TOPIC1 = [d_ohm, d_kcl_kvl, d_series_parallel, d_node, d_mesh, d_source_transform, d_thevenin,
          d_maxpower, d_superposition, d_sine, d_rms, d_phasor, d_rl, d_power_triangle]
TOPIC2 = [d_dc_machine, d_fleming, d_motor_types, d_transformer, d_rotating]
NAMED = {"resonance": d_resonance, "generator": d_generator, "threephase": d_threephase}


def all_diagrams():
    out = [(f"t1_{i+1:02d}", f()) for i, f in enumerate(TOPIC1)]
    out += [(f"t2_{i+1:02d}", f()) for i, f in enumerate(TOPIC2)]
    out += [(f"x_{k}", f()) for k, f in NAMED.items()]
    return out


if __name__ == "__main__":
    import os
    from playwright.sync_api import sync_playwright
    os.makedirs("_diag2", exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 900, "height": 400})
        for name, html in all_diagrams():
            pg.set_content(f'<body style="margin:0;background:#fff"><div style="width:880px;padding:8px;text-align:center">{html}</div></body>')
            pg.screenshot(path=f"_diag2/{name}.png", full_page=True)
        br.close()
    print("rendered", len(all_diagrams()))
