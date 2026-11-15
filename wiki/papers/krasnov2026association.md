---
type: paper
title: "The association between long-term exposure to PM2.5 constituents and diabetes incidence and blood glucose levels among World Trade Center Health Program general responders"
citekey: krasnov2026association
aliases: [Krasnov 2026, PM2.5 sources diabetes WTC, source-apportioned PM2.5 glucose WTC]
authors: [Krasnov, H., Knobel, P., Hsu, H.-H. L., Teitelbaum, S. L., McLaughlin, M. A., Just, A. C., Kloog, I., Yitshak-Sade, M.]
year: 2026
journal: "American Journal of Epidemiology"
volume: 195
issue: "2"
pages: "497–504"
doi: "10.1093/aje/kwaf238"
endnote_id: ""
apa: "Krasnov, H., Knobel, P., Hsu, H.-H. L., Teitelbaum, S. L., McLaughlin, M. A., Just, A. C., Kloog, I., & Yitshak-Sade, M. (2026). The association between long-term exposure to PM2.5 constituents and diabetes incidence and blood glucose levels among World Trade Center Health Program general responders. American Journal of Epidemiology, 195(2), 497–504. https://doi.org/10.1093/aje/kwaf238"
fulltext: read
metadata_checked: false
design: cohort, repeated measures; multi-exposure mixed models
population: "34,764 WTCHP general responders in the Tri-state area; 121,246 glucose tests"
setting: "New York, New Jersey, Connecticut; 2003–2019"
n: 34764
exposures: ["[[air-pollution]]", annual PM2.5 mass, five NMF source-apportioned PM2.5 exposures]
outcomes: ["[[cardiometabolic-health]]", diabetes incidence, blood glucose]
methods: [non-negative matrix factorization, mixed-effect Poisson survival (Andersen–Gill), generalized additive mixed models, inverse probability weighting]
datasets: ["[[wtc-health-program]]"]
supports: []
contradicts: []
replicates: []
extends: ["[[knobel2024association]]", "[[knobel2023socioeconomic]]"]
projects: []
portals: ["[[urban-environmental-hazards]]"]
authored_by_pablo: true
tags: [paper, my-paper, cohort, multi-exposure, effect-modification, air-pollution]
created: 2026-11-15
updated: 2026-11-15
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** Among 34,764 WTC general responders (2003–2019), an IQR increase in annual metal-industry PM2.5 was associated with 8.35% higher diabetes risk (1.39–15.79%) and 1.31% higher glucose (0.80–1.82%) in multi-source models; total PM2.5 mass and other sources were not associated ([[krasnov2026association]], p. 497, 499, Table 3). Glucose associations differed by sex (p. 499). Pablo is second author (co-author).

> [!todo] Metadata to verify
> Not checked against CrossRef/OpenAlex (WebFetch not used). Advance access October 23, 2025 (p. 497). Author contributions not printed in the PDF (acknowledgments placeholder, p. 502). Stratified estimates for diabetes are in Table S2 (supplement not in vault).

> [!uncertain] Internal inconsistencies in the source
> - Metal-industry–diabetes lower CI: 1.39% in abstract and Table 3 (p. 497, 501) vs 1.49% in Results (p. 499).
> - IQRs differ between Table 2 and Table 3: biomass 0.44 vs 0.45, oil 1.74 vs 1.79, metal 0.42 vs 0.41, industry 1.35 vs 1.46 µg/m³ (p. 500–501).
> - Glucose sub-cohort: 26,756 (p. 498, Table 1) vs 26,747 responders (p. 499).
> - Table 1 totals do not match N = 34,764 (e.g., males 36,186 + females 5,590 = 41,776); diabetes 5,149 (12.59%) overall vs 99 and 253 in the subgroups; glucose labeled mmol/L with values in mg/dL (p. 500).
> - Temperature IQR 12.93 °C with SD 2.54 °C (p. 500, Table 2).
> - The earlier WTC PM2.5–glucose study is described as "a 2023 study" (p. 498); in the vault it is [[knobel2024association]].

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| Cohort, Poisson survival (Andersen–Gill), multi-source (p. 499) | 34,764 | WTC general responders, Tri-state, 2003–2019 | Metal-industry PM2.5, annual, per IQR | Diabetes incidence | +8.35% (1.39–15.79%) (p. 501, Table 3) | Age, sex, race, education, 9/11 occupation, time on site, tract SES, temperature, year spline; other sources |
| Repeated-measures GAMM, multi-source | 121,246 tests; 26,756 people | Same | Same | Log glucose | +1.31% (0.80–1.82%); IPW +1.25% (0.75–1.76%) | Same |
| Same, PM2.5 mass (model 1) | Same | Same | Total PM2.5, per IQR 4.06 | Diabetes; glucose | −6.66% (−16.33 to 4.12); −0.45% (−0.99 to 0.09) | Same |

## Key points
- Exposure: annual 1-km XGBoost PM2.5 (RMSE 3.11 µg/m³) and 14 PM2.5 components from super-learned models (50 m urban), factored by NMF into biomass burning, oil combustion, metal industry, other industries and motor vehicles/resuspended dust (MVRD) (p. 498) → [[air-pollution]].
- Diabetes: self-report or ≥2 glucose tests >200 mg/dL; prevalent diabetes by 2003 excluded (2.09%) (p. 498).
- Sample: mean age ~47, 86.62% male, 51.56% White; 12.59% reported diabetes (p. 499).
- Mean PM2.5 9.22 µg/m³; correlations among sources low to moderate (highest r = −0.49, metal vs biomass) (p. 499).
- Sex modification of glucose: women biomass +1.08% (0.32–1.85) and MVRD +1.34% (0.76–1.93); men oil combustion +0.68% (0.03–1.34) (p. 499, Fig. 1) → [[pm25-sources--glucose--krasnov2026association-by-sex]].
- Diabetes not modified by sex, except a borderline biomass interaction (p = .050; women +12.89%, 1.03–26.15%) (p. 499).
- Authors attribute the null PM2.5-mass result to limited Tri-state variability, and the difference from the 6-month glucose association to different exposure windows (p. 500).
- Authors' limitations: generalizability, exposure measurement error, self-reported diabetes without subtype (p. 502).

## Why it matters for Pablo's work
- Claude's reading: extends [[knobel2024association]] (PM2.5 mass, same cohort) and [[knobel2023socioeconomic]] (NMF sources) to long-term sources; another sex-differential vulnerability result on [[urban-environmental-hazards]].
- Framing notes on [[2026-paper-pm25-sources-diabetes-wtc]].

## See also
- extends: [[knobel2024association]] · [[knobel2023socioeconomic]] · uses_dataset: [[wtc-health-program]]
- [[cardiometabolic-health]] · [[sex-and-gender-effect-modification]] · [[differential-vulnerability]] · [[multi-exposure-analysis]]
- Findings: [[metal-industry-pm25--diabetes--krasnov2026association]], [[metal-industry-pm25--glucose--krasnov2026association]]

## References
- Krasnov, H., Knobel, P., Hsu, H.-H. L., Teitelbaum, S. L., McLaughlin, M. A., Just, A. C., Kloog, I., & Yitshak-Sade, M. (2026). The association between long-term exposure to PM2.5 constituents and diabetes incidence and blood glucose levels among World Trade Center Health Program general responders. *American Journal of Epidemiology, 195*(2), 497–504. https://doi.org/10.1093/aje/kwaf238
- Knobel, P., Just, A. C., Colicino, E., Teitelbaum, S. L., McLaughlin, M. A., Amini, H., & Yitshak Sade, M. (2024). The association of air pollution exposure with glucose and lipid levels: The role of an extreme air pollution event alongside 2 decades of moderate exposure. *American Journal of Epidemiology, 193*(1), 87–95.
- Knobel, P., et al. (2023). Socioeconomic and racial disparities in source-apportioned PM2.5 levels across urban areas in the contiguous US, 2010. *Atmospheric Environment, 303*, Article 119753.
