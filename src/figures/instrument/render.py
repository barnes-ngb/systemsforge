"""Render figure.svg (the instrument readout) from graph.json."""
import json
from pathlib import Path

g = json.loads(Path(__file__).with_name("graph.json").read_text(encoding="utf-8"))
ins = g["instrument"]

W, H = 940, 332
A = "currentColor"
P = []


def rect(x, y, w, h, stroke=A, fill="none", sw=1, r=3):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def text(x, y, s, size=13, anchor="start", fill=A, weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{fill}" font-weight="{weight}">{s}</text>'


def line(x1, y1, x2, y2, sw=1, dash=False, arrow=True, stroke=A):
    d = ' stroke-dasharray="4 4"' if dash else ""
    m = ' marker-end="url(#a)"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>'


def node(x, y, label):  # 120x40 box centered at x,y
    return rect(x - 60, y - 20, 120, 40) + text(x, y + 4, label, 13, anchor="middle")


P.append(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{g["claim"]}" '
         'xmlns="http://www.w3.org/2000/svg" font-family="var(--font-mono)">')
P.append('<defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto">'
         '<path d="M0,0 L8,4 L0,8 z" fill="currentColor"/></marker></defs>')

# layout constants
nx = 108                       # left column center
y_cand, y_ref, y_know = 88, 160, 248
fx, fy, fw, fh = 232, 48, 408, 172   # instrument frame
cx, cy, cw, ch = 272, 104, 120, 40   # comparator
sx0, sx1, sy = 428, 628, 132         # residual scale
vx0, vy = 672, 120                   # verdict chips

# instrument frame
P.append(rect(fx, fy, fw, fh, stroke="var(--accent)", sw=1.5, r=6))
P.append(text(fx + 16, fy + 20, "instrument", 11, fill="var(--accent)", weight=500))

# left column
P.append(node(nx, y_cand, ins["inputs"][0]["label"]))
P.append(node(nx, y_ref, ins["inputs"][1]["label"]))
P.append(node(nx, y_know, g["knowledge"]["label"]))
P.append(line(nx, y_know - 22, nx, y_ref + 22))          # knowledge -> reference
P.append(text(nx + 8, y_ref + 40, "supplies", 10, fill="var(--ink-tertiary)"))

# inputs into the comparator
P.append(rect(cx, cy, cw, ch))
P.append(text(cx + cw / 2, cy + 24, ins["comparator"]["label"], 13, anchor="middle"))
P.append(line(nx + 62, y_cand, cx - 2, cy + 12))
P.append(line(nx + 62, y_ref, cx - 2, cy + ch - 12))

# residual scale
P.append(text(sx0, sy - 40, "residual", 11, fill="var(--ink-tertiary)"))
P.append(line(cx + cw + 2, cy + ch / 2, sx0 - 10, sy))
P.append(line(sx0, sy, sx1, sy, arrow=False))
for i in range(11):
    x = sx0 + i * 20
    P.append(line(x, sy, x, sy - (8 if i % 5 == 0 else 4), arrow=False))
P.append(text(sx0, sy + 16, "0", 10, anchor="middle"))
P.append(text(sx1, sy + 16, "1.0", 10, anchor="middle"))

tx = sx0 + float(ins["threshold"]["example_value"]) * 200
P.append(line(tx, sy - 6, tx, sy + 40, arrow=False, dash=True))
P.append(text(tx, sy + 54, f'threshold {ins["threshold"]["example_value"]} {ins["threshold"]["unit"]}', 10, anchor="middle", fill="var(--ink-tertiary)"))

vx = sx0 + float(ins["residual"]["example_value"]) * 200
P.append(f'<circle cx="{vx}" cy="{sy}" r="4" fill="var(--accent)"/>')
P.append(text(vx, sy - 14, f'{ins["residual"]["example_value"]} {ins["residual"]["unit"]}', 11, anchor="middle", weight=500))

# verdict chips, outside the frame: the output port
P.append(text(vx0, vy - 12, "verdict", 11, fill="var(--ink-tertiary)"))
x = vx0
for s in ins["verdict"]["states"]:
    w = len(s) * 7 + 16
    on = s == ins["verdict"]["example"]
    P.append(rect(x, vy, w, 24, stroke="var(--accent)" if on else "var(--ink-tertiary)", sw=1.5 if on else 1))
    P.append(text(x + w / 2, vy + 16, s, 11, anchor="middle", fill=A if on else "var(--ink-tertiary)", weight=500 if on else 400))
    x += w + 8
P.append(line(sx1 + 4, sy, vx0 - 4, sy))               # residual -> verdict (crosses frame edge: that is the port)

# the skip: candidate straight to verdict, over the top of the frame, no reference
skip = g["outside"]["skip"]
P.append(f'<path d="M{nx},{y_cand-22} C{nx},6 {vx0+30},6 {vx0+30},{vy-26}" fill="none" '
         'stroke="currentColor" stroke-width="1" stroke-dasharray="4 4" marker-end="url(#a)"/>')
P.append(text(fx + fw / 2, 18, f'the skip: "{skip["label"]}", no reference, no residual', 10, anchor="middle", fill="var(--ink-tertiary)"))

# return edge: instrument -> knowledge, under the frame
ret = g["outside"]["return"]
rx, ry, rb = fx + fw - 48, fy + fh, 300
P.append(line(rx, ry, rx, rb, arrow=False))
P.append(line(rx, rb, nx, rb, arrow=False))
P.append(line(nx, rb, nx, y_know + 22, arrow=True))
P.append(text((rx + nx) / 2, rb + 16, ret["label"], 10, anchor="middle", fill="var(--ink-tertiary)"))

P.append("</svg>")
out = Path(__file__).with_name("figure.svg")
out.write_text("\n".join(P), encoding="utf-8")
print(out, out.stat().st_size, "bytes")
