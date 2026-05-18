---
name: physics-source-research
description: Use when a page or cluster needs trusted content sources for Physics explanation, foundation, experiment, problem-solving, or frontier orientation in the A-Level Physics project. Returns a source recommendation by page type — never copies long source text.
model: claude-opus-4-7
effort: high
---

# A-Level Physics Source Research

## Overview

Selects trusted sources for a page or cluster. Authoritative pool and per-type
selection rules: `_meta/source-policy.md`. Copyright: `_meta/copyright-rules.md`,
`CLAUDE.md` §5.2 — paraphrase and reference; never reproduce long passages,
chapters, exercise sets, or full copyrighted worked examples.

## The Non-Negotiable Rules

- **Source selection is driven by `_meta/source-policy.md`.** Read it before recommending.
- **Never copy long source text** into any wiki page, the recommendation, or `13_Sources/`.
- **OCR is the syllabus spine.** Alignment, formulae, assessment, practical scope anchor to the local OCR source pages.
- **Frontier sources only feed shallow frontier maps** (`_meta/frontier-rules.md`).
- **No fabricated provenance pages.** Public-pool references are named in `## Source Trace`, not turned into `13_Sources/` pages.

## Workflow

1. Read `_meta/source-policy.md`.
2. Identify the page type(s) in scope (one page, or a cluster's mix of types).
3. For each, apply the "Source Selection by Page Type" table.
4. Pick the best source for each role (definition / intuition / A-Level alignment / practical-graph-experiment / common mistakes / frontier orientation), preferring OCR for syllabus alignment and OpenStax/Physics Classroom/HyperPhysics/IOPSpark for explanation.
5. Return the recommendation block. Do not write wiki pages from this skill.

## Output

```markdown
## Recommended Sources
## Best Source for Definition
## Best Source for Intuition
## Best Source for A-Level Alignment
## Best Source for Practical / Graph / Experiment
## Best Source for Common Mistakes
## Best Source for Frontier Orientation
## Notes on Source Quality
```

## Common Mistakes

| Mistake | Fix |
|---|---|
| Recommending Wikipedia as the sole explanatory source | Wikipedia = navigation only (`_meta/source-policy.md`) |
| Ignoring the OCR spine for A-Level alignment | OCR spec/handbooks anchor syllabus, formulae, assessment |
| Pulling frontier depth into core pages | Frontier sources feed shallow maps only (§3) |
| Pasting source text into the recommendation | Names and roles only — no copied passages |

## Red Flags — STOP

- About to copy a long passage from any source
- About to recommend a source outside the trusted pool without flagging it
- About to create a `13_Sources/` page for a public-pool reference
