# Maths PhD Seminar: Script

## Objective
Give a 17-minute talk that takes the audience from "what happens when drought turns into flood?" to "here's how atmospheric patterns might make that forecastable, and here's the pipeline I'm building to test it." Audience: PhD students in maths, AI, physics, not weather specialists.

## Core message
The atmospheric patterns that cause drought-to-flood transitions are partially predictable at S2S lead times. Nobody has tested whether that translates into event-level forecast skill. This PhD builds the pipeline to find out.

---

### 1. Title (~30s)

[slide title: Forecasting drought-to-flood transitions at subseasonal timescales]

Hi, I'm Lainey, I'm about three months into my PhD research in the Decarb-AI Centre. My research is in subseasonal-to-seasonal weather forecasting. I'm looking at whether we can forecast drought-to-flood transitions at that range, and whether atmospheric regimes and machine learning can help.

[~45 words, ~20s]

---

### 2. What happens when drought turns into flood? (~2.5 min)

[click — soil mechanism visual]

So what even is a drought-to-flood transition? It's where you have a long dry spell — say on agricultural soil. [put hand over dry soil image] This makes the soil hydrophobic so that when a rain event happens, the rain runs right off and you get flooding that's worse than if the drought had never happened.

A study by Matanó et al. found that a quarter of all floods globally follow or overlap with a drought. And Yang et al. looked at thirteen thousand of these events in US streamflow records and found that transitions take about six weeks on average, with faster cases under a month.

So these events are common, they're damaging, and they unfold over a timescale of weeks.

On that note, quick show of hands. Who here has any idea what the weather's going to be like in 3-6 weeks?

[pause] Are you guessing? Are you hoping?

That range is genuinely hard to predict, and because of that you don't hear about it. But it's exactly the range where these transitions play out.

[~165 words, ~70s]

---

### 3. Why is this so hard to forecast? (~2.5 min)

[click — Mariotti figure with regime-transition schematic]

So why is this so hard to forecast? This two-to-six week range is called the subseasonal-to-seasonal window, or S2S. It has a nickname: the predictability desert.

Why? It comes down to where forecast skill comes from. Short-range weather forecasting is an initial condition problem. You know what the atmosphere looks like right now, you put that into a model and run it forward. For a few days, it works well. But the atmosphere is chaotic, so small errors grow, and after about ten days those initial conditions have lost most of their value.

Seasonal forecasting is a completely different kind of problem. It's a boundary condition problem. Skill comes from slow things like sea surface temperatures that take months to evolve. You're not predicting specific weather. You're predicting whether the coming season will be wetter or warmer than average.

The S2S window sits between these two. The initial conditions have lost most of their value, and the ocean hasn't had time to steer the statistics yet. You're between two sources of skill, and neither one is doing much for you.

But skill isn't zero everywhere in this range. When a strong atmospheric pattern is active, like a persistent high-pressure system sitting over a region for weeks, the forecast system has something large-scale and slow-moving to track. These patterns are called weather regimes. But they're not always active, and some are more predictable than others. When no strong regime is in play, you're back in the desert.

So there is a source of skill at S2S timescales, and it comes from large-scale atmospheric patterns. Why does that matter for drought-to-flood transitions?

[~260 words, ~110s]

---

### 4. What causes these transitions? (~2 min)

So what causes these transitions? Earlier I described what happens at ground level. Now the question is: what's happening in the atmosphere to cause that sequence?

[click — regime-transition schematic]

Some of these weather regimes are the physical drivers of drought-to-flood transitions. A persistent blocking system sits over a region and suppresses rainfall for weeks. Soil moisture drops. Then that blocking breaks down, the atmospheric flow shifts, and moist Atlantic air moves in. Heavy rain hits preconditioned dry soil.

There's good evidence for this from two different studies. A study from Maynooth looked at how droughts end across Britain and Ireland, using really long river records. They found that over half of all drought endings were preceded by surges of atmospheric moisture linked to a shift in the large-scale pattern. They suggested that forecasting these patterns might be more useful than forecasting rainfall for predicting when droughts end, but didn't test it.

DeFlorio and colleagues looked at the same kind of sequence in California in 2022-23. Persistent blocking held the drought for months, then a sequence of atmospheric rivers — large plumes of moisture — broke it and caused catastrophic flooding. When they evaluated the S2S forecasts, the system had skill in predicting the atmospheric rivers weeks ahead, because it could track the large-scale pattern that was steering them.

Both of these studies are looking backwards at what happened. Neither tested whether a forecast system could have predicted the transition in advance.

[~250 words, ~110s]

---

### 5. Where's the gap? (~1 min)

[click — research gap slide]

So where does this leave us?

We know that weather regimes drive these transitions. And we know that regimes are predictable at S2S timescales. But nobody has tested whether you can actually predict the transitions themselves using a forecast system — and whether knowing the regime helps.

My research question is: can S2S forecasts, informed by the atmospheric regime, predict drought-to-flood transitions?

[~100 words, ~45s]

---

### 6. How do I test this? (~2.5 min)

[click — pipeline slide]

Here's what that pipeline looks like, and I'll be testing this on Irish catchments.

You start with the raw S2S forecast — temperature, precipitation, wind. The first thing I need to do is choose which forecast system to build on. ECMWF runs two systems whose lead times overlap at this range: a subseasonal system and a seasonal system. They differ in how many simulations they run and how often they're updated. So I'm comparing both over Ireland, verified against Met Eireann station observations and a global reanalysis dataset, to decide which one to take forward.

[click — system comparison slide]

From the chosen system, you need to translate the forecast into what actually matters on the ground. For drought and flood, that's streamflow — how much water is flowing through a catchment. So the next step is a hydrological model that converts the forecast into streamflow.

From streamflow, you detect drought and flood events separately. Then you look for transitions — cases where a drought episode is followed by a flood episode within a certain window.

Once you have that, the key question is: does the skill depend on the atmospheric state? If the system is better at predicting transitions during blocking events than when no strong pattern is active, that tells you when to trust the forecast and when not to. That's regime conditioning — it doesn't change the forecast, it tells you when the forecast is worth listening to.

Separately, I want to test whether machine learning can improve each stage of this pipeline, especially when it has the regime information as an input.

In the Decarb-AI programme we're encouraged to think about innovation and end use of our research. So if the skill is there, I'd hope to work towards a forecast product for farmers. Something like: this catchment is in drought. The regime forecast shows blocking breaking down in weeks 3 to 4. Based on similar historical setups, there's an above-normal chance of a drought-to-flood transition in weeks 4 to 6.

[~290 words, ~125s]

---

### 7. Conclusions

Before I conclude — are there any questions?

[take questions]

[click — takeaway slide]

Just to remind you of the 3 main takeaways:

- Drought-to-flood transitions are common, damaging, and unfold over the S2S timescale.
- The atmospheric patterns that cause them are the same ones that give S2S forecasts their skill.
- Nobody has tested whether you can use those regimes to predict drought-to-flood transitions. That's what this PhD does.
Thanks.

[~50 words, ~20s]

---

[Total: ~1160 words of spoken content, ~500s at 140 wpm. With pauses, clicks, show of hands, and Q&A: ~15 min.]
