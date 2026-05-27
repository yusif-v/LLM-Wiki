# Prompt: Wiki health check

You are auditing a personal knowledge base wiki stored as Markdown files in an Obsidian vault.

## Task
Scan all files in `wiki/` and `raw/` and audit for the following issues:

1. **Dead links** — `[[links]]` that don't resolve to an existing file
2. **Unsummarized sources** — files in `raw/` with no matching `wiki/sources/` entry
3. **Orphan concepts** — concept articles with no backlinks from other articles
4. **Inconsistencies** — contradictory claims across articles (check dates, numbers, definitions)
5. **Gaps** — concepts mentioned in articles but with no dedicated article
6. **Connection opportunities** — two articles that discuss the same theme but don't link each other

## Output
Update `wiki/_meta.md` with:
- A new health score (0–10)
- Updated open gaps list
- Updated suggested new articles list
- Interesting cross-links found

Be specific — name the files and the exact issues found.
