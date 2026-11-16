---
type: project
title: "P30 pilot: Out of Reach? (nature and impairment)"
aliases: ["Out of Reach", "HEALS pilot", "P30 pilot", "P30 Nature Impairment", "P30 idea"]
status: active
deadline:
portals: ["[[urban-nature-and-aging]]", "[[urban-green-space-quality]]"]
tags: [project]
created: 2026-11-16
updated: 2026-11-16
generated: true
reviewed: false
---

**Lead.** HEALS × Pepper Center pilot (19th call) on how impairment (vision, hearing, mobility, cognition) shapes older adults' use and benefits of urban nature, using NHATS; LOI approved (Oct 2026); building toward an R01.

> [!pablo] Pablo's notes
> (Pablo writes here; Claude never edits this block.)

## Project notes
Source: Pablo, in Claude chats (2026); summary, re-verify before reuse.
- Exposures: NDVI, park access (ParkServe 10-minute walk) and the park quality layer as a qgcomp index, built with Mount Sinai's GREENER platform.
- Aim 1: GEE with event study (exploratory). Aim 2: mortality.
- NHATS restricted files requested only after notice of award; public files meanwhile; HRS as alternative.
- Research plan v5: Aim 1 = going-out frequency (survey-weighted GEE, no event study); Aim 2 = mortality (Cox); NHATS Rounds 1–14 excluding Round 10: [[2026-grant-heals-nature-impairment-plan]] (added 2026-11-16). Not the current plan (Pablo, 2026-11-16); current version not yet in the vault.

## Papers tagged to this project
```dataview
TABLE WITHOUT ID file.link AS Paper, year AS Year, design AS Design, fulltext AS "Full text"
FROM "wiki/papers"
WHERE contains(projects, this.file.link) OR contains(projects, this.file.name)
SORT year DESC
```

## Findings
```dataview
TABLE WITHOUT ID file.link AS Finding, exposure AS Exposure, outcome AS Outcome, estimate AS Estimate, confidence AS Confidence
FROM "wiki/findings"
WHERE contains(projects, this.file.link) OR contains(projects, this.file.name)
```

## Concepts
```dataview
LIST FROM "wiki/concepts" WHERE contains(projects, this.file.link) OR contains(projects, this.file.name)
```

## My past material
```dataview
LIST FROM "wiki/my-work" WHERE contains(projects, this.file.link) OR contains(projects, this.file.name)
```

## Reference list (APA)
```dataview
LIST WITHOUT ID apa FROM "wiki/papers"
WHERE (contains(projects, this.file.link) OR contains(projects, this.file.name)) AND apa
SORT apa ASC
```
