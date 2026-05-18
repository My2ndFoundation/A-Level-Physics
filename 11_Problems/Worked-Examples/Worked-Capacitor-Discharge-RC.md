---
type: worked-example
subject: physics
tags:
  - problem-solving
  - capacitors
  - electricity
level: a-level
difficulty: 2
status: usable
sources: []
---

# Worked Capacitor Discharge RC

## Problem

A $470\ \mu\text{F}$ capacitor is charged to $12\ \text{V}$ and then discharged through a $22\ \text{k}\Omega$ resistor. Find (a) the time constant, (b) the voltage across the capacitor $15\ \text{s}$ after discharge begins, and (c) the time taken for the voltage to fall to $3.0\ \text{V}$.

## Source Reference

- Source: Original worked example; pattern aligned to OCR H556.
- Page/Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]

## Required Quantities

- [[Charge]]
- [[Capacitance]]
- [[Potential-Difference]]

## Required Concepts

- Exponential decay; time constant

## Required Methods

- [[Finding-Gradient-from-a-Graph]]

## Solution

**(a) Time constant.**

$$\tau = RC = (22\times10^{3})(470\times10^{-6}) = 10.34\ \text{s}$$

**(b) Voltage after 15 s.** Using $V = V_0 e^{-t/RC}$:

$$V = 12 \times e^{-15/10.34} = 12 \times e^{-1.451} = 12 \times 0.234 = 2.8\ \text{V}$$

**(c) Time to reach 3.0 V.** Rearrange with natural logs:

$$\frac{V}{V_0} = e^{-t/RC} \implies t = -RC\,\ln\!\left(\frac{V}{V_0}\right)$$
$$t = -10.34 \times \ln\!\left(\frac{3.0}{12}\right) = -10.34 \times \ln(0.25) = -10.34 \times (-1.386) = 14.3\ \text{s}$$

## Unit Check

$\tau = RC = \Omega \times \text{F} = (\text{V A}^{-1})(\text{C V}^{-1}) = \text{C A}^{-1} = \text{s}$. The exponent $t/RC$ is dimensionless (s/s). Voltage stays in volts. Consistent.

## Key Insight

After one time constant ($\approx 10.3\ \text{s}$) the voltage falls to about $37\%$ of its initial value, not to zero. Solving for a time requires the natural logarithm, because the decay is exponential, not linear.

## Common Mistakes

- Forgetting the microfarad and kilohm prefixes when computing $RC$.
- Assuming linear decay instead of exponential.
- Using $\log_{10}$ instead of $\ln$ when rearranging for time.

## Related Problem Types

- [[Capacitor-Discharge-Problem]]
