---
type: portal
title: "Urban nature and healthy aging"
aliases: [nature and aging, green space and aging, urban nature and aging]
tags: [portal]
created: 2026-11-15
updated: 2026-11-15
generated: true
reviewed: false
---

**Overview.** Entry point for research on how urban nature (greenness, quality, biodiversity) relates to aging outcomes such as frailty. The first longitudinal evidence in the vault comes from Pablo's own preprint on bird biodiversity and frailty ([[knobel2026residential]]).

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

## Open questions
- Why the bird diversity–frailty association fades after age 75; the authors propose reduced life-space mobility ([[knobel2026residential]], p. 10).

## See also
- [[urban-green-space-quality]]
