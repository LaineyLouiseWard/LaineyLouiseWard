# What I Have Done — Script

## Objective
Show the panel what the literature review produced: a clear diagnosis of where the field stops, and the thesis question that emerges from it.

## Core message
The literature can predict drought and flood separately, and can characterise their joint behaviour historically. But nobody asks whether forecast skill for individual variables actually carries through when the target becomes a multi-hazard event. That comparison, met skill vs impact skill vs event skill, is what the thesis tests.

---

### Slide 1 — The Prediction Gap

You're all familiar with short-range weather forecasts, and seasonal outlooks. The period in between, two weeks to two months ahead, you might not be as familiar with. That's the subseasonal-to-seasonal timescale, or S2S. It's where forecast skill is lowest, but it's also where decisions about multi-hazards like floods, droughts, and wildfires actually have to be made.

My research focuses on multi-hazard events at this timescale, starting with drought-to-flood transitions. [click] A drought dries out the soil, so when heavy rain follows the water doesn't seep in as much and you get more flooding. The flood is worse because the drought came first. Neither event needs to be extreme on its own, but because they are connected in time the overall impact can be.

These transitions aren't rare either. Matanó et al. analysed over eight thousand catchments globally and found that a quarter of all floods follow or overlap with drought conditions. Closer to home, Parry et al. studied 354 catchments across the UK and Ireland and found that more than half of drought terminations are driven by pulses of atmospheric moisture transport, particularly under positive NAO. So we have an idea of the drivers, and we know it happens here. What we don't know is whether a forecast can see it coming.

So what did the literature review find?

[~70s, ~180 words]

---

### Slide 2 — Where Does the Literature Stop?

The literature operates at two levels. [click] First, drought and flood are predicted as separate events, each extreme on its own. [click] Second, studies characterise the joint behaviour, but only retrospectively (Rashid and Wahl, 2022; Anderson et al., 2025). How often do droughts and floods co-occur, how intense is the alternation between them, what timescales do they happen at. But that's all done with long observational records, not forecasts.

[click] The natural next step would be to apply those same methods to a forecast, but it's not that simple. Forecast systems produce meteorological variables like temperature and precipitation. They don't produce impact variables like streamflow. So to get from a forecast to a drought-to-flood event, you need to translate the forecast into impact variables first, and then apply event detection on top of that. Each of those steps can lose or gain prediction skill, and nobody has checked whether useful skill actually survives. Co-occurring compound extremes have been predicted at subseasonal timescales (Malik and Mishra, 2025), but temporally compounding events remain untested beyond a single case study (DeFlorio et al., 2024).

[click] So there's a chain of work that needs to happen first.

[click] I need to know which forecast system to build on. ECMWF runs two systems, a subseasonal and a seasonal one, and nobody has compared them at weekly timescales for S2S analysis.

[click] I need to translate those forecasts into impact variables like streamflow. Hydrological models can do this, and machine learning is increasingly being used here too (e.g. Kratzert et al., 2018; Dong et al., 2025).

[click] I need to define what counts as a drought-to-flood event in Irish catchments. Joint indices exist for this, mainly from Chinese hydrology, but they haven't been applied outside that context or adapted for forecasts.

[click] And I need to know when skill emerges. At S2S timescales, that depends on the atmospheric state when the forecast is initialised.

[~150s, ~290 words]

---

### Slide 3 — Research Arc

So this brings me to my two research questions. First, how does prediction skill at S2S lead times compare across forecast variables, impact variables, and multi-hazard events? And second, under what atmospheric conditions does that skill emerge?

I aim to address these across three papers, each covering a different type of multi-hazard event (Zscheischler et al., 2020). Paper 1 is drought-to-flood transitions, which is what I've been describing, a temporally compounding multi-hazard. Paper 2 follows the same approach for renewable energy source droughts, which are multivariate, where low wind, low solar, and high demand coincide. And Paper 3 will be shaped by my involvement in the ANTICIPATE COST Action, which is a network that brings together researchers across S2S prediction and multi-hazards.

The roadmap on screen shows how Paper 1 maps out. I'm currently at the first level, met skill.

So where am I on this?

[~30s, ~75 words]
