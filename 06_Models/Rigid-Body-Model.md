---
type: model
subject: physics
tags:
  - model
  - mechanics
  - forces
  - moments
  - a-level-core
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - Rigid Body
  - Extended Rigid Body
sources: []
---

# Rigid Body Model

## Core Idea

The rigid body model treats an object as having a definite size and shape that
does not change under the forces acting on it. Unlike a point mass, a rigid
body has extent, so where a force acts matters — it can both accelerate the
body and turn it.

## Assumptions

- The body does not deform, stretch, or compress under load.
- The distance between any two points in the body stays constant.
- The body has a well-defined [[Centre-of-Mass]].
- Forces act at specific points or along specific lines of action.

## Quantities Involved

- [[Force]]
- [[Moment]]
- [[Centre-of-Mass]]

## Key Equations

- For translational equilibrium: net [[Resultant-Force]] = 0.
- For rotational equilibrium: sum of clockwise moments = sum of
  anticlockwise moments about any point (the [[Principle-of-Moments]]).
- Moment of a force: M = F × d, where d is the perpendicular distance from the
  pivot to the line of action of force F (unit: N m).

## When to Use

Use this model for any extended object where rotation, balancing, toppling, or
the position of forces matters: beams, ladders, seesaws, [[Levers]], bridges,
and any [[Equilibrium]] problem that involves moments.

## Limits of the Model

- Real materials deform; if bending or stretching is important, the rigid
  assumption fails and material behaviour must be considered.
- It ignores internal stresses and strains.
- For purely translational problems with no rotation, the simpler point-mass
  model is enough.

## Foundation Link

It extends the point-mass idea by restoring the object's size, which is needed
once turning effects and [[Moment]] enter the analysis.

## Related Methods

- Taking moments about a chosen pivot to remove an unknown force
- Resolving forces into components before applying equilibrium

## Related Applications

- [[Levers]]

## Frontier Links

- Rotational dynamics and moment of inertia (extends beyond A-Level)

## Common Mistakes

- Treating an extended body as a point and ignoring turning effects.
- Forgetting that moment depends on the perpendicular distance, not the raw
  distance to the force.

## Source Trace

OpenStax College Physics; HyperPhysics; The Physics Classroom — no copied text.

OCR alignment: [[OCR-Physics-A-H556-Specification]]
