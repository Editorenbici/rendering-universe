#!/usr/bin/env python3
"""
EXP 22 BACKGROUND SKELETON: interval geometry diagnostics
=========================================================

Status
------
Background scaffold only. Do not use as a measurement without an approved
pre-registration and an explicit run command in the project log.

Purpose
-------
Provide loaders/generators, metrics, and criteria for the Exp 22 program:
compare interval statistics in manifold-like sprinklings against
non-geometric order controls.

Conventions
-----------
R is dimensionless: [R] = 1.

epsilon_link = <N_links> / <N_past>
v_link       = <N_links>

This script separates raw causal availability from irreducible links.

Default behavior
----------------
The default command is a light dry-run. It builds tiny toy cases and prints
JSON shapes/keys only. It does not perform the full Exp 22 measurement.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


@dataclass
class PosetData:
    name: str
    dim: int | None
    coords: np.ndarray | None
    causal: np.ndarray


@dataclass
class IntervalMetrics:
    source: int
    target: int
    n_interval: int
    longest_chain: int
    n_links_internal: int
    epsilon_link_internal: float
    nm_counts: dict[int, int]


def load_npz_poset(path: Path) -> PosetData:
    """Load a poset from npz with keys causal and optional coords, dim, name."""
    data = np.load(path, allow_pickle=False)
    causal = np.asarray(data["causal"], dtype=bool)
    coords = np.asarray(data["coords"], dtype=float) if "coords" in data else None
    dim = int(data["dim"]) if "dim" in data else None
    name = str(data["name"]) if "name" in data else path.stem
    validate_causal_matrix(causal)
    return PosetData(name=name, dim=dim, coords=coords, causal=causal)


def validate_causal_matrix(causal: np.ndarray) -> None:
    if causal.ndim != 2 or causal.shape[0] != causal.shape[1]:
        raise ValueError("causal must be a square boolean matrix")
    if np.any(np.diag(causal)):
        raise ValueError("causal relation must be irreflexive on the diagonal")


def generate_minkowski_sprinkling(
    *,
    dim: int,
    n: int,
    seed: int,
    time_height: float = 1.0,
    space_half_width: float = 0.5,
) -> PosetData:
    """Generate a tiny flat-box sprinkling for dry-run/background testing."""
    if dim not in (2, 4):
        raise ValueError("dim must be 2 or 4")
    rng = np.random.default_rng(seed)
    t = rng.uniform(0.0, time_height, n)
    spatial_dim = dim - 1
    x = rng.uniform(-space_half_width, space_half_width, (n, spatial_dim))
    coords = np.column_stack([t, x])
    order = np.argsort(coords[:, 0])
    coords = coords[order]
    causal = causal_from_minkowski_coords(coords)
    return PosetData(name=f"minkowski_{dim}d_n{n}", dim=dim, coords=coords, causal=causal)


def generate_random_order(*, n: int, p: float, seed: int) -> PosetData:
    """Generate a non-geometric transitive random-order control."""
    rng = np.random.default_rng(seed)
    upper = rng.random((n, n)) < p
    upper = np.triu(upper, k=1)
    causal = transitive_closure(upper)
    return PosetData(name=f"random_order_n{n}_p{p:g}", dim=None, coords=None, causal=causal)


def causal_from_minkowski_coords(coords: np.ndarray) -> np.ndarray:
    t = coords[:, 0]
    x = coords[:, 1:]
    dt = t[None, :] - t[:, None]
    dx = x[None, :, :] - x[:, None, :]
    d2 = np.sum(dx * dx, axis=2)
    causal = (dt > 0.0) & (d2 < dt * dt)
    np.fill_diagonal(causal, False)
    return causal


def transitive_closure(causal: np.ndarray) -> np.ndarray:
    closure = np.asarray(causal, dtype=bool).copy()
    n = closure.shape[0]
    for k in range(n):
        closure |= closure[:, [k]] & closure[[k], :]
    np.fill_diagonal(closure, False)
    return closure


def transitive_reduction_links(causal: np.ndarray) -> np.ndarray:
    """Return links x<*y: causal pairs with no intermediate blocker."""
    validate_causal_matrix(causal)
    n = causal.shape[0]
    links = causal.copy()
    for i in range(n):
        js = np.flatnonzero(causal[i])
        for j in js:
            if np.any(causal[i] & causal[:, j]):
                links[i, j] = False
    return links


def interval_indices(causal: np.ndarray, source: int, target: int) -> np.ndarray:
    if not causal[source, target]:
        return np.array([], dtype=int)
    inside = causal[source] & causal[:, target]
    return np.flatnonzero(inside)


def longest_chain_length(causal_sub: np.ndarray) -> int:
    """Longest chain length in a DAG already ordered by causal-compatible index."""
    n = causal_sub.shape[0]
    if n == 0:
        return 0
    dp = np.ones(n, dtype=int)
    for j in range(n):
        preds = np.flatnonzero(causal_sub[:, j])
        if len(preds):
            dp[j] = 1 + int(np.max(dp[preds]))
    return int(np.max(dp))


def nm_counts_for_interval(causal_sub: np.ndarray, max_m: int) -> dict[int, int]:
    """Count subintervals with exactly m interior elements, for small m."""
    counts = {m: 0 for m in range(max_m + 1)}
    n = causal_sub.shape[0]
    for i in range(n):
        for j in np.flatnonzero(causal_sub[i]):
            m = int(np.count_nonzero(causal_sub[i] & causal_sub[:, j]))
            if m <= max_m:
                counts[m] += 1
    return counts


def measure_interval(
    poset: PosetData,
    source: int,
    target: int,
    *,
    max_m: int,
) -> IntervalMetrics:
    causal = poset.causal
    idx = interval_indices(causal, source, target)
    if len(idx) == 0:
        return IntervalMetrics(source, target, 0, 0, 0, 0.0, {m: 0 for m in range(max_m + 1)})
    sub = causal[np.ix_(idx, idx)]
    links = transitive_reduction_links(sub)
    n_links = int(np.count_nonzero(links))
    n_pairs = int(np.count_nonzero(sub))
    epsilon = float(n_links / n_pairs) if n_pairs else 0.0
    return IntervalMetrics(
        source=source,
        target=target,
        n_interval=int(len(idx)),
        longest_chain=longest_chain_length(sub),
        n_links_internal=n_links,
        epsilon_link_internal=epsilon,
        nm_counts=nm_counts_for_interval(sub, max_m=max_m),
    )


def select_intervals(causal: np.ndarray, n_intervals: int, seed: int) -> list[tuple[int, int]]:
    pairs = np.argwhere(causal)
    if len(pairs) == 0:
        return []
    rng = np.random.default_rng(seed)
    take = min(n_intervals, len(pairs))
    chosen = rng.choice(len(pairs), size=take, replace=False)
    return [(int(i), int(j)) for i, j in pairs[chosen]]


def summarize_poset(poset: PosetData, *, n_intervals: int, max_m: int, seed: int) -> dict:
    links = transitive_reduction_links(poset.causal)
    intervals = select_intervals(poset.causal, n_intervals=n_intervals, seed=seed)
    metrics = [
        measure_interval(poset, i, j, max_m=max_m)
        for i, j in intervals
    ]
    return {
        "name": poset.name,
        "dim": poset.dim,
        "n": int(poset.causal.shape[0]),
        "n_causal_pairs": int(np.count_nonzero(poset.causal)),
        "n_links": int(np.count_nonzero(links)),
        "epsilon_link_global": (
            float(np.count_nonzero(links) / np.count_nonzero(poset.causal))
            if np.count_nonzero(poset.causal)
            else 0.0
        ),
        "n_intervals_measured": len(metrics),
        "interval_metrics": [asdict(m) for m in metrics],
        "criteria": criteria_stub(),
    }


def criteria_stub() -> dict:
    return {
        "success": [
            "Embedding dimension recovered within the pre-registered tolerance.",
            "N_m abundances separate manifold-like sprinklings from non-geometric controls.",
            "v_link and epsilon_link remain in their valid operational ranges.",
        ],
        "failure": [
            "Manifold-like and non-geometric controls are not separable on the pre-registered metrics.",
            "epsilon_link <= 0 or epsilon_link >= 1 for the fractional definition.",
            "Longest-chain or interval-abundance estimators are unstable under the planned grid.",
        ],
    }


def build_dry_run_cases(seed: int) -> list[PosetData]:
    return [
        generate_minkowski_sprinkling(dim=2, n=32, seed=seed),
        generate_minkowski_sprinkling(dim=4, n=32, seed=seed + 1),
        generate_random_order(n=32, p=0.08, seed=seed + 2),
    ]


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", default=True)
    parser.add_argument("--input-npz", type=Path, default=None)
    parser.add_argument("--n-intervals", type=int, default=8)
    parser.add_argument("--max-m", type=int, default=4)
    parser.add_argument("--seed", type=int, default=2200)
    parser.add_argument("--out", type=Path, default=None)
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    if args.input_npz:
        cases = [load_npz_poset(args.input_npz)]
    else:
        cases = build_dry_run_cases(seed=args.seed)

    payload = {
        "status": "BACKGROUND_SKELETON_NOT_MEASUREMENT",
        "pre_registration": "notes/exp22_prereg_outline_2026-07-03.md",
        "dry_run": bool(args.dry_run),
        "cases": [
            summarize_poset(c, n_intervals=args.n_intervals, max_m=args.max_m, seed=args.seed)
            for c in cases
        ],
    }

    text = json.dumps(payload, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
