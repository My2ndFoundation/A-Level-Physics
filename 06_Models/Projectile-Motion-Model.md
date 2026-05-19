---
type: model
subject: physics
tags:
  - mechanics
  - kinematics
  - forces-and-motion
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - projectile model
  - independence of motion model
sources: []
---

# Projectile Motion Model

## Core Idea

The projectile motion model treats two-dimensional flight under gravity as two independent one-dimensional [[Constant-Acceleration-Model|constant-acceleration]] motions: a horizontal motion at constant velocity and a vertical motion accelerating downward at *g*. The two are linked only by a shared time *t*. This decomposition is the central trick: once horizontal and vertical components are separated, each axis is solved with [[Using-SUVAT-Equations|SUVAT]] independently, then recombined.

## Assumptions

- Air resistance is negligible.
- Acceleration is purely vertical and constant (*g ≈ 9.81 m s⁻²* downward).
- Horizontal acceleration is zero, so horizontal velocity is constant.
- The object is a [[Point-Mass-Model|point mass]] following a parabolic path.
- *g* is uniform over the trajectory (flat-Earth approximation).

## Quantities Involved

- Launch speed and angle → components *uₓ = u cosθ*, *u_y = u sinθ*
- [[Velocity]] components (m s⁻¹, vector)
- [[Acceleration]] *g* (m s⁻² , vertical)
- Time of flight *t* (s)
- Horizontal range and maximum height (m)

## Key Equations

- Horizontal: *x = uₓ t*
- Vertical: *y = u_y t − ½g t²* and *v_y = u_y − g t*
- See [[Using-SUVAT-Equations]].

## When to Use

Use it for any object launched into the air with no propulsion and negligible drag: a thrown ball, a stunt jump, water from a hose, a dropped package from a moving plane. The horizontal-launch case (*u_y = 0*) is a common special form.

## Limits of the Model

It breaks down when air resistance is significant (range and symmetry of the path are reduced, trajectory becomes non-parabolic), for very long ranges where Earth's curvature or varying *g* matter, or when spin produces lift (Magnus effect).

## Foundation Link

This extends the [[Constant-Acceleration-Model]] from one dimension to two, using the GCSE idea that horizontal and vertical motions don't affect each other.

## Related Methods

- [[Resolving-Forces]]
- [[Using-SUVAT-Equations]]

## Related Applications

- [[Projectile-Motion]]

## Frontier Links

- None at A-Level depth.

## Common Mistakes

- Treating horizontal velocity as changing.
- Using launch speed instead of resolved components.
- Sign errors in the vertical direction.

## Visuals

### Projectile Trajectory with Velocity Components

![[_attachments/06_Models/Projectile-Motion-Model--trajectory.svg]]
*Figure: Parabolic path resolved into independent horizontal (constant u cosθ) and vertical (accelerating at g) components; the two share only time t.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
