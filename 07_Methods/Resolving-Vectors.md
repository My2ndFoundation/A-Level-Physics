---
type: method
subject: physics
tags:
  - foundations-of-physics
  - vectors
  - mechanics
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Resolving a Vector
  - Vector Components
  - Resolving into Components
  - Resolving Vectors
sources: []
---

# Resolving Vectors

## Purpose

Resolving a vector means splitting it into two perpendicular components so each direction can be treated independently with ordinary (scalar) arithmetic.

## When to Use

- A [[Force]] or [[Velocity]] acts at an angle to the axes of interest
- An object moves on an inclined plane and you need components along and perpendicular to the slope
- Projectile motion (separate horizontal and vertical analysis)
- Equilibrium problems where forces must balance in two directions

## Prerequisites

- [[Vectors-and-Scalars]]
- [[Vector-Triangle]]

## Method

1. Draw the vector and choose two perpendicular axes (often horizontal/vertical, or parallel/perpendicular to a slope).
2. Mark the angle $\theta$ between the vector and one chosen axis.
3. The component **along** that axis is $V\cos\theta$; the component **perpendicular** to it is $V\sin\theta$.
4. Assign signs from your chosen positive directions.
5. Repeat for every vector, then add components axis-by-axis to get the resultant (or apply equilibrium: each axis sums to zero).
6. Recombine if needed: magnitude $=\sqrt{V_x^{2}+V_y^{2}}$, direction $=\tan^{-1}(V_y/V_x)$.

## Worked Example

A 50 N force pulls a sledge at 30° above the horizontal. Horizontal component $= 50\cos30° \approx 43.3$ N (drives motion); vertical component $= 50\sin30° = 25$ N (reduces the [[Normal-Contact-Force]]). See [[Resolving-Forces]] for a fuller force-balance treatment.

## Why It Works

Perpendicular directions are independent: a force along $x$ produces no acceleration along $y$. Decomposing into orthogonal components lets each axis obey Newton's laws separately, turning a 2-D vector problem into two simple 1-D ones, then the [[Vector-Triangle]] recombines them.

## Common Mistakes

- Swapping sine and cosine (cosine goes with the angle's *adjacent* axis)
- Measuring $\theta$ from the wrong axis
- Forgetting component signs
- Resolving along non-perpendicular directions

## Related Quantities

- [[Force]]
- [[Velocity]]
- [[Coefficient-of-Friction]]

## Related Laws or Results

- [[Resultant-Force]]
- [[Conservation-of-Momentum]]

## Related Problem Types

- Inclined-plane and projectile component problems

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; HyperPhysics — no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (Module 2, foundations of physics)
