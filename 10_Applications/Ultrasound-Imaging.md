---
type: application
subject: physics
tags:
  - medical-physics
  - waves
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - Ultrasound Scan
  - Medical Ultrasound
  - Sonography
sources: []
---

# Ultrasound Imaging

## Problem Context

Imaging soft tissue and monitoring blood flow safely (no ionising radiation) by sending high-frequency sound pulses into the body and timing the echoes from boundaries between tissues.

## Physical Ideas

- [[Acoustic-Impedance]]
- [[Intensity]]

## Mathematical Tools

- Echo timing for depth: $d = \dfrac{ct}{2}$, where $c$ is the speed of sound in tissue and $t$ the round-trip time.
- Reflection at a boundary: $\dfrac{I_r}{I_0} = \left(\dfrac{Z_2 - Z_1}{Z_2 + Z_1}\right)^{2}$, set by the [[Acoustic-Impedance]] mismatch.
- Doppler shift for blood-flow velocity measurement.

## Typical Questions

- Explain why a coupling gel is used between the transducer and the skin.
- Calculate the depth of a reflecting boundary from the echo time.
- Compare A-scan and B-scan modes.

## Method Outline

1. A piezoelectric transducer emits short ultrasound pulses (typically 1–15 MHz) and then listens for echoes.
2. At each tissue boundary part of the wave reflects, the fraction set by the impedance mismatch.
3. Echo arrival times give boundary depths; echo strengths give brightness.
4. An A-scan gives a 1D amplitude trace; a B-scan sweeps the beam to build a 2D cross-sectional image.

## Assumptions

- Constant average speed of sound in soft tissue.
- Negligible refraction and beam spreading for simple depth calculations.

## Links to Other Subjects

- Mathematics: timing, ratios, and the Doppler equation.
- Computer Science: real-time signal processing and image formation.

## Frontier Links

- 3D/4D ultrasound and elastography; orientation only.

## Common Mistakes

- Forgetting the factor of two in $d = ct/2$ (the pulse travels there and back).
- Omitting the coupling gel rationale: air's huge impedance mismatch would reflect almost all the energy at the skin.

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; IOPSpark
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
- Related: [[Medical-Imaging]]
