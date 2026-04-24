# Maths PhD Seminar: Script

### 1. Title (~30s)

[slide title: Subseasonal-to-seasonal forecasting of drought-to-flood transitions]

Hi, I'm Lainey, I'm about three months into my PhD research in the Decarb-AI Centre. My research is in subseasonal-to-seasonal weather forecasting. I'm looking at whether we can forecast drought-to-flood transitions at that range, and whether atmospheric regimes and machine learning can help.

[~45 words, ~20s]

---

### 2. What happens when drought turns into flood? (~2.5 min)

[click — soil mechanism visual]

So what even is a drought-to-flood transition? It's where you have a long dry spell — say on agricultural soil. [put hand over dry soil image] This makes the soil hydrophobic so that when a rain event happens, the rain runs right off and you get flooding that's worse than if the drought had never happened. And this has big consequences for things like water management and agriculture management. 

A study by Matanó found that a quarter of all floods globally are preceded by a drought or overlap with one.

And Yang looked at thirteen thousand of these events in US streamflow records and found that transitions take about six weeks on average, with faster cases under a month.

So these events have big impacts, are common, and they happen over around 4-8 weeks.

On that note, quick show of hands. Who here has any idea what the weather's going to be like in 4-8 weeks?

[pause] Are you guessing? Are you hoping?

That range is genuinely hard to predict, and because of that you don't hear about it. But it's exactly the range where these transitions play out.

[~250 words, ~105s]

---

### 3. Why is this so hard to forecast? (~2.5 min)

[click — Mariotti figure with regime-transition schematic]

So why is this so hard to forecast? This range actually has a name subseasonal-to-seasonal, or S2S. It has a nickname: the predictability desert.

It comes down to where forecast skill comes from. Short-range weather forecasting is an initial condition problem. You know what the atmosphere looks like right now, you put that into a model and run it forward. But the atmosphere is chaotic, so small errors in those initial conditions grow, and after about ten days you've lost predictable signal.

Seasonal forecasting is a completely different kind of problem. It's a boundary condition problem. Skill comes from slow things like sea surface temperatures that take months to evolve. But at S2S timescales, the ocean hasn't had enough time to move away from its initial state to provide predictability.

The S2S window sits right in between these two. That's why it's called the predictability desert.

That's not to say there's no skill here. It's intermittent.

 When a strong atmospheric pattern, also called a weather regime, is active, like a persistent high-pressure system that sits over a region for weeks, the forecast system has something large-scale and slow-moving to track. These examples on the right show what they look like. But they're not always active, and some are more predictable than others. Also, when no strong regime is in play, you're back in the desert.


[~260 words, ~110s]

---

### 4. What causes these transitions? (~2 min)

Earlier I described what happens at ground level but what's actually happening in the atmosphere to cause that sequence?

[click — regime-transition schematic]

The best example is a case study of California in 2022-23 — that's what the panels below show. On the left, persistent blocking is in place and no rain over California. Then in the middle panel, the blocking breaks down —  and a sequence of atmospheric rivers moves in. These are large plumes of moisture, and you can see the rain starting to arrive. On the right, heavy rain is hitting preconditioned dry soil. Basically California went from extreme drought to really really bad flooding in a few weeks.

A study by Parry found the same mechanism in Britain and Ireland for half of all drought terminations. Their key insight was that if you want to predict when a drought ends, you may be better off predicting the shift in the atmospheric pattern than predicting rainfall directly. So that raises the question —

[~250 words, ~110s]

---

### 5. Where's the gap? (~1.5 min)

[click — research gap slide]

So where does that leave us? There are three research areas here — S2S forecasting, weather regimes, and drought-to-flood transitions.

Up here — we know that weather regimes are predictable at S2S timescales. Forecast centres already predict these patterns weeks ahead. That's established.

Over here — we know that regimes drive these transitions. Like the 2 studies I showed on the previous slide. 

But down here — nobody has tested whether S2S forecasts can predict the transitions themselves. Drought and flood have each been forecast separately at this range, but the entire literature on transitions is retrospective. Every study looks backwards. A forecaster today who wanted to assess drought-to-flood risk would have to check separate products for drought and flood and connect the dots themselves.

And in the centre — nobody has connected all three. That's my research question: can we forecast these transitions, and does the regime tell us when?

[~170 words, ~75s]

---

### 6. How do I test this? (~2.5 min)

[click — pipeline slide]

Here's what that pipeline looks like, and I'll be testing this on Irish catchments.

You start with a raw S2S forecast — in my case from ECMWF, the European weather centre. Then you translate that forecast into what actually matters on the ground. For drought and flood, that could be streamflow for example — how much water is flowing through a catchment. So the next step is a hydrological model that converts the forecast into streamflow.

From streamflow, you detect drought and flood events separately. Then you look for transitions — cases where a drought episode is followed by a flood episode within a certain window.

Once you have that, you can verify — does the pipeline actually work? And critically, does it work better in some atmospheric states than others? That's regime conditioning. If skill is concentrated in certain regime states, that's the signal that there's something usable there — something an operational product could eventually be built on.

Separately, I want to test whether machine learning can improve each stage of this pipeline — for example, replacing the hydrological model itself so that non-linear relationships can be learned, or using regime information as an additional input.

If the skill is there, the end goal would be a forecast product for farmers. Something like: this catchment is in drought. The regime forecast shows blocking breaking down in weeks 3 to 4. Based on similar historical setups, there's an above-normal chance of a drought-to-flood transition in weeks 4 to 6.

So that's the pipeline. But there's a catch — how do you actually detect these events?

[click — global map slide]

This map shows the studies I've reviewed so far on drought-to-flood transitions. The colours are different terminology — you'll see "drought-flood abrupt alternation" in China, "hydrological whiplash" in the US, "drought-to-flood transition" in Europe. They're studying the same phenomenon but using different names.

More importantly, the shapes represent what variable they're actually using to detect the transitions. One study compared rainfall-based and streamflow-based approaches and found they give opposite frequency trends over the same period. Another tried multiple methods on the same data and missed five out of eight known impactful events.

[~320 words, ~140s]

---

### 7. Conclusions

Before I conclude — are there any questions?

[take questions]

[click — takeaway slide]

Just to remind you of the 3 main takeaways:

- Drought-to-flood transitions are common, damaging, and play out over the S2S window.
- The regime shifts that drive them are predictable at this range.
- Nobody has tried to forecast drought-to-flood transitions. That's what I hope to do.
Thanks.

[~50 words, ~20s]

---

[Total: ~1310 words of spoken content, ~560s at 140 wpm. With pauses, clicks, show of hands, and Q&A: ~15–17 min.]

























## Objective
Give a 17-minute talk that takes the audience from "what happens when drought turns into flood?" to "here's how atmospheric patterns might make that forecastable, and here's the pipeline I'm building to test it." Audience: PhD students in maths, AI, physics, not weather specialists.

## Core message
The atmospheric patterns that cause drought-to-flood transitions are partially predictable at S2S lead times. Nobody has tested whether that translates into event-level forecast skill. This PhD builds the pipeline to find out.

---
