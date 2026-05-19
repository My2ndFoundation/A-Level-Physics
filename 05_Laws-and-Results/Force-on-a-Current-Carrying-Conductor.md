---
type: law-result
subject: physics
tags:
  - magnetic-fields
  - electromagnetism
  - fields
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Force on a Current-Carrying Conductor
  - Motor Effect
  - F = BIL
  - BIL Force
sources: []
---

# Force on a Current-Carrying Conductor

## Statement

A conductor carrying a [[Current]] in a magnetic field experiences a force. This is the motor effect. The force is greatest when the current is perpendicular to the field and zero when the current is parallel to it.

## Equation

$$F = B I L \sin\theta$$

For a conductor perpendicular to the field ($\theta = 90^\circ$): $F = B I L$

## Symbols and Units

- Symbol: F — Meaning: force on the conductor — Unit: newton (N)
- Symbol: B — Meaning: [[Magnetic-Flux-Density]] — Unit: tesla (T)
- Symbol: I — Meaning: current in the conductor — Unit: ampere (A)
- Symbol: L — Meaning: length of conductor in the field — Unit: metre (m)
- Symbol: θ — Meaning: angle between current direction and field — Unit: degree or radian

## Conditions

- The conductor lies within the magnetic field of flux density B.
- B is uniform over the length L (or B and L are taken as effective averages).
- θ is the angle between the current and the field; the force vanishes when they are parallel.

## Physical Meaning

Moving charges in the wire each feel a magnetic force ([[Force-on-a-Moving-Charge]]); summed over all carriers in length L this gives the bulk force $F = BIL \sin\theta$. The force direction is perpendicular to both the current and the field, given by Fleming's left-hand rule (thumb = thrust/force, first finger = field, second finger = current). This force converts electrical energy into mechanical motion, the basis of every electric motor.

## Foundation Link

Builds on the GCSE observation that a current-carrying wire between magnet poles jumps when switched on (the motor effect), now made quantitative.

## How to Use

Identify B, I, and L; resolve for the angle θ if the wire is not perpendicular to the field; apply $F = BIL \sin\theta$; use Fleming's left-hand rule for direction.

## Derivation or Explanation

A single charge q drifting at speed v feels force $F = Bqv \sin\theta$. In length L there are $nAL$ carriers (n = number density, A = cross-section). Total force $= (nAL)(Bqv \sin\theta)$. Since current $I = nAvq$, this simplifies to $F = BIL \sin\theta$.

## Related Quantities

- [[Magnetic-Flux-Density]]
- [[Current]]
- [[Force]]

## Related Models

- [[Magnetic-Field]]

## Applications

- [[The-DC-Motor]]

## Frontier Links

- The same force, scaled up, steers and focuses charged beams in particle accelerators.

## Common Mistakes

- Forgetting the sin θ factor when the wire is not perpendicular to the field.
- Using Fleming's *right*-hand rule (that is for induced current/generators).
- Confusing this law with [[Force-on-a-Moving-Charge]] (use $F = BIL$ for wires, $F = Bqv$ for single charges).

## Visuals

### Motor-effect force diagram (F = BIL)

![[_attachments/05_Laws-and-Results/force-on-a-current-carrying-conductor--fleming-lhr.svg]]
*Figure: A horizontal wire carrying current I in a field B directed into the page experiences an upward force F = BIL. Fleming's left-hand rule gives the force direction.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

OpenStax College Physics; HyperPhysics; Physics LibreTexts — no copied text.

OCR alignment: [[OCR-Physics-A-H556-Specification]]

- Source: public physics reference pool
- Section/Page: OCR M6.3 Electromagnetism
