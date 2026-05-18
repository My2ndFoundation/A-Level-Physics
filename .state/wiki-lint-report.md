# Wiki Lint Report

- **Generated:** 2026-05-18 (read-only audit; no files fixed)
- **Scope:** `00_Home`, `01_MOCs`, `02_Foundations` … `13_Sources`, `index.md` (excluded: `_meta/`, `raw/`, `.state/`, `.git/`, `.obsidian/`)
- **Authority:** `_meta/workflows/lint-workflow.md` + CLAUDE.md §13

## Summary

| # | Check | Result |
|---|-------|--------|
| 1 | Missing / partial frontmatter | **16** (8 high, 8 med) |
| 2 | type vs folder mismatch | 0 |
| 3 | Required template-section violations | 0 |
| 4 | Missing source trace | **24** (med) |
| 5 | Orphan pages | 0 |
| 6 | Broken wikilinks | **18 genuine targets** (+ 6 `.state` op-file refs from `index.md`, low) |
| 7 | Duplicate aliases | **24 alias keys** — 20 expected physics-symbol/link-form collisions, **4 needing a human canonical-owner decision** |
| 8 | Broad-topic content pages that should be MOCs | **3** (2 intentional layer-model, 1 to review) |
| 9 | MOCs missing links to existing topic pages | 0 (all atomic pages linked in ≥1 MOC/Home) |
| 10 | Pages > 800 words | **2** (both source/index, borderline) |
| 11 | Physics-quality gaps (§12) | 0 |
| 12 | Frontier-depth violations (§3) | **2** (low — single term mentions, shallow) |
| 13 | seed/draft pages in content folders | 0 |

**Inventory:** 370 Markdown files in scope — 02_Foundations 19, 03_Physical-Quantities 49, 04_Concepts 87, 05_Laws-and-Results 29, 06_Models 13, 07_Methods 29, 08_Representations 20, 09_Experiments-and-Practicals 16, 10_Applications 19, 11_Problems 38, 12_Frontier-Maps 7, 13_Sources 7, 01_MOCs 30, 00_Home 6, index.md 1.

Overall health is strong: no orphans, no template-section violations, no type/folder mismatches, no seed/draft pages, no §12 physics-quality gaps, full MOC coverage. The actionable items are: missing source-page frontmatter keys, an under-populated source trace + frontmatter `aliases` on the problem layer, ~18 genuinely-missing link targets, and 4 word-level alias collisions needing a canonical-owner decision.

---

## 1. Missing / Partial Frontmatter

Non-MOC content pages must carry `type, subject, tags, level, status, aliases, sources` (CLAUDE.md §5.7).

**HIGH — source pages missing `level` and `sources`:**

| File | Missing | Action |
|------|---------|--------|
| `13_Sources/Frontier-References/IOP-Explore-Physics.md` | level, sources | Add `level:` (frontier) and `sources:` (self/URL) keys |
| `13_Sources/Frontier-References/NASA-Astrophysics.md` | level, sources | Same |
| `13_Sources/Frontier-References/CERN-Science.md` | level, sources | Same |
| `13_Sources/OCR-Specifications/OCR-Physics-A-H556-Specification.md` | level, sources | Add `level: a-level-core`, `sources:` self-ref |
| `13_Sources/OCR-Specifications/OCR-Physics-Practical-Skills-Handbook.md` | level, sources | Same |
| `13_Sources/OCR-Specifications/OCR-Physics-Mathematical-Skills-Handbook.md` | level, sources | Same |
| `13_Sources/GCSE-Physics/OCR-GCSE-Gateway-Physics-A-J249-Specification.md` | level, sources | Add `level: gcse-foundation`, `sources:` self-ref |
| `index.md` | no frontmatter block | Treated as MOC/home — low impact; add minimal `type: moc` block if desired |

Note: `source-template.md` does not mandate `level`/`sources` the same way atomic pages do; these are flagged for §5.7 consistency but are **medium-real** for source pages. Treat the 7 source pages as a uniform batch fix.

**MED — worked-example pages missing `aliases`:**

`11_Problems/Worked-Examples/` — all 8 pages missing the `aliases:` key:
`Worked-Momentum-Collision.md`, `Worked-Capacitor-Discharge-RC.md`, `Worked-Binding-Energy-per-Nucleon.md`, `Worked-SHM-Mass-Spring.md`, `Worked-Potential-Divider-Thermistor.md`, `Worked-Circular-Motion-Conical-Pendulum.md`, `Worked-SUVAT-Cliff-Projectile.md`, `Worked-Photoelectric-Stopping-Potential.md`

Action: add `aliases: []` to each for §5.7 conformance. Low risk, mechanical.

## 2. type vs Folder Mismatch

**None.** Every page's `type` frontmatter matches its folder per the CLAUDE.md §4 map.

## 3. Required Template-Section Violations

**None.** All content pages with a recognised `type` contain every required `##` section from the corresponding `_meta/templates/` template. Template discipline is fully maintained across the 326+ content pages.

## 4. Missing Source Trace

24 pages have BOTH `sources: []` AND an empty/absent `## Source Trace` section. All are in the problem layer — generated synthetically rather than extracted from a raw source, so this is expected by construction but should be acknowledged.

**Problem-Types (16):** `Projectile-Motion-Problem`, `Simple-Harmonic-Motion-Problem`, `Conservation-of-Momentum-Collision`, `Radioactive-Decay-Problem`, `Energy-Conservation-Problem`, `Interpret-a-Velocity-Time-Graph`, `Potential-Divider-Calculation`, `Capacitor-Discharge-Problem`, `Standing-Wave-Problem`, `Gravitational-Field-Problem`, `Find-Internal-Resistance-from-a-Graph`, `Series-Parallel-Circuit-Analysis`, `Circular-Motion-Problem`, `Calculate-Resultant-Force`, `Photoelectric-Effect-Calculation`, `SUVAT-Kinematics-Problem` (all under `11_Problems/Problem-Types/`)

**Worked-Examples (8):** all 8 pages under `11_Problems/Worked-Examples/` (same list as §1 MED).

Note: `problem-type-template.md` uses `## Example Sources` and `worked-example-template.md` uses `## Source Reference` (not `## Source Trace`), so the literal heading absence is template-correct; the real gap is those sections + `sources:` are empty. Action: populate with the originating spec reference (e.g. OCR H556 topic code) — medium priority, batchable.

## 5. Orphan Pages

**None.** Every non-source content page is reachable via an inbound wikilink or is referenced in a MOC.

## 6. Broken Wikilinks

Targets that resolve to no existing page basename, no alias in `.state/aliases.tsv`, and no frontmatter `aliases:` (case + `[[A|B]]` + `[[A#h]]` handled).

**Genuinely-missing targets (18) — create the page or retarget the link:**

| Missing target | Referenced by | Suggested type / action |
|---|---|---|
| `Adding-Forces-as-Scalars` | `04_Concepts/Resultant-Force.md` | mistake-pattern — create or retarget to existing mistake page |
| `Area` | `03_Physical-Quantities/Pressure.md` | physical-quantity — create or unlink (GCSE-trivial) |
| `Volume` | `03_Physical-Quantities/Density.md` | physical-quantity — create or unlink |
| `Balanced-and-Unbalanced-Forces` | `04_Concepts/Equilibrium.md`, `Resultant-Force.md`, `Terminal-Velocity.md` | foundation — create (3 inbound) |
| `Bohr-Model` | `04_Concepts/Energy-Levels.md`, `Ionisation.md` | model — create (2 inbound) |
| `Nuclear-Model` | `04_Concepts/Half-Life.md`, `Nuclear-Fission.md`, `Nuclear-Fusion.md`, `Radioactive-Decay.md` | model — create (4 inbound, high value) |
| `Rigid-Body-Model` | `04_Concepts/Centre-of-Mass.md`, `Equilibrium.md`, `Moment.md` | model — create (3 inbound) |
| `Principle-of-Moments` | `04_Concepts/Centre-of-Mass.md`, `Equilibrium.md`, `Moment.md` | law-result — create (3 inbound, examinable) |
| `Contact-and-Non-Contact-Forces` | `04_Concepts/Friction.md` | foundation — create or retarget |
| `Levers` | `04_Concepts/Moment.md` | application/foundation — create or unlink |
| `Reflection-and-Refraction` | `04_Concepts/Wave-Reflection.md`, `Wave-Refraction.md` | retarget to existing `Wave-Reflection`/`Wave-Refraction`, or create umbrella |
| `Series-and-Parallel-Circuits` | `04_Concepts/Potential-Divider.md` | retarget — likely meant `Series-Parallel-Circuit-Analysis` (exists) or a circuit foundation page |
| `Static-Electricity` | `04_Concepts/Ionisation.md` | foundation — create or unlink |
| `Wave` | `02_Foundations/Everyday-Physics/Why-Sky-Is-Blue.md`, `Why-Sound-Needs-a-Medium.md` | retarget to `02_Foundations/GCSE-Foundations/Waves.md` (exists) |
| `Confusing-Photon-Energy-and-Intensity` | `11_Problems/Problem-Types/Photoelectric-Effect-Calculation.md`, `Worked-Examples/Worked-Photoelectric-Stopping-Potential.md` | mistake-pattern — create (2 inbound) |
| `Confusing-Wavelength-and-Amplitude` | `11_Problems/Problem-Types/Standing-Wave-Problem.md` | mistake-pattern — create or unlink |
| `Mixing-Up-EMF-and-Terminal-PD` | `11_Problems/Problem-Types/Find-Internal-Resistance-from-a-Graph.md` | mistake-pattern — create (examinable trap) |
| `Treating-Centripetal-Force-as-an-Extra-Force` | `11_Problems/Problem-Types/Circular-Motion-Problem.md`, `Worked-Examples/Worked-Circular-Motion-Conical-Pendulum.md` | mistake-pattern — create (2 inbound, classic trap) |

**Non-content operational refs (6) — LOW, no action needed:** `index.md` links `[[log]]`, `[[unresolved-links]]`, `[[source-inventory]]`, `[[baseline-build-progress]]`, `[[baseline-build-audit]]`, `[[wiki-lint-report]]` — these point to `.state/` operational files intentionally out of content scope. Acceptable; optionally convert to relative paths or remove from `index.md`.

**Maths/CS bridge refs from `00_Home/Cross-Subject-Links.md` & `Mathematical-Methods-Map.md` (LOW, deferred):** `Data-Logging`, `Differential-Equations`, `Differentiation`, `Integration`, `Logic-Gates`, `Numerical-Modelling`, `Sensors`, `Signal-Processing`, `Simulation`, `Trigonometry`, `Dimensional-Analysis`, `Rearranging-Equations` — forward-looking maths/CS bridge stubs in Home maps. Acceptable as planned-but-unbuilt; build as `method`/`foundation` pages when the maths-bridge layer is constructed, or mark external. (Some are subsumed in the 18 above where they had a single canonical-looking name; treat as deferred, not urgent.)

## 7. Duplicate Aliases

No alias in `.state/aliases.tsv` maps to two different canonical pages. All 24 flagged keys come from **frontmatter `aliases:` fields**.

**Expected / NOT violations (20):**
- **Physics symbol collisions** (multiple physical-quantity pages legitimately share a symbol): `v` (Speed/Velocity/Potential-Difference), `p` (Momentum/Power/Pressure), `e`/`E` (Energy/Electric-Field-Strength/Young-Modulus), `a` (Acceleration/Amplitude), `f` (Force/Frequency), `i` (Current/Intensity), `w` (Weight/Work), `rho`/`ρ` (Density/Resistivity), `lambda` (Decay-Constant/Wavelength), `phi` (Magnetic-Flux/Work-Function). Inherent to physics notation; symbol is also defined in-page. Not a canonical-ownership conflict. Recommend: do not register bare single symbols as global aliases in `.state/aliases.tsv` (none currently are — good).
- **Link-form / synonym pairs that are conceptually the same or a deliberate two-layer split**: `breaking stress` (Breaking-Stress vs Stress — sub-quantity vs parent), `kinetic energy` (Energy GCSE-foundation vs Kinetic-Energy quantity — intentional §2 layer model, like Energy/Force/Power/Resistance), `resultant force`/`net force` (Force foundation vs Resultant-Force concept — intentional layer model), `radioactivity` (Activity vs Radioactive-Decay — related but distinct), `exponential decay of charge` (Capacitor-Discharge-Equation vs Capacitor-Discharge-Problem — law vs problem-type, distinct), `slope of a graph` (Finding-Gradient-from-a-Graph vs Using-Gradient), `field line diagram` (Electric- vs Magnetic-Field-Line-Diagram — distinct representations).

**NEEDS A HUMAN CANONICAL-OWNER DECISION (4):**

| Alias | Competing canonical pages | Recommendation |
|---|---|---|
| `voltage` | `Potential-Difference`, `Voltage` | Likely a true duplicate-page risk. Decide canonical owner (recommend `Potential-Difference`, fold `Voltage` → alias) per §5.3. |
| `potential divider` | `Potential-Divider`, `Potential-Divider-Model` | Concept vs model split may be intentional, but the shared alias is ambiguous. Confirm distinct purpose; if so, give each a unique alias; else merge. |
| `voltage divider calculation` | `Potential-Divider-Calculation` (problem-type), `Using-Potential-Dividers` (method) | Distinct types but identical alias — reassign alias to one (recommend the method) so links route deterministically. |
| `resolving vectors` | `Resolving-Forces`, `Resolving-Vectors` | If both exist as separate methods, confirm scope difference; otherwise consolidate (one canonical + alias). |

## 8. Broad-Topic Content Pages That Should Be MOCs

| File | type | Verdict |
|---|---|---|
| `02_Foundations/GCSE-Foundations/Energy.md` | foundation | **Intentional** — GCSE-foundation layer page coexisting with `03_Physical-Quantities/Energy.md` per CLAUDE.md §2 layer model. NOT a violation. |
| `03_Physical-Quantities/Energy.md` | physical-quantity | **Intentional** — A-Level quantity layer. NOT a violation. |
| `02_Foundations/GCSE-Foundations/Waves.md` | foundation | **Review.** `Waves` is on the §5.5 forbidden-broad-name list. As a GCSE-foundation layer page it is defensible (parallel to Energy/Force), but the bare name `Waves.md` risks collision with the MOC concept and is the root cause of the `[[Wave]]`/`[[Waves]]` link confusion in §6. Recommend rename (e.g. `Waves-GCSE-Foundation.md` or `What-Is-a-Wave.md`) keeping `Waves` as an alias, OR explicitly confirm it as the intended GCSE-layer twin. Flagged for a human decision, not auto-fixed. |

## 9. MOCs Missing Links to Existing Topic Pages

**None.** Every atomic page in `02_Foundations`–`12_Frontier-Maps` (including all newly-built Module 5–6 pages — gravitational fields, capacitors, magnetic fields, nuclear/particle, thermal, astrophysics, medical — and all `11_Problems` problem-types/worked-examples) is linked from at least one MOC or `00_Home` map. MOC coverage is complete.

## 10. Pages Over 800 Words

| File | Words | Note |
|---|---|---|
| `13_Sources/OCR-Specifications/OCR-Physics-A-H556-Specification.md` | 847 | Source/extraction record — large extracted-object list is expected; borderline, no split needed. |
| `index.md` | 830 | Home/index navigation page (MOC-class) — acceptable; monitor growth. |

No atomic content page exceeds 800 words. §5.6 atomic-size discipline is well respected.

## 11. Physics-Quality Gaps (§12)

**None detected.** All `physical-quantity` pages reference an SI unit; all `law-result` pages state conditions/validity; all `representation` pages discuss gradient/area/intercept; all `experiment-practical` pages contain IV/DV/control variables and an uncertainty section. (Heuristic scan — a spot-verify on a sample is still advisable, but no systematic gap.)

## 12. Frontier-Depth Violations (§3)

| File | Finding | Severity |
|---|---|---|
| `12_Frontier-Maps/Particle-Physics-Map.md` | wc=372, 0 block equations, mentions "Lagrangian" once | **LOW** — single named-concept mention, no derivation; within "orientation, not mastery" depth. Keep the sentence descriptive. |
| `12_Frontier-Maps/Quantum-Mechanics-Map.md` | wc=375, 0 block equations, mentions "Schrödinger equation" once | **LOW** — named without solving/derivation; acceptable as an edge-map landmark. |

No frontier page has dense formalism, block-equation derivations, or excessive length. Frontier boundary (§3) is respected; the two flags are name-drops only — no fix required.

## 13. status: seed / draft Pages in Content Folders

**None.** No content page carries `status: seed`, `draft`, `stub`, `skeleton`, or `todo`. The gap-fill passes have promoted all pages to usable status.

---

## Top Recommended Fixes (Prioritised)

1. **[HIGH] Create the 5 high-inbound missing pages** (most leverage on graph connectivity):
   - `06_Models/Nuclear-Model.md` (4 inbound) · `06_Models/Rigid-Body-Model.md` (3) · `06_Models/Bohr-Model.md` (2)
   - `05_Laws-and-Results/Principle-of-Moments.md` (3 inbound, examinable)
   - `02_Foundations/.../Balanced-and-Unbalanced-Forces.md` (3 inbound)
2. **[HIGH] Resolve the 4 word-level alias collisions** needing a canonical-owner decision (`voltage`, `potential divider`, `voltage divider calculation`, `resolving vectors`) — human picks the canonical page; fold the other into `aliases` per §5.3 to prevent duplicate-page drift.
3. **[HIGH] Decide `02_Foundations/GCSE-Foundations/Waves.md`** — confirm intentional GCSE-layer twin or rename away from the §5.5 forbidden broad name (keep `Waves` as alias); this also fixes the `[[Wave]]`/`[[Waves]]` link confusion.
4. **[MED] Batch-fix source-page frontmatter** — add `level:` + `sources:` to the 7 pages under `13_Sources/` (uniform mechanical edit).
5. **[MED] Create the 4 classic mistake-pattern pages** referenced by the problem layer: `Confusing-Photon-Energy-and-Intensity`, `Mixing-Up-EMF-and-Terminal-PD`, `Treating-Centripetal-Force-as-an-Extra-Force`, `Confusing-Wavelength-and-Amplitude` (good exam value, currently dangling).
6. **[MED] Retarget obvious mis-links** instead of creating pages: `[[Wave]]` → `[[Waves]]`; `[[Series-and-Parallel-Circuits]]` → `[[Series-Parallel-Circuit-Analysis]]` (or a circuit foundation page); `[[Reflection-and-Refraction]]` → split `[[Wave-Reflection]]`/`[[Wave-Refraction]]`.
7. **[MED] Populate problem-layer provenance** — add originating OCR H556 topic codes to `## Example Sources` / `## Source Reference` and `sources:` for the 24 problem/worked-example pages; add `aliases: []` to the 8 worked-examples.
8. **[LOW] Decide policy for `00_Home` maths/CS bridge stubs** (`Differentiation`, `Integration`, `Trigonometry`, etc.) — build the maths-bridge layer or mark them external; not urgent.
9. **[LOW] index.md `.state` links** — convert `[[log]]`/`[[wiki-lint-report]]` etc. to relative paths or drop; cosmetic.

**Net assessment:** The vault is in good structural health — zero orphans, zero template-section violations, zero type/folder mismatches, zero physics-quality gaps, zero seed/draft pages, complete MOC coverage. Remaining work is mostly additive (≈18 missing pages, chiefly models and mistake-patterns), one rename/alias-policy call, and provenance/frontmatter cleanup on the synthetic problem layer.
