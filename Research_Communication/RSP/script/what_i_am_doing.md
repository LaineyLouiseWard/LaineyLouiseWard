# What I Am Doing — Script

## Objective
Show the panel concrete progress: the pipeline exists, the data is processed, verification is producing results. Two plots as evidence.

---

### Slide 3 — The System Comparison

So which forecast system should we build on? ECMWF runs two systems that overlap in the two-to-six week range, and they make different trade-offs. The subseasonal system, EEFH, has newer model physics, better initial conditions, and it's initialised almost every other day. But it only has 11 ensemble members. The seasonal system, SEAS5, has older physics from 2016, but more than double the ensemble size and a much longer reforecast record. It initialises once a month.

So the question is: does the newer system actually give you better forecasts, or does the larger ensemble compensate? Nobody has compared them head-to-head for raw atmospheric variables at weekly resolution.

I've built a verification pipeline to answer that. Both systems are extracted at native resolution to 25 Irish stations, with initialisation dates matched so the comparison is fair. I'm verifying temperature, precipitation, and wind speed at weekly lead times out to six weeks. The deterministic verification is largely complete, both at station level and spatially. I've also started on probabilistic metrics.

[click — Plot 1]

[describe finding from plot 1]

[click — Plot 2]

[describe finding from plot 2]

[~90s, ~190 words without plot descriptions]

---

### Notes for plot selection

Pick two plots that tell a clear story to a non-specialist. Candidates:
- **RMSE by lead week** (t2m, ensmean, all stations): shows skill decay and whether the two systems diverge. Panel sees that the systems are similar per-init.
- **RMSE difference heatmap** (SEAS5 minus EEFH, variables × lead weeks): the headline figure. Shows where one system wins and by how much. Visually striking, tells the story in one image.
- **Bias by lead week** (tp): if precipitation bias is interesting, this could show a systematic difference.
- **Spatial RMSE map**: shows geographic patterns, immediately readable for the panel.

Recommendation: RMSE by lead week (simple, sets up the comparison) + RMSE difference heatmap (the punchline).
