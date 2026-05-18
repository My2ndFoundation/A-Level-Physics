---
type: law-result
subject: physics
tags:
  - nuclear-physics
  - radioactivity
  - nuclear-decay
  - ocr-h556
  - a-level-physics
level: a-level
difficulty: 3
status: usable
aliases:
  - radioactive decay law
  - exponential decay law
  - N = N0 e^(-λt)
  - activity law
sources: []
---

# Radioactive Decay Law

## Statement

Radioactive decay is a random process: each undecayed nucleus has the same fixed probability of decaying per unit time. As a result, the number of undecayed nuclei (and the activity) falls exponentially with time, characterised by a constant half-life.

## Equation

`N = N₀ e^(−λt)`

with activity `A = λN`, so `A = A₀ e^(−λt)` and half-life `t½ = ln 2 / λ`

## Symbols and Units

- `N`: number of undecayed nuclei at time `t`, dimensionless count
- `N₀`: initial number of undecayed nuclei at `t = 0`
- `λ`: decay constant (probability of decay per nucleus per second), per second `s⁻¹`
- `t`: time, seconds `s`
- `A`: activity (rate of decay), becquerels `Bq` (= `s⁻¹`)
- `t½`: half-life, seconds `s`

## Conditions

- Decay is **spontaneous and random**; it is unaffected by temperature, pressure, or chemical state.
- The law is statistical — it predicts behaviour of large numbers of nuclei, not which individual nucleus decays.
- Each nuclide has its own fixed decay constant and half-life.

## Physical Meaning

Because every nucleus decays independently with a fixed probability per second, the *rate* of decay is proportional to the number remaining. This gives the same self-limiting exponential decay as a discharging capacitor (see [[Capacitor-Discharge-Equation]]). The half-life is the time for half of any sample to decay and is independent of the starting amount — a hallmark of exponential decay.

## Foundation Link

GCSE introduces half-life and the random nature of decay using count-rate graphs. A-Level adds the decay constant, the exponential equation, the link `A = λN`, and the logarithmic-graph method for finding `λ` and `t½`.

## How to Use

1. Identify `N₀` (or `A₀`) and either `λ` or `t½`; convert using `λ = ln 2 / t½`.
2. Substitute into `N = N₀ e^(−λt)` or `A = A₀ e^(−λt)`.
3. To find `λ` from data, plot `ln A` against `t`; the gradient is `−λ`.
4. Use the half-life for quick "halving" estimates.

## Derivation or Explanation

The decay rate is proportional to the number present: `dN/dt = −λN`. Integrating this first-order equation gives `N = N₀ e^(−λt)`; setting `N = N₀/2` yields `t½ = ln 2 / λ`.

## Related Quantities

- [[Energy]]
- [[Charge]]

## Related Models

- [[Photon-Model]] (for accompanying gamma emission)

## Applications

- Radioactive dating (carbon-14, uranium-lead)
- Medical tracers and radiotherapy dose planning
- Nuclear power and waste timescales

## Frontier Links

- [[Quantum-Mechanics-Map]] — decay is a quantum tunnelling process; randomness is intrinsic, not due to ignorance.

## Common Mistakes

- Confusing decay constant `λ` with half-life
- Thinking decay rate can be changed by temperature or chemistry
- Plotting count rate vs time and expecting a straight line instead of using `ln A`

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; Physics LibreTexts — paraphrased, no copied text
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
