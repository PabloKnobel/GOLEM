---
type: concept
title: "Biobehavioral age gap (BBAG)"
aliases: [BBAG, biobehavioral age gaps, biobehavioral aging clock, accelerated aging (biobehavioral)]
kind: measure
related: ["[[phenotypic-age]]", "[[geroscience]]", "[[exposome]]"]
part_of: []
projects: []
portals: ["[[urban-nature-and-aging]]", "[[exposome-research]]"]
tags: [concept]
created: 2026-11-18
updated: 2026-11-18
last_verified: 2026-11-18
confidence: low
generated: true
reviewed: false
superseded_by: ""
---

**Lead.** A biobehavioral age gap is the difference between the age a model predicts from biobehavioral protective and risk factors (cognition, functional ability, education, cardiometabolic conditions, sensory impairments) and a person's chronological age. Positive values indicate accelerated aging ([[hernandez2025exposome]], p. 3090, Fig. 1). It is proposed as a low-cost alternative to epigenetic, proteomic or brain clocks for survey data in diverse and low-resource settings (p. 3090, 3094).

> [!info] Infobox
> **Kind:** measure (aging clock) · **Inputs:** cognition, functional ability, education, hypertension, diabetes, heart disease, female sex, visual and hearing impairment (core set) · **Model:** gradient boosting with bias correction for regression to the mean · **Key source:** [[hernandez2025exposome]] (only source so far)

## Definition and measurement
- Gradient boosting trained on 90% of the data with 10-fold cross-validation. The age gap is corrected for regression-to-the-mean bias. Accelerated and delayed groups are the top and bottom quartiles ([[hernandez2025exposome]], Methods).
- Prediction accuracy in the full sample was modest: R² 0.26, r 0.51, RMSE 8.47 years (p. 3090).
- The paper defines the sign inconsistently (see [[hernandez2025exposome]]).

## Evidence
- Larger in lower-income countries and in Africa and Latin America than in Europe. Associated with adverse country-level exposome indicators: PM2.5, inequality, democracy indices (combined d = 0.53) ([[hernandez2025exposome]], p. 3090, 3092) → [[country-exposome--biobehavioral-age-gap--hernandez2025exposome]].
- Predicted two-wave functional and cognitive decline (RR 1.40 and 1.25) ([[hernandez2025exposome]], p. 3092) → [[biobehavioral-age-gap--functional-cognitive-decline--hernandez2025exposome]].

## Open questions
- Claude's reading: how BBAG relates to [[phenotypic-age]] or epigenetic clocks in the same people is not tested in the vault's sources.

## See also
- [[phenotypic-age]] · [[geroscience]] · [[exposome]]

## References
- Hernandez, H., Santamaria-Garcia, H., Moguilner, S., … Ibanez, A. (2025). The exposome of healthy and accelerated aging across 40 countries. *Nature Medicine, 31*(9), 3089–3100. https://doi.org/10.1038/s41591-025-03808-2
