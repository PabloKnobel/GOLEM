---
type: concept
title: "Air pollution"
aliases: [ambient air pollution, PM2.5, fine particulate matter, NO2, nitrogen dioxide, traffic-related air pollution, PM2.5 components, source-apportioned PM2.5, extreme air pollution events]
kind: exposure
related: ["[[ambient-temperature]]", "[[environmental-noise]]"]
part_of: []
projects: []
portals: ["[[urban-environmental-hazards]]"]
tags: [concept]
created: 2026-11-15
updated: 2026-11-15
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**Lead.** Ambient pollutants such as fine particulate matter (PM2.5) and nitrogen dioxide (NO2), central exposures in environmental epidemiology. In the vault so far they appear as an exposure for children's glycemia ([[wu2025air]]) and as a co-exposure or confounder for noise and dementia ([[hwang2025comprehensive]], p. 8).

> [!info] Infobox
> **Kind:** exposure · **Pollutants in vault:** PM2.5, NO2 · **Exposure models:** daily 1-km hybrid satellite and machine-learning models (Mexico City) · **Key sources:** [[wu2025air]]

## Definition and measurement
- Daily 1-km PM2.5 from gradient boosting with aerosol optical depth, meteorology and land use; NO2 from a hybrid ensemble (XGBoost, random forest, geostatistics, remote sensing) ([[wu2025air]], p. 2).
- Daily 1-km PM2.5 for the New York metro from XGBoost with satellite AOD and land use, RMSE 3.11 µg/m³ in spatial cross-validation ([[knobel2024association]], p. 89).
- 14 PM2.5 components from 50-m urban super-learned models were factored by non-negative matrix factorization into five source categories (soil and crustal dust; heavy fuel oil and industrial; metal processing industry and agricultural; coal and oil combustion and biomass burning; motor vehicle) ([[knobel2023socioeconomic]], p. 2–3).
- Annual 14-component predictions factored by NMF into biomass burning, oil combustion, metal industry, other industries, and motor vehicles/resuspended dust, linked to Tri-state residential histories ([[krasnov2026association]], p. 498).

## Evidence
- PM2.5: +0.311% HbA1c per 1 µg/m³ in Mexico City children, adjusting for NO2 and temperature ([[wu2025air]], p. 3) → [[pm25--hba1c--wu2025air]]; larger at older ages → [[pm25--hba1c--wu2025air-by-age]].
- NO2: no association with HbA1c ([[wu2025air]], p. 3) → [[no2--hba1c--wu2025air]].
- In noise–dementia studies, four of seven adjusted for air pollution and three examined joint effects ([[hwang2025comprehensive]], p. 8).
- Greenspace does not substantially filter air pollution and can raise ozone ([[markevych2017exploring]], p. 303).
- PM2.5 6-month mean: +0.78 mg/dL glucose and +1.67 mg/dL total cholesterol per IQR in WTC responders; 1-week windows null ([[knobel2024association]], p. 90–91) → [[pm25--glucose--knobel2024association]], [[pm25--total-cholesterol--knobel2024association]].
- Extreme event: high WTC disaster exposure (2001) associated with +0.82 mg/dL glucose, independent of later PM2.5 ([[knobel2024association]], p. 91) → [[wtc-exposure--glucose--knobel2024association]].
- PM2.5–glucose association much larger with diabetes ([[knobel2024association]], p. 91) → [[pm25--glucose--knobel2024association-by-diabetes]].
- Exposure disparities: higher PM2.5 and several source categories in urban US ZIP codes with more non-Hispanic Black residents and lower SES; coal/oil/biomass PM2.5 inversely associated ([[knobel2023socioeconomic]], p. 3) → [[neighborhood-racial-composition--pm25-sources--knobel2023socioeconomic]], [[neighborhood-ses--pm25-sources--knobel2023socioeconomic]].
- Long-term source-apportioned PM2.5: metal-industry PM2.5 associated with diabetes incidence (+8.35%) and glucose (+1.31%) per IQR; annual total PM2.5 mass null in WTC responders ([[krasnov2026association]], p. 501) → [[metal-industry-pm25--diabetes--krasnov2026association]], [[metal-industry-pm25--glucose--krasnov2026association]].
- Sex differences in source-specific glucose associations ([[krasnov2026association]], p. 499) → [[pm25-sources--glucose--krasnov2026association-by-sex]].

## Pablo's framing
- [[2025-paper-air-pollution-temperature-hba1c-children]]: exposures "do not present in isolation" (p. 2).
- [[2024-paper-wtc-air-pollution-glucose-lipids]]: extreme events as a climate-relevant exposure, WTC compared to wildfires (p. 88).
- [[2023-paper-pm25-sources-disparities]]: sources, not only mass, drive disparities (p. 2).
- [[2026-paper-pm25-sources-diabetes-wtc]] (co-author): source effects "masked" in PM2.5 mass (p. 500).

## Open questions
- Source-specific PM2.5 effects ([[wu2025air]], p. 5).

## See also
- [[ambient-temperature]] · [[environmental-noise]] · [[cardiometabolic-health]] · [[urban-environmental-hazards]]
- [[multi-exposure-analysis]]

## References
- Wu, J., et al. (2025). Air pollution, temperature, and HbA1c levels among children in Mexico City, Mexico. *Ecotoxicology and Environmental Safety, 307*, Article 119424.
- Hwang, S. A., et al. (2025). A comprehensive systematic review and meta-analysis to unravel the noise-dementia nexus. *Public Health Reviews, 46*, Article 1607355.
- Markevych, I., et al. (2017). Exploring pathways linking greenspace to health: Theoretical and methodological guidance. *Environmental Research, 158*, 301–317.
- Knobel, P., Just, A. C., Colicino, E., Teitelbaum, S. L., McLaughlin, M. A., Amini, H., & Yitshak Sade, M. (2024). The association of air pollution exposure with glucose and lipid levels: The role of an extreme air pollution event alongside 2 decades of moderate exposure. *American Journal of Epidemiology, 193*(1), 87–95.
- Knobel, P., Hwang, I., Castro, E., Sheffield, P., Holaday, L., Shi, L., Amini, H., Schwartz, J., & Yitshak Sade, M. (2023). Socioeconomic and racial disparities in source-apportioned PM2.5 levels across urban areas in the contiguous US, 2010. *Atmospheric Environment, 303*, Article 119753.
- Krasnov, H., Knobel, P., Hsu, H.-H. L., Teitelbaum, S. L., McLaughlin, M. A., Just, A. C., Kloog, I., & Yitshak-Sade, M. (2026). The association between long-term exposure to PM2.5 constituents and diabetes incidence and blood glucose levels among World Trade Center Health Program general responders. *American Journal of Epidemiology, 195*(2), 497–504.
