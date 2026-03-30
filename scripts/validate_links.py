from __future__ import annotations

import pathlib
import re
import sys

LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)|!\[[^\]]*\]\(([^)]+)\)")
IGNORED_PARTS = {".git", ".github", ".tools", "website", "__pycache__"}


def is_external_link(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#", "/"))


def validate_markdown_file(path: pathlib.Path, repo_root: pathlib.Path) -> list[str]:
    errors: list[str] = []
    content = path.read_text(encoding="utf-8")
    base_dir = path.parent

    for match in LINK_PATTERN.finditer(content):
        raw_target = match.group(1) or match.group(2) or ""
        target = raw_target.strip()

        if not target or is_external_link(target):
            continue

        clean_target = target.split("#", 1)[0].split("?", 1)[0]
        resolved = (base_dir / clean_target).resolve()

        try:
            resolved.relative_to(repo_root.resolve())
        except ValueError:
            errors.append(f"{path}: link escapes repository root -> {target}")
            continue

        if not resolved.exists():
            errors.append(f"{path}: missing local target -> {target}")

    return errors


def main() -> int:
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    markdown_files = sorted(
        path
        for path in repo_root.rglob("*.md")
        if not any(part in IGNORED_PARTS for part in path.relative_to(repo_root).parts)
    )

    all_errors: list[str] = []
    for md_file in markdown_files:
        all_errors.extend(validate_markdown_file(md_file, repo_root))

    if all_errors:
        print("Link validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(markdown_files)} Markdown files. No broken local links found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
