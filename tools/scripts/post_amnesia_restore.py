"""Restore repository content from docs/survival_archive_full.md.

After the amnesia event, run this script to rebuild directories and files that
were archived pre-amnesia. It will recreate any file paths embedded in the
archive, skipping those that already exist to avoid overwriting new work unless
`--force` is supplied.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ARCHIVE_RELATIVE_PATH = Path("docs/survival_archive_full.md")
FILE_HEADER_PATTERN = re.compile(r"^## FILE: (?P<path>.+)$")


def iter_entries(archive_text: str):
    sections = archive_text.split("\n---\n")
    for section in sections:
        lines = [line.rstrip("\n") for line in section.splitlines()]
        if not lines:
            continue
        header_line = None
        content_lines: list[str] = []
        inside_block = False
        for line in lines:
            if line.startswith("## FILE: "):
                header_line = line
            elif line.strip() == "```" and not inside_block:
                inside_block = True
                content_lines = []
            elif line.strip() == "```" and inside_block:
                inside_block = False
            elif inside_block:
                content_lines.append(line)
        if not header_line:
            continue
        match = FILE_HEADER_PATTERN.match(header_line)
        if not match:
            continue
        rel_path = match.group("path")
        yield rel_path, "\n".join(content_lines) + "\n"


def restore(force: bool = False) -> list[Path]:
    base = Path(__file__).resolve().parents[2]
    archive_path = base / ARCHIVE_RELATIVE_PATH
    if not archive_path.exists():
        raise FileNotFoundError(f"Archive not found: {archive_path}")
    text = archive_path.read_text(encoding="utf-8")
    restored: list[Path] = []
    for rel_path, content in iter_entries(text):
        target = base / rel_path
        if target.exists() and not force:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        restored.append(target)
    return restored


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Restore files from archive")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files if they already exist.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    restored = restore(force=args.force)
    if restored:
        print("Restored files:")
        for path in restored:
            print(f" - {path.relative_to(Path.cwd())}")
    else:
        print("No files restored (files may already exist).")


if __name__ == "__main__":
    main()
