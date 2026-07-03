#!/usr/bin/env python3
"""
23: CHEQUEO GLASER-SURYA — abundancia de links N_0 en diamante causal
======================================================================
Objetivo (compuerta del Paper A): amarrar nuestra maquinaria de links
al objeto publicado. Glaser & Surya (PRD 88, 124026, 2013) estudian
las abundancias de intervalos <N_m>; para m=0 (links = covering
relations) la forma exacta en sprinkling Poisson es:

    <N_0> = rho^2 * Int_{x<y en D} e^{-rho*V_xy} dV_x dV_y,
    V_xy = (pi/24) * tau_xy^4     (diamante 4D plano; el intervalo de
                                   Alexandrov de x<y esta contenido en D)

TRES VIAS (deben coincidir):
  (a) La integral, por Monte Carlo de pares (el objeto Glaser-Surya).
  (b) Conteo EXACTO de links en diamantes sprinkleados (chequeo de
      bloqueadores — nuestra maquinaria de exps 13/18).
  (c) Nuestra aproximacion de banda cerca del cono, integrada sobre el
      diamante con clipping (la misma logica que dio pi*sqrt6*T^2 en
      slab): densidad de links por elemento fuente integrando la banda
      futura DENTRO del diamante.

CRITERIO: (a) y (b) compatibles a 2 sigma -> pipeline amarrado al
baseline; discrepancia (c) vs (a,b) mide el costo del clipping de
borde en geometria no-slab (informativo, no gate).

Geometria: diamante entre (0,origen) y (T_D,origen), T_D=10, rho=1.
N_esperado = rho*(pi/24)*T_D^4 ~ 1309.
"""

import numpy as np

RHO = 1.0
T_D = 10.0
N_REAL = 6
N_MC = 4_000_000
RNG = np.random.default_rng(23)
TAU2MAX = 6.8   # e^{-rho*pi*tau^4/24} < 3e-9 mas alla (igual que 13/18)


def sample_diamond(n, rng):
    """Puntos uniformes en el diamante 4D via rechazo desde el doble cono."""
    ts, xs = [], []
    need = n
    while need > 0:
        m = int(need * 3.2) + 100
        t = rng.uniform(0, T_D, m)
        r_max = np.minimum(t, T_D - t)
        # muestrear radio uniforme en bola de radio r_max(t): r = r_max*U^(1/3)
        r = r_max * rng.uniform(0, 1, m) ** (1.0 / 3.0)
        # peso: el volumen de la bola varia con t -> aceptar con prob (r_max/max)^3
        acc = rng.uniform(0, 1, m) < (r_max / (T_D / 2)) ** 3
        t, r = t[acc], r[acc]
        cos_t = rng.uniform(-1, 1, len(t))
        phi = rng.uniform(0, 2 * np.pi, len(t))
        sin_t = np.sqrt(1 - cos_t ** 2)
        ts.append(np.column_stack([t, r * sin_t * np.cos(phi),
                                   r * sin_t * np.sin(phi), r * cos_t]))
        need -= len(t)
    pts = np.vstack(ts)[:n]
    return pts


V_D = (np.pi / 24.0) * T_D ** 4   # volumen del diamante 4D

# ---------- (a) integral Glaser-Surya por MC de pares ----------
pa = sample_diamond(N_MC, RNG)
pb = sample_diamond(N_MC, RNG)
dt = pb[:, 0] - pa[:, 0]
d2 = np.sum((pb[:, 1:] - pa[:, 1:]) ** 2, axis=1)
causal = (dt > 0) & (d2 < dt ** 2)
tau4 = np.where(causal, (dt ** 2 - d2) ** 2, 0.0)
integrand = np.where(causal, np.exp(-RHO * (np.pi / 24.0) * tau4), 0.0)
mean_i = integrand.mean()
sem_i = integrand.std() / np.sqrt(N_MC)
N0_gs = RHO ** 2 * V_D ** 2 * mean_i
N0_gs_err = RHO ** 2 * V_D ** 2 * sem_i
print("=" * 70)
print("23: CHEQUEO GLASER-SURYA (diamante 4D, T_D=10, rho=1)")
print("=" * 70)
print(f"N esperado en el diamante: {RHO * V_D:.0f}")
print(f"\n(a) Integral <N_0> (Glaser-Surya, MC {N_MC:.0e} pares): "
      f"{N0_gs:.0f} +- {N0_gs_err:.0f}")

# ---------- (b) conteo exacto en sprinklings ----------
counts = []
for s in range(N_REAL):
    rng = np.random.default_rng([23, s])
    n = rng.poisson(RHO * V_D)
    p = sample_diamond(n, rng)
    t, x = p[:, 0], p[:, 1:]
    order = np.argsort(t)
    t, x = t[order], x[order]
    links = 0
    # candidatos: pares causales con tau2 < TAU2MAX, chequeo exacto
    for i in range(n):
        dt_i = t[i] - t[:i]
        d2_i = np.sum((x[i] - x[:i]) ** 2, axis=1)
        caus = d2_i < dt_i ** 2
        tau2 = np.where(caus, dt_i ** 2 - d2_i, np.inf)
        cand = np.flatnonzero(tau2 < TAU2MAX)
        for j in cand:
            # bloqueador k: t[j] < t[k] < t[i], j<k<i causal
            sel = slice(j + 1, i)
            dtk = t[sel] - t[j]
            d2k = np.sum((x[sel] - x[j]) ** 2, axis=1)
            up = d2k < dtk ** 2
            if not np.any(up):
                links += 1
                continue
            kk = np.flatnonzero(up) + j + 1
            dtk2 = t[i] - t[kk]
            d2k2 = np.sum((x[i] - x[kk]) ** 2, axis=1)
            if not np.any(d2k2 < dtk2 ** 2):
                links += 1
    counts.append(links)
    print(f"(b) realizacion {s}: n={n}, links exactos = {links}", flush=True)
m_b, s_b = np.mean(counts), np.std(counts, ddof=1) / np.sqrt(N_REAL)
print(f"(b) Conteo exacto: <N_0> = {m_b:.0f} +- {s_b:.0f}")

# ---------- veredicto ----------
nsig = abs(N0_gs - m_b) / np.hypot(N0_gs_err, s_b)
print(f"\n(a) vs (b): {nsig:.2f} sigma -> "
      f"{'AMARRADO al baseline Glaser-Surya' if nsig < 2 else 'DISCREPANCIA - investigar'}")

# ---------- (c) banda near-cone integrada con clipping (informativo) ----
# densidad de links futuros por elemento en x: banda sobre el cono
# futuro DENTRO del diamante; misma integral de banda que 18b pero con
# el alcance limitado por la frontera del diamante.
pc = sample_diamond(400_000, RNG)
# distancia del punto al apice futuro a lo largo del cono ~ limite r
# aproximacion slab-like: v_fut(x) ~ (pi*sqrt6/2)*sqrt(rho)*L(x)^2 con
# L(x) = extension del cono futuro dentro del diamante (hasta el apice)
L = T_D - pc[:, 0] - np.sqrt(np.sum(pc[:, 1:] ** 2, axis=1))
v_band = (np.pi * np.sqrt(6.0) / 2.0) * np.sqrt(RHO) * np.maximum(L, 0) ** 2
N0_band = RHO * V_D * v_band.mean()
print(f"\n(c) Banda near-cone con clipping (informativo): ~{N0_band:.0f} "
      f"(ratio vs (a): {N0_band / N0_gs:.2f}) — mide el costo del borde")
print("DONE")
