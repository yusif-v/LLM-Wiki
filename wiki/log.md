# Activity Log

Append-only record of every ingest, query, lint, and synthesis session.

**Format:** `## [YYYY-MM-DD HH:MM] <action> | <title>`  
**Action types:** `ingest` · `query` · `lint` · `synthesis` · `init`

Quick scan: `grep "^## " wiki/log.md | tail -10`

---

## [YYYY-MM-DD HH:MM] init | Knowledge base initialized

- **Pages created:** `_index.md`, `_meta.md`, `log.md`, `dashboard.md`, `flashcards.md`
- **Notes:** Ready to accept first source material.
