---
type: model
subject: physics
tags:
  - mechanics
  - forces
  - forces-and-motion
  - ocr-h556
level: a-level
difficulty: 1
status: usable
aliases:
  - free body model
  - isolated body model
sources: []
---

# Free Body Model

## Core Idea

The free body model isolates a single object from its surroundings and represents every external force acting *on* it as a labelled arrow, while ignoring forces the object exerts on other things. The object is reduced to a [[Point-Mass-Model|point]] (or a simple shape) and the surroundings are replaced entirely by their force effects. This isolation is what makes [[Newton-Second-Law]] applicable: the vector sum of the arrows is the resultant force on that body alone.

## Assumptions

- Only forces acting *on* the chosen body are included (not forces it exerts).
- The body is treated as a point or rigid shape.
- Each contact, field, or tension interaction is replaced by a single force vector.
- Reaction forces from Newton's third law act on *other* bodies and are excluded.

## Quantities Involved

- [[Force]] vectors: weight, normal contact force, tension, friction, drag, applied force (N)
- Resultant force (N, vector)
- [[Acceleration]] (m s⁻² , vector)

## Key Equations

- ΣF = resultant force
- [[Newton-Second-Law]]: *ΣF = ma*

## When to Use

Use it at the start of almost any dynamics or statics problem: an object on a slope, a hanging mass, a lift accelerating, connected bodies (one diagram per body). It is the first step before applying [[Resolving-Forces]] or Newton's second law.

## Limits of the Model

It does not by itself handle rotation (extended bodies need moments about a point) and it can be misleading if internal forces of a system are mistakenly included. For multi-body systems each body needs its own diagram, with action–reaction pairs split correctly.

## Foundation Link

This makes precise the GCSE "force arrows on an object" picture, adding the strict rule that only forces *on* the chosen body appear, which prepares for vector resolution.

## Related Methods

- [[Drawing-Free-Body-Diagrams]]
- [[Resolving-Forces]]
- [[Applying-Newton-Second-Law]]

## Related Applications

- [[Projectile-Motion]]

## Frontier Links

- None at A-Level depth.

## Common Mistakes

- Including forces the body exerts on others.
- Drawing both members of a third-law pair on the same body.
- Forgetting weight or the normal contact force.

## Visuals

### Free-Body Diagram: Block on a Slope

![[_attachments/06_Models/Free-Body-Model--box-on-slope.svg]]
*Figure: Three external forces on an isolated block — weight W (downward), normal contact force N (perpendicular to slope), and friction f (up the slope); no force the block exerts is shown.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
