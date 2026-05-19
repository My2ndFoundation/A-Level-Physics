---
type: physical-quantity
subject: physics
tags:
  - electric-fields
  - fields
  - a-level-core
level: a-level
difficulty: 3
status: usable
aliases:
  - Electric Potential
  - Absolute Potential
sources: []
---

# Electric Potential

## Core Idea

Electric potential is the electric potential energy per unit positive charge at a point in an [[Electric-Field]], measured relative to infinity.

## Symbol

- V

## SI Unit

- volt (V), equal to J C⁻¹.

## Scalar or Vector

- Scalar (unlike [[Electric-Field-Strength]], which is a vector).

## Definition

The electric potential at a point is the work done per unit positive charge in bringing a small test charge from infinity to that point:

- V = W / Q
  - V = electric potential, volts (V)
  - W = work done from infinity, joules (J)
  - Q = test charge, coulombs (C)

For an isolated point charge Q, the potential at distance r is:

- V = (1 / 4πε₀) · Q / r

Potential is positive near a positive charge and negative near a negative charge, and tends to zero at infinity. Note the 1/r dependence, in contrast to the 1/r² dependence of field strength.

## Related Equations

- E_p = QV (links to [[Electric-Potential-Energy]])
- W = QΔV (work done moving charge Q through potential difference ΔV)
- E = −ΔV/Δr (field strength is the negative potential gradient)
- For a [[Uniform-Electric-Field]]: V = E d

## How It Is Measured

Absolute potential is usually calculated, not measured directly. Practically, only potential **differences** are measured, with a voltmeter between two points. The zero reference is taken at infinity in field theory, or at earth/0 V in circuits.

## Graphical Meaning

On a graph of V against r for a point charge, the curve is a 1/r hyperbola. The gradient of the V–r graph gives −E (field strength is the negative potential gradient). The area under an E–r graph between two radii gives the potential difference between them.

## Foundation Links

- [[Energy-Quantity|Energy]]
- [[Potential-Difference]]
- [[Charge]]

## Related Concepts

- [[Electric-Field]]
- [[Electric-Potential-Energy]]
- [[Uniform-Electric-Field]]

## Related Laws or Results

- [[Coulombs-Law]]
- [[Newtons-Law-of-Gravitation]]

## Related Experiments

- [[Analysing-Capacitor-Charge-and-Discharge]]

## Frontier Links

- [[Semiconductor-Physics-Map]]

## Common Mistakes

- Confusing potential V (scalar, energy per charge) with field strength E (vector, force per charge).
- Forgetting the sign of V for negative charges.
- Using 1/r² for potential (that is the field/force law; potential goes as 1/r).

## Visuals

### Electric Potential vs Distance for a Point Charge

```mermaid
xychart-beta
  title "Electric potential V vs distance r from +Q"
  x-axis "Distance r / arbitrary units" [1, 2, 3, 4, 5, 6]
  y-axis "Potential V / arbitrary units" 0 --> 12
  line [12, 6, 4, 3, 2.4, 2]
```

*Figure: V ∝ 1/r for a point charge (hyperbola that approaches zero at infinity). Compare with field strength E ∝ 1/r² which falls off faster. The gradient of this V–r curve at any point gives −E (field strength is the negative potential gradient).*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; Physics LibreTexts — no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (M6.2)
