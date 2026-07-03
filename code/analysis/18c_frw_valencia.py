#!/usr/bin/env python3
"""
EXP 18 — FASE FRW (pre-registrada, BLOQUEADA hasta auditoria)
==============================================================
Pregunta: ¿como crece la valencia (links al pasado por elemento) en la
geometria en expansion real? Este exponente le pone numero a la rama
del arbol de las dos R.

GEOMETRIA: FRW era de materia, conformalmente plana, a(eta) = (eta)^2
(normalizacion absorbida). Sprinkling uniforme en 4-volumen FISICO
-> densidad conformal rho_conf(eta) = rho * a(eta)^4 ~ eta^8.
Muestreo exacto por CDF inversa: eta = eta_e * U^(1/9).
La estructura causal es la de Minkowski (conformal); los BLOQUEADORES
son elementos fisicos, asi que la probabilidad de link usa el volumen
fisico automaticamente.

PREDICCION ANALITICA PRE-REGISTRADA (servilleta integrada en el cono,
2026-07-03, ANTES de correr):
    v(eta_e) = (pi*sqrt(6)/15) * sqrt(rho) * eta_e^6 / eta_0^4
  con eta_0 la normalizacion de a. En tiempo propio (t ~ eta^3):
    v ~ t^2  — MISMO exponente que Minkowski: el peso a^2 del cono
  y el crecimiento del cono conspiran para mantener la ley de area.

CRITERIOS (congelados; auditoria autor + Codex antes de UNBLIND):
  F1: exponente conformal p_eta = 6.00 +- max(0.30, 2 sigma_fit)
  F2: amplitud dentro de +-20% de la formula (correcciones de borde
      esperadas ~10% como en el control 4D)
INTERPRETACION PRE-REGISTRADA:
  - F1 y F2 PASAN -> la valencia cruda es area/tracker tambien en FRW;
    el miembro viable del sector refinamiento para DE es log2(v) ~ ln t
    (rama A, Hartley/Gisin); el conteo crudo queda para el sector
    holografico. El arbol queda: rama A con fundamento, rama B muerta
    dos veces (Exp 19 + esto).
  - F1 FALLA -> la servilleta FRW esta mal y la expansion SI reforma
    la ley de crecimiento de links: resultado nuevo, se publica el
    exponente medido y se recalcula la rama.
COMPROMISO: publicar salga como salga.

CONTROLES YA PASADOS: 2D (v ~ 2 ln T, pendiente 2.01+-0.12 por
elemento, 18a) y 4D Minkowski (p = 2.089+-0.025, amplitud al 5%, 18b).
"""

import numpy as np

UNBLIND = False   # <- True solo tras auditoria del pre-registro

RHO = 1.0
TAU2MAX = 6.8
N_REAL = 20
ETA_GRID = [6.0, 9.0, 12.0, 16.0]
AMP_TEO = np.pi * np.sqrt(6.0) / 15.0 * np.sqrt(RHO)   # x eta^6 (eta_0=1)


def valencia_frw(seed, eta_e):
    """Valencia de un evento sonda en (eta_e, origen), FRW materia."""
    rng = np.random.default_rng([seed, int(eta_e * 10), 18])
    r_box = eta_e + 1.0
    # numero esperado: int rho*a^4 dV_conf = rho*(4pi/3)r^3 * int eta^8 deta
    n_exp = RHO * (4 * np.pi / 3) * r_box ** 3 * (eta_e ** 9) / 9.0
    n = rng.poisson(n_exp)
    eta = eta_e * rng.uniform(0, 1, n) ** (1.0 / 9.0)   # pdf ~ eta^8
    rr = r_box * rng.uniform(0, 1, n) ** (1.0 / 3.0)
    cos_t = rng.uniform(-1, 1, n)
    phi = rng.uniform(0, 2 * np.pi, n)
    sin_t = np.sqrt(1 - cos_t ** 2)
    x1 = rr * sin_t * np.cos(phi)
    x2 = rr * sin_t * np.sin(phi)
    x3 = rr * cos_t

    dt = eta_e - eta
    d2 = x1 ** 2 + x2 ** 2 + x3 ** 2
    past = d2 < dt ** 2
    # candidatos: tau_conformal^2 chico RESPECTO A LA DENSIDAD LOCAL
    tau2 = dt ** 2 - d2
    a4 = eta ** 8                       # a(eta)^4 con eta_0=1
    cand = past & (tau2 * np.sqrt(np.maximum(a4, 1e-30)) < TAU2MAX)
    cidx = np.flatnonzero(cand)
    pidx = np.flatnonzero(past)
    tp, p1, p2, p3 = eta[pidx], x1[pidx], x2[pidx], x3[pidx]
    links = 0
    for j in cidx:
        dtj = tp - eta[j]
        d2j = (p1 - x1[j]) ** 2 + (p2 - x2[j]) ** 2 + (p3 - x3[j]) ** 2
        if not np.any((dtj > 0) & (d2j < dtj ** 2)):
            links += 1
    return links


if __name__ == "__main__":
    print("=" * 70)
    print("EXP 18 - FASE FRW: v(eta) en era de materia")
    print("=" * 70)
    if not UNBLIND:
        print("\nBLOQUEADO: pre-registro pendiente de auditoria "
              "(autor + Codex). UNBLIND=False.")
        print(f"Prediccion congelada: v = {AMP_TEO:.4f} * eta^6 "
              f"(p_eta = 6; en tiempo propio t^2)")
        raise SystemExit
    print(f"Prediccion: v = {AMP_TEO:.4f} * eta^6\n")
    print(f"{'eta':>5} {'<v>':>10} {'SEM':>7} {'teoria':>10} {'ratio':>7}")
    ms, ss = [], []
    for eta_e in ETA_GRID:
        vs = [valencia_frw(s, eta_e) for s in range(N_REAL)]
        m, sem = np.mean(vs), np.std(vs, ddof=1) / np.sqrt(N_REAL)
        ms.append(m); ss.append(sem)
        teo = AMP_TEO * eta_e ** 6
        print(f"{eta_e:>5.0f} {m:>10.1f} {sem:>7.1f} {teo:>10.1f} "
              f"{m/teo:>7.3f}", flush=True)
    lx = np.log(np.array(ETA_GRID)); ly = np.log(np.array(ms))
    w = (np.array(ms) / np.array(ss)) ** 2
    xb = np.sum(w * lx) / np.sum(w); yb = np.sum(w * ly) / np.sum(w)
    den = np.sum(w * (lx - xb) ** 2)
    p = np.sum(w * (lx - xb) * (ly - yb)) / den
    sp = 1.0 / np.sqrt(den)
    ratio = np.mean(np.array(ms) / (AMP_TEO * np.array(ETA_GRID) ** 6))
    f1 = abs(p - 6.0) < max(0.30, 2 * sp)
    f2 = abs(ratio - 1.0) < 0.20
    print(f"\nExponente p_eta = {p:.3f} +- {sp:.3f} (F1: 6.00 +- 0.30)")
    print(f"Amplitud ratio = {ratio:.3f} (F2: 1.00 +- 0.20)")
    print(f"F1: {'PASA' if f1 else 'FALLA'} | F2: {'PASA' if f2 else 'FALLA'}")
    if f1 and f2:
        print("""
VEREDICTO PRE-REGISTRADO: la valencia cruda es AREA/TRACKER tambien en
FRW (v ~ t^2). El sector refinamiento viable para DE es log2(v) ~ ln t
(rama A). Rama B: muerta dos veces (Exp 19 + Exp 18).""")
    else:
        print("""
VEREDICTO PRE-REGISTRADO: la servilleta FRW FALLA — la expansion
reforma la ley de links. Se publica el exponente medido y se
reconstruye la rama con el.""")
    print("DONE")
