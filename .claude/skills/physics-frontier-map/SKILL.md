---
name: physics-frontier-map
description: Use when the user wants to create or update a shallow frontier/edge map in the A-Level Physics project — "make a frontier map for [[Relativity]]"、"update [[Quantum-Mechanics-Map]]"、"where does this lead beyond A-Level"、"画一张前沿地图". Builds orientation-only maps that connect A-Level ideas to modern Physics without university-level depth.
model: claude-opus-4-7
effort: medium
---

# A-Level Physics Frontier Mapper

## Overview

Creates or updates a `frontier-map` page in `12_Frontier-Maps/` that shows where A-Level ideas lead beyond the syllabus. Authoritative rules: `CLAUDE.md` §3 (Frontier Boundary Rule), `_meta/frontier-rules.md`, `_meta/templates/frontier-map-template.md`.

**The whole point of this skill is depth discipline.** A frontier map is orientation, not mastery; a map, not a textbook; curiosity, not syllabus burden. If a page starts teaching the field, it has failed.

## Arguments

```
/physics-frontier-map [[Quantum-Mechanics-Map]]
/physics-frontier-map Relativity            # resolves to Relativity-Map
/physics-frontier-map "Semiconductor Physics"
```

If no argument: ask which field. The filename is always `...-Map.md` (CLAUDE.md §9). Never create a deep `04_Concepts/`/`05_Laws-and-Results/` page for beyond-A-Level material under the guise of a map.

## The Non-Negotiable Rules — Depth First

- **Read `_meta/frontier-rules.md` and the frontier-map template before writing** (CLAUDE.md §4). The page must contain exactly these sections: What This Field Studies / Why It Matters / A-Level Entry Points / Key Ideas at the Edge / What Not to Worry About Yet / Useful Analogies (optional) / Related Frontier Maps / Related A-Level Pages / Source Trace.
- **Forbidden content** (CLAUDE.md §3, `_meta/frontier-rules.md`): advanced derivations; dense university-level mathematical formalism; long technical explanations; full quantum mechanics / relativity / particle physics / cosmology; speculative claims presented as settled fact; rabbit holes that distract from A-Level core.
- **Required framing:** every map must explicitly state its A-Level entry points (as `[[wikilinks]]` to real A-Level pages) **and** an explicit "What Not to Worry About Yet" section. A map without these two is not shippable.
- **Connect back, don't lead away.** Each map links to existing A-Level pages; if an A-Level entry point has no page yet, add it to `.state/unresolved-links.md` — do not invent the A-Level page here (that's `/physics-ingest-source`).
- **Length:** a map may be slightly longer than a normal atomic page but stays shallow (CLAUDE.md §5.6). If it is growing into a lesson, cut depth — do not split into more maps.
- **Provenance.** Factual claims should trace to an approved `13_Sources/` page (typically under `13_Sources/Frontier-References/`) or be flagged as general orientation knowledge at the checkpoint. Do not fabricate a source trace.
- **Checkpoint before writing** (CLAUDE.md §10 spirit): present the outline and wait.
- **No auto-commit** (CLAUDE.md §5.11).

## Workflow

**Step 1 — Read the rules, the template, and (if updating) the existing map**
Read `_meta/frontier-rules.md`, `_meta/templates/frontier-map-template.md`, and the target map if it exists. Note existing A-Level entry points and any user-written framing to preserve.

**Step 2 — Identify A-Level anchor pages**
Find the real A-Level pages this field connects to (e.g. for quantum: `[[Photoelectric-Effect]]`, photons, wave-particle duality). These become the "A-Level Entry Points". Anchors that have no page → `.state/unresolved-links.md`.

**Step 3 — Draft the outline (shallow)**
For each template section, write one to a few sentences max. "Key Ideas at the Edge" is a *named list*, not explanations. "What Not to Worry About Yet" explicitly names the advanced machinery to skip (e.g. Schrödinger equation, Hilbert spaces, tensor calculus).

**Step 4 — Checkpoint**
Report: the section outline, the A-Level entry-point wikilinks (existing vs unresolved), related frontier maps to cross-link, the source(s) backing any factual claims (or a general-knowledge flag), and a one-line self-check that nothing exceeds orientation depth. **Wait for the user.**

**Step 5 — (gate) Proceed only after confirmation.**

**Step 6 — Write / update the map**
Use the frontier-map template exactly. Frontmatter: `type: frontier-map`, `level: edge-map`, tags include `frontier`, `edge-map`, `modern-physics` and the topic. Preserve any user prose. Keep every section shallow. Add `[[...]]` to A-Level pages and related maps. Fill `## Source Trace`.

**Step 7 — Wire the graph**
Add the map to `Frontier-Physics-MOC` (and `Modern-Physics-MOC` / topic MOC where relevant) under `## Frontier Maps` — navigation only, preserving the MOC's shallow-orientation banner. Add reciprocal `## Frontier Links` bullets on the linked A-Level pages **only if** the link is genuinely useful and does not bloat them. Update `index.md` under `## Frontier Maps`.

**Step 8 — Append `log.md`**
`## [YYYY-MM-DD] frontier-map | <map>` with Created/Updated/Deferred/Notes (note unresolved A-Level anchors).

**Step 9 — DO NOT auto-commit** (CLAUDE.md §5.11).

## Edge Cases

| Situation | Handling |
|---|---|
| User asks for derivations / "explain it properly" | Decline within this skill — that violates §3. Offer: keep the map shallow and, if a part is genuinely A-Level, route to `/physics-ingest-source` for a proper A-Level page. |
| A-Level entry point has no page yet | Link it anyway as the intended canonical name and log it in `.state/unresolved-links.md`; do not create the A-Level page here. |
| Map is getting long / lesson-like | Cut depth, not scope. A longer map is fine; a *deep* one is not. |
| Two overlapping fields (quantum vs particle physics) | Separate maps, cross-linked under `## Related Frontier Maps`; don't merge into a mega-map. |
| Source contradicts another map | `> ⚠️ Source variation:` block; never overwrite. |
| User wants a frontier map for a core A-Level topic | That's not a frontier map — it's an A-Level page; route to `/physics-ingest-source`/`/physics-expand-concept`. |
| Speculative / unsettled science (interpretations of QM, quantum gravity) | Present as open questions, explicitly labelled; never as settled fact. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Adding derivations or university maths | §3 forbids it — orientation only |
| "Key Ideas" written as explanations | Make it a named list, not a lesson |
| Missing "What Not to Worry About Yet" | Required section — name the skipped machinery |
| No A-Level entry-point wikilinks | Required — connect back to real A-Level pages |
| Inventing the missing A-Level page here | Log to `.state/unresolved-links.md`; route to ingest |
| Bloating linked A-Level pages with frontier prose | One concise `## Frontier Links` bullet, only if useful |
| Fabricating a source trace | Use a `13_Sources/` page or flag as general knowledge |
| Writing before the Step 4 checkpoint | Always checkpoint |
| Auto-committing | Leave the diff |

## Red Flags — STOP

- About to write a derivation, proof, or dense formalism into a `frontier-map`
- About to write a map with no A-Level entry points or no "What Not to Worry About Yet"
- About to create a deep beyond-A-Level content page instead of a shallow map
- About to invent an A-Level page instead of logging it unresolved
- About to present a speculative interpretation as settled fact
- About to write before the user answered the Step 4 checkpoint
- About to `Write` under `raw/`, or to `git commit`

All of these mean: **stop and re-read `CLAUDE.md` §3 and `_meta/frontier-rules.md`. Orientation, not mastery.**
