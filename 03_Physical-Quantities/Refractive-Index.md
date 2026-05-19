---
type: physical-quantity
subject: physics
tags:
  - waves
  - electrons-waves-and-photons
  - a-level-core
  - definition
level: a-level
difficulty: 1
status: usable
aliases:
  - Index of Refraction
  - n
sources: []
---

# Refractive Index

## Core Idea

Refractive index measures how much a transparent medium slows light compared with a vacuum, which in turn controls how much a light ray bends when it crosses a boundary.

## Symbol

- $n$ (absolute refractive index of a medium)

## SI Unit

- None — it is a ratio of two speeds, so it is dimensionless.

## Scalar or Vector

- Scalar.

## Definition

The absolute refractive index of a medium is the ratio of the speed of light in a vacuum to the speed of light in that medium:

$$n = \frac{c}{v}$$

where $c \approx 3.00 \times 10^{8}\ \text{m s}^{-1}$ is the speed of light in vacuum and $v$ is the speed of light in the medium. Since $v < c$ in any material, $n > 1$ always. Typical values: air $\approx 1.00$, water $\approx 1.33$, glass $\approx 1.5$.

## Related Equations

- [[Snell-Law]]: $n_1 \sin\theta_1 = n_2 \sin\theta_2$
- Relative refractive index between media 1 and 2: ${}_1 n_2 = n_2 / n_1 = v_1 / v_2$
- Critical angle condition: $\sin\theta_c = 1/n$ (medium to less dense medium) — see [[Critical-Angle]]
- Frequency stays constant on refraction; speed and [[Wavelength]] change in proportion: $v = f\lambda$

## How It Is Measured

A common school method passes a ray through a rectangular or semicircular glass block, measuring the angle of incidence and angle of refraction with a protractor, then plotting $\sin\theta_1$ against $\sin\theta_2$. The gradient gives the refractive index (via [[Snell-Law]]). The semicircular block can also be used to find the [[Critical-Angle]] directly, from which $n = 1/\sin\theta_c$.

## Graphical Meaning

A graph of $\sin\theta_{\text{incidence}}$ (in air) against $\sin\theta_{\text{refraction}}$ (in the medium) is a straight line through the origin whose gradient equals $n$. Linearity confirms [[Snell-Law]].

## Foundation Links

- [[Wave-Refraction]]

## Related Concepts

- [[Total-Internal-Reflection]]
- [[Critical-Angle]]
- [[Electromagnetic-Spectrum]]

## Related Laws or Results

- [[Snell-Law]]

## Related Experiments

- [[Investigating-Diffraction-with-a-Grating]]

## Frontier Links

- Negative-index metamaterials and graded-index optical fibres are modern extensions; out of scope for A-Level.

## Common Mistakes

- Writing $n < 1$ for a real medium (impossible for absolute index).
- Forgetting that frequency, not wavelength, is unchanged on refraction.
- Using degrees inconsistently or taking $\sin$ of the ratio rather than the ratio of $\sin$ values.

## Visuals

### Refraction at a Boundary: n = c/v
![[_attachments/03_Physical-Quantities/Refractive-Index--refraction-ray.svg]]
*Figure: A ray passes from air (n₁ ≈ 1.00) into glass (n₂ ≈ 1.5). It bends toward the normal because it slows down. Snell's Law n₁ sinθ₁ = n₂ sinθ₂ relates the angles; the refractive index equals c/v for each medium.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; IOPSpark
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
