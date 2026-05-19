---
type: application
subject: physics
tags:
  - technology-link
  - mechanics
  - kinematics
  - forces-and-motion
level: a-level
difficulty: 2
status: usable
aliases:
  - Projectiles
  - Projectile Trajectory
sources: []
---

# Projectile Motion

## Problem Context

Projectile motion describes any object moving under gravity alone after release: a thrown ball, a long jumper, a stream of water, a stunt car leaving a ramp. In A-Level exams it is the classic test of whether a learner can treat a single curved path as two independent straight-line problems. The context is usually idealised so that air resistance is ignored and gravity is the only force acting after launch.

## Physical Ideas

- [[Projectile-Motion-Model]]
- [[Constant-Acceleration-Model]]
- [[Newton-Second-Law]]
- [[Velocity]]
- [[Displacement]]
- [[Resultant-Force]]

## Mathematical Tools

- [[Using-SUVAT-Equations]]
- [[Resolving-Forces]]
- Trigonometric resolution of launch velocity into horizontal and vertical components
- Quadratic equations for time of flight

## Typical Questions

- Find the range of a ball launched at a given speed and angle.
- Find the time to reach maximum height and the maximum height itself.
- Find the velocity (magnitude and direction) of a projectile at a given instant.
- Show that for a given speed the range is maximised at a launch angle of 45°.

## Method Outline

1. Resolve the launch velocity into horizontal and vertical components.
2. Treat horizontal motion as constant velocity (zero horizontal acceleration).
3. Treat vertical motion as constant acceleration with $a = g$ downward.
4. Use a shared time variable to link the two directions.
5. Recombine components vectorially when a resultant velocity or position is required.

## Assumptions

- Air resistance is negligible.
- Gravitational field strength `g` is constant over the trajectory.
- The object is a point mass with no spin or lift.
- Launch and landing heights are clearly defined.

## Links to Other Subjects

- Mathematics: parametric equations, quadratic roots for time of flight, and the parabola as the locus of the path.
- Computer Science: numerical time-stepping (Euler integration) to simulate trajectories when drag is added and no closed-form solution exists.

## Frontier Links

- [[Particle-Physics-Map]] — charged particles in fields follow analogous decomposed motion.

## Common Mistakes

- [[Forgetting-Vector-Direction]]
- [[Mixing-Speed-and-Velocity]]
- [[Treating-Scalars-as-Vectors]]

## Visuals

### Projectile Trajectory Diagram
![[_attachments/10_Applications/Projectile-Motion--trajectory-diagram.png]]
*Figure: Parabolic trajectory of a projectile launched at an angle. Horizontal velocity remains constant (no air resistance); vertical velocity increases downward under gravity. The two components combine to give the curved path. Maximum height occurs where vertical velocity = 0.*
*Source: Projectile-Motion — CS Odessa — CC BY 4.0 — https://commons.wikimedia.org/wiki/File:Projectile-Motion.png. Retrieved 2026-05-19.*

## Source Trace

- Source: OpenStax College Physics; IOPSpark; Isaac Physics; OCR examiner reports (general) — no copied text
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
