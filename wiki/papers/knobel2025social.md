---
type: paper
title: "Social vulnerability and biological aging in New York City: An electronic health records-based study"
citekey: knobel2025social
aliases: [Knobel 2025, SVI PhenoAge NYC, social vulnerability biological aging]
authors: ["Knobel, P.", "Colicino, E.", "Kloog, I.", "Litke, R.", "Lane, K.", "Federman, A.", "Mobbs, C.", "Yitshak Sade, M."]
year: 2025
journal: "Journal of Urban Health"
volume: 102
issue: "2"
pages: "240–249"
doi: "10.1007/s11524-024-00948-7"
endnote_id: ""
apa: "Knobel, P., Colicino, E., Kloog, I., Litke, R., Lane, K., Federman, A., Mobbs, C., & Yitshak Sade, M. (2025). Social vulnerability and biological aging in New York City: An electronic health records-based study. Journal of Urban Health, 102(2), 240–249. https://doi.org/10.1007/s11524-024-00948-7"
fulltext: read
metadata_checked: true
metadata_source: "CrossRef, 2026-11-15"
metadata_note: "issue filled from CrossRef (2)"
design: retrospective EHR cohort (person-years)
population: "31,913 patients ≥65 y, 116,952 person-years, Mount Sinai Health System"
setting: "New York City, 2011–2022"
n: 31913
exposures: [CDC Social Vulnerability Index, four themes (mixture)]
outcomes: ["[[phenotypic-age]]"]
methods: [quantile g-computation, qgcompint interaction, predictive mean matching imputation, cluster bootstrap]
datasets: ["[[mount-sinai-data-warehouse]]", CDC/ATSDR SVI]
supports: []
contradicts: []
replicates: []
extends: []
projects: []
portals: ["[[urban-nature-and-aging]]", "[[exposome-research]]"]
authored_by_pablo: true
tags: [paper, my-paper, cohort, ehr, mixtures, effect-modification, aging]
created: 2026-11-15
updated: 2026-11-15
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** In 31,913 adults ≥65 y in Mount Sinai EHR data (2011–2022), a decile increase in all four census-tract SVI themes was associated with +0.23 years phenotypic age acceleration (95% CI 0.21, 0.25), driven mainly by the socioeconomic status theme (61% of weight) ([[knobel2025social]], p. 243). Associations were larger in women and in racial and ethnic minority groups (p. 244). Pablo is first and corresponding author.

> [!todo] Metadata to verify
> Not checked against CrossRef (WebFetch not used in this batch). Issue not printed: `?`. Published online January 14, 2025 (p. 240).

> [!uncertain] Internal inconsistencies in the source
> - PhenoAgeAccel is defined in Methods as "the differential between chronological age and PhenoAge" with positive = accelerated aging (p. 242), while the abstract says "between PhenoAge and chronological age" (p. 240). Positive = accelerated implies PhenoAge − chronological age.
> - The weakest correlation is reported as "0.10 for household characteristics and household type and transportation", mixing theme names (p. 243).

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| EHR cohort, qGcomp (p. 242–243) | 31,913 (116,952 person-years) | NYC adults ≥65, MSHS, 2011–2022 | SVI four themes, per decile (mixture) | PhenoAgeAccel (years) | +0.23 (0.21, 0.25) | Sex, race and ethnicity, insurance, year indicator |
| Same, by sex | Same | Same | Same | Same | Women +0.27 (0.25, 0.29); men +0.13 (0.10, 0.16) | Same |
| Same, by race/ethnicity | Same | Same | Same | Same | Other groups +0.34 (0.32, 0.36); non-Hispanic White +0.12 (0.09, 0.15) | Same |

## Key points
- Exposure: CDC SVI by census tract, four themes (socioeconomic status; household composition and disability; minority status and language; housing and transportation), linked annually by last address (p. 241–242).
- Outcome: PhenoAge from Levine's formula, with yearly averaged albumin, creatinine, glucose, MCV, alkaline phosphatase, RDW, WBC; CRP (90.83%) and lymphocyte % (24.06%) imputed by PMM (p. 242). See [[phenotypic-age]].
- Exclusions: missing race/ethnicity 8.1%, insurance 4.0%, address 1.4%, biomarkers 65.8% of person-years (p. 242).
- Sample: mean age 70.21, 34.1% male, 43.8% White, 25.8% Hispanic, 16.0% Black (p. 243, Table 1).
- Overall: +0.23 years per decile; weights: SES 61%, then household composition and minority status; housing and transportation "insubstantial protective" (p. 243, Fig. 1) → [[social-vulnerability--phenotypic-age-acceleration--knobel2025social]].
- By sex: women driven by SES (71%); men by minority status (43%), SES (29%), household (27%) (p. 244) → [[social-vulnerability--phenotypic-age-acceleration--knobel2025social-by-sex]].
- By race/ethnicity: non-Hispanic White driven by minority status (55%); other groups by SES (61%) (p. 244) → [[social-vulnerability--phenotypic-age-acceleration--knobel2025social-by-race-ethnicity]].
- Sensitivity: complete-lab subset (5,853 participants, 8,670 person-years) very similar; participant- and tract-cluster bootstrap 0.23 (0.19, 0.27) and 0.23 (0.19, 0.26) (p. 244).
- Authors' limitations: selection from non-routine biomarkers, EHR representativeness, NYC-specific housing and transport, no epigenetic clocks, binary race in interactions (p. 246).
- Authors claim the first study of social vulnerability and biological aging (p. 244).

## Why it matters for Pablo's work
- Claude's reading: an EHR-based biological aging outcome for neighborhood exposures, extending [[social-hallmarks-of-aging]] to neighborhood context and applying a [[social-exposome]] mixture framing; template for urban nature × aging studies on [[urban-nature-and-aging]].
- His framing is on [[2025-paper-svi-biological-aging-nyc]].

## See also
- [[phenotypic-age]] · [[social-exposome]] · [[social-hallmarks-of-aging]] · [[geroscience]] · [[sex-and-gender-effect-modification]] · [[differential-vulnerability]] · [[mount-sinai-data-warehouse]]
- Findings: [[social-vulnerability--phenotypic-age-acceleration--knobel2025social]], [[social-vulnerability--phenotypic-age-acceleration--knobel2025social-by-sex]], [[social-vulnerability--phenotypic-age-acceleration--knobel2025social-by-race-ethnicity]]

## References
- Knobel, P., Colicino, E., Kloog, I., Litke, R., Lane, K., Federman, A., Mobbs, C., & Yitshak Sade, M. (2025). Social vulnerability and biological aging in New York City: An electronic health records-based study. *Journal of Urban Health, 102*, 240–249. https://doi.org/10.1007/s11524-024-00948-7
