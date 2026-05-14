#!/usr/bin/env python3
"""
generate_poster_figures.py — Produce the three Results figures for the
Met Éireann Symposium poster from the native O320 analysis dataset.

Figures:
  1. Spatial anomaly RMSE maps (Weeks 2, 4, 6 — earthkit grid_cells, PlateCarree)
  2. Centered ACC vs lead time (spatial ACC, Annual/DJF/JJA)
  3. Domain-mean CRPSS vs lead time (Annual/DJF/JJA, no bias correction)
  4. JJA rank histogram (pooled wk2–wk6, no bias correction)

All scoring uses anomaly fields. No bias correction is applied.

Two-phase design:
  - Scoring is slow (~60 min) and cached to poster_scores_native.pkl
  - Plotting reads the cache only — fast re-edits without rescoring

Usage:
    conda run -n S2S_AI python generate_poster_figures.py              # plot from cache
    conda run -n S2S_AI python generate_poster_figures.py --no-cache   # force rescore
    conda run -n S2S_AI python generate_poster_figures.py --plot-only  # skip scoring entirely
"""
import sys
import pickle
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr
import eccodes
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
from shapely.ops import unary_union
from shapely.geometry import Point

# ── Poster-matching font setup (Latin Modern Sans via LaTeX) ──────
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "text.latex.preamble": r"\usepackage{lmodern}\renewcommand{\familydefault}{\sfdefault}",
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

from scoring_spatial_native import (
    gridded_rmse, gridded_crps, spatial_acc, subset_by_season,
    gridded_rank_histogram, _weekly_means, select_week, build_common_mask,
    _get_variant,
)
from _scoring_common import count_unique_days

# ── Config ───────────────────────────────────────────────────────
PLOT_WEEKS = ["wk2", "wk3", "wk4", "wk5", "wk6"]
WEEK_NUMS = [int(wk[2:]) for wk in PLOT_WEEKS]
MAP_WEEKS = ["wk2", "wk4", "wk6"]
MAP_WEEK_NUMS = [int(wk[2:]) for wk in MAP_WEEKS]
DPI = 300
CACHE_PATH = POSTER_DIR / "poster_scores_native.pkl"

# GRIB template for earthkit plotting (native O320 grid structure)
GRIB_TEMPLATE = _REPO / "DATA" / "RAW" / "EEFH_NATIVE" / "lsm" / "eefh_lsm_native.grib"

# Forecast climatology (model climate) for model-referenced anomalies
FC_CLIM_PATH = (_REPO / "DATA" / "PROCESSED" / "SPATIAL_NATIVE" / "EEFH_O320"
                / "fc_clim_t2m_eefh_o320.nc")

# Poster colours
C_ANN = "#1B2A4A"   # posternavy
C_DJF = "#4A90D9"   # blue
C_JJA = "#E8943A"   # orange

# earthkit map domain (cylindrical / PlateCarree)
IRELAND_DOMAIN = [-10.8, -5.2, 51.2, 55.7]

# ── Ireland shapefile mask (Republic + NI, includes lakes) ───────
_ne_sub = shpreader.natural_earth(
    resolution="10m", category="cultural", name="admin_0_map_subunits")
_rd_sub = shpreader.Reader(_ne_sub)
IRELAND_SHAPE = unary_union([
    r.geometry for r in _rd_sub.records()
    if r.attributes.get("NAME", "") in ("Ireland", "N. Ireland")
    or r.attributes.get("SU_A3", "") in ("IRL", "NIR")
])
IRELAND_BUF = IRELAND_SHAPE.buffer(0.15)


def _fix_lons(lons):
    return np.where(lons > 180, lons - 360, lons)


def _ireland_mask(lats, lons):
    """Boolean mask: True for points within buffered Ireland shapefile."""
    lons_plot = _fix_lons(lons)
    return np.array([IRELAND_BUF.contains(Point(lo, la))
                     for lo, la in zip(lons_plot, lats)])


def _domain_mean(da, ds):
    """Area-weighted domain mean over land points."""
    vals = da.values
    area = ds["cell_area"].values
    land = ds["land_mask"].values
    valid = np.isfinite(vals) & land
    if not valid.any():
        return np.nan
    return float(np.average(vals[valid], weights=area[valid]))


# ── Scoring (slow, cached) ──────────────────────────────────────

def _load_fc_clim():
    """Load the forecast climatology (model climate) for model-referenced anomalies."""
    if not FC_CLIM_PATH.exists():
        print(f"WARNING: {FC_CLIM_PATH.name} not found. Run Process_Spatial_Native.ipynb Section 7 first.")
        return None
    return xr.open_dataset(FC_CLIM_PATH)


def _model_anomaly_weekly_means(ds, fc_clim_ds, wk, variant="ensmean"):
    """Compute weekly-mean model-referenced forecast anomalies and ERA5-referenced obs anomalies.

    fc_anom_model = fc_raw(ensmean) - fc_clim (model climate, by init DOY + lead)
    obs_anom = obs_raw - era5_clim (already in dataset)

    Returns (fc_anom_model_wm, obs_anom_wm) or (None, None).
    """
    d = select_week(ds, wk)
    if count_unique_days(d) < 7:
        return None, None

    mask = build_common_mask(d)

    # Obs anomaly (ERA5-referenced) — already in dataset
    obs_anom_vals = d["obs_anom"].values
    obs_anom_masked = np.where(mask, obs_anom_vals, np.nan)

    # Forecast ensmean raw
    fc_raw = _get_variant(d, "fc_raw", variant)
    fc_raw_masked = np.where(mask, fc_raw, np.nan)

    # Sample fc_clim for each init's DOY and the relevant leads
    init_dt = pd.DatetimeIndex(d["init"].values)
    init_doys_raw = init_dt.dayofyear
    is_leap = init_dt.is_leap_year
    init_doys = np.where(is_leap & (init_doys_raw > 59), init_doys_raw - 1, init_doys_raw)

    lead_indices = d["lead"].values
    fc_clim_da = fc_clim_ds["t2m"]

    # Build fc_clim_3d: (init, lead, values)
    n_init = len(init_dt)
    n_lead = len(lead_indices)
    n_values = d.sizes["values"]
    fc_clim_3d = np.full((n_init, n_lead, n_values), np.nan)
    for i, doy in enumerate(init_doys):
        fc_clim_3d[i] = fc_clim_da.sel(init_doy=int(doy)).isel(
            lead=lead_indices).values

    fc_clim_masked = np.where(mask, fc_clim_3d, np.nan)

    # Model-referenced forecast anomaly
    fc_anom_model = fc_raw_masked - fc_clim_masked

    # Weekly mean: average over lead dim
    with np.errstate(all="ignore"):
        fc_anom_model_wm = np.nanmean(fc_anom_model, axis=1)
        obs_anom_wm = np.nanmean(obs_anom_masked, axis=1)

    # Filter to inits with data
    any_valid = mask.any(axis=1).any(axis=1)
    valid_inits = np.where(any_valid)[0]
    if len(valid_inits) == 0:
        return None, None

    return fc_anom_model_wm[valid_inits], obs_anom_wm[valid_inits]


def compute_scores(ds):
    """Compute all scores for the four poster figures. No bias correction.

    Uses separate climatologies for anomaly metrics:
    - Forecast anomaly: fc_raw - model_climate (forecast climatology)
    - Observed anomaly: obs_raw - era5_climate (ERA5 climatology)
    """
    land_mask = ds["land_mask"].values
    lats = ds["latitude"].values
    lons = ds["longitude"].values

    data = {
        "lats": lats,
        "lons": lons,
        "land_mask": land_mask,
        "ireland_mask": _ireland_mask(lats, lons),
    }

    # Load forecast climatology for model-referenced anomalies
    fc_clim_ds = _load_fc_clim()
    if fc_clim_ds is None:
        print("ERROR: Cannot compute anomaly scores without forecast climatology.")
        sys.exit(1)

    # Spatial ACC and domain-mean CRPSS per season
    for season_label, season_key in [("Annual", None), ("DJF", "DJF"), ("JJA", "JJA")]:
        ds_sub = subset_by_season(ds, season_key) if season_key else ds
        n_inits = ds_sub.sizes["init"]
        print(f"\n── {season_label} ({n_inits} inits) ──")

        sacc_vals = []
        bias_vals = []
        crpss_vals = []
        for wk in PLOT_WEEKS:
            print(f"  {wk}...", end=" ", flush=True)

            # ACC and Bias using model-referenced fc anomalies and ERA5-referenced obs anomalies
            fc_anom_m_wm, obs_anom_wm = _model_anomaly_weekly_means(
                ds_sub, fc_clim_ds, wk, variant="ensmean")
            if fc_anom_m_wm is not None:
                sacc_val = spatial_acc(
                    fc_anom_wm=fc_anom_m_wm, obs_anom_wm=obs_anom_wm,
                    cell_area=ds_sub["cell_area"].values)
                sacc_val = float(sacc_val) if sacc_val is not None else np.nan

                # Domain-mean anomaly bias: mean(fc_anom - obs_anom) over land
                error = fc_anom_m_wm - obs_anom_wm
                bias_per_gp = np.nanmean(error, axis=0)  # (values,)
                bias_val = float(np.nanmean(bias_per_gp[land_mask]))
            else:
                sacc_val = np.nan
                bias_val = np.nan
            sacc_vals.append(sacc_val)
            bias_vals.append(bias_val)

            # CRPSS — invariant to constant shift, uses raw values
            crps_result = gridded_crps(ds_sub, wk, bias_correct=False)
            crpss_mean = _domain_mean(crps_result["crpss"], ds_sub) if crps_result else np.nan
            crpss_vals.append(crpss_mean)

            print(f"sACC={sacc_val:.3f}  Bias={bias_val:+.3f}  CRPSS={crpss_mean:.3f}")

        data[f"sacc_{season_label}"] = sacc_vals
        data[f"bias_{season_label}"] = bias_vals
        data[f"crpss_{season_label}"] = crpss_vals

    # Spatial anomaly RMSE at each gridpoint (annual, weeks 2/4/6)
    # Model-referenced fc anomaly vs ERA5-referenced obs anomaly
    print("\n── Spatial anomaly RMSE maps (model vs ERA5 clim) ──")
    for wk in MAP_WEEKS:
        print(f"  {wk}...", end=" ", flush=True)
        fc_anom_m_wm, obs_anom_wm = _model_anomaly_weekly_means(
            ds, fc_clim_ds, wk, variant="ensmean")
        if fc_anom_m_wm is not None:
            rmse_anom = np.sqrt(np.nanmean(
                (fc_anom_m_wm - obs_anom_wm) ** 2, axis=0))
            data[f"rmse_{wk}"] = rmse_anom
            data[f"rmse_mean_{wk}"] = float(np.nanmean(rmse_anom[land_mask]))
            print(f"mean={data[f'rmse_mean_{wk}']:.2f} °C")
        else:
            print("no data")

    fc_clim_ds.close()

    # JJA rank histogram (pooled across weeks 2–6, no bias correction)
    # Rank is invariant to constant shift — uses raw values, correct as-is
    print("\n── JJA rank histogram ──")
    ds_jja = subset_by_season(ds, "JJA")
    rh_counts_all = []
    n_total = 0
    for wk in PLOT_WEEKS:
        rh = gridded_rank_histogram(ds_jja, wk, bias_correct=False)
        if rh is not None:
            rh_counts_all.append(rh["ranks"])
            n_total += rh["n_samples"]
            print(f"  {wk}: {rh['n_samples']} samples")
    if rh_counts_all:
        data["rh_jja_counts"] = np.sum(rh_counts_all, axis=0)
        data["rh_jja_n"] = n_total
        data["rh_jja_n_members"] = rh["n_members"]
        print(f"  Total: {n_total} samples, {rh['n_members']} members")

    return data


def load_or_compute(ds, force=False):
    """Load cached scores or recompute."""
    if CACHE_PATH.exists() and not force:
        print(f"Loading cached scores from {CACHE_PATH.name}")
        with open(CACHE_PATH, "rb") as f:
            return pickle.load(f)

    print("Computing scores (will be cached for next run)...")
    data = compute_scores(ds)
    with open(CACHE_PATH, "wb") as f:
        pickle.dump(data, f)
    print(f"Cached to {CACHE_PATH.name}")
    return data


# ── Figure 1: Spatial RMSE maps (earthkit grid_cells) ────────────

def _write_grib_from_template(values, ireland_mask, out_path):
    """Write a 251-point field to GRIB using the native O320 template.

    Non-Ireland points are set as GRIB missing values so earthkit
    skips them.
    """
    vals_out = values.copy().astype(np.float64)
    vals_out[~ireland_mask] = 9999.0

    with open(str(GRIB_TEMPLATE), "rb") as fin:
        msgid = eccodes.codes_grib_new_from_file(fin)
        eccodes.codes_set(msgid, "bitsPerValue", 16)
        eccodes.codes_set(msgid, "bitmapPresent", 1)
        eccodes.codes_set(msgid, "missingValue", 9999.0)
        eccodes.codes_set_values(msgid, vals_out)
        with open(str(out_path), "wb") as fout:
            eccodes.codes_write(msgid, fout)
        eccodes.codes_release(msgid)


def figure1_rmse_maps(data, out_path):
    """Spatial RMSE at weeks 2, 4, 6 — earthkit grid_cells, 3-panel figure."""
    import earthkit.data as ekd
    import earthkit.plots as ekp

    ireland_mask = data["ireland_mask"]
    tmp_grib = Path("/tmp/poster_rmse_native.grib")

    # Shared colourbar range across all weeks
    all_valid = []
    for wk in MAP_WEEKS:
        rmse_vals = data.get(f"rmse_{wk}")
        if rmse_vals is not None:
            v = rmse_vals[ireland_mask]
            all_valid.append(v[np.isfinite(v)])
    all_valid = np.concatenate(all_valid)
    vmin = float(np.floor(all_valid.min() * 10) / 10)
    vmax = float(np.ceil(all_valid.max() * 10) / 10)

    style = ekp.styles.Style(
        levels=np.linspace(vmin, vmax, 12).tolist(),
        colors="YlOrRd",
    )

    fig = ekp.Figure(rows=1, columns=len(MAP_WEEKS))

    for wk, wk_num in zip(MAP_WEEKS, MAP_WEEK_NUMS):
        rmse_vals = data.get(f"rmse_{wk}")
        if rmse_vals is None:
            continue

        _write_grib_from_template(rmse_vals, ireland_mask, tmp_grib)
        ek_data = ekd.from_source("file", str(tmp_grib))

        subplot = fig.add_map(domain=IRELAND_DOMAIN)
        subplot.grid_cells(ek_data[0], style=style)
        subplot.coastlines()
        subplot.title(f"Week {wk_num}")

    fig.legend(location="bottom")
    fig.save(str(out_path))
    print(f"  Saved: {out_path.name}")

    if tmp_grib.exists():
        tmp_grib.unlink()


# ── Figure 2: Centered ACC vs lead time ─────────────────────────

def figure2_acc_leadtime(data, out_path):
    """Spatial (centred) ACC vs lead time — annual, DJF, JJA."""
    fig, ax = plt.subplots(figsize=(6.0, 3.2))

    for label, color, marker in [
        ("Annual", C_ANN, "o"),
        ("DJF",    C_DJF, "s"),
        ("JJA",    C_JJA, "D"),
    ]:
        vals = data.get(f"sacc_{label}")
        if vals is not None:
            ax.plot(WEEK_NUMS, vals, "-", color=color, marker=marker,
                    ms=7, lw=2.5, label=label, zorder=3)

    ax.axhline(0.6, color="#555555", ls=(0, (8, 4)), lw=1.5, alpha=0.7, zorder=2)
    ax.text(4.0, 0.62, "useful skill", fontsize=13,
            color="#555555", va="bottom", fontstyle="italic")
    ax.axhline(0, color="grey", ls="-", lw=0.6, alpha=0.4)

    ax.set_xlabel("Week", fontsize=13)
    ax.set_ylabel("Centred ACC", fontsize=13)
    ax.set_xticks(WEEK_NUMS)
    ax.set_ylim(-0.15, 0.75)
    ax.tick_params(axis="both", labelsize=12)
    ax.legend(loc="center right", framealpha=0.9, fontsize=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", transparent=True)
    plt.close(fig)
    print(f"  Saved: {out_path.name}")


# ── Figure 2b: Domain-mean anomaly bias vs lead time ─────────────

def figure2b_bias_leadtime(data, out_path):
    """Domain-mean anomaly bias vs lead time — annual, DJF, JJA."""
    fig, ax = plt.subplots(figsize=(6.0, 3.2))

    for label, color, marker in [
        ("Annual", C_ANN, "o"),
        ("DJF",    C_DJF, "s"),
        ("JJA",    C_JJA, "D"),
    ]:
        vals = data.get(f"bias_{label}")
        if vals is not None:
            ax.plot(WEEK_NUMS, vals, "-", color=color, marker=marker,
                    ms=7, lw=2.5, label=label, zorder=3)

    ax.axhline(0, color="grey", ls="-", lw=0.6, alpha=0.4)

    ax.set_xlabel("Week", fontsize=13)
    ax.set_ylabel("Bias (\\textdegree C)", fontsize=13)
    ax.set_xticks(WEEK_NUMS)
    ax.set_xlim(WEEK_NUMS[0] - 0.3, WEEK_NUMS[-1] + 0.3)
    ax.tick_params(axis="both", labelsize=12)
    ax.legend(loc="best", framealpha=0.9, fontsize=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", transparent=True)
    plt.close(fig)
    print(f"  Saved: {out_path.name}")


# ── Figure 3: Domain-mean CRPSS vs lead time ────────────────────

def figure3_crpss_leadtime(data, out_path):
    """Domain-mean CRPSS vs lead time — annual, DJF, JJA (no bias correction)."""
    fig, ax = plt.subplots(figsize=(6.0, 3.2))

    for label, color, marker in [
        ("Annual", C_ANN, "o"),
        ("DJF",    C_DJF, "s"),
        ("JJA",    C_JJA, "D"),
    ]:
        vals = data.get(f"crpss_{label}")
        if vals is not None:
            ax.plot(WEEK_NUMS, vals, "-", color=color, marker=marker,
                    ms=7, lw=2.5, label=label, zorder=3)

    ax.axhline(0, color="grey", ls="--", lw=0.8, alpha=0.7, zorder=1)
    ax.text(WEEK_NUMS[-1] + 0.25, 0.01, "climatology", fontsize=9,
            color="#555555", va="bottom", ha="right")

    ax.set_xlabel("Week", fontsize=13)
    ax.set_ylabel("CRPSS", fontsize=13)
    ax.set_xticks(WEEK_NUMS)
    ax.set_xlim(WEEK_NUMS[0] - 0.3, WEEK_NUMS[-1] + 0.3)
    ax.tick_params(axis="both", labelsize=12)
    ax.legend(loc="upper right", framealpha=0.9, fontsize=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.25, lw=0.5)

    fig.tight_layout()
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", transparent=True)
    plt.close(fig)
    print(f"  Saved: {out_path.name}")


# ── Figure 4: JJA rank histogram ─────────────────────────────────

def figure4_rank_histogram(data, out_path):
    """JJA rank histogram (pooled wk2–wk6, land only, no bias correction)."""
    counts = data.get("rh_jja_counts")
    if counts is None:
        print("  Skipping rank histogram (no data)")
        return

    n_total = data["rh_jja_n"]
    n_members = data["rh_jja_n_members"]
    n_ranks = len(counts)
    uniform = n_total / n_ranks

    fig, ax = plt.subplots(figsize=(5.0, 2.8))
    ax.bar(np.arange(1, n_ranks + 1), counts / 1e3,
           color="#E8943A", alpha=0.85, edgecolor="white", linewidth=0.4)
    ax.axhline(uniform / 1e3, color="#555555", ls="--", lw=1.5, alpha=0.7)

    ax.set_xlabel("Rank", fontsize=12)
    ax.set_ylabel("Count ($\\times 10^3$)", fontsize=12)
    ax.set_xticks([1, 4, 8, 12])
    ax.tick_params(axis="both", labelsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", transparent=True)
    plt.close(fig)
    print(f"  Saved: {out_path.name}")


# ── Main ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-cache", action="store_true",
                        help="Force recompute scores (ignore cache)")
    parser.add_argument("--plot-only", action="store_true",
                        help="Plot from existing cache (no dataset needed)")
    args = parser.parse_args()

    if args.plot_only:
        if not CACHE_PATH.exists():
            print(f"ERROR: {CACHE_PATH.name} not found. Run without --plot-only first.")
            sys.exit(1)
        with open(CACHE_PATH, "rb") as f:
            scores = pickle.load(f)
    else:
        ds = load_dataset()
        n_land = int(ds["land_mask"].values.sum())
        print(f"Land points: {n_land}")
        scores = load_or_compute(ds, force=args.no_cache)
        ds.close()

    # Ensure ireland_mask is in the cache (for earthkit plotting)
    if "ireland_mask" not in scores:
        scores["ireland_mask"] = _ireland_mask(scores["lats"], scores["lons"])

    print("\nGenerating poster figures...")
    figure1_rmse_maps(scores, POSTER_DIR / "poster_fig_rmse.png")
    figure2_acc_leadtime(scores, POSTER_DIR / "poster_fig_acc.png")
    figure2b_bias_leadtime(scores, POSTER_DIR / "poster_fig_bias.png")
    figure3_crpss_leadtime(scores, POSTER_DIR / "poster_fig_crpss.png")
    figure4_rank_histogram(scores, POSTER_DIR / "poster_fig_rankhist_jja.png")

    print("\nDone.")


def load_dataset():
    """Load the native O320 analysis dataset."""
    ds_path = (_REPO / "DATA" / "PROCESSED" / "SPATIAL_NATIVE" / "ANALYSIS" / "t2m"
               / "eefh_reforecasts_era5_native_analysis.nc")
    if not ds_path.exists():
        print(f"ERROR: {ds_path} not found.")
        sys.exit(1)
    ds = xr.open_dataset(ds_path)
    print(f"Loaded: {ds_path.name}  dims={dict(ds.sizes)}")
    return ds


if __name__ == "__main__":
    main()
