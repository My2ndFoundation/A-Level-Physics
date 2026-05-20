---
type: application
subject: physics
tags:
  - medical-physics
  - quantum-physics
  - electrons-waves-and-photons
  - a-level-core
level: a-level
difficulty: 2
status: usable
aliases:
  - CT Scan
  - Computed Tomography
  - CAT Scan
sources: []
---

# CT Scanning

## Problem Context

Building a three-dimensional, cross-sectional map of the body from many X-ray projections taken at different angles, overcoming the depth ambiguity of a single flat radiograph.

## Physical Ideas

- [[Photon-Energy]]
- [[Electromagnetic-Spectrum]]

## Mathematical Tools

- Exponential attenuation $I = I_0 e^{-\mu x}$ along each ray path.
- Reconstruction combines projections from many angles to solve for the attenuation at each volume element (voxel).

## Typical Questions

- Explain why a CT scan gives more diagnostic information than a single X-ray.
- State why a CT scan delivers a higher radiation dose than a plain radiograph.
- Describe how rotating the X-ray source and detectors enables 3D imaging.

## Method Outline

1. An X-ray source and ring of detectors rotate around the patient (often as the table advances — helical scanning).
2. Attenuation is recorded along thousands of ray paths at many angles.
3. A computer reconstructs the attenuation coefficient for each voxel by back-projection algorithms.
4. Voxel values are mapped to greyscale, producing slice images that stack into a 3D dataset.

## Assumptions

- Patient stationary during a slice acquisition (motion causes artefacts).
- Beam treated as effectively monoenergetic for teaching-level calculations.

## Links to Other Subjects

- Mathematics: linear algebra and reconstruction (back-projection) ideas.
- Computer Science: large-scale image reconstruction and rendering.

## Frontier Links

- Iterative reconstruction and dose reduction; orientation only.

## Common Mistakes

- Thinking CT uses a different type of radiation from plain X-rays (it uses the same X-ray photons).
- Underestimating the higher dose compared with a single radiograph.

## Visuals

### CT Scanner in a Hospital
![[_attachments/10_Applications/CT-Scanning--ct-scanner.jpg]]
*Figure: A 64-slice CT scanner showing the large rotating gantry ring into which the patient table slides. The ring houses the X-ray source and the opposite detector array that rotate together.*
*Source: Lachine Hospital CT Scanner — Ptrump16 — CC BY-SA 4.0 — https://commons.wikimedia.org/wiki/File:Lachine_Hospital_CT_Scanner.jpg. Retrieved 2026-05-19.*

### From Wikipedia

<!-- wiki-images: yes -->

#### Drawing of CT fan beam (left) and patient in a CT imaging system

![[_attachments/10_Applications/CT-Scanning--wiki-drawing-of-ct-fan-beam-left-and-patient-.gif]]
*Figure: from Wikipedia article "CT scan".*
*Source: Wikimedia Commons — [Drawing_of_CT_fan_beam_(left)_and_patient_in_a_CT_imaging_system.gif](https://commons.wikimedia.org/wiki/File:Drawing_of_CT_fan_beam_(left)_and_patient_in_a_CT_imaging_system.gif). Retrieved 2026-05-20.*

#### 12-06-11-rechtsmedizin-berlin-07

![[_attachments/10_Applications/CT-Scanning--wiki-12-06-11-rechtsmedizin-berlin-07.jpg]]
*Figure: from Wikipedia article "CT scan".*
*Source: Wikimedia Commons — [12-06-11-rechtsmedizin-berlin-07.jpg](https://commons.wikimedia.org/wiki/File:12-06-11-rechtsmedizin-berlin-07.jpg). Retrieved 2026-05-20.*

#### Axial plane CT scan of the thorax illustrative image

![[_attachments/10_Applications/CT-Scanning--wiki-axial-plane-ct-scan-of-the-thorax-illust.jpg]]
*Figure: from Wikipedia article "CT scan".*
*Source: Wikimedia Commons — [Axial plane CT scan of the thorax illustrative image.jpg](https://commons.wikimedia.org/wiki/File:Axial_plane_CT_scan_of_the_thorax_illustrative_image.jpg). Retrieved 2026-05-20.*

## Source Trace

- Source: OpenStax College Physics; HyperPhysics; IOPSpark
- OCR alignment: [[OCR-Physics-A-H556-Specification]]
- Related: [[Medical-Imaging]]
