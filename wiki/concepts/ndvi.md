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
updated: 2026-11-18
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
- Of 22 greenness–cardiometabolic studies, 68.2% measured residential surrounding greenness, mostly by NDVI; NDVI studies more often found greater protection for females/women (57.1%) ([[fernandeznunez2022differences]], p. 1057, 1061).
- In older New Yorkers, a High Cover profile, which the authors liken to NDVI-based exposure, was not clearly associated with ASCVD (HR 0.95; 0.88–1.02), unlike park access, street-tree and waterfront profiles ([[knobel2026beyond]], p. 4).
- High NDVI can be "green but unreachable" (secondhand via [[knobel2026beyond]], p. 1).
- In Europe, 300 m NDVI correlated R −0.67 with NO2 and moderately strongly (negatively) with degree of urbanisation. Its spatial contrast was stable from 2000 to 2020 (R 0.96 Europe-wide), and population-weighted NDVI rose slightly ([[dehoogh2025europewide]], p. 8–9, Fig. 4).

## Pablo's framing
- [[2021-paper-greenness-cvd-philadelphia]]: NDVI as a comparator that missed associations seen with perceived and type-specific measures.
- [[2026-paper-urban-nature-profiles-ascvd]]: single indicators "cannot capture the broader dimensions of nature" (p. 1).

## Open questions
- Remote sensing still lacks the capability to detect subtle quality-related elements ([[knobel2019systematic]], p. 1).

## See also
- [[green-space-quality-assessment]] · [[perceived-green-space-access]] · [[green-space-health-pathways]]

## References
- Knobel, P., Kondo, M., Maneja, R., Zhao, Y., Dadvand, P., & Schinasi, L. H. (2021). Associations of objective and perceived greenness measures with cardiovascular risk factors in Philadelphia, PA: A spatial analysis. *Environmental Research, 197*, Article 110990.
- Markevych, I., et al. (2017). Exploring pathways linking greenspace to health: Theoretical and methodological guidance. *Environmental Research, 158*, 301–317.
- Nieuwenhuijsen, M. J., Khreis, H., Triguero-Mas, M., Gascon, M., & Dadvand, P. (2017). Fifty shades of green: Pathway to healthy urban living. *Epidemiology, 28*(1), 63–71.
- Knobel, P., Dadvand, P., & Maneja-Zaragoza, R. (2019). A systematic review of multi-dimensional quality assessment tools for urban green spaces. *Health & Place, 59*, Article 102198.
- Fernández Núñez, M.-B., Campos Suzman, L., Maneja, R., Bach, A., Marquet, O., Anguelovski, I., & Knobel, P. (2022). The differences by sex and gender in the relationship between urban greenness and cardiometabolic health: A systematic review. *Journal of Urban Health, 99*, 1054–1067.
- Knobel, P., Singhvi, A., Krasnov, H., Colicino, E., Kloog, I., Litke, R., Lane, K., Federman, A., Mobbs, C., & Yitshak Sade, M. (2026). Beyond greenness: Multidimensional urban nature profiles and arteriosclerotic cardiovascular risk. *Environment International, 207*, Article 110033.
- de Hoogh, K., et al. (2025). A Europe-wide characterization of the external exposome: A spatio-temporal analysis. *Environment International, 200*, Article 109542. https://doi.org/10.1016/j.envint.2025.109542
