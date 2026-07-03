#!/usr/bin/env python3
"""
EXP 20: BAO + Pantheon+ + DES-Y5 combined falsifier
===================================================

PRE-REGISTRATION SKELETON

Question
--------
Does the direct R(t) power-law model that survived DESI BAO-only tension
continue to fit when supernova distances are added?

Model
-----
R(t) = R0 * (t/t0)^beta
rho_DE(z)/rho_DE(0) = (t(z)/t0)^(-4 beta)
E^2(z) = Om*(1+z)^3 + Or*(1+z)^4
       + (1-Om-Or)*(t(z)/t0)^(-4 beta)

beta = 0 is exact LCDM and is nested in the model.

Data
----
1. DESI DR2 BAO 13-point vector with covariance from Exp 15.
2. Pantheon+ SNe: external catalog + covariance.
3. DES-Y5 SNe: external catalog + covariance.

This script intentionally does NOT ship Pantheon+/DES-Y5 numbers inline.
The final run must point to the archived catalog files used by Fable/Patricio.

Parameters
----------
Cosmology:
  Om, beta

Profiled nuisance parameters:
  s_bao = c/(H0*r_d) for BAO absolute scale
  M_sn or intercept for each SN catalog

Optional Gaussian prior:
  Om = 0.3111 +/- 0.0056

Pre-registered outputs
----------------------
R1. beta_hat with 68% and 95% profile intervals.
R2. Delta chi2 = chi2_LCDM - chi2_beta.
R3. Per-dataset chi2 at beta_hat and at beta=0.
R4. Consistency pull between BAO-only beta and SN+BAO beta.
R5. Posterior status of beta>=0 at 95%.

Success criteria
----------------
S1. Combined fit keeps beta>0 inside the 68% interval.
S2. LCDM is not strongly preferred over beta-law:
    chi2(beta_hat) <= chi2(beta=0) + 2.
S3. No dataset has an individual degradation Delta chi2 > 4 relative
    to its own LCDM-profiled best fit.

Failure criteria
----------------
F1. Combined fit prefers beta<0 at >=95%.
F2. LCDM improves over beta-law by Delta chi2 >= 4.
F3. Either SN catalog rejects the BAO-preferred beta by Delta chi2 >= 9
    after profiling its intercept.
F4. Pantheon+ and DES-Y5 prefer mutually inconsistent beta values at >3 sigma.

Commitment
----------
Publish the result either way.  If BAO+SNe kills beta>0, the R(t) dark-energy
branch is removed from the active claims and kept only as a documented failure.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np


# ----------------------------- BAO: DESI DR2 -----------------------------
# (z, type, value); type: 0=DV/rd, 1=DM/rd, 2=DH/rd
BAO_DATA = [
    (0.295, 0, 7.942),
    (0.510, 1, 13.588), (0.510, 2, 21.863),
    (0.706, 1, 17.351), (0.706, 2, 19.455),
    (0.934, 1, 21.576), (0.934, 2, 17.641),
    (1.321, 1, 27.601), (1.321, 2, 14.176),
    (1.484, 1, 30.512), (1.484, 2, 12.817),
    (2.330, 2, 8.632),  (2.330, 1, 38.989),
]

BAO_COV = np.zeros((13, 13))
_bao_diag = [
    5.78998687e-03, 2.83473742e-02, 1.83928040e-01,
    3.23752442e-02, 1.11469198e-01, 2.61732816e-02,
    4.04183878e-02, 1.05336516e-01, 5.04233092e-02,
    5.83020277e-01, 2.68336193e-01, 1.02136194e-02,
    2.82685779e-01,
]
_bao_off = {
    (1, 2): -3.26062007e-02,
    (3, 4): -2.37445646e-02,
    (5, 6): -1.12938006e-02,
    (7, 8): -2.90308418e-02,
    (9, 10): -1.95215562e-01,
    (11, 12): -2.31395216e-02,
}
for _i, _v in enumerate(_bao_diag):
    BAO_COV[_i, _i] = _v
for (_i, _j), _v in _bao_off.items():
    BAO_COV[_i, _j] = BAO_COV[_j, _i] = _v


OR_RAD = 9.0e-5
NX = 700
XMAX = np.log(1.0 + 3000.0)
XG = np.linspace(0.0, XMAX, NX)
ZG = np.expm1(XG)
DX = XG[1] - XG[0]


@dataclass
class SNDataset:
    name: str
    z: np.ndarray
    mu: np.ndarray
    cov: np.ndarray
    data_path: Path
    cov_path: Path | None
    provenance: dict

    @property
    def cinv(self) -> np.ndarray:
        return np.linalg.inv(self.cov)


def load_provenance(path: Path | None) -> dict | None:
    """Load and minimally validate dataset provenance metadata."""
    if path is None:
        return None
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"provenance file not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    required = ["catalog", "version", "doi_or_url", "license_or_terms", "retrieved_or_frozen"]
    missing = [k for k in required if not str(data.get(k, "")).strip()]
    if missing:
        raise ValueError(f"{path}: missing provenance fields: {', '.join(missing)}")
    return data


def load_sn_catalog(
    name: str,
    data_path: Path | None,
    cov_path: Path | None,
    provenance_path: Path | None,
) -> SNDataset | None:
    """Load a supernova catalog with columns z, mu and optional covariance.

    Accepted data formats:
      - CSV/whitespace with columns named z and mu
      - CSV/whitespace with first two numeric columns interpreted as z, mu

    Accepted covariance formats:
      - .npy or .npz square matrix
      - text/csv square matrix
      - absent: use diagonal sigma_mu column if present, else raise
    """
    if data_path is None:
        return None
    provenance = load_provenance(provenance_path)
    if provenance is None:
        raise ValueError(
            f"{name}: provenance JSON is required before any dry-run or fit "
            "(catalog, version, DOI/URL, license/terms, frozen date)."
        )
    data_path = Path(data_path)
    if not data_path.exists():
        raise FileNotFoundError(f"{name} catalog not found: {data_path}")

    raw = np.genfromtxt(data_path, names=True, delimiter=",", dtype=None, encoding=None)
    if raw.dtype.names is None:
        arr = np.loadtxt(data_path)
        z, mu = arr[:, 0], arr[:, 1]
        sigma = arr[:, 2] if arr.shape[1] >= 3 else None
    else:
        names = {n.lower(): n for n in raw.dtype.names}
        z_key = names.get("z") or names.get("zcmb") or names.get("zhel")
        mu_key = names.get("mu") or names.get("mub") or names.get("distmod")
        sig_key = names.get("sigma_mu") or names.get("muerr") or names.get("dmu")
        if z_key is None or mu_key is None:
            raise ValueError(f"{name}: expected columns z and mu/distmod")
        z, mu = np.asarray(raw[z_key], float), np.asarray(raw[mu_key], float)
        sigma = np.asarray(raw[sig_key], float) if sig_key is not None else None

    if cov_path is not None:
        cov_path = Path(cov_path)
        if not cov_path.exists():
            raise FileNotFoundError(f"{name} covariance not found: {cov_path}")
        if cov_path.suffix == ".npy":
            cov = np.load(cov_path)
        elif cov_path.suffix == ".npz":
            loaded = np.load(cov_path)
            cov = loaded[loaded.files[0]]
        else:
            cov = np.loadtxt(cov_path, delimiter="," if cov_path.suffix == ".csv" else None)
    elif sigma is not None:
        cov = np.diag(sigma * sigma)
    else:
        raise ValueError(f"{name}: provide covariance or sigma_mu column")

    if cov.shape != (len(z), len(z)):
        raise ValueError(f"{name}: covariance shape {cov.shape} does not match N={len(z)}")
    return SNDataset(
        name=name,
        z=z,
        mu=mu,
        cov=cov,
        data_path=data_path,
        cov_path=Path(cov_path) if cov_path is not None else None,
        provenance=provenance,
    )


def covariance_summary(cov: np.ndarray) -> dict:
    diag = np.diag(np.diag(cov))
    offdiag_max = float(np.max(np.abs(cov - diag))) if cov.size else 0.0
    try:
        cond = float(np.linalg.cond(cov))
    except np.linalg.LinAlgError:
        cond = float("inf")
    return {
        "shape": list(cov.shape),
        "is_square": cov.ndim == 2 and cov.shape[0] == cov.shape[1],
        "is_diagonal": bool(np.allclose(cov, diag)),
        "max_abs_offdiag": offdiag_max,
        "condition_number": cond,
    }


def audit_inputs(sn_sets: list[SNDataset]) -> dict:
    """Return a dry-run audit payload for all external inputs."""
    audit = {
        "BAO_DESI_DR2": {
            "N": len(BAO_DATA),
            "cov_shape": list(BAO_COV.shape),
            "cov_condition_number": float(np.linalg.cond(BAO_COV)),
            "z_min": float(min(row[0] for row in BAO_DATA)),
            "z_max": float(max(row[0] for row in BAO_DATA)),
            "provenance_note": "Embedded from Exp 15 DESI DR2 likelihood values; final repo integration must cite exact release.",
        },
        "SNe": {},
    }
    for sn in sn_sets:
        cov_info = covariance_summary(sn.cov)
        ok_shape = sn.cov.shape == (len(sn.z), len(sn.z))
        audit["SNe"][sn.name] = {
            "data_path": str(sn.data_path),
            "cov_path": str(sn.cov_path) if sn.cov_path is not None else "diagonal_from_catalog",
            "N": int(len(sn.z)),
            "z_min": float(np.min(sn.z)),
            "z_max": float(np.max(sn.z)),
            "mu_shape": list(sn.mu.shape),
            "cov_shape": list(sn.cov.shape),
            "cov_shape_ok": bool(ok_shape),
            "covariance": cov_info,
            "provenance": sn.provenance,
        }
    return audit


def solve_model(om: float, beta: float, n_iter: int = 70, tol: float = 1e-9):
    """Autoconsistent E(z), tau(z)=H0*t(z), and tau0."""
    ode = 1.0 - om - OR_RAD
    e2 = om * (1.0 + ZG) ** 3 + OR_RAD * (1.0 + ZG) ** 4 + ode
    tau = None
    for _ in range(n_iter):
        e = np.sqrt(e2)
        inv_e = 1.0 / e
        integral = np.concatenate((
            (np.cumsum((inv_e[::-1][:-1] + inv_e[::-1][1:]) * 0.5 * DX))[::-1],
            [0.0],
        ))
        tail = (2.0 / 3.0) / np.sqrt(
            om * (1.0 + ZG[-1]) ** 3 + OR_RAD * (1.0 + ZG[-1]) ** 4
        )
        tau_new = integral + tail
        f_de = (tau_new / tau_new[0]) ** (-4.0 * beta)
        e2_new = om * (1.0 + ZG) ** 3 + OR_RAD * (1.0 + ZG) ** 4 + ode * f_de
        if np.any(~np.isfinite(e2_new)) or np.any(e2_new <= 0):
            return None
        delta = np.max(np.abs(np.log(e2_new / e2)))
        e2 = 0.5 * (e2 + e2_new)
        tau = tau_new
        if delta < tol:
            break
    return np.sqrt(e2), tau[0]


def comoving_distance_grid(e: np.ndarray) -> np.ndarray:
    inv_e = 1.0 / e
    integrand = np.exp(XG) * inv_e
    return np.concatenate(([0.0], np.cumsum((integrand[:-1] + integrand[1:]) * 0.5 * DX)))


def bao_model_vector(e: np.ndarray) -> np.ndarray:
    dc = comoving_distance_grid(e)
    u = np.empty(len(BAO_DATA))
    for k, (z, typ, _) in enumerate(BAO_DATA):
        x = np.log1p(z)
        ee = np.interp(x, XG, e)
        dcz = np.interp(x, XG, dc)
        if typ == 2:
            u[k] = 1.0 / ee
        elif typ == 1:
            u[k] = dcz
        else:
            u[k] = (z * dcz * dcz / ee) ** (1.0 / 3.0)
    return u


def profile_linear_scale(model: np.ndarray, data: np.ndarray, cinv: np.ndarray):
    a = model @ cinv @ model
    b = model @ cinv @ data
    scale = b / a
    resid = scale * model - data
    return float(resid @ cinv @ resid), float(scale)


def chi2_bao(e: np.ndarray):
    data = np.array([d[2] for d in BAO_DATA])
    return profile_linear_scale(bao_model_vector(e), data, np.linalg.inv(BAO_COV))


def sn_mu_model(sn: SNDataset, e: np.ndarray) -> np.ndarray:
    dc = comoving_distance_grid(e)
    x = np.log1p(sn.z)
    dcz = np.interp(x, XG, dc)
    dl_h0_units = (1.0 + sn.z) * dcz
    return 5.0 * np.log10(np.maximum(dl_h0_units, 1e-300))


def chi2_sn(sn: SNDataset, e: np.ndarray):
    """Profile one additive intercept: mu_obs = mu_model + intercept."""
    mu0 = sn_mu_model(sn, e)
    cinv = sn.cinv
    one = np.ones_like(mu0)
    resid0 = mu0 - sn.mu
    intercept = -float(one @ cinv @ resid0) / float(one @ cinv @ one)
    resid = mu0 + intercept - sn.mu
    return float(resid @ cinv @ resid), float(intercept)


def chi2_total(om: float, beta: float, sn_sets: list[SNDataset], om_prior=None):
    sol = solve_model(om, beta)
    if sol is None:
        return np.inf, {}
    e, tau0 = sol
    chi2, s_bao = chi2_bao(e)
    parts = {"BAO": chi2, "s_bao": s_bao, "tau0": tau0}
    for sn in sn_sets:
        c, intercept = chi2_sn(sn, e)
        chi2 += c
        parts[sn.name] = c
        parts[f"{sn.name}_intercept"] = intercept
    if om_prior is not None:
        prior = ((om - om_prior[0]) / om_prior[1]) ** 2
        chi2 += prior
        parts["Om_prior"] = prior
    return float(chi2), parts


def scan(sn_sets: list[SNDataset], om_prior=None):
    oms = np.linspace(0.22, 0.42, 81)
    betas = np.linspace(-0.30, 0.45, 151)
    grid = np.full((len(betas), len(oms)), np.inf)
    metadata = {}
    for i, beta in enumerate(betas):
        for j, om in enumerate(oms):
            grid[i, j], _ = chi2_total(om, beta, sn_sets, om_prior=om_prior)
    prof = grid.min(axis=1)
    i0 = int(np.argmin(prof))
    j0 = int(np.argmin(grid[i0]))
    best = {"beta": float(betas[i0]), "om": float(oms[j0]), "chi2": float(grid[i0, j0])}
    _, parts = chi2_total(best["om"], best["beta"], sn_sets, om_prior=om_prior)
    metadata["parts_best"] = parts

    lcdm_i = int(np.argmin(np.abs(betas)))
    lcdm_j = int(np.argmin(grid[lcdm_i]))
    metadata["lcdm"] = {
        "beta": float(betas[lcdm_i]),
        "om": float(oms[lcdm_j]),
        "chi2": float(grid[lcdm_i, lcdm_j]),
    }
    _, metadata["parts_lcdm"] = chi2_total(
        metadata["lcdm"]["om"], metadata["lcdm"]["beta"], sn_sets, om_prior=om_prior
    )

    delta = prof - best["chi2"]
    in68 = betas[delta <= 1.0]
    in95 = betas[delta <= 3.84]
    intervals = {
        "beta_68": [float(in68[0]), float(in68[-1])] if len(in68) else None,
        "beta_95": [float(in95[0]), float(in95[-1])] if len(in95) else None,
    }
    return betas, prof, best, intervals, metadata


def classify(best, intervals, meta):
    dchi2_lcdm_minus_beta = meta["lcdm"]["chi2"] - best["chi2"]
    beta95 = intervals["beta_95"]
    beta68 = intervals["beta_68"]
    success = (
        beta68 is not None
        and beta68[0] > 0.0
        and best["chi2"] <= meta["lcdm"]["chi2"] + 2.0
    )
    failure = (
        beta95 is not None
        and beta95[1] < 0.0
        or dchi2_lcdm_minus_beta <= -4.0
    )
    if success:
        status = "SUCCESS"
    elif failure:
        status = "FAILURE"
    else:
        status = "INCONCLUSIVE"
    return status, dchi2_lcdm_minus_beta


def main():
    parser = argparse.ArgumentParser(description="Exp 20 BAO+Pantheon+DES-Y5 skeleton")
    parser.add_argument("--pantheon", type=Path, help="Pantheon+ catalog with z,mu[,sigma_mu]")
    parser.add_argument("--pantheon-cov", type=Path, help="Pantheon+ covariance matrix")
    parser.add_argument("--pantheon-provenance", type=Path, help="Pantheon+ provenance JSON")
    parser.add_argument("--desy5", type=Path, help="DES-Y5 catalog with z,mu[,sigma_mu]")
    parser.add_argument("--desy5-cov", type=Path, help="DES-Y5 covariance matrix")
    parser.add_argument("--desy5-provenance", type=Path, help="DES-Y5 provenance JSON")
    parser.add_argument("--om-prior", action="store_true", help="Use Om=0.3111+/-0.0056 prior")
    parser.add_argument("--dry-run", action="store_true", help="Load data and print pre-reg only")
    parser.add_argument("--out", type=Path, default=Path("outputs/exp20/exp20_skeleton_results.json"))
    args = parser.parse_args()

    sn_sets = []
    for name, data, cov, prov in [
        ("PantheonPlus", args.pantheon, args.pantheon_cov, args.pantheon_provenance),
        ("DESY5", args.desy5, args.desy5_cov, args.desy5_provenance),
    ]:
        ds = load_sn_catalog(name, data, cov, prov)
        if ds is not None:
            sn_sets.append(ds)

    print("=" * 72)
    print("EXP 20: BAO + Pantheon+ + DES-Y5 combined falsifier")
    print("=" * 72)
    print(f"BAO points: {len(BAO_DATA)}")
    for sn in sn_sets:
        print(f"{sn.name}: N={len(sn.z)}, cov={sn.cov.shape}")
    if not sn_sets:
        print("SN catalogs not provided. Skeleton loaded; fit not run.")
        return
    if args.dry_run:
        print("Dry run requested. Fit not run.")
        print(json.dumps(audit_inputs(sn_sets), indent=2, ensure_ascii=False))
        return

    om_prior = (0.3111, 0.0056) if args.om_prior else None
    betas, prof, best, intervals, meta = scan(sn_sets, om_prior=om_prior)
    status, dchi2 = classify(best, intervals, meta)
    result = {
        "status": status,
        "best": best,
        "intervals": intervals,
        "delta_chi2_lcdm_minus_beta": dchi2,
        "metadata": meta,
        "datasets": ["DESI_DR2_BAO"] + [sn.name for sn in sn_sets],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
