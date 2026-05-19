---
type: method
subject: physics
tags:
  - graphs
  - graph-skill
  - practical-skills
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - area under a curve
  - integrating a graph
sources: []
---

# Finding Area Under a Graph

## Purpose

This method finds a physical quantity from the area between a plotted line and the x-axis. The area often represents an accumulated quantity — e.g. the area under a [[Velocity-Time-Graph]] is displacement, and the area under a force–extension graph is work done (elastic [[Energy]]).

## When to Use

Use it when the product of the two plotted quantities is physically meaningful: velocity × time = displacement, force × distance = work, power × time = energy, current × time = charge.

## Prerequisites

- [[Velocity-Time-Graph]]
- Areas of rectangles, triangles, trapezia

## Method

1. Identify what the product of the axes represents, with units.
2. Split the area into simple shapes: rectangles, triangles, trapezia.
3. Calculate each shape's area using axis values (not lengths on paper).
4. Sum the areas; treat area below the x-axis as negative if the quantity can be negative (e.g. reversing velocity).
5. For an irregular curve, count squares or use the trapezium rule for an estimate.
6. Attach the correct units (x-units × y-units).

## Worked Example

On a velocity–time graph, velocity rises uniformly from 0 to 8.0 m s⁻¹ over 4.0 s. The area is a triangle: ½ × base × height = ½ × 4.0 × 8.0 = 16 m. This is the displacement.

## Why It Works

Multiplying the y-value by a small x-interval and summing is exactly integration; for a velocity–time graph this sums small displacements (v Δt) into total displacement. Simple shapes give exact areas for straight-line segments.

## Common Mistakes

- Using lengths measured on the page instead of axis values.
- Ignoring sign for areas below the axis.
- Forgetting units of the resulting quantity.

## Related Quantities

- [[Velocity]]
- [[Energy]]

## Related Laws or Results

- Work–energy relationship (area under force–distance graph)

## Related Problem Types

- [[Finding-Gradient-from-a-Graph]]
- Displacement-from-graph questions

## Visuals

### Area under a velocity–time graph equals displacement
![[_attachments/07_Methods/finding-area-under-a-graph--triangle-displacement.svg]]
*Figure: Velocity increases uniformly from 0 to 8 m s⁻¹ over 4 s. The shaded triangular area = ½ × 4 × 8 = 16 m, which is the displacement. Area below the x-axis would count as negative.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
