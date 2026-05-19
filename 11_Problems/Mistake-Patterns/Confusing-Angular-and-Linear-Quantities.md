---
type: mistake-pattern
subject: physics
tags:
  - mistake-pattern
  - circular-motion
  - simple-harmonic-motion
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Confusing Angular and Linear Quantities
  - Mixing Up Angular and Linear Motion
sources: []
---

# Confusing Angular and Linear Quantities

## Mistake

Treating angular and linear quantities as interchangeable: substituting linear speed $v$ where [[Angular-Velocity]] $\omega$ is required (or vice versa), forgetting the factor of radius $r$, using degrees instead of radians, or confusing rev s⁻¹ with rad s⁻¹.

## Why It Happens

Both describe how fast something moves, and the symbols look similar. Learners forget that $v = \omega r$ links them through the radius, that the [[Radian]] is the required angular unit (one revolution $= 2\pi$ rad, not 360 in formulae), and that $\omega = 2\pi f$, not $f$.

## Example

A wheel of radius $0.25\ \text{m}$ turns at $4.0$ rev s⁻¹. A common error is to write $a = v^2/r$ with $v = 4.0$, giving a wrong answer. Correct: $\omega = 2\pi \times 4.0 = 25.1\ \text{rad s}^{-1}$, so rim speed $v = \omega r = 6.3\ \text{m s}^{-1}$ and [[Centripetal-Acceleration]] $a = \omega^2 r = 158\ \text{m s}^{-2}$. Another frequent error: leaving a calculator in degree mode when evaluating $x = A\cos(\omega t)$ in [[Simple-Harmonic-Motion]].

## Correct Approach

- Identify whether the quantity is angular ($\theta$, $\omega$, in rad, rad s⁻¹) or linear ($s$, $v$, in m, m s⁻¹).
- Always convert revolutions and frequency to angular measure: $\omega = 2\pi f = 2\pi/T$; one revolution $= 2\pi$ rad.
- Use $v = \omega r$ and $a = \omega^2 r = v^2/r$ to move between them, never dropping the radius.
- Keep the calculator in radian mode for [[Simple-Harmonic-Motion-Equation]] work.

## Foundation Link

Rooted in the GCSE habit of using only linear [[Speed]] and measuring angles in degrees, before the [[Radian]] is introduced as the natural unit for rotation and oscillation.

## Related Quantities

- [[Angular-Velocity]]
- [[Centripetal-Acceleration]]
- [[Period]]
- [[Frequency]]

## Related Concepts

- [[Circular-Motion]]
- [[Radian]]
- [[Simple-Harmonic-Motion]]

## Related Methods

- [[Solving-Circular-Motion-Problems]]
- [[Solving-SHM-Problems]]

## Related Problem Types

- [[Banked-Tracks-and-Centrifuges]]

## Source Trace

- Source: OCR examiner-report style guidance; The Physics Classroom; HyperPhysics — no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (M5.2 / M5.3)
