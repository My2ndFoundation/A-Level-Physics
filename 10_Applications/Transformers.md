---
type: application
subject: physics
tags:
  - electromagnetism
  - magnetic-fields
  - fields
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Transformers
  - Transformer
  - Step-Up Transformer
  - Step-Down Transformer
sources: []
---

# Transformers

## Problem Context

A transformer changes the size of an alternating voltage using [[Electromagnetic-Induction]]. It is the device that makes long-distance electrical power transmission efficient and that adapts mains voltage to the level a device needs.

## Physical Ideas

- [[Electromagnetic-Induction]]
- [[Faradays-Law]]
- [[Lenzs-Law]]
- [[Magnetic-Flux-Linkage]]
- [[Conservation-of-Energy]]

## Mathematical Tools

- [[Applying-Faradays-Law]]

## Typical Questions

- Given a turns ratio and primary voltage, find the secondary voltage.
- For an ideal transformer, find the secondary [[Current]] given the primary current.
- Explain why power is transmitted at high voltage and low current.
- Explain causes of energy loss and how each is reduced.

## Method Outline

1. An alternating [[Potential-Difference]] in the primary coil drives an alternating [[Current]], producing a continually changing magnetic flux in a soft-iron core.
2. The core channels almost all this flux through the secondary coil, so both coils share the same changing flux.
3. By [[Faradays-Law]], the induced e.m.f. in each coil is proportional to its number of turns: $\frac{V_s}{V_p} = \frac{N_s}{N_p}$.
4. For an ideal (100% efficient) transformer, input power = output power, so $V_p I_p = V_s I_s$, giving $\frac{V_s}{V_p} = \frac{N_s}{N_p} = \frac{I_p}{I_s}$.
5. Step-up: $N_s > N_p$ raises voltage and lowers current; step-down: $N_s < N_p$ does the reverse.

## Assumptions

- Ideal transformer: no flux leakage, no resistance heating, no core losses.
- Same flux links every turn of both coils.
- Operation with alternating current only (a steady d.c. gives no changing flux and no output).

## Links to Other Subjects

- Mathematics: ratios and proportionality; sinusoidal (a.c.) functions.
- Computer Science: switched-mode power supplies in electronics adapt this principle.

## Frontier Links

- Resonant and high-frequency transformers are central to wireless power transfer and modern compact chargers.

## Common Mistakes

- Thinking a transformer works on d.c. (it needs *changing* flux).
- Believing a transformer creates energy (it conserves power; raising V lowers I).
- Confusing the turns ratio direction for step-up vs step-down.

## Visuals

### Electrical Substation Transformer
![[_attachments/10_Applications/Transformers--substation-transformer.jpg]]
*Figure: A large step-down transformer in an electrical substation. The primary and secondary windings are wound on a laminated iron core; high-voltage transmission lines enter from above and lower-voltage distribution cables leave below.*
*Source: Electrical substation transformer, Love Lane, Liverpool — Rept0n1x — CC BY-SA 3.0 — https://commons.wikimedia.org/wiki/File:Electrical_substation_transformer,_Love_Lane,_Liverpool.JPG. Retrieved 2026-05-19.*

## Source Trace

OpenStax College Physics; HyperPhysics; Physics LibreTexts — no copied text.

OCR alignment: [[OCR-Physics-A-H556-Specification]]

- Source: public physics reference pool
- Section/Page: OCR M6.3 Electromagnetism
