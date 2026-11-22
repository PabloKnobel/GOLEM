---
type: project
title: "R21 Birds and Aging"
aliases: ["R21 birds", "bird biodiversity R21", "PA-25-304"]
status: active
deadline:
portals: ["[[urban-nature-and-aging]]"]
tags: [project]
created: 2026-11-16
updated: 2026-11-16
projects: []
last_verified:
confidence:
superseded_by: ""
generated: true
reviewed: false
---

**Lead.** NIH R21 (PA-25-304) proposal linking residential bird biodiversity to frailty in older adults (65+) in NYC, through a soundscape pathway and a bioindicator pathway.

> [!pablo] Pablo's notes
> (Pablo writes here; Claude never edits this block.)

## Project notes
Source: Pablo, in Claude chats (2026); summary, re-verify before reuse.
- Data: MSHS EHR-linked cohort, citywide bird biodiversity model, and P30-funded acoustic fieldwork across NYC sites (2025).
- Primary outcome: frailty index.
- Status as last recorded (Oct 13, 2026): final review of the science sections done; pending EndNote reference fixes and a few checks.
- Research Strategy dated Oct 14, 2026, submitted: [[2026-grant-r21-birds-aging-science]] (added 2026-11-16).

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
