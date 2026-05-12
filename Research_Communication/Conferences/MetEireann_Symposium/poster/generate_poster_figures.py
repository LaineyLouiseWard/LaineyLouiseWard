#!/usr/bin/env python3
"""
generate_poster_figures.py — Produce the three Results figures for the
Met Éireann Symposium poster from any gridded analysis dataset.

Figures:
  1. ACC vs lead time (line plot, 0.6 threshold)
  2. Rank histogram before/after bias correction (pooled wk2-wk6)
  3. Spatial Fair CRPSS maps (Weeks 2, 4, 6 — bias-corrected)

Usage:
    python generate_poster_figures.py                # default: 0.28° dataset
    python generate_poster_figures.py --grid 075     # use 0.75° dataset
    python generate_poster_figures.py --no-cache     # force recompute scores
"""
import sys
import pickle
import argparse
from pathlib import Path

import numpy as np
import xarray as xr
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.colors import BoundaryNorm
from shapely.ops import unary_union
import cartopy.io.shapereader as shpreader
import shapely.geometry as sgeom

# ── Poster-matching font setup (sans-serif, close to lmodern) ────
plt.rcParams.update({
    "text.usetex": False,
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial"],
    "mathtext.fontset": "dejavusans",
    "axes.labelsize": 10,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
})

# ── Repo and module setup ────────────────────────────────────────
POSTER_DIR = Path(__file__).resolve().parent
_REPO = POSTER_DIR
for _ in range(10):
    if (_REPO / "S2S_AI" / "DATA").exists():
        _REPO = _REPO / "S2S_AI"
        break
    _REPO = _REPO.parent
else:
    raise RuntimeError("Could not find S2S_AI repo root")

sys.path.insert(0, str(_REPO / "CONFIG"))
sys.path.insert(0, str(_REPO / "SCRIPTS" / "UTILS"))

from scoring_spatial_028 import (
    score_week, gridded_crps,
    _weekly_means_members, _loyo_seasonal_bias_correct,
)
from scoring_spatial_028 import subset_by_season
from _scoring_common import LEAD_WEEKS

# ── Config ───────────────────────────────────────────────────────
PLOT_WEEKS = ["wk2", "wk3", "wk4", "wk5", "wk6"]
WEEK_NUMS = [int(wk[2:]) for wk in PLOT_WEEKS]
MAP_WEEKS = ["wk2", "wk4", "wk6"]
DPI = 300

# Poster colours
C_ANN = "#1B2A4A"   # posternavy
C_DJF = "#2166ac"
C_JJA = "#b2182b"
C_EEFH = "#2166ac"
C_RAW = "#888888"
C_SKILL = "#7AB648"  # drivcol from poster

PROJ = ccrs.LambertConformal(central_longitude=-8.0, central_latitude=53.5)
EXTENT = [-11.0, -5.0, 51.0, 56.0]

# ── Ireland geometry (for masking non-Irish land) ────────────────
_shpfile = shpreader.natural_earth(
    resolution="10m", category="cultural", name="admin_0_map_subunits")
_reader = shpreader.Reader(_shpfile)
_ireland_geoms = [
    r.geometry for r in _reader.records()
    if r.attributes.get("NAME", "") in ("Ireland", "N. Ireland")
    or r.attributes.get("SU_A3", "") in ("IRL", "NIR")
]
IRELAND_SHAPE = unary_union(_ireland_geoms)


# ── Scoring cache ────────────────────────────────────────────────

def compute_scores(ds, land_mask):
    """Compute all scores needed for the three poster figures."""
    data = {"lats": ds.latitude.values, "lons": ds.longitude.values}

    # ACC per season
    for season_label, ds_sub in [("Annual", ds),
                                  ("DJF", subset_by_season(ds, "DJF")),
                                  ("JJA", subset_by_season(ds, "JJA"))]:
        sacc_vals = []
        for wk in PLOT_WEEKS:
            det = score_week(ds_sub, wk, "ensmean")
            if det is not None and det["sacc"] is not None:
                sacc_vals.append(float(det["sacc"]))
            else:
                sacc_vals.append(np.nan)
        data[f"sacc_{season_label}"] = sacc_vals
        print(f"  ACC {season_label}: done")

    # Rank histograms (raw + seasonal-LOYO BC), land-only
    for bc_label, bc in [("raw", False), ("bc", True)]:
        all_counts = []
        n_total = 0
        for wk in PLOT_WEEKS:
            result = _weekly_means_members(ds, wk)
            if result[0] is None:
                continue
            obs_wm, clim_wm, member_wm, _, _, init_years, init_doys = result
            if bc:
                member_wm = _loyo_seasonal_bias_correct(
                    member_wm, obs_wm, init_years, init_doys)
            rank = (member_wm < obs_wm[np.newaxis, :, :, :]).sum(axis=0) + 1
            valid = np.isfinite(obs_wm) & np.all(np.isfinite(member_wm), axis=0)
            valid &= land_mask[np.newaxis, :, :]
            ranks_flat = rank[valid]
            n_members = member_wm.shape[0]
            counts = np.bincount(ranks_flat,
                                 minlength=n_members + 2)[1:n_members + 2]
            all_counts.append(counts)
            n_total += int(valid.sum())

        data[f"rh_counts_{bc_label}"] = np.sum(all_counts, axis=0) if all_counts else None
        data[f"rh_n_{bc_label}"] = n_total
        print(f"  Rank hist {bc_label}: done")

    # Spatial CRPSS maps (BC)
    for wk in MAP_WEEKS:
        r = gridded_crps(ds, wk, bias_correct=True)
        if r is not None:
            crpss_vals = r["crpss"].values.copy()
            crpss_vals[~land_mask] = np.nan
            data[f"crpss_{wk}"] = crpss_vals
            data[f"crpss_mean_{wk}"] = float(np.nanmean(crpss_vals[land_mask]))
        print(f"  CRPSS {wk}: done")

    data["land_mask"] = land_mask
    return data


def load_or_compute(ds, land_mask, grid, force=False):
    """Load cached scores or recompute."""
    cache_path = POSTER_DIR / f"poster_scores_{grid}.pkl"
    if cache_path.exists() and not force:
        print(f"Loading cached scores from {cache_path.name}")
        with open(cache_path, "rb") as f:
            return pickle.load(f)

    print("Computing scores (will be cached for next run)...")
    data = compute_scores(ds, land_mask)
    with open(cache_path, "wb") as f:
        pickle.dump(data, f)
    print(f"Cached to {cache_path.name}")
    return data


# ── Masking ──────────────────────────────────────────────────────

def _mask_non_ireland(ax, proj):
    """White overlay outside Ireland; redraw only Ireland's coastline."""
    ireland_proj = proj.project_geometry(IRELAND_SHAPE, ccrs.PlateCarree())
    x0, y0, x1, y1 = ax.get_extent(proj)
    pad = max(x1 - x0, y1 - y0) * 0.5
    outer = sgeom.box(x0 - pad, y0 - pad, x1 + pad, y1 + pad)
    mask_geom = outer.difference(ireland_proj)

    geoms = mask_geom.geoms if hasattr(mask_geom, "geoms") else [mask_geom]
    for g in geoms:
        ax.add_geometries([g], crs=proj, facecolor="white",
                          edgecolor="none", zorder=3)
    # Ireland coastline only (no Scotland/Wales)
    ax.add_geometries([ireland_proj], crs=proj, facecolor="none",
                      edgecolor="#444444", linewidth=0.8, zorder=4)


# ── Figure 1: ACC vs lead time ───────────────────────────────────

def figure1_acc_leadtime(data, out_path):
    """ACC vs lead time --- annual, DJF, JJA."""
    fig, ax = plt.subplots(figsize=(4.5, 3.0))

    for label, color in [
        ("Annual", C_ANN),
        ("DJF",    C_DJF),
        ("JJA",    C_JJA),
    ]:
        vals = data.get(f"sacc_{label}")
        if vals is not None:
            ax.plot(WEEK_NUMS, vals, "-", color=color,
                    lw=2.5, label=label, zorder=3)

    ax.axhline(0.6, color=C_SKILL, ls="--", lw=2.0, alpha=0.7, zorder=2)
    ax.text(4.0, 0.62, "useful skill", fontsize=9,
            color=C_SKILL, va="bottom", fontstyle="italic")
    ax.axhline(0, color="grey", ls="-", lw=0.6, alpha=0.4)

    ax.set_xlabel("Week")
    ax.set_ylabel("ACC")
    ax.set_xticks(WEEK_NUMS)
    ax.set_ylim(-0.15, 0.75)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.25),
              ncol=3, frameon=False, fontsize=8)
    # No background grid — clean for poster
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved: {out_path.name}")


# ── Figure 2: Rank histograms ───────────────────────────────────

def figure2_rank_histograms(data, out_path):
    """Rank histograms: raw vs seasonal-LOYO BC, pooled wk2--wk6, land only."""
    fig, axes = plt.subplots(1, 2, figsize=(4.5, 1.6), sharey=True)

    for col, (suffix, label, color) in enumerate([
        ("raw", "Raw", C_RAW),
        ("bc",  "Bias-corrected", "#7AB648"),  # drivcol green — distinct from blue ACC
    ]):
        ax = axes[col]
        counts = data.get(f"rh_counts_{suffix}")
        n_total = data.get(f"rh_n_{suffix}", 0)

        if counts is not None:
            n_ranks = len(counts)
            uniform = n_total / n_ranks
            ax.bar(np.arange(1, n_ranks + 1), counts / 1e3,
                   color=color, alpha=0.8, edgecolor="white", linewidth=0.4)
            ax.axhline(uniform / 1e3, color="black", ls="--", lw=1.2, alpha=0.5)

        ax.set_xlabel("Rank", fontsize=8)
        if col == 0:
            ax.set_ylabel("Count ($\\times 10^3$)", fontsize=8)
        ax.set_yticks([0, 10, 20, 30])
        ax.set_xticks([1, 4, 8, 12])
        ax.tick_params(axis="both", labelsize=7)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        # Title ON the plot (inside top area)
        ax.text(0.5, 0.95, label, transform=ax.transAxes,
                fontsize=9, fontweight="bold", ha="center", va="top")

    # Warm/cold bias annotations — symmetric, pointing to rank 1 and 12
    ax_raw = axes[0]
    ylim = ax_raw.get_ylim()
    y_arr = ylim[1] * 0.72
    ax_raw.annotate("warm", xy=(1.0, y_arr), xytext=(4.0, y_arr),
                    fontsize=7, color="#b2182b", fontstyle="italic",
                    fontweight="bold", va="center",
                    arrowprops=dict(arrowstyle="-|>", color="#b2182b",
                                    lw=1.5, mutation_scale=12,
                                    shrinkA=0, shrinkB=2))
    ax_raw.annotate("cold", xy=(12.0, y_arr), xytext=(9.0, y_arr),
                    fontsize=7, color="#2166ac", fontstyle="italic",
                    fontweight="bold", va="center",
                    arrowprops=dict(arrowstyle="-|>", color="#2166ac",
                                    lw=1.5, mutation_scale=12,
                                    shrinkA=0, shrinkB=2))

    fig.tight_layout()
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved: {out_path.name}")


# ── Figure 3: Spatial Fair CRPSS maps ────────────────────────────

def figure3_crpss_maps(data, out_path):
    """Spatial Fair CRPSS at weeks 2, 4, 6 (bias-corrected)."""
    lons = data["lons"]
    lats = data["lats"]
    lons_2d, lats_2d = np.meshgrid(lons, lats)

    import cmcrameri.cm as cmc
    levels = [-0.4, -0.3, -0.2, -0.1, -0.05,
               0.0,
               0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
    cmap = cmc.vik_r
    norm = BoundaryNorm(levels, cmap.N)

    fig, axes = plt.subplots(1, 3, figsize=(6, 2.8),
                             subplot_kw={"projection": PROJ})
    fig.subplots_adjust(wspace=0.0)

    pcm = None
    for i, wk in enumerate(MAP_WEEKS):
        ax = axes[i]
        ax.set_extent(EXTENT, crs=ccrs.PlateCarree())

        crpss_data = data.get(f"crpss_{wk}")
        if crpss_data is not None:
            pcm = ax.pcolormesh(lons_2d, lats_2d, crpss_data,
                                cmap=cmap, norm=norm,
                                transform=ccrs.PlateCarree(), shading="auto")
            dm = data.get(f"crpss_mean_{wk}", 0)
            ax.text(0.03, 0.97, "$\\bar{{x}}$ = {:.2f}".format(dm),
                    transform=ax.transAxes,
                    fontsize=9, va="top",
                    bbox=dict(boxstyle="round,pad=0.2", fc="white",
                              alpha=0.85, edgecolor="none"))

        _mask_non_ireland(ax, PROJ)

        wk_num = WEEK_NUMS[PLOT_WEEKS.index(wk)]
        ax.set_title(f"Week {wk_num}")

    fig.subplots_adjust(bottom=0.22, top=0.95, wspace=0.0)

    # Horizontal colorbar dynamically centred under the three maps
    if pcm is not None:
        # Get the left edge of first axes and right edge of last axes
        pos_left = axes[0].get_position()
        pos_right = axes[-1].get_position()
        cbar_left = pos_left.x0
        cbar_right = pos_right.x0 + pos_right.width
        cbar_width = cbar_right - cbar_left
        cbar_ax = fig.add_axes([cbar_left, 0.10, cbar_width, 0.04])
        cbar = fig.colorbar(pcm, cax=cbar_ax, orientation="horizontal",
                            extend="both",
                            ticks=[-0.4, -0.2, -0.1, 0.0, 0.1, 0.2, 0.4])
        cbar.set_label("Fair CRPSS", fontweight="bold", fontsize=10)
        cbar.ax.tick_params(labelsize=8)
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved: {out_path.name}")


# ── Main ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", default="028", choices=["028", "075"],
                        help="Grid resolution (default: 028)")
    parser.add_argument("--no-cache", action="store_true",
                        help="Force recompute scores (ignore cache)")
    args = parser.parse_args()

    ds = load_dataset(args.grid)
    land_mask = ds.land_mask.values
    n_land = int(land_mask.sum())
    print(f"Land points: {n_land}")

    scores = load_or_compute(ds, land_mask, args.grid, force=args.no_cache)
    ds.close()

    print("\nGenerating poster figures...")
    figure1_acc_leadtime(scores, POSTER_DIR / "poster_fig_acc.png")
    figure2_rank_histograms(scores, POSTER_DIR / "poster_fig_rankhist.png")
    figure3_crpss_maps(scores, POSTER_DIR / "poster_fig_crpss.png")

    print("\nDone.")


def load_dataset(grid):
    """Load the analysis dataset for the specified grid."""
    ds_path = (_REPO / "DATA" / "PROCESSED" / f"SPATIAL_{grid}" / "ANALYSIS" / "t2m"
               / f"eefh_reforecasts_era5_{grid}_analysis.nc")
    if not ds_path.exists():
        print(f"ERROR: {ds_path} not found.")
        sys.exit(1)
    ds = xr.open_dataset(ds_path)
    print(f"Loaded: {ds_path.name}  dims={dict(ds.sizes)}")
    return ds


if __name__ == "__main__":
    main()
