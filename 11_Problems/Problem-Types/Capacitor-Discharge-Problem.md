---
type: problem-type
subject: physics
tags:
  - problem-solving
  - capacitors
  - electricity
level: a-level
difficulty: 2
status: usable
aliases:
  - Capacitor Discharge Calculation
  - RC Discharge Problem
  - Exponential Decay of Charge
sources: []
---

# Capacitor Discharge Problem

## Problem Signal

A charged capacitor discharges (or charges) through a resistor, and the question asks for the charge, voltage, or current after a given time, the time constant, or the half-time. Trigger phrases: "capacitor discharges through a resistor", "time constant", "RC circuit", "voltage falls to 37%", "how long until the charge halves".

## Required Quantities

- [[Charge]]
- [[Capacitance]]
- [[Potential-Difference]]

## Required Concepts

- Exponential decay
- Time constant $\tau = RC$

## Required Laws or Results

- [[Capacitor-Discharge-Equation]]: $Q = Q_0 e^{-t/RC}$
- $V = V_0 e^{-t/RC}$, $I = I_0 e^{-t/RC}$

## Required Methods

- [[Finding-Gradient-from-a-Graph]]

## Standard Approach

1. Identify $R$, $C$ and the initial value ($Q_0$, $V_0$ or $I_0$).
2. Compute the time constant $\tau = RC$ (units: seconds).
3. Apply the relevant exponential: $Q = Q_0 e^{-t/RC}$ (same form for $V$ and $I$).
4. To find a time, rearrange with natural logarithms: $t = -RC\ln(Q/Q_0)$.
5. For the half-time, use $t_{1/2} = RC\ln 2 \approx 0.69\,RC$.
6. Substitute consistently in SI units and state the answer with units.

## Variations

- Log-linear graph: $\ln Q$ against $t$ is a straight line with gradient $-1/RC$.
- Charging case: $V = V_0(1 - e^{-t/RC})$ rises toward the supply voltage.
- Energy stored: $E = \tfrac{1}{2}CV^2$ before and after, to find energy dissipated.

## Common Traps

- Forgetting that after one time constant the quantity falls to $1/e \approx 37\%$, not zero.
- Mixing microfarads/microcoulombs with base SI units.
- Using $\log_{10}$ instead of $\ln$ when rearranging.
- Assuming linear decay instead of exponential.

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
