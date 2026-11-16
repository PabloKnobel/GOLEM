---
type: paper
title: "Social hallmarks of aging: Suggestions for geroscience research"
citekey: crimmins2020social
aliases: [Crimmins 2020, social hallmarks of aging paper]
authors: ["Crimmins, E. M."]
year: 2020
journal: "Ageing Research Reviews"
volume: 63
issue: ""
pages: "101136"
doi: "10.1016/j.arr.2020.101136"
endnote_id: ""
apa: "Crimmins, E. M. (2020). Social hallmarks of aging: Suggestions for geroscience research. Ageing Research Reviews, 63, Article 101136. https://doi.org/10.1016/j.arr.2020.101136"
fulltext: read
metadata_checked: true
metadata_source: "CrossRef, 2026-11-15"
design: perspective with cross-sectional analysis (2-year mortality follow-up)
population: "Older US adults with 2016 venous blood data, Health and Retirement Study (paper says both 'over the age of 50' and 'over the age of 56', p. 5)"
setting: "United States, 2016"
n: 1159
exposures: ["[[social-hallmarks-of-aging]]", biological age, epigenetic age acceleration, telomere length, mtDNA copy number, polygenic scores]
outcomes: [ADL/IADL difficulty, multimorbidity, cognitive dysfunction, 2-year mortality]
methods: [linear regression, Shapley R² decomposition]
datasets: ["[[health-and-retirement-study]]"]
supports: []
contradicts: []
replicates: []
extends: ["[[kennedy2014geroscience]]"]
projects: ["[[r01-urban-exposome-aging]]"]
portals: ["[[urban-nature-and-aging]]"]
tags: [paper, perspective, aging, social-determinants]
created: 2026-11-15
updated: 2026-11-16
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** Crimmins proposes "social hallmarks of aging" (low SES, minority status, adversity, adverse psychological states, adverse behaviors) as the social analogue of the geroscience hallmarks. In 1,159 HRS participants, social factors explained 1.8 to 6.1 times more outcome variance than measured biological aging indicators, and adding biology left most social variance unexplained ([[crimmins2020social]], p. 1, 7).

> [!todo] Metadata not verified against CrossRef (WebFetch not approved in this run). Metadata from the PDF (p. 1). Table 1 (t-value heat map) and Fig. 2 are images whose text extraction is garbled; individual t values were not used.

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| Largely cross-sectional regressions; 2-year mortality | 1,159 (832 for polygenic model) | HRS 2016 Venous Blood Study, older US adults (age floor stated as both 50 and 56, p. 5) | Social hallmarks vs. biological measures (bio age − chronological age, Horvath epigenetic age acceleration, telomere length, mtDNA copy number) | ADL/IADL difficulty, multimorbidity (5 diseases), cognitive dysfunction, mortality | Ratio of R² explained, social vs. biological: mortality 1.8; multimorbidity 1.36; cognition 4.7; physical functioning 6.1 (no CIs) | Age, sex |

## Key points
- Social hallmarks: low socioeconomic status, minority status, adverse life events, adverse psychological states, adverse behaviors (p. 1, Fig. 1 p. 2); framed with Link and Phelan's "fundamental cause" (p. 2).
- Biological-only model (with age and sex): biological variables explained 9% of variance in mortality, 8% in cognitive dysfunction, 10% in number of diseases, 6% in physical functioning; bio age − chronological age was strongly linked to all outcomes, epigenetic age acceleration to physical functioning and diseases, other hallmark markers not significant (p. 7) → [[biological-aging-measures--age-related-health-outcomes--crimmins2020social]].
- Joint model: social variables explained more variance than biological ones for every outcome (ratios above) → [[social-hallmarks-of-aging--age-related-health-outcomes--crimmins2020social]].
- Social-only model: social hallmarks explained most of the explained variance except mortality (mostly age and sex); mortality and cognition had the most variance explained, 25–30% (p. 7).
- Polygenic scores (non-Hispanic whites) explained ~3% of mortality and ~1% of cognitive variance (p. 7).
- Limitations stated: missingness reduced 4,018 to 1,159, and missing people were more often minority, less educated, more impaired and more likely to die; mortality covers only two years (p. 5, 7). Data "largely cross-sectional" (p. 5).
- Conclusion: hallmark-level biology "did not provide much explanation of social variability in aging"; biologists should build social hallmarks into experimental designs (p. 7).

## Why it matters for Pablo's work
- Claude's reading: supports treating neighborhood and social context as upstream determinants of aging outcomes rather than only as confounders; links [[geroscience]] to the [[social-exposome]] view.

## See also
- extends: [[kennedy2014geroscience]] · [[social-hallmarks-of-aging]] · [[geroscience]] · [[health-and-retirement-study]]

## References
- Crimmins, E. M. (2020). Social hallmarks of aging: Suggestions for geroscience research. *Ageing Research Reviews, 63*, Article 101136. https://doi.org/10.1016/j.arr.2020.101136
