---
type: experiment-practical
subject: physics
tags:
  - practical
  - required-practical
  - electricity
  - electric-circuits
  - uncertainty
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - internal resistance experiment
  - measuring emf and internal resistance
  - Determining-Internal-Resistance
sources: []
---

# Determining Internal Resistance

## Aim

To determine the electromotive force (emf) and [[Internal-Resistance]] of a cell from how its terminal potential difference falls as the current it supplies increases.

## Variables

- Independent variable: current `I` drawn from the cell (changed with a variable resistor).
- Dependent variable: terminal potential difference `V` across the cell.
- Control variables: same cell, short measurement times (to avoid the cell running down or heating), same temperature.

## Apparatus

- Cell, variable resistor (rheostat) or resistance box, switch.
- Ammeter in series; voltmeter across the cell terminals (high resistance).
- Connecting leads (see [[Circuit-Diagram]]).

## Method

1. Connect the cell, switch, ammeter and variable resistor in series; connect the voltmeter directly across the cell terminals.
2. Set the variable resistor to its maximum and close the switch only while taking a reading.
3. Record the current `I` and terminal pd `V`.
4. Reduce the resistance in steps to increase the current, recording `I` and `V` each time over a good range.
5. Open the switch between readings to prevent the cell discharging or warming.

## Measurements

Pairs of current `I` and terminal pd `V`.

## Data Processing

From $V = \varepsilon - I r$ (terminal pd = emf − lost volts across internal resistance). A graph of `V` (y-axis) against `I` (x-axis) is a straight line: y-intercept $= \varepsilon$ (the emf), gradient $= -r$ (negative of the internal resistance).

## Graph Use

Plot `V` against `I`. The **y-intercept** gives the emf `ε` (see [[Using-Intercept]]); the **gradient** is $-r$, so internal resistance $r = -\text{gradient}$ (see [[Using-Gradient]]).

## Uncertainty

- Sources: meter resolution, cell warming/discharging during the experiment, voltmeter not being ideal (small current through it).
- Reduction: take readings quickly with the switch open between them; use a wide range of currents; repeat; use a high-resistance (digital) voltmeter; draw worst-fit lines for intercept and gradient uncertainty.

## Safety / Practical Limits

Low risk. Avoid short-circuiting the cell (large currents heat components and drain the cell fast). Keep currents modest and measurement times short. The simple model assumes constant `r`, which weakens if the cell heats significantly.

## Related Quantities

- [[Internal-Resistance]]
- [[Potential-Difference]]
- [[Current]]

## Related Laws or Results

- [[Ohms-Law]]

## Common Mistakes

- Leaving the circuit closed so the cell discharges and `ε`, `r` drift.
- Forgetting the gradient is `−r`, not `+r`.
- Using a low-resistance voltmeter that draws significant current.

## Visuals

### V against I Graph for Internal Resistance
```mermaid
xychart-beta
    title "V = ε − Ir  →  V (y) vs I (x)"
    x-axis "Current I / A" [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    y-axis "Terminal pd V / V" 0 --> 2.0
    line [1.8, 1.6, 1.4, 1.2, 1.0, 0.8]
```
*Figure: Terminal pd V plotted against current I gives a straight line with negative gradient $-r$ (the internal resistance) and y-intercept ε (the emf). Here $\varepsilon = 1.8\ \text{V}$ and $r = \frac{1.8 - 0.8}{1.0} = 1.0\ \Omega$. The line must not be forced through the origin.*
*Source: Authored for this vault (CC0). No external copyright.*

### From Wikipedia

<!-- wiki-images: yes -->

#### Members of the Maquis in La Tresorerie

![[_attachments/09_Experiments-and-Practicals/Determining-Internal-Resistance--wiki-members-of-the-maquis-in-la-tresorerie.jpg]]
*Figure: from Wikipedia article "French Resistance".*
*Source: Wikimedia Commons — [Members_of_the_Maquis_in_La_Tresorerie.jpg](https://commons.wikimedia.org/wiki/File:Members_of_the_Maquis_in_La_Tresorerie.jpg). Retrieved 2026-05-20.*

#### "Nicole" a French Partisan Who Captured 25 Nazis in the Chartres Area, in Addition to Liquidating Others, Poses with... - NARA - 5957431 - cropped

![[_attachments/09_Experiments-and-Practicals/Determining-Internal-Resistance--wiki-nicole-a-french-partisan-who-captured-25.jpg]]
*Figure: from Wikipedia article "French Resistance".*
*Source: Wikimedia Commons — ["Nicole" a French Partisan Who Captured 25 Nazis in the Chartres Area, in Addition to Liquidating Others, Poses with... - NARA - 5957431 - cropped.jpg](https://commons.wikimedia.org/wiki/File:"Nicole"_a_French_Partisan_Who_Captured_25_Nazis_in_the_Chartres_Area,_in_Addition_to_Liquidating_Others,_Poses_with..._-_NARA_-_5957431_-_cropped.jpg). Retrieved 2026-05-20.*

#### 1944 French propaganda poster - 1939-1944

![[_attachments/09_Experiments-and-Practicals/Determining-Internal-Resistance--wiki-1944-french-propaganda-poster-1939-1944.jpg]]
*Figure: from Wikipedia article "French Resistance".*
*Source: Wikimedia Commons — [1944 French propaganda poster - 1939-1944.jpg](https://commons.wikimedia.org/wiki/File:1944_French_propaganda_poster_-_1939-1944.jpg). Retrieved 2026-05-20.*

## Source Trace

- Source: OCR Practical Skills Handbook; The Physics Classroom; IOPSpark; OpenStax
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
