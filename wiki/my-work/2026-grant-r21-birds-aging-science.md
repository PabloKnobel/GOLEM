---
type: my-work
title: "R21 Birds and Aging: Research Strategy (Oct 2026)"
aliases: ["R21 science", "R21 research strategy", "R21_Science_20261014"]
kind: grant
role: [PI]
date: 2026-10-14
venue: "NIH R21 (PA-25-304)"
status: submitted
source_file: "raw/docs/35b2edf1-r21-science-20261014-for-sub.docx"
projects: ["[[r21-birds-aging]]", "[[nyc-bird-diversity]]"]
portals: ["[[urban-nature-and-aging]]"]
tags: [my-work, grant]
created: 2026-11-16
updated: 2026-11-16
generated: true
reviewed: false
---
**Lead.** Research Strategy (Importance, Rigor and Feasibility, Expertise and Resources) of Pablo's NIH R21 linking residential bird biodiversity to frailty (VA-FI) and phenotypic age acceleration in Mount Sinai older adults in NYC, file dated October 14, 2026 and marked "for submission". Hub: [[r21-birds-aging]].

> [!info] Submitted (Pablo, 2026-11-16).

## How I framed it
- Proxy question: "whether bird biodiversity adds information beyond standard exposures or simply stands in for them" (§A.1).
- Two pathways: a ***soundscape pathway***, where birdsong is "a sensory exposure in its own right", and a ***bioindicator pathway***, where "which birds are present signals the condition of the environment" (§A.1, Figure 1).
- Gap 1: an overall biodiversity index "blends both pathways" (§A.1, Two gaps). Gap 2: biodiversity exposure "has been hard to measure at population scale" (§A.1).
- Example for the bioindicator idea: the Gray Catbird "signals understory vegetation that NDVI cannot distinguish from lawn" (§A.1).
- Every result is informative: if neither pathway holds, "the association seen in our pilot most likely reflects standard exposures" (§A.3).
- Modifiability: supplementary feeding and the NYC Urban Forest Plan; perceived richness points to bird-identification education (§A.1).

## Design at a glance
- Population: MSHS adults ≥65 with an MSHS primary care physician, NYC, 2023–2027; pilot cohort 20,388 adults, 123,103 person-years (§B.3, Table 1).
- Exposure: 1,000 acoustic tiles of 100 × 100 m (192 recorded in 2025 + 808 in 2027), BirdNET with species thresholds for ≥90% precision, occupancy models, ensemble (mixed models, random forest, gradient boosting, spatially weighted GAM) adapted from Kloog's air pollution models, 100-m citywide surfaces (§B.4).
- Metrics: Acoustic Evenness Index, audibility, passerine Shannon diversity (soundscape); detection-corrected species presence (bioindicator) (Table 2).
- Aim 1: GAMs, negative binomial for VA-FI count and Gaussian for PhenoAgeAccel, FDR across 6 models; then adjust for traffic noise and NDVI (§B.6).
- Aim 2: about 5 bioindicator species; change in the PM2.5 and greenness estimates when species presence is added, tested against 100 pseudo-species surfaces from random spatial shifts (§B.7).
- Power: 80% for 1.2% per IQR in VA-FI count; 0.3 years PhenoAgeAccel (§B.9).
- Team: Knobel (PI), Alaasam (ornithology, acoustics), Yitshak-Sade, Kloog, Midya, Federman (§C.1).

## Concepts used
- [[bird-biodiversity]] — main exposure, split into soundscape and bioindicator metrics.
- [[frailty-index]] — VA-FI, 31 deficits, 3-year lookback (§B.5).
- [[phenotypic-age]] — PhenoAgeAccel from outpatient labs, MICE for CRP, albumin, alkaline phosphatase (§B.5).
- [[environmental-noise]] — traffic noise (BTS LAeq,24h) as the competing exposure for the soundscape pathway.
- [[ndvi]] — 300-m buffer, with 100-m and 500-m sensitivity analyses.
- [[attention-restoration-theory]] — basis for natural sound and stress recovery.

## Reusable pieces
- Preliminary results: eBird latent Shannon model for NYC tracts, Spearman ρ = 0.745; pilot association −1.4% VA-FI deficit count per IQR (95% CI −2.1% to −0.8%), strongest at 65–74 (§B.1; published evidence in [[knobel2026residential]]).
- 2025 fieldwork: 192 sites, mean 6.8 species per site (SD 3.9, range 0–26) (§B.1).
- Pseudo-species null distribution for attenuation tests (§B.7, 2b).
- Negative control outcome: annual influenza vaccination (§B.7, sensitivity analyses).
- Risks and alternatives list, 8 items (§B.10).
- Figures: conceptual framework (Figure 1), NYC tract latent Shannon map (Figure 2).

## See also
- [[nyc-bird-diversity]] · [[2026-preprint-bird-biodiversity-frailty]]
