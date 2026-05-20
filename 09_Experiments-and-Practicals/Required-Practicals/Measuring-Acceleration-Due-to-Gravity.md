---
type: experiment-practical
subject: physics
tags:
  - practical
  - required-practical
  - mechanics
  - kinematics
  - uncertainty
  - ocr-h556
level: a-level
difficulty: 2
status: usable
aliases:
  - measuring g
  - acceleration due to gravity experiment
  - free fall experiment
  - Measuring-Acceleration-Due-to-Gravity
sources: []
---

# Measuring Acceleration Due to Gravity

## Aim

To determine the local acceleration of free fall `g` by timing an object falling under gravity from measured heights.

## Variables

- Independent variable: drop height `h`.
- Dependent variable: time of fall `t`.
- Control variables: same steel ball (so air resistance is negligible and consistent), same release mechanism, same apparatus alignment.

## Apparatus

- Electromagnet release and trapdoor timer (or two light gates / data logger).
- Steel ball bearing.
- Metre rule or tape to measure drop height; clamp stand.

## Method

1. Set the ball on the electromagnet directly above the trapdoor switch and measure the drop height `h` from the bottom of the ball to the trapdoor.
2. Switch off the electromagnet to release the ball; the timer starts as the ball leaves and stops as it strikes the trapdoor.
3. Record the fall time `t`. Repeat at the same height several times and take a mean.
4. Change `h` and repeat for a range of heights (typically 0.2 m to 1.0 m).

## Measurements

Drop height `h` for each setting and the corresponding mean fall time `t`.

## Data Processing

From $h = \frac{1}{2}gt^2$ (initial velocity zero), rearrange to $h = \frac{g}{2} t^2$. So a graph of `h` against $t^2$ is a straight line through the origin with gradient $g/2$. Hence $g = 2 \times \text{gradient}$.

## Graph Use

Plot `h` (y-axis) against $t^2$ (x-axis). The line should pass through the origin; gradient $= g/2$, so $g = 2 \times \text{gradient}$ (see [[Using-Gradient]]). A non-zero intercept signals a timing systematic error (see [[Using-Intercept]]).

## Uncertainty

- Sources: release delay of the electromagnet (systematic, often makes timing start late), height measurement, trapdoor switching.
- Reduction: repeat and average at each height; use a wide range of heights; use the graph gradient (which is insensitive to a constant timing offset); measure `h` consistently from the same point on the ball.

## Safety / Practical Limits

Low risk. Keep feet clear of the falling ball and trapdoor. The free-fall (no air resistance) model is only valid for a dense, compact ball over modest heights.

## Related Quantities

- [[Acceleration]]
- [[Gravitational-Field-Strength]]

## Related Laws or Results

- [[Newton-Second-Law]]

## Common Mistakes

- Using a single drop instead of repeats and a graph.
- Measuring height inconsistently (top vs bottom of the ball).
- Ignoring the electromagnet release delay when using single-shot timing.

## Visuals

### Free-Fall Diagram
![[_attachments/09_Experiments-and-Practicals/Measuring-Acceleration-Due-to-Gravity--free-fall-diagram.svg]]
*Figure: Diagram of an object in free fall showing the distance h fallen from rest under gravitational acceleration g with no air resistance — the ball accelerates uniformly downward, illustrating the $h = \frac{1}{2}gt^2$ relationship used to determine g from the gradient of an h against $t^2$ graph.*
*Source: Free fall — Pieter Kuiper — Public domain — https://commons.wikimedia.org/wiki/File:Free_fall.svg. Retrieved 2026-05-19.*

### From Wikipedia

<!-- wiki-images: yes -->

#### Gravity anomalies on Earth

![[_attachments/09_Experiments-and-Practicals/Measuring-Acceleration-Due-to-Gravity--wiki-gravity-anomalies-on-earth.jpg]]
*Figure: from Wikipedia article "Gravity of Earth".*
*Source: Wikimedia Commons — [Gravity_anomalies_on_Earth.jpg](https://commons.wikimedia.org/wiki/File:Gravity_anomalies_on_Earth.jpg). Retrieved 2026-05-20.*

#### Earth-G-force

![[_attachments/09_Experiments-and-Practicals/Measuring-Acceleration-Due-to-Gravity--wiki-earth-g-force.png]]
*Figure: from Wikipedia article "Gravity of Earth".*
*Source: Wikimedia Commons — [Earth-G-force.png](https://commons.wikimedia.org/wiki/File:Earth-G-force.png). Retrieved 2026-05-20.*

#### EarthGravityPREM

![[_attachments/09_Experiments-and-Practicals/Measuring-Acceleration-Due-to-Gravity--wiki-earthgravityprem.svg]]
*Figure: from Wikipedia article "Gravity of Earth".*
*Source: Wikimedia Commons — [EarthGravityPREM.svg](https://commons.wikimedia.org/wiki/File:EarthGravityPREM.svg). Retrieved 2026-05-20.*

## Source Trace

- Source: OCR Practical Skills Handbook; The Physics Classroom; IOPSpark; OpenStax
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
