---
type: portal
title: "Urban environmental hazards (air pollution, noise, heat)"
aliases: [environmental hazards, air pollution and noise, urban environmental stressors]
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

**Overview.** Entry point for physical environmental hazards in cities: air pollution, environmental noise and ambient temperature. The vault's first evidence is a meta-analysis linking long-term residential noise to dementia ([[hwang2025comprehensive]]) and a multi-exposure cohort of PM2.5, NO2, temperature and children's HbA1c ([[wu2025air]]). Both argue that co-occurring exposures should be studied jointly ([[hwang2025comprehensive]], p. 8; [[wu2025air]], p. 2).

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
- Standardized noise exposure assessment and separation of noise from air pollution effects on dementia ([[hwang2025comprehensive]], p. 8–9).
- Why temperature–glycemia associations differ by climate and population ([[wu2025air]], p. 5).
- Claude's reading: how green space mitigation of noise and heat ([[markevych2017exploring]], p. 303–304) interacts with these hazards is not yet covered by primary evidence in the vault.

## See also
- [[environmental-noise]] · [[air-pollution]] · [[ambient-temperature]] · [[dementia]] · [[cardiometabolic-health]]
- [[exposome-research]] · [[urban-nature-and-aging]] · [[urban-green-space-quality]]
- [[differential-vulnerability]] · [[wtc-health-program]]
- [[multi-exposure-analysis]]
- Project hub: [[srtr-pm25-liver-transplant]]

