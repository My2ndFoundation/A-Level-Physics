---
type: problem-type
subject: physics
tags:
  - problem-solving
  - quantum
  - photoelectric-effect
level: a-level
difficulty: 2
status: usable
aliases:
  - Photoelectric Calculation
  - Photon Energy and Work Function Problem
  - Stopping Potential Problem
sources: []
---

# Photoelectric Effect Calculation

## Problem Signal

Light of a stated frequency or wavelength strikes a metal surface, and the question asks for the maximum kinetic energy of emitted electrons, the threshold frequency, the work function, or the stopping potential. Trigger phrases: "photoelectric", "work function", "threshold frequency/wavelength", "stopping voltage", "maximum kinetic energy of photoelectrons".

## Required Quantities

- [[Photon-Energy]]
- [[Kinetic-Energy]]
- [[Frequency]]

## Required Concepts

- Photon model of light
- One photon, one electron interaction

## Required Laws or Results

- [[Photoelectric-Equation]]: $hf = \phi + E_{k,\max}$

## Required Methods

- [[Using-the-Photoelectric-Equation]]

## Standard Approach

1. Find the photon energy: $E = hf = hc/\lambda$.
2. Compare with the work function $\phi$; emission occurs only if $E \geq \phi$.
3. Apply $E_{k,\max} = hf - \phi$ for the maximum kinetic energy of emitted electrons.
4. For threshold, set $E_{k,\max} = 0$ to get $f_0 = \phi/h$ or $\lambda_0 = hc/\phi$.
5. For stopping potential, use $eV_s = E_{k,\max}$.
6. Convert between joules and electronvolts as required and state units.

## Variations

- Graph of $E_{k,\max}$ against $f$: gradient $= h$, x-intercept $= f_0$, y-intercept $= -\phi$.
- Intensity questions: higher intensity means more photoelectrons per second, not higher $E_{k,\max}$.
- Wavelength given instead of frequency: use $E = hc/\lambda$.

## Common Traps

- Treating intensity as affecting electron energy (it affects rate only).
- Forgetting unit conversion between eV and J ($1\ \text{eV} = 1.6\times10^{-19}\ \text{J}$).
- Using average rather than maximum kinetic energy in the equation.
- [[Confusing-Photon-Energy-and-Intensity]]

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
