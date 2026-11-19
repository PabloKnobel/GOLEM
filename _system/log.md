---
type: log
generated: true
---

# Log

Append-only. One entry per operation, newest last. Prefixes: `ingest`, `query`, `lint`, `digest`, `setup`, `conflict`.
Format: `- YYYY-MM-DD HH:MM | prefix | summary | pages touched`

- 2026-11-15 | setup | vault scaffold created: schema, templates, Home, RyC hub, green space quality portal | CLAUDE.md, Home.md, wiki/projects/ryc-2026.md, wiki/portals/urban-green-space-quality.md
- 2026-11-15 | ingest | 3 items (knobel2026residential, kaplan1995restorative, nieuwenhuijsen2017fifty); 22 PDFs converted, 19 queued; 2 non-paper PDFs removed | 3 papers, 2 findings, 4 concepts, 1 entity, 1 portal, 1 my-work
- 2026-11-15 | ingest | 5 items (wild2005complementing, kennedy2014geroscience, crimmins2020social, gudimindermann2023integrating, markevych2017exploring); 5/5 full text read; metadata not verified (CrossRef WebFetch not approved); new portal exposome-research | 5 papers, 2 findings, 4 concepts (+3 updated), 1 entity, 1 portal (+2 updated)
- 2026-11-15 | ingest | 5 items (adewuyi2023health, knobel2021associations, hwang2025comprehensive, knobel2019systematic, wu2025air); 5/5 full text read; all Pablo-authored; metadata not verified (WebFetch unavailable); new portal urban-environmental-hazards; NDVI promoted from candidates | 5 papers, 10 findings, 9 concepts (+3 updated), 1 entity, 1 portal (+3 updated), 5 my-work
- 2026-11-15 | ingest | 5 items (knobel2024association, knobel2023socioeconomic, fernandeznunez2022gender, knobel2025social, knobel2021development); 5/5 full text read (references skipped); all Pablo-authored; metadata not verified (WebFetch not used); source inconsistencies flagged on all 5 paper pages; differential-vulnerability promoted from candidates | 5 papers, 10 findings, 3 concepts (+8 updated), 3 entities, 5 my-work, 4 portals updated
- 2026-11-15 | ingest | 4 items (fernandeznunez2022differences, knobel2026beyond, knobel2021quality, krasnov2026association); 4/4 full text read (references skipped); all Pablo-authored; metadata not verified (WebFetch not used); source inconsistencies flagged on all 4 paper pages; physical-activity, multi-exposure-analysis, social-cohesion promoted from candidates; new concepts atherosclerotic-cardiovascular-disease, green-space-use | 4 papers, 11 findings, 5 concepts (+8 updated), 3 entities updated, 4 my-work, 4 portals updated

## 2026-11-15 — metadata verification (CrossRef)
- Checked all 22 paper pages against CrossRef (22/22 found; OpenAlex reachable, not needed).
- Title, year, journal, DOI and author surnames matched for 22/22.
- Fixed from CrossRef: issue for fernandeznunez2022differences (6), kennedy2014geroscience (4), knobel2025social (2), also in APA lines;
  added volume/issue/pages fields to kaplan1995restorative and nieuwenhuijsen2017fifty (APA already correct).
- Kept "Yitshak Sade, M." on knobel2026residential (CrossRef splits it as "Sade, Maayan Yitshak").
- Format fix: `authors:` lists re-quoted one item per author on all 22 pages (unquoted lists made YAML/Dataview read each initial as an author);
  fixed invalid YAML (`exposures:` with %) on knobel2023socioeconomic. Template updated. 0/144 frontmatter blocks now invalid.
- Added `_system/scripts/verify_metadata.py`; set `metadata_checked: true` + `metadata_source` on all 22.

## 2026-11-16 — project hubs
- Added 8 project hubs (r01-urban-exposome-aging, r21-birds-aging, p30-nature-impairment, greenspace-quality-metric, nyc-bird-diversity, joint-habitability, srtr-pm25-liver-transplant, nyc-311-exposures) from Pablo's statements in chats; not chosen: Larramendi, HFSP, WOODEN-CARE, SIDIAP, Shojamblo, Federman talk, EHR course, M1 selective.
- Tagged existing papers: wild2005complementing → r01-urban-exposome-aging; gudimindermann2023integrating → r01-urban-exposome-aging; kennedy2014geroscience → r01-urban-exposome-aging; crimmins2020social → r01-urban-exposome-aging; knobel2025social → r01-urban-exposome-aging; knobel2026residential → r21-birds-aging, nyc-bird-diversity; knobel2021quality → p30-nature-impairment, greenspace-quality-metric; markevych2017exploring → p30-nature-impairment; knobel2019systematic → greenspace-quality-metric; knobel2021development → greenspace-quality-metric; knobel2021associations → greenspace-quality-metric.

## 2026-11-16 — ingest: 4 documents (chat upload)
- 4 my-work pages (R21 science, HEALS nature-impairment plan v5, HEALS 311 CVD LOI, P30 311 frailty Dec 2025); 2 entities (nhats, nyc-311-service-requests); hub notes appended for r21-birds-aging, p30-nature-impairment, nyc-311-exposures.
- Full text read: R21 science, HEALS plan v5, LOI (all); P30 PDF pp. 1–7 (cover, abstract, aims, research plan, budget table); budget justification and 5 biosketches (pp. 8–35) not read. No findings created (grant preliminary data, not papers).
- Open: R21 and LOI status unknown; HEALS v5 Aim 1 differs from Oct 29 plan.
- 2026-11-16 update from Pablo: R21 submitted; 311 CVD LOI not approved; HEALS plan v5 not current (marked superseded).
- 2026-11-17 | ingest | 1 item (fernando2026association); full text read; metadata verified (CrossRef); not Pablo-authored (Mount Sinai colleagues); 4 source inconsistencies flagged | 1 paper, 2 findings, 2 concepts updated, candidates
- 2026-11-17 | ingest | 1 item (Pablo's note: RyC impact ideas); quoted verbatim in a pablo callout on the RyC hub; no paper/my-work page (short note) | wiki/projects/ryc-2026.md
- 2026-11-17 | ingest | 1 item (ibanez2024neuroecological); full text read (PMC author manuscript); metadata verified (CrossRef); commentary, no findings; new concept one-health; life-course approach reached 5 mentions | 1 paper, 1 concept (+2 updated), candidates
- 2026-11-17 | ingest | 1 item (migeot2025social); full text read (references skipped); metadata verified (CrossRef); 3 source inconsistencies flagged | 1 paper, 2 findings, 2 concepts updated, candidates
- 2026-11-17 | ingest | 1 item (R01 Urban Exposome application, 141 pp.); science sections read in full (summary, aims, research strategy, timeline; PDF p. 7–8, 106–118, 123, 126, 133); forms, biosketches, budgets, letters not read; no findings (unpublished preliminary data); 4 internal inconsistencies flagged; new entity litcog | 1 my-work, 1 entity, project hub + exposome updated, candidates
- 2026-11-17 | ingest | 1 item (neufcourt2022assessing); full text read (references skipped); metadata verified (CrossRef); scoping review, no findings; 1 source inconsistency flagged. Run total: 6 items (fernando2026association, RyC note, ibanez2024neuroecological, migeot2025social, 2026-grant-r01-urban-exposome-aging, neufcourt2022assessing); backlog 0; Drive inbox empty | 1 paper, 2 concepts updated, candidates

## 2026-11-17 — ingest: RyC proposal v0.17 (chat upload)
- my-work [[2026-grant-ryc-continuum-proposal]] (full text read, §1–6 incl. budget; reference list not read); entities sidiap, redegi, icgc-orthophotos; note appended to ryc-2026 hub.
- 2026-11-17: ryc-2026 lead rewritten at Pablo's request (was: green-space quality surface; now CONTINUUM, dementia); SIDIAP project folded into ryc-2026 (Pablo).
- 2026-11-18 | ingest | 1 item (kareem2025role); full text read (4 pp.); metadata verified (CrossRef); not Pablo-authored; short narrative review, all claims secondhand, no findings; 5 source inconsistencies flagged (incl. possible author-name order) | 1 paper, 2 concepts updated (exposome, dementia), candidates
- 2026-11-18 | ingest | held 1 item in inbox ("Review these websites.md": Pablo's note listing 2 EU project sites, stage-healthyageing.eu and expanseproject.eu); web fetch needs approval that an unattended run cannot give; not ingested, no target project named. Backlog 1; Drive inbox empty
- 2026-11-18 | ingest | 1 item (Pablo's note "Review these websites": 2 EU projects as models for his future grants' language, style, content); websites fetched in chat (home, about, work packages, partners; per-WP pages not read); extractions saved to raw/web; note + Pablo's chat purpose quoted in pablo callouts | 2 entities (stage-project, expanse-project), 2 portals linked. Backlog 0 in GitHub; Pablo reports 2 PDFs in Obsidian inbox not yet mirrored (bridge last synced 2026-11-17 20:11 UTC)
- 2026-11-18 | ingest | 1 item (dehoogh2025europewide; Drive); full text read (supplement not read); metadata verified (CrossRef); not Pablo-authored; exposure-assessment paper, no exposure–outcome findings | 1 paper, 4 concepts updated (exposome, multi-exposure-analysis, ndvi, air-pollution), expanse-project entity, candidates
- 2026-11-18 | ingest | 1 item (hernandez2025exposome; Drive); main text, Methods and Extended Data legends read (references and supplement not read); metadata verified (CrossRef); not Pablo-authored; 4 source inconsistencies flagged; new concept biobehavioral-age-gap (main outcome) | 1 paper, 2 findings, 1 new concept, 2 concepts updated, candidates. Run total today: 4 items (kareem2025role, websites note, dehoogh2025europewide, hernandez2025exposome); backlog 0
- 2026-11-18 | network | built contacts/collaborators network: tables in _system/network/, network.py (seed-openalex, add-event, apply-review, sync, who), person + event templates, portal [[network]]; seeded from OpenAlex (41 works after excluding 1 misattributed 2001 dissertation; 2 works without DOI): 199 co-authors, 199 person pages, 346 links; 15 works linked to vault paper pages; 1 name match resolved (Alex Federman → alex-d-federman) | schema updated
- 2026-11-19 | ingest | 1 item (Pablo's note "Workshops i attended" embedding the 2nd IHEN Training School for Exposome Ambassadors program, Utrecht 16–20 Nov 2026; PDF recovered from git history after it was deleted from the vault root); program read in full (4 pp.); treated as network material (program) although not in a network/ subfolder | 1 event (ihen-exposome-training-school-2026), 24 trainers added to network tables (1 matched existing: kees-de-hoogh), sync
- 2026-11-19 | ingest | held 1 item in inbox ("Antoher example eu project.md": Pablo's note with one URL, humanexposome.net, likely another EU project model like the 2026-11-18 websites note); web fetch needs approval that an unattended run cannot give; not ingested
- 2026-11-19 | ingest | 1 item (ihen2026interim; IHEN interim roadmap for exposome research in Europe, 71 pp., report); full text read (reference lists skimmed); metadata not verified (no CrossRef record; OpenAlex rate-limited; year from file name) → metadata_checked: false + todo; not Pablo-authored; policy agenda, no findings; 2 internal inconsistencies flagged | 1 paper, 3 concepts updated (exposome, social-exposome, multi-exposure-analysis), event page linked, candidates
