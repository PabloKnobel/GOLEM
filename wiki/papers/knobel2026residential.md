---
type: paper
title: "Residential bird biodiversity and frailty deficit accumulation: a longitudinal cohort study in New York City"
citekey: knobel2026residential
aliases: [bird biodiversity frailty preprint, VAFI birds paper]
authors: ["Knobel, P.", "Alaasam, V.", "Krasnov, H.", "Kloog, I.", "Midya, V.", "Federman, A.", "Ko, F.", "Yitshak Sade, M."]
year: 2026
journal: "medRxiv (preprint, not peer reviewed)"
doi: "10.64898/2026.08.18.26360707"
endnote_id: ""
apa: "Knobel, P., Alaasam, V., Krasnov, H., Kloog, I., Midya, V., Federman, A., Ko, F., & Yitshak Sade, M. (2026). Residential bird biodiversity and frailty deficit accumulation: A longitudinal cohort study in New York City [Preprint]. medRxiv. https://doi.org/10.64898/2026.08.18.26360707"
fulltext: read
metadata_checked: true
metadata_source: "CrossRef, 2026-11-15"
metadata_note: "CrossRef splits the last author as 'Sade, Maayan Yitshak'; kept 'Yitshak Sade, M.' as in the preprint"
design: retrospective cohort (EHR)
population: "20,388 adults ≥65 y in primary care, Mount Sinai Health System"
setting: "New York City, 2011–2023"
n: 20388
exposures: ["[[bird-biodiversity]]"]
outcomes: ["[[frailty-index]]"]
methods: [negative binomial GAM, latent biodiversity surface (Gamma GAM)]
datasets: ["[[ebird]]"]
supports: []
contradicts: []
replicates: []
extends: []
projects: ["[[r21-birds-aging]]", "[[nyc-bird-diversity]]"]
portals: ["[[urban-nature-and-aging]]"]
authored_by_pablo: true
tags: [paper, my-paper, preprint]
created: 2026-11-15
updated: 2026-11-16
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** In 20,388 older New Yorkers followed for 123,103 patient-years, each IQR increase in modeled residential bird Shannon diversity was associated with a 1.4% lower expected VA-FI deficit count (95% CI −2.1% to −0.8%); the association was strongest at ages 65–74 and absent at ≥85 ([[knobel2026residential]], p. 1, 8). Preprint, not peer reviewed.

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| Retrospective cohort, annual repeated measures | 20,388 (123,103 patient-years) | ≥65 y, Mount Sinai primary care, NYC, 2011–2023 | Latent bird Shannon diversity, census tract × year, per IQR | VA-FI deficit count (31 items) | −1.4% (−2.1 to −0.8) | Age, sex, race and ethnicity, insurance, tract poverty, tract % non-Hispanic Black; spline of calendar year; patient random intercept |

## Key points
- Exposure: a Gamma GAM latent biodiversity surface from complete eBird checklists, correcting for uneven observer effort; only 2,528 of 34,905 tract-years (7.2%) had enough checklists; test-set R² = 0.558, Spearman ρ = 0.745 (p. 5–6).
- Outcome: VA-FI built from ICD-10 and CPT codes with a 3-year lookback, analyzed as a deficit count (p. 6–7).
- Effect modification by age: 65–74 −3.0% (−3.9 to −2.1); 75–84 −0.8% (−1.9 to 0.3); ≥85 +1.6% (−0.0 to 3.3) (p. 8–9, Table 3).
- Sensitivity: inverse-variance weighted −1.4% (−1.5 to −1.2); quasi-Poisson −1.5% (−2.1 to −0.8) (p. 8, Table 2).
- Authors' limitations: tract-level residential exposure; residual confounding (built environment, social capital, early life); VA-FI depends on health-care use, partly addressed by ending follow-up at two years without use (p. 10–11).
- Authors frame bird diversity as both a direct experiential exposure and a bioindicator of wider environmental quality (p. 3).

## Why it matters for Pablo's work
- Claude's reading: this is Pablo's own evidence for nature *quality/biodiversity* beyond greenness quantity, in an aging outcome; it links [[urban-nature-and-aging]] and [[urban-green-space-quality]].
- His framing of the paper is on [[2026-preprint-bird-biodiversity-frailty]].

## See also
- [[bird-biodiversity]] · [[frailty-index]] · [[ebird]] · [[attention-restoration-theory]] (mechanism the authors invoke, p. 9–10)
- Findings: [[bird-biodiversity--frailty-index--knobel2026residential]], [[bird-biodiversity--frailty-index--knobel2026residential-by-age]]

## References
- Knobel, P., Alaasam, V., Krasnov, H., Kloog, I., Midya, V., Federman, A., Ko, F., & Yitshak Sade, M. (2026). Residential bird biodiversity and frailty deficit accumulation: A longitudinal cohort study in New York City [Preprint]. medRxiv. https://doi.org/10.64898/2026.08.18.26360707
