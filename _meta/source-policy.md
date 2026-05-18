# Source Policy

This file defines the trusted source pool and the per-page-type source selection
rules for the A-Level Physics vault. It is authoritative for the
`physics-source-research`, `physics-complete-page`, and `physics-build-base-cluster`
skills. Copyright rules in `_meta/copyright-rules.md` and `CLAUDE.md` §5.2 always
apply: paraphrase and reference; never reproduce long copyrighted passages,
chapters, exercise sets, or full copyrighted worked examples.

## Trusted Source Pool

### Official OCR / assessment spine

Use for syllabus alignment, formulae, assessment boundaries, practical
requirements, and exam expectations.

- OCR Physics A H556 qualification page
- OCR H556 specification — local: [[OCR-Physics-A-H556-Specification]]
- OCR assessment page
- OCR Data, Formulae and Relationships Booklet
- OCR mathematical skills handbook — local: [[OCR-Physics-Mathematical-Skills-Handbook]]
- OCR practical skills handbook — local: [[OCR-Physics-Practical-Skills-Handbook]]
- OCR past papers, mark schemes, examiner reports

### Concept explanation sources

Use for physical quantities, concepts, laws, models, representations, applications.

- OpenStax College Physics
- The Physics Classroom
- Physics LibreTexts
- HyperPhysics
- Khan Academy Physics
- Wikipedia — concept navigation and broad cross-links only, never the sole explanatory source

### UK teaching / foundation sources

Use for GCSE foundations, bridge-to-A-Level explanations, practical intuition,
misconceptions, and UK school context.

- IOPSpark
- Institute of Physics
- STEM Learning
- BBC Bitesize GCSE Physics
- A-Level Physics Online

### Problem-solving sources

Use for problem types, method patterns, common traps, practice orientation.

- Isaac Physics (Isaac Science)
- Physics & Maths Tutor (PMT)
- OCR past papers and mark schemes

### Frontier orientation sources

Use only for shallow frontier maps (orientation, not mastery — `_meta/frontier-rules.md`).

- Institute of Physics — Explore Physics
- CERN Science — local: [[CERN-Science]]
- NASA Astrophysics — local: [[NASA-Astrophysics]]
- ESA Science and Exploration
- Perimeter Institute resources
- Wikipedia — navigation only

## Source Selection by Page Type

```text
common-sense      → Physics Classroom / BBC Bitesize / IOPSpark / PhET
foundation        → Physics Classroom / BBC Bitesize / Khan Academy / IOPSpark
physical-quantity → OCR / OpenStax / Physics Classroom / HyperPhysics
concept           → OCR / OpenStax / Physics Classroom / IOPSpark / LibreTexts
law-result        → OCR / OpenStax / HyperPhysics / LibreTexts
model             → OCR / OpenStax / Physics Classroom / LibreTexts
method            → OCR / Isaac / Physics Classroom / OpenStax
representation    → OCR / OpenStax / Physics Classroom / PhET / IOPSpark
experiment        → OCR practical handbook / IOPSpark / STEM Learning / PhET
application       → OpenStax / IOPSpark / Isaac / OCR
problem-type      → OCR papers / Isaac / PMT / OpenStax
mistake-pattern   → Physics Classroom / IOPSpark / OCR examiner reports / PMT
frontier-map      → IOP / CERN / NASA / ESA / Perimeter / Wikipedia navigation
```

## Source Trace Convention for Baseline Pages

Baseline pages are built from this public pool, not from a raw ingest. Their
`## Source Trace` should:

- name the explanatory source(s) used (e.g. "OpenStax College Physics; The Physics Classroom") — **no copied text**;
- anchor syllabus alignment to the local OCR source page, e.g.
  `OCR alignment: [[OCR-Physics-A-H556-Specification]]`;
- set frontmatter `sources: []` unless a `13_Sources/` provenance page genuinely exists.

Do not fabricate `13_Sources/` provenance pages for public-pool references.
