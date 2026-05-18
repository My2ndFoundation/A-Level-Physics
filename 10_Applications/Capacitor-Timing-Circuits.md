---
type: application
subject: physics
tags:
  - technology-link
  - electricity
  - capacitors
  - electrons-waves-and-photons
level: a-level
difficulty: 3
status: usable
aliases:
  - RC Timing
  - Delay Circuits
sources: []
---

# Capacitor Timing Circuits

## Problem Context

Capacitors charging and discharging through a resistor produce predictable, smoothly changing voltages over time. This is exploited in delay circuits, flashing indicators, camera flash units, and timing stages. A-Level questions use these circuits to apply exponential decay, time constants, and energy storage to a real engineering context.

## Physical Ideas

- [[Capacitance]]
- [[Capacitor-Discharge-Equation]]
- [[Potential-Divider]]

## Mathematical Tools

- Exponential decay of charge, voltage and current during discharge
- Time constant equal to the product of resistance and capacitance
- Energy stored in a charged capacitor
- Logarithms to linearise discharge data

## Typical Questions

- Calculate the time for a capacitor voltage to fall to a given fraction.
- Determine the time constant from a discharge graph.
- Choose resistor and capacitor values for a required delay.
- Calculate the energy stored and the energy dissipated during discharge.

## Method Outline

1. Identify whether the capacitor is charging or discharging and the initial condition.
2. Find the time constant from the resistance and capacitance.
3. Apply the exponential equation for the required quantity at the given time.
4. For data analysis, plot a logarithmic graph to extract the time constant from the gradient.
5. Use the energy expression to find stored or dissipated energy if asked.

## Assumptions

- The resistor and capacitor are ideal with constant values.
- The supply (during charging) is constant.
- Leakage within the capacitor is negligible.

## Links to Other Subjects

- Mathematics: exponential functions, natural logarithms, and gradient extraction from a log-linear plot.
- Computer Science: RC circuits set timing thresholds and debounce inputs in embedded systems.

## Frontier Links

- [[Particle-Physics-Map]] — fast detector electronics use capacitive timing for signal shaping.

## Common Mistakes

- [[Confusing-Energy-and-Power]]
- [[Ignoring-Units]]
- [[Misreading-Graph-Gradient]]

## Source Trace

- Source: OpenStax College Physics; IOPSpark; Isaac Physics; OCR examiner reports (general) — no copied text
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
