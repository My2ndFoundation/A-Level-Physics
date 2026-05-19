---
type: method
subject: physics
tags:
  - waves
  - optics
  - electrons-waves-and-photons
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - using Snell's law
  - refraction calculation method
sources: []
---

# Applying Snell Law

## Purpose

This method uses [[Snell-Law]] to find an unknown angle, refractive index, or wave speed when light crosses a boundary between two media, and to determine the critical angle for total internal reflection.

## When to Use

Use it for refraction at any interface (air–glass, glass–water), prism and lens ray problems, optical fibres, and critical-angle / total internal reflection questions.

## Prerequisites

- [[Snell-Law]]
- [[Ray-Model-of-Light]]

## Method

1. Identify the two media and their refractive indices *n₁*, *n₂*.
2. Measure all angles from the normal to the surface, not the surface itself.
3. Apply [[Snell-Law]]: $n_1 \sin\theta_1 = n_2 \sin\theta_2$.
4. Solve for the unknown (angle or refractive index).
5. For wave speed, use $n = c/v$ (light slows in a denser medium; frequency is unchanged, wavelength shortens).
6. For total internal reflection (going to a less dense medium), find the critical angle from $\sin\theta_c = n_2/n_1$.

## Worked Example

Light passes from air ($n_1 = 1.00$) into glass ($n_2 = 1.50$) at 40° to the normal. Then $1.00 \times \sin 40° = 1.50 \times \sin\theta_2$, so $\sin\theta_2 = 0.643 / 1.50 = 0.429$, giving $\theta_2 \approx 25°$. The ray bends toward the normal on entering the denser medium, as expected.

## Why It Works

Refraction occurs because the wave changes speed at the boundary; the wavefronts bend (see [[Wavefront-Model]]). Snell's law is the geometric consequence of this speed change, with refractive index $n = c/v$.

## Common Mistakes

- Measuring angles from the surface instead of the normal.
- Swapping which medium is *n₁* and *n₂*.
- Trying total internal reflection going *into* a denser medium (impossible).

## Related Quantities

- Refractive index, angle of incidence/refraction

## Related Laws or Results

- [[Snell-Law]]

## Related Problem Types

- Refraction, prism, and optical-fibre problems

## Visuals

### Refraction ray diagram at an interface
![[_attachments/07_Methods/applying-snell-law--refraction-ray.svg]]
*Figure: Incident ray in medium 1 (n₁) hits the interface and refracts into medium 2 (n₂ > n₁). All angles (θ₁, θ₂) are measured from the normal. The refracted ray bends toward the normal when entering the denser medium.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
