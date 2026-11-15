---
type: concept
title: "Normalized difference vegetation index (NDVI)"
aliases: [NDVI, normalized difference vegetation index, greenness density, surrounding greenness]
kind: measure
related: ["[[green-space-health-pathways]]", "[[green-space-quality-assessment]]"]
part_of: []
projects: ["[[ryc-2026]]"]
portals: ["[[urban-green-space-quality]]"]
tags: [concept]
created: 2026-11-15
updated: 2026-11-15
last_verified: 2026-11-15
confidence: medium
generated: true
reviewed: false
superseded_by: ""
---

**Lead.** A satellite-derived index of greenness density, ranging from −1 to 1, with higher values indicating more photosynthetically active land cover ([[knobel2021associations]], p. 3). It is the most common green space exposure in epidemiology but cannot capture quality ([[markevych2017exploring]], p. 306).

> [!info] Infobox
> **Kind:** measure · **Range:** −1 (water) to ~1 (dense vegetation) · **Typical sources:** MODIS MOD13Q1 (250 m, 16-day), Landsat, Sentinel-2 · **Key sources:** [[knobel2021associations]], [[markevych2017exploring]]

## Definition and measurement
- Based on reflectance: healthy vegetation absorbs visible light and reflects near-infrared; negative values are water, values near zero unvegetated surfaces such as pavement ([[knobel2021associations]], p. 3).
- Usually summarized as mean NDVI or % green within a buffer around the residence ([[nieuwenhuijsen2017fifty]], p. 66); buffers in the literature range 30–5,000 m ([[markevych2017exploring]], p. 308).
- Overall greenness indices cannot distinguish vegetation types (trees vs grass) or measure perceived access ([[knobel2021associations]], p. 2).

## Evidence
- In 377 Philadelphia census tracts, MODIS NDVI was close to null for obesity, high blood pressure and diabetes, while perceived park access and tree canopy were protective; NDVI correlated only 0.12 with perceived access ([[knobel2021associations]], p. 4).
- An inaccessible overgrown lot can score like a well-used park ([[markevych2017exploring]], p. 306).

## Pablo's framing
- [[2021-paper-greenness-cvd-philadelphia]]: NDVI as a comparator that missed associations seen with perceived and type-specific measures.

## Open questions
- Remote sensing still lacks the capability to detect subtle quality-related elements ([[knobel2019systematic]], p. 1).

## See also
- [[green-space-quality-assessment]] · [[perceived-green-space-access]] · [[green-space-health-pathways]]

## References
- Knobel, P., Kondo, M., Maneja, R., Zhao, Y., Dadvand, P., & Schinasi, L. H. (2021). Associations of objective and perceived greenness measures with cardiovascular risk factors in Philadelphia, PA: A spatial analysis. *Environmental Research, 197*, Article 110990.
- Markevych, I., et al. (2017). Exploring pathways linking greenspace to health: Theoretical and methodological guidance. *Environmental Research, 158*, 301–317.
- Nieuwenhuijsen, M. J., Khreis, H., Triguero-Mas, M., Gascon, M., & Dadvand, P. (2017). Fifty shades of green: Pathway to healthy urban living. *Epidemiology, 28*(1), 63–71.
- Knobel, P., Dadvand, P., & Maneja-Zaragoza, R. (2019). A systematic review of multi-dimensional quality assessment tools for urban green spaces. *Health & Place, 59*, Article 102198.
