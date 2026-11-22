---
type: my-work
title: "P30 pilot application: 311-derived exposures and frailty progression (Dec 2025)"
aliases: ["311 frailty pilot", "P30 311 submission", "Untangling 311-Derived Exposures"]
kind: grant
role: [PI]
date: 2025-12
venue: "HEALS P30 (ES023515) pilot program, early-stage investigators"
status: submitted
source_file: "raw/docs/c50d0b5d-p30-knobel-submission.pdf"
projects: ["[[nyc-311-exposures]]"]
portals: ["[[exposome-research]]", "[[urban-environmental-hazards]]"]
tags: [my-work, grant]
created: 2026-11-16
updated: 2026-11-16
last_verified:
confidence:
superseded_by: ""
generated: true
reviewed: false
---
**Lead.** December 2025 HEALS P30 early-stage investigator pilot application (MPIs Knobel and Yitshak-Sade; $20,000 direct costs) on what NYC 311 complaints measure and how they relate to frailty outcomes in Mount Sinai older adults. The 2026 LOI calls itself a resubmission ([[2026-loi-heals-311-cvd]]). Hub: [[nyc-311-exposures]].

## How I framed it
- The urban exposome as "a three-legged stool—ambient, built, and social", where the social environment "remains the weakest link" (Background, p. 4).
- 311 complaints may encode three signals: (A) objective neighborhood conditions, (B) population sensitivity or perception, (C) propensity or ability to complain; "Treating 311 complaints solely as objective issues discards B and C" (Background, p. 4).
- Goal: "untangle what 311-based social exposure metrics capture" (Specific Aims, p. 3).
- Elevates the social environment "to a first-class component of the urban exposome" (Innovation, p. 4).

## Design at a glance
- Aim 1: NYC 311, 2011–2023, tract-level yearly rates (overall and by theme); data quality checks; comparison with PLUTO and road/rail data; bivariate Moran's I with census sociodemographics (pp. 3–4).
- Aim 2: frail MSHS patients (VA-FI ≥ 0.21), outcomes falls, hip fractures, pressure ulcers, mortality and health care use; GAMMs (Andersen–Gill, Cox, Poisson) with person and tract random intercepts, FDR; qgcomp for the 311-theme mixture (pp. 5–6).
- Aim 3: Gaussian mixture neighborhood profiles of 311 + built + ambient exposures; growth mixture models for frailty trajectories (p. 6).
- Fallback if 311 proves unusable: CDC Environmental Justice Index (p. 6).
- Team: Knobel, Yitshak-Sade (MPIs); Kloog, Midya, Ko (frailty) (p. 3).

## Concepts used
- [[social-exposome]] · [[exposome]] — framing.
- [[frailty-index]] — VA-FI, frailty cutoff 0.21.
- [[multi-exposure-analysis]] — qgcomp and model-based clustering.

## Reusable pieces
- The A/B/C signal decomposition of 311 complaints (p. 4).
- Future-funding paragraph tied to a career development award or R01 on frailty (p. 6).

> [!info] Not ingested: budget pages and the co-investigators' biosketches (pp. 7–35); they stay in `raw/` only.

## See also
- [[2026-loi-heals-311-cvd]] (later version) · [[nyc-311-service-requests]] · [[mount-sinai-data-warehouse]]
