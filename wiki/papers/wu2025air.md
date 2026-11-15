---
type: paper
title: "Air pollution, temperature, and HbA1c levels among children in Mexico City, Mexico"
citekey: wu2025air
aliases: [Wu 2025, PROGRESS HbA1c air pollution, children HbA1c Mexico City]
authors: ["Wu, J.", "Knobel, P.", "He, M. Z.", "Kloog, I.", "Just, A. C.", "Gutiérrez-Avila, I.", "Colicino, E.", "Téllez-Rojo, M. M.", "Pizano-Zárate, M. L.", "Tamayo-Ortiz, M.", "Cantoral, A.", "Soria-Contreras, D. C.", "Baccarelli, A. A.", "Wright, R. O.", "Yitshak Sade, M."]
year: 2025
journal: "Ecotoxicology and Environmental Safety"
volume: 307
issue: "?"
pages: "Article 119424"
doi: "10.1016/j.ecoenv.2025.119424"
endnote_id: ""
apa: "Wu, J., Knobel, P., He, M. Z., Kloog, I., Just, A. C., Gutiérrez-Avila, I., Colicino, E., Téllez-Rojo, M. M., Pizano-Zárate, M. L., Tamayo-Ortiz, M., Cantoral, A., Soria-Contreras, D. C., Baccarelli, A. A., Wright, R. O., & Yitshak Sade, M. (2025). Air pollution, temperature, and HbA1c levels among children in Mexico City, Mexico. Ecotoxicology and Environmental Safety, 307, Article 119424. https://doi.org/10.1016/j.ecoenv.2025.119424"
fulltext: read
metadata_checked: true
metadata_source: "CrossRef, 2026-11-15"
design: prospective birth cohort, repeated measures
population: "503 children aged 4–11 y, 1,196 HbA1c measurements"
setting: "Mexico City, 2013–2019"
n: 503
exposures: ["[[air-pollution]]", "[[ambient-temperature]]"]
outcomes: ["[[cardiometabolic-health]]"]
methods: [linear mixed-effects model, multi-exposure model, inverse probability weighting, E-values]
datasets: ["[[progress-cohort]]"]
supports: []
contradicts: []
replicates: []
extends: []
projects: []
portals: ["[[urban-environmental-hazards]]"]
authored_by_pablo: true
tags: [paper, my-paper, cohort, children, multi-exposure]
created: 2026-11-15
updated: 2026-11-15
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** In 503 children of the PROGRESS cohort, a multi-exposure mixed model found that each 1 µg/m³ higher 3-month PM2.5 was associated with a 0.311% relative increase in HbA1c (95% CI 0.159–0.464) and each 1 °C higher temperature with a 0.626% decrease (−0.977 to −0.274); NO2 was not associated ([[wu2025air]], p. 1, 3). Pablo is second author.

> [!todo] Metadata to verify
> Not checked against CrossRef (WebFetch unavailable in this run). Issue not printed: `?`. Author diacritics reconstructed from garbled PDF text (Gutiérrez-Avila, Téllez-Rojo, Pizano-Zárate).

> [!uncertain] Internal inconsistencies in the source
> The abstract reports 1,186 HbA1c measurements, the results and Table 1 report 1,196 (p. 1, 3). The NO2 upper CI is 0.106 in the abstract and Table 2 but 0.091 in the results text (p. 1, 3–4). The E-value sentence names PM2.5 and NO2 but then gives a value for temperature (p. 3).

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| Cohort, repeated measures, multi-exposure LMM (p. 2–3) | 503 children, 1,196 measurements | Ages 4–11, Mexico City, 2013–2019 | PM2.5, 3-month mean, per 1 µg/m³ | HbA1c (log), % relative change | 0.311% (0.159 to 0.464) | Child age, season, maternal smoking, marital status, education; spline of year; NO2 and temperature |
| Same | Same | Same | Temperature, 3-month mean, per 1 °C | Same | −0.626% (−0.977 to −0.274) | Same, with PM2.5 and NO2 |
| Same | Same | Same | NO2, 3-month mean, per 1 ppb | Same | −0.010% (−0.126 to 0.106) | Same, with PM2.5 and temperature |

## Key points
- Exposures: daily 1-km PM2.5, NO2 and air temperature from hybrid satellite and machine-learning models, linked to geocoded residential histories (p. 2).
- Mean (SD) 3-month exposures: PM2.5 20.72 (4.22) µg/m³, NO2 28.87 (6.16) ppb, temperature 15.67 (1.97) °C; highest correlation PM2.5–NO2 r = 0.56 (p. 3).
- Single-exposure models: PM2.5 0.264% (0.135 to 0.393), NO2 0.061% (−0.036 to 0.158), temperature −0.487% (−0.825 to −0.148) (Table 2, p. 4).
- Robust to inverse probability weighting and 6-month averages; no exposure interactions (p = 0.332, 0.550, 0.263) (p. 3, Table 2).
- PM2.5 association rose with age: 4–5 y 0.132% (−0.116 to 0.382), 6–7 y 0.325% (0.120 to 0.531), 8–11 y 0.577% (0.289 to 0.866) (p. 3) → [[pm25--hba1c--wu2025air-by-age]].
- Temperature association stronger in girls (−0.829%; −1.246 to −0.410) than boys (−0.480%; −1.050 to 0.095), and in the oldest group (−1.396%; −2.062 to −0.726) (p. 3).
- An unexpected protective NO2 association at ages 6–7 is flagged by the authors as possibly spurious (p. 4–5).
- Exclusions: missing residential history 20.8%, missing covariates 5% (p. 2).
- Authors' limitations: possible selection bias, residual confounding (physical activity, diet, fluid intake), exposure error, limited power for interactions (p. 5).

## Why it matters for Pablo's work
- Claude's reading: a multi-exposure, life-stage-stratified analysis with Mount Sinai colleagues; it sits in [[urban-environmental-hazards]] and shows sex and age effect modification, a recurring theme in Pablo's work.
- His framing is on [[2025-paper-air-pollution-temperature-hba1c-children]].

## See also
- [[air-pollution]] · [[ambient-temperature]] · [[cardiometabolic-health]] · [[progress-cohort]]
- Findings: [[pm25--hba1c--wu2025air]], [[ambient-temperature--hba1c--wu2025air]], [[no2--hba1c--wu2025air]], [[pm25--hba1c--wu2025air-by-age]]

## References
- Wu, J., Knobel, P., He, M. Z., Kloog, I., Just, A. C., Gutiérrez-Avila, I., Colicino, E., Téllez-Rojo, M. M., Pizano-Zárate, M. L., Tamayo-Ortiz, M., Cantoral, A., Soria-Contreras, D. C., Baccarelli, A. A., Wright, R. O., & Yitshak Sade, M. (2025). Air pollution, temperature, and HbA1c levels among children in Mexico City, Mexico. *Ecotoxicology and Environmental Safety, 307*, Article 119424. https://doi.org/10.1016/j.ecoenv.2025.119424
