---
type: worked-example
subject: physics
tags:
  - problem-solving
  - quantum
  - photoelectric-effect
level: a-level
difficulty: 2
status: usable
sources: []
---

# Worked Photoelectric Stopping Potential

## Problem

Monochromatic light of wavelength $4.5 \times 10^{-7}\ \text{m}$ falls on a clean sodium surface whose work function is $2.3\ \text{eV}$. Take $h = 6.63 \times 10^{-34}\ \text{J s}$, $c = 3.0 \times 10^8\ \text{m s}^{-1}$, $e = 1.6 \times 10^{-19}\ \text{C}$. Find (a) the photon energy in eV, (b) the maximum kinetic energy of the emitted photoelectrons, and (c) the stopping potential.

## Source Reference

- Source: Original worked example; pattern aligned to OCR H556.
- Page/Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]

## Required Quantities

- [[Photon-Energy]]
- [[Kinetic-Energy]]
- [[Frequency]]

## Required Concepts

- Photon model; one photon per electron

## Required Methods

- [[Using-the-Photoelectric-Equation]]

## Solution

**(a) Photon energy.**

$$E = \frac{hc}{\lambda} = \frac{(6.63\times10^{-34})(3.0\times10^8)}{4.5\times10^{-7}} = 4.42 \times 10^{-19}\ \text{J}$$

Convert to eV: $E = \dfrac{4.42\times10^{-19}}{1.6\times10^{-19}} = 2.76\ \text{eV}$.

**(b) Maximum kinetic energy.** Using $E_{k,\max} = hf - \phi$:

$$E_{k,\max} = 2.76 - 2.3 = 0.46\ \text{eV}$$

In joules: $0.46 \times 1.6\times10^{-19} = 7.4 \times 10^{-20}\ \text{J}$.

**(c) Stopping potential.** Since $eV_s = E_{k,\max}$:

$$V_s = \frac{E_{k,\max}}{e} = \frac{0.46\ \text{eV}}{e} = 0.46\ \text{V}$$

## Unit Check

$hc/\lambda$: $(\text{J s})(\text{m s}^{-1})/\text{m} = \text{J}$. Dividing energy in J by charge in C gives volts: $eV_s = E_{k}$ so $V_s = E_k/e$ in J/C = V. Consistent.

## Key Insight

Energy expressed in electronvolts makes the stopping potential immediate: $E_{k,\max}$ in eV equals $V_s$ in volts numerically, because the electron carries charge $e$.

## Common Mistakes

- [[Confusing-Photon-Energy-and-Intensity]]
- Forgetting the eV–joule conversion.
- Using the photon energy instead of $E_{k,\max}$ for the stopping potential.

## Related Problem Types

- [[Photoelectric-Effect-Calculation]]
