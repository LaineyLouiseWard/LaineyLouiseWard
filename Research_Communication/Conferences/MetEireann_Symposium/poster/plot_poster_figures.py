"""
plot_poster_figures.py — generate poster figures from cached data.

Fast to re-run: reads only the small poster_data.pkl cache.
Produces:
  - spatial_crpss_poster.png    (3-panel CRPSS maps: Weeks 2, 4, 6)
  - lineplot_skill_poster.png   (dual-panel ACC + CRPSS vs lead time)

Usage:
    conda run -n S2S_AI python plot_poster_figures.py
"""

import pickle
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.tri as tri
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
from shapely.ops import unary_union
import cmcrameri.cm as cmc

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 12,
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
})

# ── Config ───────────────────────────────────────────────────────
DATA_FILE = Path(__file__).parent / "poster_data.pkl"
OUT_DIR = Path(__file__).parent

# Line plot colours (matched to poster palette)
LINE_COLOURS = {
    "Annual": "#1B2A4A",   # posternavy
    "DJF": "#4A90D9",      # blue
    "JJA": "#E8943A",      # orange
}
LINE_STYLES = {
    "Annual": {"lw": 2.5, "marker": "o", "ms": 8, "zorder": 3},
    "DJF":    {"lw": 2.0, "marker": "s", "ms": 7, "zorder": 2},
    "JJA":    {"lw": 2.0, "marker": "D", "ms": 7, "zorder": 2},
}

# Spatial: vik_r colourmap (blue = positive skill)
CMAP_CRPSS = cmc.vik_r
CRPSS_LEVELS = [-0.4, -0.3, -0.2, -0.1, -0.05,
                 0.0,
                 0.05, 0.1, 0.2, 0.3, 0.4, 0.5]

# Projection: LambertConformal centred on Ireland (matching S2S_AI notebooks)
PC = ccrs.PlateCarree()
PROJ = ccrs.LambertConformal(central_longitude=-8.0, central_latitude=53.5,
                              standard_parallels=(53.5,))
IRELAND_EXTENT = [-10.8, -5.5, 51.3, 55.5]  # tight crop, Ireland only

# Ireland coastline from Natural Earth
_ne_path = shpreader.natural_earth(resolution="10m", category="cultural",
                                    name="admin_0_countries")
_reader = shpreader.Reader(_ne_path)
_ireland_geoms = [g.geometry for g in _reader.records()
                  if g.attributes["NAME"] in ("Ireland", "United Kingdom")]
IRELAND_SHAPE = unary_union(_ireland_geoms)


def load_data():
    with open(DATA_FILE, "rb") as f:
        return pickle.load(f)


def _fix_lons(lons):
    return np.where(lons > 180, lons - 360, lons)


# ── Figure 3: Spatial CRPSS maps (3 panels) ─────────────────────

def plot_spatial_crpss(data):
    """3-panel Ireland CRPSS maps using tripcolor + LambertConformal."""
    spatial_crpss = data["spatial_crpss"]
    spatial_weeks = data["spatial_weeks"]
    n = len(spatial_weeks)

    fig, axes = plt.subplots(
        1, n,
        figsize=(n * 3.5, 4.5),
        subplot_kw={"projection": PROJ},
    )
    if n == 1:
        axes = [axes]

    norm = mcolors.BoundaryNorm(CRPSS_LEVELS, CMAP_CRPSS.N)

    for ax, wk in zip(axes, spatial_weeks):
        sp = spatial_crpss[wk]
        lons = _fix_lons(sp["longitude"])
        lats = sp["latitude"]
        vals = sp["values"]

        # Ireland shape as background fill
        ax.add_geometries([IRELAND_SHAPE], crs=PC,
                          facecolor="#e8e8e0", edgecolor="none", zorder=1)

        # Delaunay triangulation for filled contours
        triang = tri.Triangulation(lons, lats)
        tc = ax.tripcolor(triang, vals, cmap=CMAP_CRPSS, norm=norm,
                          transform=PC, zorder=2, edgecolors="none")

        # Ireland coastline on top
        ax.add_geometries([IRELAND_SHAPE], crs=PC,
                          facecolor="none", edgecolor="#444444",
                          linewidth=0.8, zorder=3)

        ax.set_extent(IRELAND_EXTENT, crs=PC)
        ax.set_title(f"Week {wk[2:]}", fontweight="bold", pad=6)

    # Shared colourbar
    cbar = fig.colorbar(tc, ax=axes, orientation="vertical",
                        fraction=0.03, pad=0.02)
    cbar.set_label("CRPSS", fontsize=12)
    cbar.ax.tick_params(labelsize=10)

    fig.subplots_adjust(wspace=0.05)

    out = OUT_DIR / "spatial_crpss_poster.png"
    fig.savefig(out, dpi=250, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved {out}")


# ── Figure 4: Dual-panel line plot (ACC + CRPSS vs lead) ────────

def plot_lineplot(data):
    """Two panels: ACC (left), CRPSS (right). No suptitle."""
    weeks = data["week_numbers"]

    fig, (ax_acc, ax_crpss) = plt.subplots(1, 2, figsize=(9, 4.5))

    for season in ["Annual", "DJF", "JJA"]:
        col = LINE_COLOURS[season]
        sty = LINE_STYLES[season]

        acc = data.get(f"sacc_{season}")
        if acc is not None:
            ax_acc.plot(weeks, acc, color=col, label=season,
                        lw=sty["lw"], marker=sty["marker"], ms=sty["ms"],
                        zorder=sty["zorder"])

        crpss = data.get(f"crpss_{season}")
        if crpss is not None:
            ax_crpss.plot(weeks, crpss, color=col, label=season,
                          lw=sty["lw"], marker=sty["marker"], ms=sty["ms"],
                          zorder=sty["zorder"])

    # ACC 0.6 "useful skill" reference line (Hollingsworth et al. 1980)
    ax_acc.axhline(0.6, color="0.65", ls=":", lw=1.0, zorder=0)
    ax_acc.annotate("useful skill", xy=(weeks[-1] + 0.25, 0.6),
                    fontsize=9, color="0.45", va="bottom", ha="right")

    for ax, panel_label, ylabel in [
        (ax_acc, "Spatial ACC", "Anomaly Correlation"),
        (ax_crpss, "CRPSS", "CRPS Skill Score"),
    ]:
        ax.axhline(0, color="0.5", ls="--", lw=0.8, zorder=0)
        ax.annotate("climatology", xy=(weeks[-1] + 0.25, 0),
                     fontsize=9, color="0.45", va="bottom", ha="right")
        ax.set_title(panel_label, fontweight="bold")
        ax.set_xlabel("Week")
        ax.set_ylabel(ylabel)
        ax.set_xticks(weeks)
        ax.set_xlim(weeks[0] - 0.3, weeks[-1] + 0.3)
        ax.grid(axis="y", alpha=0.25, lw=0.5)

    # Single shared legend below panels
    handles, labels = ax_acc.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=3,
               fontsize=11, frameon=False, bbox_to_anchor=(0.5, -0.04))

    fig.tight_layout(rect=[0, 0.04, 1, 1])

    out = OUT_DIR / "lineplot_skill_poster.png"
    fig.savefig(out, dpi=250, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved {out}")


# ── Main ─────────────────────────────────────────────────────────

def main():
    data = load_data()
    plot_spatial_crpss(data)
    plot_lineplot(data)


if __name__ == "__main__":
    main()
