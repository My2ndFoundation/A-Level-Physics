---
type: experiment-practical
subject: physics
tags:
  - practical
  - required-practical
  - quantum-physics
  - photoelectric-effect
  - uncertainty
  - ocr-h556
level: a-level
difficulty: 3
status: usable
aliases:
  - photoelectric effect experiment
  - photocell experiment
  - stopping potential experiment
  - Investigating-Photoelectric-Effect
sources: []
---

# Investigating Photoelectric Effect

## Aim

To investigate the [[Photoelectric-Effect]] — demonstrating that emission depends on light frequency, not intensity — and, with a stopping-potential apparatus, to estimate the Planck constant.

## Variables

- Independent variable: frequency `f` of the incident light (set by coloured filters or LEDs of known wavelength).
- Dependent variable: the stopping potential `V_s` needed to just halt the most energetic photoelectrons.
- Control variables: same photocell/metal surface, same source geometry, intensity held within a sensible range.

## Apparatus

- Vacuum photocell with a clean photoemissive cathode.
- Monochromatic light sources of known frequency (filtered lamp or set of LEDs).
- Variable voltage supply, sensitive microammeter, voltmeter.
- (Demonstration) gold-leaf electroscope with a zinc plate and UV source.

## Method

1. *Qualitative (electroscope):* charge a clean zinc plate negatively on an electroscope; shine UV — the leaf falls (emission). Place glass between source and plate — emission stops, showing UV frequency is required, not brightness.
2. *Quantitative (photocell):* illuminate the photocell with one frequency; apply a reverse (retarding) voltage.
3. Increase the retarding voltage until the photocurrent just falls to zero — record this stopping potential `V_s`.
4. Repeat for each light frequency.
5. Repeat readings for each frequency and take a mean stopping potential.

## Measurements

Stopping potential `V_s` for each light frequency `f` (frequency obtained from the known wavelength via `c = fλ`).

## Data Processing

The maximum kinetic energy of emitted electrons is `eV_s = hf − φ`, where `φ` is the work function. Rearranged: `V_s = (h/e) f − φ/e`. A graph of `V_s` against `f` is a straight line.

## Graph Use

Plot `V_s` (y-axis) against `f` (x-axis): gradient `= h/e`, so `h = e × gradient` (see [[Using-Gradient]]). The x-intercept gives the threshold frequency; the y-intercept relates to `φ/e` (see [[Using-Intercept]]).

## Uncertainty

- Sources: judging exactly where photocurrent reaches zero, reverse current/leakage in the photocell, impure source frequency, surface contamination.
- Reduction: take the stopping potential as the clear zero-current point and repeat; use truly monochromatic sources; keep the cathode clean; plot many frequencies and use the best-fit gradient.

## Safety / Practical Limits

UV sources can harm eyes and skin — never look directly at UV; use shielding. High voltages should be handled with care. A-Level treatment is largely demonstrative and qualitative; the quantitative `h` determination is sensitive and approximate.

## Related Quantities

- _Photon energy, work function, threshold frequency (quantum quantities)._

## Related Laws or Results

- [[Photoelectric-Effect]]

## Common Mistakes

- Expecting brighter light (higher intensity) to free electrons below the threshold frequency.
- Misidentifying the stopping potential (small residual/reverse currents).
- Using a non-monochromatic source so the frequency is ill-defined.

## Visuals

### Photoelectric Effect Diagram
![[_attachments/09_Experiments-and-Practicals/Investigating-Photoelectric-Effect--photoelectric-effect-diagram.svg]]
*Figure: Diagram of the photoelectric effect showing a photon of energy hf striking a metal surface and ejecting an electron (photoelectron) with maximum kinetic energy Ek = hf − φ, where φ is the work function. The threshold frequency f₀ is the minimum frequency that can eject an electron.*
*Source: Photoelectric effect — Wolfmankurd — CC BY-SA 3.0 — https://commons.wikimedia.org/wiki/File:Photoelectric_effect.svg. Retrieved 2026-05-19.*

## Source Trace

- Source: OCR Practical Skills Handbook; The Physics Classroom; IOPSpark; OpenStax
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
