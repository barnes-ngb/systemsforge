---
layout: ../../layouts/BaseLayout.astro
title: "Directive Engine"
description: "Pixels to atoms — a directive engine that bridges detection and execution for field teams, with installer-language directives and pass/fail verification."
---

<div class="instrument-hero">
  <div class="instrument-hero__status">
    <span class="chip chip--ok">DEMO LIVE</span>
    <span class="chip">PIXELS TO ATOMS</span>
    <span class="chip">BROWSER-FIRST</span>
  </div>
  <h1 class="instrument-hero__title">Directive Engine</h1>
  <p class="instrument-hero__subtitle">Pixels to atoms — a directive engine that bridges <strong>detection and execution</strong> for field teams. Deviations in, installer-language directives out, with pass/fail verification of closure.</p>
</div>

<div class="artifact-bar">
  <a href="https://directive-engine.vercel.app/" class="btn btn--primary btn--large" target="_blank" rel="noopener">Open Live Demo</a>
  <a href="https://github.com/barnes-ngb/directive-engine" class="artifact-link" target="_blank" rel="noopener">Repository</a>
  <a href="mailto:barnes.ngb@gmail.com" class="artifact-link">Contact</a>
</div>

<!-- TODO: replace Directive-Engine.png with a v0.2 viewer screenshot after Track B capture. -->
![Directive Engine Screenshot](/images/Directive-Engine.png)

---

## Problem

When something is off in the field, the hardest part is not detecting it — it's expressing the correction in a **field-executable format** that's:

<div class="steps">
  <div class="step">
    <span class="step__number">1</span>
    <div class="step__content">
      <div class="step__title">Unambiguous</div>
      <div class="step__description">A directive an installer can execute with a wrench — <em>"translate +3.2mm along slot S2"</em>, not <em>"translate +3.2mm in part-frame Y."</em></div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">2</span>
    <div class="step__content">
      <div class="step__title">Constrained</div>
      <div class="step__description">Respects what the part is <em>physically allowed</em> to do — named pivots, slots, and indexed bolt patterns, not abstract axes.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">3</span>
    <div class="step__content">
      <div class="step__title">Verifiable</div>
      <div class="step__description">Pass/fail closure check after adjustment — did the residual drop inside tolerance?</div>
    </div>
  </div>
</div>

---

## Inputs (Signal)

<div class="metric-grid">
  <div class="metric-card">
    <span class="metric-card__label">Nominal Model</span>
    <span class="metric-card__value">Design Intent</span>
    <span class="metric-card__unit">3D geometry + named features</span>
  </div>
  <div class="metric-card">
    <span class="metric-card__label">As-Built Scan</span>
    <span class="metric-card__value">Field Reality</span>
    <span class="metric-card__unit">Point cloud or survey data</span>
  </div>
</div>

**Data format:** JSON contracts for as-built poses, constraint metadata (joints, slots, indexed patterns), and directive outputs. Schemas live in the repo; the engine output is identical with or without named features declared — features are pure presentation metadata.

---

## Calibration

The engine operates on a calibrated frame: as-built poses expressed in a shared world coordinate system, with each part's pose represented as `T_world_part` (translation + quaternion). The v0.2 demo runs on the synthetic `toy_facade_v1` fixture — a 12-panel subsection with deviations designed to exercise the contract end-to-end.

<div class="metric-grid">
  <div class="metric-card">
    <span class="metric-card__label">Worst Deviation</span>
    <span class="metric-card__value">~8<span class="metric-card__unit">mm</span></span>
    <div class="metric-card__status">
      <span class="chip chip--pending">BEFORE</span>
    </div>
  </div>
  <div class="metric-card">
    <span class="metric-card__label">After Apply</span>
    <span class="metric-card__value">&lt;1<span class="metric-card__unit">mm</span></span>
    <div class="metric-card__status">
      <span class="chip chip--ok">PASS</span> within tolerance
    </div>
  </div>
</div>

<div class="callout callout--info">
  <span class="callout__icon">📐</span>
  <div class="callout__content">
    <div class="callout__title">Synthetic fixture, real engine</div>
    The geometry and deviations are designed to exercise the contract; the engine math (DOF projection, indexed rotation quantization, status logic) is real and unit-tested. Same primitives generalize to larger installs.
  </div>
</div>

---

## Constraints / DOF

Each part declares its kinematic features — the things an installer can actually adjust. The engine projects raw deviations onto these features, so corrections come out in the vocabulary of the hardware, not abstract axes.

<div class="directive-card">
  <h4 class="directive-card__title">Example: Panel P-05</h4>
  <div class="directive-card__constraints">
    <span class="chip">J1 PIVOT</span>
    <span class="chip">S2 SLOT (±10mm)</span>
    <span class="chip">P3 INDEX (4-position)</span>
  </div>
  <p class="directive-card__action">Allowed motion: pivot about joint J1, slide along lateral mounting slot S2, and rotate to one of four discrete index positions on bolt pattern P3. Everything else is held by the structure.</p>
  <div class="directive-card__dof">Corrections that don't fit are <code>clamped</code> or <code>blocked</code> — never silently rounded.</div>
</div>

---

## Action Format (Directive Card)

The engine emits **directive cards** — structured correction instructions in installer language:

<div class="directive-card">
  <div class="directive-card__header">
    <h4 class="directive-card__title">DIRECTIVE: P-05</h4>
    <span class="chip chip--pending">PENDING</span>
  </div>
  <div class="directive-card__constraints">
    <span class="chip">TRANSLATE</span>
    <span class="chip">INDEX</span>
  </div>
  <p class="directive-card__action">
    <strong>Action:</strong> Translate −6.5mm along slot S2 (lateral mounting slot, ±10mm). Rotate to index 0 on P3 (four-position bolt pattern about vertical axis).<br>
    <strong>Frame:</strong> Part-local, features declared in <code>constraints.json</code>.<br>
    <strong>Tolerance:</strong> ±2.0mm translation, ±1.0° rotation.<br>
    <strong>Verify:</strong> before/after deviation metric, <code>pass</code> chip when within tolerance.
  </p>
  <div class="directive-card__dof">Status: <code>pending</code> → <code>ok</code> after apply</div>
</div>

The mapping from engine math to physical features happens in `src/presentation/format-directive.ts`; the engine stays generic, the language stays installer-facing.

---

## Verification Loop

The live demo walks through the loop in five beats — detection, constraint, directive, apply, verify — on the synthetic `toy_facade_v1` fixture. Try it on desktop or mobile:

<div class="artifact-bar">
  <a href="https://directive-engine.vercel.app/" class="btn btn--primary" target="_blank" rel="noopener">Open Live Demo</a>
  <a href="/demo/" class="artifact-link">Demo Walkthrough →</a>
</div>

<div class="verification-panel">
  <div class="verification-panel__header">Verification Result</div>
  <div class="verification-panel__body">
    <div class="verification-panel__result">
      <span class="chip chip--ok">PASS</span>
      <span>Before: <code>~8mm</code> → After: <code>&lt;1mm</code> (tolerance: ±2.0mm)</span>
    </div>
  </div>
</div>

<div class="steps">
  <div class="step">
    <span class="step__number">1</span>
    <div class="step__content">
      <div class="step__title">Detection</div>
      <div class="step__description">As-built scene loads. Panels glow yellow or red where deviation exceeds tolerance.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">2</span>
    <div class="step__content">
      <div class="step__title">Constraint</div>
      <div class="step__description">Camera dollies to the worst panel. Allowed DOF surface as named features.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">3</span>
    <div class="step__content">
      <div class="step__title">Directive</div>
      <div class="step__description">Engine emits the correction as an installer-language card.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">4</span>
    <div class="step__content">
      <div class="step__title">Apply (simulated)</div>
      <div class="step__description">Panel animates to corrected pose. Status flips <code>pending → ok</code>.</div>
    </div>
  </div>
  <div class="step">
    <span class="step__number">5</span>
    <div class="step__content">
      <div class="step__title">Verify</div>
      <div class="step__description">Camera returns to the wide shot. Before/after metric closes the loop.</div>
    </div>
  </div>
</div>

---

## Artifacts

<div class="artifact-bar">
  <a href="https://directive-engine.vercel.app/" class="artifact-link" target="_blank" rel="noopener">Live Demo</a>
  <a href="https://github.com/barnes-ngb/directive-engine" class="artifact-link" target="_blank" rel="noopener">Repository</a>
  <a href="/demo/" class="artifact-link">Demo Walkthrough →</a>
</div>

<!-- TODO: add 60-90s demo video link once Track B capture lands. -->

---

## Limits + Next Steps

<div class="callout callout--info">
  <span class="callout__icon">📋</span>
  <div class="callout__content">
    <div class="callout__title">Current Limits</div>
    <ul style="margin-bottom:0">
      <li>Synthetic fixture (<code>toy_facade_v1</code>) — real scan-data ingestion not yet wired in</li>
      <li>Single-part directives per beat (no multi-part dependency chains yet)</li>
      <li>Browser-only viewer (no native mobile app)</li>
      <li>Prototype: engine math is unit-tested, but the end-to-end loop hasn't been run against a field deployment</li>
    </ul>
  </div>
</div>

**Why this generalizes.** The primitives — pose as `T_world_part` with a quaternion, DOF projection onto declared kinematic features, indexed-rotation quantization, tolerance clamping, before/after verification — are domain-agnostic. The directive engine is the *generation* half of the loop (deviation → instruction). For the *capture* half (as-built reality → deviation) in an aerospace-flavored deployment, see <a href="https://www.azahner.com/labs/surveylink/" target="_blank" rel="noopener external">SurveyLink ↗</a>, a real-time link between as-designed models and as-built field data.

**Roadmap:**
- Real scan-data ingestion on top of the existing contract
- Step ordering / dependencies (anchors → part → verification)
- Confidence scoring with `needs_review` flags surfaced in the UI
- Tolerance heatmaps to spot systemic drift across a facade
- AR overlay as an output target — not the core product
