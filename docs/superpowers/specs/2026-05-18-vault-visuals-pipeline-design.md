# Vault Visuals Pipeline — Design Spec

- **Date:** 2026-05-18
- **Project:** A-Level Physics knowledge vault
- **Goal:** Add visuals (authored diagrams + openly-licensed real photos) to wiki
  pages in folders `03_*` through `12_*`, sourced only from authoritative,
  license-verifiable origins, fully autonomously, without violating CLAUDE.md.

---

## 1. Scope

- **In scope:** pages under `03_Physical-Quantities`, `04_Concepts`,
  `05_Laws-and-Results`, `06_Models`, `07_Methods`, `08_Representations`,
  `09_Experiments-and-Practicals`, `10_Applications`, `11_Problems`,
  `12_Frontier-Maps` (~320 pages at design time).
- **Out of scope:** `00_Home`, `01_MOCs`, `02_Foundations`, `13_Sources`,
  `_meta`, `raw/`. (`raw/` is read-only per §5.1.)
- **Coverage policy:** value-driven. A page gets a visual only where it
  genuinely aids understanding. Low-value pages (many method, problem-type,
  worked-example, mistake-pattern, source, moc) are intentionally skipped.

## 2. Locked decisions

| Decision | Choice |
|---|---|
| Visual type | Hybrid: authored diagrams + openly-licensed real photos |
| Photo storage | Local download into `_attachments/`, source URL + license + author kept in caption |
| Template governance | Amend `_meta/templates/*.md` to add a standardised `## Visuals` section |
| Coverage | Value-driven only (skip low-value pages) |
| Execution | Fully autonomous batch, single final report |
| License allowlist | Public Domain, CC0, CC BY, CC BY-SA, NASA-PD, US-Gov-PD |
| License rejected | CC BY-NC, CC BY-ND, GFDL-only, fair-use, non-free, **unknown/empty** |

## 3. Governance & structure

### 3.1 Template amendment

Add a `## Visuals` section **immediately before `## Source Trace`** in these
templates (types that benefit from visuals):

`physical-quantity`, `concept`, `law-result`, `model`, `representation`,
`experiment-practical`, `application`, `frontier-map`, `foundation`,
`common-sense`.

Do **not** add the section to: `method`, `problem-type`, `worked-example`,
`mistake-pattern`, `source`, `moc`. A page of these types may still receive a
visual in exceptional cases, but the section is not mandatory there.

Section body to insert:

```markdown
## Visuals

<!-- Each entry: an authored diagram (Mermaid/SVG) OR an openly-licensed image.
     Every image MUST carry: caption, license, author, source URL. -->

### [Diagram/Photo title]
![[_attachments/<file>]]
*Figure: <one-line caption explaining what to look at>.*
*Source: <Title> — <Author> — <License> — <canonical URL>. Retrieved <date>.*
```

Authored-diagram source line:
`*Source: Authored for this vault (CC0). No external copyright.*`

Templates are amended **once, by the driver, before any subagent runs**, so all
subagents target identical structure. This keeps CLAUDE.md §4 intact (templates
remain the highest authority and now legitimately include the section).

### 3.2 Attachments structure

New top-level `_attachments/`, mirrored by folder number:

```
_attachments/03_Physical-Quantities/<page-slug>--<descriptor>.svg|png|jpg
_attachments/04_Concepts/...
...
```

- Deterministic filenames (`<page-slug>--<descriptor>.<ext>`) → idempotent
  re-runs, no duplicate images.
- Prefer SVG (authored diagrams) and PNG; JPG allowed for photos.
- Longest edge ≤ 1600px for raster images.
- Files are committed to git (local-download decision). No `git commit` is run
  by this workflow (§5.11) — working tree left dirty for human review.

### 3.3 Caption & provenance backbone

Every embedded **photo** must record in its caption block: title,
author/creator, license short-name, canonical source URL, retrieval date. A
photo with missing or unverifiable author or license is **never embedded**;
it is logged as `skipped: license unverifiable`.

## 4. The visual pipeline

### 4.1 Per-page classification

Classify each page into one outcome:

| Outcome | When | Example |
|---|---|---|
| Diagram | Relationship/structure/graph cleaner authored than photographed | `Velocity-Time-Graph`, `Ohms-Law` |
| Photo | Real apparatus, instrument, phenomenon, technology | `Using-a-Micrometer`, `Medical-Imaging` |
| Both | Needs explanatory diagram *and* real-world photo | `Photoelectric-Effect`, `Diffraction` |
| None | Visual adds no understanding | abstract method/problem pages |

Ambiguous page type → default to **None** (do not force a weak visual).

### 4.2 Diagram authoring strategy

- **Mermaid** (native Obsidian render) for relationship maps, flow/process,
  energy chains, decay chains, and simple graphs (`xychart-beta`).
- **Hand-authored inline SVG** (saved `.svg` in `_attachments/`) for free-body,
  ray, circuit, field-line, and vector-resolution diagrams Mermaid cannot
  express.
- Every authored diagram is physics-checked against the page's own
  equations/definitions before embedding. No invented values. If it cannot be
  validated, skip and log `diagram needs human` rather than embed a wrong
  figure.

### 4.3 Photo sourcing — authoritative APIs only

Query order; stop at first license-passing hit with good relevance:

1. **Wikimedia Commons API** — `commons.wikimedia.org/w/api.php`,
   `prop=imageinfo&iiprop=url|extmetadata`; read `LicenseShortName`, `Artist`,
   `Credit`, `UsageTerms`. Primary source.
2. **NASA Images API** — `images-api.nasa.gov`; NASA media is public domain.
   Use for astro/space/cosmology.
3. **CERN CDS / ESA** — secondary, particle/space only, per-item license read.

No general web image scraping. If 1–3 yield nothing license-clean → fall back
to a diagram (if feasible) or log `no compliant photo found`.

### 4.4 License-verification gate (hard, non-bypassable)

Embed an image **only if** machine-read license ∈ allowlist (§2).

- Pass → download, capture author + license + canonical URL + retrieval date
  into caption.
- Reject (incl. unknown/empty, NC, ND) → do not download, log reason, fall
  back to diagram or skip.

This gate is what makes "fully autonomous" safe under CLAUDE.md §5.2.

## 5. Execution architecture (autonomous)

1. Driver amends the relevant `_meta/templates/*.md` once (§3.1).
2. Driver processes folders in order `03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 →
   11 → 12`.
3. Folders handled by **per-folder subagents in parallel batches** (3–4
   concurrent). Each subagent receives:
   - the amended template(s) for the page types in its folder (MUST read them
     — §4 / CLAUDE.md §4),
   - the visual pipeline rules (classification → diagram/photo → license gate →
     caption),
   - its folder's page list.
4. Each subagent returns a structured manifest: per page → outcome, file(s),
   license, source URL, or skip reason.
5. Driver aggregates and performs vault-wide bookkeeping (§6), then emits the
   final report (§7).

### 5.1 Idempotency & non-destruction

- Deterministic filenames + "skip if page already has a non-empty `## Visuals`
  section with a valid image" → safe re-runs, no duplicates.
- Pages are **edited, not rewritten**: only the `## Visuals` section is
  inserted/updated; all other content and frontmatter preserved (CLAUDE.md
  §5.4 — never silently overwrite).
- `raw/` untouched (§5.1). No `git commit` (§5.11).

## 6. Bookkeeping

- Append `log.md` with a dated batch entry (folders processed, counts).
- Append a visual-manifest TSV under `.state/` (page, outcome, file, license,
  source URL, date) for provenance and future lint.
- Update affected `source` pages' provenance where an image came from a source
  already tracked; image-only origins get a short `source` record per the
  source template.

## 7. Error handling & final report

### 7.1 Error handling

| Failure | Behaviour |
|---|---|
| API down / timeout | Retry once → fall back to diagram → else log `photo deferred` |
| No license-clean candidate | Fall back to diagram if feasible → else log `no compliant visual` |
| License unverifiable/empty | Reject, never embed, log reason |
| Diagram unvalidatable vs page physics | Skip, log `diagram needs human` |
| Page type ambiguous | Default to `None` |

A failure never breaks a page: worst case the page is left without a visual.

### 7.2 Final report

Total pages scanned; visuals added (diagrams vs photos); skipped-with-reasons;
license breakdown; list of `deferred / needs-human` pages; files touched.
Nothing committed — working tree left dirty for review.

## 8. Out of scope (YAGNI)

- No general web image scraping.
- No relaxing the license gate for NC/ND content.
- No automatic git commit.
- No new lint rule implementation now (the manifest enables one later).
- No reusable skill packaging in this pass (one-off spec→plan→execute; can be
  promoted to a `physics-*` skill afterwards if it proves out).
