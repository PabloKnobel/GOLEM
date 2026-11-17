---
type: paper
title: "The association between short-term nitrogen dioxide (NO2) exposure and ischemic stroke or transient ischemic attacks (TIA): a national study in Israel"
citekey: fernando2026association
aliases: [NO2 stroke Israel, Israeli stroke registry NO2]
authors: ["Fernando, P. S.", "Krasnov, H.", "Kloog, I.", "He, M. Z.", "Ifergane, G.", "Zucker, I.", "Novack, V.", "Libruder, C.", "Yitshak-Sade, M."]
year: 2026
journal: "Scientific Reports"
doi: "10.1038/s41598-026-75950-x"
endnote_id: ""
apa: "Fernando, P. S., Krasnov, H., Kloog, I., He, M. Z., Ifergane, G., Zucker, I., Novack, V., Libruder, C., & Yitshak-Sade, M. (2026). The association between short-term nitrogen dioxide (NO2) exposure and ischemic stroke or transient ischemic attacks (TIA): A national study in Israel. Scientific Reports. Advance online publication. https://doi.org/10.1038/s41598-026-75950-x"
fulltext: read
metadata_checked: true
metadata_source: "CrossRef, 2026-11-17"
metadata_note: "Article in Press; CrossRef lists no volume or article number yet"
design: time-stratified case-crossover with distributed lag nonlinear models
population: "85,162 adults ≥18 y with ischemic stroke or TIA in the Israeli National Stroke Registry"
setting: "Israel, 2014–2018"
n: 85162
exposures: ["[[air-pollution]]"]
outcomes: ["[[atherosclerotic-cardiovascular-disease]]"]
methods: [case-crossover, DLNM, conditional GNM, likelihood ratio test for effect modification]
datasets: []
supports: []
contradicts: []
replicates: []
extends: []
projects: []
portals: ["[[urban-environmental-hazards]]"]
authored_by_pablo: false
tags: [paper, article-in-press]
created: 2026-11-17
updated: 2026-11-17
last_verified: 2026-11-17
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** In a nationwide case-crossover study of 85,162 ischemic stroke or TIA admissions in Israel (2014–2018), an 8-ppb (1 SD) increase in residential NO2 summed over lag days 0–5 was associated with 5.7% higher odds of the event (OR 1.057, 95% CI 1.034–1.081), adjusting for PM2.5 and temperature; associations peaked on lag days 3–5 ([[fernando2026association]], p. 1, 4). Lab colleagues of Pablo (Mount Sinai Environmental Medicine); Pablo is not an author.

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| Case-crossover (control days matched on day of week, same month and year), DLNM | 85,162 cases (69.9% ischemic stroke, 30.1% TIA) | Adults ≥18 y, Israeli National Stroke Registry, 2014–2018 | Daily 1-km NO2 at residence, cumulative lag 0–5, per 8 ppb (SD) | Hospital admission for ischemic stroke or TIA (ICD-9) | OR 1.057 (1.034–1.081) | PM2.5 (same window), temperature lag 0–4; time-invariant confounders by design |

## Key points
- Exposure: daily 1-km NO2 from a hybrid random forest + gradient boosting model with satellite, land-use and meteorological inputs; 10-fold CV R² 0.88, RMSE 3.81 µg/m³ (p. 3). 1,289 individuals without valid address excluded (1.6%) (p. 3).
- Mean NO2 12.34 ppb in text; Table 2 gives 12.32; higher in large cities (13.62) than suburban/rural (11.02) (p. 4–5).
- Lag structure: lag 1 OR 0.976 (0.961–0.994); lag 5 OR 1.042 (1.022–1.063) (p. 4–5, Fig. 1B).
- Effect modification (LRT): urbanicity p = 0.030, sex p = 0.009, age p = 0.035; diabetes, hypertension and IHD not significant (p. 5–6, Table 3) → [[no2--atherosclerotic-cardiovascular-disease--fernando2026association-by-subgroup]].
- Sensitivity: 3- to 6-day windows 1.053–1.057; excluding recurrent events 1.061 (1.036–1.086); adding same-day PM2.5 1.065 (1.042–1.089); ischemic stroke only 1.042 (1.015–1.070) (p. 5, 7).
- PM2.5 itself was not associated (OR 0.997, 0.993–1.001 per 10 µg/m³) (p. 7).
- Authors' limitations: residential-only exposure; possible over-representation of severe cases given high mortality; no stroke severity data (p. 8).
- Authors frame NO2 as a traffic-related marker that bundles gaseous toxicity and noise (p. 8).

> [!uncertain] Source inconsistencies
> - Table 1 reports "Died in the hospital" 59,825 (70.24%), which the authors call "relatively high mortality" (p. 5, 8); value as printed, not checked.
> - Text mentions ~15% CHF and ~3% prior MI, which are not in Table 1 (p. 4–5).
> - Mean age 71.8 in abstract/text vs 71.7 in Table 1 (p. 1, 5).
> - Text says cumulative associations were larger in urban areas, but on lag 5 the urban OR (1.025) is smaller than rural/suburban (1.066) (p. 5); the authors describe this as a steeper lag pattern in rural/suburban residents.

## Why it matters for Pablo's work
- Claude's reading: NO2 independent of PM2.5 for a cerebrovascular endpoint, from the same Mount Sinai exposure-modeling group; relevant to traffic-related co-exposures with [[environmental-noise]] and to stroke as an [[atherosclerotic-cardiovascular-disease]] component.

## See also
- [[air-pollution]] · [[atherosclerotic-cardiovascular-disease]] · [[urban-environmental-hazards]] · [[sex-and-gender-effect-modification]]
- Findings: [[no2--atherosclerotic-cardiovascular-disease--fernando2026association]], [[no2--atherosclerotic-cardiovascular-disease--fernando2026association-by-subgroup]]

## References
- Fernando, P. S., Krasnov, H., Kloog, I., He, M. Z., Ifergane, G., Zucker, I., Novack, V., Libruder, C., & Yitshak-Sade, M. (2026). The association between short-term nitrogen dioxide (NO2) exposure and ischemic stroke or transient ischemic attacks (TIA): A national study in Israel. *Scientific Reports*. Advance online publication. https://doi.org/10.1038/s41598-026-75950-x
