#!/usr/bin/env python3
"""
EXP 24 (DRAFT): epsilon_link scaling in 2D and 4D sprinklings
================================================================

Purpose
-------
Generate finite Poisson sprinklings in flat slabs and measure:

  v_link      = mean number of links to a probe event
  epsilon     = N_links / N_past

as functions of sprinkling density rho and resolution/depth R.

This script is a draft tool only. It should not be run as a new measurement
without a committed pre-registration.

Definitions
-----------
For a probe event at t=R and x=0:

  N_past  = number of sprinkled elements in its causal past.
  N_links = number of past elements with no intermediate blocker.
  epsilon = N_links / N_past.

In 4D, prior Exp 18b measured v_link ~ pi*sqrt(6)*sqrt(rho)*R^2.
The fraction epsilon is expected to scale differently because N_past grows
like rho*R^4.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np


TAU2MAX_2D = 12.0
TAU2MAX_4D = 6.8


@dataclass
class Row:
    dim: int
    rho: float
    R: float
    seed0: int
    n_real: int
    links_mean: float
    links_sem: float
    past_mean: float
    past_sem: float
    epsilon_mean: float
    epsilon_sem: float


def sem(x):
    x = np.asarray(x, dtype=float)
    if len(x) < 2:
        return float("nan")
    return float(x.std(ddof=1) / np.sqrt(len(x)))


def sprinkle_2d(rng, rho, R):
    """Uniform sprinkling in a rectangle containing the probe past cone."""
    x_half = R + 1.0
    volume = 2.0 * x_half * R
    n = rng.poisson(rho * volume)
    t = rng.uniform(0.0, R, n)
    x = rng.uniform(-x_half, x_half, n)
    return t, x


def count_probe_links_2d(seed, rho, R):
    rng = np.random.default_rng([24, seed, int(1000 * rho), int(100 * R), 2])
    t, x = sprinkle_2d(rng, rho, R)
    dt = R - t
    dx = np.abs(x)
    past = (dt > 0) & (dx < dt)
    past_idx = np.flatnonzero(past)
    tau2 = dt * dt - dx * dx
    cand = past & (rho * tau2 < TAU2MAX_2D)
    p_t, p_x = t[past_idx], x[past_idx]
    links = 0
    for j in np.flatnonzero(cand):
        dtj = p_t - t[j]
        dxj = np.abs(p_x - x[j])
        if not np.any((dtj > 0) & (dxj < dtj)):
            links += 1
    return links, int(len(past_idx))


def sprinkle_4d(rng, rho, R):
    """Uniform sprinkling in a time slab times a spatial ball."""
    r_box = R + 2.0
    volume = (4.0 * np.pi / 3.0) * r_box**3 * R
    n = rng.poisson(rho * volume)
    t = rng.uniform(0.0, R, n)
    rr = r_box * rng.uniform(0.0, 1.0, n) ** (1.0 / 3.0)
    costh = rng.uniform(-1.0, 1.0, n)
    phi = rng.uniform(0.0, 2.0 * np.pi, n)
    sinth = np.sqrt(1.0 - costh * costh)
    x1 = rr * sinth * np.cos(phi)
    x2 = rr * sinth * np.sin(phi)
    x3 = rr * costh
    return t, x1, x2, x3


def count_probe_links_4d(seed, rho, R):
    rng = np.random.default_rng([24, seed, int(1000 * rho), int(100 * R), 4])
    t, x1, x2, x3 = sprinkle_4d(rng, rho, R)
    dt = R - t
    d2 = x1 * x1 + x2 * x2 + x3 * x3
    past = (dt > 0) & (d2 < dt * dt)
    past_idx = np.flatnonzero(past)
    tau2 = dt * dt - d2
    cand = past & (tau2 * np.sqrt(rho) < TAU2MAX_4D)
    p_t = t[past_idx]
    p1, p2, p3 = x1[past_idx], x2[past_idx], x3[past_idx]
    links = 0
    for j in np.flatnonzero(cand):
        dtj = p_t - t[j]
        d2j = (p1 - x1[j]) ** 2 + (p2 - x2[j]) ** 2 + (p3 - x3[j]) ** 2
        if not np.any((dtj > 0) & (d2j < dtj * dtj)):
            links += 1
    return links, int(len(past_idx))


def measure_grid(dim, rhos, Rs, n_real):
    rows = []
    counter = 0
    for rho in rhos:
        for R in Rs:
            links = []
            pasts = []
            for s in range(n_real):
                seed = counter * 10_000 + s
                if dim == 2:
                    lnk, pst = count_probe_links_2d(seed, rho, R)
                elif dim == 4:
                    lnk, pst = count_probe_links_4d(seed, rho, R)
                else:
                    raise ValueError("dim must be 2 or 4")
                links.append(lnk)
                pasts.append(pst)
            links = np.asarray(links, dtype=float)
            pasts = np.asarray(pasts, dtype=float)
            eps = np.divide(links, pasts, out=np.full_like(links, np.nan), where=pasts > 0)
            rows.append(Row(
                dim=dim,
                rho=float(rho),
                R=float(R),
                seed0=int(counter * 10_000),
                n_real=int(n_real),
                links_mean=float(np.nanmean(links)),
                links_sem=sem(links),
                past_mean=float(np.nanmean(pasts)),
                past_sem=sem(pasts),
                epsilon_mean=float(np.nanmean(eps)),
                epsilon_sem=sem(eps),
            ))
            counter += 1
    return rows


def fit_power_law(rows, quantity):
    """Fit quantity ~ C * rho^a * R^b in log-space."""
    xs = []
    ys = []
    for row in rows:
        y = getattr(row, quantity)
        if np.isfinite(y) and y > 0:
            xs.append([1.0, np.log(row.rho), np.log(row.R)])
            ys.append(np.log(y))
    X = np.asarray(xs)
    y = np.asarray(ys)
    coeff, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ coeff
    rms = float(np.sqrt(np.mean((y - pred) ** 2)))
    return {
        "quantity": quantity,
        "log_C": float(coeff[0]),
        "C": float(np.exp(coeff[0])),
        "rho_power": float(coeff[1]),
        "R_power": float(coeff[2]),
        "log_rms": rms,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dims", nargs="+", type=int, default=[2, 4])
    parser.add_argument("--rhos", nargs="+", type=float, default=[0.5, 1.0, 2.0])
    parser.add_argument("--Rs", nargs="+", type=float, default=[4.0, 6.0, 8.0, 10.0])
    parser.add_argument("--n-real", type=int, default=8)
    parser.add_argument("--out", type=Path, default=Path("outputs/exp24_epsilon_link_scaling.json"))
    args = parser.parse_args()

    all_rows = []
    fits = []
    for dim in args.dims:
        rows = measure_grid(dim, args.rhos, args.Rs, args.n_real)
        all_rows.extend(rows)
        fits.append({"dim": dim, **fit_power_law(rows, "links_mean")})
        fits.append({"dim": dim, **fit_power_law(rows, "epsilon_mean")})

    payload = {
        "status": "DRAFT_NOT_PREREGISTERED",
        "warning": "Do not use as measurement without committed pre-registration.",
        "rows": [asdict(r) for r in all_rows],
        "fits": fits,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
