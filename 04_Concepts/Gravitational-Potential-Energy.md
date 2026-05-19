---
type: concept
subject: physics
tags:
  - gravitational-fields
  - newtonian-world
  - a-level-core
  - energy
level: a-level
difficulty: 2
status: usable
aliases:
  - GPE
  - Gravitational PE
sources: []
---

# Gravitational Potential Energy

## Core Idea

Gravitational potential energy is the energy a mass has because of its
position in a gravitational field. Moving a mass away from the body that
produces the field requires work, which is stored as potential energy.

## Meaning

At A-Level there are two complementary expressions for gravitational
potential energy (GPE).

**Near a surface (uniform field):**

$$\Delta E_p = m g \Delta h$$

valid only when g is approximately constant and $\Delta h$ is small compared with the
distance to the planet's centre. Symbols: m = mass (kg), g = field strength
(N kg⁻¹), $\Delta h$ = change in height (m), $\Delta E_p$ in joules (J).

**General radial field (point mass / outside a sphere):**

$$E_p = -\frac{G M m}{r}$$

where $G = 6.67 \times 10^{-11}$ N m² kg⁻², M = source mass (kg), m = the mass placed
in the field (kg), r = separation of centres (m).

The minus sign is essential. The zero of potential energy is taken at
**infinite separation**, where the masses no longer interact. Any finite
separation has *less* energy than this, so $E_p$ is negative — the masses are
"bound". GPE per unit mass is the [[Gravitational-Potential]]:
$E_p = m \times V_\text{grav}$.

## Everyday Intuition

Lifting a bag onto a shelf stores energy you get back if it falls. Sending a
rocket "uphill" away from Earth needs energy; the deeper in the well it
starts, the more energy escape requires.

## GCSE Foundation

- [[Weight]]
- [[Mass]]
- [[Conservation-of-Energy]]

GCSE uses only $E_p = m g h$. A-Level adds the negative inverse-r form and the
idea that the reference point is infinity, not the ground.

## Why It Matters

GPE underlies escape velocity, orbital energy, satellite transfers and energy
conservation in any gravitational problem. Combined with kinetic energy it
explains why orbiting bodies have a fixed total mechanical energy.

## Related Quantities

- [[Gravitational-Potential]]
- [[Gravitational-Field-Strength]]
- [[Mass]]
- [[Weight]]

## Related Laws or Results

- [[Newtons-Law-of-Gravitation]]
- [[Conservation-of-Energy]]

## Related Models

- [[Orbital-Motion]]

## Representations

- Potential well diagram: E_p against r curving up to zero from below
- Gradient of the E_p–r graph gives gravitational force

## Experiments or Observations

- Energy analysis of projectile and satellite motion
- Spacecraft escape-energy calculations

## Applications

- [[Satellites-and-Geostationary-Orbits]]
- [[Orbital-Motion]]

## Frontier Links

- [[Cosmology-Map]]

## Common Mistakes

- Dropping the minus sign in $E_p = -GMm/r$
- Using m g h over large distances where g is not constant
- Confusing E_p (J) with [[Gravitational-Potential]] (J kg⁻¹)
- Thinking GPE is zero at the surface rather than at infinity

## Visuals

### Gravitational potential energy well (E_p vs r)
```mermaid
xychart-beta
  title "E_p = −GMm/r: potential well deepens toward the source mass"
  x-axis "Distance from centre r (relative units)" [1, 2, 3, 4, 5, 6, 7, 8]
  y-axis "E_p (relative units, negative)" -8 --> 0
  line [-8.0, -4.0, -2.67, -2.0, -1.6, -1.33, -1.14, -1.0]
```
*Figure: E_p is always negative (bound system) and rises toward zero at infinite separation. The steep well near the source shows that more energy is needed to escape from a close orbit than a distant one.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; NASA educational material — no copied text
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
- Section/Page: OCR M5.4 Gravitational fields
