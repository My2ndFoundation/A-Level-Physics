---
type: problem-type
subject: physics
tags:
  - problem-solving
  - circular-motion
  - newtonian-world
level: a-level
difficulty: 2
status: usable
aliases:
  - Circular Motion Calculation
  - Centripetal Force Problem
  - Uniform Circular Motion Problem
sources: []
---

# Circular Motion Problem

## Problem Signal

A body moves in a circular path at constant speed and the question involves the centripetal force or acceleration, period, or the maximum speed before something fails (string snaps, car skids, contact lost). Trigger phrases: "circular path", "centripetal", "swung in a circle", "car on a bend", "satellite orbit", "loop the loop", "conical pendulum".

## Required Quantities

- [[Speed]]
- [[Force]]
- [[Acceleration]]

## Required Concepts

- Centripetal acceleration directed toward the centre
- Angular speed $\omega = 2\pi/T$

## Required Laws or Results

- $a = \dfrac{v^2}{r} = \omega^2 r$
- $F = \dfrac{mv^2}{r} = m\omega^2 r$

## Required Methods

- [[Solving-Circular-Motion-Problems]]
- [[Resolving-Forces]]

## Standard Approach

1. Identify what physical force provides the centripetal force (tension, gravity, friction, normal contact, or a combination).
2. Draw a free-body diagram and resolve forces toward the centre of the circle.
3. Set the net inward force equal to $\dfrac{mv^2}{r}$.
4. Relate $v$ and $\omega$ via $v = \omega r$ and $\omega = 2\pi f = 2\pi/T$ if periods are involved.
5. Solve for the unknown (speed, tension, radius, or period).
6. For "maximum/minimum" cases, apply the limiting condition (e.g. tension or normal force just reaches zero).

## Variations

- Vertical circle: tension/contact varies; minimum speed at the top where gravity alone supplies the centripetal force.
- Conical pendulum: resolve tension into vertical (balances weight) and horizontal (centripetal) components.
- Car on a banked or flat curve: friction and/or the banking component supplies the centripetal force.

## Common Traps

- Treating centripetal force as an extra "outward" force — it is the resultant of real forces, inward.
- Forgetting that speed is constant but velocity (direction) changes, so there is acceleration.
- [[Treating-Centripetal-Force-as-an-Extra-Force]]
- Mixing $v$ and $\omega$ without converting.

## Visuals

### Conical Pendulum — Force Resolution Setup

![[_attachments/11_Problems/Circular-Motion-Problem--conical-pendulum-setup.svg]]

*Figure: A conical pendulum of mass m with string at angle θ from the vertical. Tension T is resolved into a vertical component T cosθ (which balances weight mg) and a horizontal component T sinθ (which provides the centripetal force mv²/r toward the pivot axis). The radius of the circular orbit r is the horizontal distance from the axis to the ball. This geometry applies directly to the "conical pendulum" variation listed in the Standard Approach.*

*Source: Authored for this vault (CC0). No external copyright.*

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
