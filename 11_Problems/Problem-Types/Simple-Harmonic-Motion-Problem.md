---
type: problem-type
subject: physics
tags:
  - problem-solving
  - simple-harmonic-motion
  - newtonian-world
level: a-level
difficulty: 2
status: usable
aliases:
  - SHM Problem
  - Oscillation Calculation
  - Mass-Spring and Pendulum Problem
sources: []
---

# Simple Harmonic Motion Problem

## Problem Signal

An oscillating system (mass–spring, simple pendulum, floating object, vibrating particle) is described, and the question asks for period, frequency, maximum speed or acceleration, displacement at a given time, or energy in the oscillation. Trigger phrases: "simple harmonic motion", "oscillates", "period of oscillation", "amplitude", "restoring force proportional to displacement".

## Required Quantities

- [[Displacement]]
- [[Acceleration]]
- [[Frequency]]

## Required Concepts

- Restoring force $\propto$ displacement, directed to equilibrium
- Energy interchange between kinetic and potential

## Required Laws or Results

- $a = -\omega^2 x$
- $x = A\cos\omega t$ (or $A\sin\omega t$), $v_{\max} = \omega A$, $a_{\max} = \omega^2 A$
- Mass–spring: $T = 2\pi\sqrt{m/k}$; pendulum: $T = 2\pi\sqrt{L/g}$

## Required Methods

- [[Solving-SHM-Problems]]
- [[Applying-Conservation-of-Energy]]

## Standard Approach

1. Confirm the motion is SHM (restoring force/acceleration proportional and opposite to displacement).
2. Find $\omega = 2\pi/T = 2\pi f$ using the relevant period formula.
3. Use $x = A\cos\omega t$ (start at maximum) or $x = A\sin\omega t$ (start at equilibrium) as appropriate.
4. Apply $v = \pm\omega\sqrt{A^2 - x^2}$ for speed at a given displacement, and $v_{\max} = \omega A$.
5. For energy, use $E_{\text{total}} = \tfrac{1}{2}m\omega^2 A^2$, splitting into $E_k$ and $E_p$ as needed.
6. State units and check phase choices against the stated starting position.

## Variations

- Energy questions: maximum $E_k$ at equilibrium, maximum $E_p$ at amplitude.
- Damped oscillations: amplitude decays; period roughly unchanged for light damping.
- Resonance: driven system reaches large amplitude near the natural frequency.

## Common Traps

- Using degrees instead of radians for $\omega t$.
- Confusing maximum speed ($\omega A$, at equilibrium) with maximum acceleration ($\omega^2 A$, at amplitude).
- Choosing the wrong sine/cosine form for the stated starting condition.
- Forgetting that period is independent of amplitude for ideal SHM.

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
