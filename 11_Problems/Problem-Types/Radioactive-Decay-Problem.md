---
type: problem-type
subject: physics
tags:
  - problem-solving
  - nuclear-physics
  - radioactivity
  - nuclear-decay
level: a-level
difficulty: 2
status: usable
aliases:
  - Radioactive Decay Calculation
  - Half-Life Problem
  - Activity and Decay Constant Problem
sources: []
---

# Radioactive Decay Problem

## Problem Signal

A radioactive sample's quantity (number of nuclei, activity, or mass) changes over time, and the question asks for the remaining amount, activity, half-life, decay constant, or age (radioactive dating). Trigger phrases: "half-life", "activity in becquerels", "decay constant", "how long until 1/8 remains", "carbon dating".

## Required Quantities

- [[Activity]]
- [[Decay-Constant]]
- [[Half-Life]]

## Required Concepts

- Random, spontaneous decay
- Exponential decrease in nuclei

## Required Laws or Results

- [[Radioactive-Decay-Law]]: $N = N_0 e^{-\lambda t}$
- $A = \lambda N$, $A = A_0 e^{-\lambda t}$, $T_{1/2} = \dfrac{\ln 2}{\lambda}$

## Required Methods

- [[Finding-Gradient-from-a-Graph]]

## Standard Approach

1. Identify the initial quantity and which quantity is being tracked ($N$, $A$ or mass).
2. Relate half-life and decay constant: $\lambda = \dfrac{\ln 2}{T_{1/2}}$.
3. Apply the exponential: $N = N_0 e^{-\lambda t}$ (same form for activity and mass).
4. For "how many half-lives", use $N = N_0 (1/2)^{t/T_{1/2}}$ when $t$ is a whole number of half-lives.
5. To find a time, rearrange with $\ln$: $t = \dfrac{1}{\lambda}\ln(N_0/N)$.
6. Use $A = \lambda N$ to convert between activity and number of nuclei; state units (Bq, s⁻¹).

## Variations

- Log-linear graph: $\ln A$ against $t$ has gradient $-\lambda$.
- Dating problems: compare current activity/ratio to the original.
- Number of atoms from mass: $N = \dfrac{m}{M}N_A$.

## Common Traps

- Confusing decay constant $\lambda$ with half-life $T_{1/2}$.
- Using $(1/2)^n$ when $t$ is not an exact whole number of half-lives.
- Forgetting $\lambda$ has units s⁻¹ and consistency with time units.
- Treating decay as a fixed rate rather than exponential.

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
