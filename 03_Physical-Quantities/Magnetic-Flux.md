---
type: physical-quantity
subject: physics
tags:
  - magnetic-fields
  - electromagnetism
  - fields
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Magnetic Flux
  - Flux
  - Phi
sources: []
---

# Magnetic Flux

## Core Idea

Magnetic flux measures the total amount of magnetic field passing perpendicularly through a given area.

## Symbol

- Φ (Greek capital phi)

## SI Unit

- weber (Wb), where 1 Wb = 1 T m²

## Scalar or Vector

- Scalar (a flux through a chosen surface; it carries a sign relative to a chosen positive normal but is not itself a vector)

## Definition

Magnetic flux through a flat area is the product of the [[Magnetic-Flux-Density]] component perpendicular to the area and the area:

$$\Phi = B A \cos\theta$$

where θ is the angle between the field direction and the normal to the area. When the field is perpendicular to the area (θ = 0), flux is a maximum, $\Phi = B A$. When the field lies in the plane of the area (θ = 90°), $\Phi = 0$.

## Related Equations

- $\Phi = B A \cos\theta$
- Flux linkage $N\Phi = B A N \cos\theta$ (see [[Magnetic-Flux-Linkage]])
- Induced e.m.f. magnitude $= \left|\frac{d(N\Phi)}{dt}\right|$ (see [[Faradays-Law]])

## How It Is Measured

Flux is not measured directly. **B** is found with a Hall probe or search coil, the area A is measured geometrically, and the orientation angle θ is set or recorded. Changing flux is detected through the induced e.m.f. it produces in a search coil connected to a data logger or oscilloscope.

## Graphical Meaning

On a graph of flux linkage NΦ against time, the gradient gives the negative of the induced e.m.f. (Faraday's law). For a coil rotating uniformly, NΦ varies sinusoidally and the induced e.m.f. is its cosine — peaking when the flux passes through zero.

## Foundation Links

- [[Current]]
- [[Force]]

## Related Concepts

- [[Magnetic-Field]]
- [[Electromagnetic-Induction]]

## Related Laws or Results

- [[Faradays-Law]]
- [[Lenzs-Law]]

## Related Experiments

- [[Investigating-Electromagnetic-Induction]]

## Frontier Links

- Magnetic flux is quantised in superconductors (flux quanta), the basis of SQUID magnetometers.

## Common Mistakes

- Using $B A$ instead of $B A \cos\theta$ when the field is not perpendicular to the area.
- Confusing flux Φ with flux linkage NΦ.
- Using the wrong area (e.g. coil cross-section vs the area the field actually threads).

## Visuals

### Flux Through a Tilted Coil: Φ = BA cosθ
![[_attachments/03_Physical-Quantities/Magnetic-Flux--area-angle-geometry.svg]]
*Figure: Parallel field lines (B, green) pass through a coil of area A. Flux Φ = BA cosθ is greatest when B is perpendicular to the coil plane (θ = 0) and zero when B is parallel to it (θ = 90°).*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

OpenStax College Physics; HyperPhysics; Physics LibreTexts — no copied text.

OCR alignment: [[OCR-Physics-A-H556-Specification]]

- Source: public physics reference pool
- Section/Page: OCR M6.3 Electromagnetism
