---
type: method
subject: physics
tags:
  - cross-subject
  - maths-link
  - further-maths-link
  - a-level-core
level: a-level
difficulty: 2
status: draft
aliases:
  - Differential Equation
  - ODE
sources: []
---

# Differential-Equations

> Deliberately shallow **cross-subject orientation** page — how a Maths idea appears in A-Level Physics, not a full Maths lesson.

## Purpose

A differential equation relates a quantity to its own rate of change. Many A-Level laws *are* differential equations in disguise — you mostly recognise and use their **solutions** rather than solve them from scratch.

## When to Use

Whenever a rate of change is proportional to the current amount (exponential change) or to displacement (oscillation).

## Prerequisites

- [[Differentiation]]
- [[Integration]]

## Method

1. Recognise the form: `dN/dt = −λN` → exponential decay; `a = −ω²x` → SHM.
2. Quote the standard solution: `N = N₀e^(−λt)`; `x = A cos(ωt)`.
3. Substitute the physical constants and read off the behaviour.

## Worked Example

Capacitor discharge obeys `dQ/dt = −Q/(RC)`, solved by `Q = Q₀e^(−t/RC)`. See [[Capacitor-Discharge-Equation]] and [[Radioactive-Decay-Law]].

## Why It Works

The exponential and sinusoidal functions are the unique functions whose derivative reproduces themselves (up to a constant), so they solve these rate laws exactly.

## Common Mistakes

- Treating exponential decay as linear.
- Dropping the minus sign that signals decay or a restoring effect.

## Related Quantities

- [[Half-Life]]

## Related Laws or Results

- [[Simple-Harmonic-Motion-Equation]]
- [[Radioactive-Decay-Law]]

## Related Problem Types

- Exponential decay (capacitor, radioactivity) and SHM modelling questions.

## External Resources

- Khan Academy — Differential equations: https://www.khanacademy.org/math/differential-equations
- Isaac Physics — Mathematics for physics: https://isaacphysics.org
- Wikipedia — Differential equation: https://en.wikipedia.org/wiki/Differential_equation

## Source Trace

- Source: Authored for this vault — cross-subject orientation; external resources listed inline.
- Section/Page: n/a
