---
type: method
subject: physics
tags:
  - graphs
  - graph-skill
  - practical-skills
  - ocr-h556
level: a-level
difficulty: 3
status: usable
aliases:
  - linearisation
  - straight-line graph method
  - y = mx + c method
sources: []
---

# Linearising a Graph

## Purpose

Linearising a graph rearranges a non-linear physical relationship into the straight-line form $y = mx + c$, so that a chosen quantity can be found from the gradient or intercept of a straight-line plot. Straight lines are easier to draw a best fit through and reveal whether the data truly follow the proposed law.

## When to Use

Use it for relationships like $T = 2\pi\sqrt{L/g}$, *I–V* of non-ohmic components, exponential decay, or any power/exponential law where a direct plot would be a curve.

## Prerequisites

- [[Finding-Gradient-from-a-Graph]]
- Algebraic rearrangement; logs for power/exponential laws

## Method

1. Write the suspected relationship between the variables.
2. Rearrange it into the form $y = mx + c$: choose what to plot on each axis so the relationship is linear.
3. For power laws $y = ax^n$, take logs: $\log y = n \log x + \log a$ (plot $\log y$ vs $\log x$).
4. For exponentials $y = A e^{-kx}$, take ln: $\ln y = -kx + \ln A$.
5. Tabulate the transformed variables and plot.
6. Draw the best-fit line; obtain the constant from the gradient and/or intercept.

## Worked Example

For a pendulum, $T = 2\pi\sqrt{L/g}$ gives $T^2 = \dfrac{4\pi^2}{g} L$. Plotting $T^2$ (y) against *L* (x) yields a straight line through the origin with gradient $4\pi^2/g$. Measuring the gradient lets you calculate $g = 4\pi^2 / \text{gradient}$.

## Why It Works

Any relationship reducible to $y = mx + c$ maps onto a straight line whose slope and intercept carry the physical constants. Logarithms convert multiplicative power and exponential laws into additive linear ones.

## Common Mistakes

- Plotting raw variables and forcing a straight line through a curve.
- Forgetting the intercept can carry information.
- Mixing natural log and base-10 log.

## Related Quantities

- [[Acceleration]] (e.g. *g* from a pendulum)

## Related Laws or Results

- [[Simple-Harmonic-Motion-MOC]]

## Related Problem Types

- [[Finding-Gradient-from-a-Graph]]
- Required-practical graph analysis

## Visuals

### Choosing the linearisation transformation

```mermaid
flowchart TD
    A[Suspected relationship] --> B{Type of law?}
    B -->|"Power: y = axⁿ"| C["Take logs: log y vs log x<br/>gradient = n, intercept = log a"]
    B -->|"Exponential: y = A e^(−kx)"| D["Take ln: ln y vs x<br/>gradient = −k, intercept = ln A"]
    B -->|"Polynomial (e.g. T² ∝ L)"| E["Rearrange algebraically<br/>Plot transformed variables"]
    C --> F[Straight-line plot — apply<br/>Finding-Gradient-from-a-Graph]
    D --> F
    E --> F
    F --> G[Gradient and intercept give<br/>the physical constant(s)]
```
*Figure: Decision tree for selecting the correct linearisation. Power laws use log–log; exponential laws use ln–linear; polynomial relationships use algebraic rearrangement.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
