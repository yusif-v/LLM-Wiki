# Dashboard

Live queries powered by the [Dataview](https://github.com/blacksmithgu/obsidian-dataview) Obsidian plugin.

---

## Low Confidence Pages
Pages that need more sources or evidence.

```dataview
TABLE confidence, file.mtime AS "Updated"
FROM "wiki/concepts" OR "wiki/entities" OR "wiki/syntheses"
WHERE confidence = "low" OR confidence = "medium"
SORT confidence ASC, file.mtime ASC
```

---

## Recently Updated

```dataview
TABLE file.folder AS "Type", tags, file.mtime AS "Updated"
FROM "wiki/concepts" OR "wiki/entities" OR "wiki/syntheses" OR "wiki/sources"
SORT file.mtime DESC
LIMIT 15
```

---

## Pages with Most Sources

```dataview
TABLE length(sources) AS "Source count", tags
FROM "wiki/concepts" OR "wiki/entities"
SORT length(sources) DESC
LIMIT 10
```

---

## All Concepts

```dataview
TABLE summary, tags, confidence, file.mtime AS "Updated"
FROM "wiki/concepts"
SORT file.name ASC
```

---

## All Entities

```dataview
TABLE type, tags, file.mtime AS "Updated"
FROM "wiki/entities"
SORT file.name ASC
```

---

## Orphan Check
Pages with no incoming links — review and connect or delete.

```dataview
TABLE file.inlinks AS "Inbound links"
FROM "wiki/concepts" OR "wiki/entities" OR "wiki/syntheses"
WHERE length(file.inlinks) = 0
SORT file.name ASC
```
