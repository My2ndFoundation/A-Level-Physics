---
type: application
subject: physics
tags:
  - medical-physics
  - quantum-physics
  - electrons-waves-and-photons
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - X-ray Radiography
  - Radiography
sources: []
---

# X-ray Imaging

## Problem Context

Producing a two-dimensional shadow image of internal anatomy by passing X-rays through the body and recording how strongly different tissues absorb them.

## Physical Ideas

- [[Photon-Energy]]
- [[Electromagnetic-Spectrum]]
- [[The-Electronvolt]]

## Mathematical Tools

- Photon energy $E = hf = hc/\lambda$.
- Energy from accelerating voltage: $E_{\max} = eV$ (see [[The-Electronvolt]]).
- Exponential attenuation of intensity through tissue: $I = I_0 e^{-\mu x}$, where $\mu$ is the attenuation coefficient and $x$ the thickness.

## Typical Questions

- Calculate the maximum photon energy produced by an X-ray tube operating at a given accelerating voltage.
- Explain why bone appears white and soft tissue grey on a radiograph.
- Determine the fraction of intensity transmitted through a stated thickness of tissue.

## Method Outline

1. Electrons are accelerated through a large [[Potential-Difference]] and strike a metal target.
2. Their kinetic energy converts mostly to heat and partly to X-ray photons (continuous bremsstrahlung plus characteristic lines).
3. The beam passes through the patient; dense, high-atomic-number tissue (bone) absorbs more strongly than soft tissue.
4. Transmitted X-rays expose a detector, forming a contrast image; contrast media can enhance soft-tissue boundaries.

## Assumptions

- Beam approximately monoenergetic for simple attenuation calculations.
- Tissue treated as uniform layers with a single attenuation coefficient.
- Scattering simplified or neglected at A-Level level.

## Links to Other Subjects

- Mathematics: exponential decay and logarithms for attenuation.
- Computer Science: digital detector readout and image processing.

## Frontier Links

- Dose optimisation and digital tomosynthesis; orientation only.

## Common Mistakes

- Confusing tube accelerating voltage (sets maximum photon energy) with beam current (sets photon rate).
- Treating attenuation as linear rather than exponential.

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; IOPSpark
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
- Related: [[Medical-Imaging]]
