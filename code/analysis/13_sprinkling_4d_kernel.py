#!/usr/bin/env python3
"""
EXPERIMENTO 13: FASE 4D - EL TEST DECISIVO DEL KERNEL
======================================================
Dos brazos comparados sobre el MISMO sprinkling 3+1D:
  (a) psi_a = conteo CRUDO de elementos-fuente en el interior de J^-(e)
      [la hipotesis original de Render: "R = contar el pasado causal"]
  (b) psi_b = K * conteo de LINKS fuente->evento (propagador de
      Johnston 4D, arXiv:0806.3083, K = sqrt(rho/6)/(2*pi))

Fuente: bola estatica de radio a=3 en el origen (elementos marcados,
sprinkling uniforme rho=1, unidades de Planck adimensionales).
Eventos de medicion a distancia r y r+dh sobre el eje x1, tiempo t0.

PREDICCIONES ANALITICAS (derivadas ANTES de correr):
  (a) psi_a = rho*V*(t0 - r_promedio); delta_psi_a = rho*V*dh,
      INDEPENDIENTE de r, y psi_a CRECE con t0 (sin limite estatico).
  (b) psi_b = rho*V/(4*pi*r)  [EXACTO para r>a, teorema de la cascara];
      delta_psi_b = (rho*V/4pi)*(1/r - 1/(r+dh)) = (rho*V/4pi)*dh/r_eff^2
      con r_eff = sqrt(r*(r+dh)); ESTATICO (independiente de t0).

============================ PRE-REGISTRO ============================
CRITERIOS (100-250 realizaciones, 2 sigma salvo indicacion):
  F1. Kernel del potencial: exponente log-log de L_mean(r) = -1
      dentro de 2sigma, y exponente 0 excluido por >=5sigma.
  F2. Kernel de la fuerza: exponente de delta_L(r_eff) = -2 dentro
      de 2sigma.
  F3. Brazo (a) NO newtoniano: exponente de delta_Na(r_eff) = 0
      dentro de 2sigma Y exponente -2 excluido por >=5sigma.
  F4. Estaticidad (r=12, t0 en {19,25,31}): L_mean plano (max
      discrepancia pareada < 2sigma); Na_mean crece con t0
      (pendiente > 5sigma de 0).
  I1 (informativo, no gate): ratio psi_b/(rho*V/(4pi r)) ~ 1.
      Correcciones de discretizacion O(1/(r*rho^(1/4))) esperadas.
  N1. Control nulo sin masa: todos los conteos = 0 exacto.

INTERPRETACION PRE-REGISTRADA DEL VEREDICTO:
  - F1,F2,F4(b) PASAN y F3,F4(a) CONFIRMAN
      -> "R como conteo crudo del pasado causal FALLA en 4D;
          R como conteo de links (Johnston) REPRODUCE Newton."
      -> El Postulado 6 debe reformularse en terminos de links.
  - F1 o F2 FALLAN -> el mecanismo de links tampoco funciona;
      el programa gravitacional de Render queda sin mecanismo.
  - F3 FALLA (conteo crudo newtoniano) -> Fable se retracta.

COMPROMISO: resultado publicado en el repo salga como salga.
======================================================================
"""

import numpy as np

RHO = 1.0
A_BALL = 3.0
DH = 4.0
TAU2MAX = 3.5 ** 2          # P(link) < 1e-15 mas alla; corte seguro
K_JOHNSTON = np.sqrt(RHO / 6.0) / (2.0 * np.pi)
V_BALL = (4.0 / 3.0) * np.pi * A_BALL ** 3

N_KERNEL = 250   # realizaciones por r para F1-F3
N_STATIC = 150   # realizaciones por t0 para F4
N_NULL = 30

R_LIST = [8.0, 12.0, 17.0, 24.0]
T0_OF = {r: r + DH + A_BALL + 4.0 for r in R_LIST}
T0_STATIC = [19.0, 25.0, 31.0]   # en r=12


def realizacion(seed, r, t0, sin_masa=False, tag=0):
    """Sprinkle cilindro minimo; devuelve (Na, L) para base y cima."""
    rng = np.random.default_rng([seed, int(r * 10), int(t0 * 10), tag])
    L_lo, L_hi = -A_BALL - 4.0, r + DH + 4.0
    Rcyl = A_BALL + 4.0
    vol = (L_hi - L_lo) * np.pi * Rcyl ** 2 * t0
    n = rng.poisson(RHO * vol)
    ts = rng.uniform(0.0, t0, n)
    x1 = rng.uniform(L_lo, L_hi, n)
    rr = Rcyl * np.sqrt(rng.uniform(0.0, 1.0, n))
    th = rng.uniform(0.0, 2.0 * np.pi, n)
    x2 = rr * np.cos(th)
    x3 = rr * np.sin(th)
    if sin_masa:
        marked = np.zeros(n, dtype=bool)
    else:
        marked = (x1 ** 2 + x2 ** 2 + x3 ** 2) <= A_BALL ** 2

    def evento(re):
        dt = t0 - ts
        d2 = (x1 - re) ** 2 + x2 ** 2 + x3 ** 2
        past = d2 < dt ** 2
        Na = int(np.count_nonzero(past & marked))
        # candidatos a link: marcados, causales, cerca del cono
        tau2 = dt ** 2 - d2
        cidx = np.flatnonzero(past & marked & (tau2 < TAU2MAX))
        pidx = np.flatnonzero(past)
        tp, p1, p2, p3 = ts[pidx], x1[pidx], x2[pidx], x3[pidx]
        links = 0
        for j in cidx:
            dtj = tp - ts[j]
            d2j = (p1 - x1[j]) ** 2 + (p2 - x2[j]) ** 2 + (p3 - x3[j]) ** 2
            if not np.any((dtj > 0) & (d2j < dtj ** 2)):
                links += 1
        return Na, links

    Na_b, L_b = evento(r)
    Na_t, L_t = evento(r + DH)
    return Na_b, L_b, Na_t, L_t


def stats(vals):
    v = np.asarray(vals, float)
    return v.mean(), v.std(ddof=1) / np.sqrt(len(v))


def ajuste_loglog(xs, means, sems):
    lx = np.log(np.asarray(xs, float))
    ly = np.log(np.asarray(means, float))
    wgt = (np.asarray(means, float) / np.asarray(sems, float)) ** 2
    xb = np.sum(wgt * lx) / np.sum(wgt)
    yb = np.sum(wgt * ly) / np.sum(wgt)
    den = np.sum(wgt * (lx - xb) ** 2)
    return (np.sum(wgt * (lx - xb) * (ly - yb)) / den, 1.0 / np.sqrt(den))


print("=" * 72)
print("EXP 13: FASE 4D - CONTEO CRUDO vs LINKS (JOHNSTON) - PRE-REGISTRADO")
print("=" * 72)
print(f"\nrho={RHO}, a={A_BALL}, V_bola={V_BALL:.1f}, dh={DH}, "
      f"K_Johnston={K_JOHNSTON:.5f}, N_kernel={N_KERNEL}")

# ------------------- barrido en r (F1, F2, F3, I1) -----------------------
res = {}
for r in R_LIST:
    t0 = T0_OF[r]
    datos = np.array([realizacion(s, r, t0) for s in range(N_KERNEL)])
    res[r] = datos  # columnas: Na_b, L_b, Na_t, L_t

print("\n--- Barrido en r (t0 = r+dh+a+4 en cada caso) ---")
print(f"{'r':>5} {'Na_base':>10} {'L_base':>14} {'L_teo':>7} "
      f"{'dNa':>10} {'dL':>12} {'dL_teo':>7}")
Lm, Ls, dLm, dLs, dNam, dNas, ratios = [], [], [], [], [], [], []
for r in R_LIST:
    d = res[r]
    na_m, na_s = stats(d[:, 0])
    l_m, l_s = stats(d[:, 1])
    dna_m, dna_s = stats(d[:, 0] - d[:, 2])
    dl_m, dl_s = stats(d[:, 1] - d[:, 3])
    l_teo = (RHO * V_BALL / (4 * np.pi * r)) / K_JOHNSTON
    reff2 = r * (r + DH)
    dl_teo = (RHO * V_BALL / (4 * np.pi)) * DH / reff2 / K_JOHNSTON
    Lm.append(l_m); Ls.append(l_s)
    dLm.append(dl_m); dLs.append(dl_s)
    dNam.append(dna_m); dNas.append(dna_s)
    ratios.append(K_JOHNSTON * l_m * 4 * np.pi * r / (RHO * V_BALL))
    print(f"{r:>5.0f} {na_m:>10.1f} {l_m:>8.2f}+-{l_s:<4.2f} {l_teo:>7.2f} "
          f"{dna_m:>6.1f}+-{dna_s:<4.1f} {dl_m:>7.2f}+-{dl_s:<4.2f} {dl_teo:>7.2f}")

r_eff = [np.sqrt(r * (r + DH)) for r in R_LIST]

crit = {}

# F1: kernel del potencial (links): exponente -1
b, sb = ajuste_loglog(R_LIST, Lm, Ls)
crit['F1'] = abs(b + 1.0) < 2 * sb and abs(b - 0.0) / sb >= 5.0
print(f"\nF1 (potencial links ~ 1/r): exponente {b:.3f} +- {sb:.3f} "
      f"(esperado -1; 0 excluido por {abs(b)/sb:.1f} sigma)  "
      f"{'PASA' if crit['F1'] else 'FALLA'}")

# F2: kernel de la fuerza (links): exponente -2 en r_eff
b2, sb2 = ajuste_loglog(r_eff, dLm, dLs)
crit['F2'] = abs(b2 + 2.0) < 2 * sb2
print(f"F2 (fuerza links ~ 1/r_eff^2): exponente {b2:.3f} +- {sb2:.3f} "
      f"(esperado -2)  {'PASA' if crit['F2'] else 'FALLA'}")

# F3: conteo crudo NO newtoniano: exponente 0, -2 excluido
b3, sb3 = ajuste_loglog(r_eff, dNam, dNas)
crit['F3'] = abs(b3) < 2 * sb3 and abs(b3 + 2.0) / sb3 >= 5.0
print(f"F3 (fuerza conteo crudo): exponente {b3:.4f} +- {sb3:.4f} "
      f"(esperado 0; -2 excluido por {abs(b3+2.0)/sb3:.0f} sigma)  "
      f"{'PASA' if crit['F3'] else 'FALLA'}")

# I1 informativo
print(f"I1 (informativo) ratio psi_b/teoria por r: "
      + ", ".join(f"{q:.3f}" for q in ratios))

# ------------------- F4: estaticidad en r=12 -----------------------------
print("\n--- F4: estaticidad (r=12, t0 variable) ---")
Lst, Lss, Nst, Nss = [], [], [], []
for t0 in T0_STATIC:
    datos = np.array([realizacion(s, 12.0, t0, tag=7) for s in range(N_STATIC)])
    lm, lsem = stats(datos[:, 1])
    nm, nsem = stats(datos[:, 0])
    Lst.append(lm); Lss.append(lsem); Nst.append(nm); Nss.append(nsem)
    print(f"  t0={t0:>4.0f}: L_base = {lm:.2f} +- {lsem:.2f}   "
          f"Na_base = {nm:.0f} +- {nsem:.1f}")
difs = [abs(Lst[i] - Lst[j]) / np.hypot(Lss[i], Lss[j])
        for i in range(3) for j in range(i + 1, 3)]
# pendiente de Na vs t0 (lineal, WLS)
t0a = np.array(T0_STATIC)
wn = 1.0 / np.array(Nss) ** 2
tb = np.sum(wn * t0a) / np.sum(wn)
nb = np.sum(wn * np.array(Nst)) / np.sum(wn)
den = np.sum(wn * (t0a - tb) ** 2)
pend = np.sum(wn * (t0a - tb) * (np.array(Nst) - nb)) / den
pend_s = 1.0 / np.sqrt(den)
crit['F4'] = max(difs) < 2.0 and pend / pend_s > 5.0
print(f"  L plano: max {max(difs):.2f} sigma | Na pendiente "
      f"{pend:.1f} +- {pend_s:.1f} (teo {RHO*V_BALL:.1f}, "
      f"{pend/pend_s:.0f} sigma de 0)  {'PASA' if crit['F4'] else 'FALLA'}")

# ------------------- N1: control nulo -------------------------------------
datos = np.array([realizacion(s, 12.0, 23.0, sin_masa=True, tag=9)
                  for s in range(N_NULL)])
crit['N1'] = bool(np.all(datos == 0))
print(f"\nN1 (sin masa, todo=0): {'PASA' if crit['N1'] else 'FALLA'}")

# ------------------- VEREDICTO --------------------------------------------
print("\n" + "=" * 72)
print("VEREDICTO PRE-REGISTRADO (4D)")
print("=" * 72)
for k in ['F1', 'F2', 'F3', 'F4', 'N1']:
    print(f"  {k}: {'PASA' if crit[k] else 'FALLA'}")
todos = all(crit.values())
print()
if crit['F1'] and crit['F2'] and crit['F4'] and crit['F3']:
    print("CONCLUSION PRE-REGISTRADA:")
    print("  R como conteo CRUDO del pasado causal FALLA en 4D")
    print("  (fuerza independiente de r, sin limite estatico).")
    print("  R como conteo de LINKS (Johnston) REPRODUCE Newton")
    print("  (potencial 1/r, fuerza 1/r^2, estatico).")
    print("  -> El Postulado 6 debe reformularse: R cuenta LINKS,")
    print("     no elementos del interior del pasado causal.")
elif not (crit['F1'] and crit['F2']):
    print("CONCLUSION: el mecanismo de links tampoco reproduce Newton.")
    print("El programa gravitacional de Render queda sin mecanismo.")
else:
    print("CONCLUSION: resultado mixto; revisar antes de interpretar.")
print("\nDONE")
