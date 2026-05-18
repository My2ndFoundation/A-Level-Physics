---
type: worked-example
subject: physics
tags:
  - problem-solving
  - circular-motion
  - newtonian-world
level: a-level
difficulty: 3
status: usable
sources: []
---

# Worked Circular Motion Conical Pendulum

## Problem

A small ball of mass $0.25\ \text{kg}$ is attached to a string of length $0.90\ \text{m}$ and swung so that it moves in a horizontal circle while the string makes a constant angle of $30^\circ$ to the vertical (a conical pendulum). Take $g = 9.81\ \text{m s}^{-2}$. Find (a) the tension in the string, and (b) the speed of the ball.

## Source Reference

- Source: Original worked example; pattern aligned to OCR H556.
- Page/Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]

## Required Quantities

- [[Force]]
- [[Speed]]
- [[Acceleration]]

## Required Concepts

- Centripetal force as the resultant of real forces

## Required Methods

- [[Solving-Circular-Motion-Problems]]
- [[Resolving-Forces]]

## Solution

**Set up.** The string tension $T$ acts along the string at $30^\circ$ to the vertical. Resolve it into vertical and horizontal components.

**Vertical equilibrium** (no vertical acceleration):

$$T\cos 30^\circ = mg$$
$$T = \frac{mg}{\cos 30^\circ} = \frac{(0.25)(9.81)}{0.8660} = 2.83\ \text{N}$$

**(b) Speed.** The horizontal component of tension provides the centripetal force. The circle radius is $r = L\sin 30^\circ = 0.90 \times 0.5 = 0.45\ \text{m}$.

$$T\sin 30^\circ = \frac{mv^2}{r}$$
$$(2.83)(0.5) = \frac{(0.25)v^2}{0.45}$$
$$1.415 = 0.5556\,v^2 \implies v^2 = 2.547 \implies v = 1.60\ \text{m s}^{-1}$$

## Unit Check

Tension: $(\text{kg})(\text{m s}^{-2}) = \text{N}$. Speed: $v^2 = (\text{N})(\text{m})/\text{kg} = (\text{kg m s}^{-2})(\text{m})/\text{kg} = \text{m}^2\text{s}^{-2}$, so $v$ in m s⁻¹. Consistent.

## Key Insight

There is no separate "centripetal force": the inward horizontal component of the tension *is* the centripetal force, while the vertical component balances the weight. Resolving the single tension into two perpendicular directions solves the whole problem.

## Common Mistakes

- [[Treating-Centripetal-Force-as-an-Extra-Force]]
- Using the string length instead of the circle radius $L\sin\theta$.
- Forgetting that there is no vertical acceleration, so the vertical forces balance.

## Related Problem Types

- [[Circular-Motion-Problem]]
