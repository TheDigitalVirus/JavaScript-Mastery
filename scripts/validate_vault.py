#!/usr/bin/env python3
"""Validate the JavaScript Mastery Obsidian vault.

This script is intentionally dependency-free so it can run anywhere Python 3 is
available. It checks for unresolved Git conflicts, Markdown/frontmatter issues,
Canvas JSON validity, and Spaced Repetition flashcard discoverability.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFLICT_MARKER_RE = re.compile(r"^(<<<<<<<|=======|>>>>>>>)", re.MULTILINE)
OLD_FLASHCARD_TAG_RE = re.compile(r"(?<!s)#flashcard(?!s)(?:\s|$)")
INLINE_CARD_SPACE_RE = re.compile(r"(?m)^[^\n]+?::\s+")
TRAILING_WHITESPACE_RE = re.compile(r"(?m)[ \t]+$")


def run_git(args: list[str]) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def tracked_and_untracked_files() -> list[Path]:
    files = set(run_git(["ls-files"]).splitlines())
    status = run_git(["status", "--porcelain"]).splitlines()
    for line in status:
        if line.startswith("?? "):
            files.add(line[3:])
    return sorted(ROOT / file for file in files if file)


def frontmatter(text: str, path: Path, errors: list[str]) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append(f"Unclosed frontmatter: {path.relative_to(ROOT)}")
        return ""
    return text[4:end]


def main() -> int:
    errors: list[str] = []

    unmerged = run_git(["ls-files", "-u"]).strip()
    if unmerged:
        errors.append("Git index has unresolved merge entries:\n" + unmerged)

    files = tracked_and_untracked_files()
    markdown_files = [p for p in files if p.suffix == ".md"]
    canvas_files = [p for p in files if p.suffix == ".canvas"]

    for path in markdown_files + canvas_files:
        text = path.read_text(encoding="utf-8")
        if CONFLICT_MARKER_RE.search(text):
            errors.append(f"Conflict marker found: {path.relative_to(ROOT)}")

    for path in canvas_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # pragma: no cover - human-facing validation
            errors.append(f"Invalid Canvas JSON in {path.relative_to(ROOT)}: {exc}")

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if text.count("```") % 2:
            errors.append(f"Unbalanced Markdown code fences: {rel}")
        if TRAILING_WHITESPACE_RE.search(text):
            errors.append(f"Trailing whitespace found: {rel}")
        fm = frontmatter(text, path, errors)
        if OLD_FLASHCARD_TAG_RE.search(text):
            errors.append(f"Old singular #flashcard tag remains: {rel}")
        if INLINE_CARD_SPACE_RE.search(text):
            errors.append(f"Inline flashcard must use Pergunta::Resposta without spaces after separator: {rel}")

        is_flashcard_source = path.parts[-2:-1] == ("Flashcards",) or "01 - Variáveis e Strings" in path.parts
        if is_flashcard_source and "::" in text:
            if "#flashcards" not in text:
                errors.append(f"Missing inline #flashcards deck tag: {rel}")
            if fm and "  - flashcards" not in fm:
                errors.append(f"Missing YAML flashcards tag: {rel}")

        if "01 - Variáveis e Strings" in path.parts and "## Flashcards" in text:
            if fm and "  - review" not in fm:
                errors.append(f"Missing review tag for note-review queue: {rel}")

    if errors:
        print("Vault validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Vault validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
