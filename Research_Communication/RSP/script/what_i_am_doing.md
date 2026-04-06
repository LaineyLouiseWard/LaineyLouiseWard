# What I Am Doing — Script

## Objective
Show the panel concrete progress: the pipeline exists, the data is processed, verification is producing results. Plots as evidence.

---

### Slide 4 — Subseasonal vs Seasonal

The first step is choosing which forecast system to build on. The subseasonal system has newer physics, better initial conditions, and it's initialised almost every other day. The seasonal system has older physics but more than double the ensemble size and a much longer record. One samples more in time, the other samples more across ensemble members.

I've compared both systems over a common 10-year period, on a common 0.3 by 0.3 degree grid over Ireland, for three variables: 2-metre temperature, total precipitation, and 10-metre wind speed. I have two reference datasets: observations from 25 Met Éireann stations, and ERA5-Land reanalysis at the same grid spacing.

First I need to understand the biases in ERA5-Land compared to the station observations, because ERA5-Land is my spatial reference.

- [finding on ERA5-Land vs station bias]
- [finding on ERA5-Land vs station bias]

---

### Slide 5 — Deterministic Verification

From there, I performed deterministic verification at weekly lead times. At the station level, both systems are verified against Met Éireann observations. Spatially, they're verified against ERA5-Land.

- [finding from station verification]
- [finding from spatial verification]

The next stage is probabilistic verification, things like Brier skill score and CRPSS, which is about to get underway. Getting the deterministic foundations right first is important because everything else builds on top of it.

That's where the research is. What about training and development?

---

### Notes for plot selection

**Slide 4 (reference comparison):** Pick one or two plots showing ERA5-Land vs station biases.
- Bias by variable: does ERA5-Land have a systematic offset for t2m, precipitation, or wind?

**Slide 5 (deterministic verification):** Plots that show the head-to-head system comparison.
- RMSE by lead week (t2m, ensmean): shows skill decay and whether the systems diverge
- Bias by lead week: if one system has a systematic offset
- Spatial RMSE map (EEFH vs SEAS5 side by side)
- RMSE difference map (SEAS5 minus EEFH): where one system wins
- Spatial ACC map: where anomaly correlation is positive
