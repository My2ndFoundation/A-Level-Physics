---
type: method
subject: physics
tags:
  - electricity
  - electric-circuits
  - circuits
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - reading circuit diagrams
  - circuit analysis method
sources: []
---

# Analysing Circuit Diagrams

## Purpose

This method works out currents, potential differences, and power in a circuit by reading its diagram, identifying series and parallel sections, and applying the circuit laws systematically.

## When to Use

Use it for any circuit problem: combinations of resistors, finding the reading of an ammeter or voltmeter, comparing brightness of lamps, or analysing sensor circuits.

## Prerequisites

- [[Ohms-Law]]
- [[Kirchhoffs-First-Law]]
- [[Kirchhoffs-Second-Law]]

## Method

1. Identify the source (emf), and whether [[Internal-Resistance]] must be included.
2. Mark which components are in series (same current) and which are in parallel (same p.d.).
3. Reduce resistor networks: series add directly; parallel combine as $1/R_\text{total} = \Sigma(1/R)$.
4. Find the total current from the source using $I = \varepsilon / R_\text{total}$ (or $\varepsilon/(R+r)$).
5. Work back through the network using [[Ohms-Law]] and [[Kirchhoffs-First-Law]] to find branch currents and p.d.s.
6. Check: sum of p.d.s around any loop equals the emf ([[Kirchhoffs-Second-Law]]).

## Worked Example

A 6.0 V supply (no internal resistance) drives a 4.0 Ω and 2.0 Ω resistor in series. Total resistance = 6.0 Ω, so current $= 6.0 / 6.0 = 1.0 \text{ A}$. P.d. across the 4.0 Ω resistor $= 1.0 \times 4.0 = 4.0 \text{ V}$; across the 2.0 Ω resistor = 2.0 V; these sum to the 6.0 V supply, as required.

## Why It Works

Charge conservation gives [[Kirchhoffs-First-Law]] at junctions, and energy conservation gives [[Kirchhoffs-Second-Law]] around loops. Together with [[Ohms-Law]] for each component, these fully determine a circuit.

## Common Mistakes

- Treating a parallel pair as if in series (or vice versa).
- Ignoring internal resistance when it matters.
- Assuming current is "used up" round a series loop.

## Related Quantities

- Current, potential difference, resistance

## Related Laws or Results

- [[Ohms-Law]]
- [[Kirchhoffs-First-Law]]
- [[Kirchhoffs-Second-Law]]

## Related Problem Types

- [[Using-Kirchhoffs-Laws]]
- Resistor-network problems

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
