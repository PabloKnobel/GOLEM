---
type: concept
title: "Exposome-wide association study"
aliases: [ExWAS, EWAS (exposome), agnostic exposome approach, hypothesis-free exposome analysis]
kind: method
related: ["[[multi-exposure-analysis]]", "[[exposome]]"]
part_of: ["[[multi-exposure-analysis]]"]
projects: ["[[r01-urban-exposome-aging]]"]
portals: ["[[exposome-research]]"]
tags: [concept]
created: 2026-11-22
updated: 2026-11-22
last_verified: 2026-11-22
confidence: low
generated: true
reviewed: false
superseded_by: ""
---

**Lead.** An exposome-wide association study (ExWAS) tests many exposures one by one against an outcome, with correction for multiple testing, as an agnostic screen of the [[exposome]]. The IHEN roadmap lists it with causal inference and deep learning as approaches for detecting exposure–health associations ([[ihen2026interim]], p. 57).

> [!info] Infobox
> **Kind:** method · **Also known as:** ExWAS, agnostic exposome approach · **Key sources:** [[ihen2026interim]], [[neufcourt2022assessing]]

## Definition and measurement
- One of the statistical approaches named in the IHEN roadmap, alongside causal inference and deep learning ([[ihen2026interim]], p. 57); the roadmap also asks for ExWAS on biodiversity-related exposures ([[ihen2026interim]], p. 17).

## Evidence
- Critique: agnostic exposome-wide approaches treat upstream stratifying variables (race/ethnicity, class) as equivalent to downstream exposures, ignoring their hierarchy ([[neufcourt2022assessing]], p. 4).
- No ExWAS result is filed in the vault yet.

## Pablo's framing
- R01 Urban Exposome Aim 1: ExWAS with GAMs (Benjamini-Hochberg FDR) followed by mixed-effects qGcomp in the Mount Sinai EHR cohort; see [[2026-grant-r01-urban-exposome-aging]] (an FDR vs Bonferroni inconsistency is flagged there).

## Open questions
- Claude's reading: how to respect the upstream/downstream hierarchy raised by [[neufcourt2022assessing]] inside an ExWAS of built, social and ambient layers is not addressed by vault sources.

## See also
- part_of: [[multi-exposure-analysis]] · related: [[exposome]] · [[social-exposome]] · [[r01-urban-exposome-aging]]

## References
- IHEN Consortium. (2026). Interim roadmap focused on exposome research in Europe [Report]. International Human Exposome Network.
- Neufcourt, L., Castagné, R., Mabile, L., Khalatbari-Soltani, S., Delpierre, C., & Kelly-Irving, M. (2022). Assessing how social exposures are integrated in exposome research: A scoping review. Environmental Health Perspectives, 130(11), Article 116001. https://doi.org/10.1289/EHP11015
