---
source_file: 85bb8fdf-research-proposal-v0-17.docx
sha256: 14cae0dfd42026c36847b661a3986f546629889ddcba909c31456305eb54ec2b
converted: 2026-11-17
method: pandoc
pages: 
---
**RESEARCH PROPOSAL**

***Ramón y Cajal Grants, Call 2026***

# 1. RESEARCH PROPOSAL DATA

**PRINCIPAL INVESTIGATOR (Name and surname):** Pablo Knobel

**TITLE OF THE RESEARCH PROPOSAL (ACRONYM):** Mapping where we age: the urban continuum and dementia (CONTINUUM)

**TÍTULO DEL PROYECTO (ACRÓNIMO):** Cartografiar dónde envejecemos: el continuo urbano y la demencia (CONTINUUM)

# 2. JUSTIFICATION AND NOVELTY OF THE RESEARCH PROPOSAL

## 2.1. Motivation of the research proposal

### 2.1.1. Overview

CONTINUUM asks which features of the places where older adults live matter for dementia, from city centers to remote villages, when all are measured consistently across space and time. I call this full range of places and features the **urban continuum**. CONTINUUM first uses high-resolution aerial imagery and machine learning to describe where people live at two levels: **types of place**, the kinds of environment people live in, from dense mixed-use neighborhoods to remote villages; and **features**, specific elements such as playgrounds or street trees. The result is a series of annual maps of all of Catalonia. CONTINUUM then uses these maps to estimate the joint association of the mapped features with developing dementia and with its severity at diagnosis.

Catalonia combines three resources that are rarely available together (data source boxes, Sections 3.2.2–3.2.4): orthophotos of the whole territory at 25 cm every year since 2012, released openly by the Institut Cartogràfic i Geològic de Catalunya (ICGC); the primary care records of about three quarters of the population in the Information System for Research in Primary Care (SIDIAP), with validated dementia diagnoses; and the Girona Dementia Registry (ReDeGi), which records the Mini-Mental State Examination (MMSE) at diagnosis and has already been linked to SIDIAP.

### 2.1.2. Relevance and state of knowledge

<u>Population aging makes dementia one of Spain's main public health challenges.</u> People aged 65 and over make up 21.1% of Spain's population today, and this share is projected to reach about 30.9% by 2076 (Instituto Nacional de Estadística \[INE\], 2026). In Spain's 2023 national health survey, 12.1% of people aged 85 and over reported Alzheimer's disease or another dementia, 15.1% of women and 5.9% of men (Ministerio de Sanidad, 2025). Dementia is a leading cause of disability and dependency in later life (World Health Organization \[WHO\], 2025), and most of its care falls on families. In Spain, dementia costs about €28,700 per person per year (Montes-Martinez et al., 2026), most of it informal care by families (Meijer et al., 2022).

<u>There is still no curative treatment, so prevention is central.</u> The 2024 Lancet Commission estimated that addressing 14 modifiable risk factors could prevent or delay about 45% of dementia cases (Livingston et al., 2024). Several of these factors, such as physical inactivity, social isolation, depression, hypertension and air pollution, are shaped by where people live (Chen et al., 2022). In other words, part of dementia prevention happens outside the clinic, in the neighborhoods that older adults use every day.

<u>The environments where people live shape how they age.</u> Greenness and walkability have been linked to better cognitive function, mental health and physical capability in older adults (de Keijzer et al., 2020). For dementia, higher residential greenness has been associated with lower incidence in UK Biobank (Hu et al., 2023) and with slower cognitive decline in the Whitehall II cohort (de Keijzer et al., 2018), while living near major roads has been associated with higher incidence (Yuchi et al., 2020). In Japan, older adults in neighborhoods with more sidewalks had lower dementia incidence, but only in urban areas (Tani et al., 2021). Two systematic reviews found that population density, street connectivity, walkability, land-use mix and neighborhood resources were mostly associated with better cognition, but exposure measures were too heterogeneous to pool, most studies were cross-sectional, and only one was set in a rural area (Besser et al., 2017; Song et al., 2024). Quality may also matter as much as quantity: in Barcelona, the quality of nearby green spaces was associated with their use, physical activity and weight, independently of how much green space was available (Knobel et al., 2021b; Section 3.5).

<u>Most studies measure the residential environment with tools built for other purposes, one exposure at a time.</u> Greenness comes from vegetation indices such as the Normalized Difference Vegetation Index (NDVI), walkability from street networks, land-use mix from cadastral or zoning data, traffic from road inventories, and street-level detail from audits or street view images. Many of these layers are produced city by city, with different methods, definitions and years, so they cannot be compared across places, and towns and villages are often not covered (Besser et al., 2017; Song et al., 2024). Most are also snapshots: a city may audit its streets or count its trees once, but dementia develops over decades, and studies need exposure measured the same way every year (Song et al., 2024). Audits capture the most detail, such as the 90 items in 11 dimensions of green space quality rated by RECITAL (Knobel et al., 2021a), but they are costly and rarely repeated.

| **Gap 1. No consistent measure across places and years.** Measures differ from city to city and some are rarely repeated, so exposure cannot be compared between areas or followed over time. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<u>The residential environment can act on dementia through several co-occurring pathways.</u> Markevych et al. (2017) grouped the pathways linking green space to health into three domains that also apply to the wider built environment: *reducing harm*, such as lower exposure to traffic, noise and heat; *restoring capacities*, such as stress recovery in attractive spaces; and *building capacities*, such as the physical activity and social contact that walkable streets, squares and parks encourage. These pathways can work in either direction: depending on the feature, the residential environment can reduce or add harm, and build or erode capacities. Because features co-occur, they are best studied together: single-exposure models may under- or overestimate their effects. The exposome, the totality of environmental exposures a person encounters throughout life (Wild, 2005), offers a framework for this, and mixture methods have been developed to answer the questions it poses. Joint analyses of the neighborhood environment exist for mortality (Klompmaker et al., 2020) and stroke (Poulsen et al., 2023) but remain rare for dementia.

| **Gap 2. Environmental exposures are studied one at a time.** Joint analyses of the residential environment remain rare for dementia, so it is still open which features matter most when all are considered together. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<u>Prevention is not only about who develops dementia, but also about how advanced it is when it is diagnosed.</u> Severity at diagnosis shapes treatment options, care planning and the burden on families, and reflects both the disease and access to diagnosis. A link between place and severity at diagnosis could therefore reflect two stories: slower decline, for example through the reserve built by activity and social contact, or later diagnosis, through poorer access to care. Both matter, and they call for different responses. Environmental studies of dementia, however, have mostly examined who develops it, not how advanced it is when diagnosed.

| **Gap 3. Onset is studied, severity rarely.** How the residential environment relates to severity at diagnosis has rarely been examined. |
|------------------------------------------------------------------------------------------------------------------------------------------|

<u>Deep learning applied to images has opened a new route for exposure science</u> (Weichenthal et al., 2019). Street view and satellite images have been used to characterize greenery and the built environment in relation to dementia, obesity and cardiometabolic disease (Maharana & Nsoesie, 2018; Chen et al., 2024; Jimenez et al., 2026), and 1 m maps of tree canopy have been linked to mortality in about 6.2 million Swiss adults (Chi et al., 2025), which shows that high-resolution maps can be linked to whole populations. These studies, however, measure one or two elements, describe places only by type, or summarize images in scores that cannot be interpreted. Aerial photographs offer more: they cover whole regions and are retaken at regular intervals, so one method, deep learning in this proposal, can measure every place, every year; and each image shows many features at once, so they can be measured together and modeled jointly.

### 2.1.3. Originality and innovation

CONTINUUM is original in three ways, one for each gap:

- **The whole urban continuum, mapped every year (Gap 1; Aim 1).** CONTINUUM measures every place where people live, from dense centers to villages, with one approach: at 25 cm, every year since 2012, at two levels, types of place and presence of features. Labels and models will be released openly, so the maps can be updated each year and transferred to the rest of Spain through the national orthophoto program (Plan Nacional de Ortofotografía Aérea, PNOA; Instituto Geográfico Nacional, n.d.). To my knowledge, no study has mapped a broad array of named features of the residential environment, beyond land cover, every year across an entire region, let alone linked them to dementia or any other health outcome.

- **The residential environment as a mixture (Gap 2; Aims 1 and 2).** Studies of residential features and dementia typically examine one feature at a time or combine several into a single index. CONTINUUM measures all features with one pipeline, so they are comparable without harmonizing data from different sources. It keeps each feature separate and models them jointly with quantile g-computation (Keil et al., 2020) and Bayesian kernel machine regression (BKMR; Bobb et al., 2015), two methods designed for exposures that co-occur. The design can show whether a few features account for most of the joint association, which identifies the strongest candidates for intervention studies and natural experiments.

- **Beyond diagnosis: severity (Gap 3; Aim 2b).** Most environmental epidemiology of dementia stops at diagnosis: it asks who develops dementia and when. CONTINUUM goes one step further and asks how advanced dementia is when it is diagnosed, an outcome that matters for patients, families and services because it shapes treatment options, care planning and costs (Gómez Maldonado et al., 2024). Aim 2b also explores the two stories behind severity, slower decline and later diagnosis, so the results can point either to the design of places or to timely diagnosis.

### 2.1.4. Novelty of the expected contribution

CONTINUUM will contribute the three products set out in Section 2.1.3: **an open, annual map** of every place in Catalonia; **a transferable pipeline** of labels, models and code; and **joint evidence** on residential features and dementia, from onset to severity. Each rests on established parts (Section 3.5).

### 2.1.5. Interdisciplinarity

The proposal sits in Biomedicine and draws on Information and Communication Technologies (computer vision for Aim 1), Environmental Sciences and Technologies (remote sensing and exposure assessment) and Social Sciences (geography and urban planning).

## 2.2. Starting hypothesis and novelty

### 2.2.1. Starting hypothesis

**Overarching hypothesis.** The types and features of the places where people live can be measured from aerial imagery consistently across the whole urban continuum and over time, and these potentially modifiable factors are associated with developing dementia and with its severity at diagnosis.

- **H1a (Gaps 1 and 2; Aim 1a).** Aerial images of all of Catalonia can be grouped into types of place that are stable and interpretable across years and along the whole continuum.

- **H1b (Gaps 1 and 2; Aim 1b).** Features of the residential environment can be detected in 25 cm orthophotos with accuracy that does not differ materially between urban, peri-urban and rural settings, so that one map can serve cities, towns and villages.

- **H2a (Gap 2; Aim 2a).** Among adults aged 65 and over, the features of the census section where people live are associated with dementia incidence, individually and jointly, with a few features accounting for most of the joint association.

- **H2b (Gaps 2 and 3; Aim 2b).** Among people diagnosed with dementia, the features of the places where they lived before diagnosis are associated with severity at diagnosis (MMSE score and Clinical Dementia Rating), individually and jointly.

For H2a and H2b, we will also test whether associations differ along the urban continuum (by setting) and by sex, without a pre-specified direction (Section 4.6). The hypothesis rests on the pathways in Section 2.1, through which features can act on several modifiable risk factors for dementia; on prior associations of single features with dementia; and on my previous work showing that such features can be detected in aerial images (Section 3.5).

### 2.2.2. Starting point

CONTINUUM is a thematic follow-up of my previous work, not the direct continuation of one project. Aim 1b adapts the pipeline I coordinated in the United States, where my team labeled about 8,000 aerial image tiles and trained models that mapped 10 green space quality items across the continental United States. On held-out tiles, the models reached a macro F1 of 0.81 (Knobel et al., 2026a; Section 3.5). The rest builds on two lines of my work. In exposure assessment, I developed RECITAL, which rates green space quality item by item, and built new exposure maps, such as annual maps of bird diversity. In the urban exposome, I have studied air pollution, urban nature and social vulnerability with mixture methods, in relation to aging outcomes such as biological age, frailty and cardiovascular disease. I therefore have experience in every part of CONTINUUM.

### 2.2.3. Novelty

The novelty of CONTINUUM is the question it makes answerable: which parts of the places where people live matter for dementia, measured the same way in every city, town and village, every year. It gets there by bringing together approaches that are mature but rarely combined: deep learning and exposure assessment, to measure the residential environment consistently across space and time; the exposome and mixture methods, to study its features together; and environmental epidemiology and large health records, to link them to dementia in over one million older adults. Each part has been tested; none can answer the question alone.

# 3. OBJECTIVES, METHODOLOGY AND WORK PLAN

## 3.1. General and specific objectives

**General objective.** To map the types and features of the places where people live across all of Catalonia, every year since 2012, and to test whether they are related to developing dementia and to how severe dementia is when diagnosed.

**Aim 1 (Gaps 1 and 2).** Build an annual, open map of the types and features of every census section of Catalonia, from 2012 onward.

- **1a (H1a).** Identify the types of place in aerial photographs with unsupervised learning.

- **1b (H1b).** Train and validate computer models that recognize features in aerial photographs.

**Aim 2 (Gaps 2 and 3).** Estimate how the features of where people live relate to dementia across the urban continuum.

- **2a (H2a).** Among adults aged 65 and over in Catalan primary care records, test whether the features of where they live, individually and as a mixture, are associated with the risk of developing dementia.

- **2b (H2b).** Among people diagnosed with dementia in the Girona Dementia Registry and linked to SIDIAP, test whether the places they lived before diagnosis are associated with how severe dementia was when it was diagnosed.

Aim 1 yields the open maps and pipeline, and Aim 2 the evidence on dementia (Section 4.1).

## 3.2. Description of the methodology

### 3.2.1. Overview

CONTINUUM has two linked parts (Figure 1). <u>Aim 1 is an exposure science study:</u> it builds annual maps of types and features for every census section of Catalonia from 25 cm orthophotos. <u>Aim 2 is an epidemiological study:</u> it links these maps to dementia incidence in SIDIAP (Aim 2a) and to dementia severity at diagnosis in ReDeGi (Aim 2b).

<img src="media/image1.png" style="width:6.26443in;height:2.1595in" alt="Diagrama El contenido generado por IA puede ser incorrecto." />

**Figure 1. Gaps, aims and hypotheses.** Numbers on each aim mark the gaps it addresses. Aim 1 maps types and features of the residential environment every year; Aim 2 links these maps to dementia incidence and to severity at diagnosis. BKMR, Bayesian kernel machine regression; MMSE, Mini-Mental State Examination.

### 3.2.2. Aim 1: Measuring the urban continuum across Catalonia

Aim 1 turns annual aerial photographs of Catalonia (Figure 2a) into two products. **Types** (Aim 1a) group tiles by what they look like, with an unsupervised approach that needs no labels (Figure 2b). **Features** (Aim 1b) record specific elements present in each sub-tile, with a supervised approach trained on labeled images (Figure 2c). Features are the main exposure in Aim 2. Types have three roles: they guide which images are labeled, they describe places for planners, and they are tested as a secondary exposure.

| **Units used in this proposal.** **Setting**: urban, peri-urban or rural. **Context**: broad kind of place from the first clustering stage, such as built-up areas, farmland or forest. **Type**: finer kind of place within a context. **Sub-tile** (32 m): unit at which features are labeled and predicted. **Tile** (64 m): unit for types. **Census section**: unit at which each person's exposure is assigned. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Data source: ICGC orthophotos.** The ICGC territorial orthophoto series covers all of Catalonia every year at 25 cm since 2012. It is released under a Creative Commons Attribution 4.0 (CC BY 4.0) license and can be downloaded free of charge from the ICGC download service or accessed through its web map services, which the pilot used (Section 3.5). |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<img src="media/image2.png" style="width:6.29921in;height:2.42014in" alt="Mapa El contenido generado por IA puede ser incorrecto." />

**Figure 2. Census section 1707906003 in Girona.** (a) 25 cm orthophoto (ICGC, 2025, CC BY 4.0). (b) Contexts from the pilot typology on 64 m tiles; types within each context are shown in Figure 6. (c) Simulated example of one feature, sidewalks, recorded as present or absent in 32 m sub-tiles; this panel illustrates the planned output and is not a model result. Areas outside the section are lightened.

#### Generating tiles

We divide all of Catalonia into a regular grid of 64 m tiles, the unit for types, and split each tile into four 32 m sub-tiles, the unit for features (Figure 3). A 32 m square is small enough to show whether a tree crown or a crossing is present, and a 64 m square gives the context needed to tell what kind of place a tile is. Each tile is also assigned a setting, urban, peri-urban or rural, from the Eurostat Degree of Urbanisation (Eurostat, 2021), which we use to stratify sampling, validation and analyses.

<img src="media/image3.png" style="width:6.3in;height:1.50903in" alt="Imagen que contiene Diagrama El contenido generado por IA puede ser incorrecto." />

**Figure 3. Study area and tiles.** We cover all of Catalonia's census sections in full on a regular grid of 64 × 64 m tiles (256 × 256 pixels at 25 cm), the unit for the typology, and split each tile into four 32 × 32 m sub-tiles, the unit at which features are labeled and predicted; each person's exposure is the census section where they live. Catalonia comprises about 7.8 million tiles and 31 million sub-tiles per year. Shapes and squares are not to scale; the example tile is from section 1707906003 (Girona), ICGC 2025 orthophoto (CC BY 4.0), and the dashed quarter marks the enlarged sub-tile.

#### Aim 1a: Types

Using the orthophotos of every year, Aim 1a groups the 64 m tiles of Catalonia into types of place that look alike (H1a).

Each tile is summarized with image embeddings, a numerical summary of what an image looks like, from a model pretrained on millions of images (DINOv2; Oquab et al., 2023). As in recent studies that grouped satellite images into types of place (Metzler et al., 2023; Chen et al., 2026), tiles are then grouped in two stages. First, each tile's embedding is averaged with those of its neighbors over about 320 m (5 × 5 tiles), a walkable distance, and these neighborhood summaries are clustered into broad **contexts**, such as built-up areas, farmland or forest. Second, tiles are clustered within each context by their own embedding into finer **types**, so that dense areas, which hold most residents but a small share of the territory, keep their internal diversity. At each stage, the number of groups is set by the elbow of the clustering curve, the point beyond which more groups explain little more, and checked by its stability across bootstrap samples. Types are described afterwards from representative tiles and outside data, which never enter the clustering. The clustering will be fitted on a sample of tiles stratified by year and setting, with built-up contexts over-represented because most people live there, and applied to every year, so that each type means the same thing across years. We will report how often a tile changes type between consecutive years, and two team members will name each type blind from random tiles, with their agreement reported as a check of interpretability.

#### Aim 1b: Features

Using about 10,000 labeled sub-tiles, Aim 1b trains models that detect features in every 32 m sub-tile of Catalonia, every year (H1b). It has four steps: selecting the features, labeling a sample of sub-tiles, training the models and applying them to every sub-tile.

| **Table 1.** Initial features  |                                                        |
|--------------------------------|--------------------------------------------------------|
| **Feature**                    |                                                        |
| Tree canopy                    | Sports and play areas                                  |
| Tree-lined streets and ramblas | Marked pedestrian crossings                            |
| Blue space                     | Sidewalks                                              |
| Public park or garden          | Major roads and railways                               |
| Square or plaza                | Large sealed surfaces                                  |
| Inner-block courtyards         | Industrial and warehouse yards                         |
| Vegetable plots                | Neglect (vacant or derelict plots, roofless buildings) |

| <img src="media/image4.png" style="width:1.87294in;height:3.21075in" alt="Interfaz de usuario gráfica, Aplicación El contenido generado por IA puede ser incorrecto." />            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Figure 4. Labeling task (mockup).** The tool shows nine 32 m sub-tiles and asks the labeler to mark every one that contains a given feature, here trees. Images: ICGC, CC BY 4.0. |

**Feature selection.** Each feature must meet four criteria, in this order: **(i)** relevance, it maps onto at least one of the three pathways; **(ii)** visibility, it can be seen at 25 cm; **(iii)** reliability, two labelers agree on it beyond chance; and **(iv)** variability, it is present in some sub-tiles and absent in others across most of the continuum. From 95 candidates, drawn from two audit tools (POSDAT, Edwards et al., 2013; RECITAL, Knobel et al., 2021a), the literature on the built environment and cognition (Cerin et al., 2024; Michael et al., 2024; Song et al., 2024) and features typical of Catalan towns and villages, such as ramblas and vegetable plots, I selected 14 initial features (Table 1). The set is a starting point: features will be removed or added as we pilot and iterate.

**Labeling.** The team will label sub-tiles with a grid task (Figure 4): the tool shows nine separate 32 m sub-tiles and asks the labeler to mark every one that contains a given feature, a format that is fast, needs little training and works well for rare features. Labeling will follow a written protocol. Labels are drawn from flights spread over years 2012–2025. 10% of sub-tiles are labeled twice, and features with agreement (Cohen's κ) below 0.60 are merged or dropped; known positive and negative sub-tiles are mixed into every set to check each labeler. The typology from Aim 1a guides labeling: it ensures that every type is sampled and decides which features are asked about in each sub-tile, so, for example, that labelers are not asked about sidewalks in a forest; features not asked about are left out of the training loss rather than treated as absent. After a first batch sampled across types and settings, we will use active learning, which asks labelers about the images the model is least sure of or where rare features are likely, to make the most of labeling time.

**Model training.** We will fine-tune the pretrained image model with a classification layer that predicts, for each sub-tile, the presence of each feature. Labeled sub-tiles will be split by spatial block, because nearby tiles are similar and random splits overstate accuracy: the test set is drawn from the first, type-stratified batch, before active learning, so that it represents Catalonia rather than the hardest images, and the remaining labels are split 75/25 into training and tuning sets. Augmentation, random changes in color, brightness and orientation during training, and per-year color normalization will make the models robust to differences between flights.

**Validation.** For each feature, we will report the F1 score on the test set, a measure that penalizes both missed and false detections, with its precision and recall, overall, within each setting and within each flight year, with bootstrap confidence intervals. A feature passes if its F1 is at least 0.70 overall and in each setting. Accuracy is compared between settings because a map that is less accurate in villages would bias comparisons along the continuum: H1b is supported if the 90% confidence interval of the difference in F1 between settings lies within ±0.10. It will be tested for features with at least 100 test positives in each setting; the rest will be reported descriptively. To check the maps as exposures, we will compare predicted and labeled prevalence in a sample of fully labeled census sections in each setting, and report how often predictions change between consecutive years in sub-tiles whose type does not change.

**Annual maps and open release.** We will apply the models to every sub-tile for each year from 2012. For each year and census section, each feature will be summarized as its prevalence: the percentage of the section's sub-tiles in which it is present. A section where trees appear in 40 of every 100 sub-tiles has a tree canopy prevalence of 40%. The share of each type will be computed in the same way. Because rural sections are large and mostly farmland or forest, we will also compute a residential prevalence, over the sub-tiles within 300 m of a residential building, so that a village is described by its streets and not by the surrounding fields. Before any health analysis, we will describe how features are distributed by setting and census-section deprivation, to show where they are scarce. Maps will be summarized on each year's census-section boundaries, with a crosswalk between years. The annual tile-level and census-section maps (features in private spaces and neglect only as census-section summaries; Section 6), labeled images, trained models and code will be released under licenses compatible with the ICGC license (CC BY 4.0), in a public repository with a persistent identifier.

| **Critical stage (Month 24).** A feature enters Aim 2 only if labelers agree on it (κ ≥ 0.60) and its model reaches an F1 of at least 0.70 overall and in each setting; features that fail are excluded (Section 3.4). |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### 3.2.3. Aim 2a: Features and incident dementia

Using the Aim 1 maps and the primary care records of over one million older adults, Aim 2a tests whether the features of where people live, separately and together, are associated with dementia incidence (H2a), and which matter most.

| **Data source: SIDIAP.** SIDIAP contains the pseudonymized primary care records of the 5.8 million people assigned to the 328 primary care centers of the Catalan Institute of Health, about 75% of the Catalan population (Recalde et al., 2022). It includes diagnoses, prescriptions and dispensing, clinical measurements, smoking status, primary care visits, nursing-home residence, death, residence history and census section of residence, and it can be linked to hospital discharge records. Its dementia diagnoses have been validated (positive predictive value 91%; Ponjoan et al., 2019a), and it has been linked to environmental exposures at census-section level (de Bont et al., 2021). Access is open to researchers from public institutions, after approval by the SIDIAP scientific committee and the ethics committee of the Jordi Gol i Gurina Foundation Research Institute for Primary Health Care (IDIAPJGol). |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Population.** We will include people aged 65 and over registered on 1 January 2013, or reaching age 65 during follow-up, through the latest available year. We will exclude people with a dementia record before entry and require at least one year of registration before entry, to avoid counting prevalent cases as incident. We will also exclude people living in a care home at entry and end follow-up when a person moves into one, because the neighborhood no longer describes their daily environment; a dementia diagnosis recorded within 90 days after the move will count as an event. Because care-home entry often accompanies undiagnosed dementia, we will report how many first diagnoses fall in the year around entry and, as a sensitivity analysis, treat entry as a competing event. Catalonia has about 1.6 million residents aged 65 and over (Institut d'Estadística de Catalunya \[Idescat\], 2025), so we expect over one million eligible people. Results apply to the population served by the Catalan Institute of Health.

**Exposure.** Each person will be assigned the Aim 1 values of the census section where they live for each year, updated when they move using the residence history in SIDIAP. The main exposure is the residential prevalence of each feature; whole-section prevalence is a sensitivity analysis, and the share of each type is used in the analysis of types. The main exposure window will be the year before each follow-up year, to reduce reverse causation from the prodromal phase; longer windows are sensitivity analyses.

**Outcome.** Incident dementia will be defined with the validated SIDIAP case definition (diagnostic codes for dementia, positive predictive value 91%; Ponjoan et al., 2019a), complemented with dementia diagnoses from hospital discharge records linked to SIDIAP, so that cases recorded only in hospital are not missed; the date of the first record will be the event date. A sensitivity analysis will add dispensing of anti-dementia drugs, following the algorithms validated against ReDeGi (Ponjoan et al., 2019b). Because recording may be less complete in some settings, we will estimate the sensitivity of the SIDIAP definition by setting and deprivation in the Girona Health Region, using ReDeGi as the reference, and use it in a quantitative bias analysis. Alzheimer's disease, vascular dementia and unspecified dementia will be analyzed separately as exploratory analyses, because unspecified codes are common in primary care.

**Covariates.** We will select confounders with a directed acyclic graph. The main model will adjust for age (as the time scale), sex, calendar year, country of birth where available, smoking status, census-section deprivation (the 2011 deprivation index of the Spanish Society of Epidemiology, which covers rural areas; Duque et al., 2021), annual census-section household income from 2015 (INE, n.d.), population density, municipality size class, individual income (the pharmacy co-payment level recorded in SIDIAP) and the share of residents with low education in the census section, because individual education is not recorded. Physical activity, body mass index, hypertension, diabetes, cardiovascular disease and depression lie on the pathways described in Section 2.1, so they will not be adjusted for in the main model; adding them in an exploratory analysis will show how much of the association they explain. Air pollution and road-traffic noise lie on the pathway from roads and sealed surfaces but can confound green features; a sensitivity model will add annual census-section NO2 and PM2.5, which have already been linked to SIDIAP (de Bont et al., 2021), and noise where available.

**Statistical analysis.** The analysis has two stages. <u>First, single-feature models:</u> each feature will be tested on its own, as most studies do, with Cox proportional hazards models with age as the time scale, time-varying exposures and robust standard errors clustered by census section. Death will be treated as a competing event: the main estimand is the cause-specific hazard, and Fine–Gray models will give the cumulative incidence of dementia as a secondary result. These models allow comparison with the existing literature and provide a baseline for interpreting the mixture models. <u>Second, mixture models:</u> we will estimate the joint association of all features with quantile g-computation for survival outcomes (Keil et al., 2020). Harm features (major roads, sealed surfaces, industrial yards, neglect) are reversed, so that a higher value always points to the environment expected to be healthier, and the joint association compares sections at the 25th and 75th percentiles of all features. Feature weights show how much each one contributes.

**Effect modification.** We will test effect modification by sex, age group (65–79 and 80 and over), deprivation tertile and setting, with interaction terms and stratified models, and we will report differences on the additive scale as well. We will control the false discovery rate with the Benjamini–Hochberg procedure separately for the main single-feature results and for the exploratory effect-modification tests.

**Types.** In a separate analysis, we will relate the share of each type in the census section to dementia incidence with Cox models, using the most common type as the reference, with the same false discovery rate control. Types do not enter the mixture, because types and features describe the same images.

**Sensitivity analyses and missing data.** We will **(i)** exclude the first two years of follow-up, because prodromal dementia can prompt moves and earlier contact with services; **(ii)** restrict to people who did not move, and separately ignore moves in the three years before diagnosis; **(iii)** use five-year lagged and cumulative exposure windows, from 2017, and the exposure at entry; **(iv)** exclude 2020–2021, when diagnoses dropped during the COVID-19 pandemic; **(v)** estimate E-values, which show how strong an unmeasured confounder would need to be to explain an association away; **(vi)** use negative-control outcomes with empirical calibration (Schuemie et al., 2014); **(vii)** adjust for each person's number of primary care visits in the three years before entry, because features such as sidewalks also mark easier access to care, which can lead to earlier diagnosis; **(viii)** use whole-section prevalence; **(ix)** correct prevalence for the setting-specific accuracy of the models; and **(x)** add municipality fixed effects, so that contrasts come from within the same municipality. Missing covariates will be handled with multiple imputation by chained equations.

**Power.** With an incidence of 8.6 per 1,000 person-years (Ponjoan et al., 2019a), about one million people aged 65 and over at entry and about 70,000 more reaching 65 each year, we expect roughly 100,000 incident cases from 2013; we base power conservatively on 60,000. Because exposure varies only between census sections, people in the same section are not independent. With about 5,000 census sections (about 215 people aged 65 and over in each) and an assumed intraclass correlation of 0.005, within the range expected for binary outcomes of this frequency (Gulliford et al., 2005), the design effect is about 2. A Cox model would then have 80% power (two-sided α = 0.05) to detect a hazard ratio of about 1.02 per interquartile range of a continuous exposure (Schoenfeld approximation), a 2% difference in risk, smaller than the 3% lower risk per interquartile range of green space reported in UK Biobank (Hu et al., 2023) (1.03 and 1.05 with intraclass correlations of 0.01 and 0.05); correlation between features and covariates will raise these values. We will therefore confirm the number of events with SIDIAP and estimate power by simulation once the maps exist (Month 24), using the observed feature correlations, the validation error and these intraclass correlations; the statistical analysis plan and simulations will be preregistered in an open repository (Month 30).

| **Critical stage (Months 1–12 and 12–24).** Access to SIDIAP (Months 1–12) sets when Aim 2a starts, and the geography it releases (Months 12–24) sets the spatial level; a coarser geography lowers precision but keeps the aim feasible (Section 3.4). |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### 3.2.4. Aim 2b: Features and severity at diagnosis

Using the Aim 1 maps and about 5,000 ReDeGi cases linked to SIDIAP, Aim 2b tests whether the places people lived before diagnosis are associated with how severe dementia is at first specialist diagnosis (H2b). Severity at diagnosis reflects both how advanced the disease is and how timely the diagnosis was; Aim 2b explores, under stated assumptions, how much each contributes.

| **Data source: ReDeGi.** ReDeGi is a population-based clinical registry of incident dementia diagnosed in the public hospitals of the Girona Health Region since 2007, run by the Institut d'Assistència Sanitària (Garre-Olmo et al., 2009). It records about 700 new cases a year with standardized assessments at diagnosis, including the MMSE for over 95% of cases (Garre-Olmo et al., 2016). It has already been linked to SIDIAP with encoded health identifiers, without access to identifying data, in a study of 4,996 patients (Ponjoan et al., 2019b). Access is through a data use agreement with the Institut d'Assistència Sanitària. I have contacted the SIDIAP and ReDeGi teams to confirm access conditions. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Population.** We will include ReDeGi cases diagnosed from 2013 who can be linked to SIDIAP, which gives the subcohort the same exposure and covariate information as Aim 2a. Because about 500 cases a year were linked in a previous study (Ponjoan et al., 2019b), we expect about 5,000 linked cases. Because only people assigned to the Catalan Institute of Health are in SIDIAP, we will compare linked and unlinked cases on registry variables and use inverse probability weights for linkage. The Girona Health Region spans the whole continuum, from the city of Girona to coastal towns and Pyrenean villages, and results will apply to this region.

**Exposure.** The main exposure will be the mean residential prevalence of each feature over the five years before diagnosis, or over the available years since 2012.

**Outcomes.** The two main outcomes will be the MMSE score at diagnosis (0–30; lower = more severe), corrected for age and education with Spanish norms, and the Clinical Dementia Rating (CDR; global staging), which depends less on education. The duration of symptoms before diagnosis, reported by the informant, will be a secondary outcome and the mediator in the delay-adjusted model.

**Statistical analysis.** The two stages follow Aim 2a. <u>Single-feature associations</u> will be estimated with regression models suited to each outcome (linear or bounded models for the MMSE, ordinal models for the CDR), adjusted for the Aim 2a covariates plus education and dementia subtype, which ReDeGi records; diagnosing hospital is added as a fixed effect in a sensitivity model, because it partly reflects access. Effect modification by sex and setting will be tested as in Aim 2a. The main estimate is the total association. Adding symptom duration, which lies on the path through later diagnosis, gives a controlled direct effect: the association not explained by diagnostic delay, under the assumption of no unmeasured confounding of delay and severity, which we will probe with E-values and, where recorded, with the time from the first cognitive complaint in primary care to diagnosis. Because only diagnosed and referred people enter the registry, we will weight cases by their probability of appearing in ReDeGi, estimated from SIDIAP incident cases in the Girona Health Region; these weights correct referral among diagnosed cases, not undiagnosed dementia. The <u>joint association</u> of all features will be estimated with BKMR (Bobb et al., 2015), which allows for non-linear and interacting effects and gives the probability that each feature contributes, using knot-based approximation, a random intercept by census section and features grouped by pathway; quantile g-computation, as in Aim 2a, will be fitted for comparison. We do not use BKMR in Aim 2a because it does not work with large datasets.

**Types.** Types will be analyzed as in Aim 2a, with the MMSE and CDR as outcomes.

**Sensitivity analyses and missing data.** We will **(i)** use the Blessed Dementia Rating Scale (BDRS), which measures limitations in daily activities, as an alternative outcome; **(ii)** use the uncorrected MMSE; **(iii)** stratify by dementia subtype, because the MMSE captures frontotemporal and Lewy body dementia poorly; **(iv)** restrict to diagnoses from 2017, which have full five-year exposure windows; **(v)** use a one-year exposure window; and **(vi)** restrict to people who did not move in the five years before diagnosis. Missing covariates will be handled with multiple imputation by chained equations.

**Power.** With about 5,000 linked cases and an MMSE standard deviation of 5.4 at diagnosis in ReDeGi (Garre-Olmo et al., 2016), a linear model has 80% power (two-sided α = 0.05) to detect a difference of about 0.3 MMSE points per interquartile range of a feature, a small shift in the population mean rather than a change for any one person; we will also report the change in the share of people diagnosed at the moderate or severe stage (MMSE below 20). Power for BKMR has no closed form, so it will be assessed by simulation with the observed exposure distributions.

| **Critical stage (Months 12–24).** The number of linked ReDeGi–SIDIAP cases sets the precision of Aim 2b (Section 3.4). |
|-------------------------------------------------------------------------------------------------------------------------|

## 3.3. Work plan and schedule

### 3.3.1. Schedule, milestones and deliverables

The project runs over five years (Figure 5). Aim 1 takes Years 1 and 2, because the maps are needed before any health analysis; data access is requested in Month 1 and cohort preparation starts in Year 1, so that Aim 2a runs in Years 3 and 4 and Aim 2b in Years 4 and 5, each with a six-month buffer. All deliverables are reached by Month 54, and the last milestone, M5, at Month 60. The European Research Council (ERC) Starting Grant application runs from the start of Year 2 to the end of the project, and the last semester is also kept for dissemination.

<img src="media/image5.png" style="width:6.29921in;height:3.64724in" alt="Mapa El contenido generado por IA puede ser incorrecto." />

**Figure 5. Work plan by semester (S1–S10).** Bars show tasks, colored by lead, with pale segments for buffers; ticks mark deliverables (D1–D11), dots the user panel meetings and diamonds the milestones (M1–M5). PI, principal investigator; TFG and TFM, bachelor's and master's final projects; ERC, European Research Council.

**Milestones.** <u>M1 (Month 12):</u> both predoctoral researchers hired, data access agreements and ethics approval, and final feature set after piloting. M2 (Month 24): types and validated feature models, with test-set results by setting (H1b), and annual maps released. <u>M3 (Month 36):</u> SIDIAP cohort and ReDeGi–SIDIAP subcohort built, and first Aim 2a results. <u>M4 (Month 48):</u> Aim 2a results submitted. <u>M5 (Month 60):</u> Aim 2b results submitted and both doctoral theses completed. The interim report at Month 37 will present M1 to M3.

**Deliverables (lead).** D1 data management plan (Month 6; PI); D2 open maps, labels, models and code (Month 24; predoctoral researcher 1, PR1); D3 plain-language guide (Month 24; PI); D4 Aim 1a paper (Month 30; PR1); D5 preregistered Aim 2 analysis plan (Month 30; predoctoral researcher 2, PR2); D6 Aim 1b paper (Month 36; PR1); D7 containerized update pipeline for the ICGC (Month 36; PR1); D8 Aim 2a paper (Month 48; PR2); D9 Aim 2b paper (Month 54; PR2); D10 types and dementia paper (Month 54; PI); D11 policy brief (Month 54; PI).

### 3.3.2. Research team

- **Principal investigator.** I will lead the project: I will define the feature set and labeling protocol, lead the data access requests, ethics approvals and data management plan, supervise model development, as well as the Aim 2 analyses. I will lead the paper on types and dementia outcomes, and direct two doctoral theses. I will also supervise the bachelor's and master's students, run the user panel, write the plain-language guide and policy brief, lead outreach and prepare the ERC Starting Grant application.

- **Predoctoral researcher 1 (Aim 1).** Starts around Month 6, ideally with a master's degree in geography, remote sensing, computer science or data science and programming experience in Python. They will run the imagery pipeline, labeling tool, typology, models, annual maps and open release. The thesis will cover the typology, the feature models and their validation, the open maps and the distribution of features by deprivation and setting.

- **Predoctoral researcher 2 (Aim 2).** Starts around Month 6, with a master's degree in epidemiology, public health or biostatistics and programming experience in R. While the maps are built, they will prepare the SIDIAP cohort and the ReDeGi–SIDIAP subcohort; they will then run the Aim 2a and 2b analyses.

- **Bachelor's and master's students (TFG and TFM).** Students will label sub-tiles as supervised final projects and explore extensions outside the core aims that will provide preliminary results for an ERC Starting Grant application.

- **Collaborators and thesis co-directors.** Collaborators from the host institution and from my previous work can co-direct the theses and advise on each part: Payam Dadvand and Mark Nieuwenhuijsen (Barcelona Institute for Global Health, ISGlobal), the urban environment and health in Catalonia; Roser Maneja (Forest Science and Technology Centre of Catalonia, CTFC), management and human–nature interfaces; Maayan Yitshak-Sade, environmental epidemiology, and Itai Kloog, geospatial exposure modeling (Icahn School of Medicine at Mount Sinai); Vishal Midya and Elena Colicino, biostatisticians who specialize in mixture methods (Mount Sinai); and Kees de Hoogh and Roel Vermeulen (EXPANSE, International Human Exposome Network), the urban exposome and co-exposure data. For Aim 2, I have contacted the SIDIAP and ReDeGi teams about data access; they will advise on case definitions and record linkage.

**Hiring.** Positions will be advertised internationally in Month 1 through the host institution, with selection by a panel that follows its gender equality plan. Until the predoctoral researchers start, I will set up the labeling tool and the data access requests with students.

### 3.4. Identification of critical points and contingency plan

The critical stages are access to the health data (Months 1–12), the geography and number of linked cases released by SIDIAP and ReDeGi (Months 12–24) and the validation of the feature models (H1b, Month 24); Table 2 lists the main risks and responses. Aim 1 does not depend on access to health data, so delays in Aim 2 do not stop the project.

Although it is unlikely, access to SIDIAP or ReDeGi could fail altogether. Aim 2 would then use other population-based health data linked to place of residence: in Catalonia, the Public Data Analysis Program for Health Research and Innovation (PADRIS), which covers the whole public health system; in Spain, the primary care database for pharmacoepidemiological research (BIFAP; Maciá-Martínez et al., 2020), with orthophotos from the PNOA. As a last resort, I have access to the electronic health records of the Mount Sinai Health System, the World Trade Center cohort and Medicare data in the United States, where aerial imagery is also available.

**Table 2.** Critical points and contingency plans

| **Risk**                                                      | **Likelihood** | **Impact on aims and tasks**       | **Contingency**                                                                                                                                     |
|---------------------------------------------------------------|----------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Delays in access to SIDIAP or ReDeGi data                     | Medium         | Medium; Aim 2 timing               | Requests in Month 1; Aim 1 proceeds independently; code tested on synthetic data; six-month buffers for Aims 2a and 2b (Figure 5).                  |
| SIDIAP releases a geography coarser than census sections      | Medium         | Medium; Aim 2a precision           | Aggregate maps to the finest geography released and report the expected attenuation; all aims remain feasible.                                      |
| Some features cannot be labeled reliably or detected at 25 cm | Medium         | Low; Aim 1b feature set            | Merge or drop features below κ = 0.60; Aim 2 proceeds with the features that pass, and types remain as an exposure.                                 |
| Accuracy differs between settings (H1b not supported)         | Medium         | Medium; H1b, Aim 2 exposures       | Active learning targets weak settings; features that fail in any setting are excluded from Aim 2, so comparisons along the continuum stay unbiased. |
| Later or less complete diagnosis in rural areas               | Medium         | Medium; Aim 2 estimates by setting | Effect modification by setting; adjustment for municipality size and primary care visits; in Aim 2b, diagnosing hospital and symptom duration.      |
| Aim 1 takes longer than two years                             | Low            | Medium; Aim 2a timing              | Cohort preparation proceeds in parallel; Aim 2a starts with the features and years already validated.                                               |
| Differences between flights across years                      | Medium         | Medium; Aim 1 annual maps          | Augmentation and per-year color normalization; flip rates in sub-tiles whose type does not change between years.                                    |
| Residual confounding by socioeconomic position                | Medium         | Medium; Aim 2 estimates            | Area and individual deprivation adjustment; negative-control outcomes with empirical calibration; E-values.                                         |
| Small linked subcohort for Aim 2b                             | Low            | Medium; Aim 2b precision           | Add unlinked registry cases if ReDeGi records residence; prioritize single-feature models and report mixture results with their uncertainty.        |

## 3.5. Previous results related to the topic of the research proposal which supports its feasibility

I have built similar pipelines and analyses in other settings, during my PhD in Barcelona and postdoc at the Icahn School of Medicine at Mount Sinai. Each block below names the study or grant and what it contributes to CONTINUUM.

**Candidate.** Since July 2026, I have been Instructor (faculty) at the Icahn School of Medicine at Mount Sinai, where I lead my own research line on urban nature, the exposome and aging, with 25 peer-reviewed papers (11 as first author and 3 as senior author). I am PI of two pilot projects funded by the US National Institute of Environmental Health Sciences (NIEHS) and of a pending US National Institute on Aging (NIA) R01 and a pending NIEHS R21 based on them, co-investigator on an NIA pilot and an NIEHS pilot, and co-investigator, as built environment expert, on three R01 applications under review. I have co-supervised 13 bachelor's and master's theses and chair the Mentoring Committee of the North America Chapter of the International Society for Environmental Epidemiology (ISEE).

**Green space quality and health (PhD, Barcelona; Aim 1).** I reviewed existing multidimensional tools for assessing green space quality (Knobel et al., 2019), developed RECITAL, which assesses 90 quality items in 11 dimensions and was applied to 149 green spaces in Barcelona with good to excellent reliability (Knobel et al., 2021a), and showed that, among 2,053 adults in Barcelona, higher green space quality was associated with more use of green spaces, higher odds of moderate-to-vigorous physical activity (OR = 1.13; 95% CI: 1.00, 1.27) and lower odds of overweight or obesity (OR = 0.88; 95% CI: 0.79, 0.98) (Knobel et al., 2021b). This work shows that I can turn an audit concept into reliable items, the basis of the Aim 1b feature set.

**Mixtures in health records (NIEHS pilot, PI; first author; Aim 2).** As PI of an NIEHS-funded pilot, I used quantile g-computation in health records and found that a decile increase across four social vulnerability dimensions was associated with 0.23 years of biological age acceleration (Knobel et al., 2025b). Additionally, as co-first author, I estimated the joint association of PM2.5 components with cardiovascular mortality in about 66 million Medicare beneficiaries (Ma et al., 2025). These studies used the mixture methods proposed for Aim 2 in large health records.

**Green space quality across the United States (NIA Pilot, co-investigator; Aim 1).** In this pilot project for the Gateway Exposome Coordinating Center, I coordinated the definition of audit-based items, the labeling of about 8,000 aerial image tiles by trained students, the training of convolutional neural networks and their prediction of 10 quality items across the continental United States. On a held-out test set, the models reached a macro F1 of 0.81 and a macro PR-AUC of 0.88, lowest for the rarest items, such as playgrounds (0.59) (Knobel et al., 2026a). This is the pipeline that Aim 1 adapts to Catalonia.

**Bird diversity and frailty (NIEHS P30, PI; Aims 1 and 2a).** I built annual census-tract maps of bird diversity from citizen-science data and found that, among 20,388 adults aged 65 and over in health records, each interquartile-range increase was associated with 1.4% fewer frailty deficits (95% CI: 0.8%, 2.1%) (Knobel et al., 2026b). This shows that annual small-area maps can be linked to aging outcomes in health records.

**Urban nature profiles and cardiovascular disease (Aim 2).** Among 36,830 New York City residents aged 55 and over, I classified surrounding urban nature into five profiles from eight high-resolution indicators and found lower risk of atherosclerotic cardiovascular disease for the waterfront (HR = 0.88; 95% CI: 0.81, 0.95), park access (HR = 0.89; 95% CI: 0.84, 0.94) and street tree (HR = 0.92; 95% CI: 0.87, 0.98) profiles than for the low-nature profile (Knobel et al., 2025a). This shows that several co-occurring features can be analyzed together in health records.

**Dementia (Aim 2).** I was senior author of a systematic review and meta-analysis of noise exposure and dementia risk (Hwang et al., 2025) and first author of a review of the molecular mechanisms that link biological age and environmental risk factors to dementia and stroke (Knobel et al., 2022). This work grounds Aim 2 in the dementia literature.

**Pilot for this proposal (Aim 1).** In Girona, I downloaded and processed ICGC orthophotos for 87 census sections (about 42,000 tiles in 2025) through the ICGC web map service, which shows that the imagery can be accessed and processed. The two-stage typology described in Aim 1a, applied to these images alone, produced five contexts and 27 types, from dense blocks to farmland and forest (Figures 2 and 6). Contexts were highly stable across bootstrap samples (adjusted Rand index 0.99), and types within them were stable too (0.90). Processing one year of the pilot area took about 10 minutes on a consumer graphics card.

<img src="media/image6.png" style="width:5.11811in;height:2.51469in" />

**Figure 6. Pilot typology in Girona (2025).** Types on 64 m tiles over the pilot area, with census-section boundaries. Types are grouped by the context of the first clustering stage (color family) and numbered within it; codes are labels, not names. Described afterwards with the cadastre, context 1 holds nearly all dwellings, context 3 the scattered housing at the urban edge, and contexts 2, 4 and 5 farmland and forest. Images: ICGC, CC BY 4.0.

## 3.6. Description of the material resources, infrastructure and/or unique equipment required to implement the proposed methodology

- **Imagery and computing.** The orthophotos and census-section boundaries are public (Institut Cartogràfic i Geològic de Catalunya, n.d.; INE, 2024). Raw imagery for all years is estimated at 20–30 TB; we will store compressed tiles and process the series year by year. Model training and annual inference need graphics processing unit (GPU) computing. Based on the pilot's processing speed, the full series (about 7.8 million tiles per year, 2012–2025) can be processed in weeks on the single GPU workstation included in the budget (Section 5).

- **Software.** Open-source Python (PyTorch) for Aim 1 and R (survival, qgcomp and bkmr packages) for Aim 2; no licenses are needed.

- **Secure computing for health data.** Health data from SIDIAP and ReDeGi will be analyzed only inside the secure environments required by the data providers. No individual-level health data will be stored on personal devices, the maps are linked to health records by census section inside these environments, and only aggregated results will leave them.

The host, a Spanish public research institution, will provide office space, IT support, secure network access and a doctoral program.

# 4. EXPECTED IMPACT OF THE RESULTS

## 4.1. Expected impact on the generation of scientific and technological knowledge

CONTINUUM will have five main scientific impacts:

- **A new exposure layer.** An open, annual map of the types and features of every place in Catalonia since 2012, ready for any health or planning question and to be combined with the ambient and social layers of the urban exposome; its use will be tracked through downloads, citations and reuse.

- **A method any region can adopt.** The PNOA covers all of Spain with orthophotos at 25 cm (15 cm in some regions), renewed every one to three years, population-based health databases such as BIFAP cover other regions, and most European countries run similar national orthophoto programs, harmonized under the EU INSPIRE Directive. Predoctoral researcher 1 will test the trained models on PNOA imagery of a second Spanish region and report the loss in accuracy, so other groups can reuse a tested workflow rather than a one-off result.

- **Evidence on which features matter for dementia.** Single-feature and mixture estimates for over one million older adults (Aim 2a), showing which features matter most when all are modeled together. This evidence feeds international efforts on modifiable risk factors for dementia (Livingston et al., 2024).

- **A first look at the environment and dementia severity.** New estimates for an outcome that environmental studies have rarely examined (Aim 2b), relevant to care planning and the burden on families.

- **A building block of the urban exposome.** The maps form the built and natural layer of the urban exposome (Nieuwenhuijsen et al., 2019), ready to be combined with its ambient and social domains, and they connect exposure science, remote sensing, epidemiology and urban planning.

**Indicators.** Five open-access papers (Months 30–54); dataset with a persistent identifier and at least one external reuse by Month 54; at least one public agency integrating the maps by Month 54; the transfer test to a second Spanish region; and at least one conference presentation a year from Year 2.

**Beyond CONTINUUM.** CONTINUUM will become one component of an ERC Starting Grant application, prepared from the start of Year 2, that will add image segmentation to measure features as areas, address-level health data and tracking of where older adults spend their time, moving from the place where people live to the places they actually use.

## 4.2. Social and economic impact of the expected results

Main social and economic impacts:

- **Evidence for better places to age in.** Spain has made dementia a health priority (Ministerio de Sanidad, Servicios Sociales e Igualdad, 2016; Ministerio de Sanidad, Consumo y Bienestar Social, 2019), and the Spanish Urban Agenda guides how towns and cities are planned (Ministerio de Fomento, 2019); CONTINUUM connects the two. By identifying which features are associated with dementia, it can identify candidate elements for planners to consider, and to test in intervention studies, when they regenerate streets, squares and parks, for example through the municipal urban plan (Pla d'Ordenació Urbanística Municipal, POUM), which sets where public spaces and green areas go, or municipal street-tree plans. Results will be translated into planning quantities, such as the length of tree-lined street that an interquartile range represents in a census section of median size, and into absolute risks per 1,000 older adults, always as associations.

- **Data for every municipality, however small.** The maps cover every town and village, so small municipalities without their own environmental data can see where features are scarce and compare their census sections with the rest of Catalonia, at no cost.

- **Savings for families and the health system.** Dementia care costs rise with severity (Gómez Maldonado et al., 2024); if the associations reflect causal effects, even small reductions in incidence or in severity at diagnosis would carry large savings. If Aim 2b finds areas where diagnosis comes late, the results will be shared with the Catalan Health Service (CatSalut) and the memory clinics of the Girona Health Region to target timely diagnosis.

- **Fairer prevention.** The plain-language guide will follow web accessibility standards and have an easy-read version reviewed with associations of people with dementia. Because the maps describe features by deprivation and setting, they include the rural and deprived areas that environmental data often leave out; the policy brief will present feature gaps alongside deprivation and flag the risk that upgrades displace older, low-income residents.

## 4.3. Plan for scientific communication and internationalization of the results

**Papers.** Results will be published in five open-access, peer-reviewed papers in international journals: **(1)** Aim 1a, the typology and its maps; **(2)** Aim 1b, the feature models and their maps; **(3)** Aim 2a, single-feature and mixture results for dementia incidence; **(4)** Aim 2b, single-feature and mixture results for severity at diagnosis; and **(5)** the types from Aim 1a and both dementia outcomes. Target journals include Environmental Health Perspectives, Environment International, Health & Place, Urban Forestry & Urban Greening, Alzheimer's & Dementia and Remote Sensing of Environment. Preprints will be posted at submission, and accepted manuscripts and their data will be deposited in an open repository on publication.

**Conferences.** The team will present results at international conferences, such as those of ISEE and the Alzheimer's Association International Conference, and at the annual meeting of the Spanish Society of Epidemiology, and will propose a symposium on aerial imagery for exposure assessment at the ISEE conference.

**Internationalization.** Internationalization builds on my collaborations at the Icahn School of Medicine at Mount Sinai and on my role in the International Human Exposome Network as an exposome ambassador. Each predoctoral researcher will complete a three-month stay abroad, the first to apply the CONTINUUM models to a second setting and the second to apply the Aim 2 methods in another health records cohort.

## 4.4. Plan for the dissemination of results to the groups most relevant to the topic of the research proposal and to society in general

The open maps, labeled images, trained models and code will be released through a public repository with a persistent identifier, together with a plain-language guide for non-specialists (Month 24). A policy brief for the Agència de Salut Pública de Catalunya and the Departament de Territori will show where features are scarce, by deprivation and setting, and which features are candidates for evaluation in intervention studies, expressing results in units that planners use (Month 54). Results will also be shared with associations of people with dementia and their families, such as the Confederación Española de Alzheimer y otras Demencias (CEAFA), in two sessions after the Aim 2 results (Months 48–60), and through the host institution's press office and science outreach events. Every paper will be accompanied by a plain-language summary in Catalan, Spanish and English. A user panel, with the Agència de Salut Pública de Catalunya, the Departament de Territori, the ICGC, planners from one large and one small municipality and CEAFA, will meet three times: to review the feature list (Month 6), to test the maps and the guide (Month 24), and to interpret the Aim 2 results before the policy brief (Month 48).

## 4.5. Brief description of the research data management plan

Aim 1 data will follow the FAIR principles (findable, accessible, interoperable and reusable): annual maps (GeoTIFF and CSV), labeled tiles, trained models and code will be deposited in a public repository, such as Zenodo, with a persistent identifier, metadata and a data dictionary, under licenses compatible with the ICGC license (CC BY 4.0). Health data from SIDIAP and ReDeGi will remain in the environments set by the data providers, and only aggregated, non-identifiable results will leave them. Analyses will follow the STROBE and RECORD reporting guidelines for observational studies and routinely collected health data. I will write the full data management plan in the first semester and deposit it in an open repository.

## 4.6. Description of the effects of the inclusion of gender in the research content

Dementia is more common among women, who also live longer with it and provide most informal care (Ministerio de Sanidad, 2025). Women and men may also use and experience their neighborhoods differently, for example in time spent near home or in perceived safety. Sex therefore enters every stage of Aim 2: the hypotheses include whether associations differ by sex, without a pre-specified direction; all analyses will be stratified by sex and test effect modification by sex; and results will be reported for women and men separately, so that differences are not hidden in pooled estimates. Aim 1 describes places, not people. SIDIAP records sex but not gender, so we will interpret sex differences as reflecting both biology and gendered patterns of daily life, and state this limitation explicitly.

Results will be reported following the Sex and Gender Equity in Research (SAGER) guidelines (Heidari et al., 2016), and student labelers will be recruited with a gender balance.

## 4.7. Plan for the transfer and valorization of results (where applicable)

CONTINUUM does not aim at patents: its main transferable products are the open maps, models and code, designed to be reused by public agencies. We will offer the annual maps to the ICGC and to the Agència de Salut Pública de Catalunya for integration into their open data portals and urban health indicators. To keep the maps alive after the project, we will meet the ICGC at Month 24 to agree who runs the annual update, hand over a documented, containerized pipeline at Month 36 (D7), and run the updates ourselves until the end of the project if no agency has adopted them.

# 5. JUSTIFICATION OF THE REQUESTED BUDGET

The project budget requests €332,000 in direct costs, above the minimum of €200,000.

| **Concept**                            | **Justification**                                                    | **Amount (€)** |
|----------------------------------------|----------------------------------------------------------------------|----------------|
| Predoctoral researcher 1 (Months 6–54) | Aim 1; doctoral thesis; four-year contract                           | 124,000        |
| Predoctoral researcher 2 (Months 6–54) | Aim 2; doctoral thesis; four-year contract                           | 124,000        |
| GPU workstation and storage            | Model training and annual inference; storage for 20–30 TB of imagery | 20,000         |
| Health data access                     | SIDIAP and ReDeGi extraction and linkage                             | 20,000         |
| Open-access publication                | Five papers                                                          | 15,000         |
| Travel and stays                       | Conferences; a three-month stay for each predoctoral researcher      | 26,000         |
| Repository and dissemination           | Data deposit, backup and plain-language materials                    | 3,000          |
| **Total direct costs**                 |                                                                      | **332,000**    |

- **Personnel.** Two predoctoral researchers, each on a four-year contract with salary and employer social security (Months 6–54), are essential to carry out the project, and each completes a doctoral thesis within it.

- **Equipment.** A GPU workstation (one 48 GB professional graphics card, a 32-core processor, 256 GB of RAM, 4 TB of solid-state storage and about 40 TB of redundant disk storage for 20–30 TB of imagery, with an external backup) is needed for model training and annual inference for 2012–2025; it is cheaper than buying computing time for the full series and remains with the host after the project.

- **Health data access.** Fees set by SIDIAP for data extraction and the secure analysis environment, including the linkage to hospital records, and by ReDeGi for the ReDeGi–SIDIAP linkage.

- **Travel and stays.** Attendance at international conferences for the PI and both predoctoral researchers, to communicate results, and a three-month stay abroad for each predoctoral researcher (Section 4.3).

- **Publication and dissemination.** Open-access fees for five papers, and the costs of data deposit, backup and plain-language materials (Sections 4.3 to 4.5).

# 6. SPECIFIC CONDITIONS FOR THE EXECUTION OF CERTAIN RESEARCH PROPOSALS

CONTINUUM uses secondary health data, with no new data collection from participants, biological samples or animals; in the application, it answers Yes to A (research in humans) and D (use of personal data). It complies with the General Data Protection Regulation (GDPR) and Organic Law 3/2018 on the Protection of Personal Data (LOPDGDD); the legal basis for reusing pseudonymized health data without consent is Article 9.2(j) of the GDPR and the seventeenth additional provision of the LOPDGDD, with approval by the research ethics committee. The research team will not receive names, addresses or identification numbers: the data providers assign each person to a census section and link ReDeGi and SIDIAP with encoded identifiers (Ponjoan et al., 2019b). Analyses will run in the environments required by the data providers, results will be reported only in aggregate, and cells with fewer than five individuals will be suppressed. Features in private spaces (inner-block courtyards, vegetable plots) and neglect will be released openly only as census-section summaries. The orthophotos are public data at 25 cm, at which people cannot be identified.

**Authorizations and facilities.** **(i)** SIDIAP scientific committee and IDIAPJGol research ethics committee; **(ii)** ReDeGi data use agreement with the Institut d'Assistència Sanitària and approval by the corresponding research ethics committee; **(iii)** review by the host institution's data protection officer. None is held yet; **(i)** and **(ii)** will be requested in Month 1.

**REFERENCES**

Besser, L. M., McDonald, N. C., Song, Y., et al. (2017). Neighborhood environment and cognition in older adults: A systematic review. American Journal of Preventive Medicine, 53(2), 241–251.

Bobb, J. F., Valeri, L., Claus Henn, B., et al. (2015). Bayesian kernel machine regression for estimating the health effects of multi-pollutant mixtures. Biostatistics, 16(3), 493–508.

Cerin, E., Soloveva, M. V., Molina, M. A., et al. (2024). Neighbourhood environments and cognitive health in the longitudinal Personality and Total Health (PATH) through life study: A 12-year follow-up of older Australians. Environment International, 191, 108984.

Chen, R., Xue, Z., Fu, K., et al. (2026). Deep learning on satellite imagery reveals landscape drivers of metabolic syndrome. Environmental Health Perspectives, 134(7), 878–891.

Chen, X., Lee, C., & Huang, H. (2022). Neighborhood built environment associated with cognition and dementia risk among older adults: A systematic literature review. Social Science & Medicine, 292, 114560.

Chen, Z., Dazard, J.-E., Khalifa, Y., et al. (2024). Deep learning–based assessment of built environment from satellite images and cardiometabolic disease prevalence. JAMA Cardiology, 9(6), 556–564.

Chi, D., Manoli, G., Lin, B., et al. (2025). Residential tree canopy configuration and mortality in 6 million Swiss adults: A longitudinal study. The Lancet Planetary Health, 9(3), e186–e195.

de Bont, J., Díaz, Y., de Castro, M., et al. (2021). Ambient air pollution and the development of overweight and obesity in children: A large longitudinal study. International Journal of Obesity, 45(5), 1124–1132.

de Keijzer, C., Bauwelinck, M., & Dadvand, P. (2020). Long-term exposure to residential greenspace and healthy ageing: A systematic review. Current Environmental Health Reports, 7(1), 65–88.

de Keijzer, C., Tonne, C., Basagaña, X., et al. (2018). Residential surrounding greenness and cognitive decline: A 10-year follow-up of the Whitehall II cohort. Environmental Health Perspectives.

Duque, I., Domínguez-Berjón, M. F., Cebrecos, A., et al. (2021). Índice de privación en España por sección censal en 2011. Gaceta Sanitaria, 35(2), 113–122.

Edwards, N., Hooper, P., Trapp, G. S. A., et al. (2013). Development of a Public Open Space Desktop Auditing Tool (POSDAT): A remote sensing approach. Applied Geography, 38, 22–30.

Eurostat. (2021). Applying the degree of urbanisation: A methodological manual to define cities, towns and rural areas for international comparisons (2021 ed.). Publications Office of the European Union.

Garre-Olmo, J., et al. (2009). A clinical registry of dementia based on the principle of epidemiological surveillance. BMC Neurology, 9, 5.

Garre-Olmo, J., et al. (2016). Diagnosis of dementia in the specialist setting: A comparison between the Swedish Dementia Registry (SveDem) and the Registry of Dementias of Girona (ReDeGi). Journal of Alzheimer's Disease, 53(4), 1341–1351.

Gómez Maldonado, L., et al. (2024). Cost of patients with Alzheimer's disease in Spain according to disease severity. PharmacoEconomics – Open, 8(1), 103–114.

Gulliford, M. C., Adams, G., Ukoumunne, O. C., et al. (2005). Intraclass correlation coefficient and outcome prevalence are associated in clustered binary data. Journal of Clinical Epidemiology, 58(3), 246–251.

Heidari, S., Babor, T. F., De Castro, P., et al. (2016). Sex and Gender Equity in Research: Rationale for the SAGER guidelines and recommended use. Research Integrity and Peer Review, 1, 2.

Hu, H.-Y., Ma, Y.-H., Deng, Y.-T., et al. (2023). Residential greenness and risk of incident dementia: A prospective study of 375,342 participants. Environmental Research, 216(Pt 3), 114703.

Hwang, S. A., Singhvi, A., Patil, L., et al. (2025). Noise exposure and dementia risk: A systematic review and meta-analysis. Public Health Reviews, 46, 1607355.

Institut Cartogràfic i Geològic de Catalunya. (n.d.). Ortofoto territorial de Catalunya.

Institut d'Estadística de Catalunya. (2025). Population estimates, 1 January 2025. Idescat.

Instituto Geográfico Nacional. (n.d.). Plan Nacional de Ortofotografía Aérea (PNOA).

Instituto Nacional de Estadística. (2024). Cartografía digitalizada de secciones censales. INE.

Instituto Nacional de Estadística. (2026, June 17). Population projections 2026–2076 \[Press release\]. INE.

Instituto Nacional de Estadística. (n.d.). Atlas de distribución de renta de los hogares. INE.

Jimenez, M. P., et al. (2026). Streetview greenspace types and dementia risk in older adults: The Multi-Ethnic Study of Atherosclerosis. American Journal of Epidemiology.

Keil, A. P., Buckley, J. P., O'Brien, K. M., et al. (2020). A quantile-based g-computation approach to addressing the effects of exposure mixtures. Environmental Health Perspectives, 128(4), 047004.

Klompmaker, J. O., Hoek, G., Bloemsma, L. D., et al. (2020). Surrounding green, air pollution, traffic noise exposure and non-accidental and cause-specific mortality. Environment International, 134, 105341.

Knobel, P., Alaasam, V., Krasnov, H., et al. (2026b). Residential bird biodiversity and frailty deficit accumulation: A longitudinal cohort study in New York City \[Preprint\]. medRxiv. https://doi.org/10.64898/2026.08.18.26360707

Knobel, P., Colicino, E., Kloog, I., et al. (2025b). Social vulnerability and biological aging in New York City: An electronic health records-based study. Journal of Urban Health, 102, 1–10.

Knobel, P., Dadvand, P., & Maneja-Zaragoza, R. (2019). A systematic review of multi-dimensional quality assessment tools for urban green spaces. Health & Place, 59, 102198.

Knobel, P., Dadvand, P., Alonso, L., et al. (2021a). Development of the urban green space quality assessment tool (RECITAL). Urban Forestry & Urban Greening, 57, 126895.

Knobel, P., et al. (2026a). Mapping urban green space quality across the continental United States \[Preprint\].

Knobel, P., Litke, R., & Mobbs, C. V. (2022). Biological age and environmental risk factors for dementia and stroke: Molecular mechanisms. Frontiers in Aging Neuroscience, 14, 1042488.

Knobel, P., Maneja, R., Bartoll, X., et al. (2021b). Quality of urban green spaces influences residents' use of these spaces, physical activity, and overweight/obesity. Environmental Pollution, 271, 116393.

Knobel, P., Singhvi, A., Krasnov, H., et al. (2025a). Beyond greenness: Multidimensional urban nature profiles and atherosclerotic cardiovascular risk. Environment International, 185, 110033.

Livingston, G., Huntley, J., Liu, K. Y., Costafreda, S. G., Selbæk, G., Alladi, S., et al. (2024). Dementia prevention, intervention, and care: 2024 report of the Lancet standing Commission. The Lancet, 404(10452), 572–628.

Ma, T., Knobel, P., Hadley, M., et al. (2025). PM2.5 component mixtures and atherosclerotic cardiovascular disease mortality among Medicare beneficiaries. NEJM Evidence, 4(6), EVIDoa2400221.

Maciá-Martínez, M.-A., Gil, M., Huerta, C., et al. (2020). Base de Datos para la Investigación Farmacoepidemiológica en Atención Primaria (BIFAP): A data resource for pharmacoepidemiology in Spain. Pharmacoepidemiology and Drug Safety, 29(10), 1236–1245.

Maharana, A., & Nsoesie, E. O. (2018). Use of deep learning to examine the association of the built environment with prevalence of neighborhood adult obesity. JAMA Network Open, 1(4), e181535.

Markevych, I., Schoierer, J., Hartig, T., et al. (2017). Exploring pathways linking greenspace to health: Theoretical and methodological guidance. Environmental Research, 158, 301–317.

Meijer, E., Casanova, M., Kim, H., et al. (2022). Economic costs of dementia in 11 countries in Europe: Estimates from nationally representative cohorts of a panel study. The Lancet Regional Health – Europe, 20, 100445.

Metzler, A. B., Nathvani, R., Sharmanska, V., Bai, W., Muller, E., Moulds, S., et al. (2023). Phenotyping urban built and natural environments with high-resolution satellite images and unsupervised deep learning. Science of the Total Environment, 893, 164794.

Michael, Y. L., Senerat, A. M., Buxbaum, C., et al. (2024). Systematic review of longitudinal evidence and methodologies for research on neighborhood characteristics and brain health. Public Health Reviews, 45, 1606677.

Ministerio de Fomento. (2019). Agenda Urbana Española. Gobierno de España.

Ministerio de Sanidad, Consumo y Bienestar Social. (2019). Plan Integral de Alzheimer y otras Demencias (2019–2023). Gobierno de España.

Ministerio de Sanidad, Servicios Sociales e Igualdad. (2016). Estrategia en Enfermedades Neurodegenerativas del Sistema Nacional de Salud. Gobierno de España.

Ministerio de Sanidad. (2025). Encuesta de Salud de España 2023: Nota técnica.

Montes-Martinez, M., Welter, L. S., Boon, P., et al. (2026). The economic burden of dementia in Europe: COIN-Eu dementia. Journal of Alzheimer's Disease.

Nieuwenhuijsen, M. J., Agier, L., Basagaña, X., et al. (2019). Influence of the urban exposome on birth weight. Environmental Health Perspectives, 127(4), 047007.

Oquab, M., et al. (2023). DINOv2: Learning robust visual features without supervision \[Preprint\]. arXiv. https://arxiv.org/abs/2304.07193

Ponjoan, A., Garre-Olmo, J., Blanch, J., et al. (2019a). Epidemiology of dementia: Prevalence and incidence estimates using validated electronic health records from primary care. Clinical Epidemiology, 11, 217–228.

Ponjoan, A., Garre-Olmo, J., Blanch, J., et al. (2019b). How well can electronic health records from primary care identify Alzheimer's disease cases? Clinical Epidemiology, 11, 509–518.

Poulsen, A. H., Sørensen, M., Hvidtfeldt, U. A., et al. (2023). Concomitant exposure to air pollution, green space, and noise and risk of stroke: A cohort study from Denmark. The Lancet Regional Health – Europe, 31.

Recalde, M., Rodríguez, C., Burn, E., et al. (2022). Data resource profile: The Information System for Research in Primary Care (SIDIAP). International Journal of Epidemiology, 51(6), e324–e336.

Schuemie, M. J., Ryan, P. B., DuMouchel, W., et al. (2014). Interpreting observational studies: Why empirical calibration is needed to correct p-values. Statistics in Medicine, 33(2), 209–218.

Song, Y., Liu, Y., Bai, X., et al. (2024). Effects of neighborhood built environment on cognitive function in older adults: A systematic review. BMC Geriatrics, 24, 194.

Tani, Y., Hanazato, M., Fujiwara, T., et al. (2021). Neighborhood sidewalk environment and incidence of dementia in older Japanese adults. American Journal of Epidemiology, 190(7), 1270–1280.

Weichenthal, S., Hatzopoulou, M., & Brauer, M. (2019). A picture tells a thousand…exposures: Opportunities and challenges of deep learning image analyses in exposure science and environmental epidemiology. Environment International, 122, 3–10.

Wild, C. P. (2005). Complementing the genome with an "exposome": The outstanding challenge of environmental exposure measurement in molecular epidemiology. Cancer Epidemiology, Biomarkers & Prevention, 14(8), 1847–1850.

World Health Organization. (2025). Dementia \[Fact sheet\].

Yuchi, W., Sbihi, H., Davies, H., et al. (2020). Road proximity, air pollution, noise, green space and neurologic disease incidence: A population-based cohort study. Environmental Health, 19(1), 8.
