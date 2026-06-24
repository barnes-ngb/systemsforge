---
layout: ../../layouts/BaseLayout.astro
title: "Fabricator API"
description: "Early fabrication constraint checks for complex geometry workflows."
---

# Fabricator API

## Problem
Design teams need **fabrication constraints earlier** in the modeling cycle to avoid late-stage rework, value engineering, or downstream constructability surprises.

## Approach
We embedded constraint “bumpers” inside Grasshopper. Rules and geometric relationships encode production constraints so designers get immediate feedback while they explore forms.

## Capabilities
- Surface analysis and curvature checks.
- Panelization guidance with outlier detection.
- Sheet sizing, nesting, and takeoff outputs.
- Panel span and performance sanity checks.

## What shipped
A reusable tool library with a plugin distribution approach that allowed teams to install, update, and standardize constraint checks across projects.

## Where this transfers

The specific rules here are facade panelization, but the move is general: put production constraints inside the tool where the geometry is created, so a violation shows up while the form is still cheap to change instead of at the shop. That is the same shift-left idea behind design-for-manufacturing checks in aerospace structures and in sheet-metal and CNC work. Wherever a design environment and a manufacturing process are separated by a handoff, constraint feedback at design time is what keeps late rework and value engineering from becoming the default.

## Collaboration
Built in collaboration with a top-tier architecture firm.

## Notes on rights/credits
No client imagery or proprietary details are shown.
