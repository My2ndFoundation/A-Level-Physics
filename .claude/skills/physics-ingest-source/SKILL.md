---
name: physics-ingest-source
description: Use when the user wants to ingest a raw A-Level Physics source into the wiki. Triggers on "ingest", "process this source", "消化这份资料", or when the user supplies a path under raw/ in the A-Level Physics project (specification, textbook, past paper, practical guide, GCSE/foundation material, frontier reference, or notes).
model: claude-opus-4-7
effort: high
---

# A-Level Physics Ingest Workflow

## Overview

Processes one raw source from `raw/` into the physics knowledge graph (`02_Foundations/`、`03_Physical-Quantities/`、`04_Concepts/`、`05_Laws-and-Results/`、`06_Models/`、`07_Methods/`、`08_Representations/`、`09_Experiments-and-Practicals/`、`10_Applications/`、`11_Problems/`、`12_Frontier-Maps/`、`13_Sources/`、`01_MOCs/`). The authoritative procedure is `CLAUDE.md` §10 and `_meta/workflows/ingest-workflow.md`; this skill enforces the step ordering, the **template-read step**, the **learning-layer classification step**, the **user checkpoint**, and the **copyright** and **no-overwrite** rules so they cannot be skipped.

This is **not** a textbook-copying workflow. The source page is a provenance and extraction record, not reproduced source text.

## Arguments

The skill accepts one raw file path:
```
/physics-ingest-source raw/specifications/<file>
/physics-ingest-source raw/textbooks/<file>
/physics-ingest-source raw/gcse-foundations/<file>
/physics-ingest-source raw/past-papers/<file>
/physics-ingest-source raw/practicals/<file>
/physics-ingest-source raw/frontier/<file>
/physics-ingest-source raw/notes/<file>
```

If no argument: ask "想 ingest `raw/` 下的哪一份资料？(specifications / textbooks / gcse-foundations / past-papers / practicals / frontier / notes / other)" Do not guess. Do not scan-and-pick on your own — that is `/physics-scan-raw`'s job.

## The Three Non-Negotiable Rules

**1. You MUST read the required `_meta/templates/` template for every page type you will write, BEFORE writing any page of that type (CLAUDE.md §4, §10 Step 4).**

This is the project's signature rule. The page `type:` in frontmatter determines the required template. If a template and any lower-level instruction conflict, **the template wins**. Skipping this step makes the skill wrong.

**2. You MUST classify the source's learning layer BEFORE the checkpoint (CLAUDE.md §2, §10 Step 5).**

Every candidate is tagged to one layer: everyday / pre-GCSE / GCSE / bridge-to-A-Level / A-Level OCR H556 core / frontier. The A-Level H556 layer is the main detailed layer; foundation layers stay simple; **frontier pages stay shallow** (CLAUDE.md §3, `_meta/frontier-rules.md`) — orientation, not mastery, no university derivations.

**3. You MUST run the Step 6 checkpoint and wait for the user to confirm BEFORE writing anything to the wiki (CLAUDE.md §10 Step 7).**

No file in `02_…`–`13_…`、`01_MOCs/`、`00_Home/`、`index.md`、`log.md`、`.state/` is touched until the user has confirmed direction.

Equally non-negotiable:
- **`raw/` is read-only.** Never write, rename, reformat, or delete anything under `raw/` (CLAUDE.md §5.1). The only exception is creating `.gitkeep` placeholders, which is not part of ingest.
- **Do not reproduce copyrighted source material** (CLAUDE.md §5.2, `_meta/copyright-rules.md`). No full chapters, no long verbatim passages, no full reproduced copyrighted worked examples, no bulk exercise copying. Paraphrase; use formula-level excerpts, page/section/question references, and original explanations only. The `13_Sources/` page must **never** contain full source text.
- **Never silently overwrite** a differing claim — preserve it with the source-variation block (CLAUDE.md §5.4):
  ```markdown
  > ⚠️ Source variation:
  > This source presents the idea differently from [[Existing-Page]].
  > Difference: ...
  > Action: preserved as a variant, not silently overwritten.
  ```
- **Never duplicate** an entity that already exists under an alias — alias-search first (CLAUDE.md §5.3). One physical object / concept / law / model / method / representation / misconception = one canonical page.
- **Broad topics are MOCs only.** Never create `Mechanics.md`, `Electricity.md`, `Waves.md`, `Energy.md`, etc. as content pages (CLAUDE.md §5.5).
- **Physics pages connect intuition, maths, graphs, experiment, and assumptions** (CLAUDE.md §5.10, §12) — not formula-only notes.

## Workflow (follow in order, no skipping)

**Step 1 — Read the raw source end-to-end (CLAUDE.md §10 Step 1)**
Read the entire file (or the relevant chapter/section the user named). Note the source type (specification / textbook / past paper / practical guide / GCSE-foundation / frontier reference / notes), publisher/exam board if identifiable, and chapter/section/page or question references. Identify the OCR module it maps to (Modules 1–6 of H556) if applicable. Never modify the raw file.

**Step 2 — Identify candidate knowledge objects (CLAUDE.md §10 Step 2)**
List candidates grouped by page type: `foundation`, `common-sense`, `physical-quantity`, `concept`, `law-result`, `model`, `method`, `representation`, `experiment-practical`, `application`, `problem-type`, `worked-example`, `mistake-pattern`, `frontier-map`. Keep each candidate atomic (one object per page, ~300–800 words target; frontier maps may be slightly longer but stay shallow). If a candidate is a broad topic (Mechanics, Waves…), it is a MOC update, not a content page.

**Step 3 — Search aliases and existing pages (CLAUDE.md §10 Step 3)**
Before deciding what is "new":
- Grep `.state/aliases.tsv` and existing filenames/frontmatter `aliases:` across `02_…`–`13_…` for every candidate. One object = one page.
- For each existing match, plan an **update** (append source trace + add nuance only), not a new page.
- Record any candidate you cannot resolve in `.state/unresolved-links.md` planning notes for Step 13.

**Step 4 — Read the required templates ← MUST NOT BE SKIPPED (CLAUDE.md §4, §10 Step 4)**
For every page type you intend to write or substantially update, read its template from `_meta/templates/` now:

| `type:` | Template | Default folder |
|---|---|---|
| `foundation` | `_meta/templates/foundation-template.md` | `02_Foundations/` |
| `common-sense` | `_meta/templates/common-sense-template.md` | `02_Foundations/Everyday-Physics/` |
| `frontier-map` | `_meta/templates/frontier-map-template.md` | `12_Frontier-Maps/` |
| `physical-quantity` | `_meta/templates/physical-quantity-template.md` | `03_Physical-Quantities/` |
| `concept` | `_meta/templates/concept-template.md` | `04_Concepts/` |
| `law-result` | `_meta/templates/law-result-template.md` | `05_Laws-and-Results/` |
| `model` | `_meta/templates/model-template.md` | `06_Models/` |
| `method` | `_meta/templates/method-template.md` | `07_Methods/` |
| `representation` | `_meta/templates/representation-template.md` | `08_Representations/` |
| `experiment-practical` | `_meta/templates/experiment-practical-template.md` | `09_Experiments-and-Practicals/<subfolder>/` |
| `application` | `_meta/templates/application-template.md` | `10_Applications/` |
| `problem-type` | `_meta/templates/problem-type-template.md` | `11_Problems/Problem-Types/` |
| `worked-example` | `_meta/templates/worked-example-template.md` | `11_Problems/Worked-Examples/` |
| `mistake-pattern` | `_meta/templates/mistake-pattern-template.md` | `11_Problems/Mistake-Patterns/` |
| `source` | `_meta/templates/source-template.md` | `13_Sources/<subfolder>/` |
| `moc` | `_meta/templates/moc-template.md` | `01_MOCs/` or `00_Home/` |

Every page written in Steps 8–10 must follow its template's frontmatter and section structure exactly.

**Step 5 — Classify the learning layer ← MUST NOT BE SKIPPED (CLAUDE.md §2, §3, §10 Step 5)**
For the source overall and per candidate, assign a layer: `everyday-physics` / `pre-gcse` / `gcse-foundation` / `bridge-to-a-level` / `a-level-core` / `frontier`. This drives folder, `level:` frontmatter, tags (`_meta/tags.md`), and depth. Frontier candidates must be shallow `frontier-map` pages under `12_Frontier-Maps/` — never deep textbook expansions (`_meta/frontier-rules.md`).

**Step 6 — Checkpoint with the user ← REQUIRED BEFORE ANY WRITES (CLAUDE.md §10 Step 6)**
Report in chat:
- One-paragraph summary of the source and its overall learning layer.
- Extracted entity list, grouped by page type, each marked **new page** or **update existing `[[Page]]`**, with its learning layer.
- Proposed source page filename and target subfolder under `13_Sources/` (e.g. `13_Sources/Textbooks/<title>.md`, `13_Sources/OCR-Physics-H556/<title>.md`, `13_Sources/Practical-Resources/<title>.md`).
- MOCs that will be touched (e.g. `[[Mechanics-MOC]]`, `[[Practical-Skills-MOC]]`).
- Copyright considerations (what will be paraphrased vs. referenced-only).
- Frontier-depth note: confirm any frontier candidates will stay shallow.
- Any contradictions with existing pages, gaps, or unresolved candidates.

**Wait for the user.** They may redirect emphasis, rename pages, drop entities, merge aliases, narrow scope, or reclassify a layer.

**Step 7 — (gate) Proceed only after explicit user confirmation.**

**Step 8 — Create or update the source page (CLAUDE.md §10 Step 8, §11)**
Use `_meta/templates/source-template.md`. Fill frontmatter (`type: source`, `source_type:`, `exam_board:`, `raw_path:`, `learning_layer:`, `processed_date:` = today, `status:`). Populate the metadata block, one-sentence summary, and the extracted-* sections as `[[wikilinks]]`. Record copyright limitations and page/question references. **No full source text** — this page must be a self-contained metadata + extraction record.

**Step 9 — Create stubs / update atomic pages (CLAUDE.md §10 Step 9)**
- **New entity** → create the page in its default folder using its template's full scaffolding. Set `status: draft`. Populate the core sections from the source (paraphrased/original), wikilink related objects, connect intuition/maths/graph/experiment where the template asks (CLAUDE.md §5.10, §12), and fill `## Source Trace` pointing at the Step 8 source page.
- **Existing entity** → append the source under `## Source Trace` / `sources:`; enrich a content section only if this source genuinely adds nuance. On any difference in notation/scope/assumptions/model-limits/sign-convention/graph-interpretation/practical-method/syllabus-emphasis/maths-level/GCSE-vs-A-Level/frontier-vs-A-Level, insert the `> ⚠️ Source variation:` block — never overwrite. Bump frontmatter `sources:` and `status:` as appropriate.
- All pages: mandatory frontmatter (CLAUDE.md §5.7), mandatory wikilinks (CLAUDE.md §5.9), 300–800-word target (CLAUDE.md §5.6), equations define every symbol + units + conditions, graphs explain gradient/area/intercepts (CLAUDE.md §12).

**Step 10 — Update relevant MOCs (CLAUDE.md §10 Step 10, `_meta/workflows/moc-update-workflow.md`)**
Add each new page under the correct heading in its MOC(s). MOCs are navigation only — no explanations, no duplicated content (CLAUDE.md §5.8). Preserve existing entries and ordering; use canonical wikilinks.

**Step 11 — Update `index.md` (CLAUDE.md §10 Step 11)**
Add new pages under their type section (Foundations / Common-Sense Physics / Physical Quantities / Concepts / Laws and Results / Models / Methods / Representations / Experiments and Practicals / Applications / Problems / Frontier Maps). Add the source page under `## Sources`.

**Step 12 — Append to `log.md` (CLAUDE.md §10 Step 12)**
Append one parseable entry using today's date:
```
## [YYYY-MM-DD] ingest | <source title>
- Created: <source page + new atomic pages>
- Updated: <updated pages + MOCs + index>
- Deferred: <unresolved candidates>
- Notes: <contradictions / source variations / copyright notes / layer notes>
```

**Step 13 — Append to `.state/ingested.tsv` (CLAUDE.md §10 Step 13)**
This file is the canonical "processed raw" list that `/physics-scan-raw` diffs against. The header is:
```
raw_path	date	source_page	status	notes
```
Append exactly one TAB-separated row, no quoting, 5 fields (the last may be empty but the tabs must be present):
```
<raw_path>\t<YYYY-MM-DD>\t<source_page>\t<status>\t<notes>
```
- `<raw_path>` — the exact path you were given (e.g. `raw/textbooks/<file>`).
- `<YYYY-MM-DD>` — today's date (same date as the `log.md` entry).
- `<source_page>` — the file written in Step 8 (e.g. `13_Sources/Textbooks/<title>.md`).
- `<status>` — `ingested` for a complete pass, `partial` if some candidates were deferred.
- `<notes>` — short note or empty.

Append-only: never reorder, deduplicate, or rewrite prior rows. Also update `.state/aliases.tsv` for any new aliases and `.state/unresolved-links.md` for anything mentioned but not yet resolved to a canonical page.

**Step 14 — Report back (CLAUDE.md §10 Step 14)**
Tell the user: number of pages created/updated by layer, list of `⚠️ Source variation` flags raised, deferred/unresolved items, and that `.state/ingested.tsv` (and aliases / unresolved-links) was updated.

**Step 15 — DO NOT auto-commit (CLAUDE.md §5.11)**
Leave the working tree untouched by git. Only commit if the user explicitly asks.

## Edge Cases

| Situation | Handling |
|---|---|
| Raw file unreadable / unparseable (e.g. scanned PDF with no text) | Stop. Report. Write nothing. Suggest the user supply a text version. |
| Source is a copyrighted textbook chapter | Paraphrase + reference only. Source page records structure and page numbers, not text. Worked examples must be re-derived/original. |
| Candidate is a broad topic (Mechanics, Waves, Fields…) | It is a MOC update, not a content page (CLAUDE.md §5.5). |
| Candidate is beyond A-Level (quantum formalism, GR, QFT…) | Make it a shallow `frontier-map` page (CLAUDE.md §3, `_meta/frontier-rules.md`) — orientation only, links back to A-Level. |
| Ambiguous entity (could be 2 existing pages) | Alias-search first; if still unresolved, ask the user in the Step 6 checkpoint. |
| Source contradicts an existing wiki claim | `> ⚠️ Source variation:` block inside the entity page; surface in Step 14. Do not edit the contradicted claim. |
| GCSE simplification vs A-Level treatment of the same idea | Keep both: foundation/bridge page for the GCSE view, A-Level page for the precise view; cross-link, don't merge into one blurred page. |
| Practical guide with apparatus/method/uncertainty | Use `experiment-practical` pages; capture variables, uncertainty, graph use (CLAUDE.md §12). Consider routing to `/physics-practical-extract`. |
| Past paper with many questions | Extract recurring `problem-type` / `mistake-pattern` pages + a few original `worked-example` pages; cite question numbers, do not bulk-copy. Consider `/physics-problem-extract`. |
| Page would exceed ~800 words / covers a whole chapter | Split into atomic pages (CLAUDE.md §5.6). |
| Batch request (>1 raw file) | Confirm explicitly — default is one source at a time. Direct the user to `/physics-scan-raw` for sequenced batches. |
| `.state/ingested.tsv` header missing/corrupt | Surface to the user; do not silently rewrite the file. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Writing pages before reading the `_meta/templates/` template | Step 4 is non-optional and is the project's signature rule (CLAUDE.md §4) |
| Skipping the learning-layer classification | Step 5 — every candidate gets a layer; frontier stays shallow |
| Writing wiki pages before the Step 6 checkpoint | Always checkpoint first — the single most-skipped step |
| Copying long passages or full worked examples from a textbook | Paraphrase / re-derive; reference page & question numbers only |
| Putting source text into the `13_Sources/` page | Source pages are metadata + extraction records, never source text |
| A formula-only page with no intuition/graph/experiment | CLAUDE.md §5.10, §12 — connect meaning, maths, graph, measurement, traps |
| Letting a frontier page become a university textbook | `_meta/frontier-rules.md` — orientation, not mastery |
| Creating a duplicate page because alias-search was skipped | Step 3 is mandatory; grep `.state/aliases.tsv` + `aliases:` everywhere |
| Overwriting a claim the new source contradicts | Use the `> ⚠️ Source variation:` block, never silent overwrite |
| Creating `Mechanics.md` / `Waves.md` as content pages | Broad topics are MOCs only |
| Missing or partial frontmatter / no wikilinks | Every content page: full template frontmatter + wikilinks |
| Writing to `raw/` (header, typo fix, reformat) | `raw/` is immutable. Read only. |
| Writing a 3-field `ingested.tsv` row | This project's header is 5 fields: `raw_path date source_page status notes` |
| Reordering / rewriting prior `ingested.tsv` rows | Append-only. Surface bad rows to the user instead. |
| Forgetting to update MOCs / `index.md` / `log.md` | Steps 10–12 are part of every ingest |
| Auto-committing at the end | Step 15 — leave the diff for the user |

## Red Flags — STOP

- About to `Write`/`Edit` a wiki page without having read its `_meta/templates/` template (Step 4)
- About to write pages without having classified their learning layer (Step 5)
- About to `Write`/`Edit` a wiki file before the user responded to the Step 6 checkpoint
- About to `Write`/`Edit` anything under `raw/`
- About to paste a long verbatim textbook passage or a full copyrighted worked example anywhere
- About to put source text into a `13_Sources/` page
- About to write a frontier page with university-level derivations
- About to create `04_Concepts/X.md` (etc.) without grepping `aliases:` for X
- About to create a broad-topic content page instead of updating a MOC
- About to overwrite a contradicting claim instead of using the `⚠️ Source variation` block
- About to finish without appending to `.state/ingested.tsv` (5-field row)
- About to rewrite or reorder rows in `.state/ingested.tsv`
- About to run `git commit`

All of these mean: **stop, back up, re-read `CLAUDE.md` §2, §3, §4, §5, §10 and `_meta/copyright-rules.md`, `_meta/frontier-rules.md`.**
