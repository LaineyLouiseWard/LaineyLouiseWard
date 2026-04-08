# Title

Thanks everyone for coming. I'm Lainey, and just to remind you Abdollah, I'm based in the Decarb-AI Centre. I did my masters in Atmosphere, Ocean and Climate, and I did my undergrad in physics here in UCD.

Over the next ten minutes I'll bring you through three things. First, what my literature review found and how that shaped my research question. Then, what I've actually done so far in terms of my first paper. And finally the admin bits like: credits and conferences. 

# What Is the Prediction Gap?
My research starts from this idea that there's a prediction gap in weather forecasting. You're all familiar with short-range weather forecasting, and with seasonal forecasting. The period in between is the subseasonal-to-seasonal window, or S2S, which is about two to ten weeks ahead.

Skill is intermittent in this range because the skill from initial conditions has decayed by this point,
and slower influences like ocean temperatures aren't yet strong enough at S2S

But this is exactly when important decisions need to be made — agriculture, water management, energy management, especially in response to multi-hazards. 

A good example is drought-to-flood event. A drought hardens the soil, so when heavy rain follows, the water runs off and causes worse flooding than it would have otherwise. Matanó et al. found that a quarter of all floods globally follow or overlap with drought. 

For this reason, first paper is focusing on drought-to-flood transitions.

I'll tell you what the literature says on that.

# What Does the Literature Say?

The literature operates at two levels.

In the vast majority of the literature, only really looked at S2S so far, flood and drought are considered as entirely separate events, with different drivers and mechanisms. 

The studies that do look at them together, only do so retrospectively, understand the propoerties,
— how often do they co-occur, how intense is the alternation, what timescales do they happen at. But that's all done with observations and reanalysis, not forecasts.

The natural next step would be to try to predict these events using a forecast. However, it's not that simple — there's a pipeline that needs to be built, and you can see the steps on the right.

First, I need to choose a forecast system. ECMWF runs two, a subseasonal and a seasonal, and nobody has compared them at S2S timescales over Ireland.

Then I need to translate those forecasts into impact variables like streamflow, because the forecast doesn't produce that directly. Hydrological models can do this, and machine learning is increasingly being used here too.

From there I need to detect the events themselves. There are two main bodies of work on this — the American and European literature tends to detect drought and flood episodes separately and link them by time proximity, while the Chinese literature uses a single index. Neither has been applied to Irish catchments.

And finally I need to understand when skill emerges. At S2S timescales, that means conditioning on the atmospheric state when the forecast is initialised.

None of the studies I've read has checked whether useful skill actually survives that full chain.

# Research Arc

So from all of that, my two research questions are:

First, how does prediction skill at S2S lead times compare across forecast variables, impact variables, and multi-hazard events? And second, under what atmospheric conditions does that skill emerge?

I'm addressing these across three papers, each covering a different type of multi-hazard event. Paper 1 is drought-to-flood transitions. I'm hoping that Hafssa will be a coauthor on this, because she'll have more expertise on the machine learning in hydrology.

Paper 2 will focus on renewable energy source droughts, where low wind, low solar, and high demand coincide. I'm hoping I'll be able to collaborate with Boris on this.

And Paper 3 will be shaped by my involvement in the ANTICIPATE COST Action, a European research network on S2S prediction and multi-hazards.

The roadmap on screen shows how Paper 1 maps out. I'm currently at the first level, met skill.

So where am I on this?

# Subseasonal vs Seasonal

The first step is choosing which forecast system to build on. The reason this isn't straightforward is that ECMWF's subseasonal system has newer physics, better initial conditions, and it's initialised almost every other day. The seasonal system has older physics but more than double the ensemble size and a much longer record. One samples more in time, the other samples more across ensemble members.

I've compared both over a common 10-year period, on a 0.3 degree grid over Ireland, for three variables so far, but I'm only going to show 2-metre temperature today. I'm verifying these forecasts against both Met Éireann station observations and ERA5-Land reanalysis.

For the station verification, I just took the nearest-neighbour land grid point for simplicity.

# Observation–Forecast Temperature Chain

S2S verification works with weekly means, so here I've plotted mean weekly-mean 2m temperature at Week 3, for both references and both forecasts.

ERA5-Land tends to run warm compared to Met Éireann. You can see it at the upper stations: they're cool blue in Met Éireann but shift to orange in ERA5-Land. That matters because verifying the forecasts against ERA5-Land can make them look cold-biased when they're actually close to the station observations. That's why I verify against both.

The other thing to notice is the seasonal system runs warmer than the subseasonal.

# Spatial Verification

Here I'm showing bias spatially, with ERA5-Land as the gridded reference and Met Éireann station values in the circles.

Look at the subseasonal panel. Against ERA5-Land, lots of blue — looks cold-biased. But the station circles are close to zero. So that cold bias is exaggerated by ERA5-Land being warm.

Now look at the difference panel. Blue everywhere — the seasonal runs warmer than the subseasonal, and the station circles are blue too. So the seasonal warm bias we saw on the previous slide holds against both references.

This is one metric, one variable, one lead time. I need to see how these systems compare across RMSE, ACC, all three variables, and different lead times before I can say which system is better for my purposes.

What about training and development?

# Training & Development

I have 10 credits from two completed modules, with AI for Time Series planned for Spring 2027 and RPL pending, which brings me to 30.

All training is done: research integrity, HPC, the Ark presentation course, and the DestinE machine learning course.

The timeline shows what's coming. This week I'm presenting at the Mathematics PhD Seminar. Then both ANTICIPATE COST Action meetings in April, Glasgow and Lausanne. In May I have a poster at the Met Éireann Research Showcase, and I'm targeting a submission to Remote Sensing by end of May where I'm first author. Then the EMS Annual Meeting in September, followed by RSP2.

The dashed items on the right are things I'd like to do in 2027 but aren't confirmed yet: a COST short-term scientific mission, a summer school, and potentially the S2S2D Conference and EMS again.

I'm also the School of Maths postgrad representative, so I organise biweekly PhD research seminars and I'm presenting at one this week. I'm also organising a research symposium soon, and I've started a postgrad blog which I'm launching at the seminar.
