---
type: method
subject: physics
tags:
  - graphs
  - graph-skill
  - practical-skills
  - ocr-h556
level: a-level
difficulty: 1
status: usable
aliases:
  - measuring gradient
  - slope of a graph
sources: []
---

# Finding Gradient from a Graph

## Purpose

This method extracts a physical quantity from the slope of a graph. The gradient often equals a meaningful rate or constant — e.g. the gradient of a [[Velocity-Time-Graph]] is [[Acceleration]], and of a force–extension graph is the spring constant.

## When to Use

Use it whenever a relationship is plotted as a straight line (or you take the tangent to a curve) and the slope represents a quantity you need: acceleration, resistance, spring constant, wave speed, or any "rate of change".

## Prerequisites

- [[Velocity-Time-Graph]]
- Basic graph reading

## Method

1. Identify what each axis represents, with units.
2. For a straight line, draw the line of best fit through the data.
3. Choose two points on the *line* (not raw data points) far apart for accuracy.
4. Read their coordinates carefully, including units.
5. Gradient $= \dfrac{\text{change in } y}{\text{change in } x} = \Delta y / \Delta x$.
6. Attach the correct units (y-units per x-unit) and interpret the physical meaning.
7. For a curve, draw a tangent at the point of interest and find its gradient instead.

## Worked Example

On a velocity–time graph, the line passes through (1.0 s, 2.0 m s⁻¹) and (5.0 s, 14 m s⁻¹). Gradient $= (14 - 2.0) / (5.0 - 1.0) = 12 / 4.0 = 3.0 \text{ m s}^{-2}$. This is the acceleration.

## Why It Works

For a linear relationship $y = mx + c$, the gradient *m* is exactly the constant of proportionality between the plotted quantities. Using a best-fit line averages out random measurement scatter.

## Common Mistakes

- Using raw data points instead of points on the best-fit line.
- Choosing points too close together (large fractional error).
- Forgetting units, or reading the tangent incorrectly on a curve.

## Related Quantities

- [[Acceleration]]
- [[Velocity]]

## Related Laws or Results

- [[Ohms-Law]] (gradient of *V*–*I* graph)

## Related Problem Types

- [[Linearising-a-Graph]]
- Graph-analysis questions

## Visuals

### Reading gradient from a best-fit line
![[_attachments/07_Methods/finding-gradient-from-a-graph--best-fit-triangle.svg]]
*Figure: Velocity–time graph with best-fit line. Two points on the line (not data points) define the triangle: $\Delta x = 4 \text{ s}$, $\Delta y = 12 \text{ m s}^{-1}$, giving gradient $= 3.0 \text{ m s}^{-2}$ (the acceleration). Use widely separated points for accuracy.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
