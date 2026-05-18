# Wiki Log

This log records major wiki operations.

## Format

```text
## [YYYY-MM-DD] action | title
- Created:
- Updated:
- Deferred:
- Notes:
```

## Entries

## [2026-05-18] setup | initial vault framework
- Created: project structure, `_meta` control layer, templates, MOCs, standards, state files
- Updated: index.md
- Deferred: skill implementation
- Notes: raw/ is immutable; ingestion workflow requires checkpoint before writes; page templates are mandatory; frontier pages are shallow maps only

## [2026-05-18] ingest | OCR Physics A (H556) Specification
- Created: 13_Sources/OCR-Specifications/OCR-Physics-A-H556-Specification.md
- Updated: 00_Home/OCR-Physics-Map.md (populated 6-module/sub-topic structure + assessment overview), index.md, .state/ingested.tsv, .state/aliases.tsv
- Deferred: per-topic atomic pages (created from future module content ingests); separate raw bookmark ocr-physics-h556-specification-update-2024.url to ingest separately
- Notes: raw file is a .url bookmark; structure read from official accredited H556 spec PDF v3.0 (© Cambridge OCR 2026). Layer = a-level-core (syllabus skeleton, not content). No atomic content pages. No copyrighted text reproduced (titles/section numbers/assessment facts only; PAG apparatus table referenced by §5g only). No source variations.

## [2026-05-18] ingest | OCR Physics A H556 — Specification at a Glance
- Created: (none — folded into existing source page per user choice B)
- Updated: 13_Sources/OCR-Specifications/OCR-Physics-A-H556-Specification.md (added related-raw bookmark + aliases + note), .state/ingested.tsv, .state/aliases.tsv
- Deferred: none
- Notes: raw file is a .url bookmark → OCR "specification at a glance" page; a condensed summary view of the same H556 spec. No new knowledge objects, no MOC change. Module list and component figures confirmed identical to the canonical spec page — no source variation. Layer = a-level-core.

## [2026-05-18] ingest | OCR Physics A H556 — Specification Updates (2024 cycle)
- Created: (none — folded into existing source page per user choice)
- Updated: 13_Sources/OCR-Specifications/OCR-Physics-A-H556-Specification.md (added Specification version history subsection + related-raw bookmark + aliases), .state/ingested.tsv, .state/aliases.tsv
- Deferred: none
- Notes: raw file is a .url bookmark → OCR subject-update / spec-change page. Documents superseded v2.7 cycle (5 Nov 2024; minor clarity edits to §1d/2c/3/3d/3e/4a/5c/5f; LOs & assessment unchanged; Data/Formulae booklet → 2025). Canonical record is v3.0 (2026). Pure versioning metadata — no knowledge objects, no MOC change, no source variation. Layer = a-level-core.

## [2026-05-18] ingest | OCR Physics A H556 — Official Spec PDF (deeper pass)
- Created: (none)
- Updated: 00_Home/OCR-Physics-Map.md (enriched with all 66 third-level §2c sub-topics under each second-level heading), 13_Sources/OCR-Specifications/OCR-Physics-A-H556-Specification.md (recorded PDF as primary local provenance), .state/ingested.tsv
- Deferred: per-topic atomic pages still deferred to content-source ingests (spec is skeleton; empty stubs would violate §5.6/§5.10)
- Notes: raw file = official accredited spec PDF, byte-identical to the bookmark-sourced doc (v3.0 © Cambridge OCR 2026, 96pp) — no source variation. Deeper pass per user choice A: third-level structure (numbers + short titles only, no LO prose) added to [[OCR-Physics-Map]]. Layer = a-level-core. No new aliases.

## [2026-05-18] ingest | OCR Physics Mathematical Skills Handbook
- Created: 13_Sources/OCR-Specifications/OCR-Physics-Mathematical-Skills-Handbook.md
- Updated: 01_MOCs/Mathematical-Methods-in-Physics-MOC.md (added OCR Mathematical Skills Framework M0–M4 section + Sources), index.md, .state/ingested.tsv, .state/aliases.tsv
- Deferred: per-skill atomic method/representation pages (M0.1…M4.7) — created from future content-source ingests
- Notes: OCR Mathematical Skills Handbook v1.3 (Feb 2026). Maps M0–M4 framework (no M5). Also covers Physics B (H157/H557) — out of H556 scope, recorded as scope note; only M-framework mapped. M-codes are DfE/OCR factual identifiers; descriptors paraphrased, no handbook prose/worked examples copied. No atomic pages (skills framework, not content). No source variation. Layer = a-level-core. 00_Home/Mathematical-Methods-Map.md left unchanged (thematic tracker, different purpose).

## [2026-05-18] ingest | OCR Physics Practical Skills Handbook
- Created: 13_Sources/OCR-Specifications/OCR-Physics-Practical-Skills-Handbook.md; 04_Concepts/Measurement-Uncertainty.md, Systematic-and-Random-Errors.md, Resolution-Accuracy-and-Precision.md; 07_Methods/Estimating-Uncertainty-from-Apparatus.md, Combining-Uncertainties.md, Calculating-Percentage-Uncertainty.md, Significant-Figures-in-Measurements.md, Calculating-Percentage-Difference.md; 08_Representations/Results-Table.md, Line-of-Best-Fit-Graph.md
- Updated: 01_MOCs/Practical-Skills-MOC.md (skills framework + PAG1–PAG12 + linked new pages), index.md, .state/ingested.tsv, .state/aliases.tsv, .state/unresolved-links.md
- Deferred: individual experiment-practical pages (full methods on Teach Cambridge, not in PDF); uncertainty/graph problem-type & mistake-pattern pages → future /physics-problem-extract
- Notes: OCR Practical Skills Handbook v2.1 (Jan 2026), PDF supplied by user after the .url bookmark proved gated. 10 atomic pages created (3 concept, 5 method, 2 representation) — all original/paraphrased explanations, formula-level rules + page refs only, no verbatim text. All targets new → no source variation. Layer = a-level-core. Full-scope pass per user confirmation.

## [2026-05-18] ingest | OCR GCSE Gateway Physics A (J249) Specification
- Created: 13_Sources/GCSE-Physics/OCR-GCSE-Gateway-Physics-A-J249-Specification.md
- Updated: 01_MOCs/GCSE-Foundations-MOC.md (added GCSE syllabus structure P1–P9 + assessment + aliases + Sources), index.md, .state/ingested.tsv, .state/aliases.tsv
- Deferred: per-topic GCSE-foundation atomic pages (P1.1…P8.3) → future GCSE teaching-content ingests; bridge-to-A-Level pages linking GCSE P-topics to H556 modules
- Notes: OCR GCSE (9–1) Gateway Science Physics A J249, v4.2 (Feb 2024), 104pp. Syllabus skeleton only (no atomic content pages — empty foundation stubs would violate §5.6/§5.10). Layer = gcse-foundation. Factual topic/section structure + assessment only; no LO prose copied. Clean slate — no source variation.
