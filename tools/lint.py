#!/usr/bin/env python3
"""
Wiki health check — finds dead links, orphans, unsummarized sources, and gaps.
Prints a report; does NOT write to _meta.md (pipe output to the LLM to update it).
"""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
WIKI_DIR = BASE / "wiki"
RAW_DIR = BASE / "raw"
SOURCES_DIR = WIKI_DIR / "sources"
CONCEPTS_DIR = WIKI_DIR / "concepts"
ENTITIES_DIR = WIKI_DIR / "entities"
SYNTHESES_DIR = WIKI_DIR / "syntheses"

LINK_RE = re.compile(r"\[\[([^\]|#]+)")


def slugify(name: str) -> str:
    return name.lower().replace(" ", "-")


def all_wiki_stems() -> set[str]:
    return {f.stem for f in WIKI_DIR.rglob("*.md")}


def check_dead_links():
    stems = all_wiki_stems()
    issues = []
    for md in WIKI_DIR.rglob("*.md"):
        text = md.read_text(errors="ignore")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip().split("/")[-1]
            if target not in stems:
                issues.append(f"  {md.relative_to(BASE)}: [[{match.group(1)}]]")
    return issues


def check_unsummarized_sources():
    raw_files = [f for f in RAW_DIR.rglob("*") if f.is_file() and f.suffix in (".md", ".txt", ".pdf")]
    summarized = {f.stem for f in SOURCES_DIR.glob("*.md")}
    return [str(f.relative_to(BASE)) for f in raw_files if slugify(f.stem) not in summarized]


def check_orphans():
    all_text = ""
    for md in WIKI_DIR.rglob("*.md"):
        all_text += md.read_text(errors="ignore")
    orphans = []
    for directory, label in [(CONCEPTS_DIR, "concepts"), (ENTITIES_DIR, "entities"), (SYNTHESES_DIR, "syntheses")]:
        for page in directory.glob("*.md"):
            if f"[[{label}/{page.stem}]]" not in all_text and f"[[{page.stem}]]" not in all_text:
                orphans.append(str(page.relative_to(BASE)))
    return orphans


def check_low_confidence():
    issues = []
    conf_re = re.compile(r"confidence:\s*(low)", re.IGNORECASE)
    for directory in [CONCEPTS_DIR, ENTITIES_DIR, SYNTHESES_DIR]:
        for md in directory.glob("*.md"):
            text = md.read_text(errors="ignore")
            if conf_re.search(text):
                issues.append(f"  {md.relative_to(BASE)}")
    return issues


def main():
    print("=== Wiki Lint Report ===\n")

    dead = check_dead_links()
    print(f"Dead links ({len(dead)}):")
    for d in dead or ["  none"]:
        print(d)

    unsummarized = check_unsummarized_sources()
    print(f"\nUnsummarized sources ({len(unsummarized)}):")
    for u in unsummarized or ["  none"]:
        print(f"  {u}")

    orphans = check_orphans()
    print(f"\nOrphan pages ({len(orphans)}):")
    for o in orphans or ["  none"]:
        print(f"  {o}")

    low_conf = check_low_confidence()
    print(f"\nLow confidence pages ({len(low_conf)}):")
    for l in low_conf or ["  none"]:
        print(l)

    total_issues = len(dead) + len(unsummarized) + len(orphans) + len(low_conf)
    score = max(0, 10 - total_issues)
    print(f"\nHealth score: {score}/10  (issues found: {total_issues})")


if __name__ == "__main__":
    main()
