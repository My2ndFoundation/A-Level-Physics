---
type: method
subject: physics
tags:
  - aqa-7407-7408
  - a-level-physics
  - mechanics
  - engineering-physics
  - rotational-dynamics
  - problem-solving
level: a-level
difficulty: 3
status: draft
aliases:
  - Rotational Dynamics Method
  - Solving Engineering Physics Rotational Problems
sources: []
---

# Solving Rotational Dynamics Problems

## Purpose

A general decision procedure for AQA Engineering Physics rotational problems: pick the right rotational analogue tool — kinematics, Newton's second law, energy, or angular-momentum conservation — and apply it cleanly.

## When to Use

- A problem involves rotation about a **fixed axis** of a rigid body, gear train, flywheel, motor shaft, or similar.
- Quantities to handle are angular: $\theta$, $\omega$, $\alpha$, $T$, $I$, $L = I\omega$, $E_k = \tfrac{1}{2}I\omega^{2}$.
- A force in the problem acts at a distance from the axis, or you are told a torque, moment of inertia, or angular velocity.

## Prerequisites

- [[Rotational-Motion]]
- [[Moment-of-Inertia]]
- [[Torque-and-Angular-Acceleration]]
- [[Conservation-of-Angular-Momentum]]
- [[Rotational-Kinetic-Energy]]
- [[Using-SUVAT-Equations]]
- [[Radian]]

## Method

1. **Identify the axis** of rotation. Every $I$, $T$, and $L$ in your working must refer to this axis.
2. **List the rotational analogues** for each linear quantity in the problem ($s \to \theta$, $m \to I$, $F \to T$, $p \to L$, $\tfrac{1}{2}mv^{2} \to \tfrac{1}{2}I\omega^{2}$, $W = Fs \to W = T\theta$, $P = Fv \to P = T\omega$).
3. **Choose the right tool** by looking at what is given:
   - Constant $\alpha$ and a kinematics question (find $\theta$, $\omega$, or $t$): use rotational SUVAT from [[Rotational-Motion]].
   - A torque acts and you want $\alpha$ (or vice versa): use $T = I\alpha$ from [[Torque-and-Angular-Acceleration]] — include frictional torque if present.
   - Energy in / out, or a "stored energy" or speed-from-energy question: use $E_k = \tfrac{1}{2}I\omega^{2}$, work $W = T\theta$, and [[Conservation-of-Energy]].
   - Power delivered or absorbed by a torque: $P = T\omega$.
   - No external torque between two states: use [[Conservation-of-Angular-Momentum]], $I_1\omega_1 = I_2\omega_2$.
   - Known torque applied for known time: angular impulse $T\,\Delta t = \Delta(I\omega)$.
4. **Convert units**: $\omega$ in rad s⁻¹, $\alpha$ in rad s⁻², $T$ in N m. Convert revolutions or rev min⁻¹ to radians and seconds before substituting.
5. **Substitute and solve**. Check the answer's order of magnitude against the linear analogue you already trust.

## Worked Example

A flywheel of moment of inertia $I = 0.40\ \mathrm{kg\,m^{2}}$ is at rest. A constant torque $T = 2.0$ N m is applied for $5.0$ s.

- $\alpha = T/I = 2.0/0.40 = 5.0\ \mathrm{rad\,s^{-2}}$.
- Final $\omega = \alpha t = 5.0 \times 5.0 = 25\ \mathrm{rad\,s^{-1}}$.
- Stored energy $E_k = \tfrac{1}{2}I\omega^{2} = \tfrac{1}{2}(0.40)(25)^{2} = 125\ \mathrm{J}$.
- Check using work: $\theta = \tfrac{1}{2}\alpha t^{2} = 62.5$ rad, $W = T\theta = 2.0 \times 62.5 = 125$ J. ✓

## Why It Works

Every step uses an exact rotational counterpart of a linear law you already trust. $T = I\alpha$ comes from applying [[Newton-Second-Law]] to each mass element and summing. Energy and momentum results follow from the same accounting in angular variables.

## Common Mistakes

- Forgetting to convert revolutions or degrees to radians.
- Using $I$ about a different axis from $T$ or $L$.
- Ignoring frictional torque, then being surprised that $\alpha$ is smaller than predicted.
- Using $T = I\alpha$ when $T$ is not constant — that gives $\alpha$ only at the instant when $T$ has the stated value.
- Assuming rotational KE is conserved during internal rearrangement (it usually is not — only $L$ is, when no external torque acts).

## Related Quantities

- [[Moment-of-Inertia]]
- [[Angular-Velocity]]
- [[Angular-Momentum]]
- [[Work]]
- [[Power]]

## Related Laws or Results

- [[Torque-and-Angular-Acceleration]]
- [[Conservation-of-Angular-Momentum]]
- [[Conservation-of-Energy]]
- [[Newton-Second-Law]]

## Related Problem Types

- [[...]]

## Source Trace

- Source: [[AQA-Physics-7407-7408-Specification]] §3.11.1 (Engineering Physics — Rotational dynamics)
- Section/Page: Public reference — HyperPhysics; OpenStax College Physics
