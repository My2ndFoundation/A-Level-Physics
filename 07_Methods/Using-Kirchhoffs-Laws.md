---
type: method
subject: physics
tags:
  - electricity
  - electric-circuits
  - circuits
  - ocr-h556
level: a-level
difficulty: 3
status: usable
aliases:
  - Kirchhoff's laws method
  - applying Kirchhoff's rules
sources: []
---

# Using Kirchhoffs Laws

## Purpose

This method sets up and solves simultaneous equations for unknown currents and potential differences in circuits too complex for simple series/parallel reduction, using [[Kirchhoffs-First-Law]] (junctions) and [[Kirchhoffs-Second-Law]] (loops).

## When to Use

Use it for multi-loop circuits, circuits with more than one source, or networks where resistors are not in simple series/parallel arrangements.

## Prerequisites

- [[Kirchhoffs-First-Law]]
- [[Kirchhoffs-Second-Law]]
- [[Ohms-Law]]

## Method

1. Label every branch current with a symbol and an assumed direction.
2. Apply [[Kirchhoffs-First-Law]] at junctions: total current in = total current out.
3. Choose independent loops and assign a direction to travel each.
4. Apply [[Kirchhoffs-Second-Law]] around each loop: sum of emfs = sum of *IR* p.d.s, watching signs (gain across a source, drop across a resistor with the current).
5. Solve the resulting simultaneous equations.
6. A negative current means the real direction is opposite to the assumed one.

## Worked Example

Two cells of emf 6.0 V and 2.0 V drive current through a shared 4.0 Ω resistor. Suppose the first law gives the resistor current as the sum of two branch currents, and the loop equations give 6.0 = 4.0 I₁ + ... Solving the simultaneous set yields each branch current; a negative value simply reverses that branch's assumed direction.

## Why It Works

[[Kirchhoffs-First-Law]] is conservation of charge; no charge accumulates at a junction. [[Kirchhoffs-Second-Law]] is conservation of energy; the total energy gained per coulomb from sources equals the total dissipated round any closed loop.

## Common Mistakes

- Sign errors traversing a loop (source vs resistor).
- Choosing non-independent loops.
- Forgetting internal resistance of cells.

## Related Quantities

- Current, emf, potential difference

## Related Laws or Results

- [[Kirchhoffs-First-Law]]
- [[Kirchhoffs-Second-Law]]
- [[Ohms-Law]]

## Related Problem Types

- [[Analysing-Circuit-Diagrams]]
- Multi-loop circuit problems

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
