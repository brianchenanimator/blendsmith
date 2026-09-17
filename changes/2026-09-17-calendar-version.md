# Change: Adopt calendar version labels

- Base version / commit: blendsmith 0.2.0 local source; remote commit not inspected.
- Author: blendsmith maintainer, assisted by Codex.
- Date: 2026-09-17.
- Type: packaging.
- Affected rule IDs: R07 synchronized language copies; no production behavior change.
- Changed / renamed / deleted files: current SKILL.md, SKILL.zh-TW.md, both READMEs, CHANGELOG.md, docs/publishing.md and scripts/validate.py updated; this record added. No files deleted.
- Status: implemented; user review pending.

## Problem

The maintainer requested a date-based version such as v2026.09.010 and asked to update the files themselves.

## Before and after

Before: current local package 0.2.0 and guidance for patch/minor increments. After: quoted current version 2026.09.010, GitHub tag v2026.09.010, calendar-version guidance and format validation.

## Scope and exclusions

Current packaging metadata only. Existing historical 0.2.0/0.1.x records and archives remain unchanged. No Blender files, production rules, license, invocation or GitHub repository changed.

## Evidence and tests

PASS: repository document checks, current bilingual version consistency and meaningful validator cases. Invalid months, zero or malformed sequences and an old-format current version are rejected. Original historical change record and unaffected files are compared by hash. Release ZIP is verified per file. Blender tests and remote GitHub publication: NOT RUN (outside scope).

## Compatibility

Skill name remains blendsmith. Version consumers must treat CalVer as a string and not assume SemVer. Sequence 010 is an initial label chosen for this migration; earlier releases are not implied. Future months restart at 001; compatibility remains explicit in release notes.

## Language sync

English and Traditional Chinese current versions are 2026.09.010; both README pages explain the date-based format. English maintenance guidance is authoritative.

## Limitations and feedback

Checks concern package consistency, not Blender output. User review pending. No remote tag or release was created.
