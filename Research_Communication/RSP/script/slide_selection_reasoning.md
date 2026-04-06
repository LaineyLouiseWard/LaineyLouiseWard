# What I Am Doing — Slide Selection

## The problem

The RSP is 10 minutes across three sections. "What I Am Doing" currently has 4 slides:

| Slide | Content | Time |
|-------|---------|------|
| 4 | System comparison + station map | ~50s |
| 4b | Raw t2m chain (obs → forecast) | ~35s |
| 5 | Station RMSE/Bias at Knock Airport | ~30s |
| 6 | Spatial bias 4-panel | ~40s |

That's ~155s for one section of a 600s talk. The literature review section ("What I Have Done") needs ~250s for three dense slides. The opening is ~30s, the training/development slide is ~60s. That leaves ~260s for "What I Am Doing" — workable but tight, with no buffer for the panel interrupting or asking questions mid-flow.

## What does the panel actually need from this section?

1. Evidence that the pipeline works and produces results
2. A concrete finding they can interrogate
3. Enough to trust the methodology without drowning in detail

They do NOT need a full tour of every verification plot. That's what the backup PDF is for.

## The station verification slide (Slide 5)

**What it shows:** RMSE and Bias by lead week at a single station (Knock Airport), for subseasonal 2m temperature only. Ensemble mean outperforms climatology through ~week 3, then skill drops. Persistent warm bias ~0.2–0.4°C.

**What it proves:** The verification pipeline works. Ensemble mean is the best variant. Skill decays with lead time (expected). There's a systematic warm bias.

**The problem:** It's one station, one variable, one system. The panel's immediate question will be "what about the other stations?" or "what about the seasonal system?" — and the answer is "similar" but you can't show it without more slides. A single-station line plot is inherently anecdotal.

**The key finding (week 3 skill cutoff) can be stated in one sentence** while narrating the spatial slide: "At the station level, skill persists through about week 3 before the forecast loses value over climatology."

## The spatial bias slide (Slide 6)

**What it shows:** Bias across Ireland for climatology, subseasonal, seasonal, and their difference. Station markers overlaid. Week 3.

**What it proves:** Both systems verified, methodology works at scale, the subseasonal system is generally less biased than the seasonal. Shows the head-to-head comparison the panel cares about.

**Why it's stronger for the main talk:** It covers the whole domain, compares both systems directly, and the difference panel is a clear visual takeaway. It's one slide that answers the question "which system is better and where?"

## The raw t2m chain (Slide 4b)

**What it shows:** Mean weekly-mean t2m at 4 stations across Met Eireann → ERA5-Land → Subseasonal → Seasonal. Signal compression from observations to forecasts.

**What it proves:** You understand the data chain. The forecasts smooth spatial gradients.

**Is it essential?** It's a nice bridge — visually intuitive, sets up verification. But the finding ("forecasts smooth the gradient") is unsurprising and could be stated verbally. On the other hand, it's the kind of visual that makes a panel think "they really know this data," which builds trust.

## Options

### Option A: Current (4 slides, ~155s)
System comparison → Raw chain → Station verification → Spatial bias

Pro: thorough. Con: 4 slides is a lot for one section; station slide is anecdotal.

### Option B: Drop station verification to backup (3 slides, ~125s)
System comparison → Raw chain → Spatial bias

Pro: tighter, spatial bias is the stronger result, station detail available as backup. Saves ~30s for the literature review or for panel questions.

Con: you lose the lead-week skill decay plot. But you can state "skill persists through about week 3" verbally on the spatial slide.

### Option C: Drop raw chain AND station verification (2 slides, ~90s)
System comparison → Spatial bias

Pro: maximum time for other sections. Con: jumps from setup to results with no bridge — feels abrupt.

### Option D: Drop raw chain, keep station + spatial (3 slides, ~120s)
System comparison → Station verification → Spatial bias

Pro: both verification views. Con: loses the bridge, and you still have the anecdotal-station problem.

## Recommendation

**Option B.** The raw t2m chain earns its place — not just as a visual bridge, but as a methodological setup that makes the spatial bias slide interpretable. The station verification is backup for panel questions.

The "What I Am Doing" section then becomes:
1. **System comparison + map** (~50s) — here's what I'm comparing and where
2. **Raw t2m chain** (~40s) — here's what the raw data looks like, and why the reference dataset matters
3. **Spatial bias** (~40s) — here's the headline result, plus transition to next steps

Total: ~130s. That frees up ~25s compared to the current plan.

---

## Slide 4b narrative — what am I actually explaining?

### What's plotted

S2S verification works with weekly means, so this is the actual quantity being verified: mean weekly-mean 2m temperature at Week 3 lead time, averaged across all initialisations in the 2006–2016 window. Shown at 4 representative stations across my two reference datasets (Met Éireann, ERA5-Land) and my two forecast systems (Subseasonal, Seasonal).

### What you see

**ERA5-Land is warm-biased relative to Met Éireann.** The northwest station is the clearest example. In the Met Éireann panel it's cool blue (~9.5°C). In ERA5-Land it shifts to warm orange (~10.5°C). That's roughly a degree of warm bias in the reanalysis at that location.

**Why this matters for verification.** ERA5-Land is the spatial reference — it's the only gridded dataset available, so spatial verification has to use it. But if ERA5-Land runs warm at certain locations, then verifying forecasts against it will make the forecasts look cold-biased, even if the forecasts are actually closer to reality. The northwest station is a case in point: the forecast values sit closer to Met Éireann (good agreement with truth), but compared to ERA5-Land they'd appear cold-biased. This is why having both reference datasets is essential — it separates genuine forecast bias from reference dataset bias.

**Seasonal is warm-biased relative to Subseasonal.** Comparing the two right-hand panels, the seasonal system shows warmer values, particularly at the southern stations. This warm offset then shows up in the spatial bias slide as the blue in the difference panel (subseasonal minus seasonal is negative = subseasonal is cooler/less biased).

### The message in one breath

"These four panels show the same quantity across both references and both forecasts. Two things stand out: ERA5-Land runs warm compared to Met Éireann, especially in the north, which means verifying against ERA5-Land can make the forecasts look cold-biased when they're actually fine. And the seasonal system runs warmer than the subseasonal — which is what the spatial bias maps on the next slide confirm."

### Why this slide earns its place

Without it, the spatial bias slide raises questions the audience can't answer:
- "Why did you use two references?" — because ERA5-Land has its own biases.
- "Is that cold bias in the north real or a reference problem?" — reference problem, as this slide shows.
- "Why is the seasonal system warmer?" — visible here before it's quantified spatially.

The t2m chain doesn't just show "forecasts smooth the gradient." It sets up the methodology: dual references, awareness of reference bias, and the subseasonal–seasonal contrast. The spatial bias slide then lands cleanly because the audience already knows what to look for.

---

## Slide 5 narrative — spatial bias

### What's plotted

Bias of 2m temperature at Week 3. Gridded cells verified against ERA5-Land, station circles verified against Met Éireann. Four panels: Climatology, Subseasonal, Seasonal, Subseasonal − Seasonal.

### Reading order

Start with the two central panels (Subseasonal and Seasonal), then the difference panel on the right. The Climatology panel on the left is a baseline check (near-zero, as expected) — don't dwell on it.

### What you see

**Subseasonal panel:** Gridded cells are predominantly blue (cold-biased vs ERA5-Land), especially inland. But the station circles are close to zero. The subseasonal is near Met Éireann — accurate — but looks cold against ERA5-Land because the reference is warm. This is exactly what the t2m chain slide predicted.

**Seasonal panel:** Gridded is more mixed — less blue, some warm patches. Station circles shift slightly warm. The seasonal has a genuine warm bias against both references. Again, consistent with the t2m chain showing the seasonal running warmer.

**Difference panel (Subseasonal − Seasonal):** Blue everywhere in the grid: subseasonal is cooler than seasonal across the domain. Crucially, the station circles are also blue. Since subseasonal ≈ Met Éireann (near-zero bias), the blue station circles mean the seasonal overshoots observations. The warm bias in the seasonal is real, not a reference artefact.

### The two-slide story

| Slide | Finding | Method |
|-------|---------|--------|
| t2m chain | ERA5-Land runs warm; seasonal runs warmer than subseasonal | Visual comparison at 4 stations |
| Spatial bias | Subseasonal cold bias vs ERA5-Land is a reference artefact; seasonal warm bias is genuine (confirmed by both references) | Gridded + station verification |

The second slide doesn't just repeat the first — it *resolves* it. The t2m chain raises the question "is the subseasonal cold or is ERA5-Land warm?" The spatial bias answers it: ERA5-Land is warm (station circles near zero), and the seasonal is genuinely warm-biased (station circles also confirm).
