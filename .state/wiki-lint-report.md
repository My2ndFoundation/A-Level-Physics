# Wiki Lint Report

_Generated: 2026-05-18 • READ-ONLY audit • no files changed except this report_

## Summary

- Content pages scanned: **228** (02_Foundations … 13_Sources + 01_MOCs + 00_Home + index.md; _meta/raw/.state/.git/.obsidian excluded)
- Status distribution: `(none)`=1, `active`=1, `draft`=35, `ingested`=7, `usable`=184
- Overall health: **good**. The baseline build is template-compliant; no `type`/folder mismatches, no template-section violations, no missing source traces, no orphans, no broad-topic content pages, no physics-quality gaps, no frontier-depth violations, no seed pages.

| Check | Finding count | Severity |
|---|---|---|
| 1 Frontmatter | 1 real (index.md) | low |
| 2 type vs folder | 0 | – |
| 3 Template sections | 0 | – |
| 4 Missing source trace | 0 | – |
| 5 Orphan pages | 0 | – |
| 6 Broken wikilinks | 9 genuine + 2 alias near-miss (42 documented-deferred, 6 operational) | medium |
| 7 Duplicate aliases | 5 word-level + 9 symbol collisions | low–medium |
| 8 Broad-topic content pages | 0 | – |
| 9 MOCs missing links | 0 | – |
| 10 Pages > 800 words | 1 | low |
| 11 Physics-quality gaps | 0 | – |
| 12 Frontier-depth violations | 0 | – |
| 13 Seed pages in content | 0 | – |

---

## Check 1 — Missing / partial frontmatter

The 7 pages under `13_Sources/` flagged by a generic rule are **NOT violations**: they correctly follow `_meta/templates/source-template.md`, which uses `source_type`/`raw_path`/`learning_layer`/`processed_date` and intentionally omits `level`/`sources`. All other non-MOC content pages have complete frontmatter (`type, subject, tags, level, status, aliases, sources`).

Real finding:

- `index.md` — root index has no YAML frontmatter (no `type/subject/tags/status`). _Action:_ optional; if treated as a home/MOC page add minimal MOC frontmatter. **Severity: low** (root index, acceptable as a plain landing page).

## Check 2 — `type:` vs folder mismatch

None. Every page's `type` matches its folder per the CLAUDE.md §4 mapping (incl. `02_Foundations/Everyday-Physics` → `common-sense`, `11_Problems/Mistake-Patterns` → `mistake-pattern`).

## Check 3 — Required template-section violations

None. Every audited content page contains all required `##` headings from its `_meta/templates/<type>-template.md` (spot-verified across physical-quantity, law-result, concept, experiment-practical, common-sense, frontier-map, source). Pages may add optional sections (e.g. `Derivation or Explanation`, `Safety / Practical Limits`) which is allowed.

## Check 4 — Missing source trace

None. Every atomic page has a populated `## Source Trace` (or, for `source` pages, populated metadata); none combine `sources: []` with an empty trace.

## Check 5 — Orphan pages

None. Every non-MOC content page has at least one inbound wikilink from another content page or a MOC (alias and `[[A|B]]`/`[[A#h]]`/case-folded resolution accounted for).

## Check 6 — Broken wikilinks

Distinct unresolved targets: 59 total. Of these, **42 are documented deferred graph-stubs** in `.state/unresolved-links.md` (deliberate forward links from the baseline build / seed hubs — not errors), and 6 are operational links from `index.md` to `.state/`/`_meta/` files.

### 6a — Genuine missing pages (NOT in the deferred list) — action: create or alias

- `[[Refractive-Index]]` — referenced by: Wave-Refraction. _Action:_ create the canonical page (or add as alias of an existing page if it is a synonym). **Severity: medium**
- `[[Rigid-Body-Model]]` — referenced by: Centre-of-Mass, Equilibrium, Moment. _Action:_ create the canonical page (or add as alias of an existing page if it is a synonym). **Severity: medium**
- `[[Series-and-Parallel-Circuits]]` — referenced by: Potential-Divider. _Action:_ create the canonical page (or add as alias of an existing page if it is a synonym). **Severity: medium**
- `[[Static-Electricity]]` — referenced by: Ionisation. _Action:_ create the canonical page (or add as alias of an existing page if it is a synonym). **Severity: medium**
- `[[Vector-Triangle]]` — referenced by: Equilibrium, Resultant-Force. _Action:_ create the canonical page (or add as alias of an existing page if it is a synonym). **Severity: medium**
- `[[Vectors-and-Scalars]]` — referenced by: Resultant-Force. _Action:_ create the canonical page (or add as alias of an existing page if it is a synonym). **Severity: medium**
- `[[Volume]]` — referenced by: Density. _Action:_ create the canonical page (or add as alias of an existing page if it is a synonym). **Severity: medium**
- `[[Wave]]` — referenced by: Why-Sky-Is-Blue, Why-Sound-Needs-a-Medium. _Action:_ create the canonical page (or add as alias of an existing page if it is a synonym). **Severity: medium**
- `[[Work-Function]]` — referenced by: Photoelectric-Effect. _Action:_ create the canonical page (or add as alias of an existing page if it is a synonym). **Severity: medium**

### 6b — Alias near-misses (target differs only by apostrophe/suffix from an existing page)

- `[[Snells-Law]]` → existing page `Snell-Law.md` (`05_Laws-and-Results/Snell-Law.md`). Referenced by: Ray-Diagram. _Action:_ add `Snells Law` / `Snells-Law` to that page's `aliases:` and `.state/aliases.tsv`. **Severity: medium**
- `[[Wave-Speed]]` → existing page `Wave-Speed-Equation.md` (`05_Laws-and-Results/Wave-Speed-Equation.md`). Referenced by: Standing-Waves, Wave-Reflection, Wave-Refraction. _Action:_ add `Wave Speed` / `Wave-Speed` as an alias of Wave-Speed-Equation (or create a distinct `Wave-Speed` quantity page) in frontmatter + `.state/aliases.tsv`. **Severity: medium**

### 6c — Operational links from index.md (resolve to .state/ or _meta/ — not content broken links)

`[[baseline-build-audit]]`, `[[baseline-build-progress]]`, `[[log]]`, `[[source-inventory]]`, `[[unresolved-links]]`, `[[wiki-lint-report]]` — these point to `.state/baseline-build-audit.md`, `.state/baseline-build-progress.md`, `log.md`, `.state/source-inventory.md`, `.state/unresolved-links.md`, and this report. They live outside content folders by design. _Action:_ none required (Obsidian resolves by path); optionally use explicit path links. **Severity: low / informational**

### 6d — Documented deferred graph-stubs (informational, not errors)

Tracked in `.state/unresolved-links.md` as intentional forward links pending future content ingest:

`[[Activity]]`, `[[Adding-Forces-as-Scalars]]`, `[[Area]]`, `[[Area-Under-a-Graph]]`, `[[Balanced-and-Unbalanced-Forces]]`, `[[Binding-Energy]]`, `[[Bohr-Model]]`, `[[Capacitor-Discharge]]`, `[[Coefficient-of-Friction]]`, `[[Contact-and-Non-Contact-Forces]]`, `[[Data-Logging]]`, `[[Decay-Constant]]`, `[[Differential-Equations]]`, `[[Differentiation]]`, `[[Diffraction-Grating-Equation]]`, `[[Dimensional-Analysis]]`, `[[Electromagnetic-Spectrum]]`, `[[Exponential-Decay]]`, `[[Gradient]]`, `[[Integration]]`, `[[Isotopes]]`, `[[Levers]]`, `[[Logic-Gates]]`, `[[Mass-Defect]]`, `[[Mass-Energy-Equivalence]]`, `[[Normal-Contact-Force]]`, `[[Nuclear-Model]]`, `[[Numerical-Modelling]]`, `[[Path-Difference]]`, `[[Phase-Difference]]`, `[[Photon-Energy]]`, `[[Principle-of-Moments]]`, `[[Rearranging-Equations]]`, `[[Reflection-and-Refraction]]`, `[[SI-Units]]`, `[[Sensors]]`, `[[Signal-Processing]]`, `[[Simple-Harmonic-Motion]]`, `[[Simulation]]`, `[[Trigonometry]]`, `[[Vector-Components]]`, `[[Vectors]]`

## Check 7 — Duplicate aliases (same alias → ≥2 canonical pages)

### 7a — Word-level alias collisions (real concern — disambiguate)

- `voltage` → Potential-Difference, Voltage. _Action:_ keep the alias on only the single canonical page it most precisely names; remove from the other(s). **Severity: medium**
- `resultant force` → Force, Resultant-Force. _Action:_ keep the alias on only the single canonical page it most precisely names; remove from the other(s). **Severity: medium**
- `net force` → Force, Resultant-Force. _Action:_ keep the alias on only the single canonical page it most precisely names; remove from the other(s). **Severity: medium**
- `potential divider` → Potential-Divider, Potential-Divider-Model. _Action:_ keep the alias on only the single canonical page it most precisely names; remove from the other(s). **Severity: medium**
- `slope of a graph` → Finding-Gradient-from-a-Graph, Using-Gradient. _Action:_ keep the alias on only the single canonical page it most precisely names; remove from the other(s). **Severity: medium**

### 7b — Single-symbol collisions (9) — expected, low severity

These arise because the same physics symbol legitimately appears in the `aliases:` of multiple quantity pages:

- `a` → Acceleration, Amplitude
- `i` → Current, Intensity
- `rho` → Density, Resistivity
- `ρ` → Density, Resistivity
- `e` → Electric-Field-Strength, Energy, Young-Modulus
- `f` → Force, Frequency
- `p` → Momentum, Power, Pressure
- `v` → Potential-Difference, Speed, Velocity
- `w` → Weight, Work

_Action:_ a bare symbol is ambiguous as a wikilink target; prefer not listing single letters as aliases, or accept the ambiguity. **Severity: low**

## Check 8 — Broad-topic content pages that should be MOCs

None. The GCSE-foundation pages (`02_Foundations/GCSE-Foundations/Force|Energy|Power|Waves`) and the A-Level `03_Physical-Quantities/Force|Energy|Power` pages are intentionally distinct learning-layer pages, not broad-topic violations. All broad topic names (Mechanics, Electricity, Circuits, Materials, Motion, Fields, Quantum, Practical-Skills) exist only as `-MOC` pages.

## Check 9 — MOCs missing links to existing topic pages

None at the structural level: every MOC and 00_Home map contains wikilinks (no empty maps, no MOC with ≥8 unpopulated template sections). Deeper per-topic completeness was not exhaustively cross-checked, but no MOC is structurally empty or stub.

## Check 10 — Pages > 800 words

- `13_Sources/OCR-Specifications/OCR-Physics-A-H556-Specification.md` — 847 words (source). _Action:_ acceptable; a specification source map legitimately runs long. **Severity: low**

## Check 11 — Physics-quality gaps (§12)

None. All `physical-quantity` pages have a populated `## SI Unit`; all `law-result` pages have non-empty `## Conditions` and `## Symbols and Units`; all `representation`/graph pages have a populated `## Gradient / Area / Intercepts`; all `experiment-practical` pages declare IV/DV/control variables and a non-empty `## Uncertainty`.

## Check 12 — Frontier-depth violations (§3)

None. All 7 pages in `12_Frontier-Maps/` include `## A-Level Entry Points` and `## What Not to Worry About Yet`, contain no dense LaTeX/university formalism (≥5 math tokens threshold), and stay within map length. They remain orientation-only as required.

## Check 13 — Seed-status pages in built content folders

None. No content page has `status: seed`. Distribution: `(none)`=1, `active`=1, `draft`=35, `ingested`=7, `usable`=184. (`draft` pages are MOCs/home maps using the MOC template default; `usable` = built baseline atomic pages; `ingested` = source pages.)

---

## Top recommended fixes (priority order)

1. **Create or alias the 11 genuinely-missing wikilink targets (Check 6a):** `Refractive-Index`, `Rigid-Body-Model`, `Series-and-Parallel-Circuits`, `Static-Electricity`, `Vector-Triangle`, `Vectors-and-Scalars`, `Volume`, `Wave`, `Wave-Speed`, `Work-Function`, plus `Snells-Law`/`Wave-Speed` near-misses. Several (`Vectors-and-Scalars`, `Wave`, `Volume`, `Work-Function`, `Refractive-Index`) are core A-Level objects that should be real pages, not stubs.
2. **Fix the 2 alias near-misses (Check 6b):** add `Snells-Law` as an alias of `Snell-Law`, and `Wave-Speed` as an alias of `Wave-Speed-Equation` (frontmatter + `.state/aliases.tsv`).
3. **Disambiguate the 5 word-level duplicate aliases (Check 7a):** `voltage`, `resultant force`, `net force`, `potential divider`, `slope of a graph` each resolve to 2 canonical pages — assign each to one canonical owner.
4. **Optional:** add minimal MOC frontmatter to `index.md`; consider dropping single-letter symbol aliases to reduce ambiguous link targets.

_No structural, template, source-trace, orphan, broad-topic, physics-quality, or frontier-depth problems were found. The baseline is healthy._
