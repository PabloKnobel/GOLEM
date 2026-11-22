---
type: my-work
title: "R01 Urban Exposome: From Evidence to Intervention for Healthy Aging (submitted Jun 2026)"
aliases: ["R01 Urban Exposome grant", "1R01AG107495-01", "R01_UrbanExposome_1_grant", "Urban Exposome R01 application"]
kind: grant
role: [PI]
date: 2026-06-04
venue: "NIH R01, PA-25-301 (NIA, dual ES); SRG SBCP; council 01/2027"
status: submitted
source_file: "raw/docs/r01-urbanexposome-1-grant.pdf"
fulltext: partial
fulltext_note: "Read in full: project summary and narrative (PDF p. 7–8), specific aims and research strategy (p. 106–118), lifespan inclusion, study timeline and team structure (p. 123, 126, 133). Not read: SF424 forms, facilities, biosketches, other support, budgets and justifications, human-subjects forms, references, letters (p. 1–6, 9–105, 119–122, 124–125, 127–132, 134–141)."
projects: ["[[r01-urban-exposome-aging]]"]
portals: ["[[exposome-research]]", "[[urban-nature-and-aging]]"]
tags: [my-work, grant]
created: 2026-11-17
updated: 2026-11-17
last_verified:
confidence:
superseded_by: ""
generated: true
reviewed: false
---
**Lead.** Pablo's NIH R01 application (application number 1R01AG107495-01, received 06/04/2026, PA-25-301, Mount Sinai Environmental Medicine) on how the joint urban exposome — built, social and ambient — relates to six healthy-aging outcomes in two cohorts (MSHS EHR, NYC; LitCog, Chicago), with scenario projections of feasible urban interventions (PDF p. 1, 106). Hub: [[r01-urban-exposome-aging]].

> [!info] Status from the cover sheet: received 06/04/2026; council 01/2027 (PDF p. 1). Review outcome not in the vault.

## How I framed it
- Urban Exposome defined as a facet of the exposome with two key features: "its exposures are geospatial and, in most cases, directly modifiable by decision-makers"; three dimensions: built, social, ambient (Specific Aims, PDF p. 106).
- Outcome framework: the Healthy Aging Phenotype (HAP) — physiological and metabolic health, physical capability, cognitive function, psychological wellbeing, social wellbeing (Specific Aims).
- Three gaps: (1) "no study has linked the urban exposome to healthy aging"; (2) most work "focuses on single aging outcomes"; (3) evidence "rarely extends beyond association to the actionable question of what would happen to aging outcomes if specific urban features were improved" (Specific Aims).
- Single-exposure models as "a necessary first step", multi-exposure models as "an essential next step to account for the reality that no exposure acts in isolation" (§A.1, PDF p. 107).
- "We treat the Urban Exposome as an operational framework: it defines which exposures we measure, how we model them jointly, and how we interpret the results" (§A.1).
- Pathways: built environment acts "primarily through behavioral intermediaries"; social through chronic stress and allostatic load; ambient through inflammation, oxidative stress and autonomic dysregulation (§A.1, PDF p. 108).
- Aim 3 framed "explicitly as exploratory"; "What we produce is a prioritization tool", "not a substitute for a randomized trial" (§B.5, PDF p. 115).
- Scenario targets constrained to "levels already observed in comparable neighborhoods" — feasible minimum risk rather than theoretical optima (§A.2, §B.5.2).
- Generalizability argued "at the neighborhood level", not city level (§B.7, PDF p. 117).

## Design at a glance
- Aim 1 (MSHS EHR): ~20,000 adults ≥55 with an MSHS primary care physician, 2011–2025, ~160,000 person-years; PhenoAgeAccel (outpatient labs, MICE) and VA-FI (31 deficits, 3-year lookback); ExWAS with GAMs (BH FDR q < 0.05) and mixed-effects qGcomp (§B.3, PDF p. 111–113).
- Aim 2 (LitCog): 900 Chicago adults enrolled 2008–2010 at age 55–74, six waves over 15 years; PROMIS PF-10a, MMSE, PROMIS Depression, LSNS-6; BVCKMR for baseline level and rate of change (§B.4, PDF p. 113–115).
- Aim 3: ensemble (elastic net, random forest, XGBoost), multi-output t → t+1 prediction; up to five exposure targets; moderate (median of top quartile) and ambitious (90th percentile) scenarios; synthetic populations vs business as usual; bootstrap CIs; clinical cutoffs (VA-FI > 0.21; MMSE ≤ 23; PROMIS PF ≤ 40; PROMIS Depression ≥ 60; LSNS < 12) (§B.5, PDF p. 115–116).
- Exposures: ~40 built, social and ambient layers harmonized to census tract × year, from the Mount Sinai GREENER platform plus team-developed metrics (green space quality from the Gateway Exposome pilot; bird biodiversity from the HEALS pilot) (§B.2, Table 2, PDF p. 110–111).
- Power: Aim 1, 80% for 0.02 SD at Bonferroni α = 0.00125; Aim 2, d = 0.04 (N = 900) and d = 0.07 (N ≈ 400 at T4) (§B.6, PDF p. 116).
- Team: Knobel (PI); Yitshak-Sade, Kloog, Midya, Federman (Mount Sinai); Wolf and Rogers (Northwestern, LitCog) (§C.1, PDF p. 117).

## Concepts used
- [[exposome]] — operationalized as the Urban Exposome (built, social, ambient).
- [[phenotypic-age]] — PhenoAgeAccel, Aim 1 outcome.
- [[frailty-index]] — VA-FI, Aim 1 outcome.
- [[multi-exposure-analysis]] — ExWAS, qGcomp, BVCKMR.
- [[social-exposome]] — social domain (SVI, crime, safety and neighborhood perception).
- [[air-pollution]] · [[environmental-noise]] · [[ambient-temperature]] · [[ndvi]] · [[bird-biodiversity]] · [[green-space-quality-assessment]] — exposure layers.

## Reusable pieces
- Preliminary results paragraph set (§B.1, PDF p. 109–110): urban nature profiles and ASCVD ([[knobel2026beyond]]); SVI and PhenoAgeAccel ([[knobel2025social]]); Medicare PM2.5 sources and ASCVD mortality (not yet in vault); PM2.5 components and frailty velocity in 20,880 MSHS patients (unpublished); LitCog PM2.5/NDVI and aging outcomes (unpublished); WTC PM2.5, temperature, GVI and frailty/depression (unpublished); XGBoost frailty scenario pilot (Figure 1).
- Unpublished preliminary estimates as written in the grant (preliminary, not findings): PM2.5 and frailty velocity β = 0.013 (0.006, 0.022) per IQR, lead β = 0.103 (0.057, 0.149); LitCog PM2.5 and MMSE β = −0.23 (−0.34, −0.13), NDVI and depressive symptoms β = −5.05 (−9.51, −0.59); WTC PM2.5 +2.16% frailty, GVI −1.51%; scenario pilot: lead reduction −7.4%, urban greening −0.8%, combined −8.0% predicted VA-FI (PDF p. 109–110).
- Table 2 exposure catalog with descriptions (PDF p. 110–111) — reusable for any urban exposome proposal.
- Table 1 aim × cohort × outcome × method matrix (PDF p. 109); Table 5 instrument table (PDF p. 114).
- Limitations and alternatives lists for each aim (§B.3.4, §B.4.4, §B.5.4).
- Five-year timeline (PDF p. 126).

> [!uncertain] Internal inconsistencies in the application (for reuse)
> - ExWAS multiple testing: Benjamini-Hochberg FDR in §B.3.3 (PDF p. 113) vs "applying Bonferroni correction" in the timeline (PDF p. 126); power uses Bonferroni (PDF p. 116).
> - NDVI described as "30-m resolution (MODIS)" (Table 2, PDF p. 110); MODIS NDVI is not 30 m (Claude's note; check the product).
> - Wolf is listed as "Other (Specify)-SubAward PI" on the cover sheet (PDF p. 1) but "Co-I" in §C.1 (PDF p. 117).
> - Preliminary ASCVD paragraph compares to "Low Nature" and then "Low Green" profile in the same sentence (PDF p. 109).
> - HAP described with five domains and "six outcomes" — consistent (two Aim 1 outcomes in one domain), noted for clarity.

## See also
- [[r01-urban-exposome-aging]] · [[litcog]] · [[mount-sinai-data-warehouse]] · [[2025-paper-svi-biological-aging-nyc]] · [[2026-paper-urban-nature-profiles-ascvd]]
