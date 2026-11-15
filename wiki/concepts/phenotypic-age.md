---
type: concept
title: "Phenotypic age (PhenoAge) and phenotypic age acceleration"
aliases: [PhenoAge, phenotypic age, PhenoAgeAccel, phenotypic age acceleration, Levine PhenoAge, biological age]
kind: measure
related: ["[[geroscience]]", "[[frailty-index]]", "[[social-hallmarks-of-aging]]"]
part_of: []
projects: []
portals: ["[[urban-nature-and-aging]]"]
tags: [concept]
created: 2026-11-15
updated: 2026-11-15
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**Lead.** A biological age measure computed from chronological age and routine clinical blood biomarkers; phenotypic age acceleration (PhenoAgeAccel) is the gap between PhenoAge and chronological age, with positive values meaning accelerated aging ([[knobel2025social]], p. 241–242). Because it uses common clinical labs, it can be derived in large EHR cohorts, unlike DNA methylation clocks ([[knobel2025social]], p. 241).

> [!info] Infobox
> **Kind:** measure (biological age) · **Also known as:** PhenoAge, Levine phenotypic age · **Inputs:** albumin, creatinine, glucose, CRP, lymphocyte %, mean cell volume, RDW, alkaline phosphatase, WBC, chronological age · **Key sources:** [[knobel2025social]]

## Definition and measurement
- PhenoAge is a weighted linear combination of lab results transformed into years using two parametric proportional hazards models (Levine et al.) ([[knobel2025social]], p. 242).
- Inputs routinely drawn: albumin, creatinine, glucose, MCV, alkaline phosphatase, RDW, WBC; CRP and lymphocyte % often ordered only when clinical concern arises ([[knobel2025social]], p. 242).
- In an older-adult EHR cohort, CRP was imputed for 90.83% and lymphocyte % for 24.06% of person-years (predictive mean matching); complete-lab results were similar ([[knobel2025social]], p. 242, 244).
- Phenotypic age is one of several downstream summaries of hallmark biology alongside biological age and pace of aging ([[crimmins2020social]], p. 2).

## Evidence
- Neighborhood social vulnerability (SVI mixture) was associated with +0.23 years PhenoAgeAccel per decile in NYC adults ≥65 ([[knobel2025social]], p. 243) → [[social-vulnerability--phenotypic-age-acceleration--knobel2025social]].
- PhenoAgeAccel predicts morbidity and mortality better than chronological age (secondhand via [[knobel2025social]], p. 241).

## Pablo's framing
- [[2025-paper-svi-biological-aging-nyc]]: EHR-feasible biological aging outcome for neighborhood exposures.

## Open questions
- Claude's reading: no urban nature exposure has yet been tested against PhenoAgeAccel in the vault.

## See also
- [[geroscience]] · [[frailty-index]] · [[social-hallmarks-of-aging]]

## References
- Knobel, P., Colicino, E., Kloog, I., Litke, R., Lane, K., Federman, A., Mobbs, C., & Yitshak Sade, M. (2025). Social vulnerability and biological aging in New York City: An electronic health records-based study. *Journal of Urban Health, 102*, 240–249.
- Crimmins, E. M. (2020). Social hallmarks of aging: Suggestions for geroscience research. *Ageing Research Reviews, 63*, Article 101136.
