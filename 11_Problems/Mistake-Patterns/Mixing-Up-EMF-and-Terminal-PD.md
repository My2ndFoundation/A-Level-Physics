---
type: mistake-pattern
subject: physics
tags:
  - mistake-pattern
  - electricity
  - electric-circuits
  - a-level-core
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - EMF vs Terminal PD
  - Confusing EMF and Terminal Voltage
sources: []
---

# Mixing Up EMF and Terminal PD

## Mistake

Treating the [[Electromotive-Force]] of a cell as the same as the voltage
measured across its terminals when current is flowing.

## Why It Happens

For an ideal cell with no [[Internal-Resistance]] they *are* equal, and many
early problems assume this. Students then carry the assumption into questions
where internal resistance matters.

## Example

A 1.5 V cell with internal resistance 0.5 Ω drives 2 A through an external
circuit. A student writes the terminal voltage as 1.5 V. Correctly, the cell
loses I·r = 2 × 0.5 = 1.0 V internally, so the terminal pd is only
1.5 − 1.0 = 0.5 V. Using 1.5 V overestimates the power delivered to the load.

## Correct Approach

Use ε = I(R + r), so terminal pd V = ε − I·r. The EMF is the total energy per
coulomb supplied; the terminal pd is what is left for the external circuit
after the internal "lost volts".

## Foundation Link

It builds on the basic idea that a real battery is not a perfect, lossless
source of voltage.

## Related Quantities

- [[Electromotive-Force]]
- [[Internal-Resistance]]

## Related Concepts

- [[Internal-Resistance]]

## Related Methods

- Applying ε = I(R + r) and finding "lost volts" I·r

## Related Problem Types

- Determining internal resistance from a terminal-pd vs current graph

## Source Trace

OpenStax College Physics; HyperPhysics; The Physics Classroom — no copied text.

OCR alignment: [[OCR-Physics-A-H556-Specification]]
