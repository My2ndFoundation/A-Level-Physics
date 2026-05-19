---
type: physical-quantity
subject: physics
tags:
  - electricity
  - electric-circuits
  - resistance
  - materials
  - ocr-h556
  - a-level-physics
level: a-level
difficulty: 3
status: usable
aliases:
  - rho
  - "ρ"
  - electrical resistivity
  - specific resistance
sources: []
---

# Resistivity

## Core Idea

Resistivity is a material property that tells you how strongly a substance opposes current, independent of the size or shape of the sample. Copper has a low resistivity (good conductor); rubber has an enormous one (insulator). It is to resistance what density is to mass: the intrinsic, sample-free measure.

## Symbol

`ρ` (Greek rho)

## SI Unit

`Ω m` (ohm metre). Copper ≈ 1.7 × 10⁻⁸ Ω m.

## Scalar or Vector

Scalar. Magnitude only; a positive material constant (temperature-dependent).

## Definition

Resistivity is the property of a material defined so that the resistance of a uniform sample equals resistivity times length divided by cross-sectional area.

## Related Equations

- $R = \rho L / A$ → $\rho = RA / L$ — `ρ` = resistivity (Ω m), `R` = resistance (Ω), `A` = cross-sectional area (m²), `L` = length (m).
- $A = \pi d^2/4$ for a wire of diameter `d`.
- Conductivity $\sigma = 1/\rho$ (S m⁻¹).

## How It Is Measured

Use a uniform wire: measure its resistance ($R = V/I$) for several lengths, its diameter with a micrometer (to get `A`). Plot `R` against `L`; the gradient is $\rho/A$, so $\rho =$ gradient $\times A$. This averages out random errors and gives a reliable value.

## Graphical Meaning

A graph of resistance against length (constant cross-section) is a straight line through the origin with gradient $\rho/A$. Multiplying the gradient by the measured area gives the resistivity.

## Foundation Links

- [[Energy-Quantity|Energy]] (GCSE-Foundations layer — conductors vs insulators)

## Related Concepts

- [[Resistance]]
- [[Current]]
- [[Density]]

## Related Laws or Results

- [[Ohms-Law]]

## Related Experiments

- Determining the resistivity of a metal wire

## Frontier Links

- [[Semiconductor-Physics-Map]] (resistivity of semiconductors and doping — orientation only)

## Common Mistakes

- Confusing resistivity (material property) with resistance (sample property)
- Forgetting to convert diameter to cross-sectional area
- Ignoring the temperature dependence of resistivity

## Visuals

```mermaid
flowchart LR
    rho["Resistivity ρ (Ω m)<br/>material property"]
    R["Resistance R = ρL/A (Ω)<br/>sample property"]
    L["Length L (m)"]
    A["Cross-section A = πd²/4 (m²)"]
    graph["R vs L graph<br/>gradient = ρ/A"]

    rho -->|"× L/A"| R
    L --> R
    A --> R
    R -->|"plot R vs L"| graph
    graph -->|"gradient × A"| rho
```
*Figure: Resistivity ρ is extracted by measuring R for several wire lengths L (constant cross-section A). The gradient of the R–L graph equals ρ/A, so ρ = gradient × A.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; HyperPhysics (paraphrased, no copied text)
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
