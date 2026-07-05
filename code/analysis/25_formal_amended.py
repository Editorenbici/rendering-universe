#!/usr/bin/env python3
"""
EXP 25 — RUN FORMAL (Enmienda 1 aplicada)
==========================================
Prereg: notes/foundations/exp25_prereg_biased_insertion_2026-07-05.md
(+ Enmienda 1 commiteada en 8da69e6 ANTES de este run).

Enmienda 1 implementada:
  - P_pos(x) ∝ ℛ(x)²  (el presupuesto disforme; BHS lo da gratis en
    sprinklings reales, el toy debe otorgarlo).
  - h LOCAL: cadena más larga restringida a ventana espacial |Δx|<0.25
    (aprox. recursiva local; documentado como toy).
Base: esqueleto de Codex (25_biased_insertion_background.py), regla de
relaciones intacta: P_chain = p0·ℛ(x)^(−b).

Repartos de referencia pre-registrados:
  (−1,+3) disforme | (+0.5,+1.5) isótropo | patrón conforme = alerta.
Grilla congelada: b∈{0,0.5,…,4}, α∈{0.05,0.1,0.2}, N∈{256,512,1024},
32 reales, seeds = 250000 + 1000·i_b + 100·i_α + 10·i_N + r.
Controles: b=0 (en grilla) + shuffle de etiquetas de masa (1 config).
"""

import json
import numpy as np

P0, MASS_W, WINDOW = 0.08, 0.18, 0.25
BGRID = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
AGRID = [0.05, 0.10, 0.20]
NGRID = [256, 512, 1024]
NREAL = 32


def mass_profile(x):
    return np.exp(-0.5 * (x / MASS_W) ** 2)


def transitive_closure(c):
    c = c.copy()
    n = c.shape[0]
    for k in range(n):
        c |= c[:, [k]] & c[[k], :]
    np.fill_diagonal(c, False)
    return c


def generate(n, b, alpha, seed, shuffle_mass=False):
    rng = np.random.default_rng(seed)
    # ENMIENDA 1: posiciones con densidad ∝ ℛ(x)²
    xs = []
    while len(xs) < n:
        cand = rng.uniform(-1, 1, n)
        acc = ((1 + alpha * mass_profile(cand)) / (1 + alpha)) ** 2
        keep = rng.random(n) < acc
        xs.extend(cand[keep].tolist())
    x = np.array(xs[:n])
    order = np.argsort(x * 0 + rng.normal(size=n))   # orden de nacimiento aleatorio
    x = x[order]
    m = mass_profile(x)
    r_rel = 1.0 + alpha * m
    causal = np.zeros((n, n), dtype=bool)
    for j in range(1, n):
        p_chain = np.clip(P0 * r_rel[j] ** (-b), 0.0, 1.0)
        causal[:j, j] = rng.random(j) < p_chain
    causal = transitive_closure(causal)
    if shuffle_mass:
        r_rel = rng.permutation(r_rel)   # control: borra la correlacion
    return x, r_rel, causal


def h_local(causal, x):
    n = causal.shape[0]
    h = np.ones(n)
    for j in range(n):
        preds = np.flatnonzero(causal[:, j] & (np.abs(x - x[j]) < WINDOW))
        if len(preds):
            h[j] = 1 + h[preds].max()
    return h


def w_local(causal, h, x):
    n = causal.shape[0]
    w = np.zeros(n)
    hr = np.rint(h).astype(int)
    for j in range(n):
        inc = ~(causal[:, j] | causal[j, :])
        near = (np.abs(hr - hr[j]) <= 1) & (np.abs(x - x[j]) < WINDOW)
        w[j] = np.count_nonzero(inc & near)
    return w


def fit_power(r, y):
    ok = (r > 0) & (y > 0)
    if ok.sum() < 3 or np.ptp(np.log(r[ok])) == 0:
        return np.nan
    a = np.column_stack([np.ones(ok.sum()), np.log(r[ok])])
    co, *_ = np.linalg.lstsq(a, np.log(y[ok]), rcond=None)
    return float(co[1])


def run_cell(n, b, alpha, ib, ia, i_n, shuffle=False):
    ph, pw, pq = [], [], []
    for r in range(NREAL):
        seed = 250000 + 1000 * ib + 100 * ia + 10 * i_n + r
        x, rr, c = generate(n, b, alpha, seed, shuffle_mass=shuffle)
        h = h_local(c, x)
        w = w_local(c, h, x)
        ph.append(fit_power(rr, h))
        pw.append(fit_power(rr, w))
        pq.append(fit_power(rr, h * w))
    def ms(v):
        v = np.array(v)
        v = v[np.isfinite(v)]
        return (float(v.mean()), float(v.std(ddof=1) / np.sqrt(len(v)))) if len(v) > 2 else (np.nan, np.nan)
    return {"p_h": ms(ph), "p_w": ms(pw), "p_hw": ms(pq)}


if __name__ == "__main__":
    out = {"prereg": "exp25_prereg (+Enmienda 1, commit 8da69e6)",
           "grid": {}, "controls": {}}
    print("EXP 25 FORMAL — reparto del presupuesto R^2", flush=True)
    for i_n, n in enumerate(NGRID):
        for ia, alpha in enumerate(AGRID):
            for ib, b in enumerate(BGRID):
                cell = run_cell(n, b, alpha, ib, ia, i_n)
                out["grid"][f"n{n}_a{alpha}_b{b}"] = cell
                (mh, sh), (mw, sw), (mq, sq) = cell["p_h"], cell["p_w"], cell["p_hw"]
                print(f"n={n} a={alpha} b={b}: p_h={mh:+.2f}±{sh:.2f} "
                      f"p_w={mw:+.2f}±{sw:.2f} p_hw={mq:+.2f}±{sq:.2f}", flush=True)
    print("\n--- control shuffle (n=512, a=0.1, b=2) ---", flush=True)
    out["controls"]["shuffle"] = run_cell(512, 2.0, 0.10, 4, 1, 1, shuffle=True)
    c = out["controls"]["shuffle"]
    print(f"shuffle: p_h={c['p_h'][0]:+.2f}±{c['p_h'][1]:.2f} "
          f"p_w={c['p_w'][0]:+.2f}±{c['p_w'][1]:.2f} (esperado ~0)", flush=True)
    with open("outputs/exp25_formal_results.json", "w") as f:
        json.dump(out, f, indent=1)
    print("DONE — resultados en outputs/exp25_formal_results.json", flush=True)
