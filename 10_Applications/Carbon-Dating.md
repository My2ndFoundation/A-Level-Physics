---
type: application
subject: physics
tags:
  - nuclear-physics
  - particles-and-medical-physics
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Radiocarbon Dating
  - Carbon-14 Dating
  - Radioactive Dating
sources: []
---

# Carbon Dating

## Problem Context

Estimating the age of once-living material (wood, bone, charcoal) from the residual proportion of the radioactive isotope carbon-14, using the exponential decay law.

## Physical Ideas

- [[Radioactive-Decay]]
- [[Radioactive-Decay-Law]]
- [[Half-Life]]
- [[Isotopes]]
- [[Activity]]

## Mathematical Tools

- [[Decay-Constant]]
- Exponential and natural-logarithm manipulation

## Typical Questions

- A sample's ¹⁴C activity is one quarter of that in a living sample — find its age.
- Given t₁/₂ of ¹⁴C ≈ 5730 years, find λ and hence the age from N/N₀.

## Method Outline

1. While alive, an organism exchanges carbon with the environment, keeping a near-constant ratio of ¹⁴C to stable ¹²C. At death, intake stops and ¹⁴C decays with no replacement.
2. Use t₁/₂ = ln 2 / λ to obtain the decay constant from the known half-life.
3. Apply N = N₀ e^(−λt) (or A = A₀ e^(−λt)), where the ratio N/N₀ equals the measured fraction of ¹⁴C (or activity) compared with living material.
4. Rearrange: t = (1/λ) ln(N₀/N).

## Assumptions

- Atmospheric ¹⁴C/¹²C ratio has been effectively constant over the timescale (corrections exist via calibration).
- No contamination or exchange of carbon after death.
- The sample originally had the standard living-tissue ratio.

## Links to Other Subjects

- Mathematics: exponential decay, logarithms, rearranging equations
- Computer Science: simulating stochastic decay (links to [[Modelling-Radioactive-Decay]])

## Frontier Links

- [[Particle-Physics-Map]]

## Common Mistakes

- Using N instead of N₀/N inside the logarithm
- Inconsistent time units between λ and t
- Assuming dating works for very recent or extremely old samples (limited by ¹⁴C half-life range)

## Visuals

### Radioactive Decay of Carbon-14
![[_attachments/10_Applications/Carbon-Dating--carbon14-decay.png]]
*Figure: Schematic of carbon-14 (¹⁴C) beta-minus decay to nitrogen-14 (¹⁴N). A neutron converts to a proton with emission of a beta particle (electron) and an antineutrino, with a half-life of ~5730 years. Carbon dating uses the ratio of remaining ¹⁴C to stable ¹²C.*
*Source: Radioactive decay of Carbon-14 — Kurt Rosenkrantz — CC BY-SA 3.0 — https://commons.wikimedia.org/wiki/File:Radioactive_decay_of_Carbon-14.png. Retrieved 2026-05-19.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; CERN educational material — no copied text
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
