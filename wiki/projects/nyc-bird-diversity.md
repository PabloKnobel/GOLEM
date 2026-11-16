---
type: project
title: "NYC bird diversity (VAFI)"
aliases: ["VAFI", "eBird NYC", "nyc_tract_year_latent_shannon", "acoustic bird survey"]
status: active
deadline:
portals: ["[[urban-nature-and-aging]]"]
tags: [project]
created: 2026-11-16
updated: 2026-11-16
generated: true
reviewed: false
---

**Lead.** Spatiotemporal GAM-based latent Shannon diversity of birds from eBird for NYC census tracts by year, plus an acoustic recorder survey run with a collaborator.

> [!pablo] Pablo's notes
> (Pablo writes here; Claude never edits this block.)

## Project notes
Source: Pablo, in Claude chats (2026); summary, re-verify before reuse.
- Model integrates air quality components and urban nature metrics; validated with temporal hold-out.
- Acoustic survey: recorders in 100 m grid cells; health analyses limited to cross-sectional use given sparse coverage.
- Feeds [[r21-birds-aging]].

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
