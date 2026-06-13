---
layout: ../../layouts/BaseLayout.astro
title: "Work"
description: "Instruments I've built. Stage and year, plainly listed."
---

<div class="title-block">
  <div class="title-block__id">work / index · rev 1</div>
</div>

<div class="page-header">
  <h1 class="page-header__title">Work</h1>
  <p class="page-header__subtitle">Instruments I've built. Stage and year, plainly listed.</p>
</div>

<div class="summary-strip">
  <span><span class="summary-strip__label">instruments </span>4</span>
  <span><span class="summary-strip__label">deployed </span>3</span>
  <span><span class="summary-strip__label">earliest </span>2025</span>
  <span><span class="summary-strip__label">latest </span>2026</span>
</div>

<div class="catalog-group-label">deployed</div>

<div class="catalog-row">
  <span class="catalog-row__index">01</span>
  <div class="catalog-row__body">
    <div class="catalog-row__title"><a href="/work/directive-engine/">Directive Engine</a></div>
    <div class="catalog-row__subtitle">Convert nominal ↔ as-built deltas into installer-ready directive cards.</div>
  </div>
  <div class="catalog-row__meta">
    <span class="status-chip status-chip--deployed">deployed</span>
    <span class="catalog-row__year">2025 · ts</span>
    <a href="https://directive-engine.vercel.app/" class="catalog-row__sublink" target="_blank" rel="noopener">live demo →</a>
  </div>
</div>

<div class="catalog-row">
  <span class="catalog-row__index">02</span>
  <div class="catalog-row__body">
    <div class="catalog-row__title"><a href="/work/moda-design-platform/">Moda Design Platform</a></div>
    <div class="catalog-row__subtitle">Interactive design platform for exploring configurable facade patterns, finishes, and fabrication-ready options.</div>
  </div>
  <div class="catalog-row__meta">
    <span class="status-chip status-chip--deployed">deployed</span>
    <span class="catalog-row__year">2026 · ts</span>
  </div>
</div>

<div class="catalog-row">
  <span class="catalog-row__index">03</span>
  <div class="catalog-row__body">
    <div class="catalog-row__title"><a href="/work/fabricator-api/">Fabricator API</a></div>
    <div class="catalog-row__subtitle">Parametric feasibility tooling that evaluates panelization, tolerances, and fabrication constraints directly in design workflows.</div>
  </div>
  <div class="catalog-row__meta">
    <span class="status-chip status-chip--deployed">deployed</span>
    <span class="catalog-row__year">2025 · grasshopper</span>
  </div>
</div>

<div class="catalog-group-label">validated</div>

<div class="catalog-row">
  <span class="catalog-row__index">04</span>
  <div class="catalog-row__body">
    <div class="catalog-row__title"><a href="/work/passthrough/">passthrough</a></div>
    <div class="catalog-row__subtitle">Round-trip instrument for the reverse problem. Carry identity across the mesh boundary; the failures separate into position, which it closes, and curvature, which it does not.</div>
  </div>
  <div class="catalog-row__meta">
    <span class="status-chip status-chip--research">validated</span>
    <span class="catalog-row__year">2026 · python · c#</span>
    <a href="https://github.com/barnes-ngb/passthrough" class="catalog-row__sublink" target="_blank" rel="noopener">repository →</a>
  </div>
</div>

---

## Instrument Template

Building your own case study? See the [instrument documentation template](/work/_template/) for the recommended structure: Problem → Signal → Calibration → Constraints → Action → Verification → Artifacts.
