# Prompt: Write a concept article

You are writing an article for a personal knowledge base wiki stored in an Obsidian vault.

## Task
Write `wiki/concepts/<concept-name>.md` for the concept: **{{CONCEPT}}**

Use only information from the sources listed below. Where the sources don't cover something, note it as a gap. Set confidence based on source coverage: `high` (multiple sources, concrete examples), `medium` (single source or limited examples), `low` (speculative or one mention).

## Format

```markdown
---
title: <Concept Name>
type: concept
tags: [tag1, tag2]
confidence: high | medium | low
sources: [[[sources/slug]]]
updated: <date>
---

# <Concept Name>

> One-sentence definition.

## Overview
<2-3 paragraphs>

## Key ideas
- ...

## How it relates to
- [[related-concept]] — explanation of relationship
- [[related-entity]] — explanation of relationship

## Sources
- [[sources/source-slug]] — what this source contributes

## Gaps
- _(topics not yet covered by available sources)_
```

## Relevant sources
<list source summaries or paste content>
