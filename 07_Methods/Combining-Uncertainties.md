---
type: method
subject: physics
tags:
  - uncertainty
  - practical-skills
  - practical
  - maths-link
level: a-level
difficulty: core
status: usable
aliases:
  - Propagating uncertainties
  - Combining uncertainties
sources:
  - OCR-Physics-Practical-Skills-Handbook
---

# Combining Uncertainties

## Purpose

To propagate individual [[Measurement-Uncertainty|uncertainties]] through a calculation so the final result carries the correct uncertainty.

## When to Use

Whenever a final quantity is computed from two or more measured quantities (e.g. density from mass and volume, resistance from V and I).

## Prerequisites

- [[Measurement-Uncertainty]]
- [[Calculating-Percentage-Uncertainty]]

## Method

Let measured quantities be `a, b` with absolute uncertainties `Δa, Δb` and percentage uncertainties `%a, %b`.

1. **Adding or subtracting** (`y = a + b` or `y = a − b`): **add the absolute uncertainties** → `Δy = Δa + Δb`.
2. **Multiplying or dividing** (`y = ab` or `y = a/b`): **add the percentage uncertainties** → `%y = %a + %b`.
3. **Raising to a power** (`y = aⁿ`): **multiply the percentage uncertainty by n** → `%y = |n| × %a` (this includes roots, where n is a fraction).
4. **Multiplying by an exact constant** (`y = ka`): the percentage uncertainty is unchanged; the absolute uncertainty scales by `k`.
5. Convert the final percentage uncertainty back to an absolute uncertainty if the answer is quoted as `value ± Δy`.

## Worked Example

Density `ρ = m / V`. If `%m = 1%` and `%V = 3%`, then `%ρ = 1% + 3% = 4%`. For `ρ = 2500 kg m⁻³`, the absolute uncertainty is `0.04 × 2500 = 100 kg m⁻³`, so `ρ = 2500 ± 100 kg m⁻³`.

## Why It Works

For independent small uncertainties, fractional doubts add through products, and the power rule follows because `aⁿ` multiplies the fractional change n times. (At A-Level the simple *sum* of percentages is used, not the quadrature rule.)

## Common Mistakes

- Adding absolute uncertainties for a product/quotient (should be percentages).
- Forgetting to multiply by the power n (especially for square roots, n = ½).

## Related Quantities

- _None directly._

## Related Laws or Results

- _None directly._

## Related Problem Types

- _Deferred — uncertainty problem types from past-paper ingests._

## Source Trace

- Source: [[OCR-Physics-Practical-Skills-Handbook]]
- Section/Page: Appendix 3 — *Uncertainties* (combining rules, p31–33)
