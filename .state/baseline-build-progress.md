# Baseline Build Progress — COMPLETE

_2026-05-18. Usable-baseline construction pass finished._

## Phase status

| Phase | Status |
|---|---|
| 1 — Audit (`.state/baseline-build-audit.md`) | ✅ complete |
| 2 — Skills (3 new + 3 cross-referenced) | ✅ complete |
| 3 — Policy files + CLAUDE.md §5.12 | ✅ complete |
| 4 — Baseline page construction (8 builders) | ✅ complete |
| 5 — MOCs + index (5 MOC builders + central index) | ✅ complete |
| 6 — log + state | ✅ complete |
| 7 — Lint + final report | ✅ complete (`.state/wiki-lint-report.md`) |

## Result

- **184 atomic content pages** (was ~30). **All `usable`**, zero content-folder `seed`/`draft`.
- ~150 created + ~22 completed-in-place / elevated.
- ~30 MOCs + 6 home maps rebuilt navigation-only; user banners (GCSE P1–P9, M0–M4, PAG framework, frontier shallow banner) preserved.
- Lint: zero template/source-trace/orphan/physics-quality/frontier-depth/seed violations. Residual: ~11 mentioned-but-unbuilt pages + a few duplicate aliases (logged, for second pass).

## Cluster ledger (Phase 4 — all builders verified on disk)

| Folder | Created | In-place | Skipped/Untouched |
|---|---|---|---|
| 02_Foundations | 15 | 4 | — |
| 03_Physical-Quantities | 31 | 1 | — |
| 04_Concepts | 24 | 0 | 3 pre-existing untouched |
| 05_Laws-and-Results | 16 | 1 | — |
| 06_Models | 12 | 1 | — |
| 07_Methods | 15 | 1 | 5 uncertainty methods untouched |
| 08_Representations | 13 | 1 | 2 untouched |
| 09_Experiments-and-Practicals | 10 | 0 | 3 skipped (dup of 04/07) |
| 10_Applications | 10 | 0 | — |
| 11_Problems/Mistake-Patterns | 11 | 1 | — |
| 12_Frontier-Maps | 4 | 1 | 2 elevated draft→usable |

## Clusters PARTIAL / NOT STARTED (deliberate — second pass)

- `11_Problems/Problem-Types/` + `11_Problems/Worked-Examples/` + `Extension-Problems/` — **not built** (needs OCR past-paper alignment). MOCs hold placeholders.
- Circular-motion-specific & SHM-specific atomic pages (Centripetal-Force, Angular-Velocity, pendulum/spring practicals) — **gap**; those two MOCs map only loosely-related pages.
- Thermal/medical/astro have thin atomic coverage (umbrella only).
- ~11 genuinely-missing + ~42 deferred forward-link stubs → `.state/unresolved-links.md`.

## Honesty note

Phase 4 file counts verified on disk (184, all usable). Phases 5–7 outcomes confirmed from agent manifests + the written lint report. The problem/worked-example layer is intentionally out of this baseline and is the recommended next pass. No git commit (CLAUDE.md §5.11).
