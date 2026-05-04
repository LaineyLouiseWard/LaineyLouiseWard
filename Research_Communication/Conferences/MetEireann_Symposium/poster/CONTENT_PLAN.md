# Met Eireann Symposium Poster -- Content Plan

## Audience
Operational meteorologists and researchers at Met Eireann. They understand NWP, verification, and Irish weather intimately. They know the 9 Tier 1 stations by name. They use ECMWF products daily. They'll care about whether S2S forecasts add value for Ireland.

## What draws people to a poster
1. **A compelling problem** -- not a method, not a dataset
2. **Visual impact** -- maps of Ireland, a striking diagram, clean figures
3. **A clear gap** -- "nobody has done X" is magnetic
4. **Brevity** -- if they can't get the message in 30 seconds from 2m away, they'll walk past

## Core message (one sentence)
Nobody has forecast drought-to-flood transitions at S2S timescales -- this work establishes that the atmospheric skill exists over Ireland to begin building towards that goal.

## Title
**Towards Subseasonal-to-Seasonal Drought-to-Flood Prediction**

## Research questions
1. Do ECMWF extended-range forecasts carry probabilistic skill for temperature over Ireland at S2S lead times?
2. Which system (subseasonal or seasonal) is more suitable as a basis for downstream multi-hazard prediction?

---

## Layout

```
+=============================================================+
|  [UCD]    Title                        [Decarb] [Innovate]  |
|           Lainey Ward, UCD                                  |
+=============================================================+
| INTRODUCTION        | DROUGHT-TO-FLOOD CAUSAL CHAIN         |
| (col 0)             | (cols 1-2)                            |
|                     | [dft_causal_diagram.pdf]               |
+---------------------+---------------------------------------+
| DATA                | RESULTS                               |
| (col 0)             | (cols 1-2)                             |
|                     | [figures -- see below]                 |
|                     |                                       |
+---------------------+---------------------------------------+
| DISCUSSION & FUTURE WORK                         (span=3)   |
+-------------------------------------------------------------+
| REFERENCES                                       (span=3)   |
+=============================================================+
```

---

## Sections

### 1. Introduction (col 0, top left)

**Purpose:** Hook the viewer. State the problem, the gap, and the research questions.

**What to include:**
- Open with impact: drought-to-flood transitions produce up to 8x greater socio-economic losses than isolated events (Worou & Messori 2025); ~25% of floods globally are drought-preceded (Matano et al. 2024)
- The gap: all existing DFT research is retrospective -- nobody has forecast these transitions at any lead time
- S2S timescales (2 weeks to 2 months) are the natural window for early action, but skill over Ireland has never been assessed
- **State RQ1 and RQ2 clearly** -- these frame the entire poster

**What NOT to include:**
- Don't explain what S2S means beyond the parenthetical
- Don't explain verification methodology here
- Don't list all five research traditions (save for thesis/paper)

**Format:** Short paragraphs or bullet points. ~100-150 words max. Bold the key phrases ("no study has forecast", "first assessment"). Left-aligned.

---

### 2. Drought-to-Flood Causal Chain (cols 1-2, top right)

**Purpose:** The visual anchor. Shows *why* atmospheric skill matters -- it's the first link in a physical chain leading to compound impact.

**What to include:**
- `dft_causal_diagram.pdf` -- the Bevacqua-style causal chain
  - Blocking/NAO- → Precipitation deficit + High ET → Drought → Modified catchment state → IVT surge / intense precipitation → Flood → Compound drought-flood impact
  - Colour grammar: Modulator (yellow), Driver (green), Hazard (blue), Precondition (orange), Impact (red)
  - Evidenced links (solid arrows) vs plausible links (dashed)
- One-line caption: "Causal chain for British-Irish Isles drought-to-flood transitions (colour grammar after Bevacqua et al. 2021). This work verifies skill at the atmospheric driver level."

**Why this figure:**
- It's yours (from thesis Chapter 2), follows best-practice guidelines
- It immediately communicates the physical story to Met Eireann staff who understand blocking, NAO, IVT
- The arrow from "Blocking/NAO-" to "Drought" is exactly what the S2S system needs to predict
- The dashed "plausible links" are honest about what's not yet established

**What NOT to include:**
- Don't use a BBC news image (you have a better, citable, original diagram)
- Don't add extra text explaining every box -- the legend does this

---

### 3. Data (col 0, middle left)

**Purpose:** What goes in. Compact. The viewer glances at this, doesn't study it.

**Format:** Bullet points, ~6 lines. No table needed unless space allows naturally.

**Content:**
- Subseasonal: ECMWF EEFH, 11 members, weekly init.
- Seasonal: ECMWF SEAS5, 25 members, monthly init.
- Reference: ERA5-Land reanalysis (gridded, 0.3° common grid)
- Variable: 2m temperature (strongest skill signal)
- Lead times: Weeks 2--6
- Period: 2006--2016 reforecasts
- Metrics: CRPSS, BSS (Fair scoring, Ferro 2014)
- Verification is fully spatial (gridded), not station-based

**Why temperature only:**
- Cleanest story for a poster; precip and wind can be mentioned in future work
- Temperature skill is the base -- if there's no atmospheric skill, there's no downstream skill

---

### 4. Results (cols 1-2, main area)

**Purpose:** The centrepiece. Answer both research questions with figures. Let the figures speak -- minimal text.

**This is where viewers will spend most of their time.** Figures must be self-explanatory with clear captions.

#### Recommended figures (Tier 1 -- must include):

**Figure A: `domain_crpss_eefh_t2m.png`** -- Headline quantitative result
- Shows Fair CRPSS declining from ~0.42 (Week 2) to ~0.28 (Week 6) with uncertainty band
- Clean, single-metric, immediately readable
- Caption: "Domain-mean CRPSS for 2m temperature (Fair CRPS). Shading: 10th--90th percentile across gridpoints. Positive = skilful vs climatology."
- **Answers RQ1:** Yes, positive skill persists through Week 6.

**Figure B: `spatial_crpss_eefh_t2m.png`** -- Where is the skill?
- 4 spatial maps (Weeks 2, 3, 5, 6) showing CRPSS over Ireland
- Strong blues (high skill) in Week 2, fading by Week 6
- Met Eireann audience loves maps of Ireland
- Caption: "Spatial CRPSS for EEFH 2m temperature at Weeks 2, 3, 5, 6."
- **Shows spatial structure** -- are there regional differences?

**Figure C: `crpss_vs_rmss_comparison.png`** -- The system comparison
- CRPSS (left) and RMSS (right) for EEFH vs SEAS5 across lead weeks
- Key finding: probabilistic skill comparable between systems; deterministic skill diverges
- Caption: "CRPSS and RMSS for EEFH (blue) vs SEAS5 (red). Probabilistic skill is comparable; deterministic skill of EEFH degrades faster."
- **Answers RQ2:** For probabilistic applications, both systems are viable.

#### Optional (Tier 2 -- if space allows):

**Figure D: `spatial_reliability_eefh_t2m.png`** -- Is the ensemble calibrated?
- Reliability diagrams for below/above-normal terciles
- Shows forecasts are reasonably calibrated (close to diagonal)
- Important for operational trust -- but may be too technical for a poster

#### Layout within Results box:

```
+-------------------------------------------+
| [Figure A: domain CRPSS]  [Figure B: maps]|
|                                           |
| Caption A                  Caption B      |
|                                           |
| [Figure C: EEFH vs SEAS5 comparison]      |
|                                           |
| Caption C                                 |
+-------------------------------------------+
```

Figures A and B side by side at top (quantitative + spatial), Figure C below spanning the width (the comparison = the novelty).

---

### 5. Discussion & Future Work (full width)

**Purpose:** What this means, and where it goes next. Connect back to the causal chain.

**Format:** Two columns within the box. Left = Discussion, Right = Future Work. Bullet points.

**Discussion (left side):**
- First evidence that S2S forecasts carry useful probabilistic signal for temperature over Ireland
- Positive skill at Weeks 4--6 is encouraging for operational applications
- This establishes skill at the atmospheric driver level of the causal chain (top of poster)
- Probabilistic framing more robust than deterministic -- ensemble spread adds value

**Future Work (right side):**
- Extend to precipitation (next variable in the chain)
- Trace skill through hydrological impact variables (soil moisture, runoff via hydrological modelling)
- Define and verify drought-to-flood transition events from ensemble trajectories
- Explore ML for transition probability estimation

**Key framing:** The future work is not speculative -- it's the research programme. Each bullet maps to a specific gap identified in the thesis (Gaps A-D). The causal chain in the top right is the roadmap.

**Include:** LinkedIn QR code in bottom-right corner of this box with "Connect" label.

---

### 6. References (full width, flat strip)

**Purpose:** Key citations only. Flat format, small text. 5-8 refs max.

**Must include:**
- Worou & Messori (2025) -- 8x impact amplification (hooks the Introduction)
- Matano et al. (2024) -- 25% of floods drought-preceded
- Ferro (2014) -- Fair CRPS methodology
- Bevacqua et al. (2021) -- causal chain colour grammar
- Parry et al. (2023) -- Irish drought termination via IVT/NAO+
- Brunner et al. (2025) -- UK/Ireland flood-during-drought hotspot

**Optional:**
- Anderson et al. (2025) -- "What is a drought-to-flood transition?"
- Pechlivanidis et al. (2025) -- hydrological skill amplification

---

## Figures summary

- [x] `dft_causal_diagram.pdf` -- causal chain (exists, from thesis)
- [x] `crpss_vs_rmss_comparison.png` -- EEFH vs SEAS5 (exists, in poster dir)
- [x] `qrcode_linkedin.png` -- LinkedIn QR with logo (exists, in poster dir)
- [ ] Copy `eefh_probabilistic/spatial_crpss_eefh_t2m.png` from S2S_AI
- [ ] Copy `eefh_probabilistic/domain_crpss_eefh_t2m.png` from S2S_AI
- [ ] Check logo resolution for print (decarb_ai 830x328, InnovateforIreland 899x240 -- both below 300 DPI at A0)

## What makes this poster compelling

1. **The hook is the problem, not the method.** "8x worse impacts, nobody has forecast these" -- that stops people walking past.
2. **The causal chain diagram is the visual anchor.** It's colourful, follows best-practice guidelines, tells a physical story that Met Eireann staff intuitively understand, and it's *yours*.
3. **The maps of Ireland draw the eye.** Spatial CRPSS maps are familiar and satisfying for this audience.
4. **The gap is clear.** "All DFT research is retrospective" is a one-line novelty statement.
5. **The research questions give structure.** Two questions, two answers from the figures, clean story arc.
6. **The future work connects back to the diagram.** The poster tells you where this research is going -- each step in the chain is a future paper.
7. **Less is more.** One variable, three figures, two research questions. The viewer gets the full story in 3 minutes.

## Figures to create or consider

### For the Results box (2-3 figures):
1. **Combined CRPSS figure** (TO CREATE): Your plan for a figure showing domain-mean CRPSS at each lead time over the spatial area. This is the centrepiece -- it answers RQ1 directly. If it combines maps + a summary line, it replaces the separate spatial maps and domain-mean line plot.
2. **EEFH vs SEAS5 comparison** (EXISTS: `crpss_vs_rmss_comparison.png`): Answers RQ2. Could be used as-is or cleaned up for poster. Key message: probabilistic skill comparable, deterministic diverges.
3. **Optional third figure**: BSS or a single reliability panel if space allows. The existing 12-panel reliability diagram is too busy for a poster -- consider a single Week 3 panel if you want to show calibration.

### For the Data box (optional visual):
- **Small pipeline schematic** (TO CREATE, optional): A simple horizontal arrow diagram showing the verification chain: ECMWF ensemble → weekly means → probabilistic verification vs ERA5-Land (0.3° grid) → skill scores. Gives the Data box visual weight beyond just bullet points. Could be a simple TikZ figure or hand-drawn. Not essential -- bullet points alone work fine here.

### For the Causal Chain box:
- `dft_causal_diagram.pdf` (EXISTS) -- no changes needed. This is the visual anchor.

### Dropped:
- Reliability diagrams (too technical, 12 panels)
- Deterministic-only figures (RMSE maps -- the probabilistic story is stronger)
- Station-level box plots (good for paper, too detailed for poster)

## What NOT to do
- Don't show all three variables (temperature is enough for a poster)
- Don't include a table (figures are more engaging; data details are bullet points)
- Don't explain the five research traditions (save for thesis/paper)
- Don't include deterministic-only figures (the probabilistic story is stronger)
- Don't add a Methods section -- the metrics are listed in Data, the approach is implicit from the figures
- Don't overcrowd Results -- three figures maximum
