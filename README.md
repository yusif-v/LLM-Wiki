# LLM Wiki

A personal knowledge base template maintained collaboratively with an AI coding agent, inspired by [Andrej Karpathy's LLM Wiki concept](https://x.com/karpathy/status/1756380066580455557). Drop raw sources in, let the agent compile them into a structured, interlinked wiki — then query, synthesize, and explore.

Model-agnostic: works with any agent that reads `AGENTS.md` ([Claude Code](https://claude.ai/code), [Codex](https://github.com/openai/codex), [Gemini CLI](https://github.com/google-gemini/gemini-cli), etc.).

## How it works

1. **Drop** raw content (articles, papers, repos, datasets) into `raw/`
2. **The agent compiles** each source into a summary, extracts concepts and entities, and links them together
3. **The source is consumed** — moved from `raw/` to `archive/`, so `raw/` always shows exactly what's still unprocessed
4. **Query** the wiki with natural language; the agent answers from the structured content
5. **Health-check** with `python tools/lint.py` to catch dead links, orphans, missing index entries, and gaps

The wiki lives in plain Markdown, works great in [Obsidian](https://obsidian.md) (with Dataview for live queries), and is fully readable in any editor.

---

## Vault structure

```
raw/
  articles/       ← blog posts, essays, web pages
  papers/         ← academic papers, PDFs
  repos/          ← code repositories, READMEs
  datasets/       ← structured data, CSVs
  images/         ← screenshots, diagrams, figures

archive/          ← consumed originals, moved here after ingestion (keeps provenance)

wiki/
  _index.md       ← master index: ALL content listed here
  _meta.md        ← health score, open gaps, suggestions
  log.md          ← append-only activity log
  dashboard.md    ← Dataview live queries (Obsidian)
  flashcards.md   ← spaced repetition cards
  sources/        ← one .md per raw source (summaries)
  concepts/       ← abstract ideas, techniques, patterns
  entities/       ← specific things: people, papers, tools, companies
  syntheses/      ← comparisons and cross-concept analyses
  maps/           ← thematic overviews / MOCs

outputs/
  queries/        ← saved research question answers
  slides/         ← generated slide decks

tools/            ← Python CLI scripts
prompts/        ← reusable prompt templates for the agent
AGENTS.md       ← agent instructions
```

---

## Getting started

### Prerequisites

- An AI coding agent that reads `AGENTS.md` — [Claude Code](https://claude.ai/code), [Codex](https://github.com/openai/codex), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Cursor](https://cursor.sh), etc.
- Python 3.10+ (for the tools)
- Obsidian (optional, for Dataview dashboard)

### Setup

```bash
git clone https://github.com/<you>/LLM-Wiki
cd LLM-Wiki
```

No dependencies to install — the Python tools use only the standard library.

### Quick start

```bash
python tools/start.py
```

Detects installed AI agents on your system (Claude Code, Codex, Gemini CLI, Cursor, Aider, OpenCode) and launches your pick in the project directory.

---

## Core workflows

### Add a new source

1. Drop the file into the right `raw/` subfolder, named as a lowercase-hyphenated slug:
   ```
   raw/papers/attention-is-all-you-need.pdf
   raw/articles/the-bitter-lesson.md
   ```

2. Open your agent and run:
   ```
   compile wiki/sources/<slug>.md from raw/papers/attention-is-all-you-need.pdf
   ```
   The agent will use `prompts/compile-source.md` to write the source summary, create or update any concept/entity pages, update `_index.md`, move the original to `archive/` (the **consume** step), and append to `log.md`.

> **Lifecycle:** inbox (`raw/`) → ingest (summarize + link) → consumed (`archive/`). `raw/` holds only unprocessed files, so `python tools/compile.py` is always a true to-do list.

### Answer a research question

```
using prompts/qa-query.md, answer: "What is the difference between MoE and dense models?"
```

The agent reads the wiki and writes the answer to `outputs/queries/<slug>.md`. If the answer is worth keeping, it can be promoted to a synthesis page.

### Write a concept, entity, or synthesis

Use the corresponding prompt:
- `prompts/write-concept.md` → `wiki/concepts/<name>.md`
- `prompts/write-entity.md` → `wiki/entities/<name>.md`
- `prompts/write-synthesis.md` → `wiki/syntheses/<name>.md`

### Health check

```bash
python tools/lint.py
```

Reports dead wikilinks, unsummarized sources, orphan pages, pages missing from `_index.md`, and low-confidence pages. Pipe the output to the agent with `prompts/lint-check.md` to auto-update `wiki/_meta.md`.

### Search

```bash
python tools/search.py "attention transformer"
```

Full-text search across all wiki files — useful before writing a new concept to find related material.

### Check compile queue

```bash
python tools/compile.py
```

Lists raw files that don't yet have a corresponding `wiki/sources/` summary. Because consumed files are moved to `archive/`, this is exactly the set of sources still waiting to be ingested.

---

## Prompt templates

| Template | Purpose |
|----------|---------|
| `prompts/compile-source.md` | Compile a raw file into wiki pages |
| `prompts/write-concept.md` | Write a new concept article |
| `prompts/write-entity.md` | Write a new entity page |
| `prompts/write-synthesis.md` | Write a comparison / synthesis |
| `prompts/qa-query.md` | Answer a research question from the wiki |
| `prompts/lint-check.md` | Interpret lint output and update `_meta.md` |
| `prompts/slide-gen.md` | Generate a slide deck from wiki content |

---

## Wiki conventions

- **Wikilinks** — all internal references use `[[wikilinks]]`, never bare file paths
- **Confidence levels** — every concept, entity, and synthesis page carries a `confidence` field: `high` (multiple corroborating sources), `medium` (single source), or `low` (speculative)
- **Activity log** — `wiki/log.md` is append-only; every ingest, consume, query, and lint session gets an entry: `## [YYYY-MM-DD HH:MM] <action> | <title>`
- **Consume every source** — after a summary is written, the original moves from `raw/` to `archive/`; `raw/` never holds processed files
- **No hallucinated sources** — the agent only cites `[[sources/slug]]` files that actually exist in `wiki/sources/`

---

## Obsidian setup (optional)

Open the repo root as an Obsidian vault. Install the [Dataview](https://github.com/blacksmithgu/obsidian-dataview) plugin to get live queries in `wiki/dashboard.md`:

- Low-confidence pages needing more sources
- Recently updated pages
- Pages ranked by source count
- Orphan check (pages with no incoming links)

---

## Tips

- **Name files as slugs** — lowercase, hyphen-separated (e.g. `attention-is-all-you-need.pdf`). The tools derive wiki slugs directly from filenames.
- **Read `_index.md` first** — the agent is instructed to always start here, so keeping it accurate makes every query faster and more reliable.
- **Promote good query answers** — if a `outputs/queries/` answer is evergreen, move it to `wiki/syntheses/` so it gets indexed and linked.
- **Run lint regularly** — a health score of 8+/10 means the graph is well-connected and low-confidence pages are rare.

---

## Credits

Concept by [Andrej Karpathy](https://x.com/karpathy). Template designed for any AGENTS.md-compatible coding agent.
