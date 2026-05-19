---
type: physical-quantity
subject: physics
tags:
  - waves
  - simple-harmonic-motion
  - circular-motion
  - ocr-h556
  - a-level-physics
level: a-level
difficulty: 1
status: usable
aliases:
  - T
  - time period
  - periodic time
sources: []
---

# Period

## Core Idea

The period is the time for one complete cycle of a repeating motion — one full swing of a pendulum, one full rotation, or the passage of one whole wave. A short period means a rapidly repeating event (high frequency).

## Symbol

`T`

## SI Unit

`s` (second)

## Scalar or Vector

Scalar. Magnitude only; positive.

## Definition

The period is the time taken for one complete oscillation, rotation, or wave cycle.

## Related Equations

- $T = 1 / f$ — `T` = period (s), `f` = frequency (Hz).
- $T = 2\pi/\omega$ — `ω` = angular frequency (rad s⁻¹).
- Simple pendulum (small angle): $T = 2\pi\sqrt{L/g}$ — `L` = length (m), `g` = 9.81 N kg⁻¹.
- Mass–spring: $T = 2\pi\sqrt{m/k}$ — `m` = mass (kg), `k` = spring constant (N m⁻¹).
- Circular orbit: $T = 2\pi r/v$ — `r` = radius (m), `v` = speed (m s⁻¹).

## How It Is Measured

Time a large number of complete cycles with a stopwatch (or light gate / data-logger) and divide by the number of cycles, then average over repeats. Timing many cycles greatly reduces the percentage uncertainty caused by reaction time.

## Graphical Meaning

On a displacement–time graph, the period is the time for one full cycle (peak to next equivalent peak). The gradient of a $T^2$ against `L` graph for a pendulum gives $4\pi^2/g$, allowing `g` to be found.

## Foundation Links

- [[From-Speed-to-Velocity]] (rates and timing)

## Related Concepts

- [[Frequency]]
- [[Wavelength]]
- [[Amplitude]]

## Related Laws or Results

- None named (links to SHM and circular motion relations)

## Related Experiments

- Measuring g from the period of a simple pendulum

## Frontier Links

- [[Cosmology-Map]] (orbital periods and Kepler's third law — orientation only)

## Common Mistakes

- Confusing period with frequency (reciprocals)
- Timing a single cycle (high percentage uncertainty)
- Forgetting the small-angle condition for the pendulum formula

## Visuals

```mermaid
flowchart LR
    T["Period T (s)<br/>one complete cycle"]
    f["Frequency f = 1/T (Hz)"]
    omega["Angular frequency<br/>ω = 2π/T (rad s⁻¹)"]
    pend["Simple pendulum<br/>T = 2π√(L/g)"]
    spring["Mass–spring<br/>T = 2π√(m/k)"]

    T <-->|"reciprocal"| f
    T -->|"2π/T"| omega
    T --- pend
    T --- spring
```
*Figure: Period T is the reciprocal of frequency f; it connects to angular frequency ω and to the SHM formulas for a pendulum and a mass–spring system.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; HyperPhysics (paraphrased, no copied text)
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
