---
layout: ../layouts/BaseLayout.astro
title: "Demo"
description: "Directive Engine demo — a 5-beat guided walkthrough bridging detection and execution on a synthetic facade fixture. Works on desktop and mobile."
---

<div class="instrument-hero">
  <div class="instrument-hero__status">
    <span class="chip chip--ok">LIVE</span>
    <span class="chip">BROWSER-FIRST</span>
    <span class="chip">5-BEAT</span>
  </div>
  <h1 class="instrument-hero__title">Directive Engine Demo</h1>
  <p class="instrument-hero__subtitle">A 5-beat guided walkthrough of how the directive engine bridges <strong>detection and execution</strong> on a synthetic facade fixture. Works on desktop and mobile.</p>
</div>

<div style="text-align: center; margin: 2rem 0;">
  <a href="https://directive-engine.vercel.app/" class="btn btn--primary btn--large" target="_blank" rel="noopener">
    Open Live Demo →
  </a>
</div>

<!-- TODO: embed 60-90s demo video here once Track B capture lands. -->

---

## The 5-beat walkthrough

<div class="steps">
  <div class="step">
    <span class="step__number">1</span>
    <div class="step__content">
      <div class="step__title">Detection</div>
      <div class="step__description">Reality doesn't match the model. The as-built scene loads; panels glow yellow or red where deviation exceeds tolerance.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">2</span>
    <div class="step__content">
      <div class="step__title">Constraint</div>
      <div class="step__description">What motion is allowed. Camera dollies to the worst panel; its named features (pivots, slots, indexed bolt patterns) surface as the only legal axes for correction.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">3</span>
    <div class="step__content">
      <div class="step__title">Directive</div>
      <div class="step__description">Engine emits an installer-language correction — <em>"Translate −6.5mm along slot S2. Rotate to index 0 on P3."</em> — with status, tolerance band, and deviation magnitude.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">4</span>
    <div class="step__content">
      <div class="step__title">Apply (simulated)</div>
      <div class="step__description">Panel animates to its corrected pose. Status flips <code>pending → ok</code>.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">5</span>
    <div class="step__content">
      <div class="step__title">Verify</div>
      <div class="step__description">Camera returns to the wide shot. Before/after metric closes the loop — residual drops from ~8mm to &lt;1mm; <span class="chip chip--ok">PASS</span> chip lights.</div>
    </div>
  </div>
</div>

---

## Artifacts & Resources

<div class="artifact-bar">
  <a href="https://directive-engine.vercel.app/" class="artifact-link" target="_blank" rel="noopener">Live Demo</a>
  <a href="https://github.com/barnes-ngb/directive-engine" class="artifact-link" target="_blank" rel="noopener">Repository</a>
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
