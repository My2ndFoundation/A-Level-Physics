# Future Agents and Skills

This file describes future agent/skill roles for this vault.

No skills are implemented during initialisation.

## physics-ingest-source

Purpose:
Process one raw Physics source into source page, atomic pages, MOCs, index, log, and ingestion state.

Must obey:
- `CLAUDE.md`
- `_meta/templates/`
- `_meta/workflows/ingest-workflow.md`
- `_meta/copyright-rules.md`
- `_meta/frontier-rules.md`

## physics-scan-raw

Purpose:
Compare `raw/` with `.state/ingested.tsv` and report unprocessed files.

## physics-lint-wiki

Purpose:
Check page health, duplicate aliases, missing metadata, orphan pages, missing source trace, template violations, frontier-depth violations, and MOC gaps.

## physics-expand-concept

Purpose:
Take an existing atomic page and improve it using approved sources while preserving source trace and template compliance.

## physics-build-moc

Purpose:
Rebuild or improve a MOC based on existing linked pages and tags.

## physics-problem-extract

Purpose:
Process worked examples or exercises into problem types, methods, common traps, and worked-example pages.

## physics-practical-extract

Purpose:
Process practical guides into experiment/practical pages, measurement methods, uncertainty pages, graph-analysis pages, and apparatus technique pages.

## physics-frontier-map

Purpose:
Create or update shallow frontier maps that connect A-Level Physics ideas to modern Physics without going into excessive detail.
