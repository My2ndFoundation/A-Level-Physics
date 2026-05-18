# Ingest Workflow

This workflow processes one raw Physics source into the wiki layer. It must be consistent with `CLAUDE.md` and must never bypass `_meta/templates/`.

## Steps

```text
1. Read raw source
2. Identify candidate page objects
3. Search aliases and existing pages
4. Read relevant templates
5. Classify source layer: everyday / pre-GCSE / GCSE / bridge / A-Level / frontier
6. Produce checkpoint
7. Wait for user confirmation
8. Write source page
9. Write/update atomic pages
10. Update MOCs
11. Update index
12. Append log
13. Append .state/ingested.tsv
14. Report
15. Do not auto-commit
```

## Hard Rules

- **No wiki files may be written before the user checkpoint (Step 6) is accepted (Step 7).**
- **Step 4 must never be skipped.** Every page type written must follow its required `_meta/templates/` template.
- `raw/` is immutable. Never edit, rename, reformat, or delete raw files.
- Do not reproduce copyrighted material. Follow `_meta/copyright-rules.md`.
- Frontier pages must remain shallow. Follow `_meta/frontier-rules.md`.
- Do not silently overwrite. Preserve source variations as a variation block (see `CLAUDE.md` §5.4).
- Do not auto-commit. Leave the working tree dirty for human review.

## Checkpoint Contents (Step 6)

The checkpoint summary to the user should include:

- the raw source and classified learning layer
- the list of candidate knowledge objects with their proposed page types
- which are new pages vs updates to existing pages
- any alias collisions or duplicate-page risks
- which templates will be used
- any copyright or frontier-depth concerns
- any unresolved links anticipated

Only after explicit user confirmation may Steps 8–15 proceed.
