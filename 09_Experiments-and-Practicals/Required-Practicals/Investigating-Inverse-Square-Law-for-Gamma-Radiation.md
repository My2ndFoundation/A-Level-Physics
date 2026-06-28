---
type: experiment-practical
subject: physics
tags:
  - practical
  - required-practical
  - aqa-7407-7408
  - a-level-physics
  - nuclear-physics
  - radioactivity
level: a-level
difficulty: 3
status: draft
aliases:
  - AQA Required Practical 12
  - Gamma Inverse Square Law
  - RP12
sources: []
---

# Investigating Inverse Square Law for Gamma Radiation

## Aim

Show that the corrected count rate from a small gamma source falls as the inverse square of distance, consistent with [[Intensity]] spreading over a sphere of area `4πd²`.

## Variables

- Independent variable: distance `d` between the gamma source and the front face of the Geiger–Müller (GM) tube (m).
- Dependent variable: corrected count rate `C` (counts per second), found from total count divided by counting time, then with background subtracted.
- Control variables: same source and GM tube throughout, same counting time per reading, geometry (source square-on to tube), background measured before and after the run.

## Apparatus

- Sealed gamma source (e.g. cobalt-60 or radium-226) in a long-handled holder.
- GM tube on a clamp, connected to a ratemeter/scaler with timer.
- Metre rule taped to the bench so the source can be moved along a straight line away from the tube.
- Stopwatch (if using a manual scaler).

## Method

1. With the source locked in its store, measure the background count `B` over at least three intervals of (say) 60 s; record the mean background count rate.
2. Place the source `0.05 m` from the GM tube face; record total counts over a fixed time (e.g. 60 s).
3. Move the source to `0.10, 0.15, 0.20, …, 0.50 m`, recording counts for the same time at each.
4. Repeat each distance and take a mean.
5. Re-measure background at the end of the experiment.

## Measurements

- Distance `d` from source to tube (m).
- Total counts `N` in fixed time `t`.
- Background counts `N_B` in the same `t`.

## Data Processing

Corrected count rate:

`C = (N − N_B) / t`.

If [[Intensity]] obeys an inverse-square law, `C = k / d²`.

There is an unknown offset `x` between the centre of the source/tube and the marked distance, so write `r = d + x` and `C = k / (d + x)²`. Rearranging,

`1/√C = (1/√k) · (d + x)`.

## Graph Use

- Easiest test: plot `C` (y) against `1/d²` (x). A straight line through the origin supports inverse-square behaviour; gradient = `k`.
- Better when the source–tube offset matters: plot `1/√C` (y) against `d` (x). A straight line confirms inverse-square; the x-intercept gives `−x`, i.e. the geometric offset between the marked distance and the true source-to-detector distance.
- See [[Linearising-a-Graph]] and [[Finding-Gradient-from-a-Graph]].

## Uncertainty

- Statistical: for a count `N`, the standard uncertainty is `√N`; long counting times reduce the fractional error.
- Background drift: take fresh background readings if anything in the lab changes.
- Distance: parallax in reading `d`; source-centre and tube-window positions are not the marked positions — this is exactly what `x` captures.
- Combine uncertainties in `C`, `d`, and any computed `1/d²` using [[Combining-Uncertainties]].

## Safety / Practical Limits

- Use long-handled tongs; do not point the source at people or yourself.
- Keep distances and times to the minimum needed for sensible statistics — minimise exposure.
- Return the source to the locked store as soon as the run is finished; record use in the source log.
- Follow the school's CLEAPSS guidance for sealed sources; only a qualified user should retrieve them.

## Related Quantities

- [[Activity]]
- [[Intensity]]

## Related Laws or Results

- Inverse-square law for radiation intensity
- [[Radioactivity]]

## Common Mistakes

- Forgetting to subtract background, so the data looks like `C → const` at large `d`.
- Ignoring the source-to-detector offset and being puzzled when a `C` vs `1/d²` line misses the origin.
- Treating `√N` uncertainty as a percentage of distance rather than of count.

## Visuals

### Geometry and offset

```mermaid
flowchart LR
    Src[Gamma source] -- marked d --> Mark[Ruler reading]
    Mark -. true distance r = d + x .- Tube[GM tube window]
```

*Figure: The marked distance `d` and the true source-to-window distance `r` differ by a constant offset `x`, which the `1/√C` vs `d` plot reveals.*
*Source: Authored for this vault (CC0). No external copyright.*

## Source Trace

- Source: [[AQA-Physics-7407-7408-Specification]] §3.8 (Required practical 12)
- Public reference: AQA practical handbook (referenced, not copied); IOPSpark inverse-square-law-for-gamma guidance.
