---
type: portal
title: "Exposome research"
aliases: [exposome, urban exposome, exposomics]
tags: [portal]
created: 2026-11-15
updated: 2026-11-15
generated: true
reviewed: false
---

**Overview.** Entry point for research on the exposome, the totality of life-course non-genetic exposures ([[wild2005complementing]], p. 1848), including its social domain ([[gudimindermann2023integrating]], p. 1). Both sources in the vault so far are conceptual; there is no primary exposome evidence filed yet.

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
- Claude's reading: how to operationalize the social exposome dimension by dimension, and where green space quality and biodiversity sit in an urban exposome, are open in the vault ([[gudimindermann2023integrating]], p. 15–16).

## See also
- [[exposome]] · [[social-exposome]] · [[urban-green-space-quality]] · [[urban-nature-and-aging]]
- [[urban-environmental-hazards]]
