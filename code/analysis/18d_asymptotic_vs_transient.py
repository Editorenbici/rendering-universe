#!/usr/bin/env python3
"""
EXP 18d: ¿el 2.7 del Exp 18 es asintotico o transitorio?
=========================================================
El Exp 18 midio p_eta = 2.700 +- 0.071 en eta in [6,20], con ratios
medido/teoria creciendo monotonicamente (0.146 -> 0.387). Dos lecturas
posibles que ese rango no separa:
  (T) TRANSITORIO: exponente asintotico 2 (ley de area) con amplitud
      de convergencia lenta que contamina el fit.
  (G) GENUINO: la expansion reforma la ley; exponente asintotico ~2.7.

============================ PRE-REGISTRO ============================
(Commiteado antes de correr; auditoria del autor waiveada por
instruccion explicita 2026-07-03 — el orden temporal lo prueba git.)

DISENO: grilla extendida eta in {6,9,12,16,20,26,32,40} (x2 el rango
del 18: la profundidad propia maxima pasa de 6.7 a 13.3 t_P),
N_REAL=20, misma maquinaria 18c (importada, sin editar).

MODELOS:
  M1 (genuino):     v = A * eta^p            (2 parametros, WLS log-log)
  M2a (transitorio): v = A * eta^2 * (1 - B/eta)    (lineal en v/eta^2 vs 1/eta)
  M2b (transitorio): v = A * eta^2 * (1 - B/eta^2)  (idem vs 1/eta^2;
      forma que siguio el control Minkowski 18b)

CRITERIOS (congelados):
  D1 (pendiente local lejana): p_far = pendiente log-log usando solo
      eta in {26,32,40}.
      p_far <= 2.15 -> favorece (T); p_far >= 2.50 -> favorece (G);
      intermedio -> indeciso.
  D2 (seleccion de modelo): AIC = chi2 + 2k sobre la grilla completa.
      dAIC = AIC(M1) - min(AIC(M2a), AIC(M2b)).
      dAIC >= +10 -> (T) decisivo; dAIC <= -10 -> (G) decisivo;
      |dAIC| < 10 -> indeciso.
  D3 (consistencia): si gana (T), el A asintotico de M2 debe caer en
      0.513 +- 30% (la amplitud 3/5-de-Minkowski de la servilleta);
      si cae fuera, (T) explica el exponente pero NO la amplitud, y se
      publica asi.
VEREDICTO GLOBAL: (T) si D1 y D2 apuntan a (T); (G) si ambos a (G);
cualquier mezcla -> INDECISO, se publica la tabla y se disena 18e con
eta mayor. COMPROMISO: publicar salga como salga.
======================================================================
"""

import importlib.util
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("m18c", HERE / "18c_frw_valencia.py")
m18c = importlib.util.module_from_spec(spec)
sys.modules["m18c"] = m18c
spec.loader.exec_module(m18c)          # __main__ guard: no corre nada

ETA = [6.0, 9.0, 12.0, 16.0, 20.0, 26.0, 32.0, 40.0]
N_REAL = 20
AMP = float(m18c.AMP_TEO)              # 0.5130 (pi*sqrt6/15)

print("=" * 70)
print("EXP 18d: asintotico (G) vs transitorio (T)")
print("=" * 70)
print(f"{'eta':>5} {'<v>':>10} {'SEM':>7} {'v/(0.513 eta^2)':>16}")

ms, ss = [], []
for eta in ETA:
    vs = [m18c.valencia_frw(s, eta) for s in range(N_REAL)]
    m, sem = np.mean(vs), np.std(vs, ddof=1) / np.sqrt(N_REAL)
    ms.append(m); ss.append(sem)
    print(f"{eta:>5.0f} {m:>10.1f} {sem:>7.1f} {m/(AMP*eta**2):>16.3f}",
          flush=True)

ms, ss, eta_a = np.array(ms), np.array(ss), np.array(ETA)


def wls_loglog(x, y, s):
    lx, ly = np.log(x), np.log(y)
    w = (y / s) ** 2
    xb = np.sum(w * lx) / np.sum(w)
    yb = np.sum(w * ly) / np.sum(w)
    den = np.sum(w * (lx - xb) ** 2)
    p = np.sum(w * (lx - xb) * (ly - yb)) / den
    return p, 1.0 / np.sqrt(den), np.exp(yb - p * xb)


# ---- D1: pendiente local lejana ----
sel = eta_a >= 26
p_far, sp_far, _ = wls_loglog(eta_a[sel], ms[sel], ss[sel])
d1 = "T" if p_far <= 2.15 else ("G" if p_far >= 2.50 else "indeciso")
print(f"\nD1: p_far(eta 26-40) = {p_far:.3f} +- {sp_far:.3f} -> {d1}")

# ---- D2: AIC M1 vs M2a/M2b ----
p1, sp1, A1 = wls_loglog(eta_a, ms, ss)
chi2_m1 = np.sum(((ms - A1 * eta_a ** p1) / ss) ** 2)
aic1 = chi2_m1 + 2 * 2

def fit_m2(power):
    """v/eta^2 = A - A*B/eta^power  (lineal en 1/eta^power)."""
    y = ms / eta_a ** 2
    sy = ss / eta_a ** 2
    x = 1.0 / eta_a ** power
    w = 1.0 / sy ** 2
    xb = np.sum(w * x) / np.sum(w)
    yb = np.sum(w * y) / np.sum(w)
    b = np.sum(w * (x - xb) * (y - yb)) / np.sum(w * (x - xb) ** 2)
    a0 = yb - b * xb                    # A
    pred = (a0 + b * x) * eta_a ** 2
    chi2 = np.sum(((ms - pred) / ss) ** 2)
    return a0, -b / max(a0, 1e-12), chi2

A2a, B2a, chi2_m2a = fit_m2(1.0)
A2b, B2b, chi2_m2b = fit_m2(2.0)
aic2a, aic2b = chi2_m2a + 2 * 2, chi2_m2b + 2 * 2
best2 = min(aic2a, aic2b)
daic = aic1 - best2
d2 = "T" if daic >= 10 else ("G" if daic <= -10 else "indeciso")
print(f"D2: M1 p={p1:.3f}+-{sp1:.3f} chi2={chi2_m1:.1f} AIC={aic1:.1f}")
print(f"    M2a(1/eta):  A={A2a:.3f} chi2={chi2_m2a:.1f} AIC={aic2a:.1f}")
print(f"    M2b(1/eta^2): A={A2b:.3f} chi2={chi2_m2b:.1f} AIC={aic2b:.1f}")
print(f"    dAIC(M1 - mejor M2) = {daic:+.1f} -> {d2}")

# ---- D3: consistencia de amplitud si (T) ----
A_best = A2a if aic2a <= aic2b else A2b
d3 = abs(A_best / AMP - 1.0) < 0.30
print(f"D3: A_asintotico(M2) = {A_best:.3f} vs 0.513 "
      f"({'dentro' if d3 else 'FUERA'} de +-30%)")

# ---- VEREDICTO ----
print("\n" + "=" * 70)
if d1 == "T" and d2 == "T":
    v = ("VEREDICTO: TRANSITORIO. El exponente asintotico es consistente "
         "con 2 (ley de area en FRW); el 2.7 del Exp 18 era contaminacion "
         "de convergencia." + ("" if d3 else " PERO la amplitud no cuadra "
         "con la servilleta: deficit real, se publica."))
elif d1 == "G" and d2 == "G":
    v = ("VEREDICTO: GENUINO. La expansion reforma la ley de links; el "
         "exponente asintotico es ~2.5-2.7, no 2. La rama A sigue viva "
         "(log de potencia es log); la coincidencia de area muere.")
else:
    v = (f"VEREDICTO: INDECISO (D1={d1}, D2={d2}). Se publica la tabla y "
         "se disena 18e con eta mayor.")
print(v)
print("DONE")
