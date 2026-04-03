"""
Geographic map of drought-to-flood transition research.
One marker per paper. Shape = method family, colour = terminology.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Nimbus Roman", "Times New Roman", "Times"],
    "mathtext.fontset": "stix",
    "font.size": 14,
    "axes.titlesize": 16,
    "legend.fontsize": 13,
    "figure.dpi": 300,
    "savefig.dpi": 300,
})

# ── Colour by terminology ────────────────────────────────────────────
TERM_COLOURS = {
    "DFAA":                "#E15759",  # warm red
    "Whiplash":            "#4E79A7",  # steel blue
    "D-to-F transition":   "#59A14F",  # sage green
    "Weather whiplash":    "#B07AA1",  # muted purple
    "Other":               "#EDC948",  # gold
}

# ── Shape by method family ───────────────────────────────────────────
METHOD_MARKERS = {
    "Precipitation-based": "o",   # circle
    "Streamflow-based":    "^",   # triangle up
    "Circulation-based":   "s",   # square
    "Combination":      "D",   # diamond
}

# ── Paper data: (lat, lon, terminology, method) ──────────────────────
rng = np.random.RandomState(42)

def jitter(lat, lon, n, spread=1.5):
    """Return n slightly jittered (lat, lon) pairs arranged in a grid-like scatter."""
    if n == 1:
        return [(lat, lon)]
    lats = lat + rng.uniform(-spread, spread, n)
    lons = lon + rng.uniform(-spread, spread, n)
    return list(zip(lats, lons))


papers = []

# ── CHINA: DFAA tradition (~22 papers) ───────────────────────────────
# Yangtze basin papers (Wu 2006, Wang 2024, Yang 2013, Su 2024)
for lat, lon in jitter(30.5, 117, 4, 2.0):
    papers.append((lat, lon, "DFAA", "Precipitation-based"))

# Pearl River Basin (Bai 2024 copula, Lai 2025, Zhao 2020)
for lat, lon in jitter(23.5, 113, 2, 1.5):
    papers.append((lat, lon, "DFAA", "Precipitation-based"))
papers.append((22.5, 111, "DFAA", "Combination"))  # Bai 2024 MSDFI

# Wei River (Wang 2025)
papers.append((34.5, 108, "DFAA", "Precipitation-based"))

# Hanjiang Basin (Zhao 2020 SWAP)
papers.append((32, 112.5, "DFAA", "Precipitation-based"))

# Huang-Huai-Hai (Ren 2023)
papers.append((35.5, 117, "DFAA", "Precipitation-based"))

# Poyang Lake (Tu 2026)
papers.append((29, 116.5, "DFAA", "Precipitation-based"))

# Ganjiang River (Liu 2024)
papers.append((26.5, 115, "DFAA", "Precipitation-based"))

# China national (Bi 2023, Shi 2021, Wei 2025, Fu 2023, Su 2024, Bai 2026, Wang 2025)
for lat, lon in jitter(37, 104, 7, 3.0):
    papers.append((lat, lon, "DFAA", "Precipitation-based"))

# Northern China (Ji 2025, Liang 2025)
for lat, lon in jitter(41, 117, 2, 1.5):
    papers.append((lat, lon, "DFAA", "Precipitation-based"))

# High-plateau basin (Liu 2023)
papers.append((32, 99, "DFAA", "Precipitation-based"))

# Reviews (Zhang 2025, Bai 2023) — place at western China
for lat, lon in jitter(33, 102, 2, 2.0):
    papers.append((lat, lon, "DFAA", "Precipitation-based"))

# ── BRAHMAPUTRA (Nie 2025) ───────────────────────────────────────────
papers.append((28.5, 90, "DFAA", "Streamflow-based"))

# ── US CALIFORNIA (3 papers) ────────────────────────────────────────
papers.append((37.5, -121, "Whiplash", "Precipitation-based"))   # Swain 2018
papers.append((36, -119.5, "Whiplash", "Circulation-based"))      # DeFlorio 2024
papers.append((38.5, -122, "Whiplash", "Precipitation-based"))    # Swain 2025

# ── US CONUS / MIDWEST (6 papers) ───────────────────────────────────
papers.append((41, -95, "Whiplash", "Streamflow-based"))      # Yang 2025
papers.append((39, -99, "D-to-F transition", "Streamflow-based"))          # Götte & Brunner 2024
papers.append((37, -92, "Whiplash", "Precipitation-based"))  # Mullens & Engström 2025
papers.append((42, -88, "Whiplash", "Precipitation-based"))  # Ford 2021
papers.append((43, -96, "Whiplash", "Precipitation-based"))  # Loecke 2017
papers.append((36, -100, "Whiplash", "Streamflow-based"))     # Hammond 2025

# ── US/CANADA GREAT LAKES + N. AMERICA (2 papers) ───────────────────
papers.append((44, -82, "Whiplash", "Precipitation-based"))   # Na & Najafi 2024
papers.append((46, -79, "Other", "Combination"))         # Rahimimovaghar 2024

# ── EUROPE (2 papers) ───────────────────────────────────────────────
papers.append((49, 12, "D-to-F transition", "Streamflow-based"))           # Brunner et al. 2025
papers.append((55, 0, "Weather whiplash", "Circulation-based"))            # Francis et al. 2023

# ── FRANCE (1 paper) ────────────────────────────────────────────────
papers.append((46, 2, "D-to-F transition", "Streamflow-based"))            # Guimarães 2026

# ── CHILE + SWITZERLAND (Muñoz-Castro 2026 — plot both locations) ────
papers.append((-33, -71, "D-to-F transition", "Streamflow-based"))         # Chile
papers.append((47, 8.5, "D-to-F transition", "Streamflow-based"))         # Switzerland

# ── AUSTRALIA (Goswami 2026) ─────────────────────────────────────────
papers.append((-28, 135, "Other", "Precipitation-based"))

# ── ENGLAND AND WALES (Parry 2013) ──────────────────────────────────
papers.append((52, -2, "D-to-F transition", "Precipitation-based"))

# ── IRAN (Farzin 2025) ──────────────────────────────────────────────
papers.append((33, 53, "Other", "Combination"))


# ── PLOT ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(20, 10), facecolor="white")
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Miller(central_longitude=10))
ax.set_extent([-180, 180, -60, 85], crs=ccrs.PlateCarree())
ax.spines["geo"].set_visible(False)
ax.set_facecolor("white")  # sea = white

# Map features — two-tone land: studied countries darker, others lighter
STUDIED_COUNTRIES = {
    "China", "United States of America", "Canada", "France", "Switzerland",
    "Chile", "United Kingdom", "Iran", "Australia", "India", "Nepal",
    "Germany", "Austria", "Norway", "Italy", "Spain", "Portugal",
}

# Base: all land in light grey
ax.add_feature(cfeature.LAND, facecolor="#E8E8E8", edgecolor="none", zorder=1)

# Overlay studied countries in darker grey
shpfilename = shpreader.natural_earth(resolution="110m", category="cultural", name="admin_0_countries")
reader = shpreader.Reader(shpfilename)
for country in reader.records():
    name = country.attributes["NAME"]
    if name in STUDIED_COUNTRIES:
        ax.add_geometries(
            [country.geometry], ccrs.PlateCarree(),
            facecolor="#D0D0D0", edgecolor="none", zorder=1.5,
        )

ax.add_feature(cfeature.COASTLINE, linewidth=0.3, color="#AAAAAA", zorder=2)
ax.add_feature(cfeature.BORDERS, linewidth=0.15, color="#C0C0C0", zorder=2)

# Plot each paper — larger markers, thicker edges
MS = 10  # marker size — base for circles
# Triangles/squares/diamonds appear smaller at same markersize due to geometry
MS_ADJUST = {"o": 10, "^": 11, "s": 10, "D": 10}
for lat, lon, term, method in papers:
    colour = TERM_COLOURS[term]
    marker = METHOD_MARKERS[method]
    ax.plot(
        lon, lat,
        marker=marker,
        color=colour,
        markersize=MS_ADJUST.get(marker, MS),
        markeredgecolor="white",
        markeredgewidth=0.7,
        transform=ccrs.PlateCarree(),
        zorder=5,
        alpha=0.9,
    )


# ── Region labels (subtle, positioned to avoid markers) ──────────────

# ── Legends (side by side below the map) ─────────────────────────────
# Full terminology labels
TERM_LABELS = {
    "DFAA":              "Drought-flood abrupt alternation",
    "Whiplash":          "Whiplash",
    "D-to-F transition": "Drought-to-flood transition",
    "Weather whiplash":  "Weather whiplash",
    "Other":             "Other",
}

METHOD_LABELS = {
    "Precipitation-based": "Precipitation-based",
    "Streamflow-based":    "Streamflow-based",
    "Circulation-based":   "Circulation-based",
    "Combination":      "Combination",
}

term_handles = [
    mpatches.Patch(facecolor=TERM_COLOURS[k], edgecolor="white", linewidth=0.5, label=v)
    for k, v in TERM_LABELS.items()
]
method_handles = [
    mlines.Line2D(
        [], [],
        marker=METHOD_MARKERS[k], color="#555555", linestyle="None",
        markersize=MS_ADJUST.get(METHOD_MARKERS[k], MS), markeredgecolor="white", markeredgewidth=0.7,
        label=v,
    )
    for k, v in METHOD_LABELS.items()
]

# Combined legend: terminology left column, method right column
# Interleave so ncol=2 puts terminology left, method right
spacer = mpatches.Patch(facecolor="none", edgecolor="none", label=" ")
n_rows = max(len(term_handles), len(method_handles))
col_handles = []
col_labels = []
for i in range(n_rows):
    if i < len(term_handles):
        col_handles.append(term_handles[i])
        col_labels.append(term_handles[i].get_label())
    else:
        col_handles.append(spacer)
        col_labels.append(" ")
for i in range(n_rows):
    if i < len(method_handles):
        col_handles.append(method_handles[i])
        col_labels.append(method_handles[i].get_label())
    else:
        col_handles.append(spacer)
        col_labels.append(" ")

leg = fig.legend(
    handles=col_handles,
    labels=col_labels,
    ncol=2,
    fontsize=13,
    loc="lower left",
    bbox_to_anchor=(0.38, -0.02),
    frameon=True,
    facecolor="white",
    edgecolor="#BBBBBB",
    framealpha=0.95,
    borderpad=1.0,
    labelspacing=0.5,
    columnspacing=2.5,
    title="Terminology (colour)                        Method (shape)",
    title_fontsize=14,
)
leg.get_title().set_fontweight("bold")

# ── Footnote ─────────────────────────────────────────────────────────

# ── Title ────────────────────────────────────────────────────────────
ax.set_title(
    "Terminology and methods of drought-to-flood literature",
    fontsize=17, fontweight="bold", pad=18, linespacing=1.3,
)

plt.subplots_adjust(left=0.02, right=0.98, top=0.92, bottom=0.05)

outdir = "/home/lainey/Documents/Github/Research_Communication/RSP/slides"
plt.savefig(f"{outdir}/terminology_map.png", dpi=300, bbox_inches="tight", facecolor="white")
print("Saved terminology_map.png")
