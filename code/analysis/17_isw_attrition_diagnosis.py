#!/usr/bin/env python3
"""
EXP 17 BACKGROUND: attrition diagnosis
======================================

Status
------
Diagnostic script for the already-published Exp 17 result. This does not
change the closed ISW measurement, does not alter UNBLIND flags, and does not
rerun the stack estimator. It only reproduces the mask attrition bookkeeping:

  discarded if inner_valid_fraction < 0.7 or ring_valid_fraction < 0.7

Inputs are the same data products used by 17_isw_stacking_pipeline.py.

Outputs
-------
A CSV/JSON table with one row per void:

  gc, void_index, ra, dec, gal_l, gal_b, z, L, theta_v,
  inner_valid, ring_valid, masked_frac_inner, masked_frac_ring,
  max_masked_frac, discarded

No output is written unless --out-json or --out-csv is provided.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


NSIDE = 2048
H_LITTLE = 0.6797


@dataclass
class AttritionRow:
    gc: str
    void_index: int
    ra: float
    dec: float
    gal_l: float
    gal_b: float
    z: float
    L: float
    theta_v: float
    inner_valid: float
    ring_valid: float
    masked_frac_inner: float
    masked_frac_ring: float
    max_masked_frac: float
    discarded: bool


def require_runtime():
    try:
        import healpy as hp  # type: ignore
        from astropy.io import fits  # type: ignore
        from astropy.coordinates import SkyCoord  # type: ignore
        import astropy.units as u  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "Missing runtime dependency for Exp 17 attrition diagnosis: "
            f"{exc}. Run in the same WSL/Python environment used for "
            "17_isw_stacking_pipeline.py."
        ) from exc
    return hp, fits, SkyCoord, u


def redshift_from_comoving_mpc_h(rcom_mpc_h: np.ndarray) -> np.ndarray:
    zg = np.linspace(0.0, 0.35, 400)
    om = 0.315
    ez = np.sqrt(om * (1.0 + zg) ** 3 + 1.0 - om)
    dc = np.concatenate(
        ([0.0], np.cumsum((1.0 / ez[:-1] + 1.0 / ez[1:]) * 0.5 * np.diff(zg)))
    ) * (299792.458 / 67.36)
    return np.interp(rcom_mpc_h / H_LITTLE, dc, zg)


def load_void_catalog(data_dir: Path):
    _, fits, _, _ = require_runtime()
    rows = []
    for gc in ("NGC", "SGC"):
        path = data_dir / f"DESIVAST_BGS_VOLLIM_VoidFinder_{gc}.fits"
        with fits.open(path, memmap=False) as hdul:
            d = hdul["MAXIMALS"].data
            ok = d["EDGE"] == 0
            ra = np.asarray(d["RA"][ok] % 360.0, dtype=float)
            dec = np.asarray(d["DEC"][ok], dtype=float)
            rcom = np.asarray(d["R"][ok], dtype=float)
            reff = np.asarray(d["R_EFF"][ok], dtype=float)
            z = redshift_from_comoving_mpc_h(rcom)
            L = reff / H_LITTLE
            theta_v = reff / rcom
            for i in range(len(ra)):
                rows.append(
                    {
                        "gc": gc,
                        "void_index": i,
                        "ra": float(ra[i]),
                        "dec": float(dec[i]),
                        "z": float(z[i]),
                        "L": float(L[i]),
                        "theta_v": float(theta_v[i]),
                    }
                )
    return rows


def load_mask(planck_fits: Path):
    hp, fits, _, _ = require_runtime()
    with fits.open(planck_fits, memmap=False) as hdul:
        # Exp 17 used the FITS-provided TMASK. Keep this explicit so failures
        # reveal a provenance mismatch instead of silently picking a map.
        mask = None
        for hdu in hdul:
            names = getattr(hdu, "columns", None)
            if names is None:
                continue
            if "TMASK" in names.names:
                mask = np.asarray(hdu.data["TMASK"], dtype=float)
                break
        if mask is None:
            raise ValueError(f"TMASK column not found in {planck_fits}")
    expected = hp.nside2npix(NSIDE)
    if len(mask) != expected:
        raise ValueError(f"TMASK has {len(mask)} pixels, expected {expected}")
    return mask


def galactic_coords(ra: float, dec: float) -> tuple[float, float]:
    _, _, SkyCoord, u = require_runtime()
    c = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs").galactic
    return float(c.l.deg), float(c.b.deg)


def patch_valid_fractions(mask: np.ndarray, ra: float, dec: float, theta_v: float):
    hp, _, _, _ = require_runtime()
    vec = hp.ang2vec(np.radians(90.0 - dec), np.radians(ra))
    inner = hp.query_disc(NSIDE, vec, theta_v)
    outer = hp.query_disc(NSIDE, vec, theta_v * np.sqrt(2.0))
    ring = np.setdiff1d(outer, inner, assume_unique=True)
    if len(inner) == 0 or len(ring) == 0:
        return 0.0, 0.0
    return float(mask[inner].mean()), float(mask[ring].mean())


def diagnose(data_dir: Path, planck_fits: Path) -> list[AttritionRow]:
    mask = load_mask(planck_fits)
    rows = []
    for void in load_void_catalog(data_dir):
        inner_valid, ring_valid = patch_valid_fractions(
            mask, void["ra"], void["dec"], void["theta_v"]
        )
        masked_inner = 1.0 - inner_valid
        masked_ring = 1.0 - ring_valid
        gal_l, gal_b = galactic_coords(void["ra"], void["dec"])
        rows.append(
            AttritionRow(
                gc=void["gc"],
                void_index=void["void_index"],
                ra=void["ra"],
                dec=void["dec"],
                gal_l=gal_l,
                gal_b=gal_b,
                z=void["z"],
                L=void["L"],
                theta_v=void["theta_v"],
                inner_valid=inner_valid,
                ring_valid=ring_valid,
                masked_frac_inner=masked_inner,
                masked_frac_ring=masked_ring,
                max_masked_frac=max(masked_inner, masked_ring),
                discarded=(inner_valid < 0.7 or ring_valid < 0.7),
            )
        )
    return rows


def summarize(rows: list[AttritionRow]) -> dict:
    total = len(rows)
    discarded = sum(r.discarded for r in rows)
    by_gc = {}
    for gc in sorted({r.gc for r in rows}):
        sub = [r for r in rows if r.gc == gc]
        by_gc[gc] = {
            "total": len(sub),
            "discarded": sum(r.discarded for r in sub),
            "retained": sum(not r.discarded for r in sub),
            "discard_fraction": sum(r.discarded for r in sub) / len(sub) if sub else None,
        }
    abs_b = np.asarray([abs(r.gal_b) for r in rows], dtype=float)
    max_masked = np.asarray([r.max_masked_frac for r in rows], dtype=float)
    return {
        "status": "BACKGROUND_DIAGNOSTIC_ONLY",
        "criterion": "discard if inner_valid < 0.7 or ring_valid < 0.7",
        "total": total,
        "discarded": discarded,
        "retained": total - discarded,
        "discard_fraction": discarded / total if total else None,
        "by_gc": by_gc,
        "abs_gal_b_quantiles": np.quantile(abs_b, [0.05, 0.25, 0.5, 0.75, 0.95]).tolist()
        if total
        else [],
        "max_masked_quantiles": np.quantile(max_masked, [0.05, 0.25, 0.5, 0.75, 0.95]).tolist()
        if total
        else [],
    }


def write_csv(path: Path, rows: list[AttritionRow]) -> None:
    import csv

    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(asdict(rows[0]).keys()) if rows else list(AttritionRow.__dataclass_fields__)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=Path("/home/hermes/exp1data"))
    parser.add_argument(
        "--planck-fits",
        type=Path,
        default=Path("/home/hermes/exp1data/COM_CMB_IQU-smica_2048_R3.00_full.fits"),
    )
    parser.add_argument("--out-json", type=Path, default=None)
    parser.add_argument("--out-csv", type=Path, default=None)
    parser.add_argument("--expect-discarded", type=int, default=1029)
    parser.add_argument("--expect-retained", type=int, default=460)
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    rows = diagnose(args.data_dir, args.planck_fits)
    summary = summarize(rows)
    summary["expected"] = {
        "discarded": args.expect_discarded,
        "retained": args.expect_retained,
        "matches_discarded": summary["discarded"] == args.expect_discarded,
        "matches_retained": summary["retained"] == args.expect_retained,
    }
    payload = {"summary": summary, "rows": [asdict(r) for r in rows]}
    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.out_csv:
        write_csv(args.out_csv, rows)
    print(json.dumps(summary, indent=2))
    return 0 if summary["expected"]["matches_discarded"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
