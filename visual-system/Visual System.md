# SystemsForge — Visual System Spec

**Status:** Draft v1 · proposed for `systemsforge.build`
**Owner:** Nathan Barnes
**Stack target:** Astro 5.16, plain CSS, no Tailwind
**Last updated:** 2026-05-16

---

## Purpose

This document specifies the visual language for `systemsforge.build`. It exists so that:

1. The site's chrome reads as a calibrated instrument, not a generic developer portfolio.
2. Anyone (human or Claude Code) can apply the system consistently without re-deriving it.
3. The system has a single source of truth — when something changes, this file changes first.

The companion files `tokens.css` and `components.css` are the executable form of this spec. If they drift from this doc, this doc wins; update the CSS to match.

---

## Scope

**In:** color tokens, typography, spacing, borders, status-chip vocabulary, page-level patterns (title block, metadata strip, section header, figure, catalog row, limits callout, lab entry).

**Out:** copy, content architecture, deployment, Astro component composition (above the CSS layer). The system tells you *how* to render a title block; it doesn't tell you what to put in one.

---

## Status — open decisions

Before full implementation, the following are PROPOSED and need sign-off. The CSS files use these values as placeholders; updating them is a single-line change.

| Decision | Proposed value | Notes |
|---|---|---|
| Accent color (light mode) | `#3D6B5C` | A grounded patina copper-green. Calibrate by sampling from a real patinated copper photo from the patina-model work. |
| Accent color (dark mode) | `#7FAB99` | Lighter partner of the above. |
| Paper color (light mode) | `#FAF8F4` | Subtle warm off-white. Plain `#FFFFFF` is the alternative if the warmth feels editorial. |
| Paper color (dark mode) | `#14181C` | Deep neutral, slight cool cast. |
| Sans typeface | IBM Plex Sans | Free, technical, coherent with Plex Mono. Alternatives: Inter, Söhne (paid). |
| Mono typeface | IBM Plex Mono | Pairs with Plex Sans. Alternatives: JetBrains Mono, Berkeley Mono (paid). |
| Serif typeface (lab pages only) | Fraunces | Distinctive, characterful. Alternatives: IBM Plex Serif (more coherent), Source Serif 4. |
| Numbered entries on catalog | Keep | Confirmed. |
| Default catalog grouping | By stage | Confirmed. |

---

## 1 · Design tokens

### 1.1 Color

All tokens defined on `:root`, overridden under `:root[data-theme="dark"]` for the explicit toggle and under `@media (prefers-color-scheme: dark)` (scoped to `:root:not([data-theme="light"])`) as the system-preference fallback. The toggle in `BaseLayout.astro` writes `data-theme` to `<html>`; the explicit selector wins over the media query so a user choice always sticks.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#FAF8F4` | `#14181C` | Page background |
| `--surface` | `#FFFFFF` | `#1B2025` | Card/figure background |
| `--ink` | `#1A1A1A` | `#ECECEC` | Body text, headings |
| `--ink-secondary` | `#555555` | `#A6A6A6` | Subtitles, metadata values |
| `--ink-tertiary` | `#888888` | `#6B6B6B` | Metadata labels, captions |
| `--accent` | `#3D6B5C` | `#7FAB99` | Patina — deployed chips, fig 01 highlight, brand mark |
| `--accent-soft` | `#E8EFEC` | `#22302C` | Pale patina fills (rare; for hover states only) |
| `--border` | `rgba(26,26,26,0.12)` | `rgba(236,236,236,0.14)` | All hairlines |
| `--border-strong` | `rgba(26,26,26,0.22)` | `rgba(236,236,236,0.25)` | Limits callout, featured rows |
| `--status-info` | `#3578B5` | `#7AAFE0` | `in review`, `prototype` chips |
| `--status-warning` | `#A56A0E` | `#E0AC5C` | `pending` chips |
| `--status-danger` | `#9E3232` | `#E08585` | `blocked`, `archived` (if used in red) |

### 1.2 Typography

```
Sans:  'IBM Plex Sans', system-ui, sans-serif
Mono:  'IBM Plex Mono', ui-monospace, monospace
Serif: 'Fraunces', 'Source Serif 4', Georgia, serif   ← lab pages only
```

| Token | Size (rem / px) | Use |
|---|---|---|
| `--text-xs` | 0.6875 / 11 | Mono title block, captions, chip text |
| `--text-sm` | 0.8125 / 13 | Catalog subtitles, lab margin column |
| `--text-base` | 0.9375 / 15 | Body text inside cards, lab note prose |
| `--text-md` | 1.000 / 16 | Page body, subtitle under H1 |
| `--text-lg` | 1.125 / 18 | Sub-headings (H3) |
| `--text-xl` | 1.250 / 20 | Section headings (H2) |
| `--text-2xl` | 1.625 / 26 | Page title (H1) |
| `--text-3xl` | 2.000 / 32 | Reserved — hero only, use sparingly |

**Two weights only:** `400` regular, `500` medium. No `600+`. This is a hard rule.

| Token | Value | Use |
|---|---|---|
| `--lh-tight` | 1.20 | Page titles |
| `--lh-snug` | 1.35 | Section headings |
| `--lh-normal` | 1.55 | Body text |
| `--lh-relaxed` | 1.70 | Long-form reading (lab notes, case study prose) |

| Token | Value | Use |
|---|---|---|
| `--tracking-wide` | 0.05em | Status chips, mono metadata labels |
| `--tracking-wider` | 0.08em | Section header indices (`01 · problem`) |
| `--tracking-widest` | 0.10em | Title block strip |

**Sentence case everywhere.** Never Title Case. ALL CAPS only inside a mono title block context, and even there prefer lowercase + tracking.

### 1.3 Spacing

8-point scale (with one 4-point quarter step for micro adjustments).

| Token | Value | Use |
|---|---|---|
| `--space-1` | 4px | Gap between chip text and chip border |
| `--space-2` | 8px | Inline gaps, small label-value gaps |
| `--space-3` | 12px | Component-internal padding |
| `--space-4` | 16px | Card padding (compact) |
| `--space-5` | 24px | Card padding (standard), gap between rows |
| `--space-6` | 32px | Gap between page sections |
| `--space-7` | 48px | Major section breaks |
| `--space-8` | 64px | Reserved — hero-area only |

### 1.4 Borders & radii

| Token | Value | Use |
|---|---|---|
| `--border-thin` | 0.5px | Default for almost everything |
| `--border-emphasis` | 2px | Limits callout left-rule, featured items only |
| `--radius-sm` | 3px | Status chips |
| `--radius-md` | 6px | Figures, content cards, directive-card artifacts |
| `--radius-lg` | 8px | Page-level containers (rare) |

**Rule:** never round corners on single-sided borders. If using `border-left` accent, `border-radius: 0`.

### 1.5 Layout

| Token | Value | Use |
|---|---|---|
| `--content-max` | 720px | Page container max-width |
| `--prose-max` | 64ch | Inline `<p>` and prose paragraphs |
| `--page-pad-x` | clamp(20px, 5vw, 40px) | Horizontal page padding |

---

## 2 · Patterns

Each pattern below has a single canonical class. Don't fork the styling per page; if a variant is needed, name it (`.status-chip--deployed` not a separate `.deployed-tag`).

### 2.1 Title block

The mono strip with project ID on the left and status chip on the right. Sits below the site nav, above the page H1.

```html
<div class="title-block">
  <div class="title-block__id">work / instrument 03 · rev 2</div>
  <span class="status-chip status-chip--deployed">deployed</span>
</div>
```

### 2.2 Status chip

One component, semantic variants. Lowercase content always.

```
.status-chip                — bordered, color comes from variant
.status-chip--deployed      — accent (patina) border + text
.status-chip--in-review     — info border + text
.status-chip--pending       — warning border + text
.status-chip--research      — ink-tertiary border + text (quiet)
.status-chip--archived      — ink-tertiary border + text (same as research, semantically different)
.status-chip--prototype     — info, optional
```

### 2.3 Metadata strip

Mono row of label-value pairs, separated by space, with a thin rule above and below.

```html
<div class="metadata-strip">
  <span><span class="metadata-strip__label">built </span>2025</span>
  <span><span class="metadata-strip__label">stack </span>ts · three.js · vite</span>
  <span><span class="metadata-strip__label">tol </span>±1mm</span>
  <span><span class="metadata-strip__label">stage </span>v0.2</span>
</div>
```

### 2.4 Section header (numbered)

```html
<div class="section-header">
  <div class="section-header__index">01 · problem</div>
  <h2>The directive layer is missing.</h2>
</div>
```

### 2.5 Figure with caption

The container that wraps any diagram, image, or visual artifact.

```html
<figure class="figure">
  <!-- svg / img / artifact here -->
  <figcaption class="figure__caption">fig 01 · pipeline: scan to directive</figcaption>
</figure>
```

### 2.6 Catalog row

The repeating row in the work index.

```html
<div class="catalog-row">
  <span class="catalog-row__index">01</span>
  <div class="catalog-row__body">
    <div class="catalog-row__title">Directive Engine</div>
    <div class="catalog-row__subtitle">Convert nominal-vs-as-built deltas into installer-ready directive cards.</div>
  </div>
  <div class="catalog-row__meta">
    <span class="status-chip status-chip--deployed">deployed</span>
    <span class="catalog-row__year">2025 · ts</span>
    <a href="..." class="catalog-row__sublink">live demo →</a>
  </div>
</div>
```

`.catalog-row__sublink` — small mono secondary link inside `__meta`. Use for at-most-one quiet pointer per row (live demo, external repo, paper). Patina text, hairline underline, mono, text-xs. Never use for the primary case-study link — that's the row title itself, which is the whole row's primary affordance.

### 2.7 Limits callout

The trademark honest-scoping section. Single-sided left rule, no rounded corners.

```html
<aside class="limits-callout">
  <div class="limits-callout__label">limits</div>
  <p>v0.2 is a minimal shell. Panel-level only — no assembly groups. Re-scan is manual.</p>
</aside>
```

### 2.8 Lab entry

The two-column research-note layout. Margin column on the left holds date / entry number / project tag. Body uses serif type.

```html
<article class="lab-entry">
  <aside class="lab-entry__margin">
    <div class="lab-entry__date">2026-04-18</div>
    <div class="lab-entry__id">entry 014</div>
    <div class="lab-entry__project">patina-model</div>
  </aside>
  <div class="lab-entry__body">
    <h3>A weathering function for variable copper</h3>
    <p>First passes assumed uniform exposure. Field reality has gradient drift...</p>
  </div>
</article>
```

### 2.9 Writing footer

Closes every writing post (and any future post-template page like lab entries that read as authored pieces). Three jobs only: mark the end of the post, attribute it, point somewhere useful next.

```html
<footer class="writing-footer">
  <div class="writing-footer__end-mark">— end · entry 011 · 2026-05-13</div>

  <div class="writing-footer__byline">
    <div class="writing-footer__name">Nathan Barnes</div>
    <div class="writing-footer__role">
      Design-to-Fabrication Systems Engineer ·
      <a href="mailto:barnes.ngb@gmail.com" class="writing-footer__contact">barnes.ngb@gmail.com</a>
    </div>
  </div>

  <div class="writing-footer__see-also">
    <div class="writing-footer__see-also-label">see also</div>
    <ul class="writing-footer__see-also-list">
      <li class="writing-footer__see-also-item">
        <a href="/work/directive-engine" class="writing-footer__see-also-link">Directive Engine</a>
        <span class="writing-footer__see-also-tag">instrument 03</span>
      </li>
      <li class="writing-footer__see-also-item">
        <a href="/demo" class="writing-footer__see-also-link">Live demo</a>
        <span class="writing-footer__see-also-tag">browser</span>
      </li>
    </ul>
  </div>
</footer>
```

**Rules:**

- End-mark format: `— end · entry NNN · YYYY-MM-DD`. The em-dash + tracking-wider mono treatment matches figure captions. Entry number is the same one used in the title block at the top of the page; date is the post's published date.
- Byline is always present. Name + role + contact, in that order, in restrained sans.
- See-also is optional but should appear whenever the post has at least one meaningful related link. Don't pad with filler — three rows is plenty, two is fine, zero is acceptable.
- See-also items have two parts: a link on the left (the thing), a mono tag on the right (what kind of thing it is). Tag examples: `instrument 03`, `entry 010`, `browser`, `paper · acadia 2024`, `github`, `external`.
- No share buttons, no subscribe forms, no comments, no social row, no headshot. The footer is restrained on purpose.
- On lab pages (§2.8), the `.writing-footer` is not used — lab entries close more like log entries and need their own pattern when the time comes.

---

## 3 · Implementation plan

Four phases. Each is a self-contained pull request.

### Phase 1 — Foundation (1–2 hours)

1. Create `src/styles/tokens.css` from this spec.
2. Create `src/styles/components.css` from this spec.
3. Import both in `BaseLayout.astro`, replacing the current global stylesheet.
4. Add Google Fonts `<link>` for IBM Plex Sans, IBM Plex Mono, Fraunces.
5. Smoke-test: load the homepage in the dev server, confirm body type renders in Plex Sans and the page background uses `--paper`.

### Phase 2 — Apply to existing pages (2–3 hours)

Convert one page at a time. Don't try to update all five at once.

1. `index.md` — homepage. Apply title block + metadata strip pattern.
2. `work/directive-engine.md` — case study. Apply title block, section headers with indices, figure pattern.
3. `work/index.md` — catalog. Rebuild as catalog rows grouped by stage.
4. `about.md` — bio. Lightweight: title block, prose.
5. `contact.md` — contact. Lightweight: title block, prose.
6. `writing/*.md` — apply title block, metadata strip, figure pattern,
   and close with .writing-footer (§2.9).

Per page: read the existing content, wrap in the new patterns, verify visually, commit.

### Phase 3 — Add lab surface (3–4 hours)

The lab page is new. It uses the same tokens but a different content pattern (lab-entry, serif body).

1. Create `src/pages/lab/index.md` — list of research entries.
2. Create `src/pages/lab/patina-model.md` (or similar) — at least one full entry.
3. Add `lab` to the nav.

### Phase 4 — Polish (1–2 hours)

1. Add a "what I'm looking for" page (positioning surface for visiting founders).
2. Surface publications somewhere (sidebar on about, or its own page).
3. Add the resume PDF to `public/` and link from About.

---

## 4 · Using this with Claude Code (PowerShell)

The intended flow:

1. Copy `VISUAL_SYSTEM.md`, `tokens.css`, and `components.css` into the repo at `docs/visual-system/`.
2. In a Claude Code session, point it at the doc and one phase:

   ```powershell
   # from the site repo root, in PowerShell
   cd C:\path\to\barnes-portfolio-site-astro
   claude code
   ```

   Then in the session:

   > Read `docs/visual-system/VISUAL_SYSTEM.md`. Implement Phase 1 only. Show me the diff before committing.

3. After Phase 1 lands and you've previewed it, run Phase 2 in a fresh session, scoped to one page at a time:

   > Read `docs/visual-system/VISUAL_SYSTEM.md`. Apply the patterns to `src/pages/index.md`. Don't change content — only wrap in the new structure. Show me the diff.

**Why one phase at a time:** keeps diffs reviewable, lets you catch a rendering issue before it propagates across five pages, matches the "ask before modifying" preference.

---

## 5 · What this spec doesn't cover

Honest scope. The following are deliberately out of band, to be decided later or left as-is:

- **Animations.** None defined. The Directive Engine demo has its own animations; the site chrome should be still.
- **Imagery treatment.** Photo aspect ratios, captions for raster images, hover behavior on figures — TBD when you have actual photos to place.
- **Navigation transitions / mobile menu.** Astro defaults are fine for v1.
- **Forms.** The contact page has none; if it ever does, design at that point.
- **Search / filter on the catalog.** Visible filter strip is sketched, behavior is not specified.
- **Print stylesheet.** Worth doing eventually (your case studies would print beautifully) but not v1.
- **Final accent color.** The proposed patina hex is calibrated for legibility but not sampled from your actual work. Worth a single short session to lock in.
