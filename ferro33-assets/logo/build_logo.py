"""Rebuilds the Ferro 33 hair club wordmark as clean vector SVGs.

Glyphs are monoline centerlines with round caps (matching the shop sign),
the tagline is Michroma converted to outlines, the barber profile is a
potrace trace of the pylon sign. Run: python3 build_logo.py <michroma.ttf>
"""
import math, re, sys
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = Path(__file__).parent
SW = 13            # stroke width
H = SW / 2
CAP, XH, BASE = H + 5, 46.5, 100 - H - 0   # centerline y for cap top, x-height top, baseline
BASE = 93.5
R = 15             # corner radius
GAP = 13           # space between glyph boxes
LW = 58            # lowercase glyph width (extended, like the sign)

INK, WHITE, NEON = "#0B0C0E", "#F4F5F7", "#1EB8F5"


def rounded(points, r=R):
    """Polyline through points with rounded interior corners."""
    d = [f"M{points[0][0]:.2f},{points[0][1]:.2f}"]
    for i in range(1, len(points) - 1):
        p0, p1, p2 = points[i - 1], points[i], points[i + 1]
        v1 = (p1[0] - p0[0], p1[1] - p0[1]); v2 = (p2[0] - p1[0], p2[1] - p1[1])
        l1, l2 = math.hypot(*v1), math.hypot(*v2)
        rr = min(r, l1 / 2 if i > 1 else l1, l2 / 2 if i < len(points) - 2 else l2)
        a = (p1[0] - v1[0] / l1 * rr, p1[1] - v1[1] / l1 * rr)
        b = (p1[0] + v2[0] / l2 * rr, p1[1] + v2[1] / l2 * rr)
        sweep = 1 if v1[0] * v2[1] - v1[1] * v2[0] > 0 else 0
        d.append(f"L{a[0]:.2f},{a[1]:.2f}A{rr:.2f},{rr:.2f} 0 0 {sweep} {b[0]:.2f},{b[1]:.2f}")
    d.append(f"L{points[-1][0]:.2f},{points[-1][1]:.2f}")
    return "".join(d)


def glyphs():
    L, Rx = H, LW - H                       # standard lowercase box 0..LW
    MID = (XH + BASE) / 2
    return {
        # name: (advance, [paths], [dots])
        "f": (LW, [rounded([(L, BASE), (L, CAP), (LW - H, CAP)], 18), f"M{L},{(CAP+BASE)/2+2}H{LW - 12}"], []),
        "e": (LW, [rounded([(L, MID), (Rx, MID), (Rx, XH), (L, XH), (L, BASE), (Rx - 2, BASE)])], []),
        "r": (LW - 14, [rounded([(L, BASE), (L, XH), (LW - 14 - H, XH)])], []),
        "o": (LW, [rounded([(L + R, XH), (Rx, XH), (Rx, BASE), (L, BASE), (L, XH), (L + R + 1, XH)])], []),
        "3": (LW, [rounded([(H, CAP), (Rx, CAP), (Rx, BASE), (H, BASE)], 18),
                   f"M{12},{(CAP+BASE)/2}H{Rx}"], []),
        "h": (LW, [f"M{L},{CAP}V{BASE}", rounded([(L, XH), (Rx, XH), (Rx, BASE)])], []),
        "a": (LW, [rounded([(L, XH), (Rx, XH), (Rx, BASE), (L, BASE), (L, MID), (Rx, MID)], 12)], []),
        "i": (13, [f"M{H},{XH}V{BASE}"], [(H, CAP + 8)]),
        "c": (LW - 2, [rounded([(LW - 2 - H, XH), (L, XH), (L, BASE), (LW - 2 - H, BASE)])], []),
        "l": (13, [f"M{H},{CAP}V{BASE}"], []),
        "u": (LW, [rounded([(L, XH), (L, BASE), (Rx, BASE)]), f"M{Rx},{XH}V{BASE}"], []),
        "b": (LW, [rounded([(L, CAP), (L, BASE), (Rx, BASE), (Rx, XH), (L, XH)])], []),
        " ": (22, [], []),
    }


def word(text, x0=0.0, y0=0.0, scale=1.0, gap=GAP):
    """Returns (svg group content, width) for text set in the monoline glyphs."""
    g = glyphs(); x = 0.0; out = []
    for ch in text:
        adv, paths, dots = g[ch]
        for p in paths:
            out.append(f'<path d="{p}" transform="translate({x:.2f},0)"/>')
        for (cx, cy) in dots:
            out.append(f'<circle cx="{cx + x:.2f}" cy="{cy}" r="{SW*0.62:.2f}" stroke="none" fill="currentColor"/>')
        x += adv + (gap if ch != " " else 0)
    width = x - gap
    body = "".join(out)
    return (f'<g transform="translate({x0:.2f},{y0:.2f}) scale({scale})" fill="none" stroke="currentColor" '
            f'stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round">{body}</g>', width * scale)


def registered(cx, cy, r):
    """Registered-trademark mark: ring plus Michroma R outline."""
    rp, rw = tagline(FONT, "R", 0, 0, r * 1.0)
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="currentColor" stroke-width="{r*0.16:.2f}"/>'
            f'<g transform="translate({cx - rw / 2:.2f},{cy + r * 0.5:.2f})">{rp}</g>')


def tagline(font_path, text, x0, y0, height):
    """Tagline in Michroma, converted to outlined paths. Returns (svg, width)."""
    f = TTFont(font_path); gs = f.getGlyphSet(); cmap = f.getBestCmap()
    cap = f["OS/2"].sCapHeight or f["head"].unitsPerEm * 0.7
    s = height / cap; x = 0.0; d = []
    track = 0.10 * f["head"].unitsPerEm
    for ch in text:
        gname = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[gname].draw(TransformPen(pen, (s, 0, 0, -s, x0 + x * s, y0)))
        d.append(pen.getCommands())
        x += gs[gname].width + track
    return (f'<path fill="currentColor" stroke="currentColor" stroke-width="{height * 0.05:.2f}" '
            f'stroke-linejoin="round" d="{" ".join(d)}"/>', (x - track) * s)


def head_icon(x, y, h):
    src = (HERE / "src" / "barber-profile.svg").read_text()
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', src).group(1).split()]
    d = re.search(r' d="([^"]+)"', src).group(1)
    s = h / vb[3]
    return f'<path fill="currentColor" fill-rule="evenodd" transform="translate({x},{y}) scale({s:.5f})" d="{d}"/>', vb[2] * s


def svg(w, h, body, color, bg=None):
    rect = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    body = body.replace("currentColor", color)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" '
            f'color="{color}" style="color:{color}">{rect}{body}</svg>\n')


def build(font):
    out = {}
    pad = 40
    # 1) Horizontal wordmark: "ferro 33®  hair club" (fascia lockup)
    a, wa = word("ferro 33", pad, pad)
    b, wb = word("hair club", pad + wa + 70, pad)
    reg = registered(pad + wa + 18, pad + 14, 10)
    W = pad * 2 + wa + 70 + wb
    out["ferro33-wordmark-horizontal"] = (W, 100 + pad * 2, a + reg + b)

    # 2) Primary lockup: ferro 33® / DAS BESTE VOM BESTEN / hair club (banner sign)
    a, wa = word("ferro 33", pad, pad)
    b, wb = word("hair club", pad, pad + 175)
    tg, wt = tagline(font, "DAS BESTE VOM BESTEN", pad, pad + 145, 26)
    W = pad * 2 + max(wa, wb, wt) + 30
    reg = registered(pad + wa + 18, pad + 14, 10)
    out["ferro33-logo-primary"] = (W, pad * 2 + 275, a + reg + tg + b)

    # 3) Stacked pylon lockup with barber profile
    sc = 1.5
    a1, w1 = word("ferro", 0, 0, sc)
    a2, w2 = word("33", 0, 0, sc)
    tg, wt = tagline(font, "DAS BESTE VOM BESTEN", 0, 0, 22)
    b, wb = word("hair club", 0, 0, 1.0)
    W = max(w1, wt, wb) + pad * 2
    cx = lambda w: (W - w) / 2
    y = pad
    parts = [f'<g transform="translate({cx(w1)},{y})">{a1}</g>']; y += 100 * sc + 18
    parts.append(f'<g transform="translate({cx(w2)},{y})">{a2}</g>')
    parts.append(registered(cx(w2) + w2 + 22, y + 22, 13)); y += 100 * sc + 40
    parts.append(f'<g transform="translate({cx(wt)},{y + 22})">{tg}</g>'); y += 22 + 40
    parts.append(f'<g transform="translate({cx(wb)},{y})">{b}</g>'); y += 100 + 40
    hp, hw = head_icon(0, 0, 300)
    parts.append(f'<g transform="translate({(W - hw) / 2},{y})">{hp}</g>'); y += 300 + pad
    out["ferro33-logo-stacked"] = (W, y, "".join(parts))

    # 4) Monogram "33" in a rounded square (favicon / avatar)
    m, wm = word("33", 0, 0, 1.0, gap=12)
    S = 180
    out["ferro33-monogram"] = (S, S, f'<g transform="translate({(S - wm) / 2},{(S - 100) / 2 + 3})">{m}</g>')

    # 5) Barber profile icon on its own
    hp, hw = head_icon(20, 20, 400)
    out["ferro33-icon-barber"] = (hw + 40, 440, hp)
    return out


def main():
    global FONT
    font = FONT = sys.argv[1]
    variants = {"ink": (INK, None), "white-on-black": (WHITE, INK), "transparent-white": (WHITE, None),
                "on-white": (INK, "#FFFFFF"), "neon": (NEON, INK)}
    (HERE / "svg").mkdir(exist_ok=True)
    for name, (w, h, body) in build(font).items():
        for vname, (color, bg) in variants.items():
            if name == "ferro33-monogram" and vname in ("white-on-black", "neon"):
                body2 = f'<rect width="{w}" height="{h}" rx="36" fill="{bg}"/>' + body
                (HERE / "svg" / f"{name}-{vname}.svg").write_text(svg(w, h, body2, color))
                continue
            (HERE / "svg" / f"{name}-{vname}.svg").write_text(svg(w, h, body, color, bg))


if __name__ == "__main__":
    main()
