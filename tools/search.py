#!/usr/bin/env python3
"""Naive full-text search over the wiki. Used as an LLM tool via CLI."""
import sys
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent / "wiki"


def search(query: str, top_n: int = 10):
    terms = query.lower().split()
    results = []
    for md in WIKI_DIR.rglob("*.md"):
        text = md.read_text(errors="ignore").lower()
        score = sum(text.count(t) for t in terms)
        if score > 0:
            title = next(
                (l.strip("# \n") for l in md.read_text().splitlines() if l.strip()),
                md.stem,
            )
            results.append((score, str(md.relative_to(WIKI_DIR.parent)), title))
    results.sort(reverse=True)
    for score, path, title in results[:top_n]:
        print(f"[{score:>4}] {path}  —  {title}")


if __name__ == "__main__":
    q = " ".join(sys.argv[1:])
    if not q:
        print("Usage: search.py <query terms>")
        sys.exit(1)
    search(q)
