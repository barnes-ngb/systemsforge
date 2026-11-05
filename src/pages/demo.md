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

## Take the panel apart

The same engine, live, on one panel. Set the deviation with the three sliders; the directive, residual and verdict print from what <code>generateDirectives()</code> returns. Left alone it tours the five beats below; any click hands you control.

<figure class="figure" style="padding: 0; overflow: hidden">
  <iframe src="https://directive-engine.vercel.app/panel.html" title="Directive Engine panel teardown: one facade panel driven live by the engine" loading="lazy" style="display: block; width: 100%; aspect-ratio: 16 / 9; border: 0; background: #ecedef"></iframe>
  <figcaption class="figure__caption" style="padding: var(--space-2) var(--space-4) var(--space-3)">fig 01 · panel p-05 of toy_facade_v1, live · <a href="https://directive-engine.vercel.app/panel.html" target="_blank" rel="noopener">open full size →</a></figcaption>
</figure>

<div class="reading-grid">
  <div class="reading-card">
    <div class="reading__label">deviation · before</div>
    <div class="reading__row"><span class="reading__value reading__value--small reading__value--fail">6.6</span><span class="reading__unit">mm</span></div>
    <div class="reading__note">p-05 · +6.5 / −1.0 mm · 3° about p3</div>
  </div>
  <div class="reading-card">
    <div class="reading__label">residual · expected after</div>
    <div class="reading__row"><span class="reading__value reading__value--small reading__value--pass">0.0</span><span class="reading__unit">mm</span></div>
    <div class="reading__note">tol ±2.0 · limit 10 → blocked</div>
  </div>
  <div class="reading-card">
    <div class="reading__label">verdict</div>
    <div class="verdict-row"><span class="verdict verdict--lit">pass</span><span class="verdict">no</span><span class="verdict">blocked</span></div>
    <div class="reading__note">from expected_directives.json</div>
  </div>
</div>

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
      <div class="step__description">Camera returns to the wide shot. Before/after metric closes the loop: 6.6 mm before, 0.0 mm expected after, against ±2.0; <span class="chip chip--ok">PASS</span> chip lights.</div>
    </div>
  </div>
</div>

---

## Artifacts & Resources

<div class="artifact-bar">
  <a href="https://directive-engine.vercel.app/" class="artifact-link" target="_blank" rel="noopener">Live Demo</a>
  <a href="https://directive-engine.vercel.app/panel.html" class="artifact-link" target="_blank" rel="noopener">Panel teardown</a>
  <a href="https://github.com/barnes-ngb/directive-engine" class="artifact-link" target="_blank" rel="noopener">Repository</a>
  <a href="/work/directive-engine/" class="artifact-link">Full Case Study →</a>
</div>
