---
name: physics-build-base-cluster
description: Use to build a complete usable baseline for one major A-Level Physics cluster — "build the mechanics baseline", "construct the waves cluster", "build base cluster electricity". The main upfront construction skill, authorised by _meta/baseline-build-policy.md to write without per-page checkpoints.
model: claude-opus-4-7
effort: high
---

# A-Level Physics Base Cluster Builder

## Overview

Builds or completes every core page for one Physics cluster to `status: usable`.
This is the main upfront construction skill. Authority: `CLAUDE.md` (esp. §4,
§5, §10, §12), `_meta/baseline-build-policy.md`, `_meta/source-policy.md`.
Per-page completion delegates to `physics-complete-page`'s standard; source
choice to `_meta/source-policy.md` / `physics-source-research`.

## Recognised clusters

```
foundations · common-sense · mathematical-methods · mechanics · motion · forces ·
energy · materials · electricity · circuits · waves · quantum-entry · particles ·
fields · thermal-physics · nuclear-physics · medical-physics · astrophysics ·
practical-skills · frontier-maps · problem-solving-baseline
```

## Authorisation (the key difference from ingest)

`_meta/baseline-build-policy.md` authorises this skill to **write without a
per-page checkpoint** during the approved baseline pass. Stop only for:
copyright risk · destructive overwrite risk · major ambiguity · broken project
structure · unclear source conflict.

## The Non-Negotiable Rules

- **Read each required template before writing pages of that type** (CLAUDE.md §4).
- **Search before create** (§5.3): grep `.state/aliases.tsv` + existing `aliases:`/filenames. Existing seed/draft pages are **completed in place** (preserve content, `⚠️ Source variation` on real differences — §5.4), never recreated.
- **Correct page type + folder + template** (§4 mapping). **Broad topics are MOCs only** (§5.5) — never create `Mechanics.md`, `Waves.md`, `Energy.md` as content pages.
- **Atomic 300–800 words** (§5.6); **frontier shallow** (§3); **frontmatter + wikilinks mandatory** (§5.7, §5.9); **connect intuition/maths/graph/experiment** (§5.10, §12).
- **Sources via `_meta/source-policy.md`**, paraphrase only, no copyrighted text (§5.2).
- **No auto-commit** (§5.11).

## Cross-cluster dedup guard

`Conservation-of-Energy` / `Conservation-of-Momentum` are canonical as
`law-result` (05) — the concepts pass does not make rivals. GCSE-foundation
`Force/Energy/Power/Current/Voltage/Resistance/Waves` (02) and the A-Level
`physical-quantity` pages (03) are intentionally distinct layers (§2),
cross-linked, not duplicates. When dispatching parallel builders, partition by
page-type folder so write targets never overlap; MOC/index/log updates are done
centrally afterward, not by parallel page builders.

## Workflow

1. Read the relevant MOC(s) and existing pages in the matching folders/tags.
2. Identify empty / seed / draft / missing / weak pages; build the cluster page list (use the required-baseline list in the build brief / `CLAUDE.md`-aligned scope).
3. **Read the required templates** for every type in the list.
4. Pick sources (`_meta/source-policy.md`; `/physics-source-research` for the cluster mix).
5. Create missing pages and complete existing seed/draft pages to the `physics-complete-page` usable bar — correct template, real paraphrased physics, wikilinks, source trace, `status: usable` (hub pages may be `reviewed`).
6. (central, not per page builder) update related MOCs via `physics-build-moc`; update `index.md`; append `log.md`; update `.state/unresolved-links.md`.
7. Run a local lint pass for the cluster (`physics-lint-wiki` scope = the folder).
8. Write the Cluster Build Report.

## Minimum cluster completeness

Foundation/common-sense links where relevant · core physical quantities ·
core concepts · laws/results · models · methods · representations ·
experiments/practicals where relevant · applications · mistake patterns ·
problem types · frontier links where relevant. Not every cluster needs every
type, but a missing obvious type must be recorded in the report.

## Cluster output

```markdown
## Cluster Build Report
- Cluster:
- Pages created:
- Pages updated:
- Pages moved:
- MOCs updated:
- Status changes:
- Source traces added:
- Deferred:
- Warnings:
```

## Common Mistakes

| Mistake | Fix |
|---|---|
| Recreating an existing seed page | Complete in place; preserve + `⚠️` on differences |
| Writing before reading the template | §4 — read `_meta/templates/<type>-template.md` first |
| Creating `Mechanics.md`/`Waves.md` as content | Broad topics are MOCs (§5.5) |
| Parallel builders editing MOC/index/log | Page builders touch atomic pages only; central MOC/index/log pass |
| Duplicate `Conservation-of-*` concept vs law | Canonical = law-result (05) |
| Frontier cluster pages going deep | §3 — shallow orientation only |
| Stopping for a per-page checkpoint | Baseline pass is pre-authorised; stop only for the 5 hard reasons |
| Leaving pages `status: seed` | Set `usable` when the bar is met |

## Red Flags — STOP

- About to Write a page-type without having read its template
- About to recreate/overwrite an existing seed page instead of completing it
- About to create a broad-topic content page
- About to paste copyrighted text
- About to deepen a frontier page past orientation
- About to `git commit`
