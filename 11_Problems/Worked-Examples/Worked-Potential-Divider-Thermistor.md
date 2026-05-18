---
type: worked-example
subject: physics
tags:
  - problem-solving
  - electricity
  - electric-circuits
level: a-level
difficulty: 2
status: usable
sources: []
---

# Worked Potential Divider Thermistor

## Problem

A $9.0\ \text{V}$ supply is connected across a series combination of a fixed resistor $R = 2.2\ \text{k}\Omega$ and an NTC thermistor. The output voltage is taken across the fixed resistor. At $10\ ^\circ\text{C}$ the thermistor resistance is $4.0\ \text{k}\Omega$; at $40\ ^\circ\text{C}$ it falls to $1.0\ \text{k}\Omega$. Find the output voltage at each temperature and state how the output changes as the temperature rises.

## Source Reference

- Source: Original worked example; pattern aligned to OCR H556.
- Page/Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]

## Required Quantities

- [[Potential-Difference]]
- [[Resistance]]

## Required Concepts

- Series voltage sharing; thermistor behaviour

## Required Methods

- [[Using-Potential-Dividers]]

## Solution

The output is across the fixed resistor $R$, so

$$V_{out} = \frac{R}{R + R_{th}}\,V_{in}$$

**At $10\ ^\circ\text{C}$** ($R_{th} = 4.0\ \text{k}\Omega$):

$$V_{out} = \frac{2.2}{2.2 + 4.0} \times 9.0 = \frac{2.2}{6.2} \times 9.0 = 3.2\ \text{V}$$

**At $40\ ^\circ\text{C}$** ($R_{th} = 1.0\ \text{k}\Omega$):

$$V_{out} = \frac{2.2}{2.2 + 1.0} \times 9.0 = \frac{2.2}{3.2} \times 9.0 = 6.2\ \text{V}$$

As temperature rises from $10\ ^\circ\text{C}$ to $40\ ^\circ\text{C}$, the thermistor resistance falls, so a larger share of the supply voltage appears across the fixed resistor: $V_{out}$ **increases** from about $3.2\ \text{V}$ to $6.2\ \text{V}$.

## Unit Check

The ratio $R/(R+R_{th})$ is dimensionless (kΩ cancel), so $V_{out}$ has the units of $V_{in}$, i.e. volts. Consistent.

## Key Insight

A potential divider with a thermistor converts a temperature change into a voltage change. Choosing which component the output is taken across decides whether $V_{out}$ rises or falls with temperature.

## Common Mistakes

- Putting the thermistor resistance in the numerator when the output is across the fixed resistor.
- [[Mixing-Up-Series-and-Parallel-Circuits]]
- Assuming a connected load does not change the divider behaviour.

## Related Problem Types

- [[Potential-Divider-Calculation]]
- [[Series-Parallel-Circuit-Analysis]]
