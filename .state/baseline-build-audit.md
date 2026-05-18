# Baseline Build Audit

_Generated 2026-05-18 for the usable-baseline construction pass._

## Existing Structure

Full canonical folder tree present (`00_Home/` … `13_Sources/`, `_meta/`, `raw/`, `.state/`).
Sub-structure already in place: `02_Foundations/{Everyday-Physics,Pre-GCSE-Foundations,GCSE-Foundations,Bridge-to-A-Level}`, `09_Experiments-and-Practicals/{Measurement-and-Uncertainty,Graph-Analysis,Apparatus-and-Techniques,Required-Practicals}`, `11_Problems/{Problem-Types,Worked-Examples,Mistake-Patterns,Extension-Problems}`, `13_Sources/*`.

## Existing Skills

`.claude/skills/`: physics-ingest-source, physics-build-moc, physics-lint-wiki, physics-scan-raw, physics-expand-concept, physics-frontier-map, physics-practical-extract, physics-problem-extract. All high quality and already CLAUDE.md-compliant.

**This pass adds:** physics-source-research, physics-complete-page, physics-build-base-cluster (new); light baseline-policy cross-references added to physics-ingest-source, physics-build-moc, physics-lint-wiki.

## Existing Templates

All 16 page-type templates present under `_meta/templates/` (foundation, common-sense, frontier-map, physical-quantity, concept, law-result, model, method, representation, experiment-practical, application, problem-type, worked-example, mistake-pattern, moc, source). Authoritative — not modified.

## Current Page Counts by Type (content layer, pre-build)

| Folder | Pages |
|---|---|
| 02_Foundations | 4 (Force, Energy, From-Speed-to-Velocity, Why-Seatbelts-Matter) |
| 03_Physical-Quantities | 1 (Acceleration) |
| 04_Concepts | 3 (uncertainty cluster) |
| 05_Laws-and-Results | 1 (Newton-Second-Law) |
| 06_Models | 1 (Constant-Acceleration-Model) |
| 07_Methods | 6 (SUVAT + uncertainty methods) |
| 08_Representations | 3 (Velocity-Time-Graph, Results-Table, Line-of-Best-Fit-Graph) |
| 09_Experiments-and-Practicals | 0 |
| 10_Applications | 0 |
| 11_Problems | 1 (Confusing-Mass-and-Weight) |
| 12_Frontier-Maps | 3 (Quantum-Mechanics, Particle-Physics, Cosmology) |
| 01_MOCs | ~30 (skeletons, mostly empty section bodies) |
| 13_Sources | 7 (OCR specs/handbooks, frontier refs) |

## Current Seed/Draft/Usable Counts

Almost all content pages `status: seed` or thin `draft`. Uncertainty/practical-skills cluster (07_Methods, the 3 concept pages, 2 representation pages) is the only substantially-populated area (from the Practical Skills Handbook ingest). No `usable`+ pages.

## Empty or Near-Empty Pages

Nearly the entire content layer. MOC bodies largely `_To be populated._`. 03/04/05/06/10 essentially empty. The required-baseline list (~200 pages) is overwhelmingly missing.

## Missing Core Areas

Mechanics core (kinematics quantities, Newton's laws, momentum/energy), materials, electricity/circuits, waves, quantum-entry, fields, thermal/nuclear/medical/astro, applications, mistake patterns, and the bridge/foundation/common-sense layer are all missing or stub-only.

## Source Files Available

`raw/`: OCR H556 spec PDF + maths/practical handbooks + GCSE J249 spec PDF + frontier `.url` bookmarks (CERN/IOP/NASA). All already ingested as source-trace pages. No textbook/past-paper raw files yet. Baseline content is therefore built from the **trusted public source pool** (OCR spec for syllabus alignment + OpenStax / Physics Classroom / HyperPhysics / IOPSpark / Khan / LibreTexts for explanation) — paraphrased, no copyrighted text.

## Recommended Build Clusters

Partitioned **by page-type folder** (clean, non-overlapping write targets so parallel agents never collide). MOC/index/log updates done centrally after page construction. Order: foundations → physical-quantities → concepts → laws → models+methods → representations+experiments → applications+mistakes → frontier-maps.

## Notes

- Pre-existing seed pages (Acceleration, Newton-Second-Law, Constant-Acceleration-Model, From-Speed-to-Velocity, Force, Energy, Velocity-Time-Graph, Confusing-Mass-and-Weight, the 3 frontier maps, uncertainty cluster) are **completed in place**, not recreated — preserve content, append source trace, never silent-overwrite (CLAUDE.md §5.4).
- Cross-type duplicate guard: `Conservation-of-Energy` / `Conservation-of-Momentum` are canonical as `law-result` (05); the Concepts pass does not create rival pages. GCSE-foundation `Force/Energy/Power/Current/Voltage/Resistance/Waves` (02) and their A-Level `physical-quantity` pages (03) are intentionally distinct layers (CLAUDE.md §2), cross-linked, not duplicates.
- No auto-commit (CLAUDE.md §5.11).
