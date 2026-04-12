# Prompt: Write an entity page

You are writing an entity page for a personal knowledge base wiki stored in an Obsidian vault.

Entities are **specific named things**: people, papers, tools, models, companies — as opposed to concepts (abstract ideas).

## Task
Write `wiki/entities/<entity-name>.md` for: **{{ENTITY}}**

Use only information from the sources listed below. Note gaps where sources don't cover something.

## Format

```markdown
---
title: <Entity Name>
type: entity
entity_type: person | paper | tool | model | company
tags: [tag1, tag2]
confidence: high | medium | low
sources: [[[sources/slug]]]
updated: <date>
---

# <Entity Name>

> One-sentence description.

## Overview
<1-2 paragraphs>

## Key facts
- ...

## Related
- [[concept-name]] — how this entity connects to the concept
- [[entity-name]] — relationship between entities

## Sources
- [[sources/slug]] — what this source contributes

## Gaps
- _(what isn't covered yet)_
```

## Relevant sources
<list source summaries or paste content>
