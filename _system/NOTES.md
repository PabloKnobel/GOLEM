# NOTES (session handoff)

## Current state (2026-11-15)
- Live: Obsidian Sync ↔ VPS bridge ↔ GitHub (tested both ways). Vault has 22 papers (all read in full),
  35 findings, 25 concepts, 6 entities, 4 portals, 15 my-work pages.
- Scheduled tasks: daily ingest ~01:41 New York (all inbox items, commit per item, early exit if empty);
  weekly digest + lint Sundays 19:47 Berlin.
- Design doc: https://claude.ai/artifact/KMCdyr2Gu7NgcZZaWpexW8

## Decided
- Interface A (cloud Claude + VPS bridge); only Pablo's own + published material for now.
- Concept page for every main exposure/outcome; promotion at ≥5 mentions (any mention); co-first role;
  figure-only estimates via `estimate_in`; entity pages for datasets of active projects.

## Tried and rejected
- Creating GitHub repos from a Claude session (not allowed). WebFetch inside background agents (no approvals).
- CrossRef/OpenAlex from the shell: blocked until Pablo allows the domains.

## Open
1. Pablo: phone, Obsidian Sync file types (PDF + other), delete mine/Test From PC (only in Sync, not in repo), EndNote PDF location.
   Reported done 2026-11-15 (to confirm): Dataview, VPS hardening. Done: CrossRef/OpenAlex domains (verified reachable).
2. Next lint: create Barcelona Health Survey entity. Metadata of 22 papers verified 2026-11-15 (see log).
3. Sources with flagged inconsistencies: 12 papers carry `> [!uncertain]` callouts — Pablo to review.
4. Watch daily-run token use for the first week.
