# Physics Wiki

This is an LLM-maintained Obsidian wiki for Physics.

- `raw/` contains immutable source files. They are never edited, renamed, reformatted, or deleted.
- `_meta/` contains templates, rules, workflows, and operating constraints for LLM agents.
- The wiki layer contains atomic Physics knowledge pages, MOCs, source records, an index, a log, and ingestion state.
- Sources are **not** copied wholesale into the wiki. Pages paraphrase, reference, and connect ideas.
- Each future ingested source should create or update atomic pages, MOCs, source pages, `index.md`, `log.md`, and `.state/ingested.tsv`.
- Broad syllabus areas (Mechanics, Electricity, Waves, …) are represented through **tags and MOCs**, not large content pages.
- The vault supports **OCR Physics A H556**.
- The vault also includes common-sense Physics, pre-GCSE foundations, GCSE foundations, bridge-to-A-Level pages, and shallow frontier maps.
- Physics knowledge should connect concepts, quantities, laws, models, maths, graphs, experiments, applications, and problem-solving.

The highest-authority document for this project is [`CLAUDE.md`](CLAUDE.md). The project control layer is [`_meta/`](_meta/README.md).
