"""
compute_poster_data.py — precompute poster figure data from S2S_AI analysis datasets.

Runs once (slow: loads ~1.3GB netCDF), caches results to poster_data.pkl.
Subsequent plotting reads only the small cache file.

Usage:
    conda run -n S2S_AI python -u compute_poster_data.py
"""

import sys
from pathlib import Path
import pickle
import numpy as np

# Force unbuffered output (conda run buffers stdout)
sys.stdout.reconfigure(line_buffering=True)

# ── Paths ────────────────────────────────────────────────────────
S2S_ROOT = Path.home() / "Documents" / "Github" / "S2S_AI"
sys.path.insert(0, str(S2S_ROOT / "CONFIG"))
sys.path.insert(0, str(S2S_ROOT / "SCRIPTS" / "UTILS"))

from variable_config import LEAD_WEEKS
from scoring_spatial_native import (
    gridded_crps, gridded_acc, gridded_bias, subset_by_season,
)
import xarray as xr

DATA_DIR = S2S_ROOT / "DATA" / "PROCESSED" / "SPATIAL_NATIVE" / "ANALYSIS" / "t2m"
EEFH_FILE = DATA_DIR / "eefh_reforecasts_era5_native_analysis.nc"
OUT_FILE = Path(__file__).parent / "poster_data.pkl"

WEEKS_TO_SCORE = ["wk2", "wk3", "wk4", "wk5", "wk6"]
SPATIAL_WEEKS = ["wk2", "wk4", "wk6"]
SEASONS = {"Annual": None, "DJF": "DJF", "JJA": "JJA"}


def domain_mean(da, ds):
    """Area-weighted domain mean of a DataArray over land points."""
    vals = da.values
    if "cell_area" in ds:
        area = ds["cell_area"].values
        land = ds["land_mask"].values if "land_mask" in ds else np.ones(len(area), dtype=bool)
        valid = np.isfinite(vals) & land
        if not valid.any():
            return np.nan
        return float(np.average(vals[valid], weights=area[valid]))
    return float(np.nanmean(vals))


def extract_spatial(da):
    """Extract values, lat, lon arrays from a scored DataArray."""
    return {
        "values": da.values,
        "latitude": da.coords["latitude"].values,
        "longitude": da.coords["longitude"].values,
    }


def main():
    print("Loading dataset...", flush=True)
    ds = xr.open_dataset(EEFH_FILE)
    print(f"  Dims: {dict(ds.dims)}", flush=True)

    data = {
        "weeks": WEEKS_TO_SCORE,
        "week_numbers": [int(wk[2:]) for wk in WEEKS_TO_SCORE],
        "spatial_weeks": SPATIAL_WEEKS,
    }

    # ── Domain-mean scores by season ──
    for season_label, season_key in SEASONS.items():
        print(f"\n── {season_label} ──", flush=True)
        ds_sub = subset_by_season(ds, season_key) if season_key else ds
        n_inits = ds_sub.dims["init"]
        print(f"  {n_inits} initialisations", flush=True)

        acc_vals, crpss_vals = [], []
        for wk in WEEKS_TO_SCORE:
            print(f"  {wk}...", end=" ", flush=True)

            acc_da = gridded_acc(ds_sub, wk, variant="ensmean")
            acc_mean = domain_mean(acc_da, ds_sub) if acc_da is not None else np.nan

            crps_result = gridded_crps(ds_sub, wk, bias_correct=True)
            crpss_mean = domain_mean(crps_result["crpss"], ds_sub) if crps_result else np.nan

            acc_vals.append(acc_mean)
            crpss_vals.append(crpss_mean)
            print(f"ACC={acc_mean:.3f}  CRPSS={crpss_mean:.3f}", flush=True)

        data[f"acc_{season_label}"] = acc_vals
        data[f"crpss_{season_label}"] = crpss_vals

    # ── Spatial maps (annual, weeks 2/4/6): CRPSS + Bias ──
    print("\n── Spatial maps (CRPSS + Bias) ──", flush=True)
    spatial_crpss = {}
    spatial_bias = {}

    for wk in SPATIAL_WEEKS:
        print(f"  {wk} CRPSS...", end=" ", flush=True)
        crps_result = gridded_crps(ds, wk, bias_correct=True)
        if crps_result is not None:
            spatial_crpss[wk] = extract_spatial(crps_result["crpss"])
            print(f"mean={np.nanmean(crps_result['crpss'].values):.3f}", flush=True)

        print(f"  {wk} Bias...", end=" ", flush=True)
        bias_da = gridded_bias(ds, wk, variant="ensmean")
        if bias_da is not None:
            spatial_bias[wk] = extract_spatial(bias_da)
            print(f"mean={np.nanmean(bias_da.values):.2f} C", flush=True)

    data["spatial_crpss"] = spatial_crpss
    data["spatial_bias"] = spatial_bias

    # ── Save ──
    with open(OUT_FILE, "wb") as f:
        pickle.dump(data, f)
    print(f"\nDone. Saved {OUT_FILE.name} ({OUT_FILE.stat().st_size / 1024:.0f} KB)")

    ds.close()


if __name__ == "__main__":
    main()
