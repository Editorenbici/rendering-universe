#!/usr/bin/env python3
"""
REPLICA PRE-DECLARADA DE E4 (exp 12).
El run original dio 2.13 sigma vs umbral 2.0 (fallo marginal).
DECLARADO ANTES DE CORRER: semillas frescas (1000+), N_REAL=400 (4x),
t0 en {18, 24, 30} (meseta). PASA si todas las diferencias pareadas
< 2 sigma. Si FALLA de nuevo, hay efecto real dependiente de t0.
"""
import numpy as np

N_REAL = 400
SEED_OFFSET = 1000
RHO0, W0, R0, DH0 = 50.0, 4.0, 6.0, 5.0


def delta_psi_realizacion(seed, rho, w, r, dh, t0):
    rng = np.random.default_rng([seed, int(rho * 1000), int(w * 100),
                                 int(r * 100), int(dh * 100), int(t0 * 100), 0, 0])
    x_base, x_cima = r, r + dh
    box_t = t0 + 1.0
    lo = min(-w / 2, x_base - t0) - 2.0
    hi = max(w / 2, x_cima + t0) + 2.0
    n = rng.poisson(rho * box_t * (hi - lo))
    ts = rng.uniform(0.0, box_t, n)
    xs = rng.uniform(lo, hi, n)
    marked = np.abs(xs) < w / 2

    def psi(x0):
        past = (ts < t0) & (np.abs(xs - x0) < (t0 - ts))
        return 0.5 * np.count_nonzero(past & marked)

    return psi(x_base) - psi(x_cima)


print("REPLICA E4: t0 en meseta, N=400, semillas 1000-1399")
t0s = [18.0, 24.0, 30.0]
ms, ss = [], []
for t0 in t0s:
    vals = np.array([delta_psi_realizacion(SEED_OFFSET + s, RHO0, W0, R0, DH0, t0)
                     for s in range(N_REAL)])
    m, sem = vals.mean(), vals.std(ddof=1) / np.sqrt(N_REAL)
    ms.append(m); ss.append(sem)
    print(f"  t0={t0:>5.1f}: delta_psi = {m:.2f} +- {sem:.2f}")

difs = [(t0s[i], t0s[j], abs(ms[i] - ms[j]) / np.hypot(ss[i], ss[j]))
        for i in range(3) for j in range(i + 1, 3)]
for a, b, d in difs:
    print(f"  |t0={a:.0f} vs t0={b:.0f}|: {d:.2f} sigma")
maxd = max(d for _, _, d in difs)
print(f"\nMax discrepancia: {maxd:.2f} sigma -> E4 {'PASA' if maxd < 2 else 'FALLA'}")
