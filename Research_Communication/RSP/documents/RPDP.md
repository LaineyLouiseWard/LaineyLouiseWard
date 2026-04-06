Lainey Ward
Decarb AI, School of Civil Engineering
Primary supervisor: Fiachra O'Loughlin
Co-supervisor: Conor Sweeney


Record of ongoing research - up to 3000 characters
Please provide updates of your research progress

Subseasonal-to-seasonal (S2S) forecasts cover 2 weeks to 2 months ahead. This range is sometimes called the predictability desert, because weather skill has decayed but seasonal signals have not yet emerged. My literature review covers S2S forecast systems, sources of skill, multi-hazard event frameworks, and how machine learning is being used across these areas. Drought-to-flood transitions have been studied in parallel by separate communities under names such as hydrological whiplash and drought-flood abrupt alternation. This coverage makes them a natural starting point. They are a multi-hazard because drought conditions can harden the soil, so rainfall that follows is more likely to cause flooding. However, existing research on these events is largely diagnostic and focuses on characterising their frequency, intensity, duration, and onset from historical observations and reanalysis (Rashid & Wahl, 2022; Anderson et al., 2025) rather than forecasting them.

Subseasonal prediction has been demonstrated for co-occurring compound hot-dry extremes (Malik et al., 2025), but temporally compounding events like drought-to-flood transitions remain untested at S2S timescales. The closest evidence is DeFlorio et al. (2024), who evaluated subseasonal forecasts for California's 2022/23 drought-to-flood case, but this is a single case study rather than a systematic verification. No study has tested whether skill for individual variables carries through to event-level skill for drought-to-flood sequences.

From this review, I have developed two research questions:
	1. How does skill at S2S lead times compare across forecast variables, impact variables, and multi-hazard events?
	2. Under what atmospheric conditions does this skill emerge?
    
I aim to address these across three papers, each covering a different type of multi-hazard event (Zscheischler et al., 2020): drought-to-flood transitions (temporally compounding), renewable energy source droughts (multivariate), and a third shaped by my participation in the ANTICIPATE COST Action (a network on S2S prediction and multi-hazards). Each paper will assess skill at three levels: met skill, impact skill, and multi-hazard event skill.

I am currently working at the met level, comparing ECMWF's subseasonal and seasonal forecasts over Ireland. The goal is to determine whether either system performs better at lead times of 3 to 9 weeks, given their differences in ensemble size, model physics, and initialisation frequency. Forecasts are verified at 25 Met Éireann stations against both observations and ERA5-Land reanalysis. Deterministic verification (RMSE, Bias, ACC) is largely complete for temperature, precipitation, and wind speed. Probabilistic verification will begin soon, after which I will move to impact-level verification.


Future Plan - up to 3000 characters
Please provide updates of your research plan for the following year

Over the next year my focus is on Paper 1, which evaluates S2S forecast skill for drought-to-flood transitions. The goal is to trace S2S (2 weeks to 2 months ahead) skill through three levels — meteorological variables, impact variables, and multi-hazard events — and then explore how machine learning could improve skill along this chain.

S2S forecast systems do not produce impact variables like streamflow directly, so I will first use a hydrological model to translate the meteorological forecasts into streamflow and then assess whether impact-level skill differs from met-level skill. From streamflow I will move to event detection, applying indices and thresholds, such as those developed for detecting drought-flood alternation, to identify drought-to-flood events. Studies of Irish catchments have examined droughts and floods separately (e.g. Meresa et al., 2023) but not transitions between them. Different detection methods also give substantially different results (Anderson et al., 2025), so comparing event definitions on Irish data comes first. At S2S timescales, skill depends on the atmospheric state when the forecast is initialised, so skill will be conditioned on weather regimes.

Once the physical chain is understood, I will apply machine learning to improve it. The literature review identified three ways machine learning has been used across different stages of the variable-to-hazard pipeline: post-processing the meteorological forecast, replacing the hydrological model, and learning the atmosphere-to-surface response directly. None have yet been applied to multi-hazard events. Studies have shown that hydrological modelling is the main source of error in this translation (Dong et al., 2025), so I will likely start by replacing the physics-based model with a machine learning model such as an LSTM (Kratzert et al., 2018) and comparing skill between the two approaches.

I am attending two international ANTICIPATE COST Action meetings this month and will present at the second. I hope to establish collaborations within the network that will inform my later papers and broaden my research. Next summer I plan to apply for a funded Training School or Short-Term Scientific Mission through the COST Action. I also plan to develop my research communication throughout the year, presenting posters at the Met Éireann Research Showcase (May 2026) and the European Meteorological Society Annual Meeting (September 2026), as well as smaller opportunities such as the UCD Earth Institute flash talk and the Mathematics PhD Seminar.



Credit Bearing Module Details (840 characters)
I have completed 10 credits through Physical Meteorology & Climate (ACM41070) and AI for Weather and Climate (STAT41130). I plan to complete AI for Time Series (COMP41850) in Spring 2027, which covers time series classification and regression using AI methods and is directly relevant to my research. I will apply for 15 credits via Recognition of Prior Learning at the first opportunity in September 2026, based on my MSc in Atmosphere, Ocean and Climate. The three modules together with RPL would meet the required 30 credits.

Recognition of Prior learning
I will apply for 15 credits of RPL in September 2026 based on my MSc in Atmosphere, Ocean and Climate (University of Reading). I have mapped MSc modules onto UCD Level 4 equivalents: Numerical Modelling of Atmospheres and Oceans (MTMW14) and Introduction to Numerical Modelling (MTMW12) map onto Data Science in Python (COMP41680). Climate Change (MTMG16) maps onto Human Impact on the Environment (AESC40390). Fluid Dynamics of the Atmosphere and Oceans (MTMW11) and Global Circulation of the Atmosphere and Oceans (MTMW20) map onto Mathematics of Sustainability and the Environment (ACM41010) and Mathematical Fluid Dynamics II (ACM40070).



Professional & Career Development Activities
Record of professional and career development modules / workshops / activities

I have completed UCD Research Integrity Training, Sonic HPC Cluster training, the DestinE Machine Learning for Earth Systems Modelling course, and the Ark Speaking and Training course. iScholar training under the Innovate for Ireland programme is planned for next year.

I am first and corresponding author on a paper being finalised for submission to Remote Sensing, developed through an industry collaboration with ODOS Tech as part of an AI Sandbox programme. To prepare for submission, I have studied several textbooks on scientific writing and publishing.

I am developing my research communication by presenting at several events this year. These include a poster at the Met Éireann Research Showcase (May 2026) and at the European Meteorological Society Annual Meeting (September 2026), a flash talk on my research at the UCD Earth Institute Earth Day event, and a talk at the Mathematics PhD Seminar in April.

I am a member of the ANTICIPATE COST Action, which connects multi-hazard research with extended-range prediction. Working Group 1 focuses on sources of multi-hazard predictability, and Working Group 2 on linking multi-hazards with extended-range predictions. I am attending both COST Action meetings this month and plan to apply for a funded Training School or Short-Term Scientific Mission next summer.

I am a School of Mathematics postgraduate representative and a member of the maths committee. I organise biweekly student-led research seminars and social events to give students a low-stakes environment to practise presenting. I have also created a postgraduate blog for researchers across the School of Maths, AIMSIR, and Decarb-AI. I teach and demonstrate in the School of Maths. I am a member of the Irish Meteorological Society and the Royal Meteorological Society. I was featured in the UCD School of Mathematics Women in Maths poster exhibition for International Women's Day.





Research Integrity Training
Please record any Research Integrity Training undertaken.
2000 characters
I completed the UCD Research Integrity Training via Brightspace.


Other Relevant Activities
Please provide any additional information not covered in the sections above.
3000 characters

References cited in Record of Ongoing Research and Future Plan:

Anderson, B. J., E. Muñoz-Castro, L. M. Tallaksen, A. Matano, J. Götte, R. Armitage, E. Magee, and M. I. Brunner, 2025: What is a drought-to-flood transition? Pitfalls and recommendations for defining consecutive hydrological extreme events. Hydrology and Earth System Sciences, 29, 6069–6092, https://doi.org/10.5194/hess-29-6069-2025.
DeFlorio, M. J., and Coauthors, 2024: From California's Extreme Drought to Major Flooding: Evaluating and Synthesizing Experimental Seasonal and Subseasonal Forecasts of Landfalling Atmospheric Rivers and Extreme Precipitation during Winter 2022/23. Bulletin of the American Meteorological Society, 105, E84–E104, https://doi.org/10.1175/BAMS-D-22-0208.1.
Dong, N., H. Hao, M. Yang, J. Wei, S. Xu, and H. Kunstmann, 2025: Deep-learning-based sub-seasonal precipitation and streamflow ensemble forecasting over the source region of the Yangtze River. Hydrology and Earth System Sciences, 29, 2023–2042, https://doi.org/10.5194/hess-29-2023-2025.
Kratzert, F., D. Klotz, C. Brenner, K. Schulz, and M. Herrnegger, 2018: Rainfall–runoff modelling using Long Short-Term Memory (LSTM) networks. Hydrology and Earth System Sciences, 22, 6005–6022, https://doi.org/10.5194/hess-22-6005-2018.
Malik, I., and V. Mishra, 2025: Sub-seasonal prediction of compound hot and dry extremes in India. Clim Dyn, 63, 191, https://doi.org/10.1007/s00382-025-07668-x.
Meresa, H., C. Murphy, and S. E. Donegan, 2023: Propagation and Characteristics of Hydrometeorological Drought Under Changing Climate in Irish Catchments. Journal of Geophysical Research: Atmospheres, 128, e2022JD038025, https://doi.org/10.1029/2022JD038025.
Rashid, M. M., and T. Wahl, 2022: Hydrologic risk from consecutive dry and wet extremes at the global scale. Environ. Res. Commun., 4, 071001, https://doi.org/10.1088/2515-7620/ac77de.
Zscheischler, J., and Coauthors, 2020: A typology of compound weather and climate events. Nat Rev Earth Environ, 1, 333–347, https://doi.org/10.1038/s43017-020-0060-z.
