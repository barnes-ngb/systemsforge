---
name: figure
description: Draw a diagram or figure for systemsforge.build (a post, a work page, a demo). Use whenever an SVG, diagram, schematic, readout, or figure is asked for on this site, or when prose is describing a mechanism a reader would have to assemble in their head. Covers what to draw, the house readout style, inline SVG mechanics against the site's tokens, the data-renders-figure pattern, and the legibility check that must pass before a figure ships.
---

# figure

A figure on this site is an instrument reading, not an illustration. It earns its place when a cold reader sees a mechanism they would otherwise assemble from prose: what moves, what compares against what, where the verdict comes from. If a sentence says it faster, write the sentence and draw nothing.

Read `visual-system/Visual System.md` first if it is not already in context. Figures obey it. This skill only adds what the spec does not say about drawings.

## 1. Decide what the figure claims

One figure, one claim. Write the claim as a sentence before drawing. It becomes the `aria-label` and the test at the end: a reader who sees only the figure should be able to say that sentence back.

Draw the mechanism, not its name. A box labeled "instrument" says less than the prose. The two inputs, the comparator, the residual, the threshold, and the verdict say what the word cannot. Show the parts the argument turns on and leave out the rest. Comparing two options means drawing the difference, not two labeled boxes side by side.

Label every arrow with what moves or what the edge does. An unlabeled arrow means "related somehow."

## 2. House style: the readout

The site's chrome reads as a calibrated instrument. Figures read the same way. The reference points are MIT Press technical diagrams (black line, labeled parts, nothing decorative) and Territory Studio's screen graphics for The Martian and Ex Machina (every element on screen is a reading: a value, a tick, a threshold, a state). The overlap is the style: line, label, number.

Vocabulary to draw with:

- Hairline strokes, 1px at drawn scale. 1.5px only for the one path the claim rests on.
- Mono labels, lowercase, short. Sentence case for the rare label that is a sentence.
- Tick marks and scales where a quantity is being compared. A residual gets a value and a threshold line, not an adjective.
- A verdict rendered as a state word in a chip-like frame: `pass`, `no`, `ill-posed`, `blocked`. The site's status-chip vocabulary applies.
- Readout values set in mono, right-aligned, with units.
- Dashed stroke means one thing per figure: the path that is not taken, or the edge that disappears. Say which in the caption.
- One accent, the patina `--accent`, on at most one element: the component the post is about. Everything else is `currentColor`.
- Fills are rare. `--surface` behind a group that needs separating, the accent behind the one emphasized element, nothing else. No gradients, no shadows.
- Whitespace is part of the drawing. Nodes get at least a node-width of gap when an edge label sits between them.

What the style excludes: weight 600 or higher (the site allows 400 and 500 only), hardcoded hex, Inter or any sans in a figure, title text inside the SVG (the title is the caption), rounded corners above `--radius-md`, decorative paths, icons.

## 3. Mechanics

Author inline `<svg>` by hand or from a script (section 4). Native shapes and `<text>` only. No `<script>`, `<style>`, `<foreignObject>`, no external images, no libraries.

- `viewBox="0 0 W H"`, no `width`/`height` attributes; the `.figure` container scales it. Pick W for the content: 720 reads at full column width, 880 and 960 are fine and scale down, wider than 1080 starts losing labels on phones.
- Colors through the page's tokens so both themes work: `stroke="currentColor"`, `fill="var(--surface)"`, `stroke="var(--accent)"`, `fill="var(--ink-tertiary)"`. `currentColor` resolves to `--ink` inside `.figure`. Never a literal hex.
- Fonts through tokens: `font-family="var(--font-mono)"` on the root `<svg>`, `font-weight="400"` default, `500` for the one emphasized label.
- Text sizes at drawn scale: 13 for node labels, 11 for edge labels and readout values, 10 only for tick numbers. Nothing larger; the caption carries the sentence.
- Arrowheads are a `<defs><marker>` with `fill="currentColor"`, referenced as `marker-end="url(#a)"`. Give markers short ids and keep ids unique on the page when two figures share it (`#a-fig02`).
- Align to an 8px grid. Shared baselines, even gaps.
- Wrap in the site pattern:

```html
<figure class="figure">
  <svg viewBox="0 0 880 320" role="img" aria-label="THE CLAIM SENTENCE" xmlns="http://www.w3.org/2000/svg" font-family="var(--font-mono)">
    ...
  </svg>
  <figcaption class="figure__caption">fig 02 · lowercase caption, one line, what the picture shows</figcaption>
</figure>
```

Caption form: `fig NN · ` then the claim in lowercase. Figures are numbered per page in reading order. No em dashes anywhere in a caption or label; use a middle dot or a colon.

Inline the SVG in the markdown page rather than loading it with `<img>`. An `<img>`-loaded SVG cannot see the page's CSS variables, so it will not follow the theme or the fonts. `public/images/writing/` is for photographs.

## 4. Data renders the figure

When the figure depicts a structure that will also be read by an agent (a loop, a graph of nodes and edges, a state machine), the structure is the source of truth and the SVG is a build product:

```
src/figures/<slug>/graph.json     the structure: nodes, edges, notes, types
src/figures/<slug>/render.py      reads graph.json, writes figure.svg
src/figures/<slug>/figure.svg     generated; paste or include into the page
```

The JSON carries more than the picture shows (a `note` per node, types, the thesis sentence). A page that wants the agent-facing form publishes the JSON next to the page as `<slug>/graph.json`. Rendering from data keeps the two faces from drifting: change the JSON, rerun, both update.

Hand-authored SVG is fine when there is no structure worth exposing.

## 5. Legibility check (required)

A figure is not done until `scripts/check_figure.py` passes on it. The check:

1. Rasterizes the SVG twice with the site's tokens substituted, once light and once dark, at 2x.
2. Reports every text element whose estimated extent overlaps a rect it does not belong to, and every pair of text elements that overlap each other.
3. Reports any literal hex color, any `font-weight` above 500, any `font-size` above 13 or below 10, any font family that is not the mono token.
4. Writes the two PNGs for a human look.

Then look at both PNGs. The checks catch text-on-rect collisions and token violations. They do not see a `<path>` crossing a box it should go around, a dashed line nicking a label, or a figure that fails to say its sentence. The first instrument figure passed the script and failed all three of those by eye; the eyes are part of the check. Note also that the raster machine may not have IBM Plex Mono installed, so the PNG falls back to another font; on the site the labels will be a little narrower. Read the claim sentence back from the dark PNG with the prose covered. If it does not come back, the figure is not done.

```powershell
python scripts/check_figure.py src/figures/instrument/figure.svg
```

## 6. Filing

- One figure per PR with the page change that uses it, or its own PR when it replaces an existing figure.
- Replacing a figure that predates this skill (the two SVGs under `public/images/writing/` do): convert to inline, retoken, recheck, and note in the PR which rules the old one broke.
- The PR description names the claim sentence and includes the two check PNGs.
