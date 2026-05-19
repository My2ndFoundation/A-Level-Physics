---
type: representation
subject: physics
tags:
  - capacitors
  - electric-fields
  - fields
  - graphs
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Discharge Curve
  - Exponential Decay Graph
  - Log-Linear Capacitor Graph
sources: []
---

# Capacitor Discharge Graph

## Core Idea

The graph shows how charge, voltage, or current on a discharging [[Capacitor]] falls exponentially with time, and how a log-linear plot linearises this to find the [[Time-Constant]].

## Form

Two related forms:

- **Decay curve:** charge Q (or voltage V, or current I) on the y-axis against time t on the x-axis — a smooth exponential curve falling towards zero, never quite reaching it.
- **Log-linear plot:** $\ln Q$ (or $\ln V$) on the y-axis against time t — a descending straight line.

## Axes / Labels / Components

- Decay curve: y-axis = Q (C), V (V), or I (A); x-axis = time t (s). Starting value Q₀, V₀ or I₀ at $t = 0$.
- Log-linear: y-axis $= \ln(Q/C)$ or $\ln(V/V)$; x-axis = t (s). Straight line with negative gradient.

## Physical Meaning

The curve represents [[Capacitor-Discharge-Equation]]: $Q = Q_0 e^{-t/RC}$. Because the discharge current is proportional to the remaining charge, the curve gets shallower as it falls — a constant-ratio decay. Equal time intervals reduce the value by the same fraction.

## Gradient / Area / Intercepts

- **Decay curve intercept:** the y-intercept is the initial value Q₀ (or V₀, I₀). The curve approaches the t-axis asymptotically (never crosses it).
- **Decay curve gradient:** the initial gradient equals $-Q_0/RC$; the tangent at $t = 0$ crosses the time axis at $t = \tau = RC$.
- **Log-linear gradient:** $\ln Q = \ln Q_0 - t/RC$, so the straight line has gradient $-1/RC$ and y-intercept $\ln Q_0$. Therefore $\tau = -1/\text{gradient}$ and [[Capacitance]] $C = \tau/R$.
- **Area:** the area under the current–time curve equals the total charge that flowed (≈ Q₀).

## Converts To / From

- From: [[Capacitor-Discharge-Equation]]
- To: a value of the [[Time-Constant]] (and hence C or R)

## Related Quantities

- [[Time-Constant]]
- [[Capacitance]]
- [[Charge]]
- [[Potential-Difference]]

## Related Methods

- [[Analysing-Capacitor-Charge-and-Discharge]]

## Common Mistakes

- Reading τ as the time to reach zero (it is the time to fall to 37% of the initial value).
- Plotting log₁₀ but using the gradient as $-1/RC$ (with log₁₀ the gradient is $-1/(RC \ln 10)$); use ln for the simple $-1/RC$ result.
- Treating the curve as a straight line or reading the half-life as the time constant ($t_{1/2} = 0.69\tau$).

## Visuals

### Capacitor discharge curve: Q vs t

```mermaid
xychart-beta
    title "Capacitor discharge: Q falls exponentially (tau = 1 s)"
    x-axis "time t (s)" [0, 0.5, 1, 1.5, 2, 2.5, 3]
    y-axis "charge Q (relative to Q0)" 0 --> 100
    line [100, 61, 37, 22, 14, 8, 5]
```

*Figure: Q falls from its initial value Q₀ (here scaled to 100) following $Q = Q_0 e^{-t/RC}$. After one time constant $\tau = RC$ the charge has fallen to ~37% of Q₀ (the point where the tangent at $t = 0$ meets the t-axis). The curve is asymptotic to zero and never crosses it. The initial gradient is $-Q_0/RC$.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; Physics LibreTexts — no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (M6.1)
