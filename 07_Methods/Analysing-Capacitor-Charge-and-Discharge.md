---
type: method
subject: physics
tags:
  - capacitors
  - electric-fields
  - fields
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Capacitor Discharge Analysis
  - RC Circuit Analysis
sources: []
---

# Analysing Capacitor Charge and Discharge

## Purpose

To find the charge, voltage, current, or time in an RC circuit during exponential charging or discharging, and to determine the [[Time-Constant]] or [[Capacitance]] from data.

## When to Use

- A [[Capacitor]] is connected to a resistor and a switch.
- The question gives or asks for voltage/charge/current at a given time.
- Data of voltage against time is supplied and τ, R, or C is required.

## Prerequisites

- [[Capacitance]]
- [[Capacitor-Discharge-Equation]]
- [[Time-Constant]]

## Method

1. Identify the circuit values: R, C, and the initial charge $Q_0 = C V_0$ (or initial voltage $V_0$, initial current $I_0 = V_0/R$).
2. Compute the time constant $\tau = RC$, ensuring R is in Ω and C in F (convert μF, nF).
3. Choose the right exponential form:
   - Discharge: $Q = Q_0 e^{-t/RC}$; likewise $V = V_0 e^{-t/RC}$, $I = I_0 e^{-t/RC}$.
   - Charging: $Q = Q_0(1 - e^{-t/RC})$ towards the final charge; current still decays as $I = I_0 e^{-t/RC}$.
4. Substitute and solve. To find time, take natural logs: $t = -RC \ln(Q/Q_0)$.
5. For experimental data, plot $\ln V$ against $t$ (see [[Capacitor-Discharge-Graph]]); the gradient is $-1/RC$, so $\tau = -1/\text{gradient}$ and hence $C = \tau/R$.
6. Sanity-check: after $1\tau \approx 37\%$ remains (discharge); after $5\tau$ treat as complete.

## Worked Example

A 100 μF capacitor charged to 12 V discharges through 47 kΩ. $\tau = (47000)(100\times10^{-6}) = 4.7 \text{ s}$. After 5 s: $V = 12\, e^{-5/4.7} \approx 12 \times 0.345 \approx 4.1 \text{ V}$. (Link a full worked example if one exists.)

## Why It Works

Discharge current is proportional to the remaining charge ($I = V/R = Q/RC$), so the rate of loss is proportional to the amount present. This self-limiting feedback is the defining property of exponential decay, giving the $e^{-t/RC}$ solution.

## Common Mistakes

- Not converting μF/nF to farads before computing τ.
- Using the discharge form for the charge build-up (charge rises as $1 - e^{-t/RC}$).
- Forgetting the minus sign when taking logs to solve for t.

## Related Quantities

- [[Capacitance]]
- [[Time-Constant]]
- [[Charge]]
- [[Potential-Difference]]

## Related Laws or Results

- [[Capacitor-Discharge-Equation]]

## Related Problem Types

- [[Capacitor-Timing-Circuits]]

## Visuals

### Equation selection for RC circuits

```mermaid
flowchart TD
    A[RC circuit problem] --> B{Is the capacitor\ncharging or discharging?}
    B -->|Discharging| C["Q = Q₀ e^(−t/RC)\nV = V₀ e^(−t/RC)\nI = I₀ e^(−t/RC)"]
    B -->|Charging| D["Q = Q₀(1 − e^(−t/RC))\nI = I₀ e^(−t/RC)"]
    C --> E[Compute τ = RC\nSolve for unknown]
    D --> E
    E --> F{Finding time t?}
    F -->|Yes| G["t = −RC ln(Q/Q₀)"]
    F -->|No| H[Substitute directly]
    G --> I[Sanity-check: after 5τ ≈ complete]
    H --> I
```
*Figure: Decision flowchart for choosing the correct RC equation. Discharge → exponential decay; charging → complementary form. Time requires taking ln.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; Physics LibreTexts — no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (M6.1)
