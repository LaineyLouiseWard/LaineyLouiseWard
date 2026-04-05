# Maths PhD Seminar — Script

## Objective
Give a 17-minute talk that takes the audience from "why can't we predict weather a few weeks out?" to "here's the pipeline I'm building and where machine learning fits." Audience: PhD students in maths, AI, physics, not weather specialists.

## Core message
We can forecast temperature and rainfall a few weeks ahead with some skill. Nobody has tested whether that skill survives when the target becomes a drought turning into a flood. My research builds the pipeline to find out, and asks whether machine learning can help at each stage.

---

### 1. Hook (~2 min)

Hi, I'm Lainey. Over the next fifteen minutes I'm going to explain why and how I'm looking for an oasis in something called the predictability desert, where and when there's useful skill in S2S forecasts for multi-hazard events like droughts and floods.

Quick show of hands. Who here has any idea what the weather's going to be like in three weeks?

[pause]

Yeah, no one. But that time period, about two to six weeks ahead, is where a lot of high-stakes decisions get made. Agriculture, energy, water management. Forecasts of temperature and rainfall exist at that range, but a farmer can't act on those alone when the real question is whether a drought is about to become a flood.

[click]

Picture a farmer in the middle of a long dry spell. The soil has gone really hard. When the rain finally comes,  instead of the water soaking in, it runs off and causes flooding. The flooding is worse because of the drought that came before it. One hazard made another hazard worse. Ideally you'd want to warn that farmer before the rain arrives.

[click]

This is why the S2S timeframe has been given the nickname the predictability desert. I want to find out if there's an oasis in it, pockets of skill in predicting these events.

[~190 words, ~80s]

---

### 2. The prediction gap (~2.5 min)

[click — Mariotti figure]

Why is this window so hard to predict? It really comes down to what's giving you skill in the first place.

For short-range weather forecasts, you know what the atmosphere looks like right now. You put that into a model and run it forward. It's an initial conditions problem, and for a few days it works well. But the atmosphere is chaotic, and those initial conditions lose their value quickly.

Seasonal forecasts are a completely different game. You're not trying to predict specific weather on a specific day. You're predicting whether the coming season will be wetter or warmer than average, and that's driven by slow-moving things like ocean temperatures. Those are boundary forcings, and they take months to evolve, so they give you something to hold on to.

The subseasonal-to-seasonal window, S2S, sits right between these two. The initial conditions have lost most of their usefulness, but the ocean and land surface haven't had enough time to steer the statistics yet. You're between two sources of skill, and neither one is doing much for you. That's why it's a desert.

[click]

But here's why it matters. Matano and colleagues looked at over eight thousand catchments globally and found that a quarter of all floods follow or overlap with drought conditions. These connected events aren't rare, and they happen at exactly the timescale where forecasts are weakest. So what does the literature say about predicting them?

[~250 words, ~110s]

---

### 3. Three literatures, one gap (~2.5 min)

[click — Venn diagram]

When I started the literature review, I found three separate research communities working around this problem, mostly in isolation.

First, S2S forecasting. People who build and verify forecasts at this timescale. They've made real progress on predicting individual variables, temperature, rainfall, wind, but they haven't pushed into multi-hazard events.

Second, multi-hazard research. People studying what happens when hazards combine or follow each other. Drought then flood, or low wind and low solar hitting the energy grid at the same time. There's a lot of work here, but it's all diagnostic. How often do these events occur, how intense are they, what timescales do they happen at. All from long observational records, not forecasts.

Third, weather regimes. Large-scale atmospheric patterns, like blocking, that determine what weather a region gets. There's evidence that forecast skill depends on which regime is active when the forecast starts, and that rapid shifts between regimes can trigger drought-to-flood transitions on the ground. But nobody has used that to predict a transition in a forecast.

[click]

Where each pair of circles overlaps, there's partial work. But the centre, where all three meet, is empty. Can S2S forecasts predict multi-hazard events, and does that skill depend on the atmospheric state? That's the thesis. But before you can predict these events, how do you even detect them?

[~230 words, ~100s]

---

### 4. How do you detect these events? (~1.5 min)

Before you can predict a drought-to-flood transition, you have to define what counts as one. And there are actually different schools of thought on this.

One approach comes mainly from Chinese hydrology, where monsoon basins see a dry spring followed by a wet summer in the same year. They developed indices that compress the whole swing, how far the variable moved, how fast, into a single number. Purpose-built for that kind of seasonality.

The other approach, more common in Western hydrology, is simpler. You detect drought episodes and flood episodes independently using standard indicators, then link them if they happen close enough together in time. The parameter that varies most across studies is how wide that linking window is.

I'm using episode-linking. The assumptions are transparent, and it plugs directly into how forecasts are verified. But the idea from the other tradition, that the swing itself is worth measuring, how far and how fast, that's worth keeping. Once you have the events, you can compute that.

[~170 words, ~75s]

---

### 5. Pipeline and research questions (~2 min)

[click — roadmap]

So that brings me to my two research questions. First: how does prediction skill at S2S lead times compare across forecast variables, impact variables, and multi-hazard events? And second: under what atmospheric conditions does that skill emerge?

The way I'm addressing this is through a pipeline. You start with the raw forecast, temperature, precipitation, and you verify that against observations. That's meteorological skill, and it's where the literature already has a foothold. Then you translate those forecasts into impact variables, things like streamflow, which is what matters for drought and flood on the ground. That's a second verification step. Then you apply event detection to identify the transitions themselves. And you verify again. Each stage can gain or lose skill, and nobody has measured that chain from forecast to event.

On top of that sit two more layers. Regime conditioning: does skill depend on which atmospheric pattern is active at the time of the forecast? And machine learning: can it add value at any stage?

I'm addressing this across three papers. The first focuses on drought-to-flood transitions. The second will look at renewable energy source droughts, where low wind and low solar coincide. The third is still being shaped through a European research network I'm part of called ANTICIPATE.

[~220 words, ~95s]

---

### 6. Where machine learning enters (~3 min)

[click]

Where does ML fit in this pipeline? It shows up in three places, and they're quite different problems.

First, post-processing. S2S forecasts have systematic biases. They might consistently overestimate rainfall in winter, or underestimate temperature variability. Traditional post-processing uses statistical methods to correct these. ML can potentially capture nonlinear bias structures that statistical corrections miss. That sits right at the start of the pipeline, at the bias correction stage.

Second, you can augment or replace the hydrological model. You have a precipitation forecast and you want to turn it into streamflow. Hydrological models have done this for decades with physical equations, water balance, routing, infiltration. But in the last few years, LSTMs have started matching or beating them. Kratzert and colleagues showed this in 2018. It's a sequence-to-sequence problem: you feed in a time series of atmospheric inputs and the model learns to produce streamflow. These models are picking up physical relationships, storage, lag, nonlinear response, from data, without being told the equations.

Third, you can bypass the hydrological model entirely. Instead of going forecast to hydro model to streamflow, you go straight from forecast fields to streamflow using machine learning. Recent work has shown this can outperform the dynamical models, but it tends to underestimate the severity at the extremes, which is exactly where it matters most for multi-hazard events.

Underneath all three of these sits regime conditioning. The idea is that whichever ML model you use, you provide the atmospheric regime state as an input. There's evidence that post-processing skill varies depending on which regime is active when the forecast starts, and that regime shifts can make transitions predictable at two to three week lead times. And explainable AI matters here too. A forecast that says "transition likely" is not much use if you can't say what's driving the confidence.

[~300 words, ~130s]

---

### 7. Current progress (~2 min)

[click — system comparison]

Where am I on this? The first step was choosing which forecast system to build on. ECMWF runs two: a subseasonal system and a seasonal system. The subseasonal one has newer physics and is initialised almost every other day, 183 times a year. The seasonal one has older physics but more than double the ensemble size and a much longer record. One gives you more snapshots in time, the other gives you more members per snapshot.

I've compared both over a common ten-year period on a grid over Ireland, looking at temperature, precipitation, and wind speed. The reference datasets are Met Eireann station observations and ERA5-Land reanalysis.

The deterministic verification is done. Next is probabilistic verification, Brier skill score, CRPSS, which is about to get underway. Getting the deterministic foundations right first matters because everything downstream builds on it.

[~150 words, ~65s]

---

### 8. Close (~1 min)

I'll wrap up in a second, but does anyone have any questions first?

[Q&A]

[click — Conclusions slide]

Okay, so, back to our farmer. Could we warn them three weeks out that the drought is about to become a flood? Not yet. But now we know which forecast system to build on, and the next step is translating that forecast through impact variables and into the events themselves. Skill can leak at every step in that chain, but machine learning might recover some of it. That's the bet, and I think it's a good one.

[~75 words, ~30s]

---

[Total: ~1595 words of spoken content, ~680s at 140 wpm. With pauses, clicks, and audience interaction: ~17 min.]
