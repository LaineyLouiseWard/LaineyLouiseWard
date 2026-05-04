# Met Eireann Symposium Poster -- Draft Text

Target: 300-500 words total (excluding table, captions, references).

---

## Introduction (~100 words)

Floods and droughts can occur in sequence, with one intensifying the other. Drought hardens the soil and reduces infiltration capacity, amplifying the flood response to subsequent rainfall. Globally, approximately 25% of floods are preceded by drought [1], and socio-economic losses from these compound events can be up to eight times greater than from isolated hazards [2].

Despite growing recognition of this multi-hazard risk, all existing research on drought-to-flood transitions is retrospective. No study has attempted to forecast them at any lead time. This research evaluates whether extended-range forecasts carry useful skill over Ireland at subseasonal-to-seasonal lead times (2 weeks to 2 months) — the first step towards operational transition prediction.

[FIGURE: dft_causal_diagram.pdf — right side of box]
Figure 1: Causal chain for drought-to-flood transitions over the British-Irish Isles (after Bevacqua et al. [3]).

---

## Data (table + ~30 words)

| | EEFH (subseasonal) | SEAS5 (seasonal) |
|---|---|---|
| System | ECMWF extended-range | ECMWF System 51 |
| Members | 11 | 25 |
| Initialisation | Weekly | Monthly |
| Native resolution | Tco639 (~16 km) | ~36 km |
| Lead times | Weeks 2--6 | Weeks 2--6 |

**Reference:** ERA5-Land reanalysis on a common 0.3° grid.
**Period:** 2006--2016 reforecasts.
**Variable:** 2 m temperature.
**Verification:** Fair CRPSS [4], BSS (tercile categories), spatial and domain-mean.

---

## Results (~60 words — figure captions only)

[FIGURE A: combined CRPSS — spatial maps + domain mean, TO CREATE]
Figure 2: CRPSS for EEFH relative to climatology (Fair CRPS). Spatial maps at Weeks 2--6 (left); domain-mean with 10th--90th percentile range (right). Skill is positive across all of Ireland through Week 6.

[FIGURE B: crpss_vs_rmss_comparison.png]
Figure 3: CRPSS and RMSS for EEFH and SEAS5. Both systems show comparable probabilistic skill. Deterministic skill degrades faster, particularly for EEFH from Week 3.

---

## Discussion & Future Work (~80 words)

This is the first assessment of extended-range forecast skill over Ireland at subseasonal-to-seasonal lead times. Forecasts carry useful skill for 2 m temperature through Week 6, with CRPSS remaining positive across the full domain. Both the subseasonal and seasonal systems offer comparable performance, suggesting either can serve as a basis for downstream applications.

These results establish skill at the atmospheric driver level of the causal chain (Figure 1). Future work will extend verification to precipitation, trace skill through hydrological impact variables, and define drought-to-flood transition events from ensemble forecast trajectories.

[ICON: qrcode_linkedin.png — bottom right, with "Connect" label]

---

## References

[1] Matano et al. (2024). Nat. Hazards Earth Syst. Sci.
[2] Worou & Messori (2025). Environ. Res. Lett.
[3] Bevacqua et al. (2021). Nat. Rev. Earth Environ.
[4] Ferro (2014). Q. J. R. Meteorol. Soc.
[5] Parry et al. (2023). J. Hydrometeorol.
[6] Brunner et al. (2025). Environ. Res. Lett.

---

## Consistency checks applied

- "useful skill" used consistently (not "usable skill" / "useful signal")
- "probabilistic" used only where necessary (captions, not repeated in Discussion)
- ECMWF, EEFH, SEAS5 introduced only from Data onwards, not in Introduction
- "subseasonal-to-seasonal" spelled out in Introduction and Discussion; not abbreviated to S2S
- Figure captions tightened to 1-2 sentences each (matching Boris's density)
- ~270 words total body text (excluding table, captions, references)
