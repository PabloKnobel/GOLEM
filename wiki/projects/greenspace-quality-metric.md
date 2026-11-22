---
type: project
title: "Greenspace quality metric (CONUS)"
aliases: ["GreenSpace_CNN", "green space quality metric", "Mapping Urban Green Space Quality across the Continental U.S.", "GECC pilot"]
status: active
deadline:
portals: ["[[urban-green-space-quality]]"]
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

**Lead.** Satellite imagery (NAIP) and convolutional neural networks scoring 10 park-quality submetrics on 300 × 300 m tiles across the continental US; funded as a GECC pilot.

> [!pablo] Pablo's notes
> (Pablo writes here; Claude never edits this block.)

## Project notes
Source: Pablo, in Claude chats (2026); summary, re-verify before reuse.
- Training: ~8,000 NAIP tiles rated by MPH students; national prediction layer ready (Oct 2026); no composite score.
- Methods/validation manuscript in preparation (target: Nature Cities).
- Methods extension planned for the RyC application ([[ryc-2026]]) and an R01.

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
