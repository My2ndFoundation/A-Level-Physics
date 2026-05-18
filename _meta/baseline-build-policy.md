# Baseline Build Policy

This vault must be built upfront into a complete usable baseline.

The goal is not to wait for the course to create core knowledge pages.

The baseline build should create or complete:

- everyday physics explanations
- pre-GCSE and GCSE foundations
- bridge-to-A-Level pages
- A-Level OCR H556 core concepts
- physical quantities
- laws and results
- models
- methods
- representations
- experiments and practicals
- applications
- problem-type baseline pages
- common mistake patterns
- shallow frontier maps
- cross-subject links

The target status for core baseline pages is `usable`.

Later course progress should refine and personalise the vault through:

- classroom notes
- teacher feedback
- homework
- practical records
- mistakes
- past papers
- exam technique
- deeper explanations

## Status and learning-stage vocabulary

```yaml
status: seed | draft | usable | reviewed | mature
learning_stage: pre-a-level | year-12 | year-13 | exam-revision | extension
```

## Authorisation and checkpoints

The user has explicitly approved a full baseline construction pass. During the
baseline build, `physics-build-base-cluster` does **not** stop for a per-page
checkpoint. It stops only for: copyright risk, destructive overwrite risk, major
ambiguity, broken project structure, or an unclear source conflict.

This authorisation is specific to the baseline build. Normal long-term ingestion
(`physics-ingest-source`) keeps its Step 6 user checkpoint.

## Non-negotiables still in force

All of `CLAUDE.md` still applies during the baseline build, in particular:
the template rule (§4), search-before-create (§5.3), never-silent-overwrite
(§5.4), broad-topics-are-MOCs (§5.5), atomic size (§5.6), frontmatter (§5.7),
wikilinks (§5.9), copyright (§5.2 / `_meta/copyright-rules.md`), frontier
shallowness (§3 / `_meta/frontier-rules.md`), and no auto-commit (§5.11).
Source selection follows `_meta/source-policy.md`.
