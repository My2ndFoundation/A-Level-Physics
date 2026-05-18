---
type: method
subject: physics
tags:
  - thermal-physics
  - newtonian-world
  - a-level-core
  - problem-solving
level: a-level
difficulty: 2
status: usable
aliases:
  - Applying the Ideal Gas Equation
  - Using pV = nRT
sources: []
---

# Applying the Ideal Gas Equation

## Purpose

A reliable procedure for solving fixed-mass gas problems using the [[Ideal-Gas-Equation]], including "before-and-after" change-of-state-of-gas questions.

## When to Use

- A question gives some of: pressure, volume, temperature, amount/number of molecules of a gas.
- A gas is compressed, heated or cooled and you must find a new $p$, $V$ or $T$.
- You need the number of molecules, moles or mass of gas, or its [[Density]].

## Prerequisites

- [[Ideal-Gas-Equation]]
- [[Pressure]]
- [[Temperature]]

## Method

1. List the known quantities and the unknown.
2. Convert all temperatures to **kelvin** ($T/\mathrm{K} = \theta/^{\circ}\mathrm{C} + 273.15$).
3. Convert to SI: pressure in Pa (and **absolute**, not gauge), volume in m³.
4. Decide the route: if a fixed mass changes state, use $\dfrac{p_1V_1}{T_1} = \dfrac{p_2V_2}{T_2}$; if you need amount or molecule count, use $pV = nRT$ or $pV = NkT$.
5. Rearrange algebraically *before* substituting numbers.
6. Substitute, evaluate, and quote the answer with correct unit and sensible significant figures.
7. Sanity-check the direction (e.g. heating at constant volume should increase pressure).

## Worked Example

A sealed 2.0 × 10⁻³ m³ container holds gas at 1.0 × 10⁵ Pa and 27 °C. It is heated to 127 °C at constant volume. Find the new pressure.
Convert: $T_1 = 300\ \mathrm{K}$, $T_2 = 400\ \mathrm{K}$. Constant $V$: $\dfrac{p_1}{T_1} = \dfrac{p_2}{T_2}$, so $p_2 = 1.0\times10^{5} \times \dfrac{400}{300} \approx 1.3\times10^{5}\ \mathrm{Pa}$. Direction check: heating raised the pressure. ✓

## Why It Works

For a fixed amount of ideal gas, $pV/T = nR$ is constant, so the ratio relation holds between any two states. The molecular form follows from [[Kinetic-Theory-of-Gases]].

## Common Mistakes

- [[Confusing-Heat-and-Temperature]]
- Leaving temperature in °C
- Using gauge instead of absolute pressure
- Mixing $nR$ and $Nk$ forms

## Related Quantities

- [[Pressure]]
- [[Temperature]]
- [[Boltzmann-Constant]]
- [[Density]]

## Related Laws or Results

- [[Ideal-Gas-Equation]]

## Related Problem Types

- Before-and-after gas state changes; finding number of molecules or gas mass

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; The Physics Classroom — paraphrased, no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (Module 5.1.3)
