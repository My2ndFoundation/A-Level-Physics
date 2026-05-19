# Vault Visuals Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add value-driven visuals (authored diagrams + license-verified openly-licensed photos) to wiki pages in `03_*`–`12_*`, fully autonomously, without violating CLAUDE.md.

**Architecture:** A driver amends templates and writes an operational runbook, smoke-validates the pipeline on one page, then dispatches per-folder subagents in parallel batches that classify pages, author diagrams or fetch+license-gate photos, and edit only the `## Visuals` section. The driver aggregates a manifest and emits a final report.

**Tech Stack:** Markdown/Obsidian wiki, Mermaid + hand-authored SVG, Wikimedia Commons API, NASA Images API, CERN CDS/ESA; Bash + curl + jq for API/license queries.

**Project rule deviations (CLAUDE.md overrides the skill defaults):**
- **No git commits** (§5.11). Every "Commit" step is replaced by "verify + leave working tree dirty for human review".
- **No pytest/TDD.** This is a content vault. "Failing test → implement → passing test" is realised as **verification commands** (grep/jq/file checks) with expected output, run before and after each change.

---

## File Structure

| Path | Responsibility |
|---|---|
| `_meta/templates/{physical-quantity,concept,law-result,model,representation,experiment-practical,application,frontier-map,foundation,common-sense}-template.md` | Gain a standardised `## Visuals` section before `## Source Trace` |
| `_meta/visual-pipeline-runbook.md` | Single source of truth the driver + subagents obey: classification, API queries, license gate, caption format, idempotency, error handling |
| `_attachments/<NN_Folder>/` | Downloaded photos + authored `.svg` diagrams, deterministic filenames |
| `_attachments/.gitkeep` | Keeps the empty tree in git |
| `.state/visual-manifest.tsv` | Per-page provenance: page, outcome, file, license, source URL, date |
| `log.md` | Dated batch entry appended at the end |
| Pages under `03_*`–`12_*` | Only their `## Visuals` section is inserted/updated; nothing else touched |

---

## Task 1: Amend the 10 templates with a `## Visuals` section

**Files:**
- Modify: `_meta/templates/physical-quantity-template.md`
- Modify: `_meta/templates/concept-template.md`
- Modify: `_meta/templates/law-result-template.md`
- Modify: `_meta/templates/model-template.md`
- Modify: `_meta/templates/representation-template.md`
- Modify: `_meta/templates/experiment-practical-template.md`
- Modify: `_meta/templates/application-template.md`
- Modify: `_meta/templates/frontier-map-template.md`
- Modify: `_meta/templates/foundation-template.md`
- Modify: `_meta/templates/common-sense-template.md`

- [ ] **Step 1: Baseline verification (must show zero before change)**

Run: `grep -rl '^## Visuals' /Users/nickma/Develop/My2ndBrain/A-Level/Physics/_meta/templates/ | wc -l`
Expected: `0`

- [ ] **Step 2: Insert the Visuals block into each of the 10 templates**

In every file above, the unique anchor is the literal block:

```
## Source Trace

- Source:
- Section/Page:
```

Using the Edit tool on each file, replace that anchor with:

```
## Visuals

<!-- Each entry: an authored diagram (Mermaid/SVG) OR an openly-licensed image.
     Every image MUST carry: caption, license, author, source URL.
     Authored-diagram source line: *Source: Authored for this vault (CC0). No external copyright.* -->

### [Diagram/Photo title]
![[_attachments/<file>]]
*Figure: <one-line caption explaining what to look at>.*
*Source: <Title> — <Author> — <License> — <canonical URL>. Retrieved <date>.*

## Source Trace

- Source:
- Section/Page:
```

Do this once per file (10 Edit calls). The `## Source Trace` block is identical and unique within each file, so each Edit is unambiguous.

- [ ] **Step 3: Verify all 10 templates now have the section, in the right place**

Run:
```bash
cd /Users/nickma/Develop/My2ndBrain/A-Level/Physics/_meta/templates
grep -rl '^## Visuals' . | wc -l
for f in physical-quantity concept law-result model representation experiment-practical application frontier-map foundation common-sense; do awk '/^## Visuals/{v=NR} /^## Source Trace/{s=NR} END{print FILENAME, (v && s && v<s)?"OK":"BAD"}' "$f-template.md"; done
```
Expected: first line `10`; every file prints `OK` (Visuals appears before Source Trace).

- [ ] **Step 4: Leave uncommitted (CLAUDE.md §5.11)**

Do not run `git commit`. Run `git status --short _meta/templates/` and confirm 10 modified files. Working tree stays dirty for human review.

---

## Task 2: Create the `_attachments/` tree

**Files:**
- Create: `_attachments/.gitkeep`
- Create: `_attachments/{03_Physical-Quantities,04_Concepts,05_Laws-and-Results,06_Models,07_Methods,08_Representations,09_Experiments-and-Practicals,10_Applications,11_Problems,12_Frontier-Maps}/.gitkeep`

- [ ] **Step 1: Verify it does not exist yet**

Run: `ls /Users/nickma/Develop/My2ndBrain/A-Level/Physics/_attachments 2>/dev/null || echo ABSENT`
Expected: `ABSENT`

- [ ] **Step 2: Create the mirrored tree**

Run:
```bash
cd /Users/nickma/Develop/My2ndBrain/A-Level/Physics
for d in 03_Physical-Quantities 04_Concepts 05_Laws-and-Results 06_Models 07_Methods 08_Representations 09_Experiments-and-Practicals 10_Applications 11_Problems 12_Frontier-Maps; do mkdir -p "_attachments/$d"; touch "_attachments/$d/.gitkeep"; done
touch _attachments/.gitkeep
```

- [ ] **Step 3: Verify the tree**

Run: `find /Users/nickma/Develop/My2ndBrain/A-Level/Physics/_attachments -name .gitkeep | wc -l`
Expected: `11`

---

## Task 3: Write the operational runbook

**Files:**
- Create: `_meta/visual-pipeline-runbook.md`

This is the contract every subagent obeys. It must be complete and unambiguous — no placeholders.

- [ ] **Step 1: Write the runbook with this exact content**

````markdown
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
`public domain`, `pd`, `cc0`, `cc by 4.0`, `cc by 3.0`, `cc by 2.5`,
`cc by-sa 4.0`, `cc by-sa 3.0`, `cc by-sa 2.5`, `nasa`, `us government`.

REJECT (do not download, log reason) if it contains `nc`, `nd`,
`noncommercial`, `no derivatives`, `gfdl` (without an accompanying CC allow
match), `fair use`, `non-free`, OR if license/author is empty/unknown.

NASA Images API results: treat as `Public Domain` with author = NASA unless the
item explicitly states otherwise (then run it through the same gate).

## 5. Download + caption

On ALLOW: download the file to
`_attachments/<NN_Folder>/<page-slug>--<descriptor>.<ext>` (ext from URL;
raster longest edge ≤ 1600px — if larger, still download, note for human).
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
````

- [ ] **Step 2: Verify the runbook is complete (no placeholder tokens)**

Run:
```bash
grep -nE 'TBD|TODO|FIXME|fill in|implement later' /Users/nickma/Develop/My2ndBrain/A-Level/Physics/_meta/visual-pipeline-runbook.md || echo "CLEAN"
grep -c '^## ' /Users/nickma/Develop/My2ndBrain/A-Level/Physics/_meta/visual-pipeline-runbook.md
```
Expected: `CLEAN`; section count `8`.

---

## Task 4: Smoke-validate the pipeline on one page

Internal correctness check (not a user-review pilot — execution is autonomous). Pick one unambiguous Photo page and one unambiguous Diagram page.

**Files:**
- Modify: `09_Experiments-and-Practicals/Required-Practicals/` — one micrometer/apparatus page (Photo path)
- Modify: one `08_Representations/*-Graph.md` page (Diagram path)

- [ ] **Step 1: Pick the two pages**

Run:
```bash
cd /Users/nickma/Develop/My2ndBrain/A-Level/Physics
ls 09_Experiments-and-Practicals -R | grep -i 'micromet\|caliper\|apparatus' | head
ls 08_Representations | grep -i 'graph' | head
```
Expected: at least one apparatus-type page and one graph page printed. Record both relative paths.

- [ ] **Step 2: Run the Commons license-gate query for the Photo page**

Run (replace query with the apparatus topic, e.g. `micrometer screw gauge`):
```bash
curl -s 'https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrsearch=micrometer%20screw%20gauge&gsrlimit=5&prop=imageinfo&iiprop=url|extmetadata' | jq -r '.query.pages[]? | [.title, .imageinfo[0].extmetadata.LicenseShortName.value, .imageinfo[0].extmetadata.Artist.value, .imageinfo[0].url] | @tsv'
```
Expected: rows with title, license, author, url. Confirm at least one row's license matches the Task 3 §4 ALLOW list.

- [ ] **Step 3: Apply the runbook to both pages**

Follow `_meta/visual-pipeline-runbook.md` end-to-end for the two pages: classify, author the SVG/Mermaid diagram for the graph page, download the license-passing photo for the apparatus page into the correct `_attachments/` subfolder, and edit only each page's `## Visuals` section.

- [ ] **Step 4: Verify the smoke result**

Run:
```bash
cd /Users/nickma/Develop/My2ndBrain/A-Level/Physics
git status --short | grep -E '_attachments/|08_Representations/|09_Experiments' 
grep -A6 '^## Visuals' "<photo-page-path>" | grep -E 'Source:|!\[\['
grep -A6 '^## Visuals' "<diagram-page-path>" | grep -E 'mermaid|!\[\[|Authored for this vault'
```
Expected: a downloaded file under `_attachments/09_*`; the photo page's Visuals block has an embed AND a `*Source: … — … — <license> — <url>*` line with a license from the ALLOW list; the diagram page has either a ```mermaid block or an SVG embed plus the `Authored for this vault (CC0)` source line. No other sections of either page changed (`git diff` shows only the Visuals block added).

- [ ] **Step 5: Gate decision**

If verification fails (e.g., license line missing, page body altered outside Visuals), STOP and fix the runbook before Task 5. Do not commit (§5.11).

---

## Task 5: Autonomous batch over all folders

**Files:**
- Modify: pages under `03_*`–`12_*` (Visuals section only)
- Create: files under `_attachments/<NN_Folder>/`

- [ ] **Step 1: Build the work list**

Run:
```bash
cd /Users/nickma/Develop/My2ndBrain/A-Level/Physics
for d in 03_Physical-Quantities 04_Concepts 05_Laws-and-Results 06_Models 07_Methods 08_Representations 09_Experiments-and-Practicals 10_Applications 11_Problems 12_Frontier-Maps; do echo "$d: $(find "$d" -name '*.md' | wc -l | tr -d ' ')"; done
```
Expected: per-folder counts (~03:51 04:88 05:30 06:16 07:29 08:20 09:16 10:20 11:43 12:7 at design time).

- [ ] **Step 2: Dispatch per-folder subagents in parallel batches**

For each folder, dispatch one subagent (general-purpose) with this exact prompt, substituting `<FOLDER>` and excluding the two pages already done in Task 4. Dispatch in batches of 3–4 concurrent subagents (a single message with multiple Agent calls), waiting for each batch before the next.

Subagent prompt:
```
You are processing folder <FOLDER> of the A-Level Physics vault at
/Users/nickma/Develop/My2ndBrain/A-Level/Physics.

OBEY EXACTLY: /Users/nickma/Develop/My2ndBrain/A-Level/Physics/_meta/visual-pipeline-runbook.md
Also obey CLAUDE.md (§4 templates highest authority; §5.1 raw read-only;
§5.2 no copyrighted reproduction; §5.4 edit only the ## Visuals section,
never silently overwrite other content; §5.11 do NOT git commit).

Before editing ANY page, READ the matching template under _meta/templates/
for that page's frontmatter `type` (CLAUDE.md §4 — non-negotiable).

For every .md page in <FOLDER> (recurse subfolders): apply the runbook
(classify → diagram/photo/both/none → license gate → caption → edit only the
## Visuals section). Skip pages that already have a valid visual. Never touch
raw/. Never commit.

Return ONLY a TSV manifest, one line per page processed, in the exact format
from runbook §8. No prose.
```

- [ ] **Step 3: Collect manifests**

Concatenate every subagent's returned TSV into one in-memory manifest. Verify line count is within range of total pages scanned (allow `none`/`skip` lines). Expected: a TSV with one line per non-skipped page and a recognizable `outcome` in column 2 for every line.

---

## Task 6: Bookkeeping

**Files:**
- Create: `.state/visual-manifest.tsv`
- Modify: `log.md`
- Modify/Create: relevant `13_Sources/*` pages for image-only origins

- [ ] **Step 1: Write the manifest**

Write the aggregated TSV (Task 5 Step 3) to `.state/visual-manifest.tsv` with a header line:
`page\toutcome\tfile\tlicense\tsource_url\tdate\tnote`

- [ ] **Step 2: Verify the manifest**

Run:
```bash
cd /Users/nickma/Develop/My2ndBrain/A-Level/Physics
head -1 .state/visual-manifest.tsv
awk -F'\t' 'NR>1{c[$2]++} END{for(k in c) print k, c[k]}' .state/visual-manifest.tsv
awk -F'\t' 'NR>1 && ($2=="photo"||$2=="both") && ($4==""||$5=="") {print "MISSING PROVENANCE:", $1}' .state/visual-manifest.tsv || true
```
Expected: header prints; outcome breakdown prints; the third command prints NOTHING (every photo has a license and source URL — copyright invariant).

- [ ] **Step 3: Append the log entry**

Append to `log.md`:
```
## 2026-05-19 — Visual pipeline batch
Folders 03–12. Pages scanned: <N>. Diagrams: <d>. Photos: <p>. Both: <b>.
Skipped/none: <s>. Deferred/needs-human: <h>. Manifest: .state/visual-manifest.tsv.
No commit (CLAUDE.md §5.11).
```
Fill `<...>` from the Step 2 breakdown.

- [ ] **Step 4: Record image-only sources**

For each distinct non-NASA source domain in the manifest not already in
`13_Sources/`, create a short `source`-type page per
`_meta/templates/source-template.md` (read it first — §4) recording the
origin, license basis, and the pages it supplied. Wikimedia Commons may be a
single shared source page listing the file URLs.

- [ ] **Step 5: Verify bookkeeping, leave uncommitted**

Run: `git status --short | wc -l` (expect many changed/new files) and
`grep -c 'Visual pipeline batch' log.md` (expect `1`). Do NOT commit.

---

## Task 7: Final report & self-verification

- [ ] **Step 1: Copyright invariant re-check (must be clean)**

Run:
```bash
cd /Users/nickma/Develop/My2ndBrain/A-Level/Physics
for f in $(awk -F'\t' 'NR>1 && ($2=="photo"||$2=="both"){print $3}' .state/visual-manifest.tsv); do [ -f "$f" ] || echo "MISSING FILE: $f"; done
grep -rL 'Source:' $(grep -rl '!\[\[_attachments' 03_* 04_* 05_* 06_* 07_* 08_* 09_* 10_* 11_* 12_* 2>/dev/null) 2>/dev/null | sed 's/^/NO SOURCE LINE: /' || true
```
Expected: no `MISSING FILE` and no `NO SOURCE LINE` output. Any output here is a copyright failure — fix before reporting done.

- [ ] **Step 2: Emit the final report to the user**

Report: total pages scanned; visuals added (diagrams vs photos vs both);
skipped-with-reasons; license breakdown (from manifest col 4); list of
`deferred`/`needs-human` pages for human follow-up; count of files touched
(`git status --short`). State explicitly that nothing was committed and the
working tree is left dirty for review (CLAUDE.md §5.11).

- [ ] **Step 3: Do not commit**

Confirm no `git commit` was run at any point. End.

---

## Self-Review

**Spec coverage:** §3.1 template amend → Task 1. §3.2 attachments → Task 2.
§3.3 caption backbone → runbook §5 (Task 3) + invariant checks (Task 6 S2,
Task 7 S1). §4.1 classification → runbook §1. §4.2 diagrams → runbook §2.
§4.3 sourcing APIs → runbook §3. §4.4 license gate → runbook §4 + Task 4 S2.
§5 execution architecture → Tasks 4–5. §5.1 idempotency/non-destruction →
runbook §6 + Task 4 S4. §6 bookkeeping → Task 6. §7.1 error handling →
runbook §7. §7.2 final report → Task 7. All spec sections mapped.

**Placeholder scan:** Angle-bracket tokens (`<FOLDER>`, `<N>`, `<file>`) are
runtime substitution points with explicit fill instructions, not unspecified
work. No "TBD/handle edge cases/similar to Task N". Clean.

**Type consistency:** Manifest schema (`page,outcome,file,license,source_url,
date,note`; outcome ∈ {diagram,photo,both,none,skip,deferred,needs-human}) is
defined once in runbook §8 and used identically in Task 5 S3, Task 6 S1–S2,
Task 7 S1. License ALLOW/REJECT list defined once in runbook §4 and referenced
by Task 4 S2/S4. Consistent.
