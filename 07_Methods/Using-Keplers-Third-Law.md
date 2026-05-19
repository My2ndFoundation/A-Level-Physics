---
type: method
subject: physics
tags:
  - gravitational-fields
  - newtonian-world
  - astrophysics
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Applying Kepler's Third Law
  - T squared r cubed method
sources: []
---

# Using Kepler's Third Law

## Purpose

To find an unknown orbital quantity — period, radius, central mass or orbital
speed — for a body in a circular orbit, using the relationship

$$T^2 = \frac{4\pi^2}{GM} r^3$$

## When to Use

- A satellite, moon or planet moves in an (approximately) circular orbit.
- You are given two of {period, radius, central mass} and asked for the third.
- You need the mass of a planet/star from one of its satellites.
- You must check or design a geostationary orbit.

## Prerequisites

- [[Keplers-Third-Law]]
- [[Newtons-Law-of-Gravitation]]
- [[Circular-Motion]]
- [[Centripetal-Force]]

## Method

1. Identify the central mass M and confirm a roughly circular orbit.
2. Write the orbital condition: $GMm/r^2 = mv^2/r$, or equivalently $m\omega^2 r$ with
   $\omega = 2\pi/T$.
3. Substitute $v = 2\pi r/T$ and rearrange to $T^2 = \dfrac{4\pi^2}{GM} r^3$.
4. Insert known values in SI units (T in s, r in m measured from the
   central body's centre).
5. Solve for the unknown. For two orbits of the same central body, use the
   ratio $T_1^2/r_1^3 = T_2^2/r_2^3$ so G and M cancel.
6. Convert results to required units and check orders of magnitude.

## Worked Example

For a geostationary orbit, $T = 24 \text{ h} = 8.64 \times 10^4 \text{ s}$ and
$M_\text{Earth} \approx 5.97 \times 10^{24} \text{ kg}$. Then $r^3 = GMT^2/4\pi^2$
gives $r \approx 4.2 \times 10^7 \text{ m}$, so the satellite is about
3.6 × 10⁷ m above the surface. (See [[Satellites-and-Geostationary-Orbits]].)

## Why It Works

Gravity provides exactly the centripetal force for the orbit. Equating the two
forces eliminates the orbiting mass and yields a fixed relation between period
and radius set only by the central mass.

## Common Mistakes

- Using orbital height instead of radius from the centre
- Time not in seconds, distance not in metres
- Forgetting the orbiting body's mass cancels

## Related Quantities

- [[Gravitational-Field-Strength]]
- [[Mass]]

## Related Laws or Results

- [[Keplers-Third-Law]]
- [[Newtons-Law-of-Gravitation]]

## Related Problem Types

- [[Satellites-and-Geostationary-Orbits]]

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; NASA educational material — no copied text
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
- Section/Page: OCR M5.4 Gravitational fields
