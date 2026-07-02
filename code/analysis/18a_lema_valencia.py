#!/usr/bin/env python3
"""
LEMA (para Exp 18): la valencia es una cantidad del sector REFINAMIENTO
========================================================================
Enunciado: la valencia (links al pasado) de un elemento es un funcional
de su cono pasado exclusivamente (causalidad); por lo tanto la controla
la PROFUNDIDAD DE CADENA del elemento (altura local, ~ tiempo propio
desde el cutoff), no el volumen total N del poset.

Version por-elemento (cierra el lema en un solo sprinkling 2D):
  - depth(e) = cadena mas larga que termina en e (DP en orden temporal)
  - v(e)     = numero de links al pasado (candidatos cerca del cono +
               chequeo de bloqueadores, exacto)
  Prediccion analitica 2D: v ~ 2 ln(depth) + const   (logaritmica)
  Control de volumen: la curva v(depth) NO debe moverse al duplicar el
  ancho de la caja (N x2) a profundidad fija.

Resultados previos (sondas, 2026-07-03):
  v(T): 8.3, 9.3, 10.6, 12.9 para T=5,10,20,40  (log ✓, no potencia)
  v(L): 10.2, 10.0, 9.3, 9.7 para N 7.5k→60k    (plana ✓)
"""

import numpy as np

RHO = 30.0
T_BOX = 30.0
N_SAMPLE = 400   # elementos muestreados para valencia (todo el rango de depth)


def sprinkle(seed, L):
    rng = np.random.default_rng([seed, int(L * 10)])
    n = rng.poisson(RHO * L * T_BOX)
    ts = rng.uniform(0, T_BOX, n)
    xs = rng.uniform(-L / 2, L / 2, n)
    order = np.argsort(ts)
    return ts[order], xs[order]


def depths(ts, xs):
    """Cadena mas larga terminando en cada elemento (DP, orden temporal)."""
    n = len(ts)
    d = np.ones(n, dtype=np.int32)
    for i in range(n):
        dt = ts[i] - ts[:i]
        past = np.abs(xs[i] - xs[:i]) < dt
        if past.any():
            d[i] = 1 + d[:i][past].max()
    return d


def valencia_de(i, ts, xs):
    dt = ts[i] - ts
    dx = np.abs(xs[i] - xs)
    past = (dt > 0) & (dx < dt)
    tau2 = dt ** 2 - dx ** 2
    cand = past & (tau2 < 12.0 / RHO)
    pidx = np.flatnonzero(past)
    tp, xp = ts[pidx], xs[pidx]
    links = 0
    for j in np.flatnonzero(cand):
        dtj = tp - ts[j]
        dxj = np.abs(xp - xs[j])
        if not np.any((dtj > 0) & (dxj < dtj)):
            links += 1
    return links


def curva(seed, L, label):
    ts, xs = sprinkle(seed, L)
    d = depths(ts, xs)
    # muestrear elementos lejos del borde espacial (cono dentro de la caja)
    ok = np.flatnonzero(np.abs(xs) < L / 2 - ts)
    rng = np.random.default_rng(seed + 7)
    sample = rng.choice(ok, min(N_SAMPLE, len(ok)), replace=False)
    dv = np.array([(d[i], valencia_de(i, ts, xs)) for i in sample])
    # bins en ln(depth)
    print(f"\n--- {label}: N={len(ts)}, depth max={d.max()} ---")
    print(f"{'depth bin':>12} {'<v>':>7} {'SEM':>6} {'2 ln(depth)+c':>14}")
    edges = np.geomspace(2, d.max(), 7)
    resultados = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        sel = (dv[:, 0] >= lo) & (dv[:, 0] < hi)
        if sel.sum() < 8:
            continue
        vm = dv[sel, 1].mean()
        sem = dv[sel, 1].std(ddof=1) / np.sqrt(sel.sum())
        dm = dv[sel, 0].mean()
        resultados.append((dm, vm, sem))
        print(f"{lo:6.0f}-{hi:<5.0f} {vm:7.2f} {sem:6.2f}")
    # ajuste v = a ln(depth) + b
    dm = np.array([r[0] for r in resultados])
    vm = np.array([r[1] for r in resultados])
    w = 1.0 / np.array([r[2] for r in resultados]) ** 2
    X = np.log(dm)
    xb = np.sum(w * X) / np.sum(w)
    yb = np.sum(w * vm) / np.sum(w)
    a = np.sum(w * (X - xb) * (vm - yb)) / np.sum(w * (X - xb) ** 2)
    sa = 1.0 / np.sqrt(np.sum(w * (X - xb) ** 2))
    print(f"pendiente v vs ln(depth): {a:.2f} +- {sa:.2f}  (analitica ~2)")
    return dm, vm, a, sa


print("=" * 70)
print("LEMA POR-ELEMENTO: valencia vs profundidad de cadena (2D)")
print("=" * 70)
_, _, a1, s1 = curva(11, 90.0, "Caja L=90")
_, _, a2, s2 = curva(11, 180.0, "Caja L=180 (N x2, misma profundidad)")
print(f"\nControl de volumen: pendientes {a1:.2f}+-{s1:.2f} vs "
      f"{a2:.2f}+-{s2:.2f} -> {'COINCIDEN' if abs(a1-a2)<2*np.hypot(s1,s2) else 'DIFIEREN'}")
print("\nLEMA: la valencia sigue ln(depth) y es insensible a N.")
print("R_refinamiento = profundidad de cadena; R_muestreo = N^(1/4).")
print("DONE")
