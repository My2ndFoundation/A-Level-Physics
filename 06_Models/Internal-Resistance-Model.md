---
type: model
subject: physics
tags:
  - electricity
  - electric-circuits
  - resistance
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - real cell model
  - emf and internal resistance model
sources: []
---

# Internal Resistance Model

## Core Idea

The internal resistance model represents a real power source (cell or battery) as an ideal source of electromotive force (emf, *ε*) in series with a small fixed resistor *r* inside the source. The ideal emf would deliver its full voltage, but some energy is dissipated inside the source itself, so the voltage available to the external circuit — the terminal potential difference — is always less than the emf whenever current flows. This single addition of *r* explains why batteries "sag" under load.

## Assumptions

- The source is an ideal emf *ε* in series with a constant internal resistance *r*.
- *r* does not change with current (an idealisation of a real cell).
- Connecting wires have negligible resistance unless stated.
- emf is constant regardless of the current drawn.

## Quantities Involved

- Electromotive force *ε* (V)
- Internal resistance *r* (Ω)
- Terminal potential difference *V* (V)
- Current *I* (A)
- External (load) resistance *R* (Ω)

## Key Equations

- $\varepsilon = I(R + r)$
- $V = \varepsilon - Ir$ (terminal p.d.)
- See [[Internal-Resistance]] and [[Kirchhoffs-Second-Law]].

## When to Use

Use it whenever a question mentions emf, terminal voltage, "lost volts", a battery driving a varying load, or asks why measured cell voltage drops when a device is switched on. It is the basis of the experiment to determine *ε* and *r* from a *V*–*I* graph.

## Limits of the Model

Real internal resistance rises as a cell discharges and varies with temperature and current, so a constant *r* is only an approximation. The model also assumes a stable emf, which drops near the end of a battery's life.

## Foundation Link

This extends the GCSE idea that "batteries run down" and that voltage falls under load into a quantitative split between useful terminal voltage and internally lost volts.

## Related Methods

- [[Using-Kirchhoffs-Laws]]
- [[Finding-Gradient-from-a-Graph]]

## Related Applications

- [[Internal-Resistance]]

## Frontier Links

- None at A-Level depth.

## Common Mistakes

- Treating terminal p.d. as equal to emf.
- Ignoring internal resistance when current is large.
- Sign errors applying [[Kirchhoffs-Second-Law]] around the loop.

## Visuals

### Internal Resistance Model: Circuit Diagram

![[_attachments/06_Models/Internal-Resistance-Model--circuit.svg]]
*Figure: A real cell modelled as ideal emf ε in series with internal resistance r; terminal p.d. V = ε − Ir is the voltage available to the external load R.*
*Source: Authored for this vault (CC0). No external copyright.*

### From Wikipedia

<!-- wiki-images: yes -->

#### VFPt Solenoid correct2

![[_attachments/06_Models/Internal-Resistance-Model--wiki-vfpt-solenoid-correct2.svg]]
*Figure: from Wikipedia article "Electromotive force".*
*Source: Wikimedia Commons — [VFPt_Solenoid_correct2.svg](https://commons.wikimedia.org/wiki/File:VFPt_Solenoid_correct2.svg). Retrieved 2026-05-20.*

#### Galvanic cell labeled

![[_attachments/06_Models/Internal-Resistance-Model--wiki-galvanic-cell-labeled.svg]]
*Figure: from Wikipedia article "Electromotive force".*
*Source: Wikimedia Commons — [Galvanic cell labeled.svg](https://commons.wikimedia.org/wiki/File:Galvanic_cell_labeled.svg). Retrieved 2026-05-20.*

#### Reaction path

![[_attachments/06_Models/Internal-Resistance-Model--wiki-reaction-path.jpg]]
*Figure: from Wikipedia article "Electromotive force".*
*Source: Wikimedia Commons — [Reaction path.JPG](https://commons.wikimedia.org/wiki/File:Reaction_path.JPG). Retrieved 2026-05-20.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; Isaac Physics — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
