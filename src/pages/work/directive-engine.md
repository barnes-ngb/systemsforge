---
layout: ../../layouts/BaseLayout.astro
title: "Directive Engine"
description: "Align reality to intent → generate installer-ready directives with calibration, visualization, and verification."
---

<div class="instrument-hero">
  <div class="instrument-hero__status">
    <span class="chip chip--ok">CALIBRATED</span>
    <span class="chip">BROWSER-FIRST</span>
    <span class="chip">FIELD-READY</span>
  </div>
  <h1 class="instrument-hero__title">Directive Engine</h1>
  <p class="instrument-hero__subtitle">Convert nominal ↔ as-built deltas into <strong>installer-ready directive cards</strong> (move/rotate/index), with 3D visualization and verification loops.</p>
</div>

<div class="artifact-bar">
  <a href="/demo/" class="btn btn--primary btn--large">Open Live Demo</a>
  <a href="https://github.com/barnes-ngb/directive-engine" class="artifact-link">Repository</a>
  <a href="mailto:barnes.ngb@gmail.com" class="artifact-link">Contact</a>
</div>

![Directive Engine Screenshot](/images/Directive-Engine.png)

---

## Problem

When something is off in the field, the hardest part is not detecting it — it's expressing the correction in a **field-executable format** that's:

<div class="steps">
  <div class="step">
    <span class="step__number">1</span>
    <div class="step__content">
      <div class="step__title">Unambiguous</div>
      <div class="step__description">Clear action in a known reference frame — no interpretation required.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">2</span>
    <div class="step__content">
      <div class="step__title">Constrained</div>
      <div class="step__description">Respects what's physically allowed (DOF limits, anchor dependencies).</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">3</span>
    <div class="step__content">
      <div class="step__title">Verifiable</div>
      <div class="step__description">Can be checked after adjustment — did the gap close?</div>
    </div>
  </div>
</div>

---

## Inputs (Signal)

<div class="metric-grid">
  <div class="metric-card">
    <span class="metric-card__label">Nominal Model</span>
    <span class="metric-card__value">Design Intent</span>
    <span class="metric-card__unit">3D geometry + anchor points</span>
  </div>
  <div class="metric-card">
    <span class="metric-card__label">As-Built Scan</span>
    <span class="metric-card__value">Field Reality</span>
    <span class="metric-card__unit">Point cloud or survey data</span>
  </div>
</div>

**Data format:** JSON with paired nominal/as-built coordinates, part IDs, and optional constraint metadata.

---

## Calibration

The engine aligns nominal and as-built coordinate systems using anchor point pairs. Calibration quality is measured by:

<div class="metric-grid">
  <div class="metric-card">
    <span class="metric-card__label">RMS Residual</span>
    <span class="metric-card__value">2.3<span class="metric-card__unit">mm</span></span>
    <div class="metric-card__status">
      <span class="chip chip--ok">PASS</span> &lt; 5mm threshold
    </div>
  </div>
  <div class="metric-card">
    <span class="metric-card__label">Outlier Count</span>
    <span class="metric-card__value">0</span>
    <div class="metric-card__status">
      <span class="chip chip--ok">PASS</span> no residuals &gt; 10mm
    </div>
  </div>
</div>

<div class="callout callout--warning">
  <span class="callout__icon">⚠</span>
  <div class="callout__content">
    <div class="callout__title">Calibration Warning</div>
    If <code>RMS &gt; 5mm</code>, re-check anchor pairing before proceeding. High residuals propagate to all downstream directives.
  </div>
</div>

---

## Constraints / DOF

Each part has defined degrees of freedom that limit valid corrections:

<div class="directive-card">
  <h4 class="directive-card__title">Example: Panel P-0132</h4>
  <div class="directive-card__constraints">
    <span class="chip chip--clamped">TX CLAMPED</span>
    <span class="chip chip--clamped">TY CLAMPED</span>
    <span class="chip chip--ok">TZ FREE</span>
    <span class="chip chip--ok">RX FREE</span>
    <span class="chip chip--clamped">RY CLAMPED</span>
    <span class="chip chip--clamped">RZ CLAMPED</span>
  </div>
  <p class="directive-card__action">Panel can only be adjusted in Z-translation and X-rotation (shimming + tilt).</p>
  <div class="directive-card__dof">DOF: 2 of 6</div>
</div>

---

## Action Format (Directive Card)

The engine outputs **directive cards** — structured correction instructions:

<div class="directive-card">
  <div class="directive-card__header">
    <h4 class="directive-card__title">DIRECTIVE: P-0132</h4>
    <span class="chip chip--pending">PENDING</span>
  </div>
  <div class="directive-card__constraints">
    <span class="chip">TRANSLATE</span>
    <span class="chip">ROTATE</span>
  </div>
  <p class="directive-card__action">
    <strong>Action:</strong> Translate +12mm Z, Rotate -0.3° about X-axis<br>
    <strong>Frame:</strong> Part-local (or site grid)<br>
    <strong>Verify:</strong> Post-adjustment deviation &lt; 3mm
  </p>
  <div class="directive-card__dof">Expected closure: 14.2mm → 2.1mm</div>
</div>

---

## Verification Loop

After applying directives, the system runs a verification pass:

<div class="verification-panel">
  <div class="verification-panel__header">Verification Result</div>
  <div class="verification-panel__body">
    <div class="verification-panel__result">
      <span class="chip chip--ok">PASS</span>
      <span>Post-adjustment RMS: <code>1.8mm</code> (tolerance: 3mm)</span>
    </div>
  </div>
</div>

<div class="steps">
  <div class="step">
    <span class="step__number">1</span>
    <div class="step__content">
      <div class="step__title">Simulate Apply</div>
      <div class="step__description">Preview correction in 3D viewer before physical adjustment.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">2</span>
    <div class="step__content">
      <div class="step__title">Execute Directive</div>
      <div class="step__description">Field team applies correction per directive card.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">3</span>
    <div class="step__content">
      <div class="step__title">Re-scan & Verify</div>
      <div class="step__description">New as-built data confirms closure. System marks PASS or FAIL.</div>
    </div>
  </div>
</div>

---

## Artifacts

<div class="artifact-bar">
  <a href="/demo/" class="artifact-link">Live Demo</a>
  <a href="https://github.com/barnes-ngb/directive-engine" class="artifact-link">Repository</a>
</div>

---

## Limits + Next Steps

<div class="callout callout--info">
  <span class="callout__icon">📋</span>
  <div class="callout__content">
    <div class="callout__title">Current Limits</div>
    <ul style="margin-bottom:0">
      <li>Single-part directives (no multi-part dependency chains yet)</li>
      <li>Manual anchor pairing (auto-matching in progress)</li>
      <li>Browser-only (no native mobile app)</li>
    </ul>
  </div>
</div>

**Roadmap:**
- Step ordering / dependencies (anchors → part → verification)
- Confidence scoring + `NEEDS_REVIEW` flags for marginal cases
- Tolerance heatmaps / clustering visualization
- Optional: AR overlay as a *skin*, not the core logic
