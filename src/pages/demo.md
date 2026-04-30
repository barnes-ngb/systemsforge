---
layout: ../layouts/BaseLayout.astro
title: "Demo"
description: "Try the Directive Engine live demo — 60-second click-path to see calibration, directive generation, and verification in action."
---

<div class="instrument-hero">
  <div class="instrument-hero__status">
    <span class="chip chip--ok">LIVE</span>
    <span class="chip">BROWSER-FIRST</span>
    <span class="chip">NO INSTALL</span>
  </div>
  <h1 class="instrument-hero__title">Directive Engine Demo</h1>
  <p class="instrument-hero__subtitle">See calibration, directive generation, and verification in action. Works on desktop and mobile.</p>
</div>

<div style="text-align: center; margin: 2rem 0;">
  <a href="https://directive-engine.vercel.app/" class="btn btn--primary btn--large" target="_blank" rel="noopener">
    Open Live Demo →
  </a>
</div>

<div class="callout callout--info">
  <span class="callout__icon">⏱</span>
  <div class="callout__content">
    <strong>Time to first directive:</strong> ~60 seconds. Follow the click-path below.
  </div>
</div>

---

## 60-Second Click-Path

Follow these steps to generate your first directive:

<div class="steps">
  <div class="step">
    <span class="step__number">1</span>
    <div class="step__content">
      <div class="step__title">Load Sample Dataset</div>
      <div class="step__description">Click <strong>"Load Sample"</strong> in the top toolbar. This loads a pre-paired nominal + as-built dataset with 12 parts.</div>
      <div class="step__status"><span class="chip chip--pending">~5s</span></div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">2</span>
    <div class="step__content">
      <div class="step__title">Check Calibration Panel</div>
      <div class="step__description">Look at the <strong>Calibration</strong> panel on the left. Verify <code>RMS &lt; 5mm</code> and no outliers flagged. Green = good alignment.</div>
      <div class="step__status"><span class="chip chip--pending">~10s</span></div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">3</span>
    <div class="step__content">
      <div class="step__title">Select a Part</div>
      <div class="step__description">Click any part in the 3D view (or select from the part list). The part highlights and its deviation vector appears.</div>
      <div class="step__status"><span class="chip chip--pending">~10s</span></div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">4</span>
    <div class="step__content">
      <div class="step__title">Generate Directive</div>
      <div class="step__description">Click <strong>"Generate Directive"</strong>. A directive card appears with action (translate/rotate), frame, and expected closure.</div>
      <div class="step__status"><span class="chip chip--pending">~15s</span></div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">5</span>
    <div class="step__content">
      <div class="step__title">Simulate Apply</div>
      <div class="step__description">Click <strong>"Simulate"</strong> to preview the correction. The 3D view updates to show the adjusted position.</div>
      <div class="step__status"><span class="chip chip--pending">~10s</span></div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">6</span>
    <div class="step__content">
      <div class="step__title">Verify Result</div>
      <div class="step__description">Check the verification panel: <span class="chip chip--ok">PASS</span> if post-adjustment deviation is within tolerance.</div>
      <div class="step__status"><span class="chip chip--ok">DONE</span></div>
    </div>
  </div>
</div>

---

## Field Test Protocol

For evaluating the demo in a realistic workflow (phone + printed sheet):

<div class="callout callout--info">
  <span class="callout__icon">📱</span>
  <div class="callout__content">
    <div class="callout__title">Mobile-First Test</div>
    <p style="margin-bottom: 0.5rem;">The demo is designed to work on phones. Test it as a field installer would:</p>
  </div>
</div>

<div class="steps">
  <div class="step">
    <span class="step__number">1</span>
    <div class="step__content">
      <div class="step__title">Open on Phone</div>
      <div class="step__description">Navigate to the demo URL on your phone. Rotate to landscape for best 3D view.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">2</span>
    <div class="step__content">
      <div class="step__title">Print Directive Card</div>
      <div class="step__description">Generate a directive, then tap <strong>"Export PDF"</strong>. Print or save for field reference.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">3</span>
    <div class="step__content">
      <div class="step__title">Simulate Field Workflow</div>
      <div class="step__description">With printed sheet in hand, walk through: read directive → simulate apply on phone → mark complete.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">4</span>
    <div class="step__content">
      <div class="step__title">Test Verification</div>
      <div class="step__description">Use the "Re-scan" function (simulated) to see how verification confirms closure.</div>
    </div>
  </div>
</div>

**Evaluation criteria:**
- Can you understand the directive in <10 seconds?
- Is the reference frame clear (part-local vs. site grid)?
- Does the PASS/FAIL result match your expectation?

---

## Calibration Requirements

<div class="callout callout--warning">
  <span class="callout__icon">⚠</span>
  <div class="callout__content">
    <div class="callout__title">Calibration Warning</div>
    <p>If <code>RMS &gt; 5mm</code>, re-check anchor pairing before trusting directive outputs.</p>
    <p style="margin-bottom:0"><strong>Common causes:</strong> Misidentified anchor points, coordinate system mismatch, or scan registration error.</p>
  </div>
</div>

<div class="metric-grid">
  <div class="metric-card">
    <span class="metric-card__label">Target RMS</span>
    <span class="metric-card__value">&lt; 5<span class="metric-card__unit">mm</span></span>
    <div class="metric-card__status">
      <span class="chip chip--ok">ACCEPTABLE</span>
    </div>
  </div>
  <div class="metric-card">
    <span class="metric-card__label">Max Outlier</span>
    <span class="metric-card__value">&lt; 10<span class="metric-card__unit">mm</span></span>
    <div class="metric-card__status">
      <span class="chip chip--clamped">FLAG IF EXCEEDED</span>
    </div>
  </div>
</div>

---

## Artifacts & Resources

<div class="artifact-bar">
  <a href="https://directive-engine.vercel.app/" class="artifact-link" target="_blank">Live Demo</a>
  <a href="https://github.com/barnes-ngb/directive-engine" class="artifact-link" target="_blank">Repository</a>
  <a href="/work/directive-engine/" class="artifact-link">Full Case Study →</a>
</div>

---

## Questions or Feedback?

Testing this for your VDC, reality capture, or field installation workflow?

<div class="artifact-bar">
  <a href="mailto:barnes.ngb@gmail.com" class="btn btn--secondary">barnes.ngb@gmail.com</a>
  <a href="https://www.linkedin.com/in/barnesngb/" class="artifact-link">LinkedIn</a>
</div>

<div class="callout callout--info">
  <span class="callout__icon">💬</span>
  <div class="callout__content">
    I'm especially interested in feedback from teams doing:
    <ul style="margin-bottom:0">
      <li>Facade installation with tight tolerances</li>
      <li>MEP coordination with scan-to-BIM workflows</li>
      <li>Prefab assembly with field verification</li>
    </ul>
  </div>
</div>
