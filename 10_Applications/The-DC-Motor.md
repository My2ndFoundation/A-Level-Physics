---
type: application
subject: physics
tags:
  - electromagnetism
  - magnetic-fields
  - fields
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - The DC Motor
  - DC Motor
  - Electric Motor
sources: []
---

# The DC Motor

## Problem Context

A direct-current motor converts electrical energy into rotational mechanical energy using the force on a current-carrying coil in a magnetic field. It models how electric drills, fans, electric vehicles, and toys turn.

## Physical Ideas

- [[Force-on-a-Current-Carrying-Conductor]]
- [[Magnetic-Field]]
- [[Electromagnetic-Induction]]
- [[Lenzs-Law]]
- [[Conservation-of-Energy]]

## Mathematical Tools

- F = B I L sin θ (see [[Force-on-a-Current-Carrying-Conductor]])
- Torque = F × perpendicular distance (couple on the coil)

## Typical Questions

- Explain why the coil rotates and the function of the split-ring commutator.
- Calculate the force or turning effect on one side of the coil.
- Explain the role of back-e.m.f. and how it limits the [[Current]].
- State how to increase the motor's turning effect.

## Method Outline

1. A current flows through a coil placed between the poles of a magnet.
2. By [[Force-on-a-Current-Carrying-Conductor]], opposite sides of the coil carry current in opposite directions, so they feel forces in opposite directions, producing a couple (torque) that turns the coil.
3. As the coil passes the vertical, the **split-ring commutator** reverses the current direction in the coil, so the torque keeps acting the same rotational way and rotation continues.
4. As the coil spins it cuts field lines and, by [[Electromagnetic-Induction]] and [[Lenzs-Law]], generates a back-e.m.f. opposing the supply. The net driving voltage is (supply − back-e.m.f.), which limits the current and rises as the motor speeds up.
5. Turning effect is increased by a stronger field, more current, more turns, or a larger coil area.

## Assumptions

- Uniform field across the coil; negligible friction and coil resistance in idealised analysis.
- Steady d.c. supply with an ideal commutator switching instantaneously.

## Links to Other Subjects

- Mathematics: torque and couples; trigonometric variation of torque with coil angle.
- Computer Science: pulse-width modulation controls motor speed in robotics.

## Frontier Links

- Brushless d.c. and induction motors used in electric vehicles replace the mechanical commutator with electronic switching.

## Common Mistakes

- Forgetting the commutator's role, so predicting the coil oscillates instead of rotating continuously.
- Ignoring back-e.m.f. when explaining why current falls as speed rises.
- Using Fleming's right-hand rule (that is for generators) instead of the left-hand rule.

## Visuals

### Basic Principle of a DC Electric Motor
![[_attachments/10_Applications/The-DC-Motor--motor-diagram.png]]
*Figure: Schematic of a simple DC motor showing a rectangular coil between magnetic poles. The forces on the two sides carrying current in opposite directions produce a couple (torque), turning the coil. The split-ring commutator (not shown) reverses the current each half-turn to maintain continuous rotation.*
*Source: Basic principle of an Electric motor — K.Venkataramana — CC BY-SA 4.0 — https://commons.wikimedia.org/wiki/File:Basic_principle_of_an_Electric_motor.png. Retrieved 2026-05-19.*

## Source Trace

OpenStax College Physics; HyperPhysics; Physics LibreTexts — no copied text.

OCR alignment: [[OCR-Physics-A-H556-Specification]]

- Source: public physics reference pool
- Section/Page: OCR M6.3 Electromagnetism
