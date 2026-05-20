---
type: application
subject: physics
tags:
  - gravitational-fields
  - newtonian-world
  - a-level-core
  - technology-link
level: a-level
difficulty: 2
status: usable
aliases:
  - Geostationary Orbit
  - Satellites
  - Geosynchronous Orbit
sources: []
---

# Satellites and Geostationary Orbits

## Problem Context

Artificial satellites orbit Earth under gravity alone. A **geostationary**
satellite has an orbit chosen so it appears fixed above one point on the
equator — the basis of satellite TV, communications and weather monitoring.

## Physical Ideas

- [[Orbital-Motion]]
- [[Gravitational-Field]]
- [[Circular-Motion]]
- [[Centripetal-Force]]
- [[Newtons-Law-of-Gravitation]]

## Mathematical Tools

- [[Keplers-Third-Law]]
- [[Using-Keplers-Third-Law]]

## Typical Questions

- Show that a geostationary orbit has a period of 24 hours and radius
  $\approx 4.2 \times 10^7\ \text{m}$ (about $3.6 \times 10^7\ \text{m}$ above the surface).
- Compare a low polar orbit with a geostationary orbit.
- Calculate the speed of a satellite at a given orbital radius.

## Method Outline

1. State the geostationary conditions: period $T = 24\ \text{h}$ (one sidereal day),
   equatorial orbit, west-to-east direction matching Earth's rotation.
2. Apply the orbital condition $\frac{GMm}{r^2} = m\omega^2 r$ with $\omega = \frac{2\pi}{T}$.
3. Rearrange to $r^3 = \frac{GMT^2}{4\pi^2}$ ([[Keplers-Third-Law]]) and solve for r.
4. Subtract Earth's radius to get the height above the surface, or use
   $v = \sqrt{\frac{GM}{r}}$ for orbital speed.

## Assumptions

- Circular orbit
- Earth treated as a point mass / uniform sphere
- Only Earth's gravity acts (drag and other bodies neglected)
- Satellite mass negligible compared with Earth's

## Links to Other Subjects

- Mathematics: rearranging equations, indices and powers of ten
- Computer Science: satellite-based GPS positioning and communication links

## Frontier Links

- [[Cosmology-Map]]

## Common Mistakes

- Using height above the surface instead of radius from Earth's centre
- Thinking a geostationary satellite is stationary in space (it orbits at
  ~3 km s⁻¹)
- Placing a geostationary satellite over the poles (it must be equatorial)
- Forgetting period must be one sidereal day, not exactly the calendar day

## Visuals

### Geostationary Satellite Weather Imagery
![[_attachments/10_Applications/Satellites-and-Geostationary-Orbits--geostationary-imagery.png]]
*Figure: Full-disc Earth image taken from a geostationary satellite (GOES/Himawari). Because the satellite stays fixed above the equator at ~36,000 km, it captures the same face of Earth continuously — the basis of weather monitoring and communications.*
*Source: Geostationary Satellite imagery — NOAA, JMA — Public Domain — https://commons.wikimedia.org/wiki/File:Geostationary_Satellite_imagery.png. Retrieved 2026-05-19.*

### From Wikipedia

<!-- wiki-images: yes -->

#### Geostationaryjava3D

![[_attachments/10_Applications/Satellites-and-Geostationary-Orbits--wiki-geostationaryjava3d.gif]]
*Figure: from Wikipedia article "Geostationary orbit".*
*Source: Wikimedia Commons — [Geostationaryjava3D.gif](https://commons.wikimedia.org/wiki/File:Geostationaryjava3D.gif). Retrieved 2026-05-20.*

#### Animation of EchoStar XVII trajectory

![[_attachments/10_Applications/Satellites-and-Geostationary-Orbits--wiki-animation-of-echostar-xvii-trajectory.gif]]
*Figure: from Wikipedia article "Geostationary orbit".*
*Source: Wikimedia Commons — [Animation of EchoStar XVII trajectory.gif](https://commons.wikimedia.org/wiki/File:Animation_of_EchoStar_XVII_trajectory.gif). Retrieved 2026-05-20.*

#### Animation of EchoStar XVII trajectory Equatorial view

![[_attachments/10_Applications/Satellites-and-Geostationary-Orbits--wiki-animation-of-echostar-xvii-trajectory-eq.gif]]
*Figure: from Wikipedia article "Geostationary orbit".*
*Source: Wikimedia Commons — [Animation of EchoStar XVII trajectory Equatorial view.gif](https://commons.wikimedia.org/wiki/File:Animation_of_EchoStar_XVII_trajectory_Equatorial_view.gif). Retrieved 2026-05-20.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; NASA educational material — no copied text
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
- Section/Page: OCR M5.4 Gravitational fields
