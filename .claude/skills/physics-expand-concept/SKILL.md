---
name: physics-expand-concept
description: Use when the user wants to deepen or improve an existing atomic page in the A-Level Physics project — "expand [[Page]]"、"flesh out this concept"、"深化这一页"、"improve [[...]] from this source". Enriches one existing page while preserving its template, source trace, and existing content.
model: claude-opus-4-7
effort: high
---

# A-Level Physics Concept Expander

## Overview

Takes one **existing** atomic page (`foundation`/`common-sense`/`physical-quantity`/`concept`/`law-result`/`model`/`method`/`representation`/`experiment-practical`/`application`/`problem-type`/`mistake-pattern`/`frontier-map`) and improves it using approved sources, while preserving template compliance, the existing source trace, and prior content. Authoritative rules: `CLAUDE.md` §2, §3, §4, §10 spirit, §12. This is **not** ingestion of a new raw file — use `/physics-ingest-source` for that.

## Arguments

```
/physics-expand-concept [[Acceleration]]
/physics-expand-concept 05_Laws-and-Results/Newton-Second-Law.md  using [[Source-Page]]
```

If no target page: ask which page. If no source named: ask whether to expand from an existing `13_Sources/` page or a user-supplied (already-ingested) source — do **not** silently invent facts.

## The Non-Negotiable Rules

- **Read the page's `_meta/templates/` template before editing** (CLAUDE.md §4). Edits must keep its frontmatter and section structure.
- **Respect the learning layer** (CLAUDE.md §2). A `foundation`/GCSE page stays simple; an A-Level page gets precise; a `frontier-map` stays shallow — orientation only, no university derivations (CLAUDE.md §3, `_meta/frontier-rules.md`). Do not "upgrade" a foundation page into an A-Level page — link to the A-Level page instead.
- **Checkpoint before writing** (CLAUDE.md §10 spirit): present proposed additions and wait for the user.
- **Provenance required.** New factual content must trace to an approved source page; record it in `## Source Trace` and `sources:`. Do not inject unsourced training-data facts as if from the wiki — if you must use general knowledge, flag it for the user at the checkpoint.
- **Copyright** (`_meta/copyright-rules.md`, CLAUDE.md §5.2): paraphrase, formula-level excerpts, references — never long verbatim or full copyrighted worked examples.
- **Physics completeness** (CLAUDE.md §5.10, §12): an expanded page should connect intuition, meaning, equation (every symbol + unit + condition), graph (gradient/area/intercepts), measurement, assumptions, typical problem type, and common mistake — not become a formula-only note.
- **Never silently overwrite.** Preserve prior content; on a differing claim use the `> ⚠️ Source variation:` block (CLAUDE.md §5.4). Keep any user-written prose.
- **Stay atomic.** If expansion pushes the page past ~800 words or beyond one purpose, split into new atomic pages instead (CLAUDE.md §5.6).
- **No auto-commit** (CLAUDE.md §5.11).

## Workflow

**Step 1 — Read the target page and its required template**
Confirm `type:` ↔ folder, learning `level:`, current sections, thin/empty sections, missing wikilinks, and the existing `## Source Trace`.

**Step 2 — Gather approved material**
Use the named/existing `13_Sources/` page(s) or user-supplied already-ingested content. Identify what each section is genuinely missing (definition rigor, SI unit, scalar/vector status, conditions, prerequisites/foundation links, related laws/models, graph interpretation, measurement method, applications, common mistakes, frontier links).

**Step 3 — Checkpoint**
Report: proposed additions per section, sources backing each, any contradiction with the current page, whether a split is needed and the proposed new page names, and confirmation that the page's learning layer / frontier depth is respected. Flag any general-knowledge content. **Wait for the user.**

**Step 4 — (gate) Proceed only after confirmation.**

**Step 5 — Apply the edits**
Preserve existing content and order; fill/extend sections within the template; add wikilinks for every related object (CLAUDE.md §5.9); add `> ⚠️ Source variation:` blocks where the source differs; bump frontmatter `sources:` and `status:` (e.g. `seed`/`draft` → `draft`/`reviewed`). Update `## Source Trace`.

**Step 6 — Split if required**
Create the new atomic page(s) using their templates, wikilink them from the original, and add them to the relevant MOC and `index.md`.

**Step 7 — Propagate links**
Add new pages/links to the relevant MOC(s) (navigation only) and `index.md`. Add the page under the source page's `## Generated or Updated Pages` if applicable.

**Step 8 — Append `log.md`**
`## [YYYY-MM-DD] expand | <page>` with Created/Updated/Deferred/Notes (note any `⚠️` flags).

**Step 9 — DO NOT auto-commit** (CLAUDE.md §5.11).

## Edge Cases

| Situation | Handling |
|---|---|
| Target page does not exist | This is ingestion/creation — redirect to `/physics-ingest-source`, do not create from scratch here. |
| No approved source for a needed fact | Flag at checkpoint; either get a source or mark the section as deferred — don't fabricate provenance. |
| Source contradicts the page | `> ⚠️ Source variation:` block; never overwrite. Surface in Step 8. |
| Expansion exceeds ~800 words | Split into atomic pages (Step 6), don't bloat. |
| User asks to deepen a `frontier-map` | Add breadth/links and clearer orientation, not university maths (CLAUDE.md §3). If they want true depth, that belongs in an A-Level page, not the map. |
| User asks to "make this foundation page A-Level level" | Don't morph layers — create/expand the A-Level page and cross-link (CLAUDE.md §2). |
| Page is a broad-topic page that slipped through | Don't expand it — flag as a §5.5 violation (route to `/physics-lint-wiki`). |
| User-written prose in a section | Preserve verbatim; add alongside, don't replace. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Editing before reading the template | Step 1 is mandatory (CLAUDE.md §4) |
| Writing before the Step 3 checkpoint | Always checkpoint |
| Adding unsourced facts as if wiki-canonical | Require a source page; flag general knowledge |
| Deepening a frontier map into a textbook | Keep it shallow (CLAUDE.md §3, frontier-rules) |
| Collapsing the layer model (foundation → A-Level in place) | Cross-link layers; don't morph one page |
| Leaving a quantity/law page without unit/conditions | CLAUDE.md §12 — units, symbols, conditions are required |
| Overwriting prior content/user prose | Append + `⚠️` block; preserve |
| Bloating one page past atomic size | Split into new template-compliant pages |
| Forgetting to bump `sources:` / `status:` | Update frontmatter on every edited page |
| Skipping MOC/index propagation for new split pages | Steps 6–7 |
| Auto-committing | Leave the diff |

## Red Flags — STOP

- About to `Write`/`Edit` the page without having read its `_meta/templates/` template
- About to write before the user answered the Step 3 checkpoint
- About to add a factual claim with no source / fabricated `## Source Trace`
- About to push university-level depth into a `frontier-map`
- About to convert a foundation page into an A-Level page in place
- About to overwrite existing or user-written content
- About to let the page exceed atomic scope instead of splitting
- About to `Write` under `raw/`, or to `git commit`
