---
type: method
subject: physics
tags:
  - nuclear-physics
  - particles
  - particles-and-medical-physics
  - a-level-core
level: a-level
difficulty: 3
status: usable
aliases:
  - Binding Energy Calculation
  - Nuclear Energy Release Calculation
  - Q-value Calculation
sources: []
---

# Calculating Binding Energy and Energy Release

## Purpose

To work out the binding energy of a nucleus, the binding energy per nucleon, or the energy released in a nuclear reaction (fission, fusion, decay) from mass data.

## When to Use

- A question gives nuclear or particle masses (in u or kg) and asks for binding energy, energy released, or Q-value.
- A reaction equation is given and you must decide if energy is released.

## Prerequisites

- [[Mass-Defect]]
- [[Mass-Energy-Equivalence]]
- [[Binding-Energy]]

## Method

1. Write the balanced nuclear equation; ensure nucleon number and proton number balance.
2. Compute total mass of reactants and total mass of products (use consistent atomic or nuclear masses).
3. Find the mass change $\Delta m = (\text{mass of reactants}) - (\text{mass of products})$; for a single nucleus' binding energy, $\Delta m = (Z m_p + N m_n) - M_\text{nucleus}$.
4. Convert Δm to energy: either $\Delta E = \Delta m\, c^2$ ($\Delta m$ in kg, $c = 3.00 \times 10^8 \text{ m s}^{-1}$), or multiply Δm in u by 931.5 MeV per u.
5. For binding energy per nucleon, divide the total binding energy by the nucleon number A.
6. Convert MeV ↔ J if required ($1 \text{ MeV} = 1.60 \times 10^{-13} \text{ J}$).

## Worked Example

For a fusion reaction releasing $\Delta m = 0.0189 \text{ u}$: energy released $= 0.0189 \times 931.5 \approx 17.6 \text{ MeV} \approx 2.82 \times 10^{-12} \text{ J}$. (See linked worked examples for fuller treatment.)

## Why It Works

Energy released is the rest-mass lost, converted through [[Mass-Energy-Equivalence]]. A positive Δm (mass lost) means energy is given out; a negative Δm means energy must be supplied.

## Common Mistakes

- Not squaring c
- Mixing u and kg without converting
- Forgetting to divide by A for binding energy *per nucleon*
- Unbalanced reaction equation before computing masses

## Related Quantities

- [[Mass]]
- [[Energy-Quantity|Energy]]

## Related Laws or Results

- [[Mass-Energy-Equivalence]]
- [[Conservation-of-Energy]]

## Related Problem Types

- [[Nuclear-Fission]]
- [[Nuclear-Fusion]]

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; CERN educational material — no copied text
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
