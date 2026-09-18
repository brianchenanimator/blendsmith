# Changelog

Maintainers update release versions. Unreleased proposals live in uniquely named `changes/` records until reviewed.

## 2026.09.011 — 2026-09-18 — Actual Blender-file delivery

- Added R11: execute the authorized build, save the actual versioned `.blend`, reopen it and provide an accessible artifact. Generation scripts alone do not fulfill a model request.
- Explicitly report unavailable execution or artifact access; preserve analysis/review-only and requested script-only exceptions.
- Synchronized English/Traditional Chinese instructions, delivery checklist, recording templates and rule-ID validation. No model files changed; behavioral trial pending.

See [change record](changes/2026-09-18-actual-blend-delivery.md).

## 2026.09.010 — 2026-09-17 — Calendar versioning

- Adopted `YYYY.MM.NNN` version labels at the maintainer's request; initial label is 2026.09.010 and the matching tag is v2026.09.010.
- Synchronized current English/Chinese skill and README versions, publishing guidance and validator. Regenerated the source ZIP under the new version.
- Preserved 0.2.0 and 0.1.x historical entries, previous change records and backup/release archives. No modeling rules, license or invocation changed.
- Starting at sequence 010 does not assert nine earlier public releases. Future releases increment the monthly sequence; a new month starts at 001. Compatibility is explained in change notes, not inferred from the number.

See [change record](changes/2026-09-17-calendar-version.md). This is a local package update, not a GitHub release.

## 0.2.0 — 2026-09-17 — blendsmith public-preview packaging

- Renamed the skill from `blender-production-assets` to `blendsmith`; invocation is now `$blendsmith`, and the installable directory is `skill/blendsmith/`.
- Preserved existing R01–R10 production requirements and supporting templates/checklists.
- Replaced the machine-specific worklog default with a configured central path or the active project's `worklog/` fallback. Existing configured locations remain in force.
- Adopted GPL-3.0-only as selected by the maintainer; included the full license in repository and installable skill.
- Added English/Traditional Chinese project introductions, contribution rules, change records, PR/issue templates, publishing guidance and document validation.
- Removed private worklog links and the private video URL from the public copy; historical labels remain as explicitly unavailable provenance.
- Replaced stale top-level intake status with package status and a dated trial-status clarification. No previously pending asset is newly marked accepted.

Compatibility: old `$blender-production-assets` invocations and installation paths must be updated when adopting this package. No automatic global install, model migration or Blender file edits occur. The previous package is privately backed up and retained.

Validation scope: packaging/document checks only; no new Blender asset trial. See [change record](changes/2026-09-17-public-package.md).

## Inherited baseline — 0.1.10

Private predecessor with reference confirmation, readable shaders, four-channel BSDF delivery, topology/UV requirements, native pose controls, pre-bake normals/proxy verification and the accepted 3D07 material-source/atlas workflow. Its case histories remain in the [feedback register](skill/blendsmith/references/feedback-register.md); this is not a claim of a previous public release.
