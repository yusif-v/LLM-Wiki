# Prompt: Compile a raw source into wiki

You are maintaining a personal knowledge base wiki stored as Markdown files in an Obsidian vault.

## Task
Given the raw source document below, do the following:
1. Write a `wiki/sources/<slug>.md` summary file (200-400 words).
2. Identify which existing `wiki/concepts/*.md` files this source links to. Add backlinks.
3. Identify any concepts NOT yet in the wiki that this source introduces. List them for new article creation.
4. Update `wiki/_index.md` — add a row to the Sources table.

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
- [[concept-name-2]]

## Quotes / notable extracts
> ...
```

## Source document
<paste raw content here>
