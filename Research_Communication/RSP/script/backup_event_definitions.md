# Backup — How are drought-to-flood events defined?

## When to use
If the panel asks "what thresholds will you use?", "how are these events actually defined?", or "what did other studies find?"

---

This table is six studies' actual choices when detecting drought-to-flood transitions. Five use raw thresholding on streamflow, one uses an index. They disagree on almost everything else.

What counts as drought ranges from the 15th percentile all the way to the 50th percentile of annual minima. What counts as flood goes from the 50th percentile of annual maxima up to the 99th percentile. And the linking rule, how close in time the two need to be, goes from "during the drought itself" to a 90 day window.

The last row is Wang et al. from the Yangtze basin, which is the Chinese DFAA tradition. They don't threshold streamflow directly. They compute an alternation index from SPI and then threshold that. It's a different detection strategy, and the index embeds weighting coefficients that were calibrated for monsoon seasonality, so it wouldn't transfer to Ireland without recalibration.

Anderson et al. tested several of these approaches on the same eight catchments and only managed to detect three of eight transitions that actually happened. Switzerland, England, Italy, California, all missed. The definition isn't a formality. It changes what you find.

For Ireland, none of these have been tried. That's one of the first things I need to do: apply multiple definitions to Irish observed streamflow and see what they agree on before committing to one for the forecast verification.

[~55s, ~220 words]
