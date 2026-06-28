---
type: application
subject: physics
tags:
  - aqa-7407-7408
  - a-level-physics
  - medical-physics
  - particles-and-medical-physics
  - radioactivity
  - imaging
level: a-level
difficulty: 3
status: draft
aliases:
  - Tracer Imaging
  - Nuclear Medicine Imaging
  - SPECT
sources: []
---

# Radionuclide Imaging

## Problem Context

A patient swallows or is injected with a small amount of a chemical compound carrying a gamma-emitting radionuclide (a "tracer"). The compound is chosen so that a target organ — thyroid, bone, kidney, tumour — concentrates it. Gamma photons escape the body and are detected externally, building a *functional* image of where the tracer accumulates. This complements [[X-ray-Imaging]], which shows anatomy rather than activity.

## Physical Ideas

- [[Radioactivity]]
- [[Activity]]
- [[Half-Life]]
- [[Effective-Half-Life]]
- [[Isotopes]]

## Mathematical Tools

- $A = \lambda N$
- $N(t) = N_0 e^{-\lambda t}$
- $1/T_E = 1/T_P + 1/T_B$

## Typical Tracers

| Nuclide | Gamma energy | Physical half-life | Typical target |
|---|---|---|---|
| Technetium-99m | 140 keV | 6 h | bone, heart, kidneys, brain perfusion |
| Iodine-131 | 364 keV | 8 days | thyroid imaging and therapy |
| Indium-111 | 171 / 245 keV | 2.8 days | white-cell and tumour labelling |

A good imaging tracer should:

1. emit gamma photons (not alpha or high-energy beta) so radiation escapes the body without depositing too much dose
2. have a short *effective* half-life so dose is limited
3. have a gamma energy high enough to escape tissue but low enough to be efficiently absorbed in the detector (roughly 100–400 keV)
4. attach to a chemical carrier that targets a specific organ or process

## The Molybdenum–Technetium Generator

Technetium-99m is short-lived, so it cannot be shipped from a reactor. Hospitals receive a generator containing the longer-lived parent molybdenum-99 ($T_P \approx 67$ h) on an alumina column. Mo-99 decays to Tc-99m. Each morning the column is *eluted* with saline: Tc-99m washes off as pertechnetate ions while Mo-99 stays bound. The eluted Tc-99m is then chemically attached to the targeting carrier and injected.

## Method Outline

1. Choose nuclide and carrier for the clinical question
2. Elute or prepare tracer; check activity with a dose calibrator
3. Administer to patient
4. Wait the uptake time so the carrier concentrates at the target
5. Image with a [[Gamma-Camera]] (or a ring detector for [[PET-Scanning]])
6. Reconstruct a 2D planar image; SPECT rotates the camera to make slices

## Assumptions

- Tracer distribution reflects the physiological process of interest
- Counts collected ≫ background to give useful contrast
- Patient stays still during acquisition

## Links to Other Subjects

- Chemistry: ligand binding selects the organ
- Mathematics: exponential models for clearance and decay

## Frontier Links

- [[Particle-Physics-Map]] — positron annihilation underlies [[PET-Scanning]]

## Common Mistakes

- Confusing gamma-emitting *imaging* tracers with alpha/beta *therapy* sources
- Forgetting that the dose is governed by [[Effective-Half-Life]], not just $T_P$
- Treating SPECT (single photon) and PET (back-to-back 511 keV photons) as the same technique

## Visuals

```mermaid
flowchart LR
    A[Mo-99 generator] -->|elute| B[Tc-99m]
    B -->|label| C[carrier molecule]
    C -->|inject| D[patient organ]
    D -->|gamma photons| E[[Gamma-Camera]]
    E --> F[image]
```

*Source: Authored for this vault (CC0). No external copyright.*

### From Wikimedia

<!-- wiki-images: yes -->

#### Whole-body bone scan
![[_attachments/10_Applications/Radionuclide-Imaging--wiki-bone-scan.jpg]]
*Figure: a Tc-99m whole-body scintigraph — bright regions show where the tracer has concentrated, a functional rather than anatomical image.*
*Source: Wikimedia Commons — [BoneScanWholeBody.jpg](https://commons.wikimedia.org/wiki/File:BoneScanWholeBody.jpg) — Public domain — Kieran Maher. Retrieved 2026-06-27.*

## Source Trace

- Source: [[AQA-Physics-7407-7408-Specification]] §3.10.6
- Public reference: HyperPhysics — Nuclear medicine; OpenStax College Physics §32
