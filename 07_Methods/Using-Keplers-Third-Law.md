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
T² = (4π²/GM) r³.

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
2. Write the orbital condition: GMm/r² = mv²/r, or equivalently mω²r with
   ω = 2π/T.
3. Substitute v = 2πr/T and rearrange to T² = (4π²/GM) r³.
4. Insert known values in SI units (T in s, r in m measured from the
   central body's centre).
5. Solve for the unknown. For two orbits of the same central body, use the
   ratio T₁²/r₁³ = T₂²/r₂³ so G and M cancel.
6. Convert results to required units and check orders of magnitude.

## Worked Example

For a geostationary orbit, T = 24 h = 8.64 × 10⁴ s and M_Earth ≈ 5.97 × 10²⁴
kg. Then r³ = GMT²/4π² gives r ≈ 4.2 × 10⁷ m, so the satellite is about
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
