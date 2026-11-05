---
layout: ../layouts/BaseLayout.astro
title: "Home"
description: "Systems engineer building software for physical execution: geometry pipelines, fabrication automation, configurators, and field verification tools."
---

<div class="title-block">
  <div class="title-block__id">home · rev 1</div>
</div>

# I build software for physical execution

Geometry pipelines, fabrication automation, configurators, and field verification tools. I turn design intent and as-built reality into decisions crews and machines can act on.

I call these calibrated instruments for physical work. Each turns messy field reality into an executable, verifiable decision. Three readings from the instruments on this site:

<div class="reading-grid">
  <div class="reading-card">
    <div class="reading__label">directive engine · residual</div>
    <div class="reading__row"><span class="reading__value reading__value--small">6.6<span style="color:var(--ink-tertiary);font-weight:400"> → </span>0.0</span><span class="reading__unit">mm</span></div>
    <svg class="scale" viewBox="0 0 200 18" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><line x1="4" y1="10" x2="196" y2="10" stroke="currentColor" stroke-width="0.8"/><line x1="36.0" y1="3" x2="36.0" y2="17" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/><circle cx="109.6" cy="10" r="3" fill="none" stroke="var(--status-danger)" stroke-width="1.2"/><circle cx="4" cy="10" r="3.5" fill="var(--accent)"/></svg>
    <div class="reading__note">tol ±2.0 · 188 tests · <a href="/work/directive-engine/">deployed</a></div>
  </div>
  <div class="reading-card">
    <div class="reading__label">passthrough · drift ladder</div>
    <div class="reading__row"><span class="reading__value reading__value--small">1.9e-3</span><span class="reading__unit">drift max, rung 1</span></div>
    <svg class="scale" viewBox="0 0 200 18" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><line x1="4" y1="10" x2="196" y2="10" stroke="currentColor" stroke-width="0.8"/><circle cx="28" cy="10" r="3.5" fill="var(--accent)"/><circle cx="76" cy="10" r="3.5" fill="var(--accent)"/><circle cx="124" cy="10" r="3" fill="none" stroke="var(--status-danger)" stroke-width="1.2"/><line x1="168" y1="5" x2="176" y2="15" stroke="var(--ink-tertiary)" stroke-width="1"/><line x1="176" y1="5" x2="168" y2="15" stroke="var(--ink-tertiary)" stroke-width="1"/></svg>
    <div class="reading__note">rung 3 ill-posed · rung 4 blocked · <a href="/work/passthrough/">validated</a></div>
  </div>
  <div class="reading-card">
    <div class="reading__label">compass · smoke suite</div>
    <div class="reading__row"><span class="reading__value reading__value--small">23<span style="color:var(--ink-tertiary);font-weight:400"> / </span>1</span><span class="reading__unit">passed / skipped</span></div>
    <svg class="scale" viewBox="0 0 200 18" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><line x1="4" y1="10" x2="196" y2="10" stroke="currentColor" stroke-width="0.8"/><line x1="4" y1="10" x2="188" y2="10" stroke="var(--accent)" stroke-width="3"/><line x1="188" y1="10" x2="196" y2="10" stroke="var(--ink-tertiary)" stroke-width="3"/></svg>
    <div class="reading__note">stt phrase set not built · <a href="/work/compass/">in development</a></div>
  </div>
</div>

The hardest part of installing complex assemblies isn't detecting that something is off. It's expressing the correction in a format that's unambiguous, constrained by what's allowed, and verifiable after adjustment.

---

## Flagship Instrument

<a href="/work/directive-engine/" class="project-card">
  <div class="project-card__meta">
    <span class="chip chip--ok">CALIBRATED</span>
  </div>
  <h3>Directive Engine</h3>
  <p>Convert nominal ↔ as-built deltas into installer-ready directive cards (move / rotate / index), with 3D visualization and verification loops.</p>
</a>

<p>The geometry-to-directive loop is substrate-agnostic. The same spine retargets from architectural installation to manufacturing and aerospace assembly, anywhere a built part has to match its model.</p>

<div class="artifact-bar">
  <a href="/demo/" class="btn btn--primary">Open Live Demo</a>
  <a href="/work/directive-engine/" class="artifact-link">Case Study →</a>
</div>

---

## Instruments I Build

<div class="directive-card">
  <h4 class="directive-card__title">Directive Generation</h4>
  <div class="directive-card__constraints">
    <span class="chip chip--clamped">CONSTRAINED</span>
    <span class="chip">TOLERANCED</span>
  </div>
  <p class="directive-card__action">Actionable correction steps with DOF constraints and tolerance bounds.</p>
</div>

<div class="directive-card">
  <h4 class="directive-card__title">3D Visualization</h4>
  <div class="directive-card__constraints">
    <span class="chip">BROWSER-FIRST</span>
    <span class="chip">LEGIBLE</span>
  </div>
  <p class="directive-card__action">Web-based viewers that make adjustments auditable and field-ready.</p>
</div>

<div class="directive-card">
  <h4 class="directive-card__title">Verification Loops</h4>
  <div class="directive-card__constraints">
    <span class="chip chip--ok">PASS</span>
    <span class="chip chip--blocked">FAIL</span>
  </div>
  <p class="directive-card__action">Before/after deviation checks so teams close the gap with confidence.</p>
</div>

<div class="directive-card">
  <h4 class="directive-card__title">SurveyLink</h4>
  <div class="directive-card__constraints">
    <span class="chip">PEER-REVIEWED</span>
    <span class="chip">METROLOGY</span>
  </div>
  <p class="directive-card__action">Streams total-station data to a web app for real-time field verification and as-built reconciliation. Deployed on-site; peer-reviewed (Taylor &amp; Francis, 2022).</p>
  <a href="https://www.tandfonline.com/doi/abs/10.1080/24751448.2022.2116230" class="artifact-link" target="_blank" rel="noopener">Paper →</a>
</div>

<div class="directive-card">
  <h4 class="directive-card__title">passthrough</h4>
  <div class="directive-card__constraints">
    <span class="chip">VALIDATED</span>
    <span class="chip">OPEN SOURCE</span>
  </div>
  <p class="directive-card__action">A reverse-problem instrument: carries a morphed mesh back to an analytic CAD surface, isolating parameterization recovery from representation richness. 123 passing tests, public.</p>
  <a href="https://github.com/barnes-ngb/passthrough" class="artifact-link" target="_blank" rel="noopener">Repository →</a>
  <a href="/work/passthrough/" class="artifact-link">Case Study →</a>
</div>

<div class="directive-card">
  <h4 class="directive-card__title">Customer-facing Design Platforms</h4>
  <div class="directive-card__constraints">
    <span class="chip">MODA</span>
  </div>
  <p class="directive-card__action">3D selection and quote-entry instruments that turn customer intent into spec-ready configurations without handoffs. Built to collapse the gap from “I want this” to “here’s the exact build + price.”</p>
  <a href="/work/moda-design-platform/" class="artifact-link">Case Study →</a>
</div>

<div class="directive-card">
  <h4 class="directive-card__title">Fabricator API / Feasibility Bumpers</h4>
  <div class="directive-card__constraints">
    <span class="chip">GRASSHOPPER</span>
  </div>
  <p class="directive-card__action">Fabrication-aware bumpers embedded in the designer workflow, flagging infeasible geometry and rerouting choices before downstream rework. Keeps exploration open while enforcing what can actually be built.</p>
  <a href="/work/fabricator-api/" class="artifact-link">Case Study →</a>
</div>

---

## Calibration Background

<div class="callout callout--info">
  <span class="callout__icon">⚙</span>
  <div class="callout__content">
    <strong>Field-tested at Zahner.</strong> Built geometry pipelines, deviation analysis, and installer-facing interfaces for complex metal fabrication and installation. Deployed where <code>RMS &lt; 5mm</code> matters.
  </div>
</div>

[See all instruments →](/work/) · [About my approach →](/about/)

---

## Get in Touch

<div class="artifact-bar">
  <a href="mailto:barnes.ngb@gmail.com" class="artifact-link">barnes.ngb@gmail.com</a>
  <a href="https://www.linkedin.com/in/barnesngb/" class="artifact-link">LinkedIn</a>
  <a href="https://github.com/barnes-ngb" class="artifact-link">GitHub</a>
</div>
