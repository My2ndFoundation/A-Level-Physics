---
type: physical-quantity
subject: physics
tags:
  - mechanics
  - forces
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - mu
  - Friction Coefficient
  - Coefficient of Friction
sources: []
---

# Coefficient of Friction

## Core Idea

The coefficient of friction is a number that measures how strongly two surfaces resist sliding over each other relative to how hard they are pressed together.

## Symbol

- $\mu$ (mu)

## SI Unit

- Dimensionless (no unit) — it is a ratio of two forces

## Scalar or Vector

- Scalar

## Definition

The coefficient of friction relates the [[Friction]] force to the [[Normal-Contact-Force]] $N$ between two surfaces:

$$F_\text{f} \le \mu N$$

For kinetic (sliding) friction, $F_\text{f} = \mu_k N$. For static friction, the friction force takes whatever value (up to a maximum $\mu_s N$) is needed to prevent sliding, so the relation is an inequality until slipping begins. Typically $\mu_s > \mu_k$ for the same pair of surfaces, which is why a stationary object takes more force to start moving than to keep moving.

## Related Equations

- $F_\text{f} = \mu N$ (limiting/kinetic friction)
- On an incline at the angle of repose, $\mu_s = \tan\theta$ (the object just begins to slide)

## How It Is Measured

Tilt a surface with a block on it and increase the angle until the block just slides; the tangent of that angle gives $\mu_s$. Alternatively, pull a block at constant velocity with a force meter on a horizontal surface: $\mu_k = F_\text{pull}/N$ where $N = mg$. Repeat for several normal loads and plot friction force against normal force — the gradient is $\mu$.

## Graphical Meaning

On a graph of friction force (y) against normal force (x), the data form a straight line through the origin whose gradient is the coefficient of friction. Curvature would indicate the simple model breaking down.

## Foundation Links

- [[Force]]
- [[Friction]]

## Related Concepts

- [[Normal-Contact-Force]]
- [[Friction]]
- [[Vectors-and-Scalars]]

## Related Laws or Results

- [[Resultant-Force]]

## Related Experiments

- Tilting-plane and constant-velocity drag measurements

## Frontier Links

- Friction originates in surface adhesion and asperity contact — see [[Semiconductor-Physics-Map]]

## Common Mistakes

- Treating $F_\text{f} = \mu N$ as always an equality (static friction is $\le \mu_s N$)
- Assuming friction depends on contact area (it depends on $N$, not area, in this model)
- Giving $\mu$ a unit (it is dimensionless)
- Using $N = mg$ on an incline instead of $N = mg\cos\theta$ — see [[Resolving-Vectors]]

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; HyperPhysics — no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (Module 3, forces in action)
