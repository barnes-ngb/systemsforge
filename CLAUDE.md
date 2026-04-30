# [CLAUDE.md](http://CLAUDE.md) — barnes-portfolio-site-astro

Context and conventions for Claude (and any other AI agent) working on this repo. Read this before making changes.

## What this repo is

The source for **[systemsforge.build](http://systemsforge.build)**, Nathan Barnes' personal site. Astro 5.x static-site setup, Markdown pages with a single `BaseLayout.astro`, custom CSS in `src/styles/global.css`. Deployed to Vercel; custom domain points there. The site's `astro.config.mjs` `site:` field must be `https://systemsforge.build`.

This is the **deepest, slowest layer** of Nathan's public presence. LinkedIn and other surfaces point here for "read more." Site cadence is project-by-project, not weekly. No urgency in any single change.

A separate `career-repo` holds the source-of-truth identity, tracks, and project files. **This repo is downstream of that one — never write back to career-repo from here.** If site content conflicts with career-repo content, flag it in the PR description; don't reconcile silently.

## Positioning the site reflects

The site is intentionally **track-neutral on its surface** — it doesn't pick AEC-prefab vs aerospace vs manufacturing-SaaS. The unifying thesis across all case studies is **"instruments, not apps"**: software with contracts, tests, calibration, and verification loops, built for fabrication and field environments where tolerances and reality matter.

Vocabulary that fits the thesis: instruments, calibration, constraints, verification, directives, residual, tolerance, fabrication-ready, field reconciliation, design-to-fabrication. Vocabulary that does **not** fit: dashboards, AI-powered, transformative, revolutionary, leverage (as a verb), seamless, robust, world-class.

The home-page subtitle is "Design-to-Fabrication Systems Engineer." Do not change this without explicit instruction.

## Discretion constraints (hard rules)

These are non-negotiable. If a proposed change might violate one, refuse the change in the PR description and ask for clarification.

1. **No client names from Nathan's employer (A. Zahner Company).** The exception is projects already public on Zahner's own website (`azahner.com/works/...` or `azahner.com/profiles/...`); those may be referenced with the public URL. Even then, prefer linking to the public Zahner page over describing the project in detail here. If unsure whether something is public, refuse and ask.
2. **No "looking for work" / "open to work" / "available now" signaling anywhere on the site.** This includes "exploring roles," "currently looking," lists of target industries phrased as "I'm interested in roles in X," resume PDFs prominently linked from main pages, contact-page CTAs that read as job inquiries. Vertical interests phrased as **operating focus** are fine; phrasing as job search is not. The line is "what I work on" vs "what I want next."
3. **No overclaim on metrics or seniority.** Numbers must be defensible per the source-of-truth career-repo. If a metric appears in the site without an obvious source, flag it in the PR description rather than passing it through. Specifically: round numbers ($2M, 50%, 10x), claims without an artifact link, plurals doing rhetorical work ("APIs" when there's one), and seniority words ("led," "managed," "architected") should be checked against actual role.
4. **Employer naming is case-by-case.** Zahner may be named in a soft, factual way ("Field-tested at Zahner") without superlatives or hyperlinks. Avoid "the most ___ ___ in the industry" framings.

## Site structure

- `src/pages/[index.md](http://index.md)` — home
- `src/pages/[about.md](http://about.md)` — bio
- `src/pages/[contact.md](http://contact.md)` — contact
- `src/pages/[demo.md](http://demo.md)` — Directive Engine demo walkthrough
- `src/pages/work/[index.md](http://index.md)` — case-study catalog
- `src/pages/work/{slug}.md` — individual case studies
- `src/pages/work/_[template.md](http://template.md)` — template for new case studies
- `src/layouts/BaseLayout.astro` — single layout for all pages; reads frontmatter `title`, `description`, `og` fields
- `src/styles/global.css` — all styling

Pages currently in `src/pages/work/` but **not** linked from the catalog (`[zahner-labs.md](http://zahner-labs.md)`, `[amherst-science-center.md](http://amherst-science-center.md)`, `[the-mexican-museum.md](http://the-mexican-museum.md)`) are abandoned drafts. Do not edit, link, or delete them without explicit instruction. They contain no discretion violations as of the last audit.

## Case-study template (the "Directive Engine pattern")

Long-form case studies on `src/pages/work/{slug}.md` follow this structure:

1. **Problem** — what's broken in the world, briefly.
2. **Signal** — how Nathan noticed the problem (specific, concrete moment).
3. **Calibration** — what was measured / instrumented to make the problem precise.
4. **Constraints** — what bounds the solution (tolerances, time, format, deployment).
5. **Action** — what was built or done.
6. **Verification** — how it was checked. Quantitative if defensible; qualitative if not.
7. **Artifacts** — links to demo, repo, paper, public reference. Real links only — no `href="#"`.
8. **Limits** — honest scope statement. What it does, what it doesn't.

Case studies should match this template by default. `[directive-engine.md](http://directive-engine.md)` is the canonical reference. If a case study is being added or refactored, follow this structure unless the issue explicitly says otherwise.

## Catalog page conventions (`src/pages/work/[index.md](http://index.md)`)

- Each card uses a `chip` class to indicate state. `chip--ok` means "calibrated, deployed, verified" — only use when actually true. `chip--pending` for in-flight work. Don't apply `chip--ok` to drafts or aspirational projects.
- Card link text follows the form `Case Study →` for internal page links, and a short artifact name (`Repository →`, `Paper →`, `Live Demo →`) for external links. **Never** "Internal Case Study" — that's misleading; everything on the public site is public.

## Styling and components

There are no JS components or React. All styling is via global CSS classes. Common classes:
- `.artifact-bar` — container for a row of artifact links
- `.artifact-link` — individual link inside an artifact-bar
- `.callout`, `.callout--warn`, `.callout--info` — bordered emphasis blocks
- `.chip`, `.chip--ok`, `.chip--pending` — small status pills

When adding markup, use existing classes rather than inventing new ones. If a new class is genuinely needed, propose it in the PR description and add it to `global.css` deliberately.

## Theme and accessibility

The site has a dark/light theme toggle handled in `BaseLayout.astro` via `localStorage`. Don't add inline color values; use CSS variables defined in `global.css`. Maintain existing semantic HTML — headings in order, alt text on images, real link destinations.

## Coordination with other AI sessions

Nathan runs a multi-chat workflow. **This repo is the source of truth for the public site only.** Other surfaces (LinkedIn, resumes, applications) live elsewhere and have separate constraints. If an instruction in an issue references those surfaces, treat it as background context only — do not edit non-site content from here.

If an issue's instruction conflicts with this [CLAUDE.md](http://CLAUDE.md), follow the issue but flag the conflict prominently in the PR description so Nathan can reconcile.

## Out of scope for this repo

- Resume PDFs, cover letters, application materials
- LinkedIn post drafts, profile copy
- Career-repo source-of-truth files (identity, tracks, credentials, experience)
- Any tracker / job-search dashboard

If an issue asks for any of the above, refuse and ask Nathan to file the issue on the appropriate repo or chat.

## Working style

- Small PRs, one batch per issue. Don't combine batches that target different files unless the issue explicitly says so.
- Don't refactor surrounding code "while you're in there." Stay strictly within the issue scope.
- Verbatim find-string failures: if a find-string in the issue doesn't match the file exactly, report it in the PR description and stop. Don't guess at near-matches.
- After making changes, briefly summarize each change in the PR description, including any constraints checked.
