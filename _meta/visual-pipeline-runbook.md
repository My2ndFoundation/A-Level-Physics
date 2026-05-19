# Visual Pipeline Runbook

Authority: obeys CLAUDE.md (esp. §4 templates, §5.1 raw read-only, §5.2 no
copyrighted reproduction, §5.4 no silent overwrite, §5.11 no auto-commit).
Spec: docs/superpowers/specs/2026-05-18-vault-visuals-pipeline-design.md

## 1. Per-page classification

Read the page. Decide ONE outcome:

- **Diagram** — relationship/structure/graph cleaner authored than photographed
  (graphs, free-body, circuits, ray, field lines, energy/decay chains).
- **Photo** — real apparatus, instrument, phenomenon, or technology.
- **Both** — needs an explanatory diagram AND a real-world photo.
- **None** — visual adds no understanding. Ambiguous → choose None.

Page types that normally get a visual: physical-quantity, concept, law-result,
model, representation, experiment-practical, application, frontier-map,
foundation, common-sense. method/problem-type/worked-example/mistake-pattern/
source/moc → default None unless exceptionally warranted.

## 2. Diagrams

- Mermaid (native Obsidian) for relationship/flow/chain and simple
  `xychart-beta` graphs — embed as a fenced ```mermaid block inside `## Visuals`.
- Hand-authored inline SVG saved to `_attachments/<NN_Folder>/<slug>--<desc>.svg`
  for free-body/ray/circuit/field-line/vector diagrams; embed via
  `![[_attachments/<NN_Folder>/<slug>--<desc>.svg]]`.
- Validate every diagram against the page's own equations/definitions. Invent
  no numeric values. If unvalidatable → skip, log `diagram needs human`.
- Source line for authored diagrams:
  `*Source: Authored for this vault (CC0). No external copyright.*`

## 3. Photo sourcing — authoritative APIs only, in order

1. Wikimedia Commons:
   `https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrsearch=<query>&gsrlimit=10&prop=imageinfo&iiprop=url|extmetadata`
2. NASA Images: `https://images-api.nasa.gov/search?q=<query>&media_type=image`
   (NASA media = public domain). Use for astro/space/cosmology.
3. CERN CDS / ESA — particle/space only, per-item license read.

No general web image scraping. Stop at first license-passing, relevant hit.

## 4. License-verification gate (HARD, non-bypassable)

From Commons `imageinfo[].extmetadata`, read `LicenseShortName.value`,
`Artist.value`, `Credit.value`, canonical `descriptionurl`.

ALLOW if license short-name matches (case-insensitive) any of:
`public domain`, `pd`, `cc0`, `nasa`, `us government`, OR any `cc by` /
`cc by-sa` of ANY version (2.0, 2.5, 3.0, 4.0, …) — i.e. license short-name
contains `cc by` and does NOT contain a reject token below.

REJECT (do not download, log reason) if it contains `nc`, `nd`,
`noncommercial`, `no derivatives`, `gfdl` (without an accompanying CC allow
match), `fair use`, `non-free`, OR if license/author is empty/unknown.

NASA Images API results: treat as `Public Domain` with author = NASA unless the
item explicitly states otherwise (then run it through the same gate).

## 5. Download + caption

On ALLOW: download the file to
`_attachments/<NN_Folder>/<page-slug>--<descriptor>.<ext>` (ext from URL).
After download, if it is a raster image (jpg/jpeg/png) whose longest edge
exceeds 1600px, downscale it in place to a 1600px longest edge:
`sips -Z 1600 "<path>"` (macOS-native; preserves aspect ratio). SVGs and
images already ≤1600px are left untouched. Log the original→final dimensions
in the manifest `note` column when a downscale occurred.
Embed in `## Visuals`:

```
### <short title>
![[_attachments/<NN_Folder>/<page-slug>--<descriptor>.<ext>]]
*Figure: <what to look at>.*
*Source: <Title> — <Author> — <License> — <canonical URL>. Retrieved <YYYY-MM-DD>.*
```

## 6. Page edit rules

- Edit ONLY the `## Visuals` section (insert/replace it; it sits directly
  before `## Source Trace`). Preserve all other content and frontmatter
  verbatim (§5.4).
- If `## Visuals` already contains a valid embedded image/diagram → SKIP page
  (idempotent), log `skip: already has visual`.
- If the page has no `## Visuals` heading yet (older page predating the
  template change) → insert the section immediately before `## Source Trace`.
  If there is no `## Source Trace` either → append `## Visuals` at end.
- Deterministic filenames make re-runs safe; never create a second file for
  the same (page, descriptor).

## 7. Error handling

| Failure | Action |
|---|---|
| API down/timeout | retry once → fall back to diagram → else log `photo deferred` |
| No license-clean candidate | diagram if feasible → else log `no compliant visual` |
| License unverifiable/empty | reject, never embed, log reason |
| Diagram unvalidatable | skip, log `diagram needs human` |
| Page type ambiguous | outcome = None |

A failure never breaks a page; worst case the page gets no visual.

## 8. Subagent return manifest (one TSV line per page)

`<relpath>\t<outcome>\t<file-or-mermaid-or->\t<license-or-CC0-or->\t<source-url-or->\t<YYYY-MM-DD>\t<note>`

outcome ∈ {diagram, photo, both, none, skip, deferred, needs-human}
