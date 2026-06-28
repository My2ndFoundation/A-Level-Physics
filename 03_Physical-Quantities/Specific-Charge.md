---
type: physical-quantity
subject: physics
tags:
  - aqa-7407-7408
  - a-level-physics
  - particles
  - particle-physics
  - particles-and-medical-physics
  - charge
level: a-level
difficulty: 2
status: draft
aliases:
  - charge-to-mass ratio
  - q/m
  - e/m
sources: []
---

# Specific Charge

## Core Idea

Specific charge is the ratio of a particle's electric charge to its mass. It tells us "how much charge a particle carries per unit mass" and is a single number that captures how strongly a particle responds to electric and magnetic fields relative to its inertia.

## Symbol

- $Q/m$ (sometimes written $q/m$; for the electron, $e/m$).

## SI Unit

- coulomb per kilogram, $\text{C kg}^{-1}$.

## Scalar or Vector

- Scalar. Both [[Charge]] and [[Mass]] are scalars.

## Definition

$$\text{specific charge} = \frac{Q}{m}$$

where $Q$ is the particle's charge in coulombs and $m$ is its rest mass in kilograms.

For composite particles (nuclei, ions), $Q$ is the net charge after accounting for any missing or extra electrons, and $m$ is the total mass of all constituent nucleons (and electrons if present).

## Related Equations

- Proton: $Q/m = +1.60\times10^{-19} / 1.67\times10^{-27} \approx 9.58\times10^{7}\ \text{C kg}^{-1}$.
- Electron: $e/m \approx 1.76\times10^{11}\ \text{C kg}^{-1}$ — the largest specific charge of common particles, because the electron is very light.
- Nucleus $^{A}_{Z}X$ (fully stripped ion): $Q/m = Ze/(A\,u)$, where $u$ is the atomic mass unit.

## How It Is Measured

Specific charge is found by sending charged particles through known electric and magnetic fields and measuring their deflection. The classic example is J. J. Thomson's experiment for the electron: balancing the electric and magnetic deflections in a cathode ray tube gives the speed, and the radius of curvature in the magnetic field alone then fixes $e/m$. Mass spectrometers use the same principle for ions.

## Graphical Meaning

If a particle moves perpendicular to a uniform magnetic field $B$, it follows a circle of radius $r = mv/(QB)$. A graph of $r$ against $v$ for a given $B$ has gradient $m/(QB)$, so $1/\text{gradient}$ scales with the specific charge. Particles with larger $Q/m$ curve more tightly at the same speed.

## Foundation Links

- [[Charge]]
- [[Mass]]
- [[Atomic-Structure]]

## Related Concepts

- [[The-Nuclear-Atom]]
- [[Isotopes]] — same proton number but different specific charge because mass differs.
- [[Classification-of-Particles]]

## Related Laws or Results

- [[Conservation-of-Momentum]] — used when analysing deflections.

## Related Experiments

- Thomson's $e/m$ experiment for the electron.
- Mass spectrometry for ions and isotopes.

## Frontier Links

- [[Particle-Physics-Map]] — accelerators sort particles by specific charge.

## Common Mistakes

- Forgetting to use rest mass in kilograms (not atomic mass units) when computing SI values.
- Treating a fully ionised atom as if it still had its electrons; the charge is $+Ze$ only when all $Z$ electrons are removed.
- Confusing specific charge with charge density (charge per volume).

## Visuals

### Specific charge of common particles

| Particle | Charge $Q$ | Mass $m$ / kg | Specific charge $Q/m$ / C kg⁻¹ |
|---|---|---|---|
| Electron | $-e$ | $9.11\times10^{-31}$ | $1.76\times10^{11}$ |
| Proton | $+e$ | $1.67\times10^{-27}$ | $9.58\times10^{7}$ |
| α particle ($^{4}\text{He}^{2+}$) | $+2e$ | $6.64\times10^{-27}$ | $4.82\times10^{7}$ |
| $^{12}\text{C}^{6+}$ ion | $+6e$ | $1.99\times10^{-26}$ | $4.82\times10^{7}$ |

*Figure: the electron has by far the largest specific charge (~1840× the proton) because its mass is so small; sharing charge over heavier nuclei lowers $Q/m$.*
*Source: Authored for this vault (CC0). No external copyright.*

### From Wikimedia

<!-- wiki-images: yes -->

#### Thomson's cathode ray tube
![[_attachments/03_Physical-Quantities/Specific-Charge--wiki-thomson-cathode-ray-tube.jpg]]
*Figure: J. J. Thomson's 1897 cathode ray tube with magnet coils — the apparatus used to measure the electron's charge-to-mass ratio by balancing electric and magnetic deflection.*
*Source: Wikimedia Commons — [J J Thomsons cathode ray tube with magnet coils, 1897](https://commons.wikimedia.org/wiki/File:J_J_Thomsons_cathode_ray_tube_with_magnet_coils,_1897._(9663807404).jpg) — CC BY-SA 2.0 — Science Museum London / Science and Society Picture Library. Retrieved 2026-06-27.*

## Source Trace

- Source: [[AQA-Physics-7407-7408-Specification]] §3.2.1.1
- Section/Page: Constituents of the atom — specific charge of nuclei and ions.
- Explanatory reference: HyperPhysics (Georgia State) "Electron specific charge"; OpenStax College Physics §30.3 (no text copied).
