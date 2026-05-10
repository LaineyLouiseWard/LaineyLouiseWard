# Poster Results — Figure Specification

This spec defines two figures for the Results section. Another chat should be able to pick this up and create both figures from the S2S_AI analysis data.

---

## Decisions made

- **Weeks 2, 4, 6** for spatial maps (evenly spaced, clear decay progression)
- **EEFH (subseasonal) only** in all plots — no SEAS5. SEAS5 stays in Data table for context but results focus on the subseasonal system.
- **Two metrics**: ACC (deterministic, timing skill) + CRPSS (probabilistic, full-distribution skill). These complement rather than contradict — ACC decays faster, CRPSS stays positive longer, telling a coherent story about ensemble value.
- **Seasonal stratification** in line plot: Annual, DJF, JJA. Relevant to DFT narrative (summer is when drought-to-flood events occur, and it's the weaker season).
- **No SEAS5 in plots** — mention in text only.

---

## Figure 1: Spatial CRPSS maps

### What it shows
3-panel horizontal strip of Ireland maps showing fair CRPSS (Ferro 2014) for EEFH 2m temperature at weeks 2, 4, and 6. Bias-corrected (LOYO annual mean).

### Data source
- Notebook: `S2S_AI/notebooks/Nb2_Spatial_Structure.ipynb`, section 2.3
- Existing output: `S2S_AI/notebooks/figures/Nb2/2_3a_crpss_maps.png` (2×5 grid: EEFH top row, SEAS5 bottom; weeks 2–6 columns)
- Extract: **EEFH row only, columns for weeks 2, 4, 6**

### Layout
- 3 panels side by side, labelled "Week 2", "Week 4", "Week 6"
- Ireland coastline with gridpoint-level CRPSS values (native O320 grid, 73 land points)
- Shared colourbar on right

### Style
- Diverging colourmap: blue (positive skill) → white (zero) → red (negative). Same as existing plots.
- Colourbar range: -0.45 to +0.45 (matching existing)
- No title on figure (poster caption handles this)
- Panel labels ("Week 2" etc.) above each panel, clean sans-serif
- Coastline in dark grey, thin
- Poster-ready: large font sizes for labels and colourbar ticks (minimum ~14pt equivalent at final poster scale)
- Compact — minimise whitespace between panels

### Expected appearance
- Week 2: strong blue across all of Ireland (CRPSS ~0.3–0.4)
- Week 4: lighter blue, some areas approaching white (CRPSS ~0.1–0.2)
- Week 6: pale blue/near-white, still positive everywhere (CRPSS ~0.05–0.15)

---

## Figure 2: Dual-panel line plot (ACC + CRPSS vs lead time)

### What it shows
Two side-by-side panels showing domain-mean skill vs lead time (weeks 2–6), with seasonal stratification. Left panel: ACC. Right panel: fair CRPSS. Each panel has 3 lines: Annual, DJF, JJA.

### Data source
- ACC seasonal data: `S2S_AI/notebooks/Nb3_Seasonal_Structure.ipynb`, section 3.1 (`3_1b_acc_seasonal.png`)
- CRPSS seasonal data: `S2S_AI/notebooks/Nb3_Seasonal_Structure.ipynb`, section 3.1 (`3_1c_crpss_seasonal.png`)
- Annual data: `S2S_AI/notebooks/Nb1_LeadTime_Evolution.ipynb`, sections 1.2c and 1.3a
- All values are domain-mean (averaged across 59 Irish land gridpoints), EEFH only, bias-corrected (LOYO annual mean)
- Bootstrap confidence intervals available (block size 4, n=500) — include as shading if legible, omit if cluttered

### Layout
- 2 panels side by side: left = ACC, right = CRPSS
- x-axis: Week (2, 3, 4, 5, 6) — discrete ticks, not continuous
- y-axis left panel: ACC (range roughly -0.1 to 0.7)
- y-axis right panel: CRPSS (range roughly -0.05 to 0.5)
- Horizontal reference line at y=0 in both panels (dashed grey, thin)

### Lines (3 per panel)
| Line | Colour | Style | Label |
|------|--------|-------|-------|
| Annual (all inits) | Black | Solid, thick (2.5pt) | Annual |
| DJF (Dec–Feb) | Blue (#1f77b4 or similar) | Solid, thick (2pt) | DJF |
| JJA (Jun–Aug) | Red (#d62728 or similar) | Solid, thick (2pt) | JJA |

- Markers on each point (circles, size ~8pt) for readability
- Legend: single shared legend below or between panels, horizontal layout

### Approximate values (EEFH, from Nb1/Nb3 analysis)

**ACC (domain-mean):**
| Week | Annual | DJF | JJA |
|------|--------|-----|-----|
| 2 | 0.58 | 0.65 | 0.41 |
| 3 | 0.38 | 0.45 | 0.28 |
| 4 | 0.25 | 0.34 | 0.18 |
| 5 | 0.16 | 0.22 | 0.12 |
| 6 | 0.12 | 0.15 | 0.08 |

**CRPSS (domain-mean, fair, bias-corrected):**
| Week | Annual | DJF | JJA |
|------|--------|-----|-----|
| 2 | 0.43 | 0.43 | 0.30 |
| 3 | 0.35 | 0.36 | 0.29 |
| 4 | 0.30 | 0.30 | 0.28 |
| 5 | 0.29 | 0.26 | 0.28 |
| 6 | 0.28 | 0.24 | 0.27 |

*These are approximate from the analysis report — the actual plotting code should read from the computed data arrays, not these tables.*

### Style
- Clean, minimal — no gridlines or light grey gridlines only
- Panel titles: "ACC" and "CRPSS" (or "Anomaly Correlation" / "CRPS Skill Score") above each panel
- Sans-serif font throughout
- Poster-ready: thick lines, large markers, large axis labels (minimum ~14pt equivalent)
- If bootstrap CIs are included: thin shaded bands (alpha ~0.15) around each line, matching line colour
- Compact — minimise whitespace between panels

### Key visual message
- Both metrics decay with lead, but CRPSS decays slower (ensemble distributional value persists)
- DJF (blue) is highest at early leads in both panels
- JJA (red) is lower at week 2 but flatter — competitive with DJF by weeks 5–6 in CRPSS
- All lines stay above zero through week 6 for CRPSS; ACC approaches zero by week 5–6

---

## Poster layout for Results section

Both figures sit in the full-width Results box (span=3). Recommended arrangement:

**Option A — side by side:**
- Left ~40%: Figure 1 (3 spatial maps)
- Right ~60%: Figure 2 (2-panel line plot)
- Captions below each

**Option B — stacked:**
- Top: Figure 1 (3 spatial maps, full width)
- Bottom: Figure 2 (2-panel line plot, full width)

Try both; side-by-side saves vertical space but check that maps are large enough to read.

---

## Figure 1 edits (causal diagram — Introduction)

- [ ] Grey boxes: darken slightly (currently too light, low contrast on poster)
- [ ] "IVT surge / intense precipitation" → **"Moisture influx"** (the atmospheric driver — large moisture delivery via e.g. atmospheric rivers or persistent southwesterly flow; distinct from the precipitation outcome which can be sustained moderate rain, intense heavy rain, or both)
- [ ] "Drought development" phase label → **"Drought"**
- [ ] "Flood on modified catchment" phase label → **"Flood"**

---

## Poster text changes

- **Data table**: Keep both subseasonal and seasonal rows. SEAS5 provides context even though results only show EEFH.
- **Methods**: Add framing sentence: "We assess forecast skill across three dimensions: spatial extent, lead-time persistence, and seasonal dependence."
- **Results text**: Brief note: "EEFH outperforms SEAS5 at all leads for both metrics (not shown)."
- **Discussion**: Update bullets to reflect dual-metric and seasonal findings.
