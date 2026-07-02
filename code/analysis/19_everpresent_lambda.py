#!/usr/bin/env python3
"""
EXPERIMENTO 19: LAMBDA EVERPRESENT (ESTOCASTICA) vs DESI DR2 BAO
=================================================================
Rama B del problema de las dos R: ¿rho_DE no es un conteo sino la
FLUCTUACION del conteo? Modelo de Ahmed-Dodelson-Greene-Sorkin (2004):
Lambda fluctua con envolvente ~ 1/sqrt(V_4). En unidades practicas:

  Omega_L(t) = 0.92 * alpha * xi(t) * (t0/t)^2

donde xi(t) es un proceso aleatorio de media 0 y varianza 1 con tiempo
de correlacion ~ Hubble (re-sorteado cada paso Delta ln(1+z)), y el
prefactor 0.92 sale de (t_P/t0)^2 * (rho_Planck/rho_c0) — la magia
ADGS: O(1) hoy SIN ajuste. alpha es el unico parametro libre (O(1)).

Prior art: Zwane, Afshordi & Sorkin (2018) contra SNe+BAO+CMB previos.
Aqui: forma de H(z) contra los 13 puntos oficiales DESI DR2 + cov
(la escala c/(H0 rd) se perfila; solo se testea la FORMA).

============================ PRE-REGISTRO ============================
Ensambles de N_REAL=2000 realizaciones por alpha en {0.25,0.5,1,2},
Om perfilado en grilla, dos tiempos de correlacion (dlnz 0.3 y 0.6).
Referencias fijas (Exp 15): chi2_LCDM = 10.29, chi2_tbeta = 9.16.
  R1: fraccion de realizaciones con chi2 <= chi2_LCDM.
  R2: fraccion con chi2 <= chi2_tbeta (mejor que el mejor suave).
  R3: mediana de chi2 del ensamble por alpha.
  R4: fraccion de realizaciones invalidas (E^2<=0) — costo de Lambda
      negativa transitoria.
VEREDICTO (congelado): R1 >= 10% en algun alpha -> everpresent Lambda
COMPETITIVA contra DESI DR2 (rama B viva: el t^0.055 del Exp 15 puede
leerse como realizacion suave de una Lambda fluctuante). R1 < 1% en
todos los alpha -> DESFAVORECIDA en esta forma de juguete. Intermedio
-> inconcluso, se reporta tal cual.
COMPROMISO: publicar salga como salga.
======================================================================
"""

import numpy as np

# --- datos oficiales DESI DR2 (identicos a exp 15) ---
DATA = [
    (0.295, 0, 7.942),
    (0.510, 1, 13.588), (0.510, 2, 21.863),
    (0.706, 1, 17.351), (0.706, 2, 19.455),
    (0.934, 1, 21.576), (0.934, 2, 17.641),
    (1.321, 1, 27.601), (1.321, 2, 14.176),
    (1.484, 1, 30.512), (1.484, 2, 12.817),
    (2.330, 2, 8.632),  (2.330, 1, 38.989),
]
COV = np.zeros((13, 13))
diag = [5.78998687e-03, 2.83473742e-02, 1.83928040e-01, 3.23752442e-02,
        1.11469198e-01, 2.61732816e-02, 4.04183878e-02, 1.05336516e-01,
        5.04233092e-02, 5.83020277e-01, 2.68336193e-01, 1.02136194e-02,
        2.82685779e-01]
off = {(1, 2): -3.26062007e-02, (3, 4): -2.37445646e-02,
       (5, 6): -1.12938006e-02, (7, 8): -2.90308418e-02,
       (9, 10): -1.95215562e-01, (11, 12): -2.31395216e-02}
for i, v in enumerate(diag):
    COV[i, i] = v
for (i, j), v in off.items():
    COV[i, j] = COV[j, i] = v
CINV = np.linalg.inv(COV)
DVEC = np.array([d[2] for d in DATA])

OR_RAD = 9.0e-5
CHI2_LCDM, CHI2_TBETA = 10.29, 9.16
N_REAL = 2000
ALPHAS = [0.25, 0.5, 1.0, 2.0]
DLNZ_CORR = [0.3, 0.6]
OMS = np.linspace(0.24, 0.40, 17)

NX = 400
XMAX = np.log(1.0 + 3000.0)
XG = np.linspace(0.0, XMAX, NX)
ZG = np.expm1(XG)
DX = XG[1] - XG[0]


def solve_and_chi2(om, xi_of_x, alpha, n_iter=40, tol=1e-8):
    """Resuelve E(z) con Omega_L(t)=0.92*alpha*xi(x)*(tau0/tau)^2 y
    devuelve chi2 perfilado en escala, o None si E^2<=0."""
    e2 = om * (1 + ZG) ** 3 + OR_RAD * (1 + ZG) ** 4 + (1 - om)
    tau = None
    for _ in range(n_iter):
        e = np.sqrt(np.maximum(e2, 1e-12))
        inv_e = 1.0 / e
        integral = np.concatenate((
            np.cumsum((inv_e[::-1][:-1] + inv_e[::-1][1:]) * 0.5 * DX)[::-1],
            [0.0]))
        tail = (2.0 / 3.0) / np.sqrt(om * (1 + ZG[-1]) ** 3
                                     + OR_RAD * (1 + ZG[-1]) ** 4)
        tau_new = integral + tail
        om_L = 0.92 * alpha * xi_of_x * (tau_new[0] / tau_new) ** 2
        e2_new = om * (1 + ZG) ** 3 + OR_RAD * (1 + ZG) ** 4 + om_L
        if np.any(~np.isfinite(e2_new)):
            return None
        if np.any(e2_new[ZG < 3.0] <= 0):
            return None
        delta = np.max(np.abs(e2_new - e2) / np.maximum(np.abs(e2), 1e-6))
        e2 = 0.5 * (e2 + e2_new)
        tau = tau_new
        if delta < tol:
            break
    e = np.sqrt(np.maximum(e2, 1e-12))
    igrand = np.exp(XG) / e
    dc = np.concatenate(([0.0],
        np.cumsum((igrand[:-1] + igrand[1:]) * 0.5 * DX)))
    u = np.empty(13)
    for k, (z, typ, _) in enumerate(DATA):
        x = np.log(1 + z)
        ee = np.interp(x, XG, e)
        dcz = np.interp(x, XG, dc)
        u[k] = 1.0 / ee if typ == 2 else (
            dcz if typ == 1 else (z * dcz ** 2 / ee) ** (1.0 / 3.0))
    a = u @ CINV @ u
    b = u @ CINV @ DVEC
    return float(DVEC @ CINV @ DVEC - b * b / a)


def make_xi(rng, dlnz):
    """xi(x): gaussiano estandar, constante por tramos de ancho dlnz."""
    edges = np.arange(0.0, XMAX + dlnz, dlnz)
    vals = rng.standard_normal(len(edges))
    idx = np.minimum((XG / dlnz).astype(int), len(vals) - 1)
    return vals[idx]


print("=" * 72)
print("EXP 19: LAMBDA EVERPRESENT (ADGS) vs DESI DR2 - PRE-REGISTRADO")
print("=" * 72)
print(f"Referencias: chi2_LCDM={CHI2_LCDM}, chi2_t^beta={CHI2_TBETA} "
      f"(dof=10)\n")

resumen = {}
for dlnz in DLNZ_CORR:
    for alpha in ALPHAS:
        rng = np.random.default_rng([19, int(alpha * 100), int(dlnz * 100)])
        chis, invalid = [], 0
        for r in range(N_REAL):
            xi = make_xi(rng, dlnz)
            best = np.inf
            for om in OMS:
                c = solve_and_chi2(om, xi, alpha)
                if c is None:
                    continue
                best = min(best, c)
            if np.isfinite(best):
                chis.append(best)
            else:
                invalid += 1
        chis = np.array(chis)
        r1 = np.mean(chis <= CHI2_LCDM) if len(chis) else 0.0
        r2 = np.mean(chis <= CHI2_TBETA) if len(chis) else 0.0
        med = np.median(chis) if len(chis) else np.nan
        resumen[(dlnz, alpha)] = (r1, r2, med, invalid / N_REAL)
        print(f"dlnz={dlnz:.1f} alpha={alpha:<5}: "
              f"R1(<=LCDM)={100*r1:5.1f}%  R2(<=t^b)={100*r2:5.1f}%  "
              f"mediana chi2={med:6.1f}  invalidas={100*invalid/N_REAL:4.1f}%",
              flush=True)

print("\n" + "=" * 72)
print("VEREDICTO PRE-REGISTRADO")
print("=" * 72)
best_r1 = max(v[0] for v in resumen.values())
if best_r1 >= 0.10:
    print(f"R1 max = {100*best_r1:.1f}% >= 10% -> everpresent Lambda "
          f"COMPETITIVA contra DESI DR2. Rama B VIVA: el t^0.055 del "
          f"Exp 15 admite lectura como realizacion suave de una Lambda "
          f"fluctuante.")
elif best_r1 < 0.01:
    print(f"R1 max = {100*best_r1:.1f}% < 1% -> everpresent Lambda "
          f"DESFAVORECIDA en esta forma de juguete.")
else:
    print(f"R1 max = {100*best_r1:.1f}% (1-10%) -> INCONCLUSO; se "
          f"reporta tal cual.")
print("DONE")
