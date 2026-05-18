---
type: worked-example
subject: physics
tags:
  - problem-solving
  - simple-harmonic-motion
  - newtonian-world
level: a-level
difficulty: 2
status: usable
sources: []
---

# Worked SHM Mass Spring

## Problem

A mass of $0.30\ \text{kg}$ hangs from a spring of force constant $48\ \text{N m}^{-1}$ and oscillates vertically with simple harmonic motion of amplitude $5.0\ \text{cm}$. Find (a) the period of oscillation, (b) the maximum speed of the mass, and (c) the magnitude of the maximum acceleration.

## Source Reference

- Source: Original worked example; pattern aligned to OCR H556.
- Page/Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]

## Required Quantities

- [[Displacement]]
- [[Acceleration]]
- [[Frequency]]

## Required Concepts

- Restoring force proportional to displacement

## Required Methods

- [[Solving-SHM-Problems]]
- [[Applying-Conservation-of-Energy]]

## Solution

**Set up.** Amplitude $A = 5.0\ \text{cm} = 0.050\ \text{m}$.

**(a) Period.** For a mass–spring system:

$$T = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{0.30}{48}} = 2\pi\sqrt{6.25\times10^{-3}} = 2\pi (0.0791) = 0.497\ \text{s}$$

**Angular frequency.** $\omega = \dfrac{2\pi}{T} = \dfrac{2\pi}{0.497} = 12.65\ \text{rad s}^{-1}$.

(Check: $\omega = \sqrt{k/m} = \sqrt{48/0.30} = \sqrt{160} = 12.65\ \text{rad s}^{-1}$ — consistent.)

**(b) Maximum speed.** Occurs at the equilibrium position:

$$v_{\max} = \omega A = 12.65 \times 0.050 = 0.63\ \text{m s}^{-1}$$

**(c) Maximum acceleration.** Occurs at maximum displacement:

$$a_{\max} = \omega^2 A = (12.65)^2 \times 0.050 = 160 \times 0.050 = 8.0\ \text{m s}^{-2}$$

## Unit Check

$T = \sqrt{\text{kg}/(\text{N m}^{-1})} = \sqrt{\text{kg m / N}} = \sqrt{\text{s}^2} = \text{s}$. $v_{\max} = (\text{rad s}^{-1})(\text{m}) = \text{m s}^{-1}$. $a_{\max} = (\text{s}^{-2})(\text{m}) = \text{m s}^{-2}$. Consistent.

## Key Insight

Period depends only on $m$ and $k$, not on amplitude. Maximum speed occurs at equilibrium ($\omega A$), while maximum acceleration occurs at the extremes ($\omega^2 A$) — they never peak at the same instant.

## Common Mistakes

- Leaving the amplitude in centimetres.
- Confusing $v_{\max} = \omega A$ with $a_{\max} = \omega^2 A$.
- Assuming the period changes if the amplitude changes.

## Related Problem Types

- [[Simple-Harmonic-Motion-Problem]]
