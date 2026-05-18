---
type: application
subject: physics
tags:
  - circular-motion
  - newtonian-world
  - a-level-core
  - technology-link
level: a-level
difficulty: 3
status: usable
aliases:
  - Banked Tracks and Centrifuges
  - Banked Curves
  - Centrifuge
sources: []
---

# Banked Tracks and Centrifuges

## Problem Context

Two classic real-world contexts where a real force is engineered to supply the centripetal requirement of [[Circular-Motion]]: vehicles or athletes on a banked curve, and high-speed centrifuges used to separate mixtures.

## Physical Ideas

- [[Circular-Motion]]
- [[Centripetal-Force]]
- [[Centripetal-Acceleration]]
- [[Newton-Second-Law]]

## Mathematical Tools

- [[Angular-Velocity]]
- [[Solving-Circular-Motion-Problems]]
- [[Radian]]

## Typical Questions

- Find the ideal banking angle θ for a curve of radius r at design speed v.
- Find the maximum cornering speed when friction is present.
- Calculate the effective acceleration (in multiples of g) at the wall of a centrifuge spinning at N rev min⁻¹.

## Method Outline

1. **Banked track**: with no friction the normal contact force N is tilted by angle θ. Vertical: N cos θ = mg. Horizontal (towards centre): N sin θ = m v²/r. Dividing gives tan θ = v²/(r g) — the ideal speed needs no friction.
2. Convert any rev min⁻¹ to ω = 2π × (rev s⁻¹) before using a = ω² r.
3. **Centrifuge**: contents pressed outward in the rotating frame; in the lab frame the tube wall provides the inward [[Centripetal-Force]]. Effective field a = ω² r, often quoted as a/g (the "g-force"), drives denser particles outward fastest.
4. Solve for the requested unknown and sanity-check the inward direction.

## Assumptions

- Rigid circular path of constant radius.
- For the ideal banked case, friction is neglected (point-mass on a smooth incline).
- Steady angular speed (uniform circular motion); air resistance negligible.

## Links to Other Subjects

- Mathematics: resolving vectors, trigonometry (tan θ = v²/rg), unit conversion.
- Computer Science: numerical modelling of cornering dynamics and separation times.

## Frontier Links

- [[Particle-Physics-Map]]

## Common Mistakes

- [[Confusing-Angular-and-Linear-Quantities]]

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; The Physics Classroom — no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (M5.2 Circular motion)
