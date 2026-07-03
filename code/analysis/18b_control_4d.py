#!/usr/bin/env python3
"""
EXP 18 — CONTROL 4D (pre-registrado): valencia en Minkowski 3+1
================================================================
Prediccion analitica (servilleta integrada cerca del cono, banda de
links con P = exp(-rho*pi*tau^4/24)):

    v(T) = pi*sqrt(6)*sqrt(rho)*T^2  ~  7.695*T^2   (rho=1)

CRITERIOS DE CONTROL (deben pasar para habilitar la fase FRW):
  C1: exponente del ajuste v ~ T^p:  p = 2.00 +- 0.10 (2sigma)
  C2: amplitud A del ajuste v = A*T^2 dentro de +-15% de pi*sqrt(6)
      (correcciones de borde/cutoff esperadas a ese nivel)
Si C1 o C2 fallan: el codigo o la servilleta estan mal; NO se corre FRW.

PREDICCION FRW PRE-REGISTRADA (para la fase siguiente, era de materia,
a ~ eta^2, densidad fisica uniforme -> conformal rho*a^4):
    v ~ eta^6 ~ t^2  (MISMO exponente 2 en tiempo propio que Minkowski)
"""

import numpy as np

RHO = 1.0
TAU2MAX = 6.8      # P(link) < e^-6 mas alla
AMP_TEO = np.pi * np.sqrt(6.0) * np.sqrt(RHO)
N_REAL = 20
T_GRID = [6.0, 9.0, 12.0, 16.0]


def valencia_probe(seed, T):
    """Valencia (links al pasado) de un evento sonda en (T, origen)."""
    rng = np.random.default_rng([seed, int(T * 10), 4])
    R_box = T + 2.0
    vol = (4.0 / 3.0) * np.pi * R_box ** 3 * T
    n = rng.poisson(RHO * vol)
    ts = rng.uniform(0.0, T, n)
    # posiciones uniformes en la bola de radio R_box
    rr = R_box * rng.uniform(0, 1, n) ** (1.0 / 3.0)
    cos_t = rng.uniform(-1, 1, n)
    phi = rng.uniform(0, 2 * np.pi, n)
    sin_t = np.sqrt(1 - cos_t ** 2)
    x1 = rr * sin_t * np.cos(phi)
    x2 = rr * sin_t * np.sin(phi)
    x3 = rr * cos_t

    dt = T - ts
    d2 = x1 ** 2 + x2 ** 2 + x3 ** 2
    past = d2 < dt ** 2
    tau2 = dt ** 2 - d2
    cidx = np.flatnonzero(past & (tau2 < TAU2MAX))
    pidx = np.flatnonzero(past)
    tp, p1, p2, p3 = ts[pidx], x1[pidx], x2[pidx], x3[pidx]
    links = 0
    for j in cidx:
        dtj = tp - ts[j]
        d2j = (p1 - x1[j]) ** 2 + (p2 - x2[j]) ** 2 + (p3 - x3[j]) ** 2
        if not np.any((dtj > 0) & (d2j < dtj ** 2)):
            links += 1
    return links


print("=" * 70)
print("EXP 18 - CONTROL 4D: v(T) en Minkowski 3+1")
print("=" * 70)
print(f"Prediccion: v = {AMP_TEO:.3f} * T^2\n")
print(f"{'T':>5} {'<v>':>10} {'SEM':>7} {'teoria':>9} {'ratio':>7}")

ms, ss = [], []
for T in T_GRID:
    vs = [valencia_probe(s, T) for s in range(N_REAL)]
    m, sem = np.mean(vs), np.std(vs, ddof=1) / np.sqrt(N_REAL)
    ms.append(m)
    ss.append(sem)
    teo = AMP_TEO * T ** 2
    print(f"{T:>5.0f} {m:>10.1f} {sem:>7.1f} {teo:>9.1f} {m/teo:>7.3f}",
          flush=True)

# ajuste log-log
lx = np.log(np.array(T_GRID))
ly = np.log(np.array(ms))
w = (np.array(ms) / np.array(ss)) ** 2
xb = np.sum(w * lx) / np.sum(w)
yb = np.sum(w * ly) / np.sum(w)
den = np.sum(w * (lx - xb) ** 2)
p = np.sum(w * (lx - xb) * (ly - yb)) / den
sp = 1.0 / np.sqrt(den)
amp = np.exp(yb - p * xb)
print(f"\nExponente p = {p:.3f} +- {sp:.3f}   (C1: 2.00 +- 0.10 a 2sigma)")
print(f"Amplitud efectiva <v>/T^2 media = "
      f"{np.mean(np.array(ms)/np.array(T_GRID)**2):.3f} "
      f"(C2: {AMP_TEO:.3f} +- 15%)")
c1 = abs(p - 2.0) < max(0.10, 2 * sp)
ratio = np.mean(np.array(ms) / np.array(T_GRID) ** 2) / AMP_TEO
c2 = abs(ratio - 1.0) < 0.15
print(f"C1: {'PASA' if c1 else 'FALLA'} | C2: {'PASA' if c2 else 'FALLA'}")
print("CONTROL 4D " + ("VALIDADO - fase FRW habilitada para pre-registro"
                       if c1 and c2 else "FALLIDO - revisar antes de FRW"))
print("DONE")
