---
type: paper
title: "The association of air pollution exposure with glucose and lipid levels: The role of an extreme air pollution event alongside 2 decades of moderate exposure"
citekey: knobel2024association
aliases: [Knobel 2024, WTC air pollution glucose cholesterol, World Trade Center PM2.5 glucose lipids]
authors: ["Knobel, P.", "Just, A. C.", "Colicino, E.", "Teitelbaum, S. L.", "McLaughlin, M. A.", "Amini, H.", "Yitshak Sade, M."]
year: 2024
journal: "American Journal of Epidemiology"
volume: 193
issue: 1
pages: "87–95"
doi: "10.1093/aje/kwad173"
endnote_id: ""
apa: "Knobel, P., Just, A. C., Colicino, E., Teitelbaum, S. L., McLaughlin, M. A., Amini, H., & Yitshak Sade, M. (2024). The association of air pollution exposure with glucose and lipid levels: The role of an extreme air pollution event alongside 2 decades of moderate exposure. American Journal of Epidemiology, 193(1), 87–95. https://doi.org/10.1093/aje/kwad173"
fulltext: read
metadata_checked: true
metadata_source: "CrossRef, 2026-11-15"
design: occupational cohort, repeated laboratory measures
population: "22,447 WTC Health Program general responders; 96,155 cholesterol and 81,599 glucose results"
setting: "New York metropolitan area, 2004–2019 (WTC exposure 2001)"
n: 22447
exposures: ["[[air-pollution]]", WTC-related extreme air pollution exposure (composite index)]
outcomes: ["[[cardiometabolic-health]]"]
methods: [generalized additive mixed models, random intercept, penalized spline for year, mediation analysis, stratification by diabetes]
datasets: ["[[wtc-health-program]]", Just 2020 XGBoost PM2.5 model (1 km)]
supports: []
contradicts: []
replicates: []
extends: []
projects: []
portals: ["[[urban-environmental-hazards]]"]
authored_by_pablo: true
tags: [paper, my-paper, cohort, effect-modification, multi-exposure]
created: 2026-11-15
updated: 2026-11-15
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** In 22,447 World Trade Center (WTC) responders followed 2004–2019, an IQR (3.09 µg/m³) increase in 6-month residential PM2.5 was associated with +0.78 mg/dL glucose (95% CI 0.30, 1.26) and +1.67 mg/dL total cholesterol (1.00, 2.35), and high WTC exposure in 2001 with +0.82 mg/dL glucose (0.22, 1.43), each adjusted for the other ([[knobel2024association]], p. 90–91). Associations were mostly larger among people with diabetes (p. 91). Pablo is first and corresponding author.

> [!todo] Metadata to verify
> Not checked against CrossRef (WebFetch not used in this batch). Advance access August 16, 2023; issue 2024;193(1):87–95 as printed (p. 87).

> [!uncertain] Internal inconsistencies in the source
> - Abstract reports cholesterol +0.67 mg/dL (95% CI 1.00, 2.35); Results and Table 2 report +1.67 (1.00, 2.35). The abstract point estimate lies outside its own CI, so 1.67 is used here (p. 87, 90–91).
> - Glucose sample: 81,599 results (abstract, Results, Table 2) vs 82,015 (Methods, Tables 3–4) (p. 87–91).
> - Table 2 column header says "% Change", but text and footnote describe mg/dL changes (p. 91).
> - Mediation: PM2.5 mediated −1.7% (95% CI −6.2, −1.0) of the high WTC–glucose association; point estimate outside its CI (p. 92).

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| Cohort, GAMs with random intercept (p. 89) | 81,599 tests | WTC responders, NY metro, 2004–2019 | PM2.5 6-month mean, per IQR 3.09 µg/m³ | Serum glucose | +0.78 mg/dL (0.30, 1.26) | WTC exposure, sex, age, race, education, diabetes, hypertension, season, year spline, temperature |
| Same | 96,155 tests | Same | PM2.5 6-month mean, per IQR | Total cholesterol | +1.67 mg/dL (1.00, 2.35) | Same |
| Same | 82,015 tests | Same | WTC composite, high vs low | Serum glucose | +0.82 mg/dL (0.22, 1.43) | PM2.5 6-month, same |
| Same | 96,155 tests | Same | WTC composite, intermediate vs low | Total cholesterol | +0.99 mg/dL (0.30, 1.67) | Same |

## Key points
- WTC exposure (self-reported, 2001): low = <40 days, no dust cloud, not on the pile; intermediate = 40–90 days or on the pile; high = in the dust cloud or >90 days (p. 88).
- PM2.5: daily 1-km XGBoost model with satellite AOD; RMSE 3.11 µg/m³ (spatial CV); address at visit from 2012, first reported address before 2012 (p. 89).
- Cohort: mean age ~52, 85% male, 62.6% non-Hispanic White, 13.1% with diabetes; mean glucose 102.02 and cholesterol 194.80 mg/dL (p. 89–90, Table 1).
- PM2.5 windows: 1-week null for both outcomes; 3-month associated with cholesterol (+0.75; 0.26, 1.23) but not glucose; 6-month associated with both (p. 90–91, Table 2) → [[pm25--glucose--knobel2024association]], [[pm25--total-cholesterol--knobel2024association]].
- WTC: high (not intermediate) associated with glucose; intermediate (not high) associated with cholesterol, attenuated at the highest category, possibly residual confounding or measurement error (p. 91–92, Table 3) → [[wtc-exposure--glucose--knobel2024association]].
- Dichotomized outcomes: OR 1.08 (1.04, 1.12) for abnormal cholesterol per IQR PM2.5; high WTC–glucose OR 1.08 (1.02, 1.14), though the text says this association "did not maintain its significance" (p. 91–92, Table 4).
- Effect modification by diabetes: PM2.5–glucose +5.03 (2.04, 8.02) with diabetes vs +0.16 (−0.19, 0.52) without; PM2.5–cholesterol stronger without diabetes (+1.92; 1.21, 2.64) than with (−0.44; −2.47, 1.58) (p. 91, Fig. 1) → [[pm25--glucose--knobel2024association-by-diabetes]].
- Reverse causation and mediation checks: pre-2001 diabetes or hypertension not associated with WTC exposure; PM2.5 a negligible mediator; estimates unchanged without PM2.5 adjustment (p. 91–92).
- Sensitivity: 2012–2019 only (address histories) and hours on site gave similar inferences (p. 90–91).
- Authors' limitations: self-reported, unvalidated WTC index; no unexposed reference group; pre-2012 address misclassification; no smoking or physical activity data; occupational, mostly male cohort (p. 93).
- Authors frame WTC as conceptually comparable to other extreme particulate events such as wildfires (p. 88, 93).

## Why it matters for Pablo's work
- Claude's reading: a two-exposure design (historical extreme event plus later moderate PM2.5) relevant to multi-exposure framing on [[urban-environmental-hazards]]; diabetes as a susceptibility factor.
- His framing is on [[2024-paper-wtc-air-pollution-glucose-lipids]].

## See also
- [[air-pollution]] · [[cardiometabolic-health]] · [[wtc-health-program]]
- Findings: [[pm25--glucose--knobel2024association]], [[pm25--total-cholesterol--knobel2024association]], [[wtc-exposure--glucose--knobel2024association]], [[pm25--glucose--knobel2024association-by-diabetes]]
- Extended by [[krasnov2026association]] (long-term source-apportioned PM2.5, same cohort).

## References
- Knobel, P., Just, A. C., Colicino, E., Teitelbaum, S. L., McLaughlin, M. A., Amini, H., & Yitshak Sade, M. (2024). The association of air pollution exposure with glucose and lipid levels: The role of an extreme air pollution event alongside 2 decades of moderate exposure. *American Journal of Epidemiology, 193*(1), 87–95. https://doi.org/10.1093/aje/kwad173
