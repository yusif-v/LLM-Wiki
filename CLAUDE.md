# Claude Code Instructions — LLM Wiki Template

This is a personal knowledge base maintained collaboratively with Claude Code, based on the LLM Wiki pattern by Andrej Karpathy.

## Vault structure

```
raw/
  articles/   ← blog posts, essays, web pages
  papers/     ← academic papers, PDFs
  repos/      ← code repositories, READMEs
  datasets/   ← structured data, CSVs
  images/     ← screenshots, diagrams, figures
wiki/         ← LLM-maintained wiki
  _index.md   ← master index: ALL sources and concepts listed here
  _meta.md    ← health score, open gaps, suggestions
  concepts/   ← one .md per concept
  sources/    ← one .md per raw source (summaries)
  maps/       ← thematic overviews / MOCs
outputs/      ← generated content (queries, slides, charts)
tools/        ← Python CLI scripts
_prompts/     ← reusable prompt templates
```

## Rules

1. **Always read `wiki/_index.md` first** before answering any question — it is your map of the entire wiki.
2. **Never hallucinate sources.** Only cite `[[sources/slug]]` files that exist in `wiki/sources/`.
3. **Keep `_index.md` current.** After adding any source summary or concept article, update the relevant table row.
4. **Use `[[wikilinks]]`** for all internal references — never bare file paths.
5. **Flag gaps explicitly.** If the wiki doesn't cover something relevant, say so rather than guessing.
6. **Run `python tools/lint.py`** after bulk compile sessions and update `wiki/_meta.md` with results.

## Standard workflows

### Add a new source
1. Drop file into appropriate `raw/` subfolder (`articles/`, `papers/`, `repos/`, `datasets/`, `images/`)
   - Name the file in lowercase-hyphenated slug form, e.g. `attention-is-all-you-need.pdf`
2. Use `_prompts/compile-source.md` → write `wiki/sources/<slug>.md`
3. Update `wiki/_index.md` Sources table

### Write a new concept article
1. Check `python tools/search.py "<concept>"` for related material
2. Use `_prompts/write-concept.md` → write `wiki/concepts/<name>.md`
3. Update `wiki/_index.md` Concepts table

### Answer a research question
1. Read `wiki/_index.md`
2. Use `_prompts/qa-query.md` → write answer to `outputs/queries/<slug>.md`

### Generate slides
1. Use `_prompts/slide-gen.md` → write to `outputs/slides/<slug>.md`

### Health check
1. Run `python tools/lint.py`
2. Use `_prompts/lint-check.md` to interpret results
3. Update `wiki/_meta.md`
