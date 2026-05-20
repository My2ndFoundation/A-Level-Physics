---
type: representation
subject: physics
tags:
  - electricity
  - electric-circuits
  - graphs
  - graph-skill
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - I-V characteristic
  - IV graph
  - current voltage graph
  - characteristic curve
  - IV-Characteristic
sources: []
---

# I-V Characteristic

## Core Idea

An I-V characteristic graph shows how the [[Current]] through a component varies with the [[Potential-Difference]] across it. Its shape identifies the component and reveals whether it obeys [[Ohms-Law]].

## Form

A line graph, conventionally with potential difference on the horizontal axis and current on the vertical axis. Standard shapes:

- **Ohmic conductor (metal at constant temperature):** a straight line through the origin.
- **Filament lamp:** an S-shaped curve that flattens as the filament heats and its resistance rises.
- **Semiconductor diode:** almost zero current for reverse and small forward voltage, then a steep rise once the forward threshold (~0.6 V for silicon) is exceeded; reverse direction blocks current.
- **Thermistor / NTC:** current rises faster than proportionally as it self-heats and resistance falls.

## Axes / Labels / Components

- x-axis: potential difference `V`, in volts (V), often plotted for both polarities.
- y-axis: current `I`, in amperes (A).

## Physical Meaning

The curvature tells you how [[Resistance]] changes with conditions. A straight line means constant resistance (ohmic). A curve flattening means resistance increasing (heating filament). A diode's asymmetry shows it conducts essentially one way only.

## Gradient / Area / Intercepts

- **Gradient** of an I-against-V graph = 1 / [[Resistance]] at that point. The reciprocal of the gradient is the resistance; for a curve, take it at a *specific* point, not as a chord across the whole graph.
- The line through the origin for an ohmic conductor confirms $V \propto I$.
- **Intercept**: an ohmic conductor passes through the origin; a diode shows a threshold voltage intercept on the V-axis.
- Area under the curve has no standard meaning here.

## Converts To / From

- From: paired ammeter/voltmeter readings (see [[Determining-Internal-Resistance]] for the related circuit method).
- To: resistance values via $R = V/I$ at chosen points.

## Related Quantities

- [[Current]]
- [[Potential-Difference]]
- [[Resistance]]

## Related Methods

- [[Using-Gradient]]
- [[Finding-Gradient-from-a-Graph]]

## Common Mistakes

- Reading "resistance = gradient" — for an I-V graph resistance is the *reciprocal* of the gradient (or $V/I$ at a point).
- Taking a single resistance for a non-ohmic component whose resistance changes with V.
- Plotting axes the wrong way and misreading the gradient.

## Visuals

### From Wikipedia

<!-- wiki-images: yes -->

#### FourIVcurves

![[_attachments/08_Representations/IV-Characteristic--wiki-fourivcurves.svg]]
*Figure: from Wikipedia article "Current–voltage characteristic".*
*Source: Wikimedia Commons — [FourIVcurves.svg](https://commons.wikimedia.org/wiki/File:FourIVcurves.svg). Retrieved 2026-05-20.*

#### Gunn diode IV curve

![[_attachments/08_Representations/IV-Characteristic--wiki-gunn-diode-iv-curve.svg]]
*Figure: from Wikipedia article "Current–voltage characteristic".*
*Source: Wikimedia Commons — [Gunn diode IV curve.svg](https://commons.wikimedia.org/wiki/File:Gunn_diode_IV_curve.svg). Retrieved 2026-05-20.*

#### IvsV mosfet

![[_attachments/08_Representations/IV-Characteristic--wiki-ivsv-mosfet.svg]]
*Figure: from Wikipedia article "Current–voltage characteristic".*
*Source: Wikimedia Commons — [IvsV mosfet.svg](https://commons.wikimedia.org/wiki/File:IvsV_mosfet.svg). Retrieved 2026-05-20.*

## Source Trace

- Source: OCR Practical Skills Handbook; The Physics Classroom; IOPSpark; OpenStax
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
