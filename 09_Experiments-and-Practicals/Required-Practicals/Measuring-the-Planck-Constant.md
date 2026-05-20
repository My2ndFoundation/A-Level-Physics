---
type: experiment-practical
subject: physics
tags:
  - practical
  - quantum-physics
  - electrons-waves-and-photons
  - a-level-core
  - required-practical
level: a-level
difficulty: 2
status: usable
aliases:
  - Planck Constant from LEDs
  - LED Planck Constant Experiment
sources: []
---

# Measuring the Planck Constant

## Aim

To determine the Planck constant $h$ from the threshold (turn-on) voltages of light-emitting diodes of different colours.

## Variables

- Independent variable: LED colour, giving different emitted [[Wavelength]] $\lambda$.
- Dependent variable: minimum forward [[Potential-Difference]] $V$ at which the LED just begins to emit light.
- Control variables: ambient lighting (kept dark for consistent judgement of turn-on), same circuit and measuring instruments, temperature.

## Apparatus

- Several LEDs of known peak wavelengths (e.g. red, amber, green, blue).
- Variable d.c. supply or potentiometer, protective series resistor.
- Voltmeter (across the LED) and a means to detect first light (dark surroundings).

## Method

1. Connect an LED in forward bias with a protective resistor and voltmeter across it.
2. Slowly increase the voltage from zero until the LED just emits visible light.
3. Record the threshold voltage $V$ for that LED.
4. Repeat for each LED, taking several readings per colour and averaging.

## Measurements

The threshold voltage $V$ for each LED and the manufacturer's peak wavelength $\lambda$ for that colour.

## Data Processing

At turn-on, the energy given to a charge, $eV$, approximately equals the [[Photon-Energy]] $hc/\lambda$:

$$eV \approx \frac{hc}{\lambda} \quad\Rightarrow\quad V = \frac{hc}{e}\cdot\frac{1}{\lambda}$$

## Graph Use

Plot $V$ (y-axis) against $1/\lambda$ (x-axis). The expected straight line through (near) the origin has gradient $hc/e$. Multiply the gradient by $e/c$ to obtain $h$.

## Uncertainty

- Judging the exact turn-on point is subjective — work in the dark and average repeats.
- LED emission is a band, not a single wavelength — use the quoted peak value and note this limitation.
- Voltmeter resolution and contact resistance add small systematic errors.

## Safety / Practical Limits

Low-voltage circuit; main precaution is the series resistor to avoid burning out LEDs. The method gives an order-of-magnitude-correct value, typically within experimental scatter of the accepted $6.63 \times 10^{-34}\ \text{J s}$.

## Related Quantities

- [[Photon-Energy]]
- [[Potential-Difference]]
- [[Wavelength]]

## Related Laws or Results

- [[Photoelectric-Equation]]

## Common Mistakes

- Reversing the axes so the gradient no longer equals $hc/e$.
- Forgetting the protective resistor and damaging the LED.
- Using LED wavelength in nm without converting to metres.

## Visuals

### Assorted LEDs of Different Colours
![[_attachments/09_Experiments-and-Practicals/Measuring-the-Planck-Constant--assorted-LEDs-photo.jpg]]
*Figure: A set of LEDs of different colours (red, amber, yellow, green, blue) — each emits light at a characteristic peak wavelength; the higher the frequency, the higher the threshold voltage required to turn the LED on, giving the V against $1/\lambda$ graph its upward slope with gradient $hc/e$.*
*Source: Verschiedene LEDs — Afrank99 — CC BY-SA 2.0 — https://commons.wikimedia.org/wiki/File:Verschiedene_LEDs.jpg. Retrieved 2026-05-19. Downscaled from 3392×1193 to 1600×562 px.*

### From Wikipedia

<!-- wiki-images: yes -->

#### Black body

![[_attachments/09_Experiments-and-Practicals/Measuring-the-Planck-Constant--wiki-black-body.svg]]
*Figure: from Wikipedia article "Planck constant".*
*Source: Wikimedia Commons — [Black body.svg](https://commons.wikimedia.org/wiki/File:Black_body.svg). Retrieved 2026-05-20.*

#### Bohr atom model

![[_attachments/09_Experiments-and-Practicals/Measuring-the-Planck-Constant--wiki-bohr-atom-model.svg]]
*Figure: from Wikipedia article "Planck constant".*
*Source: Wikimedia Commons — [Bohr atom model.svg](https://commons.wikimedia.org/wiki/File:Bohr_atom_model.svg). Retrieved 2026-05-20.*

#### Max Planck Wirkungsquantums 20050815

![[_attachments/09_Experiments-and-Practicals/Measuring-the-Planck-Constant--wiki-max-planck-wirkungsquantums-20050815.jpg]]
*Figure: from Wikipedia article "Planck constant".*
*Source: Wikimedia Commons — [Max Planck Wirkungsquantums 20050815.jpg](https://commons.wikimedia.org/wiki/File:Max_Planck_Wirkungsquantums_20050815.jpg). Retrieved 2026-05-20.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; IOPSpark
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
