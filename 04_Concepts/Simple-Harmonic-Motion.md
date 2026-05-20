---
type: concept
subject: physics
tags:
  - simple-harmonic-motion
  - newtonian-world
  - a-level-core
  - oscillations
level: a-level
difficulty: 2
status: usable
aliases:
  - Simple Harmonic Motion
  - SHM
sources: []
---

# Simple Harmonic Motion

## Core Idea

Simple harmonic motion is oscillation in which the acceleration is always directed towards a fixed equilibrium position and is directly proportional to the displacement from it.

## Meaning

The defining condition is:

$$a = -\omega^2 x$$

where $x$ is displacement from equilibrium, $a$ acceleration, and $\omega$ the angular frequency ($\omega = 2\pi f = 2\pi/T$). The minus sign makes the acceleration a *restoring* effect, always pointing back to equilibrium. Solving this gives sinusoidal motion $x = A\cos(\omega t)$ or $x = A\sin(\omega t)$ with [[Amplitude]] $A$, [[Period]] $T$ and [[Frequency]] $f$. Velocity is maximum ($v_\text{max} = \omega A$) at the centre and zero at the extremes; acceleration is maximum ($a_\text{max} = \omega^2 A$) at the extremes and zero at the centre. A key feature: $T$ is independent of amplitude (isochronous).

See [[Simple-Harmonic-Motion-Equation]] for the full equation set.

## Everyday Intuition

A child on a swing, a guitar string, a mass bouncing on a spring, a pendulum for small swings — each speeds up towards the middle and slows at the ends, repeating with a steady beat.

## GCSE Foundation

- [[Force]]
- [[Hookes-Law]]

## Why It Matters

SHM is the universal model for small oscillations — springs, pendulums, molecules, AC circuits, sound, and the basis of [[Resonance]]. It links directly to [[Damping]] and [[Free-and-Forced-Oscillations]].

## Related Quantities

- [[Amplitude]]
- [[Period]]
- [[Frequency]]

## Related Laws or Results

- [[Simple-Harmonic-Motion-Equation]]
- [[Hookes-Law]]
- [[Conservation-of-Energy]]

## Related Models

- [[Simple-Harmonic-Oscillator]]
- [[Ideal-Spring-Model]]

## Representations

- [[Velocity-Time-Graph]]

## Experiments or Observations

- [[Investigating-Simple-Harmonic-Motion]]

## Applications

- [[Banked-Tracks-and-Centrifuges]]

## Frontier Links

- [[Quantum-Mechanics-Map]]

## Common Mistakes

- [[Confusing-Angular-and-Linear-Quantities]]

## Visuals

### SHM: phase relationships between displacement, velocity, and acceleration
```mermaid
xychart-beta
    title "SHM — displacement x, velocity v, acceleration a vs time (schematic)"
    x-axis "Time (fraction of period T)" [0, T/4, T/2, 3T/4, T]
    y-axis "Relative value" -10 --> 10
    line [10, 0, -10, 0, 10]
    line [0, -10, 0, 10, 0]
    line [-10, 0, 10, 0, -10]
```
*Figure: x (displacement) leads v (velocity) by 90°; a (acceleration) is antiphase with x. When x = +A (maximum displacement) velocity = 0 and a = −ω²A (maximum restoring).*
*Source: Authored for this vault (CC0). No external copyright.*

### From Wikipedia

<!-- wiki-images: yes -->

#### Simple Harmonic Motion Orbit

![[_attachments/04_Concepts/Simple-Harmonic-Motion--wiki-simple-harmonic-motion-orbit.gif]]
*Figure: from Wikipedia article "Simple harmonic motion".*
*Source: Wikimedia Commons — [Simple_Harmonic_Motion_Orbit.gif](https://commons.wikimedia.org/wiki/File:Simple_Harmonic_Motion_Orbit.gif). Retrieved 2026-05-20.*

#### Scotch yoke animation

![[_attachments/04_Concepts/Simple-Harmonic-Motion--wiki-scotch-yoke-animation.gif]]
*Figure: from Wikipedia article "Simple harmonic motion".*
*Source: Wikimedia Commons — [Scotch yoke animation.gif](https://commons.wikimedia.org/wiki/File:Scotch_yoke_animation.gif). Retrieved 2026-05-20.*

#### Simple Harmonic Motion Orbit

![[_attachments/04_Concepts/Simple-Harmonic-Motion--wiki-simple-harmonic-motion-orbit.gif]]
*Figure: from Wikipedia article "Simple harmonic motion".*
*Source: Wikimedia Commons — [Simple Harmonic Motion Orbit.gif](https://commons.wikimedia.org/wiki/File:Simple_Harmonic_Motion_Orbit.gif). Retrieved 2026-05-20.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; The Physics Classroom — no copied text
- Section/Page: OCR alignment: [[OCR-Physics-A-H556-Specification]] (M5.3 Oscillations)
