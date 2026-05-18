# A-Level Physics Knowledge Graph

An LLM-maintained Obsidian vault that turns raw Physics sources into a
**connected knowledge graph** for learning Physics before and during A-Level
study — built around **OCR Physics A (H556)**.

It is *not* a revision pack, a textbook mirror, a folder of chapter summaries,
or a formula sheet. It is a navigable web of small, single-purpose pages that
connect intuition → concepts → maths → graphs → experiments → applications →
problems → common mistakes.

## The five learning layers

Physics is treated as one continuous system, not an isolated syllabus:

| Layer | Purpose | Depth |
|---|---|---|
| Everyday intuition | Build physical common sense | simple |
| Pre-GCSE / GCSE foundation | Stabilise prerequisite ideas | accurate |
| Bridge to A-Level | Make GCSE ideas precise & mathematical | transitional |
| **A-Level OCR H556 core** | **The main examinable graph** | **detailed** |
| Frontier edge maps | Where ideas lead beyond A-Level | shallow orientation only |

## Layout

```
00_Home/            Entry points & global maps          (6)
01_MOCs/            Maps of Content — navigation        (30)
02_Foundations/     Everyday, pre-GCSE, GCSE, bridge    (21)
03_Physical-Quantities/  Measurable quantities & units  (53)
04_Concepts/        Physical ideas & phenomena          (89)
05_Laws-and-Results/  Laws, principles, equations       (31)
06_Models/          Idealised systems & assumptions     (16)
07_Methods/         Problem-solving procedures          (29)
08_Representations/ Graphs, diagrams, notations         (20)
09_Experiments-and-Practicals/  Practical skills        (16)
10_Applications/    Applied & cross-topic contexts      (20)
11_Problems/        Problem types, worked examples,
                    mistake patterns                    (43)
12_Frontier-Maps/   Shallow maps beyond A-Level          (7)
13_Sources/         Provenance records                   (7)
_meta/              Templates, rules, workflows (control layer)
raw/                Immutable source input (read-only)
.state/             Operational state (aliases, ingest log, lint)
```

~345 usable atomic pages across the OCR H556 baseline (no `seed` stubs
remaining in built clusters).

## Using the vault as a learner

- Start at **`00_Home/`** or a topic **MOC** in `01_MOCs/` (e.g.
  `Mechanics-MOC`, `Waves-MOC`, `Quantum-Physics-MOC`).
- `index.md` is the flat A-Z listing of every page by type.
- Follow the wikilinks — every page connects its quantities, laws, models,
  representations, experiments, applications, and common mistakes.
- Broad areas (Mechanics, Electricity, Waves…) exist **only as MOCs and
  tags**, never as large monolithic pages.

## How it is maintained

The vault is built and grown by LLM skills under `.claude/skills/`
(`physics-ingest-source`, `physics-build-base-cluster`,
`physics-complete-page`, `physics-expand-concept`, `physics-lint-wiki`,
`physics-build-moc`, `physics-frontier-map`, `physics-problem-extract`,
`physics-practical-extract`, `physics-scan-raw`, `physics-source-research`).

Every page created or substantially updated must follow its required
template in `_meta/templates/`. Ingestion follows the staged workflow in
`CLAUDE.md` §10 (read source → search existing → checkpoint → write →
update MOCs/index/log/state). Sources are **paraphrased and referenced,
never copied wholesale** — source pages are extraction records, not
reproduced text.

## Conventions

- `raw/` is **read-only**: never edited, renamed, or deleted; errors are
  recorded in source pages, not fixed in place.
- One canonical page per object; alternative names are aliases
  (`.state/aliases.tsv`), never duplicate pages.
- Atomic pages stay focused (~300–800 words); over-broad pages are split.
- Frontier pages stay shallow — orientation, not university-level depth.
- No auto-commit: the working tree is left for human review.

## Cloning note

The OCR A textbook under `raw/textbooks/` is stored via **Git LFS**
(it exceeds GitHub's 100 MB blob limit). Install `git lfs` before cloning
to pull the actual file; without it you get a small pointer. The smaller
specification PDFs are normal git blobs.

## Authority

The highest-authority document is [`CLAUDE.md`](CLAUDE.md) — all workflows,
skills, and agents obey it. The project control layer is documented in
[`_meta/`](_meta/README.md); build and source policy live in
`_meta/baseline-build-policy.md` and `_meta/source-policy.md`.
