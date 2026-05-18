---
type: concept
subject: physics
tags:
  - electricity
  - electric-circuits
  - resistance
  - electrons-waves-and-photons
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Potential Divider
  - Voltage Divider
  - Potentiometer Circuit
sources: []
---

# Potential Divider

## Core Idea

A potential divider is a circuit of two or more resistors in series across a supply, used to obtain an output voltage that is a chosen fraction of the supply voltage.

## Meaning

Because resistors in series carry the same current, the supply voltage is shared between them in the ratio of their resistances. For two resistors R₁ and R₂ in series across a supply Vₛ, the voltage across R₂ is:

V_out = Vₛ × R₂ / (R₁ + R₂).

By choosing the resistor ratio, any output between zero and the full supply can be produced. This is the basis of the [[Potential-Divider-Model]]. Replacing one resistor with a variable resistor or a sensor (a thermistor or light-dependent resistor) makes the output voltage respond automatically to temperature or light, which is how sensing circuits generate a control signal.

An important practical point is loading: if a device with comparable resistance is connected across the output, it draws current and changes the division, so the formula above strictly applies to the unloaded divider. A potentiometer (a single resistive track with a sliding contact) is a continuously adjustable potential divider.

## Everyday Intuition

A volume control or dimmer switch is a potential divider — sliding the contact changes the fraction of voltage delivered. A light-sensitive porch lamp uses an LDR in a potential divider to detect darkness.

## GCSE Foundation

- [[Voltage]]
- [[Resistance]]
- [[Series-Parallel-Circuit-Analysis]]

## Why It Matters

Potential dividers are the standard way to set reference voltages, build sensor circuits, and provide variable inputs to electronic systems — a heavily examined OCR H556 topic.

## Related Quantities

- [[Voltage]]
- [[Resistance]]
- [[Current]]

## Related Laws or Results

- [[Ohms-Law]]
- [[Conservation-of-Energy]]

## Related Models

- [[Potential-Divider-Model]]
- [[Internal-Resistance-Model]]

## Representations

- [[Circuit-Diagram]]

## Experiments or Observations

- Using a thermistor or LDR in a potential divider and measuring how output p.d. varies with temperature or light.

## Applications

- Temperature and light sensing circuits.
- Volume controls, dimmers and reference voltage supplies.

## Frontier Links

- Resistive sensor networks in modern instrumentation and embedded systems.

## Common Mistakes

- Forgetting the loading effect when a low-resistance device is attached.
- Putting the wrong resistor on top in the ratio formula.
- Confusing series potential dividing with parallel current sharing.

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; IOPSpark; Physics LibreTexts — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
