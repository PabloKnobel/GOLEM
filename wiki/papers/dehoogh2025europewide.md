---
type: paper
title: "A Europe-wide characterization of the external exposome: A spatio-temporal analysis"
citekey: dehoogh2025europewide
aliases: [EXPANSE exposome maps, EXPANSE external exposome paper]
authors: ["de Hoogh, K.", "Hoek, G.", "Flückiger, B.", "Bussalleu, A.", "Vienneau, D.", "Jeong, A.", "Probst-Hensch, N.", "de Pinho, M. G. M.", "Mackenbach, J. D.", "Lakerveld, J.", "Beulens, J. W. J.", "Castagné, R.", "Delpierre, C.", "Kelly-Irving, M.", "Shen, Y.", "Huss, A.", "Dadvand, P.", "Cirach Pradas, M.", "Nieuwenhuijsen, M.", "Vlaanderen, J.", "Vermeulen, R."]
year: 2025
journal: "Environment International"
volume: 200
issue: ""
pages: "109542"
doi: "10.1016/j.envint.2025.109542"
endnote_id: ""
apa: "de Hoogh, K., Hoek, G., Flückiger, B., Bussalleu, A., Vienneau, D., Jeong, A., Probst-Hensch, N., de Pinho, M. G. M., Mackenbach, J. D., Lakerveld, J., Beulens, J. W. J., Castagné, R., Delpierre, C., Kelly-Irving, M., Shen, Y., Huss, A., Dadvand, P., Cirach Pradas, M., Nieuwenhuijsen, M., Vlaanderen, J., & Vermeulen, R. (2025). A Europe-wide characterization of the external exposome: A spatio-temporal analysis. Environment International, 200, Article 109542. https://doi.org/10.1016/j.envint.2025.109542"
fulltext: read
fulltext_version: "publisher PDF (open access, CC BY), pp. 1–13; supplement not read; reference list skimmed"
metadata_checked: true
metadata_source: "CrossRef, 2026-11-18"
design: exposure-assessment study (model development and spatio-temporal correlation analysis)
population: "120,264 random building-façade points stratified by population density within NUTS1 regions"
setting: "Europe (EU27 minus Malta and Cyprus, plus UK, Norway, Switzerland, Serbia, Albania, North Macedonia), 2000–2020"
n: 120264
exposures: ["[[exposome]]", "[[air-pollution]]", "[[ambient-temperature]]", "[[environmental-noise]]", "[[ndvi]]"]
outcomes: []
methods: ["[[multi-exposure-analysis]]"]
datasets: ["[[expanse-project]]"]
supports: []
contradicts: []
replicates: []
extends: []
projects: []
portals: ["[[exposome-research]]", "[[urban-environmental-hazards]]"]
authored_by_pablo: false
tags: [paper, exposure-assessment]
created: 2026-11-18
updated: 2026-11-18
last_verified: 2026-11-18
confidence: high
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** The EXPANSE project built harmonised, fine-resolution maps of 33 external exposome factors for Europe, 2000–2020: air pollution, noise, temperature, green, blue and grey space, light-at-night, walkability and degree of urbanisation. Most factors were only weakly correlated with each other. The spatial contrasts stayed stable over time ([[dehoogh2025europewide]], p. 1–2). The authors' conclusion is that multi-exposure models are feasible, and that modest temporal misalignment between exposure maps and cohort follow-up is "not critical" (p. 2, 13). The maps are open via the Exposome maps platform (p. 13).

## Key points
- **Models.** NO2, PM2.5, PM10 and O3: annual and monthly, 2000–2019, 25 × 25 m, built with geographically weighted regression. Hold-out R² was 0.66 (NO2), 0.77 (PM10), 0.62 (PM2.5) and 0.58 (O3) (p. 3).
  - Road-traffic noise: CNOSSOS-EU, modelled at building façades for 2019 only. Lden correlated R 0.52–0.77 with national models, and 0.39 in Stockholm (p. 3).
  - Daily temperature: random forest, 1 × 1 km, 2003–2020. CV R² 0.96 (p. 4).
- **Built environment** (p. 4–5):
  - NDVI and MSAVI from MODIS at 250 m, for 2000, 2005, 2010, 2015 and 2020, in 300, 500 and 1000 m buffers.
  - Distance to green space (CORINE and Urban Atlas), distance to blue space (EU-Hydro), imperviousness (Copernicus), light-at-night (DMSP and VIIRS).
  - A Europe-wide walkability index with eight components, including NDVI and distance to green space; it correlated R ≈ 0.5 with a Dutch index.
- **Gaps.** No harmonised food or social environment (SES or deprivation) could be built at Europe scale. OSM food data were adequate only in the Randstad, Barcelona and Basel (p. 5, 12).
- **Cross-factor correlations** (Europe-wide, 2019/2020) were mostly weak (R < 0.4) (p. 8, Fig. 3a):
  - PM2.5 vs PM10: R 0.93.
  - NO2 vs PMs: R ~0.40. NO2 vs O3: R −0.37.
  - Noise vs everything else: R −0.23 to 0.28.
  - NO2 was the exception, correlating with imperviousness (R 0.75), light-at-night (0.65), NDVI and MSAVI (−0.67) and walkability (0.63).
- **Country-level correlations can reverse sign.**
  - O3 vs temperature is positive Europe-wide (R 0.35–0.43) but negative within most countries (median R −0.43 to −0.29) (p. 8).
  - O3 vs NDVI is weak Europe-wide (R 0.10) but moderate within countries (median R 0.56) (p. 8).
  - The authors advise country-specific analyses alongside pooled ones (p. 13).
- **Stability, 2000 vs 2019/20:** strong to very strong at the European level for every factor except O3 (R 0.66). Some exceptions within countries, e.g. PM2.5 in the Netherlands R 0.45 (p. 8, Fig. 4).
- **Trends, population-weighted** (p. 8–9):
  - NO2, PM10 and PM2.5 declined in all countries, with smaller decreases in Eastern Europe.
  - Mean temperature rose 0.6 °C (2005–2020).
  - NDVI and MSAVI rose slightly. Imperviousness rose 0.7–11.4 % by country.
  - Light-at-night and O3 trends were mixed.
- **Limitation:** correlations between modelled exposures partly reflect shared predictors. For example, imperviousness is an input to both the air-pollution and temperature models (p. 10, 12).

## Why it matters for Pablo's work
- Claude's reading: this is the exposure backbone of [[expanse-project]] and a concrete template for a harmonised multi-country urban-exposome database. It is relevant to [[r01-urban-exposome-aging]] and to EU grant planning (not tagged; Pablo to decide). It covers green space only as greenness and distance, with no quality measures.

## See also
- [[exposome]] · [[multi-exposure-analysis]] · [[ndvi]] · [[expanse-project]] · [[exposome-research]]

## References
- de Hoogh, K., Hoek, G., Flückiger, B., Bussalleu, A., Vienneau, D., Jeong, A., Probst-Hensch, N., de Pinho, M. G. M., Mackenbach, J. D., Lakerveld, J., Beulens, J. W. J., Castagné, R., Delpierre, C., Kelly-Irving, M., Shen, Y., Huss, A., Dadvand, P., Cirach Pradas, M., Nieuwenhuijsen, M., Vlaanderen, J., & Vermeulen, R. (2025). A Europe-wide characterization of the external exposome: A spatio-temporal analysis. *Environment International, 200*, Article 109542. https://doi.org/10.1016/j.envint.2025.109542
