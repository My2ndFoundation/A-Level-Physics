---
type: method
subject: physics
tags:
  - circular-motion
  - newtonian-world
  - a-level-core
  - problem-solving
level: a-level
difficulty: 2
status: usable
aliases:
  - Solving Circular Motion Problems
  - Circular Motion Problem Method
sources: []
---

# Solving Circular Motion Problems

## Purpose

A reliable procedure for problems where an object moves on a circular path: finding speed, period, required force, or which force supplies the centripetal requirement.

## When to Use

- An object moves on a circular or curved path (orbits, rides, corners, vertical circles, charged particles in fields).
- The question mentions radius, period, revolutions per minute, [[Angular-Velocity]], or "force needed to keep it moving in a circle".

## Prerequisites

- [[Circular-Motion]]
- [[Centripetal-Force]]
- [[Newton-Second-Law]]

## Method

1. Draw the object and a free-body diagram; mark every real force (tension, weight, normal, friction, magnetic).
2. Choose the radial direction (towards the centre) as positive.
3. Convert quantities to SI: radius in m, time in s; convert rev min⁻¹ to ω using ω = 2π × (rev s⁻¹), or use ω = 2π/T = 2πf.
4. Write the resultant of the real forces *along the radius* and set it equal to the centripetal requirement: ΣF_radial = m v²/r = m ω² r.
5. Solve for the unknown. For vertical circles, evaluate at the critical point (top: weight aids the inward force; minimum speed at top when tension/contact = 0 gives v² = gr).
6. Check units and that the force points inward (centre-seeking), not outward.

## Worked Example

A 0.20 kg ball on a 0.50 m string is whirled in a horizontal circle at 3.0 rev s⁻¹. ω = 2π(3.0) = 18.8 rad s⁻¹. Tension ≈ m ω² r = 0.20 × (18.8)² × 0.50 ≈ 35 N (ignoring weight). See [[Banked-Tracks-and-Centrifuges]] for the inclined case.

## Why It Works

[[Centripetal-Acceleration]] a = v²/r = ω²r is real because velocity direction changes. [[Newton-Second-Law]] applied radially equates the net real inward force to m a — no extra "centrifugal" force is added.

## Common Mistakes

- [[Confusing-Angular-and-Linear-Quantities]]

## Related Quantities

- [[Angular-Velocity]]
- [[Centripetal-Acceleration]]
- [[Period]]
- [[Frequency]]

## Related Laws or Results

- [[Newton-Second-Law]]

## Related Problem Types

- [[Banked-Tracks-and-Centrifuges]]

## Visuals

### Centripetal force on an object in circular motion
![[_attachments/07_Methods/solving-circular-motion-problems--radial-force.svg]]
*Figure: Object m moves on a circular orbit (dashed). Velocity v is tangential (green). The net inward force F = mv²/r (red) always points toward the centre — this is supplied by tension, gravity, normal force, or any real force, never a separate "centrifugal" force.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; The Physics Classroom — no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (M5.2 Circular motion)
