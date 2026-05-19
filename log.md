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

## [2026-05-18] ingest | CERN Science (frontier reference)
- Created: 13_Sources/Frontier-References/CERN-Science.md; 12_Frontier-Maps/Particle-Physics-Map.md
- Updated: 01_MOCs/Frontier-Physics-MOC.md (added Particle-Physics-Map + entry point), index.md, .state/ingested.tsv, .state/aliases.tsv
- Deferred: none — deeper particle-physics content intentionally out of scope (§3, frontier-rules)
- Notes: .url bookmark → home.cern/science. Layer = frontier. Created the previously-broken-link [[Particle-Physics-Map]] as a shallow orientation map (no QFT/Lagrangians/Feynman maths; explicit "what not to worry about yet"). Resolves wikilinks from OCR-Physics-Map (Module 6.4) and the practical source. No source variation. No copyrighted text.

## [2026-05-18] ingest | IOP Explore Physics (frontier reference)
- Created: 13_Sources/Frontier-References/IOP-Explore-Physics.md
- Updated: 01_MOCs/Frontier-Physics-MOC.md (added Further Exploration external pointer), index.md, .state/ingested.tsv, .state/aliases.tsv
- Deferred: none — general hub, not a single field, so no frontier-map page (CLAUDE.md §3 / §5.5)
- Notes: .url bookmark → iop.org/explore-physics. Live page HTTP 403 (bot-protected, not fetched); recorded from known nature, no content reproduced. Provenance-only per user choice A. Layer = frontier. No source variation.

## [2026-05-18] ingest | NASA Astrophysics (frontier reference)
- Created: 13_Sources/Frontier-References/NASA-Astrophysics.md; 12_Frontier-Maps/Cosmology-Map.md
- Updated: 01_MOCs/Frontier-Physics-MOC.md (added Cosmology-Map + entry point), index.md, .state/ingested.tsv, .state/aliases.tsv
- Deferred: none — deeper cosmology (GR, Friedmann/FLRW) intentionally out of scope (§3, frontier-rules)
- Notes: .url bookmark → science.nasa.gov/astrophysics. Layer = frontier. Created the previously-broken-link [[Cosmology-Map]] as a shallow orientation map (no GR field equations / FLRW maths; explicit "what not to worry about yet"). Resolves wikilinks from OCR-Physics-Map (Module 5.5), Cross-Subject-Links, and the H556 spec source. No source variation. No copyrighted text (NASA public-domain outreach, paraphrased).

## [2026-05-18] lint | whole wiki
- Created: (none)
- Updated: 04_Concepts/Measurement-Uncertainty.md & Resolution-Accuracy-and-Precision.md (retargeted dangling [[SI-Units]] → [[Physical-Quantities-MOC]]); 01_MOCs/Physics-MOC.md (linked 3 orphan MOCs: Problem-Solving-MOC, Mistake-Patterns-MOC, Modern-Physics-MOC + Frontier-Physics-MOC); .state/unresolved-links.md (recorded SI-Units + ~27 seed-hub placeholder links)
- Deferred: ~27 placeholder links in seed hub pages (Mathematical-Methods-Map, Cross-Subject-Links) — resolve as content is ingested, not by editing seed hubs; seed-page frontmatter gaps (empty tags/sources) left for /physics-expand-concept; H556 source page 934w accepted (source pages exempt from §5.6 atomic-size rule)
- Notes: Read-only audit then 3 user-confirmed mechanical fixes. Orphans 3→0; new-content dangling [[SI-Units]] cleared. Declined the "ignore copyright rule" instruction — CLAUDE.md §5.2 is non-negotiable; not engaged here anyway (link-only fixes, no source text). No content overwritten, no pages deleted.

## [2026-05-18] baseline-build | physics usable baseline construction
- Created: ~150 new atomic pages across 02_Foundations (15), 03_Physical-Quantities (31), 04_Concepts (24), 05_Laws-and-Results (16), 06_Models (12), 07_Methods (15), 08_Representations (13), 09_Experiments-and-Practicals (10), 10_Applications (10), 11_Problems/Mistake-Patterns (11), 12_Frontier-Maps (4); 3 new skills (physics-source-research, physics-complete-page, physics-build-base-cluster); _meta/source-policy.md; _meta/baseline-build-policy.md
- Updated: completed-in-place seed pages (Acceleration, Newton-Second-Law, Constant-Acceleration-Model, Using-SUVAT-Equations, Velocity-Time-Graph, Confusing-Mass-and-Weight, Why-Seatbelts-Matter, Force, Energy, From-Speed-to-Velocity, Quantum-Mechanics-Map); 12 pre-existing substantive draft pages elevated draft→usable (uncertainty cluster + Particle-Physics-Map + Cosmology-Map); CLAUDE.md §5.12; 3 existing skills cross-referenced to baseline/source policy; index.md regenerated; .state/aliases.tsv (+Refraction-of-Waves→Wave-Refraction); .state/baseline-build-audit.md; .state/baseline-build-progress.md; MOCs rebuilt centrally (parallel, navigation-only); .state/wiki-lint-report.md
- Deferred: problem-type + worked-example layer (Phase: recommended second pass — OCR past-paper alignment); ~25 mentioned-but-unbuilt atomic pages recorded in .state/unresolved-links.md (Bohr-Model, Nuclear-Model, Binding-Energy, Decay-Constant, Mass-Defect, Photon-Energy, Phase-Difference, Path-Difference, Diffraction-Grating-Equation, Electromagnetic-Spectrum, Electromotive-Force, etc.) for future content ingests
- Notes: User-authorised full baseline pass (no per-page checkpoint per _meta/baseline-build-policy.md). 8 folder-partitioned parallel builders + 5 partitioned MOC builders + read-only lint, no write collisions. All pages template-conformant (CLAUDE.md §4), 300–800w, paraphrased (no copyrighted text §5.2), wikilinked, source-traced to public pool + OCR alignment anchor. Frontier maps kept shallow (§3). No source-variation conflicts arose. No git commit (§5.11).

## [2026-05-18] baseline-build pass 2 | OCR H556 Module 5–6 gap-fill + problem layer
- Created: 142 new atomic pages (content layer 184→326, all status: usable). Thermal M5.1 (12), Circular+SHM M5.2/5.3 (16), Gravitation+Astro M5.4/5.5 (17), Capacitors+E-fields M6.1/6.2 (11), Electromagnetism M6.3 (13), Nuclear+Particle M6.4 (16), Medical M6.5 + M4 wave/photon patches (22), M3 patches+vectors/SI-Units (11), Problem-Types (16) + Worked-Examples (8 original) + 2 new Mistake-Patterns
- Updated: index.md regenerated (~376 links); MOCs rebuilt centrally (5 partitioned agents — Circular-Motion/SHM/Thermal/Fields/Problem-Solving now populated; PAG/P1–P9/M0–M4 banners preserved); .state/wiki-lint-report.md (pass-2); log.md
- Deferred: pre-GCSE foundation atomic layer (lowest priority, not H556-examinable); a few forward-link stubs (e.g. Treating-Centripetal-Force-as-an-Extra-Force) recorded in unresolved-links; 5 duplicate aliases from pass-1 lint still need a human canonical-owner decision
- Notes: Systematic gap analysis against OCR-Physics-Map H556 module structure (Modules 5–6 were the major hole; AS Modules 2–4 patched). 9 folder/topic-partitioned parallel builders (no write collisions) + 5 partitioned MOC builders + read-only lint. All pages template-conformant (§4), 300–800w, paraphrased no copyrighted text (§5.2), worked examples original (§5.2), astrophysics/Standard-Model kept A-Level depth not frontier (§3). Energy/Force/Power/Resistance dual GCSE-foundation vs A-Level-quantity pages are the intended §2 layer model, not duplicates. No git commit (§5.11).

## [2026-05-18] baseline-build pass 2 final cleanup | residual gap fill
- Created: 15 pages (Nuclear-Model, Bohr-Model, Rigid-Body-Model, Principle-of-Moments, Balanced-and-Unbalanced-Forces, Contact-and-Non-Contact-Forces, Static-Electricity, Area, Volume, Levers, + 5 exam-trap mistake-patterns). Content layer 326→341, all status: usable
- Updated: 6 mis-link retargets ([[Wave]]→[[Waves]] ×3, [[Series-and-Parallel-Circuits]]→[[Series-Parallel-Circuit-Analysis]], [[Reflection-and-Refraction]] split→[[Wave-Reflection]]/[[Wave-Refraction]]); 2 self-links cleaned; index.md regenerated (391 links); MOCs patched for the 15 pages; log.md
- Deferred: nothing examinable. Out of H556 scope by design: pre-GCSE foundation atomic layer; ~6 GCSE-trivial unlink candidates folded as real pages instead
- Notes: Closes the pass-2 lint residual. 4 "alias collisions" (voltage / potential divider / voltage-divider-calculation / resolving-vectors) are the intentional CLAUDE.md §2 layer + concept/model twins (same pattern lint classed NON-violation for Energy/Force) — documented, not merged. `02_Foundations/GCSE-Foundations/Waves.md` kept as the intentional GCSE-layer twin (explicitly in the user's baseline spec; parallels Energy/Force/Power); `Wave`/`Waves` link confusion resolved by retarget. No git commit (§5.11).

## [2026-05-18] lint | post-pass-2 confirmation + safe cleanup
- Created: (none)
- Updated: 7 self-link list items removed (6 GCSE-Foundations + Temperature); .state/aliases.tsv (+5 alias resolutions: Energy-Transfer, Principle-of-Superposition, Ionisation-Energy, Law-of-Reflection, Vector-Components); .state/wiki-lint-report.md (fresh full audit + post-cleanup delta)
- Deferred: §2 same-basename twin disambiguation (Energy/Force/Power/Resistance/Voltage) — human decision, lint-classified acceptable, documented in unresolved-links
- Notes: Fresh read-only lint of 341 usable pages — 8/13 checks zero issues; entire prior backlog (16 frontmatter, 24 source-trace, 18 broken links) resolved. Applied only safe mechanical fixes (self-link removal, alias registration); no prose/structure overwritten, no pages deleted (§5.4). Verified on disk: 0 true self-links, replacement targets exist, 5 aliases resolve. Net: clean. No git commit (§5.11).

## [2026-05-18] lint+create | alias-promotion pass (user-confirmed Tier 🟥+🟧)
- Created: 03_Physical-Quantities/Wave-Speed.md (physical-quantity, usable); 05_Laws-and-Results/Law-of-Reflection.md (law-result, usable); 04_Concepts/Radioactivity.md (concept, usable); 03_Physical-Quantities/Ionisation-Energy.md (physical-quantity, usable) — each per its `_meta/templates/` template.
- Updated: freed absorbed alias from host frontmatter — Wave-Speed-Equation.md (−Wave-Speed), Wave-Reflection.md (−Law of Reflection), Ionisation.md (−Ionisation Energy), Radioactive-Decay.md (−Radioactivity); .state/aliases.tsv repointed 3 spaced-form aliases to new canonicals + dropped 3 redundant link-form rows; index.md (+4 entries); Waves-MOC, Nuclear-Physics-MOC, Quantum-Physics-MOC (+links); .state/unresolved-links.md (Radioactivity cleared from backlog; RESOLVED note added).
- Deferred: maths/CS cross-subject stubs (Differentiation, Integration, Trigonometry, Dimensional-Analysis, Logic-Gates, Sensors, …) — out of scope by project design until maths-skills content is ingested.
- Notes: Scan found only 12 truly-dangling targets (all documented out-of-scope) + 4 distinct concepts hidden behind alias redirects. Promoted the 4; deliberately did NOT create pages for genuine synonyms (Refraction-of-Waves, Snells-Law, Energy-Transfer, Principle-of-Superposition, Vector-Components) per §5.3. No prose overwritten, no pages deleted (§5.4). No git commit (§5.11).

## [2026-05-19] lint+create | alias-link grey-node retarget pass (user-confirmed)
- Created: 04_Concepts/Energy-Transfer.md (concept, usable) — per `_meta/templates/concept-template.md`; supersedes the 2026-05-18 keep-as-alias decision (user explicitly chose to promote it).
- Updated: 16 body links retargeted to `[[Canonical|readable display]]` so they resolve to the real file regardless of Obsidian alias config — Refraction-of-Waves→Wave-Refraction ×10 (8 pages: Waves, Why-Sky-Is-Blue, From-Waves-to-Superposition, Why-Sound-Needs-a-Medium, Stars-and-Cosmology, Medical-Imaging, Optical-Fibres), Snells-Law→Snell-Law ×2 (Ray-Diagram), Principle-of-Superposition→Superposition ×3 (Standing-Waves, Interference, Superposition), Vector-Components→Vectors-and-Scalars ×1 (Mathematical-Methods-Map); 1 true duplicate bullet consolidated (Optical-Fibres had both forms); .state/aliases.tsv (Energy-Transfer rows repointed to the new concept page); index.md (+[[Energy-Transfer]]); Energy-MOC (+[[Energy-Transfer]]); .state/unresolved-links.md (RESOLVED note + Energy-Transfer cleared from baseline backlog).
- Deferred (report-only, user choice): duplicate `Energy.md` (03_Physical-Quantities vs 02_Foundations/GCSE-Foundations) makes `[[Energy]]` ambiguous — separate disambiguation task; 12 maths/CS seed-hub stubs unchanged (out of scope by design); Superposition.md now carries a self-link `[[Superposition|Principle of Superposition]]` under Related Laws — candidate for a future dedicated Principle-of-Superposition law-result page.
- Notes: Root cause = hyphenated link forms (`[[Refraction-of-Waves]]`) not matching spaced frontmatter aliases (`Refraction of Waves`), so Obsidian created grey nodes / blank-file targets. Fix makes links file-targeted with human-readable display, per the user's instruction. No prose overwritten, no pages deleted (§5.4); template followed for the new page (§4). No git commit (§5.11).

## 2026-05-19 — Visual pipeline batch
- Scope: every atomic page under folders 03–12 (325 pages scanned from filesystem ground truth).
- Outcomes (from .state/visual-manifest.tsv): diagram 241, photo 34, both 0, none 50, skip 0.
- Photos: 32 from Wikimedia Commons + 2 from NASA Images library; all licenses pass runbook §4 ALLOW (CC0 / Public Domain / CC BY / CC BY-SA, plus NASA PD). No NC/ND/non-free/fair-use. Every photo Source line carries Title — Author — License — URL — Retrieved date.
- Diagrams: authored for this vault (Mermaid native blocks or hand-authored SVG), Source line "Authored for this vault (CC0)".
- Audit: B1 path check PASS (all _attachments embeds exist and live in the subfolder matching the page top-level folder). B2 license gate PASS (0 violations). B3 size check PASS (no raster >1600px longest edge; one image pre-downscaled, logged in manifest). B4 scope PASS (only folders 03–12, _attachments/, _meta/visual-pipeline-runbook.md, _meta/templates/, .state/, docs/, log.md, pre-existing .obsidian touched). B5 non-destruction spot check PASS (5 random pages: 0 lines removed, only a `## Visuals` block added, frontmatter and all other sections verbatim).
- Manifest: .state/visual-manifest.tsv
- Provenance pages: 13_Sources/Wikimedia-Commons-Image-Pool.md, 13_Sources/NASA-Image-Library.md
- No commit (CLAUDE.md §5.11).

## [2026-05-19] create | Cross-Subject-Links stub pages (user-confirmed)
- Created: 07_Methods/Differentiation.md, Integration.md, Trigonometry.md, Differential-Equations.md (type: method, maths-link); 10_Applications/Logic-Gates.md, Sensors.md, Signal-Processing.md, Data-Logging.md, Simulation.md, Numerical-Modelling.md (type: application, computer-science-link) — 10 pages, each per its `_meta/templates/` template, status: draft.
- Updated: index.md (+4 Methods, +6 Applications); 01_MOCs/Mathematical-Methods-in-Physics-MOC.md (+4 maths methods); .state/unresolved-links.md (Cross-Subject-Links backlog marked RESOLVED).
- Deferred: Mathematical-Methods-Map seed-hub stubs (Gradient, Rearranging-Equations, Dimensional-Analysis, …) — separate task; `[[Vectors]]`/`[[Exponential-Decay]]` no longer on the page (canonical: Vectors-and-Scalars / Radioactive-Decay-Law).
- Notes: Semantic split (maths→method, CS→application) per user choice; deliberately shallow cross-subject orientation pages (~150–250 words) flagged as by-design so lint won't treat thinness as a defect. Every internal wikilink verified against an existing page — no new grey nodes. External resources limited to reputable free educational sources with stable URLs (Khan Academy, Isaac Physics, PMT, BBC Bitesize, OpenStax, Wikipedia). No prose copied; templates followed (§4). No git commit (§5.11).
