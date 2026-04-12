# Flashcards

Spaced repetition cards for the [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) Obsidian plugin.

**Format:** question, then `?` on its own line, then answer. Separate cards with a blank line.

Ask the LLM to generate cards from any wiki page:
> "Generate flashcards from [[concepts/concept-name]]"

---

## Cards

What are the three core operations of the LLM Wiki pattern?
?
**Ingest** — process a raw source into wiki pages with cross-links. **Query** — answer questions against the wiki with citations; file good answers back as syntheses. **Lint** — health-check for dead links, orphans, contradictions, and gaps.

What is the difference between a concept and an entity in this wiki?
?
**Concepts** are abstract ideas, techniques, patterns, or mechanisms (e.g. "attention mechanism", "RAG"). **Entities** are specific named things: people, papers, tools, models, or companies (e.g. "Andrej Karpathy", "GPT-4").

What do the three confidence levels mean?
?
**High** — well-established, multiple corroborating sources. **Medium** — supported but limited examples or single source. **Low** — speculative, anecdotal, or single mention.

What is the purpose of wiki/log.md?
?
Append-only chronological record of every ingest, query, lint, and synthesis session. Gives a timeline of the wiki's evolution and helps the LLM understand what's been done recently.
