#!/usr/bin/env python3
"""
EXP 25 BACKGROUND SKELETON: biased chain/antichain insertion
============================================================

Status
------
GATED background scaffold. Do not run as a formal measurement until
notes/exp25_prereg_biased_insertion_2026-07-05.md is audited.

Purpose
-------
Toy model for the anisotropy note:

  h ~ R^-1      local chain height decreases near mass
  w ~ R^+3      local antichain width increases near mass
  h*w ~ R^+2    disformal volume consistency

Default behavior is a tiny dry-run only.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass
class RunConfig:
    n: int
    b: float
    alpha: float
    seed: int
    p0: float = 0.08
    mass_width: float = 0.18


def mass_profile(x: np.ndarray, width: float) -> np.ndarray:
    return np.exp(-0.5 * (x / width) ** 2)


def transitive_closure(causal: np.ndarray) -> np.ndarray:
    closure = np.asarray(causal, dtype=bool).copy()
    n = closure.shape[0]
    for k in range(n):
        closure |= closure[:, [k]] & closure[[k], :]
    np.fill_diagonal(closure, False)
    return closure


def generate_biased_order(cfg: RunConfig) -> dict:
    rng = np.random.default_rng(cfg.seed)
    x = rng.uniform(-1.0, 1.0, cfg.n)
    order = np.argsort(x + 0.15 * rng.normal(size=cfg.n))
    x = x[order]
    m = mass_profile(x, cfg.mass_width)
    r_rel = 1.0 + cfg.alpha * m

    causal = np.zeros((cfg.n, cfg.n), dtype=bool)
    for j in range(1, cfg.n):
        # Near mass, chain probability is suppressed. The closure step then
        # tests whether the microscopic bias survives as an order property.
        p_chain = np.clip(cfg.p0 * r_rel[j] ** (-cfg.b), 0.0, 1.0)
        causal[:j, j] = rng.random(j) < p_chain
    causal = transitive_closure(causal)
    return {"x": x, "mass": m, "R": r_rel, "causal": causal}


def longest_past_chain(causal: np.ndarray) -> np.ndarray:
    n = causal.shape[0]
    h = np.ones(n, dtype=float)
    for j in range(n):
        preds = np.flatnonzero(causal[:, j])
        if len(preds):
            h[j] = 1.0 + np.max(h[preds])
    return h


def local_antichain_width(causal: np.ndarray, heights: np.ndarray, radius: int = 1) -> np.ndarray:
    n = causal.shape[0]
    width = np.zeros(n, dtype=float)
    rounded = np.rint(heights).astype(int)
    for j in range(n):
        incomparable = ~(causal[:, j] | causal[j, :])
        near_layer = np.abs(rounded - rounded[j]) <= radius
        width[j] = np.count_nonzero(incomparable & near_layer)
    return width


def fit_power(r_rel: np.ndarray, y: np.ndarray) -> dict:
    ok = (r_rel > 0) & (y > 0)
    if np.count_nonzero(ok) < 3 or np.ptp(np.log(r_rel[ok])) == 0:
        return {"power": None, "log_C": None, "log_rms": None}
    a = np.column_stack([np.ones(np.count_nonzero(ok)), np.log(r_rel[ok])])
    coeff, *_ = np.linalg.lstsq(a, np.log(y[ok]), rcond=None)
    resid = np.log(y[ok]) - a @ coeff
    return {
        "log_C": float(coeff[0]),
        "power": float(coeff[1]),
        "log_rms": float(np.sqrt(np.mean(resid * resid))),
    }


def measure(cfg: RunConfig) -> dict:
    data = generate_biased_order(cfg)
    causal = data["causal"]
    h = longest_past_chain(causal)
    w = local_antichain_width(causal, h)
    q = h * w
    return {
        "config": cfg.__dict__,
        "n_relations": int(np.count_nonzero(causal)),
        "relation_density": float(np.count_nonzero(causal) / (cfg.n * (cfg.n - 1) / 2)),
        "fits": {
            "h_vs_R": fit_power(data["R"], h),
            "w_vs_R": fit_power(data["R"], w),
            "hw_vs_R": fit_power(data["R"], q),
        },
        "criteria_targets": {
            "h_power": -1.0,
            "w_power": 3.0,
            "hw_power": 2.0,
        },
    }


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", default=True)
    parser.add_argument("--n", type=int, default=64)
    parser.add_argument("--b", type=float, default=1.0)
    parser.add_argument("--alpha", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=250000)
    parser.add_argument("--out", type=str, default=None)
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    payload = {
        "status": "BACKGROUND_SKELETON_NOT_MEASUREMENT",
        "pre_registration": "notes/exp25_prereg_biased_insertion_2026-07-05.md",
        "dry_run": bool(args.dry_run),
        "result": measure(RunConfig(n=args.n, b=args.b, alpha=args.alpha, seed=args.seed)),
    }
    text = json.dumps(payload, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
