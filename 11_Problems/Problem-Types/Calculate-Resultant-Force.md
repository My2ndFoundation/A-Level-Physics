---
type: problem-type
subject: physics
tags:
  - problem-solving
  - forces
  - vectors
  - newtons-laws
level: a-level
difficulty: 1
status: usable
aliases:
  - Resultant Force Problem
  - Net Force Calculation
  - Finding the Resultant Force
sources: []
---

# Calculate Resultant Force

## Problem Signal

The question gives two or more forces acting on a single body — often at angles — and asks for the **net (resultant) force**, or for the acceleration that follows from it. Trigger phrases: "find the resultant force", "the net force on the object", "what single force has the same effect", or a free-body diagram with several arrows. If the body is in equilibrium the resultant is zero and you instead solve for an unknown force.

## Required Quantities

- [[Force]]
- [[Acceleration]]

## Required Concepts

- Vector addition
- Equilibrium (resultant = 0)

## Required Laws or Results

- [[Newton-Second-Law]]

## Required Methods

- [[Resolving-Forces]]
- [[Applying-Newton-Second-Law]]

## Standard Approach

1. Draw a free-body diagram with every force labelled, including weight, normal contact, tension, friction and applied forces.
2. Choose convenient perpendicular axes (often horizontal/vertical, or along/perpendicular to an incline).
3. Resolve each force into components along the chosen axes using sine and cosine.
4. Sum components on each axis separately to get the resultant components $\Sigma F_x$ and $\Sigma F_y$.
5. Combine with Pythagoras: $F_R = \sqrt{(\Sigma F_x)^2 + (\Sigma F_y)^2}$, and find direction with $\tan\theta = \Sigma F_y / \Sigma F_x$.
6. If asked for acceleration, apply $a = F_R / m$ along the resultant direction.

## Variations

- Two forces only at an angle: use the parallelogram or triangle of forces directly.
- Equilibrium: set $\Sigma F_x = 0$ and $\Sigma F_y = 0$ and solve for unknowns.
- Inclined plane: resolve weight into components parallel and perpendicular to the slope.
- Three forces in equilibrium: the closed vector triangle can be solved with the sine rule.

## Common Traps

- Forgetting to include weight $mg$ as a force.
- Mixing up which component uses sine and which uses cosine — define the angle carefully.
- Adding force magnitudes arithmetically instead of as vectors.
- Treating the resultant as zero when the body moves at constant velocity is correct; treating it as zero when the body accelerates is wrong.

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
