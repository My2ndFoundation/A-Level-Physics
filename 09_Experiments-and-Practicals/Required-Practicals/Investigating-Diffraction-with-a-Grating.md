---
type: experiment-practical
subject: physics
tags:
  - practical
  - waves
  - electrons-waves-and-photons
  - a-level-core
  - required-practical
level: a-level
difficulty: 2
status: usable
aliases:
  - Grating Wavelength Measurement
  - Laser Diffraction Grating Practical
sources: []
---

# Investigating Diffraction with a Grating

## Aim

To measure the [[Wavelength]] of monochromatic light using a [[Diffraction-Grating]] and the [[Diffraction-Grating-Equation]].

## Variables

- Independent variable: order number $n$ of the observed maximum.
- Dependent variable: angle $\theta$ of each maximum from the straight-through beam.
- Control variables: grating line spacing $d$, light source (single wavelength), normal incidence, grating-to-screen distance.

## Apparatus

- Laser of known nominal wavelength (or a single-wavelength lamp with collimation).
- Diffraction grating of known lines per millimetre, mounted normal to the beam.
- Metre rule and screen (or spectrometer with vernier angular scale).

## Method

1. Set the grating perpendicular to the laser beam at a measured distance $D$ from the screen.
2. Mark the central (zero-order) spot and the symmetric first- and higher-order maxima.
3. Measure the distance $x$ from the central maximum to each order on both sides and average.
4. Calculate $\theta$ for each order from $\tan\theta = x/D$ (or read it directly with a spectrometer).

## Measurements

The line spacing $d = 1/N$ from the grating specification, distances $x$ to each order, and the grating-to-screen distance $D$.

## Data Processing

For each order use the [[Diffraction-Grating-Equation]] $d\sin\theta = n\lambda$ to find $\lambda = d\sin\theta / n$, then average over the orders measured.

## Graph Use

Plot $\sin\theta$ (y-axis) against order $n$ (x-axis). The graph is a straight line through the origin with gradient $\lambda/d$; multiply the gradient by $d$ to obtain the wavelength.

## Uncertainty

- Measuring $\theta$ via $\tan\theta = x/D$ is more precise with a large $D$ and using symmetric orders.
- Grating not exactly normal to the beam introduces a systematic error — check by symmetry of the pattern.
- Using a spectrometer reduces angular uncertainty considerably.

## Safety / Practical Limits

Never look directly into the laser or its specular reflections; keep the beam below eye level. Higher orders may be too faint or beyond $\sin\theta = 1$ to observe.

## Related Quantities

- [[Wavelength]]
- [[Refractive-Index]]

## Related Laws or Results

- [[Diffraction-Grating-Equation]]
- [[Snell-Law]]

## Common Mistakes

- Using lines per metre directly as $d$ instead of its reciprocal.
- Approximating $\sin\theta \approx \tan\theta$ at large diffraction angles, which is invalid for gratings.
- Measuring only one side of the pattern, keeping any misalignment error.

## Visuals

### Diffraction Grating Photo
![[_attachments/09_Experiments-and-Practicals/Investigating-Diffraction-with-a-Grating--diffraction-grating-photo.jpg]]
*Figure: A reflective diffraction grating showing the ruled grooves that split incident light into its component wavelengths at different angles — the same geometry applies to transmission gratings used in the A-Level practical.*
*Source: Diffraction grating — original uploader Deglr6328 at English Wikipedia — Public domain — https://commons.wikimedia.org/wiki/File:Diffraction_grating.jpg. Retrieved 2026-05-19.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; IOPSpark
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
