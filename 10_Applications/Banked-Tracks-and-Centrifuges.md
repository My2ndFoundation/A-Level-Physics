---
type: application
subject: physics
tags:
  - circular-motion
  - newtonian-world
  - a-level-core
  - technology-link
level: a-level
difficulty: 3
status: usable
aliases:
  - Banked Tracks and Centrifuges
  - Banked Curves
  - Centrifuge
sources: []
---

# Banked Tracks and Centrifuges

## Problem Context

Two classic real-world contexts where a real force is engineered to supply the centripetal requirement of [[Circular-Motion]]: vehicles or athletes on a banked curve, and high-speed centrifuges used to separate mixtures.

## Physical Ideas

- [[Circular-Motion]]
- [[Centripetal-Force]]
- [[Centripetal-Acceleration]]
- [[Newton-Second-Law]]

## Mathematical Tools

- [[Angular-Velocity]]
- [[Solving-Circular-Motion-Problems]]
- [[Radian]]

## Typical Questions

- Find the ideal banking angle θ for a curve of radius r at design speed v.
- Find the maximum cornering speed when friction is present.
- Calculate the effective acceleration (in multiples of g) at the wall of a centrifuge spinning at N rev min⁻¹.

## Method Outline

1. **Banked track**: with no friction the normal contact force N is tilted by angle θ. Vertical: $N \cos\theta = mg$. Horizontal (towards centre): $N \sin\theta = \frac{m v^2}{r}$. Dividing gives $\tan\theta = \frac{v^2}{r g}$ — the ideal speed needs no friction.
2. Convert any rev min⁻¹ to $\omega = 2\pi \times (\text{rev s}^{-1})$ before using $a = \omega^2 r$.
3. **Centrifuge**: contents pressed outward in the rotating frame; in the lab frame the tube wall provides the inward [[Centripetal-Force]]. Effective field $a = \omega^2 r$, often quoted as a/g (the "g-force"), drives denser particles outward fastest.
4. Solve for the requested unknown and sanity-check the inward direction.

## Assumptions

- Rigid circular path of constant radius.
- For the ideal banked case, friction is neglected (point-mass on a smooth incline).
- Steady angular speed (uniform circular motion); air resistance negligible.

## Links to Other Subjects

- Mathematics: resolving vectors, trigonometry ($\tan\theta = \frac{v^2}{rg}$), unit conversion.
- Computer Science: numerical modelling of cornering dynamics and separation times.

## Frontier Links

- [[Particle-Physics-Map]]

## Common Mistakes

- [[Confusing-Angular-and-Linear-Quantities]]

## Visuals

### Laboratory Centrifuge
![[_attachments/10_Applications/Banked-Tracks-and-Centrifuges--laboratory-centrifuge.jpg]]
*Figure: A medical-laboratory centrifuge with sample tubes loaded in the rotor. Spinning at high angular velocity provides a large centripetal acceleration (many multiples of g), driving denser components outward through the liquid faster than they would settle under gravity alone.*
*Source: Laboratory Centrifuge — Frankincense Diala — CC0 — https://commons.wikimedia.org/wiki/File:Laboratory_Centrifuge.jpg. Retrieved 2026-05-19.*

### From Wikipedia

<!-- wiki-images: yes -->

#### Tabletop centrifuge

![[_attachments/10_Applications/Banked-Tracks-and-Centrifuges--wiki-tabletop-centrifuge.jpg]]
*Figure: from Wikipedia article "Centrifuge".*
*Source: Wikimedia Commons — [Tabletop_centrifuge.jpg](https://commons.wikimedia.org/wiki/File:Tabletop_centrifuge.jpg). Retrieved 2026-05-20.*

#### 19thCentrifuge

![[_attachments/10_Applications/Banked-Tracks-and-Centrifuges--wiki-19thcentrifuge.jpg]]
*Figure: from Wikipedia article "Centrifuge".*
*Source: Wikimedia Commons — [19thCentrifuge.JPG](https://commons.wikimedia.org/wiki/File:19thCentrifuge.JPG). Retrieved 2026-05-20.*

#### 20G centrifuge

![[_attachments/10_Applications/Banked-Tracks-and-Centrifuges--wiki-20g-centrifuge.jpg]]
*Figure: from Wikipedia article "Centrifuge".*
*Source: Wikimedia Commons — [20G centrifuge.jpg](https://commons.wikimedia.org/wiki/File:20G_centrifuge.jpg). Retrieved 2026-05-20.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; The Physics Classroom — no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (M5.2 Circular motion)
