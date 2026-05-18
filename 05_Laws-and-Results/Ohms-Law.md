---
type: law-result
subject: physics
tags:
  - electricity
  - electric-circuits
  - resistance
  - ocr-h556
  - a-level-physics
level: a-level
difficulty: 1
status: usable
aliases:
  - Ohm's law
  - V = IR
  - V=IR
  - ohmic relationship
sources: []
---

# Ohms Law

## Statement

For a metallic conductor at constant temperature, the current through it is directly proportional to the potential difference across it. The ratio of potential difference to current is constant and equals the resistance.

## Equation

`V = IR`

## Symbols and Units

- `V`: potential difference across the component, volts `V` (scalar)
- `I`: current through the component, amperes `A` (scalar)
- `R`: resistance, ohms `Ω` (scalar)

## Conditions

- Strictly valid only for an **ohmic conductor at constant temperature**.
- A filament lamp, thermistor, and diode are **non-ohmic**: their `I–V` graphs are not straight lines, though `V = IR` still *defines* resistance at any point.
- Temperature must be constant, since resistance of a metal rises with temperature.

## Physical Meaning

Ohm's law says a metal offers a constant opposition to current flow as long as it does not heat up. On an `I–V` graph for an ohmic conductor, the line is straight through the origin, and `1/gradient` gives the resistance. For non-ohmic devices the law does not hold, but `R = V/I` can still be evaluated at each operating point.

## Foundation Link

GCSE introduces `V = IR` and ohmic vs non-ohmic `I–V` graphs (resistor, filament lamp, diode). A-Level adds resistivity, temperature dependence, and a clear distinction between Ohm's *law* (a proportionality that only some components obey) and the *definition* of resistance `R = V/I` (which always applies).

## How to Use

1. Identify two of the three quantities `V`, `I`, `R`.
2. Rearrange `V = IR` for the unknown.
3. For combined resistors, find total resistance first (series: add; parallel: reciprocals).
4. Use [[Kirchhoffs-Second-Law]] to apply it around a loop.

## Derivation or Explanation

From the drift model, `I = nAvq`; for a metal `n` and the scattering rate are roughly constant at fixed temperature, giving a constant `V/I` ratio.

## Related Quantities

- [[Potential-Difference]]
- [[Current]]
- [[Resistance]]
- [[Charge]]

## Related Models

- [[Ohmic-Conductor-Model]]

## Applications

- Designing resistor networks and current-limiting circuits
- Sensor circuits using thermistors and LDRs
- [[Kirchhoffs-Second-Law]] loop analysis

## Frontier Links

- [[Quantum-Mechanics-Map]] — superconductivity is a quantum effect where resistance drops to zero, defying ordinary resistive behaviour.

## Common Mistakes

- Applying Ohm's law to non-ohmic components as if `R` were constant
- Confusing the *law* with the *definition* `R = V/I`
- Ignoring the temperature-constant condition

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; Physics LibreTexts — paraphrased, no copied text
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
