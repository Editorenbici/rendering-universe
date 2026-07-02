#!/usr/bin/env python3
"""
EXPERIMENTO 15: LIKELIHOOD DIRECTO DE R(t) CONTRA DESI DR2 BAO
===============================================================
Arbitro pre-registrado de la tension de beta_0 (falsador #4 del paper):
reconstruccion por bins daba beta ~ -0.02..0.07; el fit w0waCDM de DESI
implica beta_0 ~ 0.14. Aqui ajustamos R(t) DIRECTAMENTE, sin pasar por
la parametrizacion w0-wa.

MODELO (una sola funcion monotona):
  R(t) = R0 * (t/t0)^beta   (beta constante; beta>0 = monotono creciente)
  rho_DE(z)/rho_DE(0) = (R/R0)^(-4) = (t(z)/t0)^(-4*beta)
  E^2(z) = Om*(1+z)^3 + Or*(1+z)^4 + (1-Om-Or)*(t(z)/t0)^(-4*beta)
  t(z) autoconsistente por iteracion (t depende de E, E de t).
  beta = 0  <=>  LCDM exacto (anidado).

DATOS (verificados 2026-07-01 contra el release oficial de likelihood,
github.com/CobayaSampler/bao_data/desi_bao_dr2; arXiv:2503.14738):
  13 mediciones (D_V, D_M, D_H sobre r_d; 7 tracers) + covarianza
  oficial completa (bloques por tracer con correlacion D_M-D_H).
  NOTA: los D_H/r_d del script 02 estaban corruptos desde un commit
  previo (crecian con z, fisicamente imposible); restaurados hoy.

PARAMETROS: Om, beta; la escala s = c/(H0*r_d) se perfila
analiticamente (todos los observables son lineales en s).

============================ PRE-REGISTRO ============================
Reportar (con y sin prior gaussiano Om = 0.3111 +/- 0.0056):
  R1. beta_hat con intervalos 68% / 95% (perfil en Om y s, delta-chi2).
  R2. Preferencia sobre LCDM: dchi2 = chi2(beta=0) - chi2(beta_hat).
  R3. Monotonicidad: ¿beta >= 0 dentro del 95%? (si beta < 0 a >2sigma,
      hallazgo ADVERSO para el marco: R decreciente).
  R4. ARBITRO de la tension: ¿cual de {0.02-0.07} y {0.14} cae dentro
      del 68% / 95%? Resultado "ambos compatibles" = la tension era un
      artefacto de comparar estimadores distintos; resultado "uno
      excluido" = ese estimador queda descartado; "ambos excluidos" =
      problema real del marco.
  R5. Bondad de ajuste: chi2_min / dof (dof = 13 - 3).
  Ademas: w0_eff = -1 + (4/3)*beta/(H0*t0) del mejor ajuste (conversion
  exacta, no la aproximacion de era de materia w0 = -1+2*beta).
COMPROMISO: publicar el resultado salga como salga.
======================================================================
"""

import numpy as np

# ------------------- DATOS OFICIALES DESI DR2 -----------------------
# (z, tipo, valor); tipo: 0=DV/rd, 1=DM/rd, 2=DH/rd
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

OR_RAD = 9.0e-5   # radiacion (fija; afecta t(z) en el 1er %, E(z<2.4) ~nada)

# ------------------- MODELO AUTOCONSISTENTE -------------------------
NX = 600
XMAX = np.log(1.0 + 3000.0)
XG = np.linspace(0.0, XMAX, NX)          # x = ln(1+z)
ZG = np.expm1(XG)
DX = XG[1] - XG[0]


def solve_model(om, beta, n_iter=60, tol=1e-9):
    """Resuelve E(z) y tau(z)=H0*t(z) autoconsistentes. Devuelve
    (E en la grilla, tau0) o None si no converge."""
    ode = 1.0 - om - OR_RAD
    e2 = om * (1 + ZG) ** 3 + OR_RAD * (1 + ZG) ** 4 + ode  # arranque LCDM
    tau = None
    for _ in range(n_iter):
        e = np.sqrt(e2)
        # tau(x) = int_x^xmax dx'/E + cola de materia analitica
        inv_e = 1.0 / e
        integral = np.concatenate((
            (np.cumsum((inv_e[::-1][:-1] + inv_e[::-1][1:]) * 0.5 * DX))[::-1],
            [0.0]))
        tau_tail = (2.0 / 3.0) / np.sqrt(om * (1 + ZG[-1]) ** 3 + OR_RAD * (1 + ZG[-1]) ** 4)
        tau_new = integral + tau_tail
        f_de = (tau_new / tau_new[0]) ** (-4.0 * beta)
        e2_new = om * (1 + ZG) ** 3 + OR_RAD * (1 + ZG) ** 4 + ode * f_de
        if np.any(~np.isfinite(e2_new)) or np.any(e2_new <= 0):
            return None
        delta = np.max(np.abs(np.log(e2_new / e2)))
        e2 = 0.5 * (e2 + e2_new)          # amortiguado
        tau = tau_new
        if delta < tol:
            break
    return np.sqrt(e2), tau[0]


def chi2_of(om, beta, om_prior=None):
    """chi2 perfilado en s. Devuelve (chi2, s_hat, tau0)."""
    sol = solve_model(om, beta)
    if sol is None:
        return np.inf, np.nan, np.nan
    e, tau0 = sol
    inv_e = 1.0 / e
    # D_C(z)/ (c/H0) = int_0^x e^{x'} dx'/E
    igrand = np.exp(XG) * inv_e
    dc = np.concatenate(([0.0],
        np.cumsum((igrand[:-1] + igrand[1:]) * 0.5 * DX)))
    u = np.empty(13)
    for k, (z, typ, _) in enumerate(DATA):
        x = np.log(1 + z)
        ee = np.interp(x, XG, e)
        dcz = np.interp(x, XG, dc)
        if typ == 2:
            u[k] = 1.0 / ee
        elif typ == 1:
            u[k] = dcz
        else:
            u[k] = (z * dcz ** 2 / ee) ** (1.0 / 3.0)
    a = u @ CINV @ u
    b = u @ CINV @ DVEC
    c0 = DVEC @ CINV @ DVEC
    s_hat = b / a
    chi2 = c0 - b * b / a
    if om_prior is not None:
        chi2 += ((om - om_prior[0]) / om_prior[1]) ** 2
    return chi2, s_hat, tau0


def scan(om_prior=None, label=""):
    oms = np.linspace(0.22, 0.42, 81)
    betas = np.linspace(-0.30, 0.45, 151)
    grid = np.full((len(betas), len(oms)), np.inf)
    for j, om in enumerate(oms):
        for i, bt in enumerate(betas):
            grid[i, j] = chi2_of(om, bt, om_prior)[0]
    prof = grid.min(axis=1)               # perfil en Om
    i0 = int(np.argmin(prof))
    j0 = int(np.argmin(grid[i0]))
    bhat, omhat = betas[i0], oms[j0]
    chi2min = grid[i0, j0]
    d = prof - chi2min
    in68 = betas[d <= 1.0]
    in95 = betas[d <= 3.84]
    # LCDM anidado
    iL = int(np.argmin(np.abs(betas)))
    chi2_lcdm = prof[iL]
    _, s_hat, tau0 = chi2_of(omhat, bhat, om_prior)
    w0_eff = -1.0 + (4.0 / 3.0) * bhat / tau0

    print(f"\n--- {label} ---")
    print(f"beta_hat = {bhat:+.3f}  68%: [{in68[0]:+.3f}, {in68[-1]:+.3f}]"
          f"  95%: [{in95[0]:+.3f}, {in95[-1]:+.3f}]")
    print(f"Om_hat = {omhat:.3f} | H0*rd = {299792.458/s_hat:.0f} km/s"
          f" | H0*t0 = {tau0:.4f}")
    print(f"chi2_min = {chi2min:.2f} (dof=10) | chi2(LCDM) = {chi2_lcdm:.2f}"
          f" | dchi2(pref. dinamica) = {chi2_lcdm - chi2min:.2f}")
    print(f"w0_eff (conversion exacta) = {w0_eff:.3f}")
    for target, name in [(0.02, "reconstr. min 0.02"), (0.07, "reconstr. max 0.07"),
                         (0.14, "DESI w0-fit 0.14")]:
        it = int(np.argmin(np.abs(betas - target)))
        dd = prof[it] - chi2min
        status = "68%" if dd <= 1.0 else ("95%" if dd <= 3.84 else "EXCLUIDO 95%")
        print(f"  beta = {target:+.2f} ({name}): dchi2 = {dd:5.2f} -> {status}")
    return betas, prof, bhat, chi2min, chi2_lcdm


print("=" * 72)
print("EXP 15: LIKELIHOOD DIRECTO DE R(t) ~ t^beta vs DESI DR2 BAO (13 pts)")
print("=" * 72)

b1, p1, bh1, c1, cl1 = scan(None, "BAO solo (Om libre)")
b2, p2, bh2, c2, cl2 = scan((0.3111, 0.0056),
                            "BAO + prior Om = 0.3111 +/- 0.0056 (aprox. Planck)")

np.savez("paper/tables/exp15_beta_profile.npz",
         betas=b1, prof_baonly=p1, prof_prior=p2)
print("\nPerfiles guardados en paper/tables/exp15_beta_profile.npz")
print("DONE")
