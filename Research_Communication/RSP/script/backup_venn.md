# Backup — Where the Literature Review Sits (Venn Diagram)

## When to use
If the panel asks "how did you scope the review?", "what fields does this draw from?", or "where are the gaps?"

---

### The three literatures

My review sits across three areas. S2S forecasting, which is about predicting weather two weeks to two months ahead. Multi-hazard events, which is about what happens when hazards occur in sequence, like drought followed by flood. And weather regimes, the large-scale atmospheric patterns like blocking that determine what weather arrives downstream.

Each of these fields has its own literature. The gaps appear where they overlap.

### Gap 1 — S2S Forecasting × Multi-hazard Events (bottom)

S2S forecasts are verified for single met variables: temperature, precipitation, wind. But nobody has verified them for multi-hazard events. We know how well a forecast predicts next month's temperature. We don't know whether that skill is still there when the target becomes a drought-to-flood transition, because that requires translating the forecast through impact variables and event detection first. Each step in that chain can lose skill, and nobody has checked. This is the central gap the thesis addresses.

### Gap 2 — S2S Forecasting × Weather Regimes (upper-left)

Kiefer et al. (2024) showed that S2S forecast skill depends on which weather regime is active when the forecast starts. When blocking is in place, some forecasts are more skilful than others. But they only tested this for single met variables like temperature. Nobody has checked whether this regime dependence also applies to impact variables like streamflow, or to multi-hazard events. If skill for drought-to-flood transitions also depends on the weather regime at initialisation, that changes how you design and evaluate the forecast.

### Gap 3 — Weather Regimes × Multi-hazard Events (upper-right)

Brunner et al. (2025) showed that specific blocking patterns are associated with drought-flood events across Europe, but these were *spatially* compounding events: drought in one region and flood in another at the same time. Francis et al. (2023) showed that rapid shifts between weather regimes, what they call weather whiplash, are the upstream atmospheric mechanism that can trigger surface-level transitions: blocking breaks down, westerlies return, and Atlantic moisture gets steered into a region.

But both studies are backwards-looking. They identified the association from historical observations. Neither uses weather regimes to *predict* a transition in a forecast. And the relationship is not straightforward: a weather regime shift doesn't always produce a drought-to-flood transition on the ground. Whether it does depends on soil moisture, catchment state, how long the drought lasted. That conditional, nonlinear relationship is a natural entry point for machine learning, and it's a separate ML application from post-processing or replacing the hydrological model. It's about learning *when* a regime shift translates into a real-world transition and when it doesn't.

Also worth noting: Brunner's work was on spatially compounding events, not temporally compounding ones. The weather regime link to temporal transitions, drought *then* flood in the same place, is even less explored.

### The centre — where all three meet

The centre of the diagram is where all three literatures converge: can S2S forecasts predict multi-hazard events, and does that skill depend on weather regimes? That's the thesis.
