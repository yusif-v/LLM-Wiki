# Agent Instructions — LLM Wiki Template

This is a personal knowledge base maintained collaboratively with an AI coding agent, based on the LLM Wiki pattern by Andrej Karpathy.

## Vault structure

```
raw/          ← inbox: unprocessed sources only (must stay empty of consumed files)
  articles/   ← blog posts, essays, web pages
  papers/     ← academic papers, PDFs
  repos/      ← code repositories, READMEs
  datasets/   ← structured data, CSVs
  images/     ← screenshots, diagrams, figures
archive/      ← consumed originals, moved here after ingestion (keeps provenance)
wiki/         ← LLM-maintained wiki
  _index.md   ← master index: ALL content listed here
  _meta.md    ← health score, open gaps, suggestions
  log.md      ← append-only activity log (every ingest, query, lint)
  dashboard.md← Dataview live queries (Obsidian)
  flashcards.md← spaced repetition cards
  sources/    ← one .md per raw source (summaries)
  concepts/   ← abstract ideas, techniques, patterns
  entities/   ← specific things: people, papers, tools, companies
  syntheses/  ← comparisons and cross-concept analyses
  maps/       ← thematic overviews / MOCs
outputs/      ← generated content (queries, slides, charts)
tools/        ← Python CLI scripts
prompts/      ← reusable prompt templates
```

## Rules

1. **Always read `wiki/_index.md` first** before answering any question — it is your map of the entire wiki.
2. **Never hallucinate sources.** Only cite `[[sources/slug]]` files that exist in `wiki/sources/`.
3. **Keep `_index.md` current.** After adding any page, update the relevant table row. `_index.md` is the graph's fan-in point: `python tools/lint.py` flags any page missing from it, so keep it accurate.
4. **Use `[[wikilinks]]`** for all internal references — never bare file paths.
5. **Flag gaps explicitly.** If the wiki doesn't cover something relevant, say so rather than guessing.
6. **Set confidence levels.** Every concept, entity, and synthesis page must have a `confidence` field: `high` (multiple corroborating sources), `medium` (single source or limited examples), `low` (speculative or one mention).
7. **Append to `wiki/log.md`** after every ingest, consume, query, or lint session. Format: `## [YYYY-MM-DD HH:MM] <action> | <title>`.
8. **Run `python tools/lint.py`** after bulk compile sessions and update `wiki/_meta.md` with results.
9. **Consume every source.** After writing its summary, move the raw file from `raw/` to `archive/` and update the summary's `**Original:**` path. `raw/` must be empty of consumed files — it is the inbox, `archive/` is the archive.
10. **`_index.md` is single-writer shared state.** When many pages are being created in one session, the same agent that starts the session owns `_index.md` updates — never leave it half-updated between turns, and reconcile it before finishing.

## Content types

| Type | Directory | Use for |
|------|-----------|---------|
| Source summary | `wiki/sources/` | Every file ingested from `raw/` |
| Concept | `wiki/concepts/` | Abstract ideas, techniques, patterns, mechanisms |
| Entity | `wiki/entities/` | Specific named things: people, papers, tools, models, companies |
| Synthesis | `wiki/syntheses/` | Comparisons, trade-off analyses, cross-concept insights |
| Map | `wiki/maps/` | Thematic overviews linking many concepts together |

## Standard workflows

### Add a new source
1. Drop file into appropriate `raw/` subfolder (`articles/`, `papers/`, `repos/`, `datasets/`, `images/`)
   - Name the file in lowercase-hyphenated slug form, e.g. `attention-is-all-you-need.pdf`
2. Use `prompts/compile-source.md` → write `wiki/sources/<slug>.md`
3. Create or update any `concepts/`, `entities/` pages introduced
4. Update `wiki/_index.md` Sources table
5. **Consume the source**: move the raw file from `raw/` to `archive/`, update the summary's `**Original:**` path
6. Append entry to `wiki/log.md`

### Write a new concept article
1. Check `python tools/search.py "<concept>"` for related material
2. Use `prompts/write-concept.md` → write `wiki/concepts/<name>.md`
3. Update `wiki/_index.md` Concepts table

### Write a new entity page
1. Use `prompts/write-entity.md` → write `wiki/entities/<name>.md`
2. Update `wiki/_index.md` Entities table

### Write a synthesis
1. Use `prompts/write-synthesis.md` → write `wiki/syntheses/<name>.md`
2. Update `wiki/_index.md` Syntheses table

### Answer a research question
1. Read `wiki/_index.md`
2. Use `prompts/qa-query.md` → write answer to `outputs/queries/<slug>.md`
3. If the answer is valuable, file it back as a synthesis page

### Generate slides
1. Use `prompts/slide-gen.md` → write to `outputs/slides/<slug>.md`

### Health check
1. Run `python tools/lint.py`
2. Use `prompts/lint-check.md` to interpret results
3. Update `wiki/_meta.md`
4. Append lint entry to `wiki/log.md`

## Coordination (when working in parallel or in batches)

The wiki is a graph: pages are nodes, wikilinks are edges. Keep the graph healthy under concurrency.

- **Design the shape of the work first.** If two ingest tasks produce no shared pages, they are independent — process them in parallel. If both write to the same concept/entity page, run them sequentially (or have one agent do both) to avoid clobbering each other.
- **`_index.md` is the shared-state choke point.** Only the session's owning agent updates it; leaf pages (`sources/`, `concepts/`, `entities/`, `syntheses/`) can be written freely. Reconcile `_index.md` in one pass at the end of the session.
- **Verify expected counts before finishing.** After a batch, run `python tools/compile.py` — every file you ingested must be gone from the queue (moved to `archive/`), and `python tools/lint.py` must show every page indexed. Never silently finish with partial output.
- **Layer large fan-ins.** When a synthesis draws on many sources, summarize in batches of 20–50 and consolidate the batch summaries — don't try to hold every source in context at once.
