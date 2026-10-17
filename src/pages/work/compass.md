---
layout: ../../layouts/BaseLayout.astro
title: "compass"
description: "A pull-default, glance-paced AI coach for smart glasses, built mock-first on a laptop. The project where the instruments get built alongside the thing."
---

<div class="title-block">
  <div class="title-block__id">work / instrument 05 · rev 1</div>
  <span class="status-chip status-chip--pending">in development</span>
</div>

<div class="page-header">
  <h1 class="page-header__title">compass</h1>
  <p class="page-header__subtitle">A pull-default, glance-paced AI coach for smart glasses. Three modes, one backend, built on a laptop mock before any hardware arrived. This page is the living record of the instruments built alongside it.</p>
</div>

<div class="metadata-strip">
  <span><span class="metadata-strip__label">started </span>2026</span>
  <span><span class="metadata-strip__label">stack </span>python · claude · faster-whisper · sqlite</span>
  <span><span class="metadata-strip__label">hardware </span>brilliant labs halo, ordered</span>
  <span><span class="metadata-strip__label">stage </span>phase 2</span>
</div>

<p><a href="https://github.com/barnes-ngb/compass" target="_blank" rel="noopener">Repository</a> · <a href="https://github.com/barnes-ngb/compass/blob/main/docs/roadmap.md" target="_blank" rel="noopener">Roadmap</a> · <a href="https://github.com/barnes-ngb/compass/tree/main/docs/decisions" target="_blank" rel="noopener">Decision log</a> · <a href="/work/compass/graph.json">graph.json</a></p>

<div class="section-header">
  <div class="section-header__index">01 · problem</div>
  <h2>Problem</h2>
</div>

The thesis sentence in the repo reads: *understand my world better, don't miss things, get insight from the wealth of knowledge plus me.* The last two words carry the design. The model holds breadth. The person holds the problem and the check.

Most smart-glasses products get this backwards. They listen all day, speak uninvited, and spend a week's worth of attention in an afternoon. compass is built on the opposite premise: it speaks when invoked, it remembers across sessions, it never records continuously, and it never surveils anyone but the wearer's own working memory.

The harder problem underneath is the one this page exists for. Building the pipeline is cheap now. Knowing whether a given piece of it is right is the work, and it has to be done in domains where the usual geometry instruments don't apply: speech recognition, vision model answers, a HUD a person has to read in a glance.

<div class="section-header">
  <div class="section-header__index">02 · signal</div>
  <h2>Signal</h2>
</div>

Retro mode came up on the laptop in June. Press a key, the last five minutes of the mic buffer go through a local Whisper model, the transcript goes to the coach, a directive lands on the simulated HUD. It worked on the first try, which is the moment this project is about.

The STT model was `base.en`, chosen because it was fast. Said aloud at one desk, "facade panels" came back as "sign tables." That was caught by ear, on one machine, in one session. The fix was a bigger model, `small.en`, and the fix was right. But the check that found the error was a person listening once, and that check does not run again. The next model swap, or the next shop vocabulary, gets no verdict unless somebody happens to be listening.

That is the skip in the figure below. The pipeline went from candidate to "looks right" with no reference in between. The reference is a phrase set: the vocabulary the coach has to hear correctly, recorded once, scored against every model. It is on the instruments list and not yet built.

<div class="section-header">
  <div class="section-header__index">03 · calibration</div>
  <h2>Calibration: what an instrument is here</h2>
</div>

<figure class="figure">
  <svg viewBox="0 0 940 332" role="img" aria-label="An instrument takes a candidate and a reference the candidate's author did not produce, compares them, reads a residual against a threshold, and returns a verdict that can be no." xmlns="http://www.w3.org/2000/svg" font-family="var(--font-mono)">
  <defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="currentColor"/></marker></defs>
  <rect x="232" y="48" width="408" height="172" rx="6" fill="none" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="248" y="68" font-size="11" text-anchor="start" fill="var(--accent)" font-weight="500">instrument</text>
  <rect x="48" y="68" width="120" height="40" rx="3" fill="none" stroke="currentColor" stroke-width="1"/><text x="108" y="92" font-size="13" text-anchor="middle" fill="currentColor" font-weight="400">candidate</text>
  <rect x="48" y="140" width="120" height="40" rx="3" fill="none" stroke="currentColor" stroke-width="1"/><text x="108" y="164" font-size="13" text-anchor="middle" fill="currentColor" font-weight="400">reference</text>
  <rect x="48" y="228" width="120" height="40" rx="3" fill="none" stroke="currentColor" stroke-width="1"/><text x="108" y="252" font-size="13" text-anchor="middle" fill="currentColor" font-weight="400">knowledge</text>
  <line x1="108" y1="226" x2="108" y2="182" stroke="currentColor" stroke-width="1" marker-end="url(#a)"/>
  <text x="116" y="200" font-size="10" text-anchor="start" fill="var(--ink-tertiary)" font-weight="400">supplies</text>
  <rect x="272" y="104" width="120" height="40" rx="3" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="332.0" y="128" font-size="13" text-anchor="middle" fill="currentColor" font-weight="400">compare</text>
  <line x1="170" y1="88" x2="270" y2="116" stroke="currentColor" stroke-width="1" marker-end="url(#a)"/>
  <line x1="170" y1="160" x2="270" y2="132" stroke="currentColor" stroke-width="1" marker-end="url(#a)"/>
  <text x="428" y="92" font-size="11" text-anchor="start" fill="var(--ink-tertiary)" font-weight="400">residual</text>
  <line x1="394" y1="124.0" x2="418" y2="132" stroke="currentColor" stroke-width="1" marker-end="url(#a)"/>
  <line x1="428" y1="132" x2="628" y2="132" stroke="currentColor" stroke-width="1"/>
  <line x1="428" y1="132" x2="428" y2="124" stroke="currentColor" stroke-width="1"/>
  <line x1="448" y1="132" x2="448" y2="128" stroke="currentColor" stroke-width="1"/>
  <line x1="468" y1="132" x2="468" y2="128" stroke="currentColor" stroke-width="1"/>
  <line x1="488" y1="132" x2="488" y2="128" stroke="currentColor" stroke-width="1"/>
  <line x1="508" y1="132" x2="508" y2="128" stroke="currentColor" stroke-width="1"/>
  <line x1="528" y1="132" x2="528" y2="124" stroke="currentColor" stroke-width="1"/>
  <line x1="548" y1="132" x2="548" y2="128" stroke="currentColor" stroke-width="1"/>
  <line x1="568" y1="132" x2="568" y2="128" stroke="currentColor" stroke-width="1"/>
  <line x1="588" y1="132" x2="588" y2="128" stroke="currentColor" stroke-width="1"/>
  <line x1="608" y1="132" x2="608" y2="128" stroke="currentColor" stroke-width="1"/>
  <line x1="628" y1="132" x2="628" y2="124" stroke="currentColor" stroke-width="1"/>
  <text x="428" y="148" font-size="10" text-anchor="middle" fill="currentColor" font-weight="400">0</text>
  <text x="628" y="148" font-size="10" text-anchor="middle" fill="currentColor" font-weight="400">1.0</text>
  <line x1="528.0" y1="126" x2="528.0" y2="172" stroke="currentColor" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="528.0" y="186" font-size="10" text-anchor="middle" fill="var(--ink-tertiary)" font-weight="400">threshold 0.50 mm</text>
  <circle cx="552.0" cy="132" r="4" fill="var(--accent)"/>
  <text x="552.0" y="118" font-size="11" text-anchor="middle" fill="currentColor" font-weight="500">0.62 mm</text>
  <text x="672" y="108" font-size="11" text-anchor="start" fill="var(--ink-tertiary)" font-weight="400">verdict</text>
  <rect x="672" y="120" width="44" height="24" rx="3" fill="none" stroke="var(--ink-tertiary)" stroke-width="1"/>
  <text x="694.0" y="136" font-size="11" text-anchor="middle" fill="var(--ink-tertiary)" font-weight="400">pass</text>
  <rect x="724" y="120" width="30" height="24" rx="3" fill="none" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="739.0" y="136" font-size="11" text-anchor="middle" fill="currentColor" font-weight="500">no</text>
  <rect x="762" y="120" width="79" height="24" rx="3" fill="none" stroke="var(--ink-tertiary)" stroke-width="1"/>
  <text x="801.5" y="136" font-size="11" text-anchor="middle" fill="var(--ink-tertiary)" font-weight="400">ill-posed</text>
  <rect x="849" y="120" width="65" height="24" rx="3" fill="none" stroke="var(--ink-tertiary)" stroke-width="1"/>
  <text x="881.5" y="136" font-size="11" text-anchor="middle" fill="var(--ink-tertiary)" font-weight="400">blocked</text>
  <line x1="632" y1="132" x2="668" y2="132" stroke="currentColor" stroke-width="1" marker-end="url(#a)"/>
  <path d="M108,66 C108,6 702,6 702,94" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="4 4" marker-end="url(#a)"/>
  <text x="436.0" y="18" font-size="10" text-anchor="middle" fill="var(--ink-tertiary)" font-weight="400">the skip: "looks right", no reference, no residual</text>
  <line x1="592" y1="220" x2="592" y2="300" stroke="currentColor" stroke-width="1"/>
  <line x1="592" y1="300" x2="108" y2="300" stroke="currentColor" stroke-width="1"/>
  <line x1="108" y1="300" x2="108" y2="270" stroke="currentColor" stroke-width="1" marker-end="url(#a)"/>
  <text x="350.0" y="316" font-size="10" text-anchor="middle" fill="var(--ink-tertiary)" font-weight="400">returns, reusable</text>
  </svg>
  <figcaption class="figure__caption">fig 01 · an instrument: a candidate against a reference the author did not make, a residual against a threshold set beforehand, a verdict that can be no</figcaption>
</figure>

Every instrument on this project has the same shape, whatever the domain. A candidate (a transcript, a vision answer, a driver) goes against a reference that neither the author nor the model produced. A comparator turns the pair into a residual, a number rather than an impression. A threshold, set before the run, turns the residual into a verdict. The verdict can be `no`.

The dashed edge is the alternative: candidate straight to verdict on the strength of looking right. It is the fast path and the one that costs understanding, because nothing from it comes back. The solid return edge is why instruments are worth building: an instrument outlives the candidate it was built for, and running it again is free.

The structure in the figure is also published as data at <a href="/work/compass/graph.json">graph.json</a>, with notes the drawing leaves out. The SVG is rendered from that file. Change the file and both faces change.

<div class="section-header">
  <div class="section-header__index">04 · constraints</div>
  <h2>Constraints</h2>
</div>

<div class="artifact-card">
  <div class="artifact-card__header">
    <span class="artifact-card__id">compass · constraints</span>
  </div>
  <div><span class="artifact-card__field-label">trigger </span>pull-default: tap, voice, or button. Never ambient</div>
  <div><span class="artifact-card__field-label">recording </span>rolling buffer in RAM only, never persisted. Transcripts persist; audio does not</div>
  <div><span class="artifact-card__field-label">hardware </span>abstracted behind a <code>Glasses</code> protocol. Mock first; a real device is one more driver</div>
  <div><span class="artifact-card__field-label">host </span>windows laptop, per-user venv, no admin, no docker</div>
  <div><span class="artifact-card__field-label">latency </span>a glance. Visual and verbal in seconds; retro in the time it takes to transcribe five minutes locally</div>
</div>

The hardware constraint is the one that shaped the build order. The Halo was ordered in May and has not arrived. Rather than wait, the three modes were built against a laptop mock (webcam, mic, a window standing in for the HUD) and the roadmap was restructured in June to match: software modes complete on the laptop first, the hardware wire-in last. Two of three modes run today on no glasses at all.

<div class="section-header">
  <div class="section-header__index">05 · action</div>
  <h2>Action: three modes, one backend</h2>
</div>

<div class="artifact-card">
  <div class="artifact-card__header">
    <span class="artifact-card__id">mode · visual</span>
    <span class="status-chip status-chip--deployed">runs on mock</span>
  </div>
  <div><span class="artifact-card__field-label">trigger </span>tap</div>
  <div><span class="artifact-card__field-label">input  </span>one camera frame</div>
  <div><span class="artifact-card__field-label">ask    </span>"what is this?" or "does this match the drawing?"</div>
  <div><span class="artifact-card__field-label">output </span>a directive on the HUD</div>
</div>

<div class="artifact-card">
  <div class="artifact-card__header">
    <span class="artifact-card__id">mode · verbal</span>
    <span class="status-chip status-chip--deployed">runs on mock</span>
  </div>
  <div><span class="artifact-card__field-label">trigger </span>key, then speak</div>
  <div><span class="artifact-card__field-label">input  </span>a fixed capture window, plus the preceding two minutes of buffer as context</div>
  <div><span class="artifact-card__field-label">output </span>a directive on the HUD</div>
</div>

<div class="artifact-card">
  <div class="artifact-card__header">
    <span class="artifact-card__id">mode · retro</span>
    <span class="status-chip status-chip--deployed">runs on mock</span>
  </div>
  <div><span class="artifact-card__field-label">trigger </span>key</div>
  <div><span class="artifact-card__field-label">input  </span>the last five minutes of the rolling buffer, transcribed locally</div>
  <div><span class="artifact-card__field-label">ask    </span>"what did they just ask?", "what did we decide?"</div>
  <div><span class="artifact-card__field-label">output </span>a directive on the HUD</div>
</div>

All three feed a layered memory store: rolling buffer, session transcript, session summary, daily digest, project memory. The same question can be asked about five minutes ago or five months ago. The rollup layers past the transcript are scaffolded, not finished.

<div class="section-header">
  <div class="section-header__index">06 · verification</div>
  <h2>Instruments</h2>
</div>

This is the list the page exists to keep. Each entry says what the instrument can say no to. Entries get added as they are built; none get removed.

<div class="artifact-card">
  <div class="artifact-card__header">
    <span class="artifact-card__id">instrument · smoke suite</span>
    <span class="status-chip status-chip--deployed">running</span>
  </div>
  <div><span class="artifact-card__field-label">reference </span>the protocols each provider must satisfy, mock inputs with known outputs</div>
  <div><span class="artifact-card__field-label">says no to </span>a wire-up change that breaks a mode without anyone running it</div>
  <div><span class="artifact-card__field-label">reading  </span>23 passed, 1 skipped (no audio device on the test host), pre-hardware baseline</div>
</div>

<div class="artifact-card">
  <div class="artifact-card__header">
    <span class="artifact-card__id">instrument · protocol check</span>
    <span class="status-chip status-chip--deployed">running</span>
  </div>
  <div><span class="artifact-card__field-label">reference </span><code>typing.Protocol</code> contracts for glasses, vision, coach, audio, marked <code>runtime_checkable</code></div>
  <div><span class="artifact-card__field-label">says no to </span>a new hardware driver that claims the interface and does not implement it</div>
</div>

<div class="artifact-card">
  <div class="artifact-card__header">
    <span class="artifact-card__id">instrument · stt phrase set</span>
    <span class="status-chip status-chip--pending">not built</span>
  </div>
  <div><span class="artifact-card__field-label">reference </span>a recorded set of shop and site phrases ("facade panels", part names, tolerances) with known transcripts</div>
  <div><span class="artifact-card__field-label">residual </span>word error rate on the set, per model</div>
  <div><span class="artifact-card__field-label">says no to </span>a faster STT model that cannot hear the vocabulary. The check that was done by ear, made repeatable</div>
</div>

<div class="artifact-card">
  <div class="artifact-card__header">
    <span class="artifact-card__id">instrument · halo wire-in measurements</span>
    <span class="status-chip status-chip--pending">waiting on hardware</span>
  </div>
  <div><span class="artifact-card__field-label">reference </span>the firmware protocol as inspected, pinned to a commit</div>
  <div><span class="artifact-card__field-label">residual </span>capture-to-host latency for a 640 px JPEG over BLE; tap reliability while worn; characters per HUD line at each font size</div>
  <div><span class="artifact-card__field-label">says no to </span>a driver that works in the SDK example and fails in the glance budget. Nothing here is measured yet; the playbook lists what to measure first</div>
</div>

<div class="section-header">
  <div class="section-header__index">07 · artifacts</div>
  <h2>Artifacts</h2>
</div>

<div class="artifact-bar">
  <a href="https://github.com/barnes-ngb/compass" class="artifact-link" target="_blank" rel="noopener">Repository →</a>
  <a href="https://github.com/barnes-ngb/compass/blob/main/docs/halo-wireup.md" class="artifact-link" target="_blank" rel="noopener">Halo wire-in playbook →</a>
  <a href="https://github.com/barnes-ngb/compass/blob/main/docs/landscape.md" class="artifact-link" target="_blank" rel="noopener">Hardware landscape →</a>
  <a href="/work/compass/graph.json" class="artifact-link">graph.json →</a>
</div>

Hardware: <a href="https://brilliant.xyz/products/halo" target="_blank" rel="noopener">Brilliant Labs Halo</a>, with the SDK and firmware at <a href="https://docs.brilliant.xyz/" target="_blank" rel="noopener">docs.brilliant.xyz</a> and <a href="https://github.com/brilliantlabsAR/halo-firmware" target="_blank" rel="noopener">github.com/brilliantlabsAR/halo-firmware</a>. What the repo's own inspection of that firmware established: a single-eye color microOLED, a camera that returns complete JPEG bytes at 640 px to a Lua app on the device, which relays them to the host over Bluetooth. A photograph of the device on this page will be one I took, once it is on the desk.

### Where it sits

compass is the glance-paced member of the same family as <a href="/work/directive-engine/">Directive Engine</a>. Same pattern, capture to reconcile to directive to log, at a different rhythm of attention: seconds to minutes during an install, milliseconds to seconds in a glance. It is also the first instrument here pointed at the person rather than the panel.

<aside class="limits-callout">
  <div class="limits-callout__label">limits</div>
  <ul>
    <li>No hardware yet. Every mode runs on a laptop mock; the Halo driver and its Lua app are pre-hardware sketches that have never executed</li>
    <li>The STT phrase set, the instrument this page is named for, is not built. The model choice rests on one listening session</li>
    <li>Memory rollups past the session transcript are scaffolded, not implemented</li>
    <li>Visual-mode answers from the vision model have no reference set; "does this match the drawing?" has not been scored against a known drawing</li>
    <li>Single wearer, single host, English only</li>
  </ul>
</aside>
