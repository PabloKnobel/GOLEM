---
type: paper
title: "Quality of urban green spaces influences residents' use of these spaces, physical activity, and overweight/obesity"
citekey: knobel2021quality
aliases: [Knobel 2021 quality, RECITAL health study, UGS quality physical activity obesity Barcelona]
authors: ["Knobel, P.", "Maneja, R.", "Bartoll, X.", "Alonso, L.", "Bauwelinck, M.", "Valentin, A.", "Zijlema, W.", "Borrell, C.", "Nieuwenhuijsen, M.", "Dadvand, P."]
year: 2021
journal: "Environmental Pollution"
volume: 271
issue: "?"
pages: "Article 116393"
doi: "10.1016/j.envpol.2020.116393"
endnote_id: ""
apa: "Knobel, P., Maneja, R., Bartoll, X., Alonso, L., Bauwelinck, M., Valentin, A., Zijlema, W., Borrell, C., Nieuwenhuijsen, M., & Dadvand, P. (2021). Quality of urban green spaces influences residents' use of these spaces, physical activity, and overweight/obesity. Environmental Pollution, 271, Article 116393. https://doi.org/10.1016/j.envpol.2020.116393"
fulltext: read
metadata_checked: true
metadata_source: "CrossRef, 2026-11-15"
design: cross-sectional (health survey linked to in-situ audits)
population: "2,053 adults in the 2016 Barcelona Health Survey with ≥1 UGS within 300 m"
setting: "Barcelona, Spain; survey 2016, audits March–May 2018"
n: 2053
exposures: ["[[green-space-quality-assessment]]", RECITAL overall and 10 dimension scores (mean and maximum, 300 m)]
outcomes: ["[[physical-activity]]", "[[cardiometabolic-health]]", "[[green-space-use]]"]
methods: [logistic regression, negative binomial regression, bootstrapped mediation, likelihood ratio interaction tests]
datasets: ["[[recital]]", Barcelona Health Survey 2016]
supports: []
contradicts: []
replicates: []
extends: ["[[knobel2021development]]"]
projects: ["[[ryc-2026]]"]
portals: ["[[urban-green-space-quality]]"]
authored_by_pablo: true
tags: [paper, my-paper, cross-sectional, green-space-quality, mediation]
created: 2026-11-15
updated: 2026-11-15
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** In 2,053 Barcelona adults, an IQR higher mean RECITAL overall quality of green spaces within 300 m was associated with higher odds of moderate-to-vigorous physical activity (OR 1.13; 1.00–1.27), lower odds of overweight/obesity (OR 0.88; 0.79–0.98) and more weekly green space use (ERC 1.08; 1.01–1.15) ([[knobel2021quality]], p. 6, Table 3). Bird biodiversity and amenities were relevant across outcomes (p. 1, 5). Pablo is first author.

> [!todo] Metadata to verify
> Not checked against CrossRef/OpenAlex (WebFetch not used). Issue: `?`. Available online December 29, 2020 (p. 1). Corresponding author is R. Maneja (p. 1). Stratified results only in Figs. S1–S3 (supplement not in vault).

> [!uncertain] Internal inconsistencies in the source
> - Overall quality–physical activity CI: abstract and Table 3 give 1.00–1.27 (p. 1, 6); Results text gives 1.0–1.31 (p. 4).
> - Bird biodiversity–physical activity CI printed as "1.15" in the text (p. 4); Table 3 gives 1.01–1.31 (p. 6). Bird biodiversity–obesity CI 0.79–0.99 in text (p. 5) vs 0.78–0.99 in Table 3 (p. 6).
> - The abstract states that physical activity "mediates" the quality–overweight/obesity association (p. 1), but that mediation was not statistically significant (9.7%; −1.3% to 42%; p = 0.066) (p. 5, Table 4).
> - RECITAL is described with 10 dimensions and a five-point Likert scale (p. 2); the tool paper describes 11 dimensions scored 0–4 ([[knobel2021development]], p. 2, 4). RECITAL is cited as "Knobel et al., 2020" (p. 2).
> - Exposure (2018 audits) postdates outcomes (2016 survey) (p. 7).

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| Cross-sectional, logistic (p. 3) | 2,053 | Adults, Barcelona 2016 | RECITAL mean overall quality, 300 m, per IQR | Moderate-to-vigorous PA (IPAQ-short) | OR 1.13 (1.00–1.27) (p. 6, Table 3) | Age, sex, education |
| Same | 2,053 | Same | Same | Overweight/obesity (self-reported BMI ≥25) | OR 0.88 (0.79–0.98) | Same |
| Cross-sectional, negative binomial | 2,053 | Same | Same | Days/week in green spaces | ERC 1.08 (1.01–1.15) | Same |

## Key points
- Exposure: 149 public green spaces >1 ha audited with [[recital]] (90 items) by four fieldworkers per site; overall ICC 0.84, Cronbach's alpha 0.92 (p. 2). Mean and maximum scores within 300 m of home (p. 2).
- Exclusions from 4,000 interviewed: <18 y (560), walking limitations (187), no UGS within 300 m (1,778); overlapping criteria (p. 2).
- Sample: 51.6% female; 28.4% moderate-to-vigorous PA; 47.2% overweight/obese; 32.4% reported no weekly UGS visits (p. 4, Table 2).
- Dimensions, mean scores: PA associated with surroundings, facilities, amenities, absence of incivilities, bird biodiversity; overweight/obesity with surroundings, amenities, absence of incivilities, bird biodiversity; use with access, aesthetics, safety, potential use, bird biodiversity (p. 4–6, Table 3).
- Animal (non-bird) biodiversity was null for all outcomes, attributed to near-zero variability (p. 7).
- Mean quality associations were generally stronger than maximum quality (p. 6).
- Mediation: UGS use mediated 9.3% (0.8–47%; p = 0.042) of quality–PA; PA 9.7% (−1.3–42%; p = 0.066) of quality–obesity; use did not mediate quality–obesity (p. 5–6, Table 4) → [[green-space-health-pathways]].
- Effect modification: no significant interactions by sex, age or education (p > 0.10); stratified results suggested stronger protection against overweight/obesity in females and higher education (p. 5) → [[sex-and-gender-effect-modification]].
- Sensitivity: PA and obesity associations lost significance with some added covariates and a 500 m buffer; use associations unchanged (p. 5).
- Test–retest of 14 UGS a year later: ICC 0.85 (p. 7).
- Authors' limitations: cross-sectional, self-reported outcomes, PA not specific to UGS, use question includes non-urban green spaces (p. 7).

## Why it matters for Pablo's work
- Claude's reading: the first health application of [[recital]], linking dimension-level quality to outcomes — direct precedent for [[ryc-2026]] (Catalonia quality surface).
- His framing is on [[2021-paper-green-space-quality-physical-activity-obesity]].

## See also
- extends: [[knobel2021development]] · uses_dataset: [[recital]]
- [[green-space-quality-assessment]] · [[bird-biodiversity]] · [[physical-activity]] · [[green-space-use]]
- Findings: [[green-space-quality--physical-activity--knobel2021quality]], [[green-space-quality--overweight-obesity--knobel2021quality]], [[green-space-quality--green-space-use--knobel2021quality]], [[bird-biodiversity--green-space-use--knobel2021quality]]

## References
- Knobel, P., Maneja, R., Bartoll, X., Alonso, L., Bauwelinck, M., Valentin, A., Zijlema, W., Borrell, C., Nieuwenhuijsen, M., & Dadvand, P. (2021). Quality of urban green spaces influences residents' use of these spaces, physical activity, and overweight/obesity. *Environmental Pollution, 271*, Article 116393. https://doi.org/10.1016/j.envpol.2020.116393
- Knobel, P., Dadvand, P., Alonso, L., Costa, L., Español, M., & Maneja, R. (2021). Development of the urban green space quality assessment tool (RECITAL). *Urban Forestry & Urban Greening, 57*, Article 126895.
