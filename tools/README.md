# Tools

## lint.py
Wiki health check. Finds dead wikilinks, unsummarized raw sources, orphan pages (concepts/entities/syntheses), and low-confidence pages needing more sources.

```bash
python tools/lint.py
```

Pipe output to the LLM with `_prompts/lint-check.md` to update `wiki/_meta.md`.

## compile.py
Lists raw sources that don't yet have a `wiki/sources/` summary — your compile queue.

```bash
python tools/compile.py
```

## search.py
Naive full-text search over all wiki files. Use before writing a new concept to find related material.

```bash
python tools/search.py "attention transformer"
```
