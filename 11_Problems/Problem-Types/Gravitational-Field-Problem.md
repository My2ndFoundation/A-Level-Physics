---
type: problem-type
subject: physics
tags:
  - problem-solving
  - fields
  - gravitational-fields
level: a-level
difficulty: 2
status: usable
aliases:
  - Gravitational Field Calculation
  - Orbit and Gravitation Problem
  - Newtonian Gravity Problem
sources: []
---

# Gravitational Field Problem

## Problem Signal

Two masses (planet–satellite, star–planet, Earth–object) interact gravitationally, and the question asks for the gravitational force, field strength, potential, orbital speed, orbital period, or escape velocity. Trigger phrases: "gravitational field strength", "satellite in orbit", "geostationary", "escape velocity", "gravitational potential energy at a distance".

## Required Quantities

- [[Force]]
- [[Gravitational-Field-Strength]]
- [[Speed]]

## Required Concepts

- Inverse-square field of a point/spherical mass
- Orbital motion as gravity providing centripetal force

## Required Laws or Results

- [[Newtons-Law-of-Gravitation]]: $F = \dfrac{GMm}{r^2}$
- $g = \dfrac{GM}{r^2}$, $V = -\dfrac{GM}{r}$

## Required Methods

- [[Solving-Circular-Motion-Problems]]

## Standard Approach

1. Identify the central mass $M$ and the separation $r$ (measured from centre, not surface).
2. For force or field, apply $F = \dfrac{GMm}{r^2}$ or $g = \dfrac{GM}{r^2}$.
3. For an orbit, set gravity equal to the centripetal requirement: $\dfrac{GMm}{r^2} = \dfrac{mv^2}{r}$, giving $v = \sqrt{GM/r}$.
4. Relate orbital speed and period via $v = \dfrac{2\pi r}{T}$, leading to Kepler's third law $T^2 \propto r^3$.
5. For energy, use $E_p = -\dfrac{GMm}{r}$ and combine with kinetic energy for escape conditions.
6. Substitute SI units and check the sign/magnitude of potential and energy.

## Variations

- Geostationary orbit: $T = 24\ \text{h}$ fixes $r$ via Kepler's third law.
- Escape velocity: set total energy to zero, $v_{esc} = \sqrt{2GM/r}$.
- Comparing surface gravity on different planets using $g = GM/R^2$.

## Common Traps

- Measuring $r$ from the surface instead of the centre of the planet.
- Forgetting gravitational potential and potential energy are negative.
- Confusing $g$ (field strength, N kg⁻¹) with $G$ (gravitational constant).
- [[Forgetting-Vector-Direction]]

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
