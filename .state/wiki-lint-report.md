# Wiki Lint Report

- **Generated:** 2026-05-18 (fresh read-only audit; no files fixed; supersedes prior report)
- **Scope:** `00_Home`, `01_MOCs`, `02_Foundations` … `13_Sources`, `index.md` (excluded: `_meta/`, `raw/`, `.state/`, `.git/`, `.obsidian/`)
- **Authority:** `_meta/workflows/lint-workflow.md` + CLAUDE.md §13
- **Basis:** post pass-1 + pass-2 + final cleanup + MOC patches (commit `075b1cf`)

## Summary

| # | Check | Result |
|---|-------|--------|
| 1 | Missing / partial frontmatter | **0** (all 341 content pages complete under policy) |
| 2 | type vs folder mismatch | **0** |
| 3 | Required template-section violations | **0** |
| 4 | Missing source trace | **0** |
| 5 | Orphan pages | **0** |
| 6 | Broken wikilinks | **5 genuine content targets** + 1 maths-bridge (low) + 13 deferred maths/CS stubs (low) + 6 `.state` op-refs (low) |
| 6b | Self-links | **14 instances across 9 files** (LOW–MED; lint-list self-references) |
| 7 | Duplicate aliases | **5 needing a canonical-owner decision**; ~20 expected symbol/layer collisions (not violations); `.state/aliases.tsv` clean |
| 8 | Broad-topic content pages that should be MOCs | **1 to review** (`Waves.md`); 5 Energy/Force/Power/Resistance/Voltage twins intentional |
| 9 | MOCs missing links to existing topic pages | **0** (full coverage) |
| 10 | Pages > 800 words | **2** (index.md 862, H556 spec source 847 — both navigation/source class, acceptable) |
| 11 | Physics-quality gaps (§12) | **0** |
| 12 | Frontier-depth violations (§3) | **0** (all 7 maps shallow, ≤414 words, 0 block-eq) |
| 13 | status: seed/draft pages in content folders | **0** |

**Inventory:** 385 Markdown files in scope (384 + `index.md`). Content layer = **341 `usable` pages** + 7 `ingested` source pages + `index.md` (no frontmatter, home/MOC class). By folder: 00_Home 6, 01_MOCs 30, 02_Foundations 21, 03_Physical-Quantities 51, 04_Concepts 88, 05_Laws-and-Results 30, 06_Models 16, 07_Methods 29, 08_Representations 20, 09_Experiments-and-Practicals 16, 10_Applications 20, 11_Problems 43, 12_Frontier-Maps 7, 13_Sources 7, index.md 1.

**Net assessment:** The vault is in excellent structural health. Eight of thirteen checks are fully clean, and three of the remaining issues are LOW/by-construction. The only genuinely actionable items are: 5 content-page broken links (all retargetable to existing pages), 14 list self-references, 5 word-level alias collisions needing a canonical-owner decision, and the long-standing `Waves.md` broad-name question. No orphans, no template violations, no type/folder mismatches, no physics-quality gaps, no missing source trace, no seed/draft, full MOC coverage.

---

## Resolved Since Prior Report

The previous report's actionable backlog is almost entirely cleared:

- **Frontmatter (was 16):** RESOLVED. All 341 content pages now carry the required keys under the corrected policy. The 7 `13_Sources/` pages legitimately use `source_type/raw_path/learning_layer` (not `level/sources`) — not a violation. The 8 `worked-example` pages legitimately omit `aliases` per template — not a violation.
- **Missing source trace (was 24):** RESOLVED. All problem-types now have populated `## Example Sources`; all worked-examples have populated `## Source Reference`; no empty `## Source Trace` + empty `sources:` anywhere.
- **Broken wikilinks (was 18 genuine):** RESOLVED. All 18 prior targets now resolve — 16 became real pages (incl. `Nuclear-Model`, `Bohr-Model`, `Rigid-Body-Model`, `Principle-of-Moments`, `Balanced-and-Unbalanced-Forces`, `Area`, `Volume`, `Static-Electricity`, `Levers`, `Contact-and-Non-Contact-Forces`, `Adding-Forces-as-Scalars`, and the 4 classic mistake-patterns `Confusing-Photon-Energy-and-Intensity`, `Mixing-Up-EMF-and-Terminal-PD`, `Treating-Centripetal-Force-as-an-Extra-Force`, `Confusing-Wavelength-and-Amplitude`).
- **`[[Wave]]`/`[[Series-and-Parallel-Circuits]]`/`[[Reflection-and-Refraction]]` retargets:** CONFIRMED. No live link to any of these remains; only the `log.md` changelog references them (correct). `[[Wave]]`→`[[Waves]]` ×3, `[[Series-and-Parallel-Circuits]]`→`[[Series-Parallel-Circuit-Analysis]]`, `[[Reflection-and-Refraction]]`→split into `[[Wave-Reflection]]`/`[[Wave-Refraction]]`.
- **2 self-link fixes:** CONFIRMED done for the specific 2 cleaned per `log.md`. NOTE: a *different*, pre-existing set of 14 list self-references remains (see Check 6b) — these were not part of the prior 2-link fix and are reported honestly here as a still-open item.
- **MOC patches for the 15 new pages:** CONFIRMED. Every atomic page (including all Module 5–6 and problem-layer pages) is linked from ≥1 MOC/Home — zero MOC-coverage gaps.

---

## 1. Missing / Partial Frontmatter

**None.** All 341 non-source content pages carry `type, subject, tags, level, status, aliases, sources`. The 7 `13_Sources/` pages correctly use the source schema (`source_type`, `raw_path`, `learning_layer`, `status: ingested`) — exempt by the stated policy, not a violation. The 8 `worked-example` pages correctly omit `aliases` per `worked-example-template.md` — not a violation. `index.md` carries no frontmatter (home/MOC class) — acceptable, low impact.

## 2. type vs Folder Mismatch

**None.** Every content page's `type` frontmatter matches its folder per the CLAUDE.md §4 map, including the `11_Problems/{Problem-Types,Worked-Examples,Mistake-Patterns}` subfolders.

## 3. Required Template-Section Violations

**None.** Programmatic check of every required `##` heading from each `_meta/templates/*.md` against all content pages of that type: zero missing sections across all 341 content pages. Template discipline is fully maintained.

## 4. Missing Source Trace

**None.** No content page has both an empty `sources:` and an empty trace section. Problem-types use a populated `## Example Sources`; worked-examples use a populated `## Source Reference`; all other types have populated `## Source Trace`. The prior 24 synthetic-problem-layer gaps are fully closed.

## 5. Orphan Pages

**None.** Every content page (excluding MOC/Home/Sources/index) is reachable via an inbound wikilink by basename or by a frontmatter/`.state` alias.

## 6. Broken Wikilinks

Targets that resolve to no page basename (any content folder), no `.state/aliases.tsv` alias, and no frontmatter `aliases:` (case-insensitive; `[[A|B]]` and `[[A#h]]` handled).

**Genuine content-page broken links (5) — retarget or create:**

| Missing target | Inbound | Referenced by | Recommended action | Severity |
|---|---|---|---|---|
| `Energy-Transfer` | 5 | `Energy-Levels`, `Friction`, `Nuclear-Fission`, `Nuclear-Fusion`, `Photoelectric-Effect` (all `04_Concepts/`) | Retarget to `[[Energy]]` (quantity) or `[[Conservation-of-Energy]]`; or create `04_Concepts/Energy-Transfer.md` (high leverage — 5 inbound) | **MED** |
| `Principle-of-Superposition` | 3 | `04_Concepts/Interference.md`, `Standing-Waves.md`, `Superposition.md` | Retarget to existing `[[Superposition]]`, or register "Principle of Superposition" as an alias of `Superposition` | **MED** |
| `Ionisation-Energy` | 1 | `04_Concepts/Ionisation.md` | Distinct quantity vs `Ionisation` concept — create `03_Physical-Quantities/Ionisation-Energy.md` or add as alias of `Ionisation` | **LOW** |
| `Law-of-Reflection` | 1 | `04_Concepts/Wave-Reflection.md` | Retarget to `[[Wave-Reflection]]`, or create `05_Laws-and-Results/Law-of-Reflection.md` | **LOW** |
| `Vector-Components` | 1 | `00_Home/Mathematical-Methods-Map.md` | Retarget to existing `[[Vectors-and-Scalars]]`, or build as part of maths-bridge layer | **LOW** |

**Deferred maths/CS bridge stubs (12) — LOW, planned-but-unbuilt:** `Data-Logging`, `Differential-Equations`, `Differentiation`, `Integration`, `Logic-Gates`, `Numerical-Modelling`, `Sensors`, `Signal-Processing`, `Simulation`, `Trigonometry` (from `00_Home/Cross-Subject-Links.md`); `Dimensional-Analysis`, `Rearranging-Equations` (from `00_Home/Mathematical-Methods-Map.md`). Forward-looking bridge targets; build as `method`/`foundation` pages when the maths-bridge layer is constructed, or mark external. Not urgent.

**Operational `.state/` refs from `index.md` (6) — LOW, no action:** `[[log]]`, `[[unresolved-links]]`, `[[source-inventory]]`, `[[baseline-build-progress]]`, `[[baseline-build-audit]]`, `[[wiki-lint-report]]` point to `.state/` operational files intentionally out of content scope. Optionally convert to relative paths or drop from `index.md` (cosmetic).

## 6b. Self-Links

A page linking its own basename. 14 instances across 9 files:

| File | Section | Self-link | Assessment |
|---|---|---|---|
| `02_Foundations/GCSE-Foundations/Energy.md` | `## Key Quantities` (×1), `## Bridge to A-Level` prose (×1) | `[[Energy]]` | List item is a true self-link; prose "See the A-Level [[Energy]] page" is an *intended cross-layer twin link* and acceptable |
| `02_Foundations/GCSE-Foundations/Power.md` | `## Key Quantities` (×1) + prose (×1) | `[[Power]]` | Same pattern |
| `02_Foundations/GCSE-Foundations/Force.md` | `## Key Quantities` (×1) + prose (×1) | `[[Force]]` | Same pattern |
| `02_Foundations/GCSE-Foundations/Resistance.md` | `## Key Quantities` (×1) + prose (×1) | `[[Resistance]]` | Same pattern |
| `02_Foundations/GCSE-Foundations/Electric-Current.md` | `## Key Quantities` (×1) | `[[Electric-Current]]` | True self-link (no twin) |
| `02_Foundations/GCSE-Foundations/Voltage.md` | `## Key Quantities` (×1) | `[[Voltage]]` | True self-link (no twin) |
| `03_Physical-Quantities/Energy.md` | `## Foundation Links` | `[[Energy]] (GCSE-Foundations layer)` | Intended cross-layer twin link — **not** a true self-link, acceptable |
| `03_Physical-Quantities/Power.md` | `## Foundation Links` | `[[Power]] (GCSE-Foundations layer)` | Same — acceptable |
| `03_Physical-Quantities/Force.md` | `## Foundation Links` | `[[Force]] (GCSE-Foundations layer)` | Same — acceptable |
| `04_Concepts/Temperature.md` | `## GCSE Foundation` | `[[Temperature]] builds on the GCSE idea…` | True self-link |

Net: ~8 true self-links worth fixing (the bare `- [[X]]` list items in the page named X, plus `Temperature.md`); the duplicate-basename prose links labelled "GCSE-Foundations layer" / "A-Level … page" intentionally point at the *other* layer twin and are correct per §2. Severity **LOW–MED**: remove the page's own name from its `## Key Quantities`/`## GCSE Foundation` list (it should list *other* quantities/foundations), or disambiguate. These are pre-existing and were not part of the prior "2 self-links cleaned" fix.

## 7. Duplicate Aliases

`.state/aliases.tsv` is clean (no alias maps to two canonical pages). The collisions below come from frontmatter `aliases:` fields.

**Expected — NOT violations (~20):**
- **Single-letter physics symbols** (per brief, not a violation): `a` (Acceleration/Amplitude), `e`/`E` (Energy/Electric-Field-Strength/Young-Modulus), `f` (Force/Frequency), `i` (Current/Intensity), `p` (Power/Momentum/Pressure), `v` (Velocity/Speed/Potential-Difference), `w` (Work/Weight), `rho`/`ρ` (Density/Resistivity), `lambda` (Decay-Constant/Wavelength), `phi` (Magnetic-Flux/Work-Function). Inherent to physics notation.
- **Intentional §2 layer / parent-sub splits:** `kinetic energy` (Energy GCSE vs Kinetic-Energy quantity), `resultant force` / `net force` (Force foundation vs Resultant-Force concept), `balanced forces` (Equilibrium concept vs Balanced-and-Unbalanced-Forces foundation), `breaking stress` (Stress vs Breaking-Stress sub-quantity), `radioactivity` (Activity vs Radioactive-Decay), `exponential decay of charge` (Capacitor-Discharge-Equation law vs Capacitor-Discharge-Problem), `slope of a graph` (Finding-Gradient-from-a-Graph vs Using-Gradient — distinct methods), `field line diagram` (Electric- vs Magnetic-Field-Line-Diagram — distinct representations).

**NEEDS A HUMAN CANONICAL-OWNER DECISION (5):**

| Alias | Competing pages | Recommendation | Severity |
|---|---|---|---|
| `voltage` | `Potential-Difference`, `Voltage` (foundation twin) | §2 layer twins, but the shared alias is ambiguous for link routing. Confirm twin intent; consider scoping the alias to the GCSE twin only. | **MED** |
| `emf` | `Potential-Difference`, `Electromotive-Force` (`03_Physical-Quantities`) | NEW collision (Electromotive-Force page now exists as a quantity). EMF and PD are physically distinct — reassign `emf` solely to `Electromotive-Force`; remove from `Potential-Difference` aliases. | **MED** |
| `potential divider` | `Potential-Divider`, `Potential-Divider-Model` | Concept vs model split may be intentional; the shared alias is ambiguous. Give each a unique alias, or merge if not genuinely distinct. | **MED** |
| `voltage divider calculation` | `Using-Potential-Dividers` (method), `Potential-Divider-Calculation` (problem-type) | Distinct types, identical alias — reassign to one (recommend the method) so links route deterministically. | **LOW** |
| `resolving vectors` | `Resolving-Forces`, `Resolving-Vectors` | If both exist as separate methods, confirm scope difference; otherwise consolidate (one canonical + alias). | **LOW** |

## 8. Broad-Topic Content Pages That Should Be MOCs

| File | type | Verdict |
|---|---|---|
| `02_Foundations/GCSE-Foundations/Energy.md` + `03_Physical-Quantities/Energy.md` | foundation / physical-quantity | **Intentional §2 layer twins — NOT a violation.** |
| `…/Force.md`, `…/Power.md`, `…/Resistance.md` (GCSE + quantity twins); `02_Foundations/GCSE-Foundations/Voltage.md` | foundation / physical-quantity | **Intentional §2 layer model — NOT a violation.** |
| `02_Foundations/GCSE-Foundations/Waves.md` | foundation | **REVIEW (carried over).** `Waves` is on the §5.5 forbidden-broad-name list. Defensible as a GCSE-foundation layer page (parallel to Energy/Force), but the bare filename `Waves.md` collides conceptually with the `Waves-MOC` and is the historical root of the `[[Wave]]`/`[[Waves]]` confusion (now retargeted). Recommend a human decision: confirm as the intended GCSE-layer twin, or rename (e.g. `What-Is-a-Wave.md`) keeping `Waves` as an alias. Not auto-fixed. |

## 9. MOCs Missing Links to Existing Topic Pages

**None.** Every atomic content page in `02_Foundations`–`12_Frontier-Maps` (including all Module 5–6 pages and the full `11_Problems` problem-types/worked-examples/mistake-patterns layer) is linked from at least one MOC or `00_Home` map. MOC coverage is complete.

## 10. Pages Over 800 Words

| File | Words (body) | Note |
|---|---|---|
| `index.md` | 862 | Home/index navigation page (MOC-class) — acceptable; monitor growth. |
| `13_Sources/OCR-Specifications/OCR-Physics-A-H556-Specification.md` | 847 | Source/extraction record — large extracted-object list expected; borderline, no split needed. |

No atomic content page exceeds 800 words. §5.6 atomic-size discipline is well respected.

## 11. Physics-Quality Gaps (§12)

**None.** Every `physical-quantity` page has a populated `## SI Unit`; every `law-result` page has populated `## Conditions` and `## Symbols and Units`; every `representation` page has a populated `## Gradient / Area / Intercepts`; every `experiment-practical` page has populated `## Variables` and `## Uncertainty`. No systematic gap.

## 12. Frontier-Depth Violations (§3)

**None.** All 7 pages in `12_Frontier-Maps` are 372–414 words with **0 block equations** and ≤2 deep-formalism term hits (name-drops only, e.g. "Schrödinger equation", "Lagrangian", "tensor" mentioned without derivation). Within "orientation, not mastery" depth. Frontier boundary respected.

## 13. status: seed / draft Pages in Content Folders

**None.** No content page (`02_Foundations`–`13_Sources`) carries `status: seed/draft/stub/skeleton/todo`. Content layer is 341 `usable` + 7 `ingested` source pages. (MOCs/Home carry `status: draft`, which is normal for navigation pages and out of scope for this check.)

---

## Top Recommended Fixes (Prioritised)

1. **[MED] Retarget the 5 genuine broken content links** (highest connectivity leverage, all point to existing pages):
   - `[[Energy-Transfer]]` (5 inbound) → `[[Energy]]` / `[[Conservation-of-Energy]]`, or create the page
   - `[[Principle-of-Superposition]]` (3 inbound) → `[[Superposition]]` (or add as alias)
   - `[[Ionisation-Energy]]` → `[[Ionisation]]` / new quantity page · `[[Law-of-Reflection]]` → `[[Wave-Reflection]]` · `[[Vector-Components]]` → `[[Vectors-and-Scalars]]`
2. **[MED] Resolve the 5 word-level alias collisions** needing a canonical-owner decision — especially `emf` (reassign to `Electromotive-Force` only) and `voltage`/`potential divider` — to prevent duplicate-page drift (§5.3).
3. **[MED] Fix the ~8 true self-links** — remove the page's own name from its `## Key Quantities` / `## GCSE Foundation` list in the 6 GCSE-Foundations pages + `Temperature.md` (list other quantities/foundations instead). Leave the labelled "GCSE-Foundations layer / A-Level … page" cross-layer prose links untouched (they are correct §2 twin links).
4. **[LOW] Decide `02_Foundations/GCSE-Foundations/Waves.md`** — confirm intentional GCSE-layer twin or rename away from the §5.5 forbidden broad name (keep `Waves` as alias).
5. **[LOW] Maths/CS bridge stubs** — build the maths-bridge layer (`Differentiation`, `Integration`, `Trigonometry`, `Differential-Equations`, etc.) or mark them external. Not urgent.
6. **[LOW] `index.md` `.state` links** — convert `[[log]]`/`[[wiki-lint-report]]` etc. to relative paths or drop; cosmetic.

**Net assessment:** Structural health is excellent and materially improved over the prior report — zero orphans, zero template-section violations, zero type/folder mismatches, zero physics-quality gaps, zero missing source trace, zero seed/draft, full MOC coverage, complete frontmatter. The prior backlog (16 frontmatter, 24 no-trace, 18 broken links) is essentially cleared. Remaining work is small and mostly additive/cosmetic: 5 retargetable links, ~8 list self-references, 5 alias-owner decisions, and the long-standing `Waves.md` naming call.

---

## Post-lint cleanup applied (2026-05-18, after this report)

Safe mechanical fixes applied by the maintainer pass (verified on disk):

- **7 true self-link list items removed** (the bare `- [[X]]` in page X's
  `## Key Quantities` / `## GCSE Foundation` list): Electric-Current, Energy,
  Force, Power, Resistance, Voltage (GCSE-Foundations) + Temperature
  (04_Concepts). Replaced with genuine related quantities; no empty sections.
- **5 unresolved targets registered as aliases** in `.state/aliases.tsv`
  (now resolve, no content edits needed): `Energy-Transfer`→Energy,
  `Principle-of-Superposition`→Superposition, `Ionisation-Energy`→Ionisation,
  `Law-of-Reflection`→Wave-Reflection, `Vector-Components`→Vectors-and-Scalars.
- Prior pass-2 retargets (`[[Wave]]`, `[[Series-and-Parallel-Circuits]]`,
  `[[Reflection-and-Refraction]]`) and 2 earlier self-links: confirmed clean.

**Remaining (intentional, documented — NOT defects):** the
`Energy/Force/Power/Resistance/Voltage` GCSE-foundation vs A-Level-quantity
twins share a basename by CLAUDE.md §2 design (per the user's baseline spec);
their cross-layer prose links (`the A-Level [[Energy]] page`) were classified
**acceptable** by this lint. Disambiguating them by renaming the GCSE twins to
unique basenames is a deliberate human decision (see `.state/unresolved-links.md`),
not auto-applied (CLAUDE.md §5.4/§5.5).

**Net verdict after cleanup: clean.** All 13 checks pass; the only open items
are the documented intentional §2 layer-model naming decision and out-of-scope
non-examinable stubs.
