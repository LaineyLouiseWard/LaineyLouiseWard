# Backup — Three research traditions

## When to use
If the panel asks "what does the literature look like?", "how fragmented is the field?", or after showing the terminology map.

This slide follows the terminology map and sets up the detection strategies slide.

---

This table breaks down the three traditions. They grew up separately, and until 2025 they barely cited each other.

The DFAA tradition comes out of Chinese hydrology. It was built for monsoon basins where you get a May drought followed by a July flood in the same season. They developed purpose-built indices that compress the intensity and speed of the swing into a single number. But the coefficients inside those indices were calibrated for monsoon seasonality, and nobody has recalibrated them for a maritime climate like ours.

The Western tradition uses standard tools, SPI or streamflow percentiles, and detects drought and flood episodes independently. If they happen close enough together, that counts as a transition. The recovery window, how many days apart the two can be, is the parameter that varies most across studies. This is also where machine learning is starting to appear, through S2S forecast post-processing.

Weather whiplash works at the circulation level. It classifies atmospheric regime patterns and identifies when one regime shifts rapidly to another. That can drive a surface transition, but it does not guarantee one. Whether a circulation shift actually produces a flood depends on moisture availability and the state of the catchment.

For this thesis, the plan is to take something from each side. From the Western tradition, episode-linking for detection, because the assumptions are transparent and it connects directly to S2S verification. From DFAA, the idea that the swing itself is worth measuring. Once we have events, we can compute how far the variable moved between the drought and flood thresholds, and how fast. That gives us DFAA-style characterisation without needing to calibrate their indices for a maritime climate.

[~75s, ~270 words]
