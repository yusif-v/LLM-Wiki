#!/usr/bin/env python3
"""
Incremental wiki compile runner.
Lists raw/ sources that have no matching wiki/sources/ entry — the compile queue.
"""
from pathlib import Path

BASE = Path(__file__).parent.parent
RAW_DIR = BASE / "raw"
SOURCES_DIR = BASE / "wiki" / "sources"


def slugify(name: str) -> str:
    return name.lower().replace(" ", "-")


def compile_queue():
    raw_files = list(RAW_DIR.rglob("*"))
    raw_files = [f for f in raw_files if f.is_file() and f.suffix in (".md", ".txt", ".pdf")]

    existing_summaries = {f.stem for f in SOURCES_DIR.glob("*.md")}

    queue = []
    for f in raw_files:
        slug = slugify(f.stem)
        if slug not in existing_summaries:
            queue.append(f)

    if not queue:
        print("All raw sources have wiki summaries. Nothing to compile.")
        return

    print(f"Sources awaiting compilation ({len(queue)}):")
    for f in queue:
        print(f"  {f.relative_to(BASE)}")


if __name__ == "__main__":
    compile_queue()
