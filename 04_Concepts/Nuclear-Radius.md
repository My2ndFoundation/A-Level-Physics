---
type: concept
subject: physics
tags:
  - aqa-7407-7408
  - a-level-physics
  - nuclear-physics
  - particles-and-medical-physics
  - a-level-core
level: a-level
difficulty: 3
status: draft
aliases:
  - Nuclear Radius
  - R = r0 A^(1/3)
  - Nuclear Size
sources: []
---

# Nuclear Radius

## Core Idea

The radius $R$ of a nucleus depends only on its nucleon number $A$ through

$$R = r_{0}\,A^{1/3}$$

with $r_{0} \approx 1.05\,\text{fm} = 1.05\times 10^{-15}\,\text{m}$.

## Meaning

Because $R \propto A^{1/3}$, the nuclear **volume** $V = \tfrac{4}{3}\pi R^{3} \propto A$. Each nucleon therefore occupies roughly the same volume in every nucleus, so [[Density|nuclear density]] is approximately constant for all stable nuclei (~$10^{17}\,\text{kg m}^{-3}$). This is one of the strongest pieces of evidence for the [[Nuclear-Model|liquid-drop / incompressible-nucleon picture]].

Symbols and units:

- $R$ — nuclear radius, in metres (m); typically reported in femtometres (1 fm = $10^{-15}$ m).
- $A$ — nucleon number (number of protons + neutrons), dimensionless.
- $r_{0}$ — empirical constant ($\approx 1.05\,\text{fm}$ across the periodic table).

Conditions: applies to a roughly spherical nucleus in its ground state; heavy/highly deformed nuclei deviate slightly.

## Everyday Intuition

Imagine packing marbles (nucleons) of fixed size into a bag. The bag grows in volume in proportion to how many marbles you add, so its radius grows as the cube root of the count — exactly the $A^{1/3}$ scaling.

## GCSE Foundation

- [[The-Nuclear-Atom]] — nucleus is tiny, dense, positively charged.
- [[Isotopes]] — same $Z$, different $A$, so different $R$.

## Why It Matters

- Sets the scale of the [[Strong-Nuclear-Force]] (~1–3 fm range).
- Underlies the constancy of nuclear density.
- Provides the geometric input to scattering cross-sections and binding-energy curves.

## Determining $R$ experimentally

**1. High-energy electron diffraction.** A monoenergetic electron beam (~hundreds of MeV) scattered by a thin foil shows a diffraction minimum at angle $\theta_{\min}$ where

$$\sin\theta_{\min} \approx \frac{1.22\,\lambda}{2R}$$

(treating the nucleus as a circular aperture of diameter $2R$; $\lambda$ from the de Broglie wavelength of the electrons). Measuring $\theta_{\min}$ gives $R$ directly. Electrons are used because they feel no [[Strong-Nuclear-Force|strong force]] — only the charge distribution.

**2. Closest approach of alpha particles.** An $\alpha$ particle of kinetic energy $E_{k}$ fired head-on at a nucleus of charge $Ze$ stops when all KE has become electric potential energy:

$$E_{k} = \frac{1}{4\pi\varepsilon_{0}}\,\frac{2Ze^{2}}{d}$$

giving an **upper bound** on $R$: $R \le d$. Less precise than electron diffraction (it ignores nuclear-force effects at contact) but historically how Rutherford first bracketed the size.

## Representations

- Log–log graph of $R$ vs $A$: $\ln R = \ln r_{0} + \tfrac{1}{3}\ln A$. A straight line of **gradient $1/3$** and $y$-intercept $\ln r_{0}$ confirms the scaling and yields $r_{0}$.
- Intensity-vs-angle plot from electron diffraction, with first minimum marked.

## Related Concepts

- [[Nuclear-Model]]
- [[The-Nuclear-Atom]]
- [[Density]]
- [[Strong-Nuclear-Force]]
- [[Isotopes]]
- [[Radioactive-Decay]]

## Common Mistakes

- Forgetting the cube root and writing $R \propto A$.
- Quoting $r_{0}$ in metres instead of femtometres.
- Treating closest-approach distance as the true radius (it's an upper bound).
- Using protons or neutrons alone instead of total nucleon number $A$.

## Visuals

### Log–log scaling of nuclear radius

```mermaid
xychart-beta
    title "ln R vs ln A (gradient = 1/3)"
    x-axis "ln A" [0, 1, 2, 3, 4, 5, 6]
    y-axis "ln R (fm)" 0 --> 3
    line [0.05, 0.38, 0.72, 1.05, 1.38, 1.72, 2.05]
```

*Figure: Straight line of gradient $1/3$ confirms $R = r_{0}A^{1/3}$; intercept gives $r_{0}$.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: [[AQA-Physics-7407-7408-Specification]] §3.8.1.5
- Public reference: HyperPhysics (Nuclear Size); OpenStax College Physics, Ch. 31.
