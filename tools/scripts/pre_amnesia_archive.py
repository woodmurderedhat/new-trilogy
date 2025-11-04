"""Pre-amnesia archival utility.

Collects markdown, text, and json files from narrative directories and stores
them inside docs/survival_archive_full.md so the story survives when other
folders are purged. Safe to rerun; overwrites the archive each time.
"""
from __future__ import annotations

from pathlib import Path


INCLUDE_PATHS = [
    "README.md",
    "COMMIT_MESSAGE.md",
    "book1_fragmented-city",
    "book2_echo-machine",
    "book3_reentry",
    "scenes",
    "meta",
    "exports",
]

ALLOWED_EXTENSIONS = {".md", ".txt", ".json"}

HEADER = """# Survival Archive Full Dump
Generated pre-amnesia: preserve narrative data outside tools/manifesto/docs.

> This file captures every markdown/text/json artifact from directories
> scheduled for deletion. If you are reading this post-amnesia, you can
> reconstruct the repository using the embedded content.
"""


def collect_files(base: Path) -> list[Path]:
    collected: list[Path] = []
    for pattern in INCLUDE_PATHS:
        target = base / pattern
        if not target.exists():
            continue
        if target.is_file():
            collected.append(target)
            continue
        for path in sorted(target.rglob("*")):
            if path.is_file() and path.suffix.lower() in ALLOWED_EXTENSIONS:
                collected.append(path)
    return collected


def write_archive(base: Path, files: list[Path]) -> Path:
    archive = base / "docs" / "survival_archive_full.md"
    archive.parent.mkdir(parents=True, exist_ok=True)
    with archive.open("w", encoding="utf-8") as fh:
        fh.write(HEADER)
        for file_path in files:
            rel = file_path.relative_to(base)
            fh.write("\n---\n\n")
            fh.write(f"## FILE: {rel.as_posix()}\n\n")
            fh.write("```\n")
            text = file_path.read_text(encoding="utf-8")
            fh.write(text)
            if not text.endswith("\n"):
                fh.write("\n")
            fh.write("```\n")
    return archive


def main() -> None:
    base = Path(__file__).resolve().parents[2]
    files = collect_files(base)
    archive_path = write_archive(base, files)
    print(f"Archive created at: {archive_path}")
    print(f"Files captured: {len(files)}")


if __name__ == "__main__":
    main()
