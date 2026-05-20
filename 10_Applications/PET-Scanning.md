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

## Visuals

### PET Scanner in Use
![[_attachments/10_Applications/PET-Scanning--pet-scan.jpg]]
*Figure: A patient positioned in a ring-shaped PET scanner. The detector ring registers pairs of 0.511 MeV gamma photons arriving simultaneously from positron annihilation events, enabling reconstruction of tracer uptake.*
*Source: PET scan — liz west — CC BY 2.0 — https://commons.wikimedia.org/wiki/File:PET_scan.jpg. Retrieved 2026-05-19.*

### From Wikipedia

<!-- wiki-images: yes -->

#### Positron emission tomography

![[_attachments/10_Applications/PET-Scanning--wiki-positron-emission-tomography.png]]
*Figure: from Wikipedia article "Positron emission tomography".*
*Source: Wikimedia Commons — [Positron_emission_tomography.png](https://commons.wikimedia.org/wiki/File:Positron_emission_tomography.png). Retrieved 2026-05-20.*

#### ECAT-Exact-HR--PET-Scanner

![[_attachments/10_Applications/PET-Scanning--wiki-ecat-exact-hr-pet-scanner.jpg]]
*Figure: from Wikipedia article "Positron emission tomography".*
*Source: Wikimedia Commons — [ECAT-Exact-HR--PET-Scanner.jpg](https://commons.wikimedia.org/wiki/File:ECAT-Exact-HR--PET-Scanner.jpg). Retrieved 2026-05-20.*

#### PET-MIPS-anim

![[_attachments/10_Applications/PET-Scanning--wiki-pet-mips-anim.gif]]
*Figure: from Wikipedia article "Positron emission tomography".*
*Source: Wikimedia Commons — [PET-MIPS-anim.gif](https://commons.wikimedia.org/wiki/File:PET-MIPS-anim.gif). Retrieved 2026-05-20.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; IOPSpark
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
- Related: [[Medical-Imaging]]
