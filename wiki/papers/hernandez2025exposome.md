---
type: paper
title: "The exposome of healthy and accelerated aging across 40 countries"
citekey: hernandez2025exposome
aliases: [biobehavioral age gaps 40 countries, BBAG Nature Medicine 2025]
authors: ["Hernandez, H.", "Santamaria-Garcia, H.", "Moguilner, S.", "Farina, F. R.", "Legaz, A.", "Prado, P.", "Cuadros, J.", "Gonzalez, L.", "Gonzalez-Gomez, R.", "Migeot, J.", "Coronel-Oliveros, C.", "Tagliazucchi, E.", "Maito, M. A.", "Godoy, M. E.", "Cruzat, J.", "Shaheen, A.", "Farombi, T.", "Salazar, D.", "Da Ros, L. U.", "Borelli, W. V.", "Zimmer, E. R.", "Njamnshi, A. K.", "Bajpai, S.", "Dey, A. B.", "Mostert, C.", "Merali, Z.", "Salama, M.", "Moustafa, S. A.", "Fittipaldi, S.", "Altschuler, F.", "Medel, V.", "Huepe, D.", "Yaffe, K.", "Momoh, C.", "Eyre, H. A.", "Swieboda, P.", "Lawlor, B.", "Miranda, J. J.", "Duran-Aniotz, C.", "Baez, S.", "Ibanez, A."]
year: 2025
journal: "Nature Medicine"
volume: 31
issue: 9
pages: "3089–3100"
doi: "10.1038/s41591-025-03808-2"
endnote_id: ""
apa: "Hernandez, H., Santamaria-Garcia, H., Moguilner, S., Farina, F. R., Legaz, A., Prado, P., Cuadros, J., Gonzalez, L., Gonzalez-Gomez, R., Migeot, J., Coronel-Oliveros, C., Tagliazucchi, E., Maito, M. A., Godoy, M. E., Cruzat, J., Shaheen, A., Farombi, T., Salazar, D., Da Ros, L. U., Borelli, W. V., Zimmer, E. R., Njamnshi, A. K., Bajpai, S., Dey, A. B., Mostert, C., … Ibanez, A. (2025). The exposome of healthy and accelerated aging across 40 countries. Nature Medicine, 31(9), 3089–3100. https://doi.org/10.1038/s41591-025-03808-2"
fulltext: read
fulltext_version: "publisher PDF incl. Methods and Extended Data legends; reference list and Supplementary Information not read"
metadata_checked: true
metadata_source: "CrossRef, 2026-11-18"
design: multi-country cross-sectional and two-wave longitudinal analysis of harmonized national aging surveys; machine-learning age prediction
population: "161,981 adults without dementia, mean age 67.06 (s.d. 9.85), 45.09% female; longitudinal n = 21,631; South Africa analyzed separately (n = 5,431)"
setting: "40 countries (Latin America and Caribbean, Europe, Asia, Africa); surveys incl. SHARE, ELSI-Brazil, ENASEM, CRELES, CLHLS, KLoSA, LASI, SABE"
n: 161981
exposures: ["[[exposome]]", "[[social-exposome]]", "[[air-pollution]]"]
outcomes: ["[[biobehavioral-age-gap]]"]
methods: []
datasets: []
supports: []
contradicts: []
replicates: []
extends: []
projects: []
portals: ["[[exposome-research]]", "[[urban-nature-and-aging]]"]
authored_by_pablo: false
tags: [paper, aging, cross-national]
created: 2026-11-18
updated: 2026-11-18
last_verified: 2026-11-18
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** The authors estimated a [[biobehavioral-age-gap]] (BBAG) for 161,981 older adults in 40 countries: the gap between an age predicted from protective and risk factors and chronological age. Larger gaps (accelerated aging) were seen in Africa and Latin America than in Europe, in lower-income countries, and where country-level exposome indicators were adverse: PM2.5, Gini index, gender inequality, migration and democracy indices (combined d = 0.53). Larger gaps predicted later functional and cognitive decline ([[hernandez2025exposome]], p. 3089–3092). All exposome measures are **country-level** and assigned by country and year of interview (Methods).

## Key points
- **Predicting age.** A gradient-boosting model predicted chronological age from cognition, functional ability, education, hypertension, diabetes, heart disease, female sex, and visual and hearing impairment (R² 0.26, r 0.51, RMSE 8.47 years) (p. 3090).
  - Top protective factors: functional ability, education, cognition. Top risk factors: hearing impairment, heart disease, hypertension (p. 3090).
- **Regional gradient** (Cliff's δ):
  - Egypt vs Europe δ 0.73; Latin America vs Europe δ 0.52; Asia vs Europe δ 0.31 (p. 3090).
  - Within Europe: eastern vs western δ 0.52 (p. 3090).
  - Lower- vs higher-income countries: GNI δ 0.48, GDP δ 0.56 (p. 3090).
- **Country-level exposome** (p. 3090, 3092; Methods):
  - All factors combined: d = 0.53. Social and physical: d 0.50. Sociopolitical: d 0.44. Each factor on its own: d > 0.37.
  - Factors: PM2.5 exposure (World Bank), Gini index, gender inequality index, migrant share, and five Global State of Democracy indicators.
  - Robust to adjusting for individual SES (p. 3094) and stronger in women (p. 3094).
- **Longitudinal** (two waves, n = 21,631): wave-1 BBAG predicted wave-2 functional ability (r −0.33, d 0.70), cognition (r −0.22, d 0.44) and wave-2 BBAG (r 0.61). The link with well-being was negligible (p. 3092).
- **Risk metrics, dichotomized BBAG > 0** (p. 3092):
  - Cross-sectional: OR 7.64 (7.13–8.19) for reduced functional ability, OR 4.41 (4.11–4.74) for poorer cognition.
  - Longitudinal: RR 1.40 (1.36–1.44) for functional decline, RR 1.25 (1.22–1.29) for cognitive decline.
  - Meta-analyses across countries showed high heterogeneity (p. 3092).
- **Limitations stated by the authors** (p. 3097–3098):
  - Associations only, not causal.
  - Smoking, social isolation and biomarkers not included.
  - Few African participants.
  - Only two waves.
  - Possible biases in the democracy indices.
  - Mean imputation of missing data.

> [!uncertain] Source inconsistencies (Pablo to review)
> - **Country count.** The title and abstract say 40 countries, but Results list 6 Latin American + 27 European + 4 Asian + 2 African = 39 (p. 3090). The Ethics section mentions Uruguay SABE, which is absent from Table 1 (p. 3091; Methods).
> - **BBAG sign.** The introduction defines BBAG as chronological minus predicted age (p. 3089–3090), but Fig. 1 and the Methods define it as predicted minus chronological, with BBAG > 0 meaning accelerated aging.
> - **South Africa.** "Larger BBAGs in wave 1 predicted larger BBAGs in wave 2", yet the reported r is −0.90 (Extended Data Fig. 5b; p. 3092).
> - **Wave adjustment.** Wave-1 BBAGs were divided by the time between waves (Methods). The effect of this on interpretation is not discussed.

## Why it matters for Pablo's work
- Claude's reading: a large, high-profile frame for "exposome → accelerated aging" in which air quality is a country-level PM2.5 indicator and there are no built-environment or green-space measures. That leaves room for small-area urban-exposome work.
  - Possibly relevant to [[r01-urban-exposome-aging]] and [[ryc-2026]] (not tagged; Pablo to decide).
  - Same senior group as [[migeot2025social]] and [[ibanez2024neuroecological]].

## See also
- [[biobehavioral-age-gap]] · [[exposome]] · [[social-exposome]] · [[phenotypic-age]] · [[exposome-research]]

## References
- Hernandez, H., Santamaria-Garcia, H., Moguilner, S., Farina, F. R., Legaz, A., Prado, P., … Ibanez, A. (2025). The exposome of healthy and accelerated aging across 40 countries. *Nature Medicine, 31*(9), 3089–3100. https://doi.org/10.1038/s41591-025-03808-2
