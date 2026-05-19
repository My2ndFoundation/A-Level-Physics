---
type: method
subject: physics
tags:
  - practical-skills
  - uncertainty
  - graph-skill
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - propagating uncertainty
  - error propagation strategy
sources: []
---

# Using Uncertainty Propagation

## Purpose

This method gives the overall *strategy* for carrying measurement uncertainties through a calculation so that a final result is quoted with a sensible uncertainty. It is the decision layer that decides *which* combination rule to apply; the detailed arithmetic of combining individual uncertainties is covered in [[Combining-Uncertainties]].

## When to Use

Use it whenever a final quantity is calculated from one or more measured quantities, each with its own uncertainty — practically every required practical that ends in a numerical result with an uncertainty.

## Prerequisites

- [[Estimating-Uncertainty-from-Apparatus]]
- [[Calculating-Percentage-Uncertainty]]
- [[Combining-Uncertainties]]

## Method

1. Estimate the absolute uncertainty in each measured quantity (instrument resolution or repeat-reading spread).
2. Convert each to a percentage uncertainty.
3. Identify how the quantities combine in the formula:
   - added or subtracted → add the *absolute* uncertainties.
   - multiplied or divided → add the *percentage* uncertainties.
   - raised to a power *n* → multiply the percentage uncertainty by *n*.
4. Apply the appropriate rule (see [[Combining-Uncertainties]] for full worked detail).
5. Convert the final percentage uncertainty back to an absolute uncertainty.
6. Quote the result with the uncertainty rounded to one significant figure and matching decimal places.

## Worked Example

Density $\rho = m/V$. If mass has 2% uncertainty and volume has 3% uncertainty, the quantities are divided, so percentage uncertainties add: $2\% + 3\% = 5\%$. A density of 8.0 g cm⁻³ is therefore quoted as 8.0 ± 0.4 g cm⁻³.

## Why It Works

Random uncertainties combine statistically; the add-percentages and add-absolutes rules are the standard first-order approximations used at A-Level, derived from how small fractional changes propagate through products and sums.

## Common Mistakes

- Adding absolute uncertainties for a product (should add percentages).
- Forgetting to multiply by the power *n*.
- Over-precise final uncertainty (use one significant figure).

## Related Quantities

- [[Acceleration]] (e.g. result of a practical)

## Related Laws or Results

- [[Combining-Uncertainties]]

## Related Problem Types

- Required-practical uncertainty evaluation

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
