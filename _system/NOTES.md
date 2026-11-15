# NOTES (session handoff)

## Current task
Setup of GOLEM (Pablo's steps in `_system/bridge/SETUP.md`, Parts A–D), then the RyC pilot.

## Done (2026-11-15)
- Design doc: https://claude.ai/artifact/KMCdyr2Gu7NgcZZaWpexW8 (decisions: interface A; own material only).
- Repo scaffold: schema (`CLAUDE.md`), templates, Home, RyC hub, green space quality portal.
- `_system/scripts/convert.py` tested on synthetic PDF/PPTX/RIS (incl. slide images, dedup).
- VPS bridge (`_system/bridge/`) tested locally with stubs: two-way mirror, conflict → alert + pause.
- Drive folder "Second Brain Inbox" (id `1LF3pYxJCMScIRXFXAdCKqeDg91zdceZS`).

## Tried and rejected
- Creating the GitHub repo from a Claude session: not allowed (sessions are bound to existing repos); Pablo created `GOLEM`.
- CrossRef/OpenAlex from the shell: blocked by the proxy until Pablo allows the domains (SETUP.md D1).

## Next
1. Pablo: SETUP.md Parts A–D; tell Claude where EndNote PDFs live.
2. Pilot step 2: file 5 core RyC papers together; tune templates and schema.
3. Then create scheduled tasks: nightly ingest, weekly digest + lint.
4. Before the full backlog: check Obsidian Sync and GitHub storage for original PDFs.
5. Untested: real `ob`/systemd on the VPS (SETUP B7), AgentMail email capture.
