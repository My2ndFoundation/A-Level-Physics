---
type: problem-type
subject: physics
tags:
  - problem-solving
  - waves
  - standing-waves
level: a-level
difficulty: 2
status: usable
aliases:
  - Stationary Wave Problem
  - Harmonics Calculation
  - Resonance on a String or in a Pipe
sources: []
---

# Standing Wave Problem

## Problem Signal

A wave is confined on a string, in a pipe, or in a microwave/melde-type apparatus and forms a standing wave with nodes and antinodes. The question asks for wavelength, frequency, harmonic number, wave speed, or string tension. Trigger phrases: "fundamental frequency", "harmonics", "nodes and antinodes", "string fixed at both ends", "open/closed pipe", "resonance".

## Required Quantities

- [[Wavelength]]
- [[Frequency]]
- [[Wave-Speed]]

## Required Concepts

- Superposition and standing-wave formation
- Boundary conditions (node at fixed/closed end, antinode at free/open end)

## Required Laws or Results

- $v = f\lambda$
- String/open pipe: $f_n = \dfrac{nv}{2L}$
- Closed pipe: $f_n = \dfrac{nv}{4L}$ ($n$ odd)

## Required Methods

- [[Finding-Gradient-from-a-Graph]]

## Standard Approach

1. Identify the boundary conditions to fix where nodes and antinodes must occur.
2. Sketch the harmonic pattern and relate the length $L$ to the wavelength (e.g. fundamental on a fixed string: $L = \lambda/2$).
3. Use $v = f\lambda$ to link speed, frequency and wavelength.
4. For a string, use $v = \sqrt{T/\mu}$ if tension and mass per unit length are involved.
5. Apply the harmonic formula to find the $n$-th frequency or to identify the harmonic.
6. State results with units and confirm the harmonic number is allowed for the system.

## Variations

- String fixed both ends: all integer harmonics present.
- Pipe open both ends: all integer harmonics.
- Pipe closed one end: only odd harmonics; fundamental has $L = \lambda/4$.
- Resonance tube with water: successive resonance lengths differ by $\lambda/2$.

## Common Traps

- Using the pipe-closed formula when the pipe is open (or vice versa).
- Forgetting the end correction is normally neglected at A-Level unless stated.
- Confusing the distance between adjacent nodes ($\lambda/2$) with a full wavelength.
- [[Confusing-Wavelength-and-Amplitude]]

## Visuals

### Standing-wave node and antinode patterns

![[_attachments/11_Problems/Standing-Wave-Problem--standing-wave-harmonics.svg]]
*Figure: Fundamental (n = 1, L = λ/2) and second harmonic (n = 2, L = λ) on a string fixed at both ends. N = node (zero displacement); A = antinode (maximum displacement). Boundary condition: nodes at both fixed ends.*
*Source: Authored for this vault (CC0). No external copyright.*

## Example Sources

- Source: Original problem-type pattern; aligned to OCR H556.
- Exercise/Question: OCR alignment: [[OCR-Physics-A-H556-Specification]]
