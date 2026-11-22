---
type: project
title: "PM2.5 and liver transplant outcomes (SRTR)"
aliases: ["SRTR", "UNOS", "STAR files", "liver transplant waitlist", "StoS"]
status: active
deadline:
portals: ["[[urban-environmental-hazards]]"]
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

**Lead.** Long-term and acute PM2.5 and liver transplant outcomes using SRTR/UNOS STAR registry data: waitlist survival, graft failure and death after transplant.

> [!pablo] Pablo's notes
> (Pablo writes here; Claude never edits this block.)

## Project notes
Source: Pablo, in Claude chats (2026); summary, re-verify before reuse.
- Waitlist: causal framework with DAGs and competing risks (Fine-Gray).
- Post-transplant (student Grace): fixed-term 1-, 3- and 5-year outcomes.
- Aim 3a (student Hope): acute PM2.5 with a case-crossover DLNM.
- Registry data stay on Mount Sinai storage; nothing from them enters this vault.

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
