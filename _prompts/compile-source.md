# Prompt: Compile a raw source into wiki

You are maintaining a personal knowledge base wiki stored as Markdown files in an Obsidian vault.

## Task
Given the raw source document below, do the following:
1. Write a `wiki/sources/<slug>.md` summary file (200-400 words).
2. Identify which existing `wiki/concepts/*.md` and `wiki/entities/*.md` files this source links to. Add backlinks.
3. Identify concepts and entities NOT yet in the wiki that this source introduces. Create them.
4. Update `wiki/_index.md` — add rows to the Sources, Concepts, and Entities tables as needed.
5. Append an entry to `wiki/log.md`.

## Format for `wiki/sources/<slug>.md`

```markdown
# <Title>
**Source type:** article | paper | repo | dataset  
**Original:** <url or path>  
**Date ingested:** <date>

## Summary
<3-5 paragraph summary>

## Key points
- ...

## Concepts referenced
- [[concept-name]]

## Entities referenced
- [[entity-name]]

## Quotes / notable extracts
> ...
```

## Format for `wiki/concepts/<slug>.md`

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
- [[related-concept]] — explanation
- [[related-entity]] — explanation

## Sources
- [[sources/slug]] — what this source contributes

## Gaps
- _(topics not yet covered)_
```

## Format for `wiki/entities/<slug>.md`

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
- [[concept-name]] — relationship
- [[entity-name]] — relationship

## Sources
- [[sources/slug]]
```

## Source document
<paste raw content here>
