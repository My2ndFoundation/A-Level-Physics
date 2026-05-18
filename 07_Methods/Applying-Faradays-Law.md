---
type: method
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
  - Applying Faraday's Law
  - Applying Faradays Law
  - Calculating Induced EMF
sources: []
---

# Applying Faradays Law

## Purpose

To calculate the magnitude and direction of an induced e.m.f. (or induced [[Current]]) when the magnetic flux linkage through a coil or conductor changes.

## When to Use

- A magnet moves relative to a coil, or a coil moves into/out of a field.
- A conductor moves through a field and "cuts" field lines.
- A coil rotates in a magnetic field (a.c. generator).
- The current — and hence field — in a nearby coil changes (transformer-type problems).

## Prerequisites

- [[Faradays-Law]]
- [[Lenzs-Law]]
- [[Magnetic-Flux]]
- [[Magnetic-Flux-Linkage]]

## Method

1. Identify the coil/conductor and the quantity that changes: [[Magnetic-Flux-Density]] B, area A, angle θ, or number of turns N.
2. Write the flux linkage: NΦ = B A N cos θ.
3. Find the rate of change: differentiate with respect to time, or use Δ(NΦ)/Δt for an average over a time interval.
4. Take the magnitude for the size of the e.m.f.: |ε| = |d(NΦ)/dt|.
5. Apply [[Lenzs-Law]] to state the direction (the induced current opposes the change in flux).
6. If a closed circuit of [[Resistance]] R is given, find induced current I = ε / R.

## Worked Example

A coil of 200 turns and area 4.0 × 10⁻³ m² sits perpendicular to a field that falls uniformly from 0.50 T to 0 in 0.10 s. Change in flux linkage = N·A·ΔB = 200 × 4.0 × 10⁻³ × 0.50 = 0.40 Wb. Induced e.m.f. = 0.40 / 0.10 = 4.0 V. Direction: by Lenz's law it opposes the decrease, so the induced current acts to maintain the original flux.

## Why It Works

The induced e.m.f. arises because moving charges in the conductor experience [[Force-on-a-Moving-Charge]], or equivalently because changing flux linkage stores/releases energy; Faraday's law quantifies the rate, and Lenz's law fixes the direction so [[Conservation-of-Energy]] holds.

## Common Mistakes

- Using flux Φ instead of flux linkage NΦ (omitting N).
- Finding total flux change but forgetting to divide by the time interval.
- Forgetting cos θ when the coil is not perpendicular to the field.
- Stating no direction (Lenz's law) when the question asks for it.

## Related Quantities

- [[Magnetic-Flux-Linkage]]
- [[Potential-Difference]]
- [[Magnetic-Flux-Density]]

## Related Laws or Results

- [[Faradays-Law]]
- [[Lenzs-Law]]

## Related Problem Types

- [[Electromagnetic-Induction]]

## Source Trace

OpenStax College Physics; HyperPhysics; Physics LibreTexts — no copied text.

OCR alignment: [[OCR-Physics-A-H556-Specification]]

- Source: public physics reference pool
- Section/Page: OCR M6.3 Electromagnetism
