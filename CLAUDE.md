# Second Brain — schema

Operating manual for Claude. Read this file first, every session. Keep it under 200 lines;
move overflow to `_system/schema-archive.md`.

Owner: Pablo Knobel (geospatial/environmental epidemiologist). The vault is a personal,
Wikipedia-like knowledge base that Claude compiles and maintains; Pablo browses it in Obsidian.

## 1. Jobs, in priority order
1. Recall: "what's the evidence on X→Y?", "where did I see…?", "how did I frame this before?"
2. Feed writing (grants, papers): evidence tables, reference lists, past framing.
3. Synthesize new literature into concepts and findings; flag contradictions.
4. Reuse Pablo's own material (decks, talks, grants, papers).

## 2. Hard rules (never break)
- No PHI or identifiable data, ever. No peer-review materials (manuscripts or grants received as a
  reviewer). If an inbox item looks like either: do not ingest, move it to `00_inbox/_rejected/`, flag it in the digest.
- For now, only Pablo's own material and published/public sources. No collaborators' or students'
  unpublished drafts until he says so. If unsure whose a draft is: hold in inbox, ask in the digest.
- Never edit `mine/` or `raw/` content. Never edit text inside a block marked `> [!pablo]`.
- Append, don't rewrite. Add new information; do not reword existing prose. Restate, never "improve".
  Restructuring a page happens only in the weekly lint, in one batched pass, and is logged.
- Pages with `reviewed: true` are append-only.
- Contradictions: never overwrite. Keep both claims, add a `> [!contradiction]` callout with both
  sources, and link the pages through `contradicts:`.
- Every factual claim in `wiki/` carries a source link: `([[paper-key]], p. N)` or `([[paper-key]], Table 2)`.
- Evidence gating: a source with `fulltext: abstract` or `fulltext: blocked` may be summarized on its
  own paper page, but cannot be the only support for a claim on a concept, finding or portal page.
- Never invent numbers, citations, DOIs, page numbers or quotes. Unknown → write `?` and flag it.
- English everywhere. Keep short original-language quotes (Spanish/Catalan) only for key terms.
- US spelling. Citations in APA 7.
- Confidence language: "X found…", "one study suggests…", "consistent across N studies…" (match the evidence).

## 3. Zones and ownership
| Folder | Owner | Content |
|---|---|---|
| `00_inbox/` | Pablo + capture routes | Anything to process. Claude empties it. |
| `raw/` | Claude writes once, never edits | Originals + text versions, by type: `papers/ decks/ docs/ web/ notes/` |
| `wiki/` | Claude | Compiled articles (see §4) |
| `mine/` | Pablo only | His own thinking. Claude may read and link to it, never write. |
| `_system/` | Claude | index, log, digests, templates, scripts |
| `Home.md` | Claude (structure) | Front page |

## 4. Page types (templates in `_system/templates/`)
| Type | Folder | Key | One page per |
|---|---|---|---|
| portal | `wiki/portals/` | topic slug | research field (entry point) |
| concept | `wiki/concepts/` | concept slug | concept, theory, measure, method |
| paper | `wiki/papers/` | citekey | source (paper, report, book chapter) |
| finding | `wiki/findings/` | `exposure--outcome--citekey` | key estimate from one paper |
| entity | `wiki/entities/` | slug | person, dataset, place, instrument, organization |
| project | `wiki/projects/` | project slug | Pablo's project (hub) |
| my-work | `wiki/my-work/` | `YYYY-type-slug` | one of Pablo's decks, talks, grants, papers |
| synthesis | `wiki/syntheses/` | question slug | a saved answer to a good question |

Every wiki page starts with frontmatter (fields per template), then:
1. **Lead**: 1–3 sentences that answer "what is this and why it matters" (Wikipedia-style lead).
2. Body sections per template.
3. `## See also` (typed links) and `## References` (APA list of cited paper pages).

Common frontmatter on every wiki page:
`type, aliases, tags, projects, portals, created, updated, last_verified, confidence (high|medium|low),
generated: true, reviewed: false, superseded_by`.

## 5. Keys, names and duplicates
- Citekey = first author's surname (lowercase, ASCII) + year + first content word of title,
  e.g. `markevych2017exploring`. Collisions: add `b`, `c`. DOI stored in `doi:`.
- Slugs: lowercase, hyphens, no dates (except my-work). File name = slug. Title in frontmatter `title:`.
- Before creating any page: search titles, `aliases:` and `_system/index.md` for the concept/entity.
  Same thing under another name → add an alias to the existing page, don't create a new one.
- A concept gets its own page only when mentioned on ≥5 pages, or when Pablo asks. Until then it is
  a bullet in the nearest concept/portal page and is listed in `_system/candidates.md` with its count.
- Entities: people only if they are authors Pablo cites often or collaborators he names; no private details.

## 6. Links
- Wikilinks `[[slug]]` in prose, like Wikipedia links. Link only where understanding A changes how
  you read B. Max ~5 new links per page per ingest.
- Typed relations go in frontmatter lists (for queries) and in `## See also`:
  `supports, contradicts, replicates, extends, uses_dataset, uses_method, part_of`.
- Every page must have at least one inbound link (portal, project hub or concept). Orphans → lint.

## 7. Operations
### Ingest (nightly, or "ingest now")
0. `git pull`. Read this file, `_system/index.md`, last 30 lines of `_system/log.md`.
1. List `00_inbox/` and the Drive folder "Second Brain Inbox" (id `1LF3pYxJCMScIRXFXAdCKqeDg91zdceZS`);
   download Drive items into `00_inbox/`, then move them to a "processed" subfolder in Drive. Process at most 10 items per run;
   oldest first. Leave the rest; the backlog count goes in the log.
2. Per item: screen (§2 hard rules) → convert with `_system/scripts/convert.py` → save original +
   `.md` text in `raw/<type>/` → record sha256 in `_system/manifest.csv`.
   Same hash already in manifest → skip as duplicate.
3. Read the full text. Create/update the source page (paper or my-work) from its template.
   Set `fulltext:` honestly (read = whole text read; abstract; blocked).
4. Check existing pages (§5), then add: findings (key estimates only, ≤5 per paper), concept
   bullets/updates (append, cited), entity mentions, project and portal membership.
5. Verify paper metadata (authors, year, title, journal, DOI) against CrossRef/OpenAlex if reachable;
   mismatch → fix from the authoritative record and note it; unreachable → `metadata_checked: false`.
6. Update `_system/index.md` (one line per new page) and append to `_system/log.md`.
7. Mark the manifest row `done` only if the wiki changed. Commit: `ingest: <n> items (<citekeys>)`. Push.
### Query (chat)
- Read `_system/index.md` first, then search (`grep -ril`, titles, aliases, frontmatter), then read pages.
- Answer with citations to wiki pages and their sources; say what the vault doesn't cover.
- Distinguish: evidence (papers), Pablo's framing (my-work, mine/), and Claude's synthesis.
- A useful answer → offer to save it as a synthesis page. Never file without saying so.
### Lint + digest (weekly)
- Checks: orphans, dead links, duplicate pages/aliases, missing frontmatter, uncited claims,
  abstract-only sources supporting concept claims, contradictions across pages, stale `last_verified`
  (>12 months), concepts in `candidates.md` that reached 5 mentions, manifest rows not done.
- Batched consolidation: restructure at most 5 pages per week, log each, keep all citations.
- Write `_system/digests/YYYY-MM-DD.md` from the digest template. Must be readable in <20 minutes.
- Monthly (first digest of the month): cross-month contradiction sweep; reminder to export EndNote.

## 8. Formats and conversion
- `convert.py` handles PDF (pymupdf4llm; OCR fallback), PPTX (text + notes + slide images),
  DOCX (pandoc), HTML/MD/TXT (pass-through). Images of slides go to `raw/decks/<slug>/`.
- EndNote exports (`.ris`, `.xml`, `.txt` RIS) in the inbox → create/update paper stubs
  (`fulltext: none` until a PDF arrives); store `endnote_id` if present. Never write to EndNote.
- Web clips: keep the URL in `source_url`; date accessed in `accessed`.

## 9. Callouts used
`> [!contradiction]`, `> [!uncertain]` (low confidence; goes to digest), `> [!pablo]` (Pablo's own
words inside a wiki page; never edit), `> [!todo]` (missing PDF, missing page number, etc.).

## 10. Git
- Work only on `main`. `git pull --rebase` before writing; small commits; never force-push.
- Never commit `.obsidian/` (Obsidian Sync handles settings). Never commit secrets.
- The VPS bridge mirrors this repo ↔ Obsidian Sync every 5 minutes. Merge conflict → stop,
  write `_system/CONFLICT.md` describing it, and flag it in the next digest.
