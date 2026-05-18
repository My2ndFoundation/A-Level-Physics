---
name: physics-lint-wiki
description: Use when the user wants to audit wiki health in the A-Level Physics project — "lint the wiki"、"check page health"、"扫一下有没有坏链/孤儿页"、"audit the vault"、"find template violations"、"find orphan pages"、"check frontier depth". Reports problems (and only fixes after explicit confirmation).
model: claude-sonnet-4-6
effort: medium
---

# A-Level Physics Wiki Linter

## Overview

Health-checks the wiki layer (`02_Foundations/`…`13_Sources/`、`01_MOCs/`、`00_Home/`、`index.md`) and reports problems. The authoritative check list is `_meta/workflows/lint-workflow.md` and `CLAUDE.md` §13. This skill **reports**; it does not silently rewrite content.

> **Baseline build note.** Used as the per-cluster lint pass during baseline
> construction (`_meta/baseline-build-policy.md`). After a baseline pass,
> `status: seed` pages in built clusters are a real finding (the bar is
> `usable`), reported with normal — not low — severity.

## Arguments

Optional scope:
```
/physics-lint-wiki                    # whole wiki
/physics-lint-wiki 04_Concepts        # one folder
/physics-lint-wiki [[Acceleration]]   # one page
```

## The Non-Negotiable Rules

- **Read-only by default.** Produce a report. Do **not** auto-fix. Apply fixes only after the user confirms specific items (CLAUDE.md §13, `_meta/workflows/lint-workflow.md`).
- **Never write to `raw/`** (CLAUDE.md §5.1).
- **No silent overwrite / no deletion as a "fix".** A contradicting claim gets the `> ⚠️ Source variation:` treatment, not removal (CLAUDE.md §5.4). Orphan pages are reported, never auto-deleted.
- **Fixes obey templates.** Any confirmed content fix must keep the page's `_meta/templates/` structure (CLAUDE.md §4).
- **`_meta/` is not learner content** — its templates/workflows are scaffolding; lint them for existence, not as wiki pages.
- **No auto-commit** (CLAUDE.md §5.11).

## Workflow

**Step 1 — Enumerate pages in scope**
Collect `.md` files under `00_Home/`、`01_MOCs/`、`02_…`–`13_…`. Exclude `.gitkeep`, `_meta/`, `.state/`, `raw/`.

**Step 2 — Run the checks (CLAUDE.md §13, lint-workflow)**
- Missing or partial frontmatter (non-MOC content needs `type, subject, tags, level, status, aliases, sources`; CLAUDE.md §5.7).
- `type:` ↔ folder mismatch (per the §4 mapping table).
- Template-section violations: required sections of the page's template missing or absent.
- Missing source trace (`## Source Trace` empty *and* `sources: []`).
- Orphan pages (no inbound wikilink anywhere and not listed in any MOC).
- Broken wikilinks (target resolves to no canonical filename and no `.state/aliases.tsv` alias). Account for Obsidian `[[Page|display]]`, `[[Page#heading]]`, and case.
- Duplicate aliases (same alias → ≥2 canonical pages, in pages' `aliases:` or `.state/aliases.tsv`).
- Broad-topic content pages that must be MOCs (`Mechanics.md`, `Electricity.md`, `Waves.md`, `Energy.md`… as content; CLAUDE.md §5.5).
- MOCs missing links to existing pages in their topic area.
- Pages > 800 words that may need splitting (CLAUDE.md §5.6).
- **Physics quality gaps (CLAUDE.md §12):** `physical-quantity` without an SI unit; `law-result` without conditions or symbol/unit definitions; `representation`/graph page without gradient/area/intercept interpretation; `experiment-practical` without independent/dependent/control variables or uncertainty; equation pages with undefined symbols.
- **Layer/connectivity gaps (CLAUDE.md §2, §5.10):** A-Level page with no foundation/prerequisite link where one is clearly relevant; `common-sense` page not linked to any A-Level idea.
- **Frontier-depth violations (CLAUDE.md §3, `_meta/frontier-rules.md`):** `frontier-map` pages containing university-level derivations, dense formalism, or missing the required "what not to worry about yet" / A-Level-entry-points framing.
- Graph gaps: `problem-type` without related methods; `method` without a worked example; `concept` without applications.
- Cross-check `.state/unresolved-links.md` for mentioned-but-missing objects.

**Step 3 — Report**
Group by check. For each offender give `path` (and section), the problem, and a recommended action. Note severity: `seed`-status pages that are intentionally thin → low severity.

**Step 4 — Ask before fixing**
List which fixes are safe and mechanical (e.g. add missing wikilink, fix `type:`/folder, add a missing template section header, add an alias to `.state/aliases.tsv`) vs. which need judgement (frontier-depth trims, splitting an over-long page, resolving a contradiction). Ask the user which to apply. Do not proceed unprompted.

**Step 5 — Apply only confirmed fixes**
Keep template structure; never overwrite a claim (use the `⚠️` block); never delete a page without explicit instruction. Splitting an over-long page requires the same care as `/physics-expand-concept` (new atomic pages via template + MOC/index update). Trimming a too-deep frontier page means moving the depth out, not deleting the orientation.

**Step 6 — Log & report**
If anything was changed, append a `## [YYYY-MM-DD] lint | <scope>` entry to `log.md` (Created/Updated/Deferred/Notes). Report what changed and what was deferred.

**Step 7 — DO NOT auto-commit** (CLAUDE.md §5.11).

## Edge Cases

| Situation | Handling |
|---|---|
| `[[Link]]` with display/heading (`[[A\|B]]`, `[[A#H]]`) | Resolve on the page name only; not a broken link. |
| Page is `status: seed` | Intentionally thin — report under low severity, do not flag as failure. |
| Alias collision is legitimate (genuine synonyms of one object) | Recommend merging into one canonical page, not splitting the alias. |
| Orphan page that is a deliberate hub/entry | Confirm with user before recommending changes; never auto-delete. |
| Broad page found as content (e.g. `04_Concepts/Mechanics.md`) | Report as a §5.5 violation; recommend converting to `01_MOCs/Mechanics-MOC.md` — do not auto-move. |
| Frontier page is deep but the user wants it that way | Report under §3; the depth rule is the project's — surface it, let the user decide. |
| GCSE-foundation page intentionally simpler than its A-Level counterpart | Not a defect — the layer model (CLAUDE.md §2) expects this. Don't flag simplicity as a quality gap. |
| Template itself changed in `_meta/templates/` | Out of scope — lint flags pages vs. their template, not the templates. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Auto-fixing without the Step 4 confirmation | Report first; fix only confirmed items |
| Deleting orphan pages | Report only; deletion is the user's call |
| "Fixing" a contradiction by overwriting | Use the `> ⚠️ Source variation:` block |
| Flagging a GCSE/foundation page as "too shallow" | Layer model expects graded depth (CLAUDE.md §2) |
| Treating `_meta/` or `raw/` files as wiki pages | They're scaffolding/immutable — exclude from content checks |
| Flagging `[[A\|B]]` as a broken link | Resolve on page name only |
| Reformatting a page beyond the confirmed fix | Minimal, template-preserving edits only |
| Auto-committing the cleanup | Leave the diff for the user |

## Red Flags — STOP

- About to `Write`/`Edit` a page before the user confirmed that specific fix
- About to delete a page or section as a "fix"
- About to overwrite a contradicting claim instead of flagging it
- About to `Write`/`Edit` anything under `raw/` or `_meta/`
- About to run `git commit`
