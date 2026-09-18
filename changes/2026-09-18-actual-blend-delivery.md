# Actual Blender-file delivery

- Base version / commit: 2026.09.010; remote baseline observed as 6032b63c4e596e316601eeaa1ca326452e9f92c8.
- Affected rule IDs: R11 (new); R05 recording fields and existing delivery checks aligned.
- Changed / renamed / deleted files: SKILL.md and SKILL.zh-TW.md; both READMEs; CONTRIBUTING.md; CHANGELOG.md; docs/publishing.md; scripts/validate.py; production-checklist.md; feedback-register.md; production-brief.template.md; worklog.template.md; this change record. No renamed or deleted files.

## Problem

The maintainer reports a trial whose output folder contained generation scripts but no `.blend`; they had to run PowerShell to obtain the model. The original trial files were not available for independent inspection.

## Before and after

Before: general save/reopen instructions did not explicitly prohibit handing final generation back to the user. After: R11 requires assistant execution, an actual versioned file, fresh reopen and an accessible artifact link/attachment. Scripts remain supplementary unless script-only output is explicitly requested.

## Scope and exclusions

Applies to agreed Blender asset deliveries and their delivery milestones. Pure analysis/review and explicit script-only tasks are excluded. If execution or artifact access is unavailable, report partial/blocked work; do not claim completion. No Blender assets, installs, budgets or rig semantics changed.

## Evidence and tests

- User report: recorded as a faithful summary in F021; not independently reproduced.
- Repository document validation and system skill metadata validation: run for this revision; actual command outcomes are recorded in the private session worklog and release verification report.
- Manual scope review: successful build must yield a reopenable file; failed build/stale output remains incomplete; unavailable Blender must be disclosed; explicit script-only and analysis-only requests retain their scope.
- Blender behavioral trial: NOT RUN; this is a documentation correction, with the next relevant asset trial pending.

## Compatibility

No file format or invocation changes. Workflows previously claiming completion with scripts alone must execute generation or report incomplete status. Version 2026.09.011 uses the established calendar sequence.

## Language sync

English R11 and its Traditional Chinese reading copy have matching scope, exceptions, verification and limitations. Both READMEs are updated.

## Limitations and feedback

Instructions cannot supply missing runtime capabilities or guarantee agent compliance. Re-test on the user's next asset/environment; check actual output and reopening, not just script presence. Post-change user acceptance is pending.
