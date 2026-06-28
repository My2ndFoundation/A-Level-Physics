---
type: concept
subject: physics
tags:
  - aqa-7407-7408
  - a-level-physics
  - medical-physics
  - particles-and-medical-physics
  - x-rays
  - exponential-decay
level: a-level
difficulty: 3
status: draft
aliases:
  - Linear Attenuation Coefficient
  - Mass Attenuation Coefficient
  - Half-Value Thickness
sources: []
---

# X-ray Attenuation

## Core Idea

When a parallel beam of X-rays passes through matter, its intensity falls exponentially with thickness because each thin slab removes a fixed *fraction* of the photons that reach it.

## Meaning

For an incident intensity $I_0$ entering a uniform absorber, the transmitted intensity after thickness $x$ is

$$ I = I_0\, e^{-\mu x} $$

- $I$ — transmitted [[Intensity]] (W m$^{-2}$)
- $I_0$ — incident intensity (W m$^{-2}$)
- $\mu$ — **linear attenuation coefficient** (m$^{-1}$): the fractional loss of intensity per unit thickness
- $x$ — absorber thickness (m)

Each layer absorbs or scatters a constant fraction, so equal thicknesses cut the surviving intensity by the same factor — the same logic as [[Radioactive-Decay]] and [[Half-Life]], but in space rather than time.

The **mass attenuation coefficient** removes the dependence on packing density:

$$ \mu_m = \frac{\mu}{\rho} $$

with units m$^2$ kg$^{-1}$ and $\rho$ the absorber density (kg m$^{-3}$). Tables of $\mu_m$ are tabulated by element and photon energy because they describe an atomic property, not how compressed the material happens to be.

The **half-value thickness** $x_{1/2}$ is the slab thickness that halves the intensity:

$$ x_{1/2} = \frac{\ln 2}{\mu} $$

A 2-mm half-value thickness means every extra 2 mm of that material drops the surviving beam by another factor of two.

## Everyday Intuition

A torch beam through fog dims more the further it travels — and dense fog dims it faster than thin fog. X-rays through tissue behave the same way, but the "fog" is electrons in atoms.

## GCSE Foundation

- [[Intensity]]
- [[Radioactivity]]
- [[Exponential-Decay]]

## Why It Matters

Different tissues have different $\mu$ at diagnostic X-ray energies. Bone (high atomic number, calcium) attenuates roughly an order of magnitude more strongly than soft tissue, which itself attenuates more than air-filled lung. The **contrast** in an [[X-ray-Imaging|X-ray image]] is the spatial pattern of $\mu$ projected onto the detector. [[CT-Scanning]] reconstructs $\mu(x,y,z)$ from many projections.

## Related Quantities

- [[Intensity]]
- [[Density]]

## Related Laws or Results

- [[Inverse-Square-Law]]

## Related Models

- [[Exponential-Decay-Model]]

## Representations

- [[Log-Linear-Graph]]

## Experiments or Observations

- Measuring $\mu$ for aluminium slabs at fixed X-ray tube voltage

## Applications

- [[X-ray-Imaging]]
- [[CT-Scanning]]
- [[Radiation-Therapy]]

## Frontier Links

- [[Quantum-Mechanics-Map]] — photoelectric absorption and Compton scattering are the atomic-scale processes behind $\mu$

## Common Mistakes

- Treating attenuation as linear ($I = I_0 - kx$) instead of exponential
- Forgetting that $\mu$ depends on photon energy: harder X-rays penetrate further
- Confusing linear ($\mu$, m$^{-1}$) with mass ($\mu_m$, m$^2$ kg$^{-1}$) attenuation coefficients
- Assuming "half-value thickness" halves the *photon energy* — it halves the *intensity*

## Visuals

```mermaid
flowchart LR
    A[I₀ incident] --> B[slab x₁/₂]
    B -->|I₀/2| C[slab x₁/₂]
    C -->|I₀/4| D[slab x₁/₂]
    D -->|I₀/8| E[detector]
```

*Source: Authored for this vault (CC0). No external copyright.*

### From Wikimedia

<!-- wiki-images: yes -->

#### Attenuation coefficient vs photon energy
![[_attachments/04_Concepts/X-ray-Attenuation--wiki-attenuation-coefficient.svg]]
*Figure: the mass attenuation coefficient of iron falling with photon energy — harder X-rays penetrate further, the energy dependence behind $I = I_0 e^{-\mu x}$.*
*Source: Wikimedia Commons — [Attenuation Coefficient Iron.svg](https://commons.wikimedia.org/wiki/File:Attenuation_Coefficient_Iron.svg) — CC BY-SA 3.0 — Jarekt. Retrieved 2026-06-27.*

## Source Trace

- Source: [[AQA-Physics-7407-7408-Specification]] §3.10.5
- Public reference: HyperPhysics — Attenuation of X-rays; OpenStax College Physics §32
