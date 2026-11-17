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
