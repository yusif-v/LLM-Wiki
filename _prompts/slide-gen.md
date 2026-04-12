# Prompt: Generate a slide deck

You are generating a Marp-compatible Markdown slide deck from wiki content.

## Task
Create a slide deck at `outputs/slides/<slug>.md` on the topic: **{{TOPIC}}**

Draw from relevant `wiki/concepts/` and `wiki/maps/` articles. Cite sources where appropriate.

## Marp format

```markdown
---
marp: true
theme: default
paginate: true
---

# <Title>

---

## Slide Title

- Bullet point
- Bullet point

> Quote or key stat

---
```

## Guidelines
- 10–20 slides
- One key idea per slide
- Use `[[wiki-links]]` in speaker notes (not visible on slides)
- Final slide: "Further Reading" linking to relevant wiki articles

## Topic
{{TOPIC}}

## Relevant wiki files to draw from
<list or paste content>
