# Change: Add walkthrough video and first-time contributor guidance

- Base version / commit: 2026.09.011 / b12a623
- Author: brianchenanimator
- Date: 2026-09-23
- Type: packaging
- Affected rule IDs: N/A — no skill rule text changed.
- Changed / renamed / deleted files: README.md, README.zh-TW.md, docs/images/video-thumbnail.jpg (new)
- Status: proposed

## Problem

Two gaps in how the repository receives people. There was no moving explanation of what the skill does, only stills and prose. And "Improve blendsmith" described the contribution flow in one arrow-separated line, which assumes the reader already knows where Fork and Contribute live and offers nothing to someone who does not use Git.

## Before and after

Before: the showcase section opened with still images; the contribution section was a single flow line plus process requirements.

After: a linked video thumbnail opens the showcase section. The contribution section keeps that flow line and adds a "New to this?" paragraph naming the actual buttons (Fork, top right; Contribute, on the fork) and pointing non-Git contributors at the issue chooser, offline ZIP submissions and Discussions.

## Scope and exclusions

Presentation only. No instruction, requirement, budget or rule identifier changed, and `skill/blendsmith/` is untouched. The added paragraph restates where existing channels are; it does not create a new contribution path or relax any review requirement in CONTRIBUTING.md.

## Evidence and tests

- Document checks: `python scripts/validate.py` — PASS (26 Markdown files; the `CONTRIBUTING.md#offline-submissions` fragment resolves to a real heading).
- Discussions: enabled on the repository before merge so the new link resolves; `GET /discussions` returns 200. PASS.
- Thumbnail: `maxresdefault.jpg` for the linked video, 1280x720, 130 KB.
- Video content: NOT REVIEWED — the link and title come from the author; the README makes no claim about what the video demonstrates.
- Rendered README on GitHub: NOT RUN — verified locally only.

## Compatibility

No effect on briefs, budgets, rigs, tools or permissions. Adds 130 KB. The video and Discussions links are absolute URLs to this repository and its YouTube source, so they are outside `validate.py`'s local link checking; if the video is removed the thumbnail still renders but the link will 404.

## Language sync

English and Traditional Chinese READMEs received equivalent changes. The video title is quoted in English in both, matching the source. No skill instruction text changed.

## Limitations and feedback

The README does not state the video's spoken language, which would help non-Chinese-speaking readers decide whether to watch; the author should add it. Branch protection on `main` was discussed alongside this change but is not part of it and remains unconfigured. No reviewer or user feedback yet; this record is pending, not accepted.
