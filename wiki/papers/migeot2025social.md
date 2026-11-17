---
type: paper
title: "Social exposome and brain health outcomes of dementia across Latin America"
citekey: migeot2025social
aliases: [multidimensional social exposome dementia, MSE ReDLat, social exposome Latin America dementia]
authors: ["Migeot, J.", "Pina-Escudero, S. D.", "Hernandez, H.", "Gonzalez-Gomez, R.", "Legaz, A.", "Fittipaldi, S.", "Resende, E. d. P. F.", "Duran-Aniotz, C.", "Avila-Funes, J. A.", "Behrens, M. I.", "Bruno, M. A.", "Cardona, J. F.", "Custodio, N.", "García, A. M.", "Godoy, M. E.", "Hu, K.", "Lanata, S.", "Lawlor, B.", "Lopera, F.", "Maito, M. A.", "Matallana, D. L.", "Miller, B.", "Miranda, J. J.", "Okada de Oliveira, M.", "Reyes, P.", "Santamaria-Garcia, H.", "Slachevsky, A.", "Sosa, A. L.", "Takada, L. T.", "Torres, J. M.", "Vanneste, S.", "Valcour, V.", "Wen, O.", "Yokoyama, J. S.", "Possin, K. L.", "Ibanez, A."]
year: 2025
journal: "Nature Communications"
volume: 16
article_number: 8196
doi: "10.1038/s41467-025-63277-6"
endnote_id: ""
apa: "Migeot, J., Pina-Escudero, S. D., Hernandez, H., Gonzalez-Gomez, R., Legaz, A., Fittipaldi, S., Resende, E. d. P. F., Duran-Aniotz, C., Avila-Funes, J. A., Behrens, M. I., Bruno, M. A., Cardona, J. F., Custodio, N., García, A. M., Godoy, M. E., Hu, K., Lanata, S., Lawlor, B., Lopera, F., . . . Ibanez, A. (2025). Social exposome and brain health outcomes of dementia across Latin America. Nature Communications, 16, Article 8196. https://doi.org/10.1038/s41467-025-63277-6"
fulltext: read
metadata_checked: true
metadata_source: "CrossRef, 2026-11-17"
metadata_note: "CrossRef lists 'de Oliveira, Maira Okada' and 'Jaime Miranda, J.'; kept the article's order (Okada de Oliveira, M.; Miranda, J. J.)"
design: cross-sectional, multicenter clinical sample; structural equation modeling, Lasso, VBM and rsfMRI
population: "2,211 adults (1,175 healthy controls, 781 Alzheimer's disease, 255 FTLD) from the ReDLat consortium"
setting: "Argentina, Brazil, Chile, Colombia, Mexico, Peru"
n: 2211
exposures: ["[[social-exposome]]"]
outcomes: ["[[dementia]]"]
methods: [structural equation modeling, confirmatory factor analysis, Lasso regression, bootstrap meta-regression, voxel-based morphometry, ROI-to-ROI functional connectivity]
datasets: []
supports: []
contradicts: []
replicates: []
extends: ["[[gudimindermann2023integrating]]"]
projects: []
portals: ["[[exposome-research]]"]
authored_by_pablo: false
tags: [paper]
created: 2026-11-17
updated: 2026-11-17
last_verified: 2026-11-17
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**TL;DR.** In 2,211 healthy controls and people with Alzheimer's disease (AD) or frontotemporal lobar degeneration (FTLD) from six Latin American countries, a latent multidimensional social exposome (MSE) score from ten self-reported lifespan dimensions was associated with worse cognition, functional ability and neuropsychiatric symptoms, and in AD and FTLD with lower gray matter volume and altered connectivity in fronto-temporo-limbic and cerebellar regions; the combined score outperformed single dimensions ([[migeot2025social]], p. 1, 3–6). Cross-sectional, non-representative clinical sample.

## Evidence table
| Design | N | Population / setting | Exposure (metric) | Outcome | Main estimate (95% CI) | Adjusted for |
|---|---|---|---|---|---|---|
| Cross-sectional SEM, multicenter | 2,211 (MRI 875; rsfMRI 500) | HC, AD, FTLD; ReDLat, 6 Latin American countries | Latent MSE score from 10 dimensions (education, food insecurity, financial status, assets, healthcare access, childhood labor, subjective SES, childhood experiences, traumatic events, relationships), ages 0–10, 35–45, recent | MMSE; Pfeffer FAQ; NPI-Q (FAQ and NPI-Q inverted) | Whole sample, standardized β: cognition 0.261 (0.18–0.282); functional ability 0.079 (0.015–0.11); neuropsychiatric 0.105 (0.033–0.132) | Sensitivity: age, sex, disease severity, age at diagnosis, years since diagnosis, FTLD subtype, country; imaging: age, sex, TIV, scanner |

## Key points
- MSE built from 319 items, min–max scaled and averaged into 10 dimension scores, then one SEM latent factor; questionnaire co-designed by ReDLat and UCSF, building on PRAPARE and ELCSA; full questionnaire on OSF (p. 2, 11–12).
- Top loadings, whole sample: education 0.732, food insecurity 0.702, financial status 0.694, assets 0.649, healthcare access 0.506 (p. 3–4).
- Healthy controls: MSE associated with cognition (β 0.610, 0.463–0.737) but not functional ability or neuropsychiatric symptoms (floor effects, per authors) (p. 4, 9) → [[social-exposome--cognition--migeot2025social-healthy-aging]].
- AD and FTLD: associations with all three domains (β 0.079–0.229 in AD; 0.140–0.165 in FTLD) (p. 4).
- Global MSE vs single dimensions (Lasso, bootstrap meta-regression): larger common effect for cognition in all subjects, 0.23 vs 0.12 (p. 4, 6, Table 2) → [[social-exposome--dementia--migeot2025social]].
- Brain: in AD, lower gray matter volume in frontal, insular and cerebellar regions; in FTLD, vermis, superior temporal, frontal and anterior cingulate (TFCE, pFDR < 0.05) (p. 4–5, 8, Tables 3–4); both lower and higher (interpreted as compensatory) connectivity (p. 5, 7).
- Sensitivity: robust to demographic, disease-related, country and scanner covariates, excluding education, and no imputation (p. 6).
- Authors' limitations: self-report (caregiver-corroborated), three life stages only, no aggregate or geocoded data, no discrimination or ancestry, no amyloid/tau biomarkers, clinical non-representative samples (p. 10–11).
- Authors call for nested spatial-buffer analyses (block 0–100 m to city 5–50 km) and geocoded air pollution and green space access in future work (p. 10–11).

> [!uncertain] Source inconsistencies
> - Direction of scaling: Fig. 1 caption says higher values = lower adversity (p. 3); Methods says 0 and 1 indicate "lower and higher levels of adversity" (p. 12).
> - Healthy controls, functional ability: β = −0.047 with 95% CI −0.026 to 0.073 (point estimate outside its CI); neuropsychiatric β = −0.032 with CI −0.114 to −0.002 but p = 0.259 (p. 4).
> - Methods says the smallest group (FTLD) had "225 participants"; Table 1 gives 255 (p. 4, 14).

## Why it matters for Pablo's work
- Claude's reading: the most fully operationalized individual-level social exposome in the vault, applied to aging and dementia; its explicit gap — no geocoded neighborhood exposures such as green space — is where Pablo's urban exposome work sits ([[r01-urban-exposome-aging]]; not tagged, Pablo to decide).
- Companion framing piece from the same senior author: [[ibanez2024neuroecological]].

## See also
- [[social-exposome]] · [[dementia]] · [[exposome-research]] · [[social-hallmarks-of-aging]]
- Findings: [[social-exposome--dementia--migeot2025social]], [[social-exposome--cognition--migeot2025social-healthy-aging]]

## References
- Migeot, J., Pina-Escudero, S. D., Hernandez, H., Gonzalez-Gomez, R., Legaz, A., Fittipaldi, S., Resende, E. d. P. F., Duran-Aniotz, C., Avila-Funes, J. A., Behrens, M. I., Bruno, M. A., Cardona, J. F., Custodio, N., García, A. M., Godoy, M. E., Hu, K., Lanata, S., Lawlor, B., Lopera, F., . . . Ibanez, A. (2025). Social exposome and brain health outcomes of dementia across Latin America. *Nature Communications, 16*, Article 8196. https://doi.org/10.1038/s41467-025-63277-6
