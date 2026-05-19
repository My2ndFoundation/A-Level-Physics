---
type: method
subject: physics
tags:
  - mechanics
  - forces
  - vectors
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - resolving vectors
  - splitting forces into components
sources: []
---

# Resolving Forces

## Purpose

Resolving forces splits each [[Force]] into perpendicular components (usually horizontal/vertical or along/perpendicular to a slope) so that forces along each direction can be added independently. This converts a two-dimensional force problem into two one-dimensional ones.

## When to Use

Use it whenever forces act at angles to each other or to the direction of motion: objects on inclines, suspended objects with angled strings, [[Projectile-Motion]], or any problem where you need a resultant or equilibrium in two dimensions.

## Prerequisites

- [[Force]]
- [[Free-Body-Diagram]]
- Basic trigonometry (sine, cosine)

## Method

1. Draw a [[Free-Body-Diagram]] with every force labelled.
2. Choose convenient perpendicular axes (often along and perpendicular to the slope).
3. For each force at angle θ to an axis, component along = *F cosθ*, component perpendicular = *F sinθ*.
4. Add components along each axis separately (with signs).
5. Combine if needed: resultant magnitude = √(ΣFₓ² + ΣF_y²), direction = arctan(ΣF_y/ΣFₓ).
6. Apply equilibrium (ΣF = 0) or [[Newton-Second-Law]] per axis.

## Worked Example

A 5.0 N force acts at 30° above the horizontal. Horizontal component = 5.0 cos30° ≈ 4.3 N; vertical component = 5.0 sin30° = 2.5 N. If a second force of 4.3 N acts horizontally in the opposite direction, the net horizontal force is zero and only the 2.5 N vertical component remains.

## Why It Works

Force is a vector. Because perpendicular directions are independent, a force's effect along one axis is unaffected by its component along the other. Trigonometry recovers each component exactly from the magnitude and angle.

## Common Mistakes

- Swapping sine and cosine (measure the angle carefully).
- Forgetting weight's components on an inclined plane.
- Dropping signs when adding opposing components.

## Related Quantities

- [[Force]]
- [[Acceleration]]

## Related Laws or Results

- [[Newton-Second-Law]]

## Related Problem Types

- Inclined plane and equilibrium problems
- [[Projectile-Motion]]

## Visuals

### Vector component diagram
![[_attachments/07_Methods/resolving-forces--vector-components.svg]]
*Figure: A force F at angle θ to the horizontal resolved into its horizontal component F cosθ (red) and vertical component F sinθ (green). Perpendicular axes are independent.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
