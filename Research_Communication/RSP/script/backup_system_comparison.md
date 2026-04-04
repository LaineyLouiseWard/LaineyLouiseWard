# Backup — Subseasonal vs Seasonal System Comparison

## When to use
If the panel asks "what's the difference between the two systems?", "why compare them?", or "which one is better?"

---

The subseasonal system runs on Cy49r1, which is eight years newer than the seasonal system's Cy43r1. It has more vertical levels, newer stochastic physics, and it initialises from ERA5 rather than ERA-Interim. On paper it should be better at everything.

But the seasonal system has more than double the reforecast ensemble size, 25 members against 11, and a much longer reforecast record, 36 years against 20. For rare events like drought-to-flood transitions you need as many samples as possible, so that matters.

To make the comparison fair I've matched them on a common window, 2006 to 2016, using only the 1st-of-month initialisations that both systems share, on the same 0.3 degree grid over Ireland. That way any differences I see are down to model physics and ensemble size, not data coverage or grid spacing.

The trade-off is basically: the subseasonal system samples more frequently in time, the seasonal system samples more across ensemble members. Which matters more depends on what you're trying to verify.

[~40s, ~170 words]
