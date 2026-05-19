---
type: problem-type
subject: physics
tags:
  - problem-solving
  - kinematics
  - forces-and-motion
level: a-level
difficulty: 2
status: usable
aliases:
  - Projectile Problem
  - 2D Projectile Motion
  - Launched Projectile Calculation
sources: []
---

# Projectile Motion Problem

## Problem Signal

A body is launched and then moves only under gravity (air resistance neglected), with motion in two dimensions. The question asks for range, maximum height, time of flight, landing velocity, or launch angle. Trigger phrases: "projectile", "launched at an angle", "fired horizontally from a cliff", "ball kicked off the edge".

## Required Quantities

- [[Velocity]]
- [[Displacement]]
- [[Acceleration]]

## Required Concepts

- Independence of horizontal and vertical motion

## Required Laws or Results

- Horizontal: constant velocity, $x = u_x t$
- Vertical: SUVAT with $a = g$

## Required Methods

- [[Using-SUVAT-Equations]]
- [[Projectile-Motion-Model]]

## Standard Approach

1. Resolve the launch velocity into horizontal $u_x = u\cos\theta$ and vertical $u_y = u\sin\theta$ components.
2. Treat horizontal motion as constant velocity ($a_x = 0$) and vertical motion as constant acceleration ($a_y = g$ downward).
3. Use the vertical equations to find the time of flight (often via the vertical displacement condition).
4. Substitute that time into the horizontal equation to find range or position.
5. For maximum height set $v_y = 0$; for landing velocity recombine the final components with Pythagoras.
6. State directions and use a consistent sign convention throughout.

## Variations

- Horizontal launch from a height: $u_y = 0$, vertical drop sets the time.
- Symmetric ground-to-ground launch: range $R = \dfrac{u^2 \sin 2\theta}{g}$.
- Landing on different level: solve the vertical quadratic and take the positive time.

## Common Traps

- Applying gravity to the horizontal motion.
- Forgetting that the vertical velocity is zero only at the peak, not the speed.
- Using the speed instead of the vertical component in vertical SUVAT.
- [[Forgetting-Vector-Direction]]

## Visuals

### Projectile geometry: independent horizontal and vertical motion

![[_attachments/11_Problems/Projectile-Motion-Problem--projectile-geometry.svg]]
*Figure: Launch velocity resolved into horizontal (u_x, constant) and vertical (u_y, decreasing under gravity) components. Gravity acts only downward; the horizontal motion is unaffected.*
*Source: Authored for this vault (CC0). No external copyright.*

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
