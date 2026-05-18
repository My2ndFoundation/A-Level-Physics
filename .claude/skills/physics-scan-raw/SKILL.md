---
name: physics-scan-raw
description: Use when the user wants to find raw/ sources that haven't been ingested yet, or asks "scan raw"、"扫一下 raw"、"还有哪些没处理"、"batch ingest"、"check for new sources" in the A-Level Physics project. Discovers unprocessed files under raw/ by diffing against .state/ingested.tsv, then dispatches /physics-ingest-source one file at a time.
model: claude-sonnet-4-6
effort: low
---

# A-Level Physics Raw Scanner

## Overview

Two-job skill:
1. **Discover** — diff every file under `raw/` against `.state/ingested.tsv`; surface the unprocessed ones.
2. **Dispatch** — for each new file, hand control to `/physics-ingest-source`, which runs its own template-read step, learning-layer step, and Step 6 user-checkpoint per source.

`.state/ingested.tsv` is the single source of truth for "processed". It is written **exclusively** by `/physics-ingest-source` (or, for problem-layer-only passes, `/physics-problem-extract`). This skill only reads it.

## The Non-Negotiable Rules

- **One source at a time** by default (CLAUDE.md §10). Never start ingest #2 before ingest #1's checkpoint and writes are complete.
- **Never write to `.state/ingested.tsv` (or any `.state/` file) from this skill.** Only the ingest/extract skills append. If a file looks "new" but was actually processed, the bug is in the state file — fix it explicitly with the user, do not silently skip.
- **Never write to `raw/`.** This skill is read-only against `raw/` (CLAUDE.md §5.1).
- **Do not invent files in `raw/`.** This skill discovers; it does not create.

## Workflow

**Step 1 — Compute the diff**

Run from the project root:

```bash
LC_ALL=C comm -23 \
  <(find raw -type f ! -name '.gitkeep' ! -name '.DS_Store' | LC_ALL=C sort) \
  <(tail -n +2 .state/ingested.tsv | cut -f1 | LC_ALL=C sort)
```

Notes:
- **`LC_ALL=C` is mandatory on both `sort`s and `comm`.** Locale-dependent collation is non-deterministic and silently mismatches the diff. Either all are byte-sorted or none — don't mix.
- `raw/` is **nested** in this project (`raw/specifications/`, `raw/textbooks/`, `raw/gcse-foundations/`, `raw/past-papers/`, `raw/practicals/`, `raw/notes/`, `raw/frontier/`, `raw/other/`). Do **not** add `-maxdepth 1` — every subfolder must be scanned.
- Sources may be any file type (`.md`, `.pdf`, `.txt`, `.docx`…). `find raw -type f` (no `-name '*.md'`) catches them all; `! -name '.gitkeep'` drops the structure placeholders.
- `tail -n +2` strips the header row (`raw_path\tdate\tsource_page\tstatus\tnotes`). `cut -f1` takes the raw-path column — use `cut`, not `awk` regex (BSD awk on macOS is fragile).
- `comm -23` = lines only in the first input. Both inputs must be sorted the same way (hence `LC_ALL=C` everywhere).
- Filenames may contain spaces/colons — fine in bash; never pipe to `xargs` without `-d '\n'`.

If `.state/ingested.tsv` does not exist: report it and stop. Ask the user whether to create the header-only file — do not auto-create, because an empty state file asserts "nothing has ever been ingested", which may be false.

**Step 2 — Report findings**

Format:

```
Scan result (raw/ total N files, M processed)

New files (N - M):
  1. raw/<subfolder>/<name>
  2. raw/<subfolder>/<name>
  ...
```

Show the actual list — never "summarize instead". If `N - M == 0`: report "All processed ✅" and stop. Do not invoke `/physics-ingest-source`.

**Step 3 — Confirm scope with the user**

Ask explicitly:
- Ingest all, in the listed order?
- Only some? (have the user give the numbers)
- Reorder / group? (e.g. the OCR H556 specification first, then textbooks, then practicals, then past papers, frontier references last)

**Wait for the user's answer.** Do not start ingest until scope is confirmed. The user may defer files (e.g. wanting the specification ingested before textbooks so the syllabus map exists first).

**Step 4 — Dispatch sequentially**

For each file in the confirmed list, invoke:

```
/physics-ingest-source raw/<subfolder>/<filename>
```

Then **let `/physics-ingest-source` run end-to-end**, including its Step 4 template-read, its Step 5 learning-layer classification, its Step 6 user-checkpoint, and its Step 13 state-file append. Only after it completes (and the user has not asked to stop) move to the next file.

Between files, give a one-line breadcrumb: `→ Entering K/N: raw/<subfolder>/<filename>`. Nothing more — the ingest skill owns its own narration.

**Step 5 — Final tally**

After the last file (or when the user says stop), report:
- Completed this run: K files
- Skipped / remaining: the leftover file list
- Any `.state/unresolved-links.md` items worth a follow-up source (informational only — do not act)

## Edge Cases

| Situation | Handling |
|---|---|
| `.state/ingested.tsv` missing | Stop, report, ask how to bootstrap. Don't assume "nothing ingested". |
| State file lists a `raw/...` path that no longer exists | Surface as a warning ("state references missing raw/..."). Likely renamed/moved. Ask before any `.state/` edit (and the edit is the user's / ingest's, not this skill's). |
| State file row has wrong field count | Surface to the user. This skill reads col 1 only; a malformed file is a data bug to fix explicitly, not silently. |
| Raw file is a binary/scanned PDF with no extractable text | Still list it as "new". `/physics-ingest-source` decides whether it's ingestable and may stop with a request for a text version. |
| User asks for "all" but there are many new files | Confirm again before starting — sequential ingests with checkpoints take real time and attention. |
| User wants to re-ingest a file already in the state file | Don't silently re-run. Ask why (source page deleted? raw updated?). Surface. |
| New file is just a placeholder/empty | List it; let the user decide whether to skip in Step 3. |
| File under `raw/practicals/` | Still dispatch `/physics-ingest-source`; it will route practical content to `experiment-practical` pages (or suggest `/physics-practical-extract`). |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Writing to `.state/ingested.tsv` from this skill | State writes belong to `/physics-ingest-source`. This skill is a reader. |
| Calling `/physics-ingest-source` for file #2 before #1's checkpoint completes | One source at a time. Wait. |
| Skipping the Step 3 user-confirmation and auto-processing all | The user may want to triage by source type or sequence the spec first — ask. |
| Suppressing the diff output and "summarizing" instead | Show the actual file list. |
| Adding `-maxdepth 1` to `find` | `raw/` is nested here — you'd miss every file in the subfolders. |
| Restricting `find` to `-name '*.md'` | Sources may be PDF/txt/docx; scan all file types except `.gitkeep`. |
| Stripping the header with `grep -v '^#'` | This project's header is a plain `raw_path\t…` line — use `tail -n +2`. |
| Piping the diff to `xargs` on whitespace | Filenames contain spaces. Use a `while read -r` loop. |

## Red Flags — STOP

- About to `Write`/`Edit` `.state/ingested.tsv` (or any `.state/` file)
- About to call `/physics-ingest-source` for the next file before the previous one finished
- About to call `/physics-ingest-source` without first showing the user the diff list
- About to declare "all done" while skipping files without user consent
- About to auto-create `.state/ingested.tsv` instead of asking the user
