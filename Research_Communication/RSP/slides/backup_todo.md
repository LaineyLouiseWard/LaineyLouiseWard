# Backup Slides — To Do

## 1. Event definition landscape — map + terminology + methods

**Question it answers:** "Which event definition will you use? What indices exist? Where has this been studied?"

### Concept
A world map (or at least a map covering China, US, Europe, Australia) with study locations marked, showing:
- What **name** each community uses for the same phenomenon
- What **variable** they detect it from (precipitation vs streamflow vs circulation)
- Roughly what **method** they use (high-level grouping, not every index)

The point is to show visually that (a) the field is fragmented across geographies and terminologies, (b) nobody has done this for Ireland, and (c) no study uses forecasts — they're all diagnostic.

### Geographic clusters and terminology

| Region | Term used | Variable | Method (high level) | Key studies |
|---|---|---|---|---|
| **China** | Drought-flood abrupt alternation (DFAA) | Precipitation (SPI) | Purpose-built alternation indices (LDFAI, SDFAI, DWAAI, MSDFAI) with empirically calibrated weighting coefficients | Wu et al. 2006; Zhao et al. 2020; Bai et al. 2024; Wang et al. 2024; Zhang et al. 2025 |
| **US (California)** | Precipitation / hydroclimate whiplash | Precipitation (SPI, SPEI, percentiles) | Drought index thresholds + temporal proximity | Swain et al. 2018; Mullens & Engstrom 2025; DeFlorio et al. 2024 |
| **US (CONUS)** | Hydrological whiplash / drought-to-flood transition | Streamflow | Streamflow percentile thresholds + transition length | Gotte & Brunner 2024; Yang et al. 2025; Hammond et al. 2025 |
| **Europe** | Spatially compounding drought-flood | Streamflow + precipitation | Percentile-based, spatial co-occurrence | Brunner et al. 2025 |
| **France** | Low/high flow transitions | Streamflow + baseflow | Threshold crossing + baseflow recovery | Guimaraes et al. 2026 |
| **Chile, Switzerland** | Drought-to-flood transition | Streamflow (modelled vs observed) | Percentile-based, focus on hydro model skill | Munoz-Castro et al. 2026 |
| **Australia + Europe** | Dry-to-wet flip-flop | Precipitation | SPI + percentile framework | Goswami et al. 2026 |
| **Global** | Consecutive dry-wet extremes | SPEI | Copula-based joint exceedance | Rashid & Wahl 2022; Matano et al. 2024 |
| **England/Wales** | (qualitative) | Rainfall, river flow | Narrative / monitoring | Parry et al. 2013 |
| **Euro-Atlantic (atmospheric)** | Weather whiplash | 500 hPa circulation | SOM-based regime classification | Francis et al. 2023 |
| **Ireland** | **Nothing** | — | — | Meresa et al. 2023 studied drought alone; no transition study exists |

### High-level method grouping (for the slide)
Three broad approaches, to avoid listing every index:
1. **Precipitation-based** — uses SPI or similar. Includes DFAA indices (China) and precipitation whiplash (US). Detects meteorological transitions.
2. **Streamflow-based** — uses flow percentiles. Western tradition (Anderson, Gotte & Brunner, Yang). Detects hydrological transitions. Requires observed or modelled streamflow.
3. **Circulation-based** — uses 500 hPa patterns. Francis et al. weather whiplash. Detects the upstream atmospheric mechanism, not the surface impact.

Key point: these three approaches can give **contradictory results** on the same data. Yang et al. (2025) showed met-based and streamflow-based analyses yield opposite frequency trends over 7 decades. Anderson et al. (2025) showed different threshold methods detect only 3 of 8 known impactful events.

### What to note on the slide
- Ireland is blank — no study has applied any of these methods here
- None of these studies use forecasts — all diagnostic / observational
- DFAA weighting coefficients are calibrated for Chinese monsoon seasonality — would need recalibration for Ireland (Lu 2009 already found different coefficients for Mississippi Valley)

**Source material:** Literature_CompoundEvents.md (summary table), Literature_Terminology.md (terminology table + DFAA section), ROADMAP Phase 3


## 2. EEFH vs SEAS5 system comparison table

**Question it answers:** "What's the difference between the two systems? Why compare them?"

Simple table:

| | EEFH (extended-range) | SEAS5 (seasonal) |
|---|---|---|
| Model cycle | Cy48r1 (2023) | Cy43r1 (2017) |
| Ensemble size | 101 members (reforecasts: 11) | 51 members (reforecasts: 25) |
| Init frequency | Every ~2 days | 1st of each month |
| Reforecast period | ~20 years (2003-2022) | 36 years (1981-2016) |
| Max lead time | 46 days | 7 months |
| Resolution | ~18 km (Tco639) → ~36 km (Tco319) day 15 | ~36 km (Tco319) |

Note: check these details against ECMWF documentation before presenting. Model cycle versions and resolution details may need updating.

**Key point to make verbally:** The matched comparison in Phase 1 uses the common overlap (2006-2016, 1st-of-month inits) so differences reflect model physics and ensemble size, not data coverage.


## 3. Irish / UK drought-to-flood evidence

**Question it answers:** "Do drought-to-flood transitions actually happen in Ireland?"

Need to find:
- **Parry et al. (2013)** — documents the 2012 drought-to-flood transition in England and Wales. Already in Zotero (LTWXYRPW). This is the closest published case study to Ireland.
- **Burt et al. (2016)** — long-term hydroclimatic variability in the British Isles, including Ireland. Already in Zotero (L7F2V3YD).
- **Meresa et al. (2023)** — Irish drought propagation characteristics. Already cited in RPDP. Shows droughts happen; doesn't cover transitions.
- **Turner et al. (2025)** — UK hydrological summary. Already in Zotero (HWPT9EM4).
- Any Met Eireann or OPW reports on flooding following dry spells?

A slide with a timeline of a known Irish or UK drought-to-flood sequence would be ideal. Even a qualitative one showing "drought here → rain here → flooding here" with dates.

**Action:** Search Zotero and literature for Irish-specific drought-to-flood cases. Check Literature_Further_Searches.md Search #1 (Irish catchment characterisation).


## 4. ML pipeline entry points

**Question it answers:** "Where does ML fit? Why do you need it?"

Diagram showing the forecast-to-event chain with ML entry points marked:

```
Met forecast → [ML 1: post-processing] → Corrected forecast
    → [ML 2: hydro model replacement] → Streamflow
    → [ML 3: hybrid hydro chain] → Streamflow (alternative)
    → Event detection → Drought-to-flood events
    → [ML 4: transition probability] → P(transition | regime, state)
    → [ML 5: regime-conditioned post-processing]
```

Key papers for each entry point:
1. Post-processing: Kiefer et al. (2024) — random forests for S2S temperature
2. Hydro replacement: Kratzert et al. (2018) — LSTM rainfall-runoff
3. Hybrid chain: Dong et al. (2025) — CNN downscaling + XAJ-LSTM
4. Transition probability: no existing work (novel contribution)
5. Regime-conditioned: Kiefer et al. (2024) — regime state as ML input

**Key point:** Entry point 4 is the most novel — nobody has tried to learn the nonlinear mapping from weather regime state + catchment state → transition probability. Entry points 1-3 have precedent but not for multi-hazard events or Irish data.

**Source:** User has a Google Slide of similar. Adapt to Beamer.


## 5. AI for S2S forecasting (potential question)

**Question it answers:** "What about AI-based S2S forecast models? Why aren't you using them?"

This is a reasonable question given the current hype around AI weather models (Pangu-Weather, GraphCast, GenCast, FourCastNet, etc.). Possible angles the panel might probe:

- **"Why not use an AI forecast model instead of ECMWF?"** — AI weather models are trained on ERA5 reanalysis and currently produce deterministic or small-ensemble forecasts. They show strong skill at medium range (1-10 days) but S2S skill is less established. ECMWF's physics-based systems remain the operational standard at S2S timescales. The thesis uses ECMWF reforecasts as the baseline, and ML enters as enhancement (post-processing, hydro modelling), not as a replacement for the dynamical forecast itself.

- **"Could you use AI models in future?"** — Yes, as they mature. But the thesis contribution is about the variable-to-impact-to-event chain, not about which forecast model generates the initial meteorological fields. The methodology transfers to any upstream forecast system.

- **"What's the difference between your ML work and these AI models?"** — AI weather models replace the atmospheric model. The thesis ML replaces or enhances downstream steps (post-processing, hydrology, transition prediction). Different part of the pipeline entirely.

**Key papers if needed:**
- Lam et al. (2023) — GraphCast
- Bi et al. (2023) — Pangu-Weather
- Price et al. (2025) — GenCast (probabilistic)
- Ben-Bouallegue et al. (2024) — ECMWF evaluation of AI models at S2S

**Action:** Check whether Ben-Bouallegue or similar S2S-specific AI evaluation papers are in Zotero. Having one reference ready is enough — the point is to show awareness without derailing into a different thesis.
