---
type: application
subject: physics
tags:
  - medical-physics
  - quantum-physics
  - electrons-waves-and-photons
  - a-level-core
level: a-level
difficulty: 3
status: usable
aliases:
  - PET Scan
  - Positron Emission Tomography
sources: []
---

# PET Scanning

## Problem Context

Imaging metabolic activity inside the body by detecting the pair of gamma photons produced when positrons from an injected radioactive tracer annihilate with electrons.

## Physical Ideas

- [[Photon-Energy]]
- [[Electromagnetic-Spectrum]]
- [[The-Electronvolt]]

## Mathematical Tools

- Mass-energy equivalence: each annihilation photon has energy $E = m_e c^2 \approx 0.511\ \text{MeV}$ (see [[The-Electronvolt]]).
- Conservation of momentum: the two photons travel almost exactly back-to-back ($180^\circ$ apart).
- Coincidence timing locates the annihilation along the line joining two detectors.

## Typical Questions

- Explain why two gamma photons are emitted in opposite directions in annihilation.
- Calculate the energy of each annihilation photon from the electron rest mass.
- Describe how coincidence detection locates the tracer within the body.

## Method Outline

1. A positron-emitting tracer (e.g. fluorine-18 in a glucose analogue) is injected and concentrates in metabolically active tissue.
2. Each emitted positron annihilates with a nearby electron, producing two 0.511 MeV gamma photons travelling in opposite directions.
3. A ring of detectors registers photon pairs arriving simultaneously (coincidence detection), defining a line of response.
4. Many such lines are reconstructed into a 3D map of tracer uptake (function, not just structure).

## Assumptions

- Positron travels only a short distance before annihilating.
- Photons emitted exactly back-to-back (small angular spread neglected at this level).

## Links to Other Subjects

- Mathematics: tomographic reconstruction from coincidence lines.
- Computer Science: real-time coincidence processing and image rendering.

## Frontier Links

- PET-CT and PET-MRI fusion imaging; orientation only.

## Common Mistakes

- Forgetting that PET shows function/metabolism, not just anatomy.
- Mis-stating annihilation photon energy (it is 0.511 MeV each, from $m_e c^2$).

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; IOPSpark
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
- Related: [[Medical-Imaging]]
