---
name: physics-practical-extract
description: Use when the user wants to turn a practical guide or experiment write-up into the practical layer of the A-Level Physics wiki — "extract the practicals from [[Source]]"、"process this practical guide"、"build the required-practical pages"、"拆实验/做实验页". Produces experiment-practical, measurement, uncertainty, graph-analysis, and apparatus-technique pages.
model: claude-opus-4-7
effort: high
---

# A-Level Physics Practical Extractor

## Overview

Processes a source's practical content into the **practical layer** under `09_Experiments-and-Practicals/`:
- `Required-Practicals/` — OCR H556 PAG / required practicals
- `Measurement-and-Uncertainty/` — measurement methods, uncertainty analysis
- `Graph-Analysis/` — linearising, gradient/intercept/area extraction of physical quantities
- `Apparatus-and-Techniques/` — instrument/technique pages (micrometer, oscilloscope, light gates…)

All pages are `type: experiment-practical` and follow `_meta/templates/experiment-practical-template.md`. It also wires links to the `physical-quantity`/`law-result`/`representation`/`method`/`mistake-pattern` pages each practical exercises. Authoritative rules: `CLAUDE.md` §4, §5, §10, §12, `_meta/copyright-rules.md`.

Scope boundary: this skill builds the practical layer from an **already-represented** source. If given a fresh raw file, run `/physics-ingest-source` first (which writes the `13_Sources/` page and `.state/ingested.tsv`); this skill then deepens the practical layer.

## Arguments

```
/physics-practical-extract [[CLEAPSS-Young-Modulus-Guide]]   # existing 13_Sources/ page
/physics-practical-extract raw/practicals/<file>              # will require ingest first
```

If no argument: ask which practical source/guide. Do not guess.

## The Non-Negotiable Rules

- **Read the templates first** (CLAUDE.md §4): `experiment-practical-template.md`, plus `representation-template.md` / `method-template.md` / `mistake-pattern-template.md` for any new linked page — before writing any of them.
- **Every practical page must carry the §12 experiment essentials** (CLAUDE.md §12): aim; **independent / dependent / control variables**; apparatus; method; what is measured and how; data processing; graph use (axes, gradient, intercept, area where relevant); **uncertainty sources and how to reduce them**; safety / practical limits where relevant. A practical page missing variables or uncertainty is wrong.
- **Copyright** (`_meta/copyright-rules.md`, CLAUDE.md §5.2): practical guides and exam-board PAG documents are copyrighted. Paraphrase method steps in original wording; cite the source guide and section. Never paste long verbatim procedure text or reproduce full copyrighted worksheets.
- **Safety is paraphrased guidance, not authority.** Record hazards/precautions as study notes referencing the source; never present the wiki as the authoritative risk assessment.
- **Checkpoint before writing** (CLAUDE.md §10): present the extraction plan and wait.
- **Search aliases / existing pages first** (CLAUDE.md §5.3). One experiment / technique = one canonical page; prefer updates over duplicates. Distinguish a *required practical* page from a generic *technique* page (e.g. `Measuring-Young-Modulus` vs `Using-a-Micrometer`).
- **Never silently overwrite** — `> ⚠️ Source variation:` block on a differing method, apparatus, or uncertainty treatment (CLAUDE.md §5.4).
- **State accounting:** if a fresh raw file was consumed *here* (not via `/physics-ingest-source`), append one 5-field row to `.state/ingested.tsv` with `status: partial` (practical-layer only). Otherwise record coverage on the existing source page's `## Extracted Experiments and Practicals`; never double-append.
- **No auto-commit** (CLAUDE.md §5.11).

## Workflow

**Step 1 — Read the source and required templates**
If a raw practical path was given and it is not yet in `.state/ingested.tsv`, stop and route to `/physics-ingest-source` first (or get explicit user permission to also do the source-page step here). Then read the experiment-practical template (and any linked-page templates).

**Step 2 — Identify practical units**
List each distinct practical/technique. For each note: aim; variables (IV/DV/control); apparatus; outline method; the physical quantity determined and the relationship used; the graph that yields it (axes, gradient/intercept/area meaning); main uncertainty sources; relevant `mistake-pattern`s; the target subfolder (`Required-Practicals` / `Measurement-and-Uncertainty` / `Graph-Analysis` / `Apparatus-and-Techniques`). Map to the OCR H556 PAG if applicable.

**Step 3 — Alias-search existing pages**
Grep `.state/aliases.tsv`, `09_Experiments-and-Practicals/`, `08_Representations/`, `07_Methods/` for each candidate. Plan updates over new pages. A graph-analysis page may reuse an existing `representation` page — link, don't duplicate.

**Step 4 — Checkpoint**
Report: proposed `experiment-practical` pages (new/update) with their subfolder, the variables/uncertainty captured for each, linked quantity/law/representation/method/mistake pages, and the copyright handling (paraphrased vs reference-only). **Wait for the user.**

**Step 5 — (gate) Proceed only after confirmation.**

**Step 6 — Write the practical layer**
Use the experiment-practical template fully: aim, variables, apparatus, method (paraphrased), measurements, data processing, graph use, uncertainty, safety/limits, related quantities/laws (wikilinks), common mistakes, source trace. Create/link `representation` (graph) and `method` pages where the analysis warrants its own atomic page. Apply `⚠️` blocks on differing methods/uncertainty treatments.

**Step 7 — Wire the graph**
Cross-link practicals ↔ measured quantities ↔ governing laws/models ↔ graph representations ↔ analysis methods ↔ mistake-patterns. Update `Practical-Skills-MOC`, the relevant topic MOC(s), and `Mistake-Patterns-MOC` if traps were added (navigation only). Update `index.md` under Experiments and Practicals. Update the source page's `## Extracted Experiments and Practicals` / `## Generated or Updated Pages`.

**Step 8 — State & log**
Per the state rule above (append `.state/ingested.tsv` only if a fresh raw file was consumed here, `status: partial`; else update the source page). Append `## [YYYY-MM-DD] practical-extract | <source>` to `log.md` (Created/Updated/Deferred/Notes incl. `⚠️` flags).

**Step 9 — DO NOT auto-commit** (CLAUDE.md §5.11).

## Edge Cases

| Situation | Handling |
|---|---|
| Raw practical guide not yet ingested | Route to `/physics-ingest-source` first; don't duplicate the source-page pipeline silently. |
| Procedure text is copyrighted (CLEAPSS / board PAG) | Paraphrase steps in original wording; cite the guide + section; never paste verbatim. |
| Page would lack IV/DV/control or uncertainty | Not shippable — fill those sections or defer the page (CLAUDE.md §12). |
| Required practical vs generic technique | Two page kinds: the named required-practical page and the reusable technique/apparatus page; cross-link, don't merge. |
| Graph analysis is substantial (linearisation, log plots) | Give it its own `Graph-Analysis/` page (still `experiment-practical`) and link the `representation`/`method`. |
| Source's method contradicts an existing practical page | `> ⚠️ Source variation:` block; never overwrite. |
| Apparatus is a frontier instrument beyond A-Level | Keep the practical page A-Level; if the user wants the modern context, route the orientation to `/physics-frontier-map`. |
| Safety/risk content | Record as paraphrased study notes referencing the source; not an authoritative risk assessment. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Copying procedure text verbatim | Paraphrase; cite guide + section |
| Practical page missing variables / uncertainty | CLAUDE.md §12 — both are required sections |
| Writing before reading the templates | CLAUDE.md §4 — Step 1 |
| Writing before the Step 4 checkpoint | Always checkpoint |
| Merging required-practical and generic-technique into one page | Separate atomic pages; cross-link |
| Duplicating a graph page that already exists as a `representation` | Alias-search (Step 3); link, don't duplicate |
| Double-appending `.state/ingested.tsv` | Append only if a fresh raw was consumed here; else update source page |
| Forgetting to wire MOCs/index/source page | Step 7 |
| Overwriting a differing method/uncertainty treatment | `> ⚠️ Source variation:` block |
| Auto-committing | Leave the diff |

## Red Flags — STOP

- About to paste verbatim procedure text or a full copyrighted worksheet
- About to ship an `experiment-practical` page with no variables or no uncertainty section
- About to write a practical-layer page without having read its `_meta/templates/` template
- About to write before the user answered the Step 4 checkpoint
- About to create a duplicate experiment/technique without alias-searching
- About to double-append `.state/ingested.tsv` for an already-ingested source
- About to overwrite a contradicting method instead of flagging it
- About to present the wiki as the authoritative safety/risk assessment
- About to `Write` under `raw/`, or to `git commit`
