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
  - Simulation
  - Computer Simulation
sources: []
---

# Simulation

> Deliberately shallow **cross-subject orientation** page — how computing models physical systems for A-Level Physics, not a full computational-physics course.

## Problem Context

A simulation uses a computer to predict how a physical system evolves by repeatedly applying the laws of physics in small steps. It lets you explore systems that are hard to set up experimentally or to solve exactly — projectiles with drag, oscillators with [[Damping]], radioactive decay.

## Physical Ideas

- [[Newton-Second-Law]]
- [[Radioactive-Decay-Law]]

## Mathematical Tools

- Step-by-step (iterative) updates; see [[Numerical-Modelling]].

## Typical Questions

- Explain how a computer model predicts the path of a projectile with air resistance.
- Discuss why smaller time steps improve accuracy but cost more computation.

## Method Outline

1. Express the physics as update rules (e.g. $v \rightarrow v + a\,\Delta t$).
2. Repeat over many small time steps.
3. Plot/inspect the predicted behaviour and compare with theory or data.

## Assumptions

- The model includes the dominant physics; Δt is small enough for stability.

## Links to Other Subjects

- Mathematics: iteration, [[Differential-Equations]].
- Computer Science: algorithms, loops, [[Numerical-Modelling]].

## Frontier Links

- [[Semiconductor-Physics-Map]]

## Common Mistakes

- Trusting a simulation without checking it against a known result.
- Using too large a time step, giving unstable or wrong output.

## Visuals

<!-- Authored diagram or openly-licensed image with full caption/license/source. -->

_None yet — a simulated vs analytic trajectory plot would suit this page._

## External Resources

- Isaac Physics — Modelling: https://isaacphysics.org
- OpenStax — University Physics (modelling): https://openstax.org/subjects/science
- Wikipedia — Computer simulation: https://en.wikipedia.org/wiki/Computer_simulation

## Source Trace

- Source: Authored for this vault — cross-subject orientation; external resources listed inline.
- Section/Page: n/a
