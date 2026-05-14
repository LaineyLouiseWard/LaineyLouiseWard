# Poster TODO

## RMSE map fixes
- [ ] Fix GRIB template metadata so earthkit colourbar reads "RMSE (°C)" instead of "Land-sea mask (dimensionless)"
  - Options: (a) set `shortName` and `units` in eccodes before writing, or (b) overlay matplotlib text after earthkit renders
- [ ] Clean up colourbar tick values — currently ugly decimals (0.9273, 1.055...). Use clean round values like 1.0, 1.2, 1.4, 1.6, 1.8, 2.0

## Interpretation of results

### ACC (centred, spatial pattern correlation)
- All seasons start ~0.28–0.30 at week 2, decaying to 0.02–0.06 by week 6
- None reach the 0.6 "useful skill" threshold at any lead
- **JJA retains slightly more ACC than DJF at longer leads** (wk6: JJA=0.056 vs DJF=0.018) — opposite to what the green summary box currently claims ("DJF skill exceeds JJA")
- Interpretation: spatial anomaly patterns are weakly predictable at wk2 but lose coherence rapidly. JJA persistence (soil moisture memory?) may sustain weak spatial correlations slightly longer

### Anomaly bias (domain-mean, model-referenced fc minus ERA5-referenced obs)
- **DJF has the largest residual anomaly bias (~0.2°C warm)**, roughly constant across leads
- Annual and JJA are similar (~0.08°C warm), also flat across leads
- The bias being flat with lead means it's a systematic offset between model and ERA5 climatologies, not a lead-dependent drift
- This DJF warm bias is interesting — the green box currently mentions "JJA warm bias" which refers to the raw seasonal cycle (Fig. 2), not the anomaly bias. These are different quantities. Both can be mentioned but should be distinguished

### Spatial anomaly RMSE
- wk2: 1.39°C, wk4: 1.76°C, wk6: 1.79°C (domain means)
- Rapid increase from wk2 to wk4, then plateau
- The plateau suggests that beyond ~4 weeks the forecast anomaly errors approach the variability of the observed anomalies (i.e. approaching climatological RMSE)

### Rank histogram (JJA, pooled wk2–6, raw values)
- Strongly L-shaped: rank 1 has ~3.5× the count of a uniform distribution
- Observations fall below all ensemble members far too often → ensemble is systematically too warm in JJA
- This is consistent with the ~0.08°C JJA anomaly bias AND the known IFS JJA warm bias in raw temperature (Fig. 2)
- Note: rank histogram uses raw values (rank is invariant to constant shift) — so it reflects both the climatological bias and any residual anomaly bias

### Overall story
The ECMWF sub-seasonal ensemble shows:
1. **Modest but positive deterministic skill** (ACC > 0) through week 6, confirming forecasts outperform climatology for spatial temperature patterns over Ireland
2. **Stronger probabilistic skill** in DJF than JJA (CRPSS: DJF stays ~0.28 at wk6, JJA drops to ~0 by wk6)
3. **The ensemble is underdispersive in JJA** (L-shaped rank histogram), likely linked to known IFS limitations in soil moisture and land–atmosphere coupling [Hersbach et al. 2020]
4. **A persistent DJF warm anomaly bias** (~0.2°C) that doesn't grow with lead — suggesting a systematic offset between model and reanalysis climatologies rather than forecast drift

This motivates the Future Work items: probabilistic bias correction could address the JJA calibration issue, and comparison with SEAS5 seasonal forecasts would show whether longer-range systems have similar skill characteristics.

## Figure captions — do they need updating?

### Fig. 2 caption (seasonal cycle)
> "Domain-mean 2 m temperature: forecast (weeks 2–6), ERA5, and Met Éireann observations."
- **Fine as-is.** This is a raw temperature plot, caption is accurate.

### Fig. 3 caption (ACC + bias)
> "(a) Centred ACC and (b) anomaly bias by lead time and season."
- **Check:** are ACC and bias actually shown as (a) and (b) subplots in a single figure, or are they separate PNGs? Currently `poster_fig_acc.png` is in the poster but `poster_fig_bias.png` is not referenced in poster.tex. Either:
  - (a) Combine ACC and bias into a single 2-panel figure, OR
  - (b) Add bias as a separate figure and update caption, OR
  - (c) Drop bias from the poster and simplify caption to just "Centred ACC by lead time and season."

### Fig. 4 caption (RMSE maps)
> "Anomaly RMSE at weeks 2, 4, and 6 over Ireland (O320 grid)."
- **Fine as-is** once the colourbar label is fixed.

### Green summary box — needs updating
Current text:
1. "JJA warm bias is consistent with known IFS limitations in soil moisture and vegetation–atmosphere coupling [5]"
2. "The forecast outperforms climatology to week 6; DJF skill exceeds JJA at early leads"

Issues:
- Point 1: Still valid for raw temperature (Fig. 2), but could be more precise about which bias (raw vs anomaly)
- Point 2: "DJF skill exceeds JJA at early leads" — **not supported by ACC** (all seasons are similar at wk2). It IS supported by **CRPSS** (DJF=0.46 vs JJA=0.19 at wk2), but CRPSS isn't shown on the poster. Consider rewording to match what the displayed figures actually show.
