# Unresolved Links

This file tracks quantities, concepts, laws, models, methods, representations, experiments, applications, foundation ideas, frontier maps, or sources mentioned during ingestion but not yet resolved to a canonical page.

## Open Items

- Mistake-pattern candidates from the Practical Skills Handbook ingest (2026-05-18), for a future `/physics-problem-extract`:
  - Confusing systematic vs random error → relates to [[Systematic-and-Random-Errors]]
  - Using wrong significant figures in a final answer → relates to [[Significant-Figures-in-Measurements]]
  - Adding absolute (not percentage) uncertainties for a product/quotient → relates to [[Combining-Uncertainties]]
- Problem-type candidates: uncertainty propagation questions; gradient/intercept-from-graph questions → relate to [[Combining-Uncertainties]], [[Line-of-Best-Fit-Graph]] (defer to past-paper ingest).

- **[[SI-Units]]** — referenced by [[Measurement-Uncertainty]] and [[Resolution-Accuracy-and-Precision]] (links retargeted to [[Physical-Quantities-MOC]] on 2026-05-18 as an interim). Wants a canonical `physical-quantity`/`concept` page on SI base units; create from a content-source ingest, then restore direct links.

- Lint 2026-05-18 — known placeholder links in pre-existing seed hub pages, pending canonical pages (do not edit the seed hubs; resolve as content is ingested):
  - From `00_Home/Mathematical-Methods-Map.md`: [[Gradient]], [[Area-Under-a-Graph]], [[Linearising-a-Graph]], [[Rearranging-Equations]], [[Dimensional-Analysis]], [[Resolving-Forces]], [[Vector-Components]], [[Projectile-Motion]], [[Simple-Harmonic-Motion]], [[Capacitor-Discharge]], [[Radioactive-Decay]], [[Acceleration-Time-Graph]]
  - From `00_Home/Cross-Subject-Links.md`: [[Differentiation]], [[Integration]], [[Vectors]], [[Trigonometry]], [[Exponential-Decay]], [[Differential-Equations]], [[Numerical-Modelling]], [[Simulation]], [[Sensors]], [[Data-Logging]], [[Signal-Processing]], [[Logic-Gates]], [[Semiconductor-Physics-Map]]
  - From seed atomic pages: [[Momentum]] (Why-Seatbelts-Matter), [[Photoelectric-Effect]] (Quantum-Mechanics-Map)

## Baseline build 2026-05-18 — mentioned-but-not-yet-built atomic pages

Created during the usable-baseline pass as forward wikilinks; resolve in a future
content ingest / second pass (not lint errors — deliberate graph stubs):

- Forces/mechanics: [[Balanced-and-Unbalanced-Forces]], [[Contact-and-Non-Contact-Forces]], [[Normal-Contact-Force]], [[Coefficient-of-Friction]], [[Adding-Forces-as-Scalars]], [[Principle-of-Moments]], [[Levers]], [[Energy-Transfer]], [[Area]]
- Electricity: [[Electromotive-Force]]
- Waves: [[Principle-of-Superposition]], [[Path-Difference]], [[Phase-Difference]], [[Diffraction-Grating-Equation]], [[Electromagnetic-Spectrum]], [[Law-of-Reflection]], [[Reflection-and-Refraction]]
- Quantum/nuclear: [[Bohr-Model]], [[Nuclear-Model]], [[Atomic-Structure]], [[Isotopes]], [[Binding-Energy]], [[Mass-Defect]], [[Mass-Energy-Equivalence]], [[Decay-Constant]], [[Activity]], [[Radioactivity]], [[Photon-Energy]], [[Ionisation-Energy]]
- Canonicalised this pass: [[Refraction-of-Waves]] → alias of [[Wave-Refraction]] (added to page frontmatter aliases + .state/aliases.tsv).

Note: targets like [[OCR-Physics-A-H556-Specification]], [[CERN-Science]], [[NASA-Astrophysics]], [[IOP-Explore-Physics]], and the topic MOCs DO resolve (they live in 13_Sources/ and 01_MOCs/); they appeared in a content-folder-only probe and are not broken.
