# Met Eireann Symposium Poster -- Content Plan

## Audience
Operational meteorologists and researchers at Met Eireann. They understand NWP, verification metrics, and Irish weather. They'll care about practical forecast skill at S2S timescales and its relevance to Irish hazards.

## Core message (one sentence)
S2S forecasts carry useful probabilistic skill for temperature over Ireland -- the first link in a chain towards predicting drought-to-flood events weeks to months ahead.

## Title
**Towards S2S Drought-to-Flood Prediction over Ireland**

Short, scannable, tells you the destination. The subtitle or Introduction makes clear this poster covers the verification step.

## Research questions
1. Do ECMWF extended-range forecasts carry probabilistic skill for temperature over Ireland at S2S lead times?
2. Which system (subseasonal or seasonal) is more suitable as a basis for downstream multi-hazard prediction?

These frame the poster. The verification results are *answers to these questions*, not the point in themselves.

## Variable focus
Temperature only (2m temperature). Strongest skill signal, cleanest story for a poster.

---

## Sections

### 1. Introduction (full width, top)
**Purpose:** Motivate *why* -- drought-to-flood events, the causal chain, and the gap.

**Content to include:**
- Ireland is exposed to both drought and Atlantic storm-driven flooding
- These can occur in sequence: drought modifies catchment state, worsening subsequent flood response
- Predicting these sequences at S2S lead times (2 weeks to 2 months) would support early action
- No study has assessed S2S forecast skill over Ireland
- **State the two research questions clearly**

**Figure:** `dft_causal_diagram.pdf` -- Bevacqua-style causal chain. This is the visual anchor of the poster. It shows the physical pathway from atmospheric drivers through drought to flood.

**Approximate length:** 3-4 sentences + research questions + the diagram

---

### 2. Data (left column, small)
**Purpose:** What goes in. Keep compact -- bullet points.

**Content to include:**
- Subseasonal: ECMWF EEFH, 11 members, weekly initialisation
- Seasonal: ECMWF SEAS5, 25 members, monthly initialisation
- Reference: ERA5-Land reanalysis (gridded)
- Period: reforecasts, weekly-mean aggregation
- Variable: 2m temperature
- Lead times: weeks 2-6

**Figure:** None

**Approximate length:** ~6 bullet points

---

### 3. Methods (left column, below Data)
**Purpose:** How verification is done.

**Content to include:**
- Ensemble forecasts verified against ERA5-Land
- Probabilistic metrics: CRPSS (relative to climatology), BSS (tercile categories), reliability diagrams
- Fair scoring (Ferro 2014) to account for finite ensemble size
- Spatial verification across Ireland

**Figure:** None, unless a small verification schematic would help

**Approximate length:** ~4-5 bullet points

---

### 4. Results (right 2 columns, main area)
**Purpose:** Answer RQ1 -- does skill exist? This is the visual centrepiece.

**Content to include:**
- Key finding: positive CRPSS for temperature across Ireland through week 6
- Skill decays with lead time but remains above climatology
- Spatial patterns if visible
- Brief caption per figure -- let the figures speak

**Figures (TBD -- to be created in S2S_AI):**
- Spatial CRPSS maps for temperature by lead time (week 2-6)
- Possibly: reliability diagram or BSS maps
- Aim for 2-3 figures that tell the story without text

**Approximate length:** 2-3 sentences of interpretation + 2-3 figures

---

### 5. Subseasonal vs Seasonal (full width)
**Purpose:** Answer RQ2 -- which system to build on?

**Content to include:**
- Both systems show comparable probabilistic skill for temperature
- Despite different ensemble sizes (11 vs 25) and initialisation frequencies
- Deterministic skill diverges more than probabilistic
- Implication: for probabilistic multi-hazard applications, subseasonal system is a viable basis

**Figure:** `crpss_vs_rmss_comparison.png` (exists)

**Approximate length:** 2-3 sentences + the figure

---

### 6. Discussion (bottom left)
**Purpose:** What this means for Irish forecasting and the multi-hazard goal.

**Content to include:**
- First evidence that S2S forecasts carry useful signal over Ireland at these lead times
- Positive skill at weeks 4-6 is encouraging for operational applications
- This establishes the base level of the verification chain shown in Introduction
- Next step is to trace whether this skill propagates to impact variables

**Figure:** None

**Approximate length:** 3-4 bullet points

---

### 7. Future Work (bottom, next to Discussion)
**Purpose:** Where this goes -- back to the causal chain.

**Content to include:**
- Extend verification to precipitation
- Trace skill through hydrological impact variables (soil moisture, runoff)
- Apply ML for drought-to-flood transition probability estimation
- Connects back to the causal chain: atmospheric skill is step 1

**Figure:** Could include a small version of the research landscape diagram here to show the gap being filled

**Approximate length:** 3-4 bullet points

---

### 8. References (bottom right, small)
**Purpose:** Key citations only.

**Candidates (5-8 max):**
- Ferro (2014) -- fair CRPS
- Bevacqua et al. (2021) -- hazard chain colour grammar
- ECMWF EEFH / SEAS5 system documentation
- Key S2S verification references
- Irish hydro-climate references if used

---

## Figures summary

- [x] `dft_causal_diagram.pdf` -- causal chain (exists, from thesis)
- [x] `crpss_vs_rmss_comparison.png` -- subseasonal vs seasonal (exists, from S2S_AI)
- [ ] Spatial CRPSS maps for temperature, weeks 2-6 (to create in S2S_AI)
- [ ] Possibly: reliability diagram or BSS for temperature (to create)
- [ ] LinkedIn QR code with logo (generate at qr-code-generator.com)
- [ ] Check logo resolution for print (decarb_ai.png, InnovateforIreland.png -- currently below 300 DPI)

## Visual best practices
- 300-800 words total
- 40-50% visual area
- 300+ DPI for all images at A0 print size
- White background, UCD green headers -- good contrast
- Sans-serif fonts, minimum 24pt body text at A0
- Left-aligned text (avoid justified)
- F-pattern reading flow for portrait poster
- Bold key words in the core message (betterposter principle)
- QR code with LinkedIn logo as call-to-action (betterposter principle)
- Every section serves the narrative: "can we predict drought-to-flood events?"
