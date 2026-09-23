# Change: Add README showcase images, logo and sponsor button

- Base version / commit: 2026.09.011 / dbb673a01777e4340f5c08342d0f4044e6bc075b
- Author: brianchenanimator
- Date: 2026-09-23
- Type: packaging
- Affected rule IDs: N/A — no skill rule text changed; the new section cites R01–R03 and R10 as captions only.
- Changed / renamed / deleted files: README.md, README.zh-TW.md, .gitattributes, .github/FUNDING.yml (new), docs/images/ (new: logo.png, social-preview.png, bottle-high-low.png, foldable-high-low.png, uv-and-shader.png, rig-cap.gif, rig-fold.gif)
- Status: proposed

## Problem

The repository presented the skill in text only. A reader could not see what a blendsmith handoff actually looks like before installing it, and the project had no way to accept support from users.

## Before and after

Before: README opened with a heading and prose; no images existed in the repository.

After: a logo appears above the heading, and a new "What it looks like" / "實際成果" section between the introduction and "What it covers" shows five captioned exhibits — high/low mesh pairs, the UV atlas beside the shader graph, and two Pose Mode rig clips. Each caption names the rule it illustrates. `.github/FUNDING.yml` adds a Buy Me a Coffee sponsor button.

## Scope and exclusions

Presentation and repository packaging only. No instruction, requirement, budget or rule identifier was modified, and `skill/blendsmith/` is untouched. The images are illustrations from this project's own trials; they are not acceptance criteria and set no numeric targets for other assets.

## Evidence and tests

- Environment: Windows 11, ffmpeg 8.0.1, Pillow 12.0.0.
- Document checks: `python scripts/validate.py` — PASS (25 Markdown files; all new image links resolve).
- Source media: 2304x1440 30fps MP4 captures, converted to 800x500 12fps GIF with a per-frame diff palette and Bayer dithering. Undithered output showed visible banding on screen gradients; `sierra2_4a` matched Bayer visually at ~30% larger size, so Bayer was kept.
- Rendered README appearance on GitHub: NOT RUN — verified locally only; confirm after merge.
- Social preview card: NOT RUN — `docs/images/social-preview.png` still has to be uploaded manually under Settings → General → Social preview; committing the file does not activate it.
- Sponsor button live state: NOT RUN — confirm after merge that the Sponsor button resolves.

## Compatibility

No effect on briefs, budgets, rigs, tools or permissions. Adds ~5.1 MB of images to the repository, of which `rig-cap.gif` is 2.67 MB. `.gitattributes` gains explicit `binary` rules for image and video extensions so `* text=auto` cannot corrupt them; this only affects files added from now on.

## Language sync

English and Traditional Chinese READMEs both received the logo and an equivalent showcase section with translated captions. No skill instruction text changed, so `SKILL.md` and `SKILL.zh-TW.md` needed no update.

## Limitations and feedback

An earlier draft of `docs/images/uv-and-shader.png` read "UV and Chader Editor"; the author corrected the artwork to "Shader" and the image was replaced before merge. The GIFs are silent, unnarrated and show a single asset each, so they illustrate the workflow without establishing reproducible evidence. No reviewer or user feedback yet; this record is pending, not accepted.
