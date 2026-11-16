---
type: project
title: "Joint habitability: biodiversity and human wellbeing"
aliases: ["habitability project", "biodiversity and wellbeing", "nature habitability"]
status: active
deadline:
portals: ["[[urban-nature-and-aging]]"]
tags: [project]
created: 2026-11-16
updated: 2026-11-16
generated: true
reviewed: false
---

**Lead.** Student-led project Pablo supervises: whether places more habitable for nature (biodiversity from eBird and iNaturalist) are also more habitable for people (CDC PLACES wellbeing), across US counties.

> [!pablo] Pablo's notes
> (Pablo writes here; Claude never edits this block.)

## Project notes
Source: Pablo, in Claude chats (2026); summary, re-verify before reuse.
- Joint habitability framing (nature and human habitability as co-outcomes); county unit; three aims (typology, shared spatial structure, drivers).
- Student paper; no aging-specific outcomes.
- Analysis plan: https://claude.ai/artifact/Ur73dCnQNdGiK8quoit5vg

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
