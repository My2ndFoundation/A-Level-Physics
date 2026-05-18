---
type: problem-type
subject: physics
tags:
  - problem-solving
  - kinematics
  - forces-and-motion
level: a-level
difficulty: 1
status: usable
aliases:
  - SUVAT Problem
  - Constant Acceleration Kinematics
  - Equations of Motion Problem
sources: []
---

# SUVAT Kinematics Problem

## Problem Signal

The body moves in a straight line with **constant acceleration** (often gravity), and the question gives three of the five kinematic quantities — displacement $s$, initial velocity $u$, final velocity $v$, acceleration $a$, time $t$ — and asks for one of the others. Trigger phrases: "uniform acceleration", "starts from rest", "decelerates uniformly", "free fall", or any numeric data set with no force/energy emphasis.

## Required Quantities

- [[Displacement]]
- [[Velocity]]
- [[Acceleration]]

## Required Concepts

- Constant acceleration assumption

## Required Laws or Results

- $v = u + at$
- $s = ut + \tfrac{1}{2}at^2$
- $v^2 = u^2 + 2as$
- $s = \tfrac{1}{2}(u+v)t$

## Required Methods

- [[Using-SUVAT-Equations]]

## Standard Approach

1. Define a positive direction and list the five symbols, marking knowns and the unknown.
2. Note which quantity is **not** involved — this selects the equation that omits it.
3. Substitute with consistent SI units; keep signs consistent with the chosen positive direction.
4. Solve algebraically before substituting where possible to reduce error.
5. For two-stage motion, treat each constant-acceleration stage separately and pass the final velocity of one stage as the initial velocity of the next.
6. Check the answer's sign and magnitude make physical sense.

## Variations

- Vertical free fall: $a = g \approx 9.81\ \text{m s}^{-2}$ downward.
- Quadratic in $t$: solve $s = ut + \tfrac{1}{2}at^2$ with the quadratic formula and reject the unphysical root.
- Reaction-time / braking distance problems combining a constant-velocity stage and a deceleration stage.

## Common Traps

- Using a SUVAT equation when acceleration is **not** constant.
- Sign errors: taking downward as positive in one line and negative in another.
- Forgetting that "dropped" or "from rest" means $u = 0$, while "thrown down" does not.
- Mixing units (cm with m, km h⁻¹ with s).

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
