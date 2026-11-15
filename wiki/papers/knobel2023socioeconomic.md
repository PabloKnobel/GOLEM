---
type: paper
title: "Socioeconomic and racial disparities in source-apportioned PM2.5 levels across urban areas in the contiguous US, 2010"
citekey: knobel2023socioeconomic
aliases: [Knobel 2023, PM2.5 source disparities, source-apportioned PM2.5 disparities]
authors: ["Knobel, P.", "Hwang, I.", "Castro, E.", "Sheffield, P.", "Holaday, L.", "Shi, L.", "Amini, H.", "Schwartz, J.", "Yitshak Sade, M."]
year: 2023
journal: "Atmospheric Environment"
volume: 303
issue: "?"
pages: "Article 119753"
doi: "10.1016/j.atmosenv.2023.119753"
endnote_id: ""
apa: "Knobel, P., Hwang, I., Castro, E., Sheffield, P., Holaday, L., Shi, L., Amini, H., Schwartz, J., & Yitshak Sade, M. (2023). Socioeconomic and racial disparities in source-apportioned PM2.5 levels across urban areas in the contiguous US, 2010. Atmospheric Environment, 303, Article 119753. https://doi.org/10.1016/j.atmosenv.2023.119753"
fulltext: read
metadata_checked: true
metadata_source: "CrossRef, 2026-11-15"
design: ecological cross-sectional (descriptive)
population: "25,790 urban ZIP codes (RUCA ≤6), ~92% of US population"
setting: "Contiguous US, 2010"
n: 25790
exposures: ["ZIP code % non-Hispanic Black", "% below poverty", "% no high school diploma", "% renters"]
outcomes: ["[[air-pollution]]"]
methods: [non-negative matrix factorization, generalized nonlinear models, regional stratification]
datasets: [Di 2019 PM2.5 ensemble model, Amini 2022 PM2.5 component models (50 m urban), 2010 US Census, ACS 5-year]
supports: []
contradicts: []
replicates: []
extends: []
projects: []
portals: ["[[urban-environmental-hazards]]", "[[exposome-research]]"]
authored_by_pablo: true
tags: [paper, my-paper, ecological, environmental-justice, exposure-assessment]
created: 2026-11-15
updated: 2026-11-15
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** Across 25,790 urban US ZIP codes in 2010, 14 modeled PM2.5 components were factored into five source categories; ZIP codes with more non-Hispanic Black residents and lower SES had higher total PM2.5 and higher Heavy Fuel Oil and Industrial, Metal Processing Industry and Agricultural, and Motor Vehicle PM2.5, with larger disparities in the West ([[knobel2023socioeconomic]], p. 1, 3). Numeric estimates are in figures and supplementary tables only. Pablo is co-first and corresponding author.

> [!todo] Metadata to verify
> Not checked against CrossRef (WebFetch not used in this batch). Issue not printed: `?`. Effect sizes are only in Fig. 3–4 and Supplementary Tables 2–4 (not in the converted text): `?`.

> [!uncertain] Internal inconsistencies in the source
> - 2010 ZIP-level ACS variables were "imputed … by linearly extrapolating between the measured years (2013–2020)", i.e., backward extrapolation described as interpolation (p. 2).
> - Table 1: % no high school has SD 9.46, identical to its 25th percentile 9.46; possible transcription error (p. 3).
> - Source labels in the abstract ("Heavy Fuel, Oil and Industrial") differ from the body ("Heavy Fuel Oil and Industrial") (p. 1, 3).

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| Ecological cross-sectional, GNMs one predictor at a time (p. 3) | 25,790 ZIP codes | Urban contiguous US, 2010 | % non-Hispanic Black, per 10% | PM2.5 mass and 5 source categories | Positive for PM2.5 mass, Heavy Fuel Oil/Industrial, Metal Processing/Agricultural, Motor Vehicle; inverse for Coal/Oil/Biomass; values `?` (Fig. 3, Supp. Table 2) | Population density, RUCA, % over 65, % female |
| Same | Same | Same | % poverty, % no high school, % renters, per 10% | Same | Positive for PM2.5 mass, Soil/Crustal Dust, Heavy Fuel Oil/Industrial, Metal Processing/Agricultural, Motor Vehicle; inverse for Coal/Oil/Biomass; values `?` | Same |

## Key points
- Components: EC, OC, NO3, SO4, Br, Ca, Cu, Fe, Ni, K, Pb, Si, V, Zn from super-learned models at 50 m, test R² ~0.90 (0.79 Cu to 0.94 SO4), averaged by ZIP code (p. 2).
- NMF with 4–7 factors and 100 runs; 5 factors chosen. Sources: Soil and Crustal Dust (Si, Ca); Heavy Fuel Oil and Industrial (Ni, V, EC, Cu); Metal Processing Industry and Agricultural (Pb, Zn, NO3); Coal and Oil Combustion and Biomass Burning (SO4, OC, V, K; poorly separated); Motor Vehicle (EC, OC, Fe, Cu) (p. 2–3).
- Mean PM2.5 9.65 µg/m³; Midwest 10.67, Northeast 9.33, South 10.22, West 6.96 (p. 3).
- Racial composition linked to Heavy Fuel Oil/Industrial, Metal Processing/Agricultural and Motor Vehicle PM2.5 → [[neighborhood-racial-composition--pm25-sources--knobel2023socioeconomic]].
- All three SES indicators linked to Soil/Crustal Dust plus the same three sources; strength varied by indicator, e.g., renters weakest for dust but strongest for Heavy Fuel Oil (p. 3, 5) → [[neighborhood-ses--pm25-sources--knobel2023socioeconomic]].
- Coal/Oil/Biomass PM2.5 was lower in more Black, poorer and less educated ZIP codes, contrary to the hypothesis; authors suggest long-range transport and less biomass burning in large cities (p. 3, 5–6).
- Regional modification: associations with PM2.5 mass and all predictors largest in the West; dust–SES associations West > South > Midwest, dissipating in the Northeast (p. 3, 7).
- Multi-predictor sensitivity: poverty reversed direction for three sources, attributed to correlation with other predictors (p. 3).
- Authors link racial patterns to redlining and highway siting (p. 2, 5).
- Authors' limitations: ZIP code unit (within-ZIP error), urban only (p. 7).

## Why it matters for Pablo's work
- Claude's reading: exposure-differential (environmental justice) evidence for PM2.5 components; complements differential-vulnerability findings in [[knobel2025social]]. See [[differential-vulnerability]].
- His framing is on [[2023-paper-pm25-sources-disparities]].

## See also
- [[air-pollution]] · [[differential-vulnerability]] · [[urban-environmental-hazards]]
- Findings: [[neighborhood-racial-composition--pm25-sources--knobel2023socioeconomic]], [[neighborhood-ses--pm25-sources--knobel2023socioeconomic]]

## References
- Knobel, P., Hwang, I., Castro, E., Sheffield, P., Holaday, L., Shi, L., Amini, H., Schwartz, J., & Yitshak Sade, M. (2023). Socioeconomic and racial disparities in source-apportioned PM2.5 levels across urban areas in the contiguous US, 2010. *Atmospheric Environment, 303*, Article 119753. https://doi.org/10.1016/j.atmosenv.2023.119753
