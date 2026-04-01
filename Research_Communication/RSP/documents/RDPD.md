I will need to fill this out online

Lainey Ward
Decarb AI, School of Civil Engineering
Primary supervisor: Fiachra O'Loughlin
Co-supervisor: Conor Sweeney


Record of ongoing research - up to 3000 characters
Please provide updates of your research progress

Subseasonal-to-seasonal (S2S) forecasts cover 2 weeks to 2 months ahead. This range is sometimes called the predictability desert, because weather skill has decayed but seasonal signals have not yet emerged. My literature review covers S2S forecast systems, sources of skill, multi-hazard event frameworks, and how machine learning is being used across these areas. Drought-to-flood transitions have been studied in parallel by separate communities under names such as hydrological whiplash and drought-flood abrupt alternation. This existing coverage makes these transitions a natural starting point. They are a multi-hazard because drought conditions can harden the soil, so rainfall that follows is more likely to cause flooding. However, existing research on these events is largely diagnostic and focuses on characterising their frequency, intensity, duration, and onset from historical observations and reanalysis (Rashid & Wahl, 2022; Anderson et al., 2025) rather than forecasting them. Subseasonal prediction has been demonstrated for co-occurring compound hot-dry extremes (Malik et al., 2025), but temporally compounding events like drought-to-flood transitions remain untested at S2S timescales. The closest evidence is DeFlorio et al. (2024), who evaluated subseasonal forecasts for California's 2022/23 drought-to-flood case, but this is a single case study rather than a systematic verification. No study has tested whether skill for individual variables carries through to event-level skill for drought-to-flood sequences.

From this review, I have developed two research questions:
	1. How does skill at S2S lead times compare across forecast variables, impact variables, and multi-hazard events?
	2. Under what atmospheric conditions does this skill emerge?
    
I aim to address these across three papers, each covering a different type of multi-hazard event (Zscheischler et al., 2020): drought-to-flood transitions (temporally compounding), renewable energy source droughts (multivariate), and a third shaped by my participation in the ANTICIPATE COST Action (a network on S2S prediction and multi-hazards). Each paper will assess skill at three levels: variable skill, impact skill, and multi-hazard event skill.

I am currently working at the variable level, comparing ECMWF's subseasonal and seasonal forecasts over Ireland. The two systems differ in ensemble size, model physics, and initialisation frequency, so the comparison matches initialisation dates and extracts forecasts at 25 Irish stations. Forecasts are verified against ERA5-Land reanalysis and Met Eireann station observations. Deterministic verification (RMSE, Bias, ACC) is largely complete for temperature, precipitation, and wind speed at lead weeks 1 to 6. Probabilistic metrics are in progress. The two systems show near-identical per-init skill, meaning the subseasonal system's advantage is its denser temporal sampling (~183 vs 12 initialisations per year), not its model physics.


Future Plan - up to 3000 characters
Please provide updates of your research plan for the following year

Over the next year my focus is on Paper 1: drought-to-flood transitions, where a drought can precondition the land surface so that the flood that follows is worse. The goal is to trace S2S (2 weeks to 2 months ahead) forecast skill through three levels: meteorological variables, impact variables (streamflow), and multi-hazard events (drought and flood states, and transitions between them).

I will first extend the variable-level verification into streamflow. Evidence suggests that hydrological modelling is the main source of error when translating S2S forecasts into streamflow predictions (Dong et al., 2025), so I will likely replace the physics-based model with a data-driven approach such as an LSTM (Kratzert et al., 2018). The literature review identified three entry points where machine learning has been used along this chain — correcting the meteorological forecast, replacing the hydrological model, and learning the atmosphere-to-surface response directly — but none have been applied to multi-hazard events.

From streamflow I will move to event detection. No study has applied transition detection to Irish catchments (Meresa et al. (2023) study Irish drought but not transitions), and different threshold methods give substantially different results (Anderson et al., 2025), so testing event definitions on Irish data comes first. At S2S timescales, skill depends on the atmospheric state when the forecast starts, so conditioning on weather regimes is part of the methodology throughout.

I will present a poster at the Met Eireann Research Showcase (May 2026) and initial results at the EMS Annual Meeting (September 2026). Paper 2 follows the same three-level approach for renewable energy source droughts, where simultaneous low wind and low solar radiation cause energy supply shortfalls. The ANTICIPATE COST Action, which connects extended-range prediction with multi-hazard research, will inform the third paper.


Credit Bearing Module Details (840 characters)
I have completed 10 credits through Physical Meteorology & Climate (ACM41070) and AI for Weather and Climate (STAT41130). I plan to complete AI for Time Series (COMP41850) in Spring 2027, which covers time series classification and regression using AI methods and is directly relevant to my research. I will apply for 15 credits via Recognition of Prior Learning at the first opportunity in September 2026, based on my MSc in Atmosphere, Ocean and Climate. The three modules together with RPL would meet the required 30 credits.

Recognition of Prior learning
I will apply for 15 credits of RPL in September 2026 based on my MSc in Atmosphere, Ocean and Climate (University of Reading). I have mapped MSc modules onto UCD Level 4 equivalents: Numerical Modelling of Atmospheres and Oceans (MTMW14) and Introduction to Numerical Modelling (MTMW12) map onto Data Science in Python (COMP41680). Climate Change (MTMG16) maps onto Human Impact on the Environment (AESC40390). Fluid Dynamics of the Atmosphere and Oceans (MTMW11) and Global Circulation of the Atmosphere and Oceans (MTMW20) map onto Mathematics of Sustainability and the Environment (ACM41010) and Mathematical Fluid Dynamics II (ACM40070).

Professional & Career Development Activities
Record of professional and career development modules / workshops / activities

I have completed UCD Research Integrity Training, Sonic HPC Cluster training, the DestinE Machine Learning for Earth Systems Modelling course, and the Ark Speaking and Training course. iScholar training under the Innovate for Ireland programme is planned for next academic year.

I am first and corresponding author on a paper being finalised for submission to Remote Sensing, developed from an AI Sandbox alongside ODOS Tech. I will present a poster at the Met Eireann Research Showcase (May 2026) and have submitted an abstract to the European Meteorological Society Annual Meeting (September 2026). I will give a flash talk at the UCD Earth Institute Earth Day event and present at the Mathematics PhD Seminar in April.

I am a member of the ANTICIPATE COST Action, which connects multi-hazard research with extended-range prediction. Working Group 1 focuses on sources of multi-hazard predictability, and Working Group 2 on linking multi-hazards with extended-range predictions. I am attending both COST Action meetings in April 2026 (Glasgow and Lausanne) and plan to apply for a Short-Term Scientific Mission and attend a COST summer school in 2027.

I am the School of Mathematics postgraduate representative and organise biweekly student-led research seminars and community events. I have created a postgraduate blog for researchers across the School of Maths, AIMSIR, and Decarb-AI. I teach and demonstrate in the School of Maths. I am a member of the Irish Meteorological Society and the Royal Meteorological Society. I was featured in the UCD School of Mathematics Women in Maths poster exhibition for International Women's Day.

Research Integrity Training
Please record any Research Integrity Training undertaken.
2000 characters
I completed the UCD Research Integrity Training via Brightspace.


Other Relevant Activities
Please provide any additional information not covered in the sections above.
3000 characters
As the School of Mathematics postgraduate representative, I organise biweekly research seminars to give PhD students practice communicating their work in a low-stakes setting. I have also created a postgraduate blog for researchers in the School of Maths, AIMSIR, and Decarb-AI, to encourage regular, informal research communication.
