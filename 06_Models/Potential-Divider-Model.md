---
type: model
subject: physics
tags:
  - electricity
  - electric-circuits
  - resistance
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - voltage divider model
  - potential divider
sources: []
---

# Potential Divider Model

## Core Idea

The potential divider model represents two (or more) resistors in series across a supply, used to obtain a chosen fraction of the supply voltage from the junction between them. Because the same current flows through series resistors, the supply voltage divides between them in the ratio of their resistances. By making one resistor a sensor (thermistor, LDR, or potentiometer track) the output voltage can be made to respond to temperature, light, or position — the basis of countless sensing circuits.

## Assumptions

- The resistors are in series and carry the same current.
- The output is taken across one resistor with negligible current drawn by the load (high-impedance output) unless stated.
- Resistor values are well defined (constant unless a sensor).
- Supply voltage is constant and connecting wires have negligible resistance.

## Quantities Involved

- Supply voltage *V_in* (V)
- Resistances *R₁*, *R₂* (Ω)
- Output voltage *V_out* (V)
- Current *I* (A)

## Key Equations

- $V_{out} = V_{in} \times \frac{R_2}{R_1 + R_2}$
- Ratio form: $\frac{V_1}{V_2} = \frac{R_1}{R_2}$
- Built on [[Ohms-Law]] and [[Kirchhoffs-Second-Law]].

## When to Use

Use it when a fixed or variable fraction of a supply voltage is needed: setting a reference voltage, light/temperature sensing circuits, potentiometer volume controls, or any "what is the voltage at this point" series problem.

## Limits of the Model

The simple formula assumes the output is unloaded. If a load with comparable resistance is connected across the output, it draws current and the output voltage falls below the predicted value, so the model must be extended with the load in parallel.

## Foundation Link

This builds on the GCSE result that voltage is shared in a series circuit, making the sharing quantitative and showing how it is exploited for sensing and control.

## Related Methods

- [[Using-Potential-Dividers]]
- [[Analysing-Circuit-Diagrams]]

## Related Applications

- [[Potential-Divider]]

## Frontier Links

- None at A-Level depth.

## Common Mistakes

- Ignoring loading effects on the output.
- Swapping which resistor the output is taken across.
- Forgetting that a sensor's resistance changes the division ratio.

## Visuals

### Potential Divider Circuit

![[_attachments/06_Models/Potential-Divider-Model--circuit.svg]]
*Figure: Two resistors R₁ and R₂ in series across supply V_in; the output V_out is taken across R₂ and equals V_in × R₂/(R₁ + R₂) when unloaded.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
