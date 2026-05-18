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
  - potential divider method
  - voltage divider calculation
sources: []
---

# Using Potential Dividers

## Purpose

This method calculates the output voltage of a potential divider and designs dividers that produce a required voltage or respond to a sensor (thermistor, LDR, potentiometer).

## When to Use

Use it whenever a fraction of a supply voltage is needed, or when analysing a sensing circuit whose output changes with temperature, light, or slider position.

## Prerequisites

- [[Potential-Divider-Model]]
- [[Ohms-Law]]

## Method

1. Identify the two series resistances *R₁* and *R₂* and which one the output is taken across.
2. Confirm the output is effectively unloaded (negligible current drawn) or include the load in parallel if not.
3. Apply *V_out = V_in × R₂ / (R₁ + R₂)*.
4. For sensor circuits, substitute the sensor's resistance at the relevant condition (hot/cold, light/dark).
5. To design for a target *V_out*, rearrange to find the required resistance ratio.
6. State how *V_out* changes as the sensor's resistance changes.

## Worked Example

A 9.0 V supply drives a 6.0 kΩ resistor in series with a 3.0 kΩ resistor, output taken across the 3.0 kΩ. *V_out = 9.0 × 3.0 / (6.0 + 3.0) = 3.0 V*. If the 3.0 kΩ resistor were a thermistor whose resistance fell when warmed, *V_out* would also fall.

## Why It Works

In a series circuit the same current flows through both resistors, so by [[Ohms-Law]] each resistor's p.d. is proportional to its resistance; the supply voltage divides in the resistance ratio ([[Kirchhoffs-Second-Law]]).

## Common Mistakes

- Ignoring loading when a real load is connected.
- Taking the output across the wrong resistor.
- Not updating the sensor resistance for the stated condition.

## Related Quantities

- Potential difference, resistance

## Related Laws or Results

- [[Ohms-Law]]
- [[Kirchhoffs-Second-Law]]

## Related Problem Types

- [[Potential-Divider]]
- Sensor circuit design

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
