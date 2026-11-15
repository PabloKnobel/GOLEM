---
type: home
generated: true
---

# GOLEM

Pablo Knobel's knowledge base: papers, concepts, evidence and his own work, compiled by Claude and browsable like a wiki.

## Portals
```dataview
LIST WITHOUT ID file.link + " — " + length(file.inlinks) + " links in"
FROM "wiki/portals"
SORT file.name ASC
```

## Active projects
```dataview
TABLE WITHOUT ID file.link AS Project, status AS Status, deadline AS Deadline
FROM "wiki/projects"
WHERE status != "done"
SORT deadline ASC
```

## Recently added
```dataview
TABLE WITHOUT ID file.link AS Page, type AS Type, created AS Added
FROM "wiki"
SORT created DESC
LIMIT 15
```

## Latest digest
```dataview
LIST FROM "_system/digests" SORT file.name DESC LIMIT 1
```

## Random article
Use the core plugin **Random note** (command palette → "Open random note"), or ask Claude.

## How this vault works
- Drop anything in `00_inbox/`, the Drive folder **Second Brain Inbox**, or tell Claude "file this".
- Claude processes the inbox nightly; you review one weekly digest (under 20 minutes).
- Your own notes go in `mine/`; Claude never edits them. Inside a wiki page, write in a `> [!pablo]` block.
- Rules Claude follows: [[CLAUDE]].
