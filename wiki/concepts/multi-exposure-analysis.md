---
type: concept
title: "Multi-exposure and mixtures analysis"
aliases: [mixtures, mixture methods, multi-exposure models, co-exposures, joint effects, quantile g-computation, qGcomp, multi-pollutant models]
kind: method
related: ["[[exposome]]", "[[social-exposome]]", "[[air-pollution]]"]
part_of: []
projects: []
portals: ["[[exposome-research]]", "[[urban-environmental-hazards]]"]
tags: [concept]
created: 2026-11-15
updated: 2026-11-15
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**Lead.** Analyses that estimate several co-occurring exposures together rather than one at a time, from mutually adjusted multi-exposure regressions to mixture methods such as quantile g-computation. A recurring design choice in Pablo's work, motivated by exposures that "do not present in isolation" ([[wu2025air]], p. 2). Promoted from candidates at 5 mentions.

> [!info] Infobox
> **Kind:** method · **Variants in vault:** multi-exposure mixed models, multi-source models of NMF-apportioned PM2.5, quantile g-computation (qGcomp, qgcompint) · **Key sources:** [[knobel2025social]], [[wu2025air]], [[krasnov2026association]]

## Definition and measurement
- Mutually adjusted multi-exposure mixed model of PM2.5, NO2 and temperature, compared with single-exposure models ([[wu2025air]], p. 2–3).
- Five source-apportioned PM2.5 exposures estimated simultaneously in one model ([[krasnov2026association]], p. 499).
- Quantile g-computation estimating the joint effect of four SVI themes, with weights by theme, and qgcompint for effect modification ([[knobel2025social]], p. 242–243).

## Evidence
- PM2.5 and temperature associated with child HbA1c in a multi-exposure model ([[wu2025air]], p. 3) → [[pm25--hba1c--wu2025air]].
- Social vulnerability mixture: +0.23 y PhenoAgeAccel per joint decile, 61% of weight from SES ([[knobel2025social]], p. 243) → [[social-vulnerability--phenotypic-age-acceleration--knobel2025social]].
- Metal-industry PM2.5 associated with diabetes and glucose, while total PM2.5 mass was null; the authors argue source effects "were masked" by pooling into mass ([[krasnov2026association]], p. 500) → [[metal-industry-pm25--diabetes--krasnov2026association]].
- Historical WTC disaster exposure and later PM2.5 both associated with glucose in the same model ([[knobel2024association]], p. 91) → [[wtc-exposure--glucose--knobel2024association]].
- In noise–dementia studies, four of seven adjusted for air pollution and three examined joint effects ([[hwang2025comprehensive]], p. 8).

## Pablo's framing
- [[2025-paper-svi-biological-aging-nyc]]: an overall score "might oversimplify"; themes evaluated "simultaneously, as they occur in real life" (p. 245).
- [[2025-paper-air-pollution-temperature-hba1c-children]] · [[2025-paper-noise-dementia-meta-analysis]].

## Open questions
- Claude's reading: [[knobel2026beyond]] handles co-occurring urban nature features by clustering into profiles instead of a mixture model; how the two approaches compare is untested in the vault.

## See also
- related: [[exposome]] · [[social-exposome]] · [[air-pollution]]

## References
- Wu, J., et al. (2025). Air pollution, temperature, and HbA1c levels among children in Mexico City, Mexico. *Ecotoxicology and Environmental Safety, 307*, Article 119424.
- Knobel, P., Colicino, E., Kloog, I., Litke, R., Lane, K., Federman, A., Mobbs, C., & Yitshak Sade, M. (2025). Social vulnerability and biological aging in New York City: An electronic health records-based study. *Journal of Urban Health, 102*, 240–249.
- Krasnov, H., et al. (2026). The association between long-term exposure to PM2.5 constituents and diabetes incidence and blood glucose levels among World Trade Center Health Program general responders. *American Journal of Epidemiology, 195*(2), 497–504.
- Knobel, P., Just, A. C., Colicino, E., Teitelbaum, S. L., McLaughlin, M. A., Amini, H., & Yitshak Sade, M. (2024). The association of air pollution exposure with glucose and lipid levels. *American Journal of Epidemiology, 193*(1), 87–95.
- Hwang, S. A., et al. (2025). A comprehensive systematic review and meta-analysis to unravel the noise-dementia nexus. *Public Health Reviews, 46*, Article 1607355.
