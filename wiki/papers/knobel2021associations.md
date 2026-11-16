---
type: paper
title: "Associations of objective and perceived greenness measures with cardiovascular risk factors in Philadelphia, PA: A spatial analysis"
citekey: knobel2021associations
aliases: [Knobel 2021, Philadelphia greenness CVD, perceived access tree canopy Philadelphia]
authors: ["Knobel, P.", "Kondo, M.", "Maneja, R.", "Zhao, Y.", "Dadvand, P.", "Schinasi, L. H."]
year: 2021
journal: "Environmental Research"
volume: 197
issue: "?"
pages: "Article 110990"
doi: "10.1016/j.envres.2021.110990"
endnote_id: ""
apa: "Knobel, P., Kondo, M., Maneja, R., Zhao, Y., Dadvand, P., & Schinasi, L. H. (2021). Associations of objective and perceived greenness measures with cardiovascular risk factors in Philadelphia, PA: A spatial analysis. Environmental Research, 197, Article 110990. https://doi.org/10.1016/j.envres.2021.110990"
fulltext: read
metadata_checked: true
metadata_source: "CrossRef, 2026-11-15"
design: ecological cross-sectional spatial analysis
population: "377 populated census tracts (adults 18+)"
setting: "Philadelphia, PA, USA, 2013"
n: 377
exposures: ["[[perceived-green-space-access]]", "[[ndvi]]", tree canopy cover, vegetation cover]
outcomes: ["[[cardiometabolic-health]]"]
methods: [spatial lag model, Queen contiguity, effect modification by tertiles]
datasets: [Southeastern Pennsylvania Household Health Survey (SEPAHH), MODIS MOD13Q1, LiDAR land cover, American Community Survey]
supports: []
contradicts: []
replicates: []
extends: []
projects: ["[[ryc-2026]]", "[[greenspace-quality-metric]]"]
portals: ["[[urban-green-space-quality]]"]
authored_by_pablo: true
tags: [paper, my-paper, ecological, effect-modification, exposure-assessment]
created: 2026-11-15
updated: 2026-11-16
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** An ecological spatial analysis of 377 Philadelphia census tracts (2013) compared three objective greenness measures and one perceived access measure against tract prevalence of obesity, high blood pressure and diabetes. High (vs low) perceived park or outdoor space access was associated with −2.68 percentage points obese (95% CI −3.93 to −1.43); tree canopy showed weaker protective associations, and vegetation cover and NDVI were near null ([[knobel2021associations]], p. 1, 4). Pablo is first author.

> [!todo] Metadata to verify
> Not checked against CrossRef (WebFetch unavailable in this run). Issue number not printed in the PDF: `?`.

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| Ecological, spatial lag models (p. 3) | 377 tracts | Philadelphia adults, 2013 | % reporting perceived park/outdoor access, tertile 3 vs 1 | % obese | −2.68 (−3.93 to −1.43) percentage points | Tract poverty, % non-Hispanic Black, population density (tertiles) |
| Same | 377 tracts | Same | % tree canopy cover, tertile 3 vs 1 | % obese | −0.89 (−2.05 to −0.28) | Same |

## Key points
- Exposures: % vegetation and % tree canopy from 1-ft LiDAR/orthophoto land cover (2008 and 2018, interpolated to 2013); annual mean MODIS NDVI at 250 m; % reporting "Is there a park or other outdoor space in your neighborhood that you are comfortable visiting during the day?" (p. 2–3).
- Outcomes: SEPAHH self-reported obesity (height, weight) and ever-diagnosed high blood pressure and diabetes, smoothed with Bayesian hierarchical models (p. 2–3).
- Perceived access, tertile 3 vs 1: obese −2.68 (−3.93 to −1.43); high blood pressure −2.13 (−3.35 to −0.9); diabetes −1.35 (−2.06 to −0.64) (p. 4) → [[perceived-green-space-access--obesity--knobel2021associations]].
- Tree canopy, tertile 3 vs 1: obese −0.89 (−2.05 to −0.28); high blood pressure −0.79 (−1.95 to 0.37); diabetes −0.57 (−1.24 to 0.1); vegetation cover and NDVI close to null; tertile 2 vs 1 null throughout (p. 4) → [[tree-canopy-cover--obesity--knobel2021associations]].
- Objective measures correlated >0.8 with each other; perceived access correlated 0.32 with tree canopy, 0.21 with vegetation, 0.12 with NDVI (p. 4, Table 2).
- Effect modification (little statistical evidence by AIC; imprecise): perceived access–high blood pressure restricted to high (−3.92; −6.42 to −1.42) and medium (−2.08; −3.89 to −0.28) poverty tracts, null in low poverty (0.46; −2.00 to 2.93) (p. 4) → [[perceived-green-space-access--hypertension--knobel2021associations-by-poverty]].
- Tree canopy–obesity appeared restricted to low-poverty tracts (−2.39; −4.26 to −0.52) and low % non-Hispanic Black tracts (−2.38; −4.14 to −0.62) (p. 4).
- Authors link the poverty pattern to the equigenic hypothesis and the racial pattern to structural racism, segregation and differential perception or safety (p. 7).
- Terminology: "greenness" = any vegetated area; "green space" = structured subset (parks, gardens), a distinction that "adds a layer of quality" (p. 2).
- Authors' limitations: ecological fallacy, reverse causation and self-selection, low-quality MODIS pixels not masked, underpowered for effect modification, broad survey question that may capture non-green open space (p. 7–8).

## Why it matters for Pablo's work
- Claude's reading: evidence that perceived, use-relevant measures can outperform satellite greenness, and that associations vary by neighborhood poverty and race; supports the quality argument in [[ryc-2026]] and [[urban-green-space-quality]].
- His framing is on [[2021-paper-greenness-cvd-philadelphia]].

## See also
- [[perceived-green-space-access]] · [[ndvi]] · [[cardiometabolic-health]] · [[green-space-health-pathways]] · [[green-space-quality-assessment]]
- Findings: [[perceived-green-space-access--obesity--knobel2021associations]], [[tree-canopy-cover--obesity--knobel2021associations]], [[perceived-green-space-access--hypertension--knobel2021associations-by-poverty]]
- Extended by [[knobel2026beyond]] (multidimensional urban nature and ASCVD).

## References
- Knobel, P., Kondo, M., Maneja, R., Zhao, Y., Dadvand, P., & Schinasi, L. H. (2021). Associations of objective and perceived greenness measures with cardiovascular risk factors in Philadelphia, PA: A spatial analysis. *Environmental Research, 197*, Article 110990. https://doi.org/10.1016/j.envres.2021.110990
