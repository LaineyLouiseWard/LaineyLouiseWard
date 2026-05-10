# Poster Session Handover — 10 May 2026

## Current state

The poster compiles and renders correctly. Two new figures are generated from cached data (`poster_data.pkl`, 34 KB):
- `spatial_crpss_poster.png` — 3-panel CRPSS maps (Weeks 2, 4, 6), LambertConformal + tripcolor
- `lineplot_skill_poster.png` — dual-panel ACC + CRPSS vs lead time, seasonal stratification

Scripts:
- `compute_poster_data.py` — runs once (~60 min), loads 1.3 GB EEFH netCDF, caches domain-mean ACC/CRPSS by season + spatial CRPSS/bias. Run with: `conda run -n S2S_AI python -u compute_poster_data.py`
- `plot_poster_figures.py` — reads cache, produces PNGs in seconds. Run with: `conda run -n S2S_AI python plot_poster_figures.py`

## Open decisions

### 1. ACC formulation: spatial vs temporal

**Current implementation:** Temporal ACC (correlation across initialisations at each gridpoint, domain-averaged). This is `gridded_acc()` in `scoring_spatial_native.py`.

**Decision needed:** Switch to spatial (pattern) ACC — correlation across gridpoints for each init, averaged over inits. This is what ECMWF scorecards show and what the 0.6 threshold applies to (Hollingsworth et al. 1980, per Wilks 2006 §7.6.4 and ECMWF FUG §12.A).

**Why it matters:**
- The ACC = 0.6 "useful skill" threshold was empirically calibrated for spatial pattern ACC of 500 hPa Z, not temporal ACC
- Met Éireann audience would recognise spatial ACC from ECMWF charts
- But: 0.6 was calibrated on hemispheric domains (~thousands of gridpoints). Ireland has ~73 land points — the threshold is approximate at best
- Temporal ACC still has value for DFT hotspot identification (where is there pointwise predictability?)

**Action items:**
- Look into whether the 0.6 value is formally applicable at the Ireland scale (small domain, ~73 points)
- Check if `scoring_spatial_native.py` already has a spatial pattern ACC function, or if one needs to be added
- If switching, update `compute_poster_data.py` to compute spatial ACC and re-run
- Consider whether to add a 0.6 reference line on the ACC panel

**Key references to check:**
- Wilks (2006) §7.6.4 — ACC threshold origin, Murphy & Epstein (1989) MSESS=0.20 correspondence
- ECMWF FUG §6.2.2 and §12.A — operational ACC definition
- Jolliffe & Stephenson (2012) Ch. 6 — centred vs uncentred, small-domain considerations
- Robertson et al. (2025) Ch. 2 (Toth) — S2S context
- All available in ~/Documents/zotero-md/

### 2. Spatial map improvements

- Tripcolor triangulation extends slightly outside Ireland at edges — needs clipping to coastline shapefile
- Scotland/Wales corners removed via LambertConformal but bounding box could be tighter
- Point density (73 land points on O320) may look sparse at poster scale — consider whether tripcolor or scatter looks better

### 3. Bias presentation

- Currently: bias mentioned only in Figure 3 caption ("Mean warm bias ~0.6 °C, corrected via LOYO") and Discussion bullet
- Spatial bias data is cached in `poster_data.pkl` (`spatial_bias` key) but not plotted
- Bias is spatially uniform (~0.6°C warm, growing slightly with lead: 0.60 → 0.70°C)
- Decision: is a text mention sufficient, or does it need a visual?

### 4. Whether both spatial CRPSS maps AND CRPSS line plot are needed

- Spatial maps show *where* skill exists (unique contribution: first for Ireland)
- Line plot CRPSS shows *decay + seasonal dependence*
- They answer different questions but both show CRPSS — slight redundancy
- Current layout works with both side-by-side. Could drop spatial if space is tight.

## Computed results (for reference)

```
Annual (2046 inits):  Wk2 ACC=0.584 CRPSS=0.428 | Wk3 ACC=0.268 CRPSS=0.315 | Wk4 ACC=0.185 CRPSS=0.293 | Wk5 ACC=0.147 CRPSS=0.289 | Wk6 ACC=0.116 CRPSS=0.283
DJF    (509 inits):   Wk2 ACC=0.663 CRPSS=0.479 | Wk3 ACC=0.314 CRPSS=0.333 | Wk4 ACC=0.239 CRPSS=0.324 | Wk5 ACC=0.208 CRPSS=0.303 | Wk6 ACC=0.115 CRPSS=0.286
JJA    (517 inits):   Wk2 ACC=0.583 CRPSS=0.433 | Wk3 ACC=0.187 CRPSS=0.294 | Wk4 ACC=0.066 CRPSS=0.272 | Wk5 ACC=0.075 CRPSS=0.290 | Wk6 ACC=0.072 CRPSS=0.288

Spatial bias (annual): Wk2 mean=0.60°C | Wk4 mean=0.66°C | Wk6 mean=0.70°C
```

Note: ACC values here are temporal (gridpoint-level, domain-averaged). Spatial pattern ACC will differ.

## Files modified this session

- `poster.tex` — widened intro text minipage, fixed arrows, updated Methods (LOYO), Results (new figures + captions), Discussion (updated findings/future work), Data (removed midrule, 6 weeks), unified impcol colour
- `compute_poster_data.py` — new: computes and caches all poster data
- `plot_poster_figures.py` — new: generates poster figures from cache
- `poster_data.pkl` — cached computed data (not tracked in git)
- `spatial_crpss_poster.png`, `lineplot_skill_poster.png` — generated figures
- `baposter.cls` — modified by user (not this session)
- `dft_causal_diagram_poster.tex/pdf` — impcol colour updated
- `verification_cone.tex` — coneRed already matched
