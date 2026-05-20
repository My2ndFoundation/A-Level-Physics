---
type: concept
subject: physics
tags:
  - electricity
  - electric-circuits
  - resistance
  - electrons-waves-and-photons
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Internal Resistance
  - Source Resistance
  - Lost Volts
sources: []
---

# Internal Resistance

## Core Idea

Internal resistance is the resistance to current flow inside a source of electromotive force (such as a battery or cell), which causes some of the source's energy to be dissipated within it.

## Meaning

A real cell is not an ideal source of potential difference. The chemicals and electrodes inside it have their own resistance, denoted r. When current I flows, a voltage $Ir$ is dissipated inside the cell — these are the "lost volts". The relationship is:

$$\text{EMF} = \text{terminal p.d.} + \text{lost volts}, \quad \text{or} \quad \varepsilon = V + Ir = I(R + r)$$

where $\varepsilon$ is the electromotive force, V the terminal potential difference across the external circuit, and R the external resistance. The EMF is the total energy given per unit charge by the source; the terminal p.d. is what is actually available to the external circuit, and it falls as current increases.

This is captured by the [[Internal-Resistance-Model]]: an ideal EMF source in series with a small resistor r. When the external resistance is very large (almost no current) the terminal p.d. is nearly equal to the EMF; under high current (small R) the lost volts become large and the terminal p.d. drops noticeably.

A graph of terminal p.d. V against current I is a straight line with intercept ε and gradient −r, which is a standard way to measure internal resistance experimentally.

## Everyday Intuition

A torch dims when the battery is "running down" — its internal resistance has risen, so more voltage is lost inside. Starting a car briefly dims the headlights because the huge starter current causes large lost volts.

## GCSE Foundation

- [[Voltage]]
- [[Current]]
- [[Resistance]]

## Why It Matters

Internal resistance explains why terminal voltage depends on load, limits the maximum current and power a source can deliver, and is a required practical and common exam graph analysis.

## Related Quantities

- [[Electromotive-Force]]
- [[Current]]
- [[Resistance]]

## Related Laws or Results

- [[Ohms-Law]]
- [[Conservation-of-Energy]]

## Related Models

- [[Internal-Resistance-Model]]
- [[Potential-Divider-Model]]

## Representations

- [[Circuit-Diagram]]
- Terminal-p.d.–current graph.

## Experiments or Observations

- Determining internal resistance by varying load resistance and plotting V against I.

## Applications

- Battery and power-supply design.
- Maximum power transfer matching.

## Frontier Links

- Electrochemical impedance modelling in modern battery research.

## Common Mistakes

- Confusing EMF with terminal p.d.
- Forgetting the lost volts term Ir when applying conservation of energy.
- Misreading the V–I graph gradient as +r instead of −r.

## Visuals

### Circuit model of a real cell with internal resistance
![[_attachments/04_Concepts/Internal-Resistance--circuit-diagram.svg]]
*Figure: The dashed box represents a real cell modelled as an ideal EMF source ε in series with the internal resistance r. The terminal p.d. $V = IR$ across the external load R is less than ε by the lost volts $Ir$. The full equation is $\varepsilon = I(R + r)$.*
*Source: Authored for this vault (CC0). No external copyright.*

### From Wikipedia

<!-- wiki-images: yes -->

#### VFPt Solenoid correct2

![[_attachments/04_Concepts/Internal-Resistance--wiki-vfpt-solenoid-correct2.svg]]
*Figure: from Wikipedia article "Electromotive force".*
*Source: Wikimedia Commons — [VFPt_Solenoid_correct2.svg](https://commons.wikimedia.org/wiki/File:VFPt_Solenoid_correct2.svg). Retrieved 2026-05-20.*

#### Galvanic cell labeled

![[_attachments/04_Concepts/Internal-Resistance--wiki-galvanic-cell-labeled.svg]]
*Figure: from Wikipedia article "Electromotive force".*
*Source: Wikimedia Commons — [Galvanic cell labeled.svg](https://commons.wikimedia.org/wiki/File:Galvanic_cell_labeled.svg). Retrieved 2026-05-20.*

#### Reaction path

![[_attachments/04_Concepts/Internal-Resistance--wiki-reaction-path.jpg]]
*Figure: from Wikipedia article "Electromotive force".*
*Source: Wikimedia Commons — [Reaction path.JPG](https://commons.wikimedia.org/wiki/File:Reaction_path.JPG). Retrieved 2026-05-20.*

## Source Trace

- Source: OpenStax College Physics; The Physics Classroom; IOPSpark; Physics LibreTexts — paraphrased, no copied text.
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
