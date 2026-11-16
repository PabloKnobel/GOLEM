---
type: my-work
title: "HEALS × Pepper pilot research plan: nature and impairment (v5, 2026)"
aliases: ["Out of Reach plan", "HEALS research plan v5", "P30 nature impairment plan"]
kind: grant
role: [PI]
date: 2026
venue: "HEALS × Pepper Center pilot program, 19th call"
status: draft
source_file: "raw/docs/7ac91a1e-heals-research-plan-2026-v5.docx"
projects: ["[[p30-nature-impairment]]"]
portals: ["[[urban-nature-and-aging]]", "[[urban-green-space-quality]]"]
tags: [my-work, grant]
created: 2026-11-16
updated: 2026-11-16
generated: true
reviewed: false
---
**Lead.** Version 5 of the full research plan for Pablo's HEALS × Pepper pilot testing whether vision, hearing, mobility and cognitive impairment modify the associations of nearby nature with going out (Aim 1) and mortality (Aim 2) in NHATS (2011–2025). Hub: [[p30-nature-impairment]].

## How I framed it
- Opening: "nearby nature can only help those who can reach it and perceive it" (§1).
- Two ways impairment blocks contact: mobility and cognition keep people at home; vision and hearing may let them out but keep them from "perceiving what surrounds them" (§1).
- Three gaps: impairment rarely tested as a modifier; "Exposure is assigned, not used"; NDVI cannot tell whether nature is accessible or usable (§1).
- Theory: Lawton and Nahemow's press–competence model, with two competing hypotheses, *environmental docility* (impaired adults benefit more) vs *out of reach* (they benefit less), "so either result is informative" (§2–3).
- Focus on contact pathways, because harm reduction "does not require contact" (§2).
- Innovation 4 uses the national deep-learning park-quality layer (§3; see [[greenspace-quality-metric]]).

## Design at a glance
- NHATS Rounds 1–14 (2011 to early 2025), excluding Round 10 (2020, phone only); community-dwelling, urban tracts (§4).
- Exposures (GREENER platform): tract Landsat NDVI, share within a 10-minute walk of a park, park presence and quality (4 categories) (§4).
- Modifiers: self-reported vision and hearing (objective tests Rounds 11–14 as sensitivity), SPPB 0–12, NHATS dementia classification (§4).
- Aim 1: survey-weighted GEE, cumulative logit for going-out frequency (primary), plus walking for exercise and valued activities. Aim 2: Cox with age as time scale, censoring at last interview (Gill et al.) (§5).
- 12 models per outcome (4 domains × 3 measures), FDR control (§5).
- Restricted data (tract linkage, death dates) after notice of award; public files meanwhile (§4).
- Future: NIA R01, target June 2028, with GPS, accelerometers and EMA in NYC older adults with impairment (§7).

> [!uncertain] Differs from the plan as last discussed (Oct 29, 2026: Aim 1 GEE with event study). v5 drops the event study and makes going-out frequency the Aim 1 primary outcome.

## Concepts used
- [[green-space-use]] — exposure "assigned, not used"; going out as the Aim 1 outcome.
- [[differential-vulnerability]] — impairment as effect modifier.
- [[ndvi]] — and its limits for access and usability.
- [[green-space-quality-assessment]] — park quality layer.
- [[green-space-health-pathways]] — contact vs non-contact pathways ([[markevych2017exploring]]).
- [[social-cohesion]] — used as the stand-in neighborhood resource in preliminary data.

## Reusable pieces
- Table 1: impairment prevalence and adjusted OR of going out daily in NHATS public files (vision 0.50, hearing 0.88, mobility 0.30, probable dementia 0.47) (§4).
- Feasibility analysis: social cohesion × impairment on walking for exercise; ratio of odds ratios 0.86 (vision) and 0.91 (hearing) (§4, Figure 2).
- Power: 80% for interaction OR 1.15–1.24 per IQR (going out daily) and HR 1.16–1.27 (mortality) (§5).
- Six challenges with mitigations, including enclave output rules (§4).
- Figures: conceptual model (Figure 1), cohesion forest plot (Figure 2), timeline.

> [!todo] In-text citation "{Knobel, 2026}" in §3 is an unformatted EndNote field.

## See also
- [[health-and-retirement-study]] (fallback cohort) · [[nhats]]
