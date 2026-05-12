---
layout: ../layouts/BaseLayout.astro
title: About — Nathan Barnes
description: Design-to-fabrication systems engineer. I build calibrated instruments for physical work — geometry pipelines, CNC automation, field verification, fabrication-aware constraint engines.
---

# About

I build **calibrated instruments for physical work**.

The word I use for what I make is *instruments*, deliberately — not platforms, not apps. An instrument is a tool you can trust because its behavior is known and its output is reproducible. A geometry pipeline, a CNC automation script, a field-verification streamer, a fabrication-aware constraint engine — each one takes a messy, ambiguous signal and produces an unambiguous decision a person or a machine can act on.

That framing came out of years on a shop floor where the digital model never matched what was actually built. The gap between design intent and fabrication reality is where most hardware programs lose money, time, and people. Closing that gap is the work I keep returning to.

## How I got here

I trained as an architect — M.Arch from UT Arlington with a Business minor, on top of an undergraduate degree in Architecture — and ended up in fabrication almost by accident. Field-tested at Zahner: bespoke metal envelopes, complex curved systems, projects where every panel was unique and every tolerance was tight.

What I learned there is that the hardest manufacturing problems aren't in the machines. They're in the gap between what the designer intended and what the shop floor can actually build. I built instruments to close that gap.

A few of them:

- **ZEMaPP** — a hybrid C# / Python / Grasshopper platform that preps CNC fabrication files for unique-part production. Used across the engineering team. Handles tens of thousands of unique components per project.
- **MODA** — a browser-based 3D configurator that translates customer design selections into spec-ready build configurations with integrated quoting. React, Three.js, TypeScript.
- **SurveyLink** — a real-time field verification platform that streams 3D positional data from a robotic total station to a web app. Documented in a [peer-reviewed paper](https://www.tandfonline.com/doi/abs/10.1080/24751448.2022.2116230) (*Construction Robotics, Taylor & Francis, 2022*); the published case reports a ~65% field-layout time reduction and thousands of anchor placements verified in-situ.
- **Directive Engine** — takes point cloud scan data, compares against nominal design models, and emits DOF-aware correction directives (move, rotate, index) with visualization and verification. Live at [directive-engine.vercel.app](https://directive-engine.vercel.app).

The full set is on [Work](/work). The pattern across all of them is the same: a signal comes in, a constraint engine reasons about feasibility and tolerance, and a directive comes out that someone — or some machine — can execute.

## What I work on

The problem shape I'm built for shows up across industries — energy hardware (battery packs, electrolyzers), defense and space hardware (rocket motors, satellite assemblies, autonomous vessels), and the next generation of design-to-fabrication SaaS. The wrapper changes; the problem doesn't. Complex 3D geometry has to become a real physical thing, and the pipeline between design intent and fabrication reality is broken.

Metal building envelopes are where I learned this. The problem rhymes anywhere a unique part has to be built right the first time.

## How I work

I lead through demonstration, not authority. Show me the problem, give me the room, and I come back with something that works. I'm at my best in the middle of a project that already has momentum.

I develop people by pointing them at gaps and clearing obstacles, not by assigning tasks or running process. I do my best thinking in environments where the work itself is the argument.

## Outside the work

Most Saturday mornings are *Dad Lab* — a learning rhythm I run with my two kids, where we build things, break things, ask *what if*, and end every session with the older one teaching the younger one what just happened. The artifact is the evidence; if you can't explain it, you don't understand it.

Dad Lab sits inside a bigger frame: **First Principles Foundry**, the homeschool we run as a family. Like everything else I work on, I've instrumented it — AI-assisted lesson setup, an evaluation system that tracks progress across subjects, and a growing toolkit of small tools that augment the day-to-day. The kids don't know they're inside a build system. They just know learning is the work, and the work makes things.

That, more than anything else on this site, explains why I build the way I do.

## Reach me

- Email: [barnes.ngb@gmail.com](mailto:barnes.ngb@gmail.com)
- LinkedIn: [in/barnesngb](https://www.linkedin.com/in/barnesngb/)
- GitHub: [barnes-ngb](https://github.com/barnes-ngb)
- Instagram: [_nathanbarnes_](https://www.instagram.com/_nathanbarnes_/)
