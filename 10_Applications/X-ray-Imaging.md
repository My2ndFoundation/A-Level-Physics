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

## Visuals

### X-ray Radiograph of a Hand
![[_attachments/10_Applications/X-ray-Imaging--hand-radiograph.jpg]]
*Figure: Early X-ray radiograph of a hand with a ring on one finger. Dense bone (high atomic number) absorbs X-rays strongly and appears white; soft tissue transmits more and appears grey; the metal ring absorbs almost completely and appears white-bright.*
*Source: X-ray of the bones of a hand with a ring on one finger — Wilhelm Röntgen / Wellcome Collection — Public Domain — https://commons.wikimedia.org/wiki/File:X-ray_of_the_bones_of_a_hand_with_a_ring_on_one_finger_Wellcome_V0029523.jpg. Retrieved 2026-05-19.*

### From Wikipedia

<!-- wiki-images: yes -->

#### Xraymachine

![[_attachments/10_Applications/X-ray-Imaging--wiki-xraymachine.jpg]]
*Figure: from Wikipedia article "Radiography".*
*Source: Wikimedia Commons — [Xraymachine.JPG](https://commons.wikimedia.org/wiki/File:Xraymachine.JPG). Retrieved 2026-05-20.*

#### AP lumbar xray

![[_attachments/10_Applications/X-ray-Imaging--wiki-ap-lumbar-xray.jpg]]
*Figure: from Wikipedia article "Radiography".*
*Source: Wikimedia Commons — [AP lumbar xray.jpg](https://commons.wikimedia.org/wiki/File:AP_lumbar_xray.jpg). Retrieved 2026-05-20.*

#### Cerebral angiography, arteria vertebralis sinister injection

![[_attachments/10_Applications/X-ray-Imaging--wiki-cerebral-angiography-arteria-vertebralis.jpg]]
*Figure: from Wikipedia article "Radiography".*
*Source: Wikimedia Commons — [Cerebral angiography, arteria vertebralis sinister injection.JPG](https://commons.wikimedia.org/wiki/File:Cerebral_angiography,_arteria_vertebralis_sinister_injection.JPG). Retrieved 2026-05-20.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; IOPSpark
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
- Related: [[Medical-Imaging]]
