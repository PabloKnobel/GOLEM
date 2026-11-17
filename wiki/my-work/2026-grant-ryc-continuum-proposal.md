---
type: my-work
title: "CONTINUUM: Ramón y Cajal research proposal (v0.17, Nov 2026)"
aliases: ["CONTINUUM", "RyC proposal v0.17", "Mapping where we age", "RESEARCH_PROPOSAL_v0.17"]
kind: grant
role: [PI]
date: 2026-11
venue: "Ramón y Cajal 2026 (research proposal)"
status: draft
source_file: "raw/docs/85bb8fdf-research-proposal-v0-17.docx"
projects: ["[[ryc-2026]]"]
portals: ["[[urban-green-space-quality]]", "[[urban-nature-and-aging]]", "[[exposome-research]]"]
tags: [my-work, grant]
created: 2026-11-17
updated: 2026-11-17
generated: true
reviewed: false
---

**Lead.** Version 0.17, the latest version of Pablo's Ramón y Cajal research proposal "Mapping where we age: the urban continuum and dementia (CONTINUUM)" (per Pablo, 2026-11-17). It maps types and features of every place in Catalonia from annual 25 cm ICGC orthophotos (2012 onward) and links them to dementia incidence (SIDIAP) and severity at diagnosis (ReDeGi). Hub: [[ryc-2026]].

## How I framed it
- Question: "which features of the places where older adults live matter for dementia, from city centers to remote villages" (§2.1.1).
- **Urban continuum**: the full range of places and features, described at two levels, **types of place** and **features** (§2.1.1).
- Three gaps: (1) "No consistent measure across places and years"; (2) "Environmental exposures are studied one at a time"; (3) "Onset is studied, severity rarely" (§2.1.2).
- Pathways: Markevych's reducing harm, restoring and building capacities, which "can work in either direction" depending on the feature (§2.1.2; [[markevych2017exploring]]).
- Severity at diagnosis tells two stories: slower decline or later diagnosis, which "call for different responses" (§2.1.2).
- Novelty: "the question it makes answerable", by combining mature approaches that are rarely combined (§2.2.3).
- Three products: an open annual map, a transferable pipeline, joint evidence on dementia (§2.1.4).

## Design at a glance
- Hypotheses H1a (stable, interpretable types), H1b (feature accuracy does not differ materially across urban, peri-urban and rural settings), H2a (features and dementia incidence, individually and jointly), H2b (features and severity at diagnosis) (§2.2.1).
- Units: 64 m tiles (types), 32 m sub-tiles (features), census section (exposure); about 7.8 million tiles and 31 million sub-tiles per year (§3.2.2, Figure 3).
- Aim 1a: DINOv2 embeddings, two-stage clustering (contexts from ~320 m neighborhood averages, then types within context), elbow plus bootstrap stability (§3.2.2).
- Aim 1b: 14 initial features (Table 1) chosen from 95 candidates by relevance, visibility, reliability, variability; ~10,000 labeled sub-tiles, grid labeling task, κ ≥ 0.60, active learning; pass rule F1 ≥ 0.70 overall and per setting; H1b if 90% CI of F1 difference within ±0.10 (§3.2.2).
- Exposure: residential prevalence (sub-tiles within 300 m of a residential building) per census section and year (§3.2.2).
- Aim 2a: SIDIAP adults ≥65 from 2013 (>1 million expected); Cox with age as time scale, death as competing event, then survival qgcomp with harm features reversed; effect modification by sex, age, deprivation, setting; 10 sensitivity analyses; power HR ≈ 1.02 per IQR (§3.2.3).
- Aim 2b: ~5,000 ReDeGi cases linked to SIDIAP; MMSE and CDR at diagnosis; symptom duration as mediator (controlled direct effect); BKMR plus qgcomp; power ≈ 0.3 MMSE points per IQR (§3.2.4).
- Team: two predoctoral researchers (Aim 1 imagery; Aim 2 epidemiology), TFG/TFM students; ERC Starting Grant planned from Year 2 (§3.3).
- Impact: five scientific impacts (new exposure layer, transferable method via PNOA/INSPIRE, which features matter, severity, urban exposome building block), indicators, and the ERC Starting Grant next step adding segmentation, address-level data and activity spaces (§4.1).
- Social impact: planning quantities (e.g., tree-lined street length per IQR) and absolute risks per 1,000 older adults, "always as associations"; displacement risk flagged (§4.2).
- User panel (public health agency, Territori, ICGC, one large and one small municipality, CEAFA) meeting at Months 6, 24, 48 (§4.4).
- Sex in every stage of Aim 2; SAGER reporting (§4.6). Privacy: private-space features and neglect released only as census-section summaries; cells <5 suppressed (§6).
- Budget €332,000 direct: two predocs €124,000 each, GPU workstation €20,000, health data access €20,000 (§5).

## Concepts used
- [[dementia]] — incidence and severity at diagnosis.
- [[multi-exposure-analysis]] — qgcomp (Aim 2a) and BKMR (Aim 2b).
- [[green-space-health-pathways]] — harm, restoration, capacity building, in either direction.
- [[green-space-quality-assessment]] — RECITAL and POSDAT as sources of candidate features.
- [[exposome]] — residential environment as a mixture ([[wild2005complementing]]).
- [[ndvi]] — named as a single-purpose tool the proposal moves beyond.

## Reusable pieces
- Gap boxes 1–3 and the units box (§2.1.2, §3.2.2).
- Table 1 (14 initial features) and the four feature-selection criteria (§3.2.2).
- Previous-results blocks linking each past study to an aim (§3.5).
- Girona pilot: 87 census sections, ~42,000 tiles (2025); 5 contexts and 27 types; adjusted Rand index 0.99 (contexts) and 0.90 (types); ~10 minutes per year on a consumer GPU (§3.5, Figure 6).
- Table 2 (9 critical points with contingencies) and the fallback data chain PADRIS → BIFAP → Mount Sinai, WTC, Medicare (§3.4).
- Figures 1–6: gaps/aims/hypotheses, Girona section example, tile grid, labeling mockup, work plan, pilot typology.


## See also
- [[greenspace-quality-metric]] (the US pipeline Aim 1b adapts) · [[sidiap]] · [[redegi]] · [[icgc-orthophotos]] · [[recital]]
