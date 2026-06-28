---
type: concept
subject: physics
tags:
  - aqa-7407-7408
  - a-level-physics
  - particles
  - particle-physics
  - particles-and-medical-physics
level: a-level
difficulty: 2
status: draft
aliases:
  - L number
  - electron lepton number
  - muon lepton number
sources: []
---

# Lepton Number

## Core Idea

Lepton number is a conserved quantum number for leptons. AQA separates it by **flavour**: the electron-lepton number $L_{e}$ and the muon-lepton number $L_{\mu}$ are each conserved independently in every interaction.

## Meaning

Assignment rules:

| Particle | $L_{e}$ | $L_{\mu}$ |
| --- | --- | --- |
| $e^{-}$, $\nu_{e}$ | $+1$ | $0$ |
| $e^{+}$, $\bar{\nu}_{e}$ | $-1$ | $0$ |
| $\mu^{-}$, $\nu_{\mu}$ | $0$ | $+1$ |
| $\mu^{+}$, $\bar{\nu}_{\mu}$ | $0$ | $-1$ |
| Everything else (hadrons, photons, $\tau$ at GCSE/AQA scope) | $0$ | $0$ |

**Conservation rule.** For any allowed reaction:

$$\sum L_{e,\text{initial}} = \sum L_{e,\text{final}}, \qquad \sum L_{\mu,\text{initial}} = \sum L_{\mu,\text{final}}.$$

Both must hold. A reaction can never convert an electron-flavour lepton into a muon-flavour one (within AQA scope).

## Everyday Intuition

Think of $L_{e}$ and $L_{\mu}$ as two separate bank balances. Neither can be overdrawn or topped up by a transfer from the other — they are independently audited.

## GCSE Foundation

- [[Atomic-Structure]]

## Why It Matters

The conservation of lepton number is the reason every $\beta$ decay produces a neutrino (or antineutrino). The missing neutrino was actually predicted from the lepton-number / energy / momentum books not balancing in early $\beta$-decay experiments.

**Example — $\beta^{-}$ decay:**

$$n \rightarrow p + e^{-} + \bar{\nu}_{e}$$

$L_{e}$: $0 = 0 + 1 + (-1)$. ✓ Without the $\bar{\nu}_{e}$ the books would not balance.

**Example — $\beta^{+}$ decay:**

$$p \rightarrow n + e^{+} + \nu_{e}$$

$L_{e}$: $0 = 0 + (-1) + 1$. ✓

**Example — muon decay:**

$$\mu^{-} \rightarrow e^{-} + \bar{\nu}_{e} + \nu_{\mu}$$

$L_{e}$: $0 = 1 + (-1) + 0$. ✓ $L_{\mu}$: $1 = 0 + 0 + 1$. ✓

## Related Quantities

- [[Charge]]
- [[Baryon-Number]]
- [[Strangeness]]

## Related Laws or Results

- [[Conservation-of-Energy]]
- [[Conservation-of-Momentum]]

## Related Models

- [[Leptons]]
- [[Classification-of-Particles]]
- [[The-Standard-Model]]

## Representations

- [[Feynman-Diagram]]

## Experiments or Observations

- Pauli's prediction of the neutrino (1930) from missing energy and angular momentum in $\beta$ decay.
- Direct detection of the electron antineutrino (Cowan and Reines, 1956).

## Applications

- Tells you whether a proposed lepton-involving reaction is allowed.
- [[PET-Scanning]] — $\beta^{+}$ decay must include a $\nu_{e}$ to balance $L_{e}$.

## Frontier Links

- [[Particle-Physics-Map]] — neutrino oscillations subtly violate flavour lepton-number conservation; total lepton number still observed to be conserved. Not in AQA.

## Common Mistakes

- Using a single "lepton number" without splitting by flavour. AQA requires $L_{e}$ and $L_{\mu}$ to be checked separately.
- Forgetting that antineutrinos have lepton number $-1$.
- Forgetting that $\nu_{\mu}$ has $L_{\mu} = +1$, not $L_{e}$.
- Assigning lepton number to a pion or a proton.

## Visuals

- Placeholder: side-by-side table showing $L_{e}$ and $L_{\mu}$ check for the three reactions above.

## Source Trace

- Source: [[AQA-Physics-7407-7408-Specification]] §3.2.1.5 and §3.2.1.7
- Section/Page: Classification of particles; conservation laws.
- Explanatory reference: HyperPhysics "Lepton Number"; OpenStax College Physics §33.3 (no text copied).
