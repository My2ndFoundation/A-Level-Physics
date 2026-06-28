---
type: method
subject: physics
tags:
  - aqa-7407-7408
  - a-level-physics
  - particles
  - particle-physics
  - particles-and-medical-physics
  - problem-solving
level: a-level
difficulty: 2
status: draft
aliases:
  - conservation law check
  - allowed or forbidden reaction
  - particle reaction check
sources: []
---

# Applying Conservation Laws to Particle Interactions

## Purpose

To decide whether a proposed particle reaction is **allowed** or **forbidden**, by checking all relevant conservation laws in turn.

## When to Use

- The exam question writes a reaction equation and asks whether it can occur.
- The question asks which exchange particle (and therefore which interaction) is responsible.
- A missing particle has to be identified by balancing conservation books.

## Prerequisites

- [[Charge]]
- [[Baryon-Number]]
- [[Lepton-Number]]
- [[Strangeness]]
- [[Classification-of-Particles]]
- [[Fundamental-Interactions]]
- [[Conservation-of-Energy]]
- [[Conservation-of-Momentum]]

## Method

1. **Write the reaction clearly** with every particle and antiparticle, including neutrinos. If a quark-level equation is needed, write that.
2. **Identify the interaction.** Strong, electromagnetic, or weak? Look for clues:
   - Neutrinos present ⇒ weak.
   - Change of quark flavour (e.g. $d \to u$, $s \to u$) ⇒ weak.
   - Only photons exchanged, no flavour change, no neutrinos ⇒ electromagnetic.
   - Hadrons interacting on very short timescales ($10^{-23}\ \text{s}$) with no flavour change ⇒ strong.
3. **Check charge $Q$.** Sum the charges on the left and on the right. They must be equal.
4. **Check baryon number $B$.** Sum on each side. Must be equal.
5. **Check lepton numbers $L_{e}$ and $L_{\mu}$ separately.** Each flavour balance must hold.
6. **Check strangeness $S$.**
   - Strong or EM: $\Delta S = 0$.
   - Weak: $\Delta S = 0$ or $\pm 1$.
7. **Sanity-check energy and momentum.** Total rest energy of products must not exceed total energy available; momentum must be conservable (e.g. annihilation requires two photons, not one).
8. **Decide.** If every test passes, the reaction is allowed. If any test fails, it is forbidden — and you should state **which** rule fails.

## Worked Example

Is $K^{-} + p \rightarrow \pi^{0} + \Lambda^{0}$ allowed by the strong interaction?

- Interaction: strong (no neutrinos, no flavour change beyond rearranged quarks).
- $Q$: $(-1) + (+1) = 0$ and $0 + 0 = 0$. ✓
- $B$: $0 + 1 = 1$ and $0 + 1 = 1$. ✓
- $L_{e}$, $L_{\mu}$: $0 = 0$. ✓
- $S$: $(-1) + 0 = -1$ and $0 + (-1) = -1$. ✓

All checks pass — allowed.

A fuller worked treatment belongs in a separate worked-example page.

## Why It Works

Each conservation law follows from a fundamental symmetry: charge from gauge symmetry of electromagnetism, baryon and lepton number from accidental global symmetries of [[The-Standard-Model]], strangeness from quark-flavour conservation in the strong and electromagnetic interactions. These are stable enough at A-level to be used as algebraic rules.

## Common Mistakes

- Forgetting to include a neutrino or antineutrino in $\beta$ decays — lepton-number books then look balanced but for the wrong reason.
- Using a single "lepton number" instead of separating $L_{e}$ from $L_{\mu}$.
- Allowing $|\Delta S| = 2$ in a single weak vertex.
- Checking only charge and declaring a reaction allowed.
- Forgetting that an antiparticle's $B$, $L$, $S$ all change sign.

## Related Quantities

- [[Charge]]
- [[Baryon-Number]]
- [[Lepton-Number]]
- [[Strangeness]]

## Related Laws or Results

- [[Conservation-of-Energy]]
- [[Conservation-of-Momentum]]

## Related Problem Types

- Allowed/forbidden reaction questions in AQA Paper 2 / Paper 7.
- "Identify the missing particle" questions.
- Exchange-particle identification linked to a [[Feynman-Diagram]].

## Source Trace

- Source: [[AQA-Physics-7407-7408-Specification]] §3.2.1.7
- Section/Page: Applications of conservation laws.
- Explanatory reference: HyperPhysics "Particle Conservation Laws"; OpenStax College Physics §33.3–§33.4 (no text copied).
