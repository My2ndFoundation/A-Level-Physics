---
name: physics-build-moc
description: Use when the user wants to rebuild or improve a Map of Content in the A-Level Physics project — "rebuild [[Mechanics-MOC]]"、"update the MOCs"、"重建 MOC"、"refresh the Waves map". Reorganises MOC navigation links from existing pages and tags without duplicating content.
model: claude-sonnet-4-6
effort: medium
---

# A-Level Physics MOC Builder

## Overview

Rebuilds or improves one (or several) MOC in `01_MOCs/` or `00_Home/` from the existing graph — member pages, tags, and wikilinks. Authoritative rules: `_meta/workflows/moc-update-workflow.md`, `_meta/templates/moc-template.md`, `CLAUDE.md` §5.8.

> **Baseline build note.** During the baseline construction pass
> (`_meta/baseline-build-policy.md`), MOC/index/log updates are run **centrally**
> here after the atomic page builders finish, so parallel page builders never
> write MOCs concurrently. The `all` scope is pre-authorised for that pass.

## Arguments

```
/physics-build-moc [[Mechanics-MOC]]
/physics-build-moc Waves              # resolves to Waves-MOC
/physics-build-moc all                # every MOC (confirm scope first)
```

If no argument: ask which MOC. Never create a broad-topic *content* page — the answer is always a MOC (CLAUDE.md §5.5).

## The Non-Negotiable Rules

- **MOCs are navigation only** (CLAUDE.md §5.8). Links and short headings — no explanations, no content duplicated from atomic pages.
- **Preserve existing user edits and ordering** (`_meta/workflows/moc-update-workflow.md`). Add under the correct heading; do not reorder or remove entries unnecessarily.
- **Follow `_meta/templates/moc-template.md`** structure when creating a new MOC (CLAUDE.md §4). Section order: Foundations / Common-Sense Links / Physical Quantities / Concepts / Laws and Results / Models / Methods / Representations / Experiments and Practicals / Applications / Problem Types / Common Mistake Patterns / Frontier Links / Sources.
- **Canonical wikilinks** — link by canonical filename (no `.md`), per `.state/aliases.tsv`.
- **No content fabrication.** A MOC only links pages that exist; planned-but-absent objects go to `.state/unresolved-links.md`, not into the MOC as dead prose.
- **Frontier MOCs stay shallow and explicitly peripheral** (CLAUDE.md §3, `_meta/workflows/moc-update-workflow.md`). `Frontier-Physics-MOC` keeps its "intentionally shallow / orientation, not mastery" framing.
- **Checkpoint before destructive/bulk changes** (large reorganisation, `all`).
- **No auto-commit** (CLAUDE.md §5.11).

## Workflow

**Step 1 — Read the MOC and the moc-template**
Note its topic, existing headings, existing entries, and any user-authored ordering or notes to preserve (including the Frontier-Physics-MOC shallow-orientation banner).

**Step 2 — Discover member pages**
Find pages that belong to this MOC's topic by: matching syllabus/topic/learning-layer tags (`_meta/tags.md`), inbound/related wikilinks from existing members, and folder/type. Map each to the right MOC heading (Foundations / Common-Sense Links / Physical Quantities / Concepts / Laws and Results / Models / Methods / Representations / Experiments and Practicals / Applications / Problem Types / Common Mistake Patterns / Frontier Links / Sources).

**Step 3 — Diff**
Compute: pages that belong but are missing from the MOC; entries in the MOC whose target no longer resolves (broken/renamed); pages mis-filed under the wrong heading.

**Step 4 — Checkpoint (for non-trivial or `all` scope)**
Report proposed additions per heading, broken links to remove/repair, and what user content is being preserved. **Wait for the user.** (Trivial single-page additions to one MOC may proceed without a full checkpoint if the user invoked the skill for exactly that.)

**Step 5 — Apply**
Insert links under the correct headings using canonical names. Keep existing entries and their order; append rather than reshuffle. Repair broken links to the renamed canonical page (or remove only if the target is genuinely gone and the user agreed). No explanatory prose.

**Step 6 — Append `log.md`**
`## [YYYY-MM-DD] moc | <MOC name(s)>` with Created/Updated/Deferred/Notes.

**Step 7 — DO NOT auto-commit** (CLAUDE.md §5.11).

## Edge Cases

| Situation | Handling |
|---|---|
| MOC does not exist yet | Create it from `moc-template.md` with correct frontmatter (`type: moc`) and topic/layer tags; populate from the graph. |
| Writing the `tags:` block | Emit one `-` item per tag (`_meta/tags.md` frontmatter format rule). Never collapse multiple tags into one item or put spaces inside a tag — Obsidian rejects it as an invalid tag name. |
| A page fits two MOCs (e.g. a page in both `Forces-MOC` and `Mechanics-MOC`) | Listing it in both is allowed when genuinely relevant. |
| Broken entry: target was renamed | Repoint to the new canonical name (check `.state/aliases.tsv`); don't just delete. |
| Member object referenced but no page exists | Add to `.state/unresolved-links.md`; do not put a dead bullet in the MOC. |
| Building a frontier MOC | Keep it a shallow link map; preserve the orientation banner; do not add explanatory physics. |
| Foundation/bridge pages belong to a topic MOC | List them under `## Foundations` of that MOC — the layer model wants prerequisites visible (CLAUDE.md §2). |
| User added custom prose/section to the MOC | Preserve it; integrate links around it. |
| `all` scope | Confirm explicitly; process MOC by MOC; one breadcrumb line each. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Writing explanations/definitions into the MOC | Navigation only — links + headings |
| Reordering or wiping existing entries | Preserve order; append under headings |
| Adding physics depth to a frontier MOC | Keep shallow + orientation banner (CLAUDE.md §3) |
| Linking non-existent pages as dead bullets | Route to `.state/unresolved-links.md` |
| Using non-canonical link text / aliases as targets | Link by canonical filename |
| Creating `Mechanics.md` instead of `Mechanics-MOC.md` | Broad topics are MOCs (CLAUDE.md §5.5) |
| Skipping the checkpoint on a bulk rebuild | Checkpoint for non-trivial / `all` |
| Auto-committing | Leave the diff |

## Red Flags — STOP

- About to add explanatory content (not just links) to a MOC
- About to delete/reorder existing MOC entries without user consent
- About to add physics depth to a frontier MOC instead of keeping it a shallow map
- About to link pages that don't exist instead of logging them as unresolved
- About to bulk-rebuild `all` without confirming scope
- About to `Write` under `raw/`, or to `git commit`
