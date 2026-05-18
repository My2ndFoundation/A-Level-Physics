---
type: worked-example
subject: physics
tags:
  - problem-solving
  - kinematics
  - forces-and-motion
level: a-level
difficulty: 2
status: usable
sources: []
---

# Worked SUVAT Cliff Projectile

## Problem

A stone is thrown horizontally with speed $14\ \text{m s}^{-1}$ from the top of a vertical cliff of height $32\ \text{m}$ above level ground. Air resistance is negligible and $g = 9.81\ \text{m s}^{-2}$. Find (a) the time the stone is in the air, (b) the horizontal distance from the base of the cliff where it lands, and (c) the speed of the stone just before impact.

## Source Reference

- Source: Original worked example; pattern aligned to OCR H556.
- Page/Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]

## Required Quantities

- [[Velocity]]
- [[Displacement]]
- [[Acceleration]]

## Required Concepts

- Independence of horizontal and vertical motion

## Required Methods

- [[Using-SUVAT-Equations]]
- [[Projectile-Motion-Model]]

## Solution

**Set up.** Take downward as positive for the vertical motion. Initial vertical velocity $u_y = 0$ (thrown horizontally). Horizontal velocity is constant at $u_x = 14\ \text{m s}^{-1}$.

**(a) Time of flight.** Vertical: $s_y = u_y t + \tfrac{1}{2} a t^2$ with $s_y = 32\ \text{m}$, $u_y = 0$, $a = 9.81\ \text{m s}^{-2}$.

$$32 = \tfrac{1}{2}(9.81)t^2 \implies t^2 = \frac{64}{9.81} = 6.524 \implies t = 2.55\ \text{s}$$

**(b) Horizontal distance.** $x = u_x t = 14 \times 2.55 = 35.8\ \text{m}$.

**(c) Impact speed.** Vertical velocity at impact: $v_y = u_y + at = 0 + 9.81 \times 2.55 = 25.0\ \text{m s}^{-1}$.

Combine components: $v = \sqrt{u_x^2 + v_y^2} = \sqrt{14^2 + 25.0^2} = \sqrt{196 + 625} = 28.7\ \text{m s}^{-1}$.

## Unit Check

$t^2 = \text{m} / (\text{m s}^{-2}) = \text{s}^2$, so $t$ in s. Horizontal distance: $(\text{m s}^{-1})(\text{s}) = \text{m}$. Speed combines m s⁻¹ components, giving m s⁻¹. All consistent.

## Key Insight

Horizontal and vertical motions are independent and share only the time. The vertical drop alone sets the flight time; horizontal speed never affects how long the stone is airborne.

## Common Mistakes

- [[Forgetting-Vector-Direction]]
- Applying gravity to the horizontal motion.
- Reporting the vertical component as the final speed instead of combining components.

## Related Problem Types

- [[Projectile-Motion-Problem]]
- [[SUVAT-Kinematics-Problem]]
