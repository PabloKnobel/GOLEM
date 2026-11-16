---
source_file: 35b2edf1-r21-science-20261014-for-sub.docx
sha256: d5630443e3d90dad99393982ff0919e3f2145c99d2fff387c4f80f68e3982876
converted: 2026-11-16
method: pandoc
pages: 
---
# A. IMPORTANCE OF RESEARCH

## A.1. Significance

**Frailty and biological aging.** Frailty and accelerated biological aging are central outcomes for healthy aging. Frailty, a state of cumulative decline across multiple physiological systems, increases older adults’ susceptibility to disability, hospitalization and death<sup>1,9</sup>. Phenotypic age acceleration captures how fast a person is aging relative to their chronological age and predicts mortality and age-related disease<sup>10</sup>. Both are dynamic: frailty states change over time and can improve<sup>2</sup>, and biological age can run ahead of or behind chronological age<sup>10</sup>. Because 80% of the U.S. population lives in urban areas<sup>3</sup>, identifying urban environmental features linked to slower physical aging is a public health priority.

**The environment shapes aging, but standard metrics miss parts of it.** Neighborhood characteristics have been associated with frailty<sup>11</sup> and successful aging<sup>12</sup>. Urban nature and sound are two well-studied examples. Residential greenness has been associated with several healthy-aging outcomes<sup>13</sup>. Transportation noise contributes to cardiovascular and other disease burden<sup>14</sup> and has been linked to incident dementia<sup>15</sup>. Yet both literatures rely on single summary metrics. Greenness is usually measured with the satellite-derived Normalized Difference Vegetation Index (NDVI), which captures photosynthetic activity but not vegetation structure or habitat quality<sup>16,17</sup>. Systematic reviews report inconsistent associations between greenness and several health outcomes, partly because of heterogeneous metrics<sup>18</sup>. Noise is usually summarized as a decibel level, which captures sound energy but not its source or whether restorative natural sound is present<sup>19</sup>.

**Bird biodiversity and the proxy question.** Bird biodiversity, the number and relative abundance of bird species in an area, is a promising but understudied feature of healthy urban environments. Studies have focused mainly on mental health and well-being<sup>4,20</sup>. County-level bird richness has been linked with greater life expectancy<sup>21</sup>, but evidence for physical aging is limited. In our P30 pilot in the same EHR population, each interquartile-range increase in residential bird diversity was associated with a 1.4% lower expected frailty deficit count<sup>22</sup>. Bird communities, however, respond to the same conditions that standard metrics capture: urban bird assemblages are shaped by habitat, food resources, noise and light pollution<sup>23</sup>. For example, lower ozone pollution has been linked to higher abundance of small land birds<sup>5</sup>. A key question, therefore, is whether bird biodiversity adds information beyond standard exposures or simply stands in for them. We propose that the answer differs by pathway (Figure 1).

**Two pathways.** In the ***soundscape pathway***, birdsong is a sensory exposure in its own right. Experimental studies show that natural sounds, including birdsong, support stress recovery and perceived attention restoration<sup>24,25</sup>, and a recent meta-analysis found that natural sound exposure reduces stress<sup>26</sup>. Birds are a major source of biological sound in urban soundscapes<sup>27,28</sup>. Traffic noise models capture only transportation sources and greenness does not measure sound, so birdsong exposure could relate to health independently of both. Repeated stress responses offer a plausible route from soundscape to physical aging. Allostatic load, the cumulative physiological cost of chronic stress, has been associated with frailty in older adults<sup>29</sup>, and chronic inflammation, captured in PhenoAge, is consistently associated with healthy aging<sup>30</sup>. If daily birdsong supports stress recovery, it may slow this accumulation, a link not yet tested for physical aging outcomes. In the ***bioindicator pathway***, which birds are present signals the condition of the environment. Birds are widely used as indicators of environmental quality because they are detectable, widespread and respond quickly to environmental change<sup>31</sup>. Which species live near a home may therefore integrate several environmental conditions, including some that standard metrics miss. For example, the Gray Catbird nests in dense shrubs, so its presence signals understory vegetation that NDVI cannot distinguish from lawn<sup>6</sup>. Other mechanisms, such as natural pest control<sup>32</sup> or opportunities for social contact<sup>33</sup>, may also link birds to health but are not tested here.

**Two gaps.** First, population-based studies have relied mostly on overall biodiversity indices. A single index blends both pathways: dense, diverse bird communities produce a richer soundscape, while the presence of a few sensitive species signals environmental conditions. An overall index therefore cannot show which pathway drives an association, or whether either adds information beyond standard exposures. Second, biodiversity exposure has been hard to measure at population scale. Most studies rely on coarse or citizen-science-based estimates<sup>34</sup>. Citizen-science observations are spatially and seasonally uneven<sup>35</sup>, and dedicated field surveys alone are too costly to cover a city. Predictive models can fill this gap: the environmental data that shape bird communities can predict biodiversity across an entire study area from a set of sampled sites<sup>36</sup>, an approach that mirrors air pollution exposure modeling. We address both gaps by deriving pathway-specific metrics from dedicated acoustic fieldwork and predicting them citywide at 100-m resolution.

**Bird communities are modifiable.** Supplementary feeding measurably restructures urban bird communities<sup>37</sup>, and New York City’s Urban Forest Plan promotes dense plantings that provide habitat where land is limited<sup>38</sup>. How much biodiversity residents perceive may also be modifiable: perceived species richness is associated with self-reported well-being<sup>39</sup>, which points to a role for bird-identification education. Bioindicator species could also give residents a visible, intuitive signal of local environmental quality.

**In summary,** frailty and biological aging are major, dynamic targets for prevention, and bird biodiversity is associated with frailty in our pilot. Whether it captures anything beyond standard exposures, and through which pathway, is unknown. By separating a soundscape pathway from a bioindicator pathway and testing each against standard exposures, we will test whether, and how, urban birds matter for physical aging.

<img src="media/image1.png" style="width:6.5in;height:1.83793in" />

**Figure 1:** Conceptual framework. Urban environmental conditions shape the bird community near the home, which may affect physical aging through two pathways. In the soundscape pathway (Aim 1), birdsong exposure supports perceived restoration. In the bioindicator pathway (Aim 2), the presence of sensitive species signals environmental conditions, including unmeasured ones. Models adjust for individual and neighborhood confounders.

**A.2. Innovation.** The proposed study is innovative in three ways. **Conceptually**, it treats bird biodiversity as a potential determinant of physical aging in its own right, and tests whether it adds information beyond the greenness, noise and air pollution metrics that dominate environmental epidemiology. **Methodologically**, it separates two pathways that overall biodiversity indices combine: it measures what residents hear (birdsong exposure) separately from what bird presence signals about the environment (bioindicator species). **Technically**, it builds 100-m citywide exposure surfaces from dedicated acoustic recordings rather than citizen-science observations, by adapting a machine-learning pipeline developed for air pollution modeling.

| **Figure 2:**GAM-estimated latent bird Shannon index across NYC census tracts.                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="media/image2.tiff" style="width:2.43072in;height:2.37995in" alt="Figure 2: latent bird Shannon index across NYC census tracts" /> |

**A.3. Expected Impact.** We will provide evidence on whether bird biodiversity is associated with frailty and biological age beyond standard environmental exposures, and through which pathway. Because bird biodiversity is a new exposure in aging research, the outcome is uncertain, and the study is designed so that each pattern of results is informative. If birdsong associations persist after accounting for traffic noise and greenness, birdsong is supported as a health-relevant exposure in its own right. If bioindicator species explain the air pollution and greenness associations, bird presence is supported as an integrative marker of environmental quality. If neither holds, the association seen in our pilot most likely reflects standard exposures, which is equally important to know before investing in biodiversity interventions. If the associations hold, the exposure surfaces and effect estimates will support two R01 directions: a nationwide observational study of regional differences, using a modeling pipeline adaptable to other U.S. cities with local acoustic data, and an intervention study that combines biodiversity-enhancing and educational interventions.

2.  **RIGOR AND FEASIBILITY**

**B.1. Preliminary results.** Our P30 pilot (HEALS, P30 ES023515) informed each component of the proposed work.

<u>+ Bird biodiversity model for NYC:</u> We developed and validated a bias-corrected latent bird biodiversity model for New York City census tracts using eBird citizen-science data (Figure 2). The model preserved the relative ranking of tracts from lowest to highest diversity (Spearman’s ρ = 0.745), with performance comparable to a national-scale bird richness model built at a coarser resolution<sup>36</sup>. We will build on this model but replace citizen-science observations with dedicated acoustic recordings, modeled with a machine-learning pipeline adapted from air pollution modeling (B.4).

<u>+ Bird biodiversity and frailty:</u> In a very similar MSHS cohort of 20,388 adults aged ≥65<sup>22</sup>, each interquartile-range (IQR) increase in residential bird Shannon diversity, an index combining the number of species and how evenly individuals are distributed among them, was associated with a 1.4% lower expected deficit count on the Veterans Affairs Frailty Index (VA-FI) (95% CI −2.1% to −0.8%). The association was strongest among adults aged 65-74 (−3.0%, 95% CI −3.9% to −2.1%), attenuated at 75-84 (−0.8%, 95% CI −1.9% to 0.3%), and not evident at 85+ (+1.6%, 95% CI −0.0% to 3.3%).

<u>+ Acoustic fieldwork:</u> In summer 2025 we recorded 192 sites of 100 × 100 m across NYC, each on three weekday mornings from 5:00 to 8:00 AM to capture the dawn chorus. All recordings have been processed with BirdNET. Sites held a mean of 6.8 species (SD 3.9; range 0-26), and species detection frequency ranged from \<1% to 95% of sites, which is enough variability to select bioindicator species for Aim 2.

**B.2. Study overview.** The proposed study is a longitudinal EHR-based cohort study. It links 100-m citywide bird biodiversity exposure surfaces, built from dedicated acoustic fieldwork, to annual frailty and biological age among older adults in the Mount Sinai Health System living in NYC (2023-2027). Aim 1 tests the soundscape pathway, Aim 2 tests the bioindicator pathway, and B.8 describes how the two are interpreted together (Figure 1).

<table>
<colgroup>
<col style="width: 70%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Table 1.</strong> Characteristics at cohort entry in the pilot</td>
</tr>
<tr class="even">
<td><strong>Characteristic</strong></td>
<td><strong>Overall (N = 20388)</strong></td>
</tr>
<tr class="odd">
<td>Age, years - mean (SD)</td>
<td>71.25 (7.18)</td>
</tr>
<tr class="even">
<td><strong>Age group - n (%)</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>65 – 74</p>
</blockquote></td>
<td>14649 (71.9)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>75 – 84</p>
</blockquote></td>
<td>4403 (21.6)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>≥ 85</p>
</blockquote></td>
<td>1336 (6.6)</td>
</tr>
<tr class="even">
<td><strong>Sex - n (%)</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Male</p>
</blockquote></td>
<td>7194 (35.3)</td>
</tr>
<tr class="even">
<td><strong>Race and ethnicity - n (%)</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>White</p>
</blockquote></td>
<td>9186 (45.1)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Black</p>
</blockquote></td>
<td>2963 (14.5)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Asian</p>
</blockquote></td>
<td>790 (3.9)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Other</p>
</blockquote></td>
<td>7449 (36.5)</td>
</tr>
<tr class="odd">
<td><strong>Insurance - n (%)</strong></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Commercial</p>
</blockquote></td>
<td>3419 (16.8)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Medicare</p>
</blockquote></td>
<td>14948 (73.3)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Medicaid</p>
</blockquote></td>
<td>558 (2.7)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Other</p>
</blockquote></td>
<td>1463 (7.2)</td>
</tr>
<tr class="even">
<td><strong>Neighborhood context - mean (SD)</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Census-tract poverty, %</p>
</blockquote></td>
<td>16.20 (11.94)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Census-tract non-Hispanic Black, %</p>
</blockquote></td>
<td>15.66 (20.66)</td>
</tr>
<tr class="odd">
<td><strong>Exposure and outcome - mean (SD)</strong></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shannon diversity, IQR-scaled</p>
</blockquote></td>
<td>3.04 (0.83)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VAFI deficit count</p>
</blockquote></td>
<td>1.74 (2.56)</td>
</tr>
</tbody>
</table>

**B.3. Study population and setting.**

<u>+ Mount Sinai Health System (MSHS):</u> MSHS comprises seven hospitals, \>400 ambulatory practice locations and \>7,200 physicians, serving a diverse patient population across all five NYC boroughs. *Inclusion criteria:* adults aged ≥65 years who had an MSHS primary care physician between 2023 and 2027 and a geocoded residential address in NYC, the extent of our exposure surfaces. *Sample:* our recent analysis of a very similar MSHS cohort included 20,388 adults and 123,103 person-years<sup>22</sup>, and we expect a cohort of comparable size (Table 1). *Follow-up:* participants enter in the first year with a documented MSHS encounter and are followed each calendar year until death or censoring. Follow-up ends at the last year of MSHS use when two consecutive years show no encounters, an approach under which missing data from low EHR continuity are minimal in this population<sup>40</sup>. *Feasibility:* residential addresses for all patients have been geocoded, and both outcomes have been calculated through 2025.

<u>+ Suitability of NYC:</u> NYC is the most populous and densely populated U.S. city<sup>41</sup>, with diverse habitats and \>400 bird species recorded annually<sup>42</sup>. Its neighborhoods range from densely built, high-pollution, low-greenspace areas to green, mixed-use ones, so findings generalize at the neighborhood level. Our exposure-modeling pipeline is adaptable to other U.S. cities.

**B.4. Exposure assessment.**

<u>+ Bird metrics:</u> Four metrics (Table 2) operationalize the two pathways in Figure 1. Three describe what residents hear (soundscape pathway): Audibility, passerine Shannon diversity and the Acoustic Evenness Index. The fourth, species presence, describes what bird presence signals about the environment (bioindicator pathway). The pipeline has five steps and all of them have been successfully piloted.

|                                                |                                                                                                                                                                                                      |                                                                                                                                                                                                          |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Table 2:** Exposure metrics.                 |                                                                                                                                                                                                      |                                                                                                                                                                                                          |
| **Method**                                     | **Brief description**                                                                                                                                                                                | **What it measures**                                                                                                                                                                                     |
| **Acoustic Evenness Index (AEI)**<sup>43</sup> | Partitions the spectrogram into frequency bins and applies the Gini coefficient to the distribution of acoustic energy across them; reverse-scored so higher values indicate a more even soundscape. | Soundscape structure: whether acoustic energy is spread evenly across frequencies (diverse, natural chorus) or concentrated in narrow bands (anthropogenic dominance, e.g. low-frequency traffic noise). |
| **Audibility**<sup>44</sup>                    | Proportion of sampled time-bins in which biological (bird) sound is detectable via BirdNET.                                                                                                          | Frequency of biophonic exposure: how often, across a day or recording period, birdsong is actually present in the ambient soundscape.                                                                    |
| **Passerine Shannon diversity**<sup>45</sup>   | Shannon Index applied to passerine species richness and relative vocal activity (detection counts, a proxy for relative abundance) from BirdNET detections.                                          | Composition of the bird community exposure: richness and evenness of passerine species heard, not just how much sound is present.                                                                        |
| **Specific species presence**                  | Detection-corrected probability of presence (occupancy model) of individually selected bioindicator species at a site.                                                                               | Bioindication: whether conditions meet the threshold a given species requires (or avoids), signaling a specific exposure (e.g., habitat quality, air quality) rather than a general diversity level.     |

**(1)** *Ground truth:* we will extend the 2025 fieldwork to 1,000 tiles of 100 × 100 m in total (808 new tiles in summer 2027), selected by spatially balanced stratified sampling with effort proportional to cohort address density, using the same recording protocol.

**(2)** *Processing:* BirdNET detections will be validated by Dr. Alaasam’s team, who will manually review a sample of detections for each species and set species-specific confidence thresholds that reach ≥90% precision. Each metric is then processed as described in Table 2. For species presence, single-season occupancy models fitted to the three recording mornings per tile<sup>46</sup> will estimate presence while accounting for the probability of detecting a species that is present, with detection allowed to vary with recording conditions such as wind, rain and background noise. Detection-corrected presence is the ground truth for step (3).

**(3)** *Modeling:* each metric is modeled separately with an ensemble model adapted from Dr. Kloog’s air pollution and temperature models<sup>47-49</sup>. Three base learners (mixed models, random forests and gradient boosting) are trained on the same predictors and combined by a generalized additive model whose weights vary in space, so that each learner contributes most where it performs best. Predictors are the high-resolution spatial layers already assembled for those models and for our urban nature work, including vegetation, land cover, built environment, road density and artificial light at night, and each metric is predicted citywide at 100-m resolution. We will train on the 2027 recordings and generate one static surface per metric, assigned to residential addresses as a long-term spatial contrast across 2023-2027. The 2025 pilot tiles are excluded from fitting and serve as temporally independent validation. Applying one surface to 2023-2027 assumes that spatial contrasts in bird communities are stable over a few years; agreement between the 2027-based predictions and the 2025 recordings tests this assumption.

**(4)** *Evaluation:* we use a spatially blocked 60/20/20 training/validation/test split to limit optimism from spatial autocorrelation, reporting RMSE, R² and Spearman’s ρ for continuous metrics and, for species presence, the area under the ROC curve (AUC) against observed detections.

**(5)** *Exposure assignment:* exposures will be assigned each year from that year’s residential address, so moves during follow-up are reflected in exposure. Residential assignment suits this population: older adults spend most of their time at home, about 72% of the week in a multi-ethnic U.S. cohort<sup>50</sup>.

<u>+ Standard environmental exposures:</u> **PM<sub>2.5</sub>** will come from Dr. Kloog’s spatiotemporal models at the same 100 × 100 m tiles, as annual averages. **Greenness** will be annual average 30-m NDVI within 300 m of the residence, with 100-m and 500-m buffers and the 100-m tiles as sensitivity analyses. **Traffic noise** will be the 24-h equivalent sound level (LAeq,24h) from the BTS National Transportation Noise Map. PM<sub>2.5</sub> and greenness have been linked to MSHS EHR data in prior analyses<sup>40,51,52</sup>.

<u>+ Covariates:</u> Selected using directed acyclic graphs, as in our prior work, to identify confounders of the bird-aging association: age, sex, race and ethnicity, insurance type, tract-level poverty, and tract-level sociodemographic metrics. Neighborhood socioeconomic status is the main confounder of concern: wealthier urban neighborhoods tend to support more diverse plant and animal communities, the “luxury effect”<sup>53</sup>, and also tend to have healthier older residents. In sensitivity analyses, we will add neighborhood (Neighborhood Tabulation Area) fixed effects, so that associations are estimated from contrasts within neighborhoods and remaining spatially structured confounding is absorbed.

**B.5. Outcomes.**

<u>+ Frailty (VA-FI):</u> We will measure frailty with the 31-item VA-FI, which captures deficit accumulation from diagnosis and procedure codes and has been updated for ICD-10<sup>54</sup>. It requires no laboratory data, which keeps it independent of our second outcome, PhenoAgeAccel. The VA-FI was developed in Veterans Affairs EHR data, so differences in coding conventions, encounter structures and clinical workflows could affect deficit ascertainment in a non-VA health system. In preliminary analyses of MSHS EHR data, we confirmed that all 31 deficits are present and calculable, with distributions consistent with published VA-FI values. Each deficit is assessed annually using a 3-year lookback window (the assessment year and the two prior years), using 2021-2022 data for lookback only.

<u>+ Biological age (PhenoAgeAccel):</u> Biological age reflects how far a person’s physiology has aged, which can diverge from chronological age. We will estimate it with Phenotypic Age (PhenoAge), which combines chronological age with nine clinical biomarkers: albumin, creatinine, glucose, C-reactive protein (CRP), lymphocyte percent, mean cell volume, red cell distribution width, alkaline phosphatase and white blood cell count<sup>10</sup>. Because PhenoAge is highly correlated with chronological age, partly because age enters its formula, we will use PhenoAge acceleration (PhenoAgeAccel): the residual from a linear regression of PhenoAge on chronological age in our cohort<sup>55</sup>. Positive values indicate an older biological age than expected for a person’s chronological age. Because PhenoAgeAccel is independent of chronological age by construction, PhenoAgeAccel models will not further adjust for age. We will derive PhenoAge from outpatient results only, because inpatient values may reflect acute illness rather than aging. Six biomarkers are part of routine annual panels and were each missing in \<1% of person-years in a very similar MSHS cohort. CRP, albumin and alkaline phosphatase are ordered more selectively and accounted for ~63%, ~16% and ~9% of incomplete person-years, respectively<sup>51</sup>. We will therefore impute missing biomarkers with multiple imputation by chained equations (MICE), which in previous analysis in this cohort gave estimates consistent with complete-case analyses while substantially increasing the analyzable sample<sup>51</sup>.

**B.6. Analysis, Aim 1.**

**(1a)** For each soundscape metric and each outcome (six models), we will fit generalized additive models (GAMs): negative binomial for the VA-FI deficit count and Gaussian for PhenoAgeAccel. Each model has a patient-level random intercept for repeated measures, a penalized spline of calendar year, the IQR-scaled exposure, and the covariates from B.4 (PhenoAgeAccel models exclude chronological age; see B.5). We will control the false discovery rate (FDR) across the six models using Benjamini-Hochberg. As a secondary analysis, an exposure × follow-up year interaction will estimate whether each metric is associated with the rate of change in each outcome, not only its level.

**(1b)** We will first report correlations between each birdsong metric and traffic noise and greenness, to confirm the exposures can be separated. We will then add traffic noise and greenness together to each 1a model, and report the adjusted estimate and its percentage change.

**B.7. Analysis, Aim 2.** *Species selection.* We will select around five species using two criteria: published evidence that the species’ presence reflects habitat quality or air quality, and sufficient prevalence and variability in our fieldwork data. Five additional species are kept as back-ups in case candidates prove too rare. Examples are the Gray Catbird (understory vegetation) and the Chimney Swift (flying-insect supply; because it nests in chimneys, its presence also depends on building stock, which we will weigh in final selection).

**(2a)** For each species and outcome, we will fit the Aim 1 GAMs with the predicted probability of species presence at the residence as a continuous, IQR-scaled predictor (dichotomized at the threshold that maximizes sensitivity plus specificity in the validation set as a sensitivity analysis), controlling FDR across species and outcomes using Benjamini-Hochberg. We will also report each species’ association adjusted for PM<sub>2.5</sub> and greenness.

**(2b)** For PM<sub>2.5</sub> and for greenness, we will fit each exposure-outcome model with and without each species’ presence probability. We will report the proportion of the exposure’s association explained by species presence (change in estimate), with confidence intervals from a bootstrap that resamples neighborhoods, to account for spatial clustering. Because species surfaces share predictors with greenness and PM<sub>2.5</sub>, some attenuation is expected by construction. We will therefore compare each species’ change in estimate with a null distribution from 100 pseudo-species surfaces, built by the same ensemble after random spatial shifts of that species’ tile labels, which preserve prevalence and spatial autocorrelation but break the link with local conditions. Species presence will be considered to explain an association only if its change in estimate exceeds the 95th percentile of this null distribution.

*Sensitivity analyses (both aims):* alternative NDVI buffers (100 m, 500 m, 100-m tiles); neighborhood fixed effects (B.4); additional adjustment for annual number of MSHS encounters, because deficit ascertainment increases with health care use; restriction to residences with low between-learner prediction variance (B.4); complete-case analyses of PhenoAgeAccel without imputation (B.5); restriction to person-years with an EHR continuity index \>0.8; and a negative control outcome, annual influenza vaccination, which reflects health-seeking behavior and access to care but has no plausible direct pathway from bird biodiversity, modeled with logistic GAMs using the same structure.

**B.8. Integrating the two pathways.** Because both aims use the same cohort, outcomes and covariates their estimates are directly comparable, and we will interpret them jointly. If birdsong exposure is associated with the outcomes beyond traffic noise and greenness, but species presence is not, the soundscape pathway is supported. If species presence explains part of the PM<sub>2.5</sub> and greenness associations, but birdsong exposure does not persist after adjustment, the bioindicator pathway is supported. If both hold, the pathways act together. If neither holds, the pilot association most likely reflects standard exposures.

**B.9. Statistical power.** In our prior MSHS cohort of similar size, the association between bird Shannon diversity and VA-FI had a standard error of 0.34% per IQR. Because exposure varies mainly between persons, precision depends mainly on the number of participants, so we assume similar precision here. We computed power conservatively at Bonferroni-adjusted α, which is stricter than the FDR control used in analysis. *Aim 1* (α = 0.0083 across six models): 80% power to detect a 1.2% difference in expected VA-FI deficit count per IQR, and \>90% power for the 1.4% observed in the pilot. For PhenoAgeAccel (SD 6.56 years in preliminary data), the minimum detectable difference is 0.3 years per IQR. *Aim 2* (α = 0.005 across about 10 tests): 80% power to detect a 2.1% difference between presence and absence for species present at ≥25% of residences when presence is dichotomized; because dichotomizing generally reduces power, this estimate is conservative for the continuous primary analysis.

**B.10. Risks and alternatives. (1)** *VA-FI outside the VA:* all deficits are calculable in MSHS data, with distributions consistent with published values (B.5). If specific deficits prove under-recorded, we will recompute the index from the deficits with adequate ascertainment and report results with and without them. **(2)** *EHR discontinuity:* addressed by the censoring rule and a high-continuity sensitivity analysis (B.3, B.7). If continuity is lower than expected, we will weight person-years by the inverse probability of high continuity, estimated from demographics and baseline health care use. **(3)** *Unmeasured confounding:* addressed by DAG-based adjustment, neighborhood fixed effects, adjustment for health care use and a negative control outcome (B.4, B.7). If the negative control outcome shows an association, we will use E-values to quantify how strong unmeasured confounding would need to be to explain the main estimates, and interpret them accordingly. **(4)** *Rare bioindicator species:* addressed by substitution from the back-up list (B.7). If fewer than five species meet the prevalence criterion, we will analyze species that share an indicator role (e.g., shrub-nesting species) as guilds, which increases prevalence. **(5)** *Correlated exposures:* checked before modeling and reported transparently (B.6). If a birdsong metric is too strongly correlated with traffic noise or greenness to separate them, we will use its residual after regressing it on both, which isolates birdsong variation not explained by standard exposures. **(6)** *Incomplete fieldwork:* tiles will be recorded in a prespecified random order within sampling strata, so a shortfall from weather, equipment loss or site access keeps the sample spatially balanced; any missing tiles will be recorded in early summer 2028 and used to update the surfaces before Aim 2 analyses (B.12). **(7)** *Low predictive performance:* if a metric is poorly predicted on the held-out test set, we will refit it at a coarser resolution (e.g., 300 m); a poorly predicted species will be replaced from the back-up list (B.7). If the spatially varying weights overfit the training tiles, we will combine the base learners with fixed weights. **(8)** Exposure prediction error: error from modeled surfaces is partly Berkson-like, which mainly widens confidence intervals, and partly classical-like, which can bias estimates <sup>56</sup>; a sensitivity analysis restricts to residences with low between-learner variance (B.7).

**B.11. Rigor and reproducibility.** Analyses will be prespecified and reported following STROBE. Exposure surfaces and all code will be shared under FAIR principles through NIH-approved repositories, Mount Sinai’s Greener platform and the lab’s GitHub, consistent with NIH’s Data Management and Sharing Policy.

**B.12. Timeline:**

<table style="width:100%;">
<colgroup>
<col style="width: 24%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="6"><blockquote>
<p><strong>2027</strong></p>
</blockquote></th>
<th colspan="12"><blockquote>
<p><strong>2028</strong></p>
</blockquote></th>
<th colspan="6"><blockquote>
<p><strong>2029</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>TIMELINE:</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Jul</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Aug</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Sep</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Oct</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Nov</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Dec</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Jan</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Feb</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Mar</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Apr</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>May</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Jun</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Jul</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Aug</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Sep</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Oct</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Nov</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Dec</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Jan</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Feb</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Mar</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Apr</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>May</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Jun</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Fieldwork</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Audio processing and validation</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Predictor processing</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Modeling and validation</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Aim 1: EHR processing</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Aim 1: Analysis</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Aim 1: Manuscript submission</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Aim 2: EHR processing</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Aim 2: Analysis</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Aim 2: Manuscript submission</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# C. EXPERTISE AND RESOURCES

**C.1. Investigators. Dr. Knobel (PI)** is a geospatial epidemiologist focused on urban nature and aging, and leads this R21 and the P30 pilot that informed it. **Dr. Alaasam** is an urban ecologist and ornithologist with experience in large-scale acoustic fieldwork and avian responses to urban disturbance. **Dr. Yitshak-Sade** is an environmental epidemiologist with expertise in older-adult cohorts, including MSHS. **Dr. Kloog** develops high-resolution spatiotemporal exposure models. **Dr. Midya** is a biostatistician specializing in environmental epidemiology and interpretable machine learning. **Dr. Federman** is a primary care physician, Professor of Medicine, and director of the NIA Aging and Dementia T32.
