---
type: portal
title: "Urban green space quality"
aliases: [green space quality, greenspace quality, park quality]
tags: [portal]
created: 2026-11-15
updated: 2026-11-22
projects: []
portals: []
last_verified:
confidence:
superseded_by: ""
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
- Standardized green space quality assessment (aesthetics, biodiversity, walkability, facilities, safety, events) is still missing in epidemiologic studies ([[nieuwenhuijsen2017fifty]], p. 69).
- Pathway-specific exposure metrics, and data on quality, access and use rather than presence alone, are recommended; candidates include Sentinel-2, street view imagery with deep learning, and species richness ([[markevych2017exploring]], p. 306, 309, 311).
- No standardized definition of urban green space or study units across audit tools, which limits replicability and comparability ([[knobel2019systematic]], p. 4, 6).
- Perceived access correlated weakly with objective greenness (r = 0.12–0.32) yet showed stronger associations with cardiometabolic outcomes ([[knobel2021associations]], p. 4, 6).

## See also
- [[green-space-health-pathways]] · [[exposome-research]]
- [[green-space-quality-assessment]] · [[ndvi]] · [[perceived-green-space-access]] · [[green-prescription]]
- [[sex-and-gender-effect-modification]] · [[recital]]
- [[physical-activity]] · [[green-space-use]] · [[atherosclerotic-cardiovascular-disease]]
- [[perceived-safety-in-green-space]] · [[barcelona-health-survey]] · [[blue-space]]

