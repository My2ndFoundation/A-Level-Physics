---
name: physics-problem-extract
description: Use when the user wants to turn worked examples or exercises into the problem layer of the A-Level Physics wiki — "extract problems from [[Source]]"、"process these past-paper questions"、"拆题/归类题型"、"build problem types from this paper". Produces problem-type, worked-example, mistake-pattern, and linked method pages.
model: claude-opus-4-7
effort: high
---

# A-Level Physics Problem Extractor

## Overview

Processes a source's exercises/worked examples into the **problem layer**: `problem-type` (`11_Problems/Problem-Types/`), `worked-example` (`11_Problems/Worked-Examples/`), `mistake-pattern` (`11_Problems/Mistake-Patterns/`), plus links to the `method`/`law-result`/`physical-quantity`/`concept`/`model` pages they invoke. Authoritative rules: `CLAUDE.md` §4, §5, §10, §12, `_meta/copyright-rules.md`.

Scope boundary: this skill builds the problem layer from an **already-represented** source. If given a fresh raw file, run `/physics-ingest-source` first (which writes the `13_Sources/` page and `.state/ingested.tsv`); this skill then deepens the problem layer.

## Arguments

```
/physics-problem-extract [[OCR-H556-2022-Paper-1]]    # existing 13_Sources/ page
/physics-problem-extract raw/past-papers/<file>        # will require ingest first
```

If no argument: ask which source/paper. Do not guess.

## The Non-Negotiable Rules

- **Read the templates first** (CLAUDE.md §4): `problem-type-template.md`, `worked-example-template.md`, `mistake-pattern-template.md`, and `method-template.md` for any new method page — before writing any of them.
- **Copyright is critical here** (`_meta/copyright-rules.md`, CLAUDE.md §5.2). Past papers and textbooks are copyrighted: **never copy question text**. Paraphrase the problem; cite exam board / year / paper / question number. Worked solutions must be **original** re-derivations, not reproduced copyrighted solutions or mark-scheme text. No bulk copying of exercise sets.
- **Physics solution quality** (CLAUDE.md §12): worked examples define every symbol, carry units through, do a unit/dimension check, state assumptions and the model used, and state the key insight — not just an answer.
- **Checkpoint before writing** (CLAUDE.md §10): present the extraction plan and wait.
- **Search aliases / existing pages first** (CLAUDE.md §5.3). One problem-type/method = one canonical page; prefer updates over duplicates.
- **Never silently overwrite** — `> ⚠️ Source variation:` block on differing approaches/sign-conventions/methods (CLAUDE.md §5.4).
- **State accounting:** if a fresh raw file was consumed *here* (not via `/physics-ingest-source`), append one 5-field row to `.state/ingested.tsv` with `status: partial` (problem-layer only). Otherwise record coverage on the existing source page's `## Extracted Problem Types`; never double-append.
- **No auto-commit** (CLAUDE.md §5.11).

## Workflow

**Step 1 — Read the source and required templates**
If a raw past-paper path was given and it is not yet in `.state/ingested.tsv`, stop and route to `/physics-ingest-source` first (or get explicit user permission to also do the source-page step here). Then read the problem-type / worked-example / mistake-pattern / method templates.

**Step 2 — Cluster the questions**
Group questions into recurring **problem-types** (by physical signal/skill, not by paper order) — e.g. "interpret a velocity-time graph", "resolve forces on an inclined plane", "find internal resistance from a graph". For each cluster note: required quantities, required concepts, required laws/models, required methods, common traps (→ mistake-patterns), and 1–2 representative questions worth an original **worked-example**.

**Step 3 — Alias-search existing pages**
Grep `.state/aliases.tsv`, `11_Problems/`, `07_Methods/` for each candidate problem-type, mistake-pattern, and method. Plan updates over new pages.

**Step 4 — Checkpoint**
Report: proposed `problem-type` pages (new/update), `worked-example` pages (original solutions, with question refs), `mistake-pattern` pages, `method`/`law-result` links or new method pages, and the copyright handling (what is paraphrased vs. reference-only). **Wait for the user.**

**Step 5 — (gate) Proceed only after confirmation.**

**Step 6 — Write the problem layer**
Use each required template. `problem-type`: signal, required quantities/concepts/laws/methods (wikilinks), standard approach, variations, common traps, example sources (board/year/paper/Q — no text). `worked-example`: paraphrased problem, source reference, original step-by-step solution with symbols defined, unit check, key insight. `mistake-pattern`: per its template, original example, foundation link. Create/link `method` pages as needed. Apply `⚠️` blocks on conflicting approaches.

**Step 7 — Wire the graph**
Cross-link problem-types ↔ methods ↔ laws/quantities ↔ concepts ↔ mistake-patterns. Update `Problem-Solving-MOC`, `Mistake-Patterns-MOC`, and the relevant topic MOC(s) (navigation only). Update `index.md` under Problems. Update the source page's `## Extracted Problem Types` / `## Generated or Updated Pages`.

**Step 8 — State & log**
Per the state rule above (append `.state/ingested.tsv` only if a fresh raw file was consumed here, `status: partial`; else update the source page). Append `## [YYYY-MM-DD] problem-extract | <source>` to `log.md` (Created/Updated/Deferred/Notes incl. `⚠️` flags).

**Step 9 — DO NOT auto-commit** (CLAUDE.md §5.11).

## Edge Cases

| Situation | Handling |
|---|---|
| Raw past-paper not yet ingested | Route to `/physics-ingest-source` first; don't duplicate the source-page pipeline silently. |
| Question text is copyrighted | Paraphrase only; cite board/year/paper/Q number; never paste the text. |
| Mark scheme / official solution available | Use for verification only; write an **original** solution — do not reproduce the mark scheme. |
| Practical / data-analysis question (graph gradient, uncertainty) | Build the `problem-type` and link the relevant `experiment-practical`/`representation` pages; consider `/physics-practical-extract` for the practical itself. |
| Many near-identical questions | One `problem-type` page; cite several question refs; don't make a page per question. |
| A worked example needs a method/law page that doesn't exist | Create the `method` page from its template (or flag at checkpoint). |
| Source's approach contradicts an existing method page (e.g. sign convention) | `> ⚠️ Source variation:` block; never overwrite. |
| Image-based diagram question (circuit, ray diagram) | Describe/paraphrase the setup; do not embed copyrighted figures. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Copying question or mark-scheme text | Paraphrase; original solutions; cite refs only |
| Writing before reading the templates | CLAUDE.md §4 — Step 1 |
| Writing before the Step 4 checkpoint | Always checkpoint |
| Worked example with no unit check / undefined symbols | CLAUDE.md §12 — define symbols, carry units, check dimensions |
| A page per question | Cluster into problem-types; cite multiple refs |
| Duplicate problem-type/method (skipped alias search) | Step 3 mandatory |
| Double-appending `.state/ingested.tsv` | Append only if a fresh raw was consumed here; else update source page |
| Forgetting to wire MOCs/index/source page | Step 7 |
| Overwriting a differing method | `> ⚠️ Source variation:` block |
| Auto-committing | Leave the diff |

## Red Flags — STOP

- About to paste verbatim question text or an official mark scheme
- About to write a problem-layer page without having read its `_meta/templates/` template
- About to write before the user answered the Step 4 checkpoint
- About to create a duplicate problem-type/method without alias-searching
- About to double-append `.state/ingested.tsv` for an already-ingested source
- About to overwrite a contradicting method instead of flagging it
- About to `Write` under `raw/`, or to `git commit`
