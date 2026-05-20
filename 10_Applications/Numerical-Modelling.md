---
type: application
subject: physics
tags:
  - cross-subject
  - computer-science-link
  - modelling
  - a-level-core
level: a-level
difficulty: 2
status: draft
aliases:
  - Numerical Modelling
  - Iterative Modelling
  - Numerical Methods
sources: []
---

# Numerical-Modelling

> Deliberately shallow **cross-subject orientation** page — the maths/CS technique behind physics [[Simulation]], not a full numerical-methods course.

## Problem Context

Numerical modelling approximates the solution of a physics problem by stepping forward in small increments instead of solving the equations algebraically. It is how capacitor discharge, radioactive decay and damped oscillations are modelled when an exact formula is awkward or unavailable.

## Physical Ideas

- [[Capacitor-Discharge-Equation]]
- [[Radioactive-Decay-Law]]

## Mathematical Tools

- The iterative (Euler) update; small time step Δt; see [[Differential-Equations]].

## Typical Questions

- Use an iterative method to estimate charge remaining on a capacitor after several time steps.
- Explain the effect of halving the step size on accuracy.

## Method Outline

1. Write the rate law, e.g. $\Delta Q = -\frac{Q}{RC} \Delta t$.
2. From the current value compute the change over Δt.
3. Update the value and repeat; tabulate or graph the results.

## Assumptions

- The rate is roughly constant within each step (good only if Δt is small).

## Links to Other Subjects

- Mathematics: [[Differentiation]], [[Differential-Equations]].
- Computer Science: loops, spreadsheets, [[Simulation]].

## Frontier Links

- [[Semiconductor-Physics-Map]]

## Common Mistakes

- Using too large a step, so the model drifts from the true curve.
- Forgetting the minus sign in a decay rate.

## Visuals

<!-- Authored diagram or openly-licensed image with full caption/license/source. -->

_None yet — an Euler-step vs exact decay-curve figure would suit this page._

### From Wikipedia

<!-- wiki-images: yes -->

#### AtmosphericModelSchematic

![[_attachments/10_Applications/Numerical-Modelling--wiki-atmosphericmodelschematic.png]]
*Figure: from Wikipedia article "Numerical weather prediction".*
*Source: Wikimedia Commons — [AtmosphericModelSchematic.png](https://commons.wikimedia.org/wiki/File:AtmosphericModelSchematic.png). Retrieved 2026-05-20.*

#### GFS 850 MB

![[_attachments/10_Applications/Numerical-Modelling--wiki-gfs-850-mb.png]]
*Figure: from Wikipedia article "Numerical weather prediction".*
*Source: Wikimedia Commons — [GFS 850 MB.PNG](https://commons.wikimedia.org/wiki/File:GFS_850_MB.PNG). Retrieved 2026-05-20.*

#### GoldenMedows

![[_attachments/10_Applications/Numerical-Modelling--wiki-goldenmedows.jpg]]
*Figure: from Wikipedia article "Numerical weather prediction".*
*Source: Wikimedia Commons — [GoldenMedows.jpg](https://commons.wikimedia.org/wiki/File:GoldenMedows.jpg). Retrieved 2026-05-20.*

## External Resources

- Isaac Physics — Modelling techniques: https://isaacphysics.org
- Physics & Maths Tutor — Capacitors / decay: https://www.physicsandmathstutor.com
- Wikipedia — Numerical analysis: https://en.wikipedia.org/wiki/Numerical_analysis

## Source Trace

- Source: Authored for this vault — cross-subject orientation; external resources listed inline.
- Section/Page: n/a
