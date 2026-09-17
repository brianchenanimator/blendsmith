# Contributing to blendsmith

English is authoritative for maintained instructions, change records and worklogs. User reports may be in any language; label translated summaries. Keep the Traditional Chinese reading copy aligned when changing skill behavior.

## Submit one understandable change

1. Identify the failing behavior or missing requirement. For a consequential change to budgets, confirmation, topology or rig semantics, open an issue with an example before proposing a universal rule.
2. Fork the repository and create a focused branch. Record the base version and commit, if available.
3. Modify the narrowest appropriate rule/reference. Preserve existing R01–R10 identifiers. Propose new IDs as `PROPOSED` until assigned by the maintainer; do not renumber old rules.
4. Copy [changes/TEMPLATE.md](changes/TEMPLATE.md) to `changes/YYYY-MM-DD-short-topic-author.md`. Use a unique filename. Complete the before/after behavior, scope, evidence and compatibility fields; use N/A with a reason where appropriate.
5. Synchronize affected English and Traditional Chinese instructions. If translation is unavailable, explicitly mark it pending in the PR; the maintainer must resolve it before release.
6. Run `python scripts/validate.py` and perform any relevant behavioral/asset tests. Open a PR with the [PR template](.github/pull_request_template.md).

Do not bump the version independently for every PR. Maintainers assign versions at integration/release, synchronize metadata and translations, and update CHANGELOG.md. A merged change record preserves the original base version and evidence.

## Evidence that helps review

Report Blender version, assistant/model when relevant, inputs, reproduction steps, expected/actual behavior and changed output. Compare before/after under matching geometry, camera and lighting where applicable. Disclose changed budgets or settings so improvements are not attributed to the wrong cause. A useful counterexample helps establish the rule's boundary.

Use **PASS**, **FAIL**, **NOT RUN** or **N/A**. Separate document validation, Blender data checks, visual/interactive checks and user acceptance. Never change old logs to make an earlier delivery appear accepted. Do not present an AI-generated assertion as measured evidence.

Behavior-changing instructions need an applicable trial or an explicit maintainer decision recording why validation remains pending. Translation-only changes can use a semantic comparison; they do not require a Blender render. Repeated failure in one asset does not establish a universal numeric threshold.

Provide evidence you can share, with relative links in the change record. Avoid private paths, account details, serial numbers and unlicensed reference files. Use concise reports/crops instead of committing large model libraries. Historical private trials shipped as summaries are not public reproduction evidence.

## How to write rules

- State the trigger, required outcome, verification and exceptions.
- Put shared requirements in SKILL.md; put conditional detail in a linked reference.
- Respect user scope and existing authorization; do not add repeated approval gates.
- Keep artist judgments and unconfirmed proposals distinguishable from measured constraints.
- Do not prescribe one asset's face count, smoothing angle, texture scale or rig mechanics for all assets.
- Keep installation/tool assumptions explicit. A dependency must not be described as bundled when it is not.

## Offline submissions

Send a ZIP containing the changed repository-relative files and the completed change record. List deleted/renamed files explicitly. Include the exact base version/commit; if unknown, state that so the maintainer can compare safely. Do not send only a replacement SKILL.md with no explanation. The maintainer imports the changes on a review branch rather than overwriting the maintained copy blindly.

## Maintainer review

Read the change record, inspect the actual diff, check rule scope and authority, inspect the evidence, resolve translation status, and run repository checks. Accept, request revisions or decline with a concrete reason. Keep unresolved artistic/functional limitations visible. Only the maintainer decides merge and release; issue and PR templates guide submissions but do not enforce branch protection by themselves.

## License

Submit contributions under this repository's [GPL-3.0-only license](LICENSE). Identify any third-party material and its terms before inclusion. Keep notices intact. Opening a PR does not transfer copyright ownership. See [NOTICE.md](NOTICE.md).
