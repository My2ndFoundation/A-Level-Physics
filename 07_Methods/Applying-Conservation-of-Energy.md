---
type: method
subject: physics
tags:
  - mechanics
  - energy
  - newtonian-world
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - energy conservation method
  - using conservation of energy
sources: []
---

# Applying Conservation of Energy

## Purpose

This method uses [[Conservation-of-Energy]] to solve problems by equating total energy before and after a process, accounting for any energy transferred away (e.g. by friction). It avoids dealing with forces and time directly when only start and end states matter.

## When to Use

Use it when a problem involves changes in speed, height, or stored energy and asks for a speed, height, or energy without needing the path or time taken — falling objects, pendulums, springs, roller-coaster style problems.

## Prerequisites

- [[Energy-Quantity|Energy]]
- [[Conservation-of-Energy]]

## Method

1. Identify the system and define a reference level for gravitational potential energy.
2. List the energy stores at the initial state (kinetic $\frac{1}{2}mv^2$, gravitational $mgh$, elastic $\frac{1}{2}kx^2$).
3. List the energy stores at the final state.
4. Account for energy transferred out (work done against friction or drag).
5. Write: total energy initial = total energy final + energy dissipated.
6. Solve for the unknown and check the result is physically reasonable.

## Worked Example

A 0.50 kg ball is dropped from 1.8 m (negligible air resistance). Taking the ground as reference: initial energy $= mgh = 0.50 \times 9.81 \times 1.8 \approx 8.8 \text{ J}$, all gravitational. At the ground this is all kinetic: $\frac{1}{2}mv^2 = 8.8 \text{ J}$, so $v = \sqrt{2 \times 8.8 / 0.50} \approx 5.9 \text{ m s}^{-1}$.

## Why It Works

Energy cannot be created or destroyed, only transferred between stores. In an isolated system the total is constant; including dissipated energy as a separate term keeps the bookkeeping exact even when friction is present.

## Common Mistakes

- Forgetting energy lost to friction or air resistance.
- Inconsistent height reference for potential energy.
- Mixing mass and weight in the energy expressions.

## Related Quantities

- [[Energy-Quantity|Energy]]
- [[Velocity]]

## Related Laws or Results

- [[Conservation-of-Energy]]

## Related Problem Types

- Falling-object, pendulum, and spring-energy problems

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
