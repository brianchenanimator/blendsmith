# Publish and maintain blendsmith

## Upload the source tree

1. Review README.md, README.zh-TW.md, LICENSE, NOTICE.md and the change record. The selected license is GPL-3.0-only.
2. Run `python scripts/validate.py`. Review the actual changes and any new public evidence.
3. Create a GitHub repository named `blendsmith` in the intended account. Choose Public when ready to make these files public.
4. Upload the contents of the blendsmith source directory, including `.github` and `.gitignore`. Do not upload the enclosing private project, backups, worklogs or just one ZIP as the entire source repository.
5. Confirm README rendering, Chinese navigation, files, template availability and the validation workflow. A local preparation check is not a GitHub execution result.
6. When approved, create a release/tag matching the version. An optional source ZIP can accompany the release; keep editable source files in the repository.

For repeated updates, GitHub Desktop or Git can maintain branches and show diffs before push. This package does not create a remote, authenticate, or publish automatically.

## Edit the introduction

Edit root README.md for the English homepage and README.zh-TW.md for its reading copy. Preview Markdown before committing. If adding images, place approved files under `docs/images/` and use repository-relative paths. No sample image directory or unlicensed promotional imagery is required.

## Review contributions

Use the PR's change record to identify base version, rule IDs, before/after behavior and test results, then inspect its actual diff. Request evidence or revision where needed. Resolve Chinese parity before release. Issue/PR templates are prompts, not access-control settings. Configure branch/ruleset protection separately in GitHub if desired and available for the repository.

Maintainers assign versions using `YYYY.MM.NNN` (CalVer): four-digit year, two-digit month (01–12) and a three-digit monthly sequence (001–999). Store the value as a quoted string so leading zeros survive. Current metadata is `2026.09.011`; use `v2026.09.011` for the GitHub tag/release and `blendsmith-v2026.09.011.zip` for the archive. The initial sequence 010 is a chosen starting label, not evidence of nine public releases. Increment the sequence for another release in the same month; start at 001 in a new month. If the sequence range is exhausted, agree a format revision before publishing.

These labels are not Semantic Versioning and do not communicate compatibility by themselves. Explain breaking and compatible changes explicitly. Synchronize current metadata, both language READMEs and the Chinese skill, prepend the changelog entry, and rebuild the archive. Preserve old release sections, base-version fields in historical change records, worklogs and backups. Do not globally replace every old version string.

## Official references

- [Create a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [Upload files](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- [About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Pull request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
- [Build/install skills](https://learn.chatgpt.com/docs/build-skills)
- [GNU GPL version 3](https://www.gnu.org/licenses/gpl-3.0.html)
