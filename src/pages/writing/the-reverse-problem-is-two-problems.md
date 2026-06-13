---
layout: ../../layouts/BaseLayout.astro
title: "The reverse problem is two problems"
description: "On finding the boundary, and what it means to develop toward it."
image: "/images/writing/two_boundaries.png"
pubDate: 2026-06-08
---

<div class="title-block">
  <div class="title-block__id">writing / 2026 · 02</div>
</div>

<div class="page-header">
  <h1 class="page-header__title">The reverse problem is two problems</h1>
  <p class="page-header__subtitle">On finding the boundary, and what it means to develop toward it</p>
</div>

<div class="metadata-strip">
  <span><span class="metadata-strip__label">published </span>2026-06-08</span>
  <span><span class="metadata-strip__label">reading </span>6 min</span>
  <span><span class="metadata-strip__label">tags </span>reverse problem, reconstruction, method</span>
</div>

There is a particular satisfaction in discovering that one problem is secretly two. It does not feel like progress at first. It feels like the ground you were standing on splitting. But it is the most useful thing that can happen in a piece of development work, because a problem you can name as two problems is a problem you have finally understood the shape of.

I want to walk through one of these, from a small instrument I built, because the specific case is concrete and the general lesson is the part I keep.

## The problem everyone treats as one

Start with a thing that sounds simple. You have a CAD surface, an analytic description with control points and knots. You turn it into a mesh, hand the mesh to a simulation that pushes on it, and the simulation hands back a deformed mesh. Now you want the CAD surface back, the analytic version, changed where the simulation changed it and unchanged everywhere else.

The forward direction, CAD to mesh, is solved. You run the kernel and tessellate. The reverse direction, the morphed mesh back to an analytic surface that behaves like the part, is not solved, and it is where the interesting work lives. People call it the reverse problem, and they tend to treat it as a single difficulty: reconstruction is hard, get better at reconstruction.

I built a small validated instrument to study the crossing. Nothing exotic. It carries identity and topology across the boundary, so that when the mesh comes back, every point still knows which point it was and which points it was next to. That carried information lets the reconstruction be a determined fit rather than a guess, and it lets you measure how far the result drifted from where it should be. The plan was to show reconstruction working, measure the drift, and call the reverse problem addressed.

<figure class="figure">
  <img src="/images/writing/collision.png" alt="Carried topology defines which closeness is legal. Two neighbors close together is expected and not a defect; two non-neighbors landing coincident is flagged as a self-intersection." />
  <figcaption class="figure__caption">fig 01 · carried topology decides which closeness is legal</figcaption>
</figure>


Then I ran an experiment that was supposed to confirm the story, and it split the ground instead.

## The experiment that split it

The experiment was a ladder. Hold the same surface and the same loop, and remove what you carry across the boundary, one rung at a time. Full information at the top: identity, topology, parameterization. Then estimate the parameterization instead of carrying it. Then strip the correspondence entirely and treat the return as a raw point cloud. Then change the connectivity, a remesh.

The positional drift behaved exactly as the single-problem story predicted. With everything carried, drift was tiny. Estimate the parameterization and it climbed about tenfold. Strip to a point cloud and it became ill-posed, drift the size of the part itself. Change the topology and the gate blocked it. A clean staircase, three orders of magnitude, and the lesson seemed to be the obvious one: carrying identity is worth a great deal, and that is the whole game.

Except one number refused to climb. The curvature deviation, how faithfully the reconstruction held the surface's curvature, was already as bad as it would get at the very top of the ladder, with full information carried. Better parameterization did nothing for it. I had predicted curvature would degrade alongside position, and it simply did not.

That refusal is the whole post.

## What the refusal meant

The curvature would not improve because curvature was never a parameterization problem. It was a problem of the representation itself: the basis, the number of control points, the degrees of freedom available to bend. A coarse basis cannot hold a sharp curvature no matter how perfectly you place the points on it. The leading edge of the surface needed more freedom than the basis had, and carrying identity, which fixes where things go, does nothing about how much freedom there is to go there.

So the reverse problem was two problems wearing one coat.

The first is parameterization recovery. Can you recover where the points belong? This governs positional drift, and carrying identity makes it well-posed. It is the boundary the instrument actually closes.

The second is representation richness. Can your description hold the properties that matter, the curvature the solver feels? This is a function of the basis, not of anything you carry. It is a different knob, and the instrument does not touch it.

<figure class="figure">
  <img src="/images/writing/two_boundaries.png" alt="The reverse problem is two problems. Boundary 1, parameterization recovery, governs positional drift and is the one passthrough closes. Boundary 2, representation richness, governs curvature fidelity and stays open." />
  <figcaption class="figure__caption">fig 02 · the reverse problem, split into two boundaries</figcaption>
</figure>


Two boundaries. One I had addressed and one I had only diagnosed. The honest version of the work was not "reconstruction works." It was "here are the two boundaries, here is the one this addresses, and here is the one that stays open." That is a smaller claim and a truer one, and it is far more useful to anyone who picks the work up, because it tells them which of the two problems they are actually facing.

## Why this is a lesson about development, not just geometry

The geometry is specific. The pattern is not. A great deal of development is exactly this: you hold a difficulty you have been treating as one thing, and the real work is finding the seam where it is two.

It tends to go the same way each time. You have an intuition that names the difficulty, "reconstruction is hard," "the build is slow," "users churn." The intuition is a single coat over what are really independent variables. And the move that unlocks the work is not pushing harder on the single name. It is building the small experiment that lets the variables move independently, and then watching for the one that refuses to move with the others. The refusal is the seam. The thing that does not climb when everything else climbs is the second problem announcing itself.

Two practices fall out of this, and they are the ones I try to hold.

The first is to build the instrument that lets the variables separate. I could have argued about whether curvature was a parameterization problem forever, in a meeting, with a whiteboard. The split only became undeniable because there was a measured ladder where one number moved and the other sat still. Development is largely the construction of the small rigs that let reality answer instead of opinion. The rig is the deliverable even when the result is the thing you remember.

The second is to keep the result that breaks the prediction. I expected curvature to climb with position. It did not. The cheap move is to not look too hard, to report the staircase that confirms the story and let the flat line pass. The valuable move is the opposite: the prediction that fails is the most information-dense thing in the whole run, because it is the only part that was telling you something you did not already believe. Keeping it is what turned a tidy confirmation into a real finding.

## What it looks like to develop toward a boundary

Once you have the two boundaries, development changes character. You stop trying to solve "the reverse problem" and start asking, for each boundary, what closes it.

For parameterization recovery, the frontier is what to do when you cannot carry identity, a raw scan, a changed topology. That points toward a learned reconstruction, a model of the inverse map that is differentiable, which incidentally gives you the gradient transfer the simulation people want for free. For representation richness, the frontier is enforcement: when you do want a property held, do you guarantee it by construction or coax it with a penalty. Those are different research directions, and you only know to pursue them separately because the boundary is split. Before the split, they were a single fog called "make reconstruction better."

That is the quiet payoff of finding the seam. It does not solve the problem. It replaces one vague problem with two sharp ones, each of which you can actually develop against, and it tells you honestly which one you have a handle on and which one you do not.

The instrument is open, with the experiment and the figures, if you want to see the boundary measured rather than asserted. But the part I would hand to someone working on anything hard is smaller than the geometry. When a difficulty resists, build the rig that lets its pieces move on their own, and watch for the piece that refuses to move with the rest. That piece is your second problem. Finding it is most of the work.

<footer class="writing-footer">
  <div class="writing-footer__end-mark">— end · 2026-06-08</div>

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
        <a href="/work/passthrough/" class="writing-footer__see-also-link">passthrough</a>
        <span class="writing-footer__see-also-tag">instrument 04</span>
      </li>
      <li class="writing-footer__see-also-item">
        <a href="https://github.com/barnes-ngb/passthrough" class="writing-footer__see-also-link">source</a>
        <span class="writing-footer__see-also-tag">github</span>
      </li>
      <li class="writing-footer__see-also-item">
        <a href="/writing/pixels-to-atoms/" class="writing-footer__see-also-link">Pixels to atoms</a>
        <span class="writing-footer__see-also-tag">writing</span>
      </li>
    </ul>
  </div>
</footer>

