---
type: portal
title: "Urban green space quality"
aliases: [green space quality, greenspace quality, park quality]
tags: [portal]
created: 2026-11-15
updated: 2026-11-15
generated: true
reviewed: false
---

**Overview.** Entry point for research on the quality (not only the amount) of urban green space and its links to health. This portal fills in as sources are ingested; nothing here is written from memory.

## Key concepts
```dataview
TABLE WITHOUT ID file.link AS Concept, kind AS Kind, length(file.inlinks) AS "Links in"
FROM "wiki/concepts"
WHERE contains(portals, this.file.link) OR contains(portals, this.file.name)
SORT length(file.inlinks) DESC
```

## Evidence at a glance
```dataview
TABLE WITHOUT ID file.link AS Finding, exposure AS Exposure, outcome AS Outcome, direction AS Direction, estimate AS Estimate, confidence AS Confidence
FROM "wiki/findings"
WHERE contains(portals, this.file.link) OR contains(portals, this.file.name)
SORT outcome ASC
```

## Key papers
```dataview
TABLE WITHOUT ID file.link AS Paper, year AS Year, design AS Design, fulltext AS "Full text"
FROM "wiki/papers"
WHERE contains(portals, this.file.link) OR contains(portals, this.file.name)
SORT year DESC
```

## Pablo's work in this field
```dataview
LIST FROM "wiki/my-work" WHERE contains(portals, this.file.link) OR contains(portals, this.file.name)
```

## Projects
- [[ryc-2026]]

## Open questions
- (Filled by Claude from the evidence; labeled as Claude's reading.)

## See also
