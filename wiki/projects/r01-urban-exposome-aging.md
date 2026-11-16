---
type: project
title: "R01 Urban Exposome and Healthy Aging (URBE-Aging)"
aliases: ["URBE-Aging", "Urban Aging", "urban exposome grant", "R01 exposome-aging"]
status: active
deadline:
portals: ["[[exposome-research]]", "[[urban-nature-and-aging]]"]
tags: [project]
created: 2026-11-16
updated: 2026-11-16
generated: true
reviewed: false
---

**Lead.** Multi-site NIH R01 (with a parallel ERC version) on how the urban exposome (built, social and ambient environment) shapes healthy aging across biological, physical, cognitive, psychological and social domains.

> [!pablo] Pablo's notes
> (Pablo writes here; Claude never edits this block.)

## Project notes
Source: Pablo, in Claude chats (2026); summary, re-verify before reuse.
- Cohorts: Mount Sinai Health System EHR cohort (NYC) and LitCog (Chicago, 6 waves).
- Aims: (1) ExWAS and quantile g-computation in the MSHS cohort (PhenoAge acceleration, VA Frailty Index); (2) BVCKMR in LitCog (physical, cognitive, psychological, social wellbeing); (3) exploratory, association-based scenario projections with ensemble machine learning.
- ERC version: name URBE-Aging; panel LS7 primary, SH7 secondary.
- Status as last recorded (Sep 2026): R01 at or near submission; ERC version in development. Re-verify.

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
