---
type: project
title: "NYC 311 exposure layers"
aliases: ["311 project", "311"]
status: active
deadline:
portals: ["[[urban-environmental-hazards]]", "[[exposome-research]]"]
tags: [project]
created: 2026-11-16
updated: 2026-11-16
generated: true
reviewed: false
---

**Lead.** Building exposure metrics from NYC 311 administrative complaint data (for example, rodent requests mapped per building or tax lot), as an example of new exposures from existing administrative data.

> [!pablo] Pablo's notes
> (Pablo writes here; Claude never edits this block.)

## Project notes
Source: Pablo's documents (see links).
- Dec 2025 P30 pilot on 311 and frailty: [[2025-grant-p30-311-frailty]]. Latest version (Oct 2026 LOI, resubmission) switches to cardiovascular disease, chronic and acute: [[2026-loi-heals-311-cvd]] (added 2026-11-16). LOI not approved (Pablo, 2026-11-16).

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
