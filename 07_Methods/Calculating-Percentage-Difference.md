---
type: method
subject: physics
tags:
  - practical-skills
  - practical
  - maths-link
  - uncertainty
level: a-level
difficulty: core
status: draft
aliases:
  - Percentage difference
  - Percentage error
sources:
  - OCR-Physics-Practical-Skills-Handbook
---

# Calculating Percentage Difference

## Purpose

To compare an experimental result with an accepted (true/reference) value, as a check on **accuracy** and a way to judge whether a [[Systematic-and-Random-Errors|systematic error]] is present.

## When to Use

In the evaluation of a practical, when a known accepted value exists (e.g. comparing a measured `g` with 9.81 m s⁻²).

## Prerequisites

- [[Resolution-Accuracy-and-Precision]]
- [[Calculating-Percentage-Uncertainty]]

## Method

1. Find the experimental value and the accepted value.
2. **Percentage difference** `= (|experimental − accepted| / accepted) × 100%`.
3. Compare this with the experiment's total [[Calculating-Percentage-Uncertainty|percentage uncertainty]]:
   - If the percentage difference is **within** the percentage uncertainty → the result is consistent with the accepted value (no evidence of systematic error).
   - If it is **larger** → there is likely an unaccounted [[Systematic-and-Random-Errors|systematic error]] to discuss.

## Worked Example

A pendulum experiment gives `g = 9.40 m s⁻²`; accepted `9.81 m s⁻²`. Percentage difference = `(0.41 / 9.81) × 100% ≈ 4.2%`. If the experiment's percentage uncertainty was only 2%, the 4.2% gap points to a systematic error (e.g. consistently late timing) rather than random scatter.

## Why It Works

Percentage difference is meaningful only relative to the experiment's own uncertainty — a "small" difference that exceeds the uncertainty still signals a problem; a "large" one inside it does not.

## Common Mistakes

- Dividing by the experimental value instead of the accepted value.
- Reporting a percentage difference without comparing it to the percentage uncertainty.

## Related Quantities

- _None directly._

## Related Laws or Results

- _None directly._

## Related Problem Types

- _Deferred — from past-paper ingests._

## Source Trace

- Source: [[OCR-Physics-Practical-Skills-Handbook]]
- Section/Page: Appendix 3 — *Percentage Difference* (p37)
