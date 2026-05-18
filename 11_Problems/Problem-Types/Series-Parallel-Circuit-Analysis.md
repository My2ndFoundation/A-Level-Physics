---
type: problem-type
subject: physics
tags:
  - problem-solving
  - electricity
  - electric-circuits
  - resistance
level: a-level
difficulty: 2
status: usable
aliases:
  - Circuit Analysis Problem
  - Series and Parallel Resistor Problem
  - Combined Circuit Calculation
sources: []
---

# Series Parallel Circuit Analysis

## Problem Signal

A circuit contains several resistors in a mix of series and parallel branches, and the question asks for total resistance, the current through or voltage across a particular component, or power dissipated. Trigger phrases: "total resistance of the network", "current in the 4 Ω resistor", "voltage across the parallel section", "power dissipated by R".

## Required Quantities

- [[Resistance]]
- [[Current]]
- [[Potential-Difference]]

## Required Concepts

- Series and parallel combination rules

## Required Laws or Results

- Series: $R_T = R_1 + R_2 + \dots$
- Parallel: $\dfrac{1}{R_T} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dots$
- Ohm's law $V = IR$

## Required Methods

- [[Using-Kirchhoffs-Laws]]

## Standard Approach

1. Redraw the circuit clearly, labelling each resistor and node.
2. Reduce parallel groups to single equivalent resistors, then combine in series step by step.
3. Find the total current from the supply using $I = V / R_T$.
4. Work back outwards: the same current flows through series elements; voltage divides across them.
5. For parallel branches, the voltage is shared equally across the branch and current splits inversely with resistance.
6. Compute the requested quantity and check with Kirchhoff's laws (currents at a node sum to zero; voltages around a loop sum to zero).

## Variations

- Multiple supplies or branches: apply Kirchhoff's laws directly with simultaneous equations.
- Internal resistance included as an extra series resistor.
- Power questions: $P = I^2R = V^2/R$ for the chosen component.

## Common Traps

- [[Mixing-Up-Series-and-Parallel-Circuits]]
- Adding parallel resistances directly instead of using reciprocals.
- Assuming current is the same everywhere in a parallel network.
- Forgetting that adding a parallel resistor *decreases* total resistance.

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
