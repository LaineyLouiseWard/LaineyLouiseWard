# What I Am Doing — Script

## Objective
Show the panel concrete progress: the pipeline exists, the data is processed, verification is producing results. Three plots as evidence.

---

### Slide 4 — Subseasonal vs Seasonal

Which forecast system should we build on? The subseasonal system has newer physics, better initial conditions, and it's initialised almost every other day. The seasonal system has older physics but more than double the ensemble size and a much longer record. One samples more in time, the other samples more across ensemble members.

Does the newer system actually give you better forecasts, or does the larger ensemble compensate? Nobody has compared them head-to-head for raw atmospheric variables at weekly resolution. I've built a verification pipeline to answer that. Both systems are extracted at native resolution to 25 Irish stations, with initialisation dates matched so the comparison is fair.

[click — point skill plot]

[describe finding from point skill plot]

[~60s, ~120 words without plot description]

---

### Slide 5 — Spatial Verification

But does that hold everywhere across Ireland? I've extended the verification spatially on a common grid.

[describe spatial plot 1]

[describe spatial plot 2]

[~40s, depends on plot descriptions]

---

### Notes for plot selection

**Slide 4 (point skill):** Pick one plot that shows the head-to-head comparison clearly.
- RMSE by lead week (t2m, ensmean): shows skill decay and whether the systems diverge
- Bias by lead week: if one system has a systematic offset

**Slide 5 (spatial):** Two plots that show geographic patterns.
- Spatial RMSE map (EEFH vs SEAS5 side by side)
- RMSE difference map (SEAS5 minus EEFH): where one system wins
- Spatial ACC map: where anomaly correlation is positive
