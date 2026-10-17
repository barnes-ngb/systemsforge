"""Legibility and token check for a systemsforge figure SVG.

Usage: python scripts/check_figure.py path/to/figure.svg [--out DIR]

Rasterizes light and dark variants, flags text/rect collisions, text/text
overlaps, literal hex colors, disallowed weights, sizes, and font families.
Exit code 1 on any violation. Requires cairosvg (pip install cairosvg).
"""
import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

LIGHT = {
    "--paper": "#FAF8F4", "--surface": "#FFFFFF", "--ink": "#1A1A1A",
    "--ink-secondary": "#555555", "--ink-tertiary": "#888888",
    "--accent": "#3D6B5C", "--accent-soft": "#E8EFEC",
    "--border": "rgba(26,26,26,0.12)", "--border-strong": "rgba(26,26,26,0.22)",
    "--status-info": "#3578B5", "--status-warning": "#A56A0E", "--status-danger": "#9E3232",
}
DARK = {
    "--paper": "#14181C", "--surface": "#1B2025", "--ink": "#ECECEC",
    "--ink-secondary": "#A6A6A6", "--ink-tertiary": "#6B6B6B",
    "--accent": "#7FAB99", "--accent-soft": "#22302C",
    "--border": "rgba(236,236,236,0.14)", "--border-strong": "rgba(236,236,236,0.25)",
    "--status-info": "#7AAFE0", "--status-warning": "#E0AC5C", "--status-danger": "#E08585",
}
MONO = "'IBM Plex Mono', 'DejaVu Sans Mono', ui-monospace, monospace"
CHAR_W = 0.62  # mono advance as a fraction of font-size
NS = "{http://www.w3.org/2000/svg}"


def substitute(svg: str, tokens: dict) -> str:
    s = svg
    for k, v in tokens.items():
        s = re.sub(r"var\(\s*%s\s*(,[^)]*)?\)" % re.escape(k), v, s)
    s = re.sub(r"var\(\s*--font-mono\s*(,[^)]*)?\)", MONO, s)
    s = s.replace("currentColor", tokens["--ink"])
    return s


def rasterize(svg_text: str, out: Path, bg: str):
    try:
        import cairosvg
    except ImportError:
        print("cairosvg not installed; skipping raster. pip install cairosvg")
        return False
    cairosvg.svg2png(bytestring=svg_text.encode(), write_to=str(out),
                     background_color=bg, output_width=1760)
    return True


def parse_geometry(root):
    rects, texts = [], []
    for el in root.iter():
        tag = el.tag.replace(NS, "")
        if tag == "rect":
            x, y = float(el.get("x", 0)), float(el.get("y", 0))
            w, h = float(el.get("width", 0)), float(el.get("height", 0))
            rects.append((x, y, x + w, y + h))
        elif tag == "text" and el.text:
            fs = float(el.get("font-size", 13))
            x, y = float(el.get("x", 0)), float(el.get("y", 0))
            w = len(el.text) * fs * CHAR_W
            anchor = el.get("text-anchor", "start")
            x0 = x - w / 2 if anchor == "middle" else x - w if anchor == "end" else x
            texts.append(((x0, y - fs * 0.8, x0 + w, y + fs * 0.25), el.text, fs))
    return rects, texts


def overlap(a, b, pad=0.0):
    return not (a[2] + pad < b[0] or b[2] + pad < a[0] or a[3] + pad < b[1] or b[3] + pad < a[1])


def inside(a, b):
    return a[0] >= b[0] and a[2] <= b[2] and a[1] >= b[1] and a[3] <= b[3]


def check(svg_path: Path, out_dir: Path) -> int:
    svg = svg_path.read_text(encoding="utf-8")
    problems = []

    for m in re.finditer(r"#[0-9a-fA-F]{3,8}\b", svg):
        if not svg[max(0, m.start() - 5):m.start()].endswith("url("):
            ctx = svg[max(0, m.start() - 20):m.end()]
            if "href" not in ctx and "marker" not in ctx and "id=" not in ctx:
                problems.append(f"literal color {m.group()} (use tokens or currentColor)")
    for m in re.finditer(r'font-weight="(\d+)"', svg):
        if int(m.group(1)) > 500:
            problems.append(f"font-weight {m.group(1)} (max 500)")
    for m in re.finditer(r'font-size="([\d.]+)"', svg):
        v = float(m.group(1))
        if v > 13 or v < 10:
            problems.append(f"font-size {v} (allowed 10 to 13)")
    for m in re.finditer(r'font-family="([^"]+)"', svg):
        if "--font-mono" not in m.group(1):
            problems.append(f'font-family "{m.group(1)}" (use var(--font-mono))')
    if 'role="img"' not in svg or "aria-label" not in svg:
        problems.append("missing role=img or aria-label (the claim sentence)")
    if "—" in svg:
        problems.append("em dash in figure text")
    if re.search(r'<svg[^>]*\s(width|height)="', svg):
        problems.append("width/height on root svg (use viewBox only)")

    root = ET.fromstring(svg)
    rects, texts = parse_geometry(root)
    for (box, label, fs) in texts:
        for r in rects:
            if overlap(box, r) and not inside(box, r):
                problems.append(f'text "{label}" collides with a rect it is not inside')
                break
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            if overlap(texts[i][0], texts[j][0]):
                problems.append(f'text "{texts[i][1]}" overlaps text "{texts[j][1]}"')

    out_dir.mkdir(parents=True, exist_ok=True)
    stem = svg_path.stem
    rasterize(substitute(svg, LIGHT), out_dir / f"{stem}-light.png", LIGHT["--surface"])
    rasterize(substitute(svg, DARK), out_dir / f"{stem}-dark.png", DARK["--surface"])

    if problems:
        print(f"{len(problems)} problem(s) in {svg_path}:")
        for p in dict.fromkeys(problems):
            print("  -", p)
        return 1
    print(f"ok: {svg_path}  (previews in {out_dir})")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("svg")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    p = Path(a.svg)
    sys.exit(check(p, Path(a.out) if a.out else p.parent / "check"))
