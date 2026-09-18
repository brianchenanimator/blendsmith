#!/usr/bin/env python3
"""Validate blendsmith's supported document conventions; not Blender assets.

Python 3.10+, standard library only. Run from any working directory.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def unfenced(text):
    return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)


def headings(text):
    found = set()
    counts = {}
    for line in unfenced(text).splitlines():
        if not re.match(r'^#{1,6} ', line):
            continue
        title = re.sub(r'^#+\s+', '', line).strip().lower()
        title = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
        number = counts.get(title, 0)
        counts[title] = number + 1
        found.add(title + (f'-{number}' if number else ''))
    return found


def validate(root):
    errors = []
    skill = root / 'skill/blendsmith'
    required = ['README.md', 'README.zh-TW.md', 'CONTRIBUTING.md', 'CHANGELOG.md',
                'LICENSE', 'NOTICE.md', 'AGENTS.md', 'changes/TEMPLATE.md',
                '.github/pull_request_template.md', '.github/workflows/validate.yml',
                'skill/blendsmith/SKILL.md', 'skill/blendsmith/SKILL.zh-TW.md',
                'skill/blendsmith/agents/openai.yaml', 'skill/blendsmith/LICENSE']
    for name in required:
        if not (root / name).is_file():
            errors.append(f'Missing file: {name}')
    if errors:
        return errors, 0
    en = (skill / 'SKILL.md').read_text(encoding='utf-8')
    zh = (skill / 'SKILL.zh-TW.md').read_text(encoding='utf-8')
    frontmatter = re.match(r'\A---\n(.*?)\n---\n', en, flags=re.S)
    if not frontmatter:
        errors.append('SKILL.md requires YAML frontmatter')
    for field in ['name: blendsmith', 'license: GPL-3.0-only']:
        if not frontmatter or field not in frontmatter[1].splitlines():
            errors.append(f'SKILL.md missing expected field: {field}')
    if not re.search(r'^description: .+', en, flags=re.M):
        errors.append('Missing skill description')
    version = re.search(r'^  version: "([0-9]{4}\.(?:0[1-9]|1[0-2])\.(?!000)[0-9]{3})"$', en, flags=re.M)
    if not version:
        errors.append('Expected quoted CalVer YYYY.MM.NNN (month 01–12, sequence 001–999)')
    else:
        v = version[1]
        for name in ['README.md', 'README.zh-TW.md', 'CHANGELOG.md', 'skill/blendsmith/SKILL.zh-TW.md']:
            if v not in (root / name).read_text(encoding='utf-8'):
                errors.append(f'Version {v} absent from {name}')
    for n in range(1, 12):
        rule = f'R{n:02}'
        if rule not in en or rule not in zh:
            errors.append(f'Rule missing from English or Chinese skill: {rule}')
    ui = (skill / 'agents/openai.yaml').read_text(encoding='utf-8')
    if '$blendsmith' not in ui or '$blender-production-assets' in ui:
        errors.append('UI invocation must use $blendsmith')
    short = re.search(r'^  short_description: "(.+)"$', ui, flags=re.M)
    if not short or not 25 <= len(short[1]) <= 64:
        errors.append('UI short description length must be 25–64 characters')
    license_data = (root / 'LICENSE').read_bytes()
    if license_data != (skill / 'LICENSE').read_bytes():
        errors.append('Installable skill license differs from repository license')
    if b'GNU GENERAL PUBLIC LICENSE' not in license_data or b'END OF TERMS AND CONDITIONS' not in license_data:
        errors.append('Complete GPL text not found')
    checked = 0
    for path in sorted(root.rglob('*.md')):
        if any(p in {'.git', 'worklog', 'backups'} for p in path.relative_to(root).parts):
            continue
        checked += 1
        text = path.read_text(encoding='utf-8')
        if re.search(r'\b[A-Za-z]:[/\\]', text):
            errors.append(f'Absolute Windows path in {path.relative_to(root)}')
        for match in re.finditer(r'!?\[[^\]\n]+\]\(([^)\n]+)\)', unfenced(text)):
            raw = match[1].strip().strip('<>')
            parts = urlsplit(raw)
            if parts.scheme or parts.netloc:
                continue  # Remote URLs are not network-tested here.
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path.resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(f'Link escapes package: {path.relative_to(root)} -> {raw}')
            elif not target.exists():
                errors.append(f'Broken link: {path.relative_to(root)} -> {raw}')
            elif parts.fragment and target.suffix.lower() == '.md':
                if unquote(parts.fragment) not in headings(target.read_text(encoding='utf-8')):
                    errors.append(f'Unknown heading: {path.relative_to(root)} -> {raw}')
    sections = ['Problem', 'Before and after', 'Scope and exclusions', 'Evidence and tests',
                'Compatibility', 'Language sync', 'Limitations and feedback']
    for path in (root / 'changes').glob('*.md'):
        if path.name == 'TEMPLATE.md':
            continue
        text = path.read_text(encoding='utf-8')
        for section in sections:
            if f'## {section}' not in text:
                errors.append(f'{path.name}: missing section {section}')
        for field in ['Base version / commit', 'Affected rule IDs', 'Changed / renamed / deleted files']:
            if not re.search(r'^- ' + re.escape(field) + r':\s*\S', text, flags=re.M):
                errors.append(f'{path.name}: missing value {field}')
    return errors, checked


if __name__ == '__main__':
    repo = Path(__file__).resolve().parents[1]
    problems, count = validate(repo)
    if problems:
        print('\n'.join('FAIL: ' + item for item in problems))
        sys.exit(1)
    print(f'PASS: {count} Markdown files; required files, naming, versions, rule IDs, local links, license copies and change records.')
    print('Scope: document/package checks only; remote URLs, full YAML semantics and Blender behavior are not tested.')
