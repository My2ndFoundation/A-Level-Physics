---
name: physics-complete-page
description: Use to turn one seed/draft A-Level Physics page into a usable page following its required template — "complete [[Page]]", "make this page usable", "fill out [[...]]". Reads the page, reads its template, applies the source policy, completes it without silent overwrite.
model: claude-opus-4-7
effort: high
---

# A-Level Physics Page Completer

## Overview

Takes one existing seed/draft page (or creates one missing baseline page) and
brings it to `status: usable`, strictly following its `_meta/templates/` template.
Authority: `CLAUDE.md` §4 (template rule), §5 (non-negotiables), §12 (quality),
`_meta/source-policy.md`, `_meta/baseline-build-policy.md`.

## The Non-Negotiable Rules

- **Read the required template before writing** (CLAUDE.md §4). The `type:` in frontmatter selects the template. Template structure wins over any lower instruction.
- **Preserve existing useful content. Never silent-overwrite** (CLAUDE.md §5.4). On a genuine difference use the `> ⚠️ Source variation:` block.
- **Search before create** (CLAUDE.md §5.3) — grep `.state/aliases.tsv` + `aliases:` so you complete the canonical page, not a duplicate.
- **Source selection via `_meta/source-policy.md`.** Paraphrase only; no copyrighted text (§5.2).
- **Mandatory frontmatter + wikilinks** (§5.7, §5.9). Canonical filenames as link targets.
- **Atomic size 300–800 words** (§5.6); frontier pages shallow (§3).
- **Connect intuition · meaning · maths · graph · experiment · assumptions · traps** (§5.10, §12).
- **No auto-commit** (§5.11).

## Workflow

1. Read the existing page (or, if missing, note it as a new baseline page).
2. Determine `type:` from frontmatter (or from the required-baseline list / target folder).
3. **Read the matching template from `_meta/templates/`** (mapping table in CLAUDE.md §4).
4. Pick sources via `_meta/source-policy.md` (use `/physics-source-research` if a cluster).
5. Write/complete the page: every template section filled with real, paraphrased physics; define every symbol + unit + condition; explain gradient/area/intercepts for graphs; identify variables + uncertainty for experiments; keep frontier shallow.
6. Add meaningful wikilinks (foundations, quantities, laws, models, methods, representations, experiments, applications, mistakes, frontier) by canonical filename.
7. Fill `## Source Trace` per the `_meta/source-policy.md` convention (name public sources; anchor `OCR alignment: [[OCR-Physics-A-H556-Specification]]`).
8. Set frontmatter: real `tags` (from `_meta/tags.md`), `level`, `aliases`, and `status: usable` once the baseline-usable bar is met (hub pages may be `reviewed`).
9. Record any mentioned-but-missing target in `.state/unresolved-links.md`.

## Baseline definition of "usable"

Explains the idea clearly · has all required template sections · meaningful
wikilinks · source trace · common mistakes where relevant · foundation links
where relevant · links to representations/methods/experiments/applications where
relevant · no copyrighted text · suitable for a student about to begin A-Level.

## Per-type required content

Follow each template's section list exactly. Minimum substance per type:

- **physical-quantity**: core idea, symbol, SI unit, scalar/vector, definition, related equations, how measured, graph meaning, foundation links, related laws, common mistakes, source trace.
- **concept**: core idea, everyday intuition, GCSE foundation, A-Level meaning, related quantities/laws/models/representations/experiments/applications, frontier links if relevant, common mistakes, source trace.
- **law-result**: statement, equation, symbols+units, conditions, physical meaning, foundation link, how to use, related models, applications, common mistakes, source trace.
- **model**: core idea, assumptions, quantities, key equations, when to use, limits, foundation link, related methods, applications, common mistakes, source trace.
- **method**: purpose, when to use, prerequisites, steps, short original worked example or pointer, why it works, common mistakes, related quantities/laws/problem types, source trace.
- **representation**: form, axes/components, physical meaning, gradient/area/intercepts, related quantities/methods, common mistakes, source trace.
- **experiment-practical**: aim, variables (IV/DV/control), apparatus, method, measurements, data processing, graph use, uncertainty, practical limits, related quantities/laws, common mistakes, source trace.
- **application**: context, physical ideas, mathematical tools, typical questions, method outline, assumptions, cross-subject links, common mistakes, source trace.
- **common-sense**: everyday question, short answer, physical explanation, what it builds toward, related A-Level ideas, common wrong intuition, boundary, source trace.
- **foundation**: prior-knowledge level, meaning, why it matters for A-Level, everyday intuition, key quantities, related concepts/laws, misconceptions, bridge to A-Level, source trace.
- **frontier-map**: what the field studies, why it matters, A-Level entry points, key edge ideas, what not to worry about yet, related frontier maps, related A-Level pages, source trace. **Shallow only — no university derivations.**

## Common Mistakes

| Mistake | Fix |
|---|---|
| Writing before reading the template | §4 — read `_meta/templates/<type>-template.md` first |
| Overwriting existing seed content | Preserve + `⚠️ Source variation` on real differences |
| Formula-only page | §5.10/§12 — connect intuition, maths, graph, experiment, traps |
| Frontier page too deep | §3 — orientation, not mastery |
| Leaving `status: seed` after completion | Set `usable` when the bar is met |
| Duplicate of an aliased page | §5.3 — alias-search first |

## Red Flags — STOP

- About to Write/Edit without having read the page's template
- About to overwrite a contradicting claim instead of using the `⚠️` block
- About to paste copyrighted text
- About to deepen a frontier page past orientation
- About to `git commit`
