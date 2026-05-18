---
type: problem-type
subject: physics
tags:
  - problem-solving
  - electricity
  - electric-circuits
level: a-level
difficulty: 2
status: usable
aliases:
  - Potential Divider Problem
  - Voltage Divider Calculation
  - Sensor Potential Divider
sources: []
---

# Potential Divider Calculation

## Problem Signal

Two resistors (or a resistor and a sensor such as a thermistor or LDR) are in series across a supply, and the question asks for the voltage across one component, or how that voltage changes when a sensor's resistance changes. Trigger phrases: "potential divider", "output voltage", "as temperature rises the thermistor resistance falls", "what voltage is across R₂".

## Required Quantities

- [[Potential-Difference]]
- [[Resistance]]

## Required Concepts

- Series voltage sharing in proportion to resistance

## Required Laws or Results

- $V_{out} = \dfrac{R_2}{R_1 + R_2} \, V_{in}$

## Required Methods

- [[Using-Potential-Dividers]]

## Standard Approach

1. Identify the supply voltage and the two series resistances forming the divider.
2. Apply $V_{out} = \dfrac{R_2}{R_1 + R_2}\,V_{in}$, with $R_2$ the component the output is taken across.
3. For sensor circuits, substitute the sensor's resistance at the stated condition.
4. To analyse a change, compute $V_{out}$ at both sensor resistances and find the difference/direction.
5. Check the limiting cases: if one resistance dominates, almost all the voltage is across it.
6. State the output voltage with units.

## Variations

- Thermistor (NTC): resistance falls as temperature rises, changing $V_{out}$.
- LDR: resistance falls in brighter light.
- Loading effect: a voltmeter or load drawing current changes the effective $R_2$.
- Potentiometer: continuously variable wiper position.

## Common Traps

- Putting the wrong resistor in the numerator (output is across the numerator resistor).
- Forgetting that a connected load changes the divider's behaviour.
- [[Mixing-Up-Series-and-Parallel-Circuits]]
- Assuming $V_{out}$ is half the supply unless the resistances are actually equal.

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
