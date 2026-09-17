# Change: Publishable blendsmith source package

- Base version / commit: private blender-production-assets 0.1.10; no public base commit.
- Author: blendsmith maintainer, assisted by Codex.
- Date: 2026-09-17.
- Type: packaging.
- Affected rule IDs: R05 portable log location; R07 bilingual parity. R01–R10 IDs retained.
- Changed / renamed / deleted files: skill folder/name/invocation renamed in public copy; SKILL.md, Chinese copy, metadata and feedback register adapted; LICENSE/NOTICE, root READMEs, contribution/release docs, templates and validator added. Original private files retained.
- Status: implementation complete; maintainer review of generated package pending.

## Problem

The private skill contained a local Windows log path, private evidence links and no public introduction or structured collaboration process. The user requested the name blendsmith, an original ZIP backup and GPL-3.0 licensing.

## Before and after

Before: a local blender-production-assets package bound to the original project. After: a blendsmith source tree with relative references, a portable log fallback, full GPL-3.0-only license, bilingual introduction and reviewable contribution records. Production requirements are retained.

## Scope and exclusions

Packaging and workflow portability only. No model edits, new Blender validation, global installation, GitHub account changes or public upload. Private evidence is not included or represented as publicly reproducible.

## Evidence and tests

Repository checks are run with `python scripts/validate.py`. The accompanying local handoff report records actual results, source ZIP content hashes, translation/name checks, link checks and destination verification. No new Blender trial: NOT RUN (outside packaging scope). Public historical evidence remains unavailable; user acceptance of this package is pending.

## Compatibility

Invoke `$blendsmith` after installing `skill/blendsmith`. Old invocations are not aliases. Existing configured central worklogs remain authoritative; new projects fall back to project-local worklog/. Original private skill and backup permit rollback. Version 0.2.0 marks the name/path change from 0.1.10.

## Language sync

English SKILL.md and Traditional Chinese copy both use 0.2.0, portable logging and the new name. Both READMEs describe the same scope, installation, evidence limits and license.

## Limitations and feedback

Template use does not configure GitHub branch protection. Documentation checks do not establish asset quality. User review pending; no public release or new asset acceptance is claimed.
