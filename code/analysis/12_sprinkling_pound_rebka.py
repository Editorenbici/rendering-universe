#!/usr/bin/env python3
"""
EXPERIMENTO 12 (v2, auditado): SPRINKLING 2D + PROPAGADOR DE JOHNSTON
======================================================================
Test pre-registrado: ¿el conteo de elementos-fuente en el pasado causal
reproduce el potencial gravitacional estático correcto en 1+1D?

RUTA ELEGIDA: (b) propagador retardado de Johnston (arXiv:0806.3083).
En 2D sin masa, G_R = (1/2)·C, entonces:
    psi(e) = (1/2) · #{elementos marcados en J^-(e)}
La materia es un CAMPO sobre el causet (elementos marcados q=1 dentro
del tubo de mundo de la "varilla"), NO sprinkling mas denso: el
sprinkling es uniforme (densidad rho), como exige CST estandar
(Bombelli-Henson-Sorkin).

PREDICCION ANALITICA DEL CONTINUO (derivada ANTES de correr):
Varilla estatica de ancho w centrada en x=0, eventos de medicion a
distancias r (base) y r+dh (cima) del centro, tiempo t0:
    psi(x0)   = (1/2)·rho·w·(t0 - r(x0))       [cono cubre varilla]
    delta_psi = psi_base - psi_cima = (1/2)·rho·w·dh
valido cuando t0 > r + dh + w/2.

============================ PRE-REGISTRO ============================
(Escrito y auditado ANTES del primer run. Corregido por auditoria de
Fable: en 1+1D el potencial newtoniano es LINEAL en |x| y la fuerza es
INDEPENDIENTE de la distancia. El test 1/r NO aplica en 2D; queda
pre-registrado para la fase 4D.)

CRITERIOS DE EXITO (todos deben cumplirse; 100 realizaciones, 2sigma):
  E1. delta_psi ∝ dh:  exponente log-log = 1 dentro de 2sigma
  E2. delta_psi ∝ w (masa): exponente log-log = 1 dentro de 2sigma
  E3. delta_psi INDEPENDIENTE de r (firma 2D): exponente log-log = 0
      dentro de 2sigma, Y el modelo 1/r (exponente -1) excluido.
  E4. Meseta en t0: para t0 > r+dh+w/2, los valores consecutivos de
      delta_psi difieren < 2sigma (aplicado a delta_psi, NO a psi
      absoluto, que crece con t0 por fisica 2D legitima).
  E5. delta_psi/rho constante al variar rho (estabilidad de densidad).
  N1. Control nulo sin masa: delta_psi = 0 exacto.
  N2. Control simetrico (base en -r, cima en +r): delta_psi = 0
      dentro de 2sigma.

CRITERIOS DE FRACASO: cualquier E fallido o N violado.

CLAUSULA CRITICA (obligatoria, auditoria Fable):
  UN EXITO EN 2D NO VALIDA EL MECANISMO EN 4D. En 2D la funcion de
  Green retardada es la indicadora del INTERIOR del cono (por eso el
  conteo crudo funciona); en 4D vive SOBRE la superficie del cono
  (delta(t-r)/4pi r) y el conteo crudo del interior NO da el kernel
  1/r. Este experimento valida el pipeline y la maquinaria de conteo
  causal, no la afirmacion de Pound-Rebka en 3+1D. El test decisivo
  es la fase 4D.

COMPROMISO: el resultado se publica en el repo salga como salga.
======================================================================
"""

import numpy as np

N_REAL = 100  # realizaciones por configuracion

# Configuracion base
RHO0, W0, R0, DH0, T00 = 50.0, 4.0, 6.0, 5.0, 30.0


def delta_psi_realizacion(seed, rho, w, r, dh, t0, simetrico=False, sin_masa=False):
    """Una realizacion: sprinkle, marcar materia, contar pasado causal.

    Devuelve delta_psi = psi(base) - psi(cima).
    base en x=+r (o -r si simetrico), cima en x=+r+dh (o +r si simetrico).
    """
    rng = np.random.default_rng([seed, int(rho * 1000), int(w * 100),
                                 int(r * 100), int(dh * 100), int(t0 * 100),
                                 int(simetrico), int(sin_masa)])
    x_base = -r if simetrico else r
    x_cima = r if simetrico else r + dh

    # Caja minima que contiene ambos conos pasados y la varilla
    box_t = t0 + 1.0
    lo = min(-w / 2, x_base - t0, x_cima - t0) - 2.0
    hi = max(w / 2, x_base + t0, x_cima + t0) + 2.0

    n = rng.poisson(rho * box_t * (hi - lo))
    ts = rng.uniform(0.0, box_t, n)
    xs = rng.uniform(lo, hi, n)

    # Materia = elementos marcados dentro del tubo de mundo de la varilla
    marked = np.zeros(n, dtype=bool) if sin_masa else (np.abs(xs) < w / 2)

    def psi(x0):
        # J^-(evento): t' < t0 y |x'-x0| < t0-t'   (cono pasado)
        past = (ts < t0) & (np.abs(xs - x0) < (t0 - ts))
        return 0.5 * np.count_nonzero(past & marked)

    return psi(x_base) - psi(x_cima)


def medir(rho=RHO0, w=W0, r=R0, dh=DH0, t0=T00, **kw):
    """Media y SEM de delta_psi sobre N_REAL realizaciones."""
    vals = np.array([delta_psi_realizacion(s, rho, w, r, dh, t0, **kw)
                     for s in range(N_REAL)])
    return vals.mean(), vals.std(ddof=1) / np.sqrt(N_REAL)


def ajuste_loglog(xs, means, sems):
    """Exponente de ley de potencias por WLS en log-log. -> (b, sigma_b)"""
    lx = np.log(np.asarray(xs, float))
    ly = np.log(np.asarray(means, float))
    wgt = (np.asarray(means, float) / np.asarray(sems, float)) ** 2  # 1/sigma_log^2
    xb = np.sum(wgt * lx) / np.sum(wgt)
    yb = np.sum(wgt * ly) / np.sum(wgt)
    den = np.sum(wgt * (lx - xb) ** 2)
    b = np.sum(wgt * (lx - xb) * (ly - yb)) / den
    return b, 1.0 / np.sqrt(den)


resultados = {}

print("=" * 72)
print("EXP 12 v2: CONTEO CAUSAL (JOHNSTON) EN 2D - TEST PRE-REGISTRADO")
print("=" * 72)
print(f"\nConfig base: rho={RHO0}, w={W0}, r={R0}, dh={DH0}, t0={T00}, "
      f"N_real={N_REAL}")
print(f"Prediccion continua: delta_psi = (1/2)*rho*w*dh")

# --- E1: linealidad en dh ------------------------------------------------
print("\n--- E1: delta_psi vs dh (esperado: exponente 1, teoria 0.5*rho*w*dh)")
dhs = [2.0, 4.0, 6.0, 8.0, 10.0]
m_dh, s_dh = [], []
print(f"{'dh':>6} {'medido':>10} {'SEM':>8} {'teoria':>10} {'medido/teo':>11}")
for dh in dhs:
    m, s = medir(dh=dh, t0=max(T00, R0 + dh + W0 / 2 + 5))
    m_dh.append(m); s_dh.append(s)
    teo = 0.5 * RHO0 * W0 * dh
    print(f"{dh:>6.1f} {m:>10.1f} {s:>8.2f} {teo:>10.1f} {m/teo:>11.4f}")
b, sb = ajuste_loglog(dhs, m_dh, s_dh)
resultados['E1'] = (b, sb, abs(b - 1.0) < 2 * sb)
print(f"  Exponente: {b:.4f} +- {sb:.4f}  (esperado 1)  "
      f"{'PASA' if resultados['E1'][2] else 'FALLA'}")

# --- E2: linealidad en w (masa) ------------------------------------------
print("\n--- E2: delta_psi vs w=masa (esperado: exponente 1)")
ws = [1.0, 2.0, 4.0, 6.0, 8.0]
m_w, s_w = [], []
print(f"{'w':>6} {'medido':>10} {'SEM':>8} {'teoria':>10} {'medido/teo':>11}")
for w in ws:
    m, s = medir(w=w, t0=max(T00, R0 + DH0 + w / 2 + 5))
    m_w.append(m); s_w.append(s)
    teo = 0.5 * RHO0 * w * DH0
    print(f"{w:>6.1f} {m:>10.1f} {s:>8.2f} {teo:>10.1f} {m/teo:>11.4f}")
b, sb = ajuste_loglog(ws, m_w, s_w)
resultados['E2'] = (b, sb, abs(b - 1.0) < 2 * sb)
print(f"  Exponente: {b:.4f} +- {sb:.4f}  (esperado 1)  "
      f"{'PASA' if resultados['E2'][2] else 'FALLA'}")

# --- E3: independencia de r (firma 2D) -----------------------------------
print("\n--- E3: delta_psi vs r (esperado: exponente 0 = firma 2D; 1/r excluido)")
rs = [5.0, 8.0, 12.0, 18.0, 26.0]
m_r, s_r = [], []
print(f"{'r':>6} {'medido':>10} {'SEM':>8}")
for r in rs:
    m, s = medir(r=r, t0=r + DH0 + W0 / 2 + 5)
    m_r.append(m); s_r.append(s)
    print(f"{r:>6.1f} {m:>10.1f} {s:>8.2f}")
b, sb = ajuste_loglog(rs, m_r, s_r)
pasa_cero = abs(b) < 2 * sb
excluye_1r = abs(b - (-1.0)) > 2 * sb
resultados['E3'] = (b, sb, pasa_cero and excluye_1r)
print(f"  Exponente: {b:.4f} +- {sb:.4f}  (esperado 0)")
print(f"  Consistente con 0: {'SI' if pasa_cero else 'NO'} | "
      f"1/r excluido por {abs(b+1.0)/sb:.1f} sigma: {'SI' if excluye_1r else 'NO'}  "
      f"{'PASA' if resultados['E3'][2] else 'FALLA'}")

# --- E4: meseta en t0 -----------------------------------------------------
print("\n--- E4: delta_psi vs t0 (umbral teorico t0 > r+dh+w/2 = "
      f"{R0 + DH0 + W0/2:.0f}; meseta despues)")
t0s = [8.0, 11.0, 14.0, 18.0, 24.0, 30.0]
m_t, s_t = [], []
print(f"{'t0':>6} {'medido':>10} {'SEM':>8}")
for t0 in t0s:
    m, s = medir(t0=t0)
    m_t.append(m); s_t.append(s)
    print(f"{t0:>6.1f} {m:>10.1f} {s:>8.2f}")
# meseta: los 3 ultimos valores (todos > umbral) compatibles entre si a 2sigma
difs = [abs(m_t[i] - m_t[j]) / np.hypot(s_t[i], s_t[j])
        for i in (-3, -2) for j in (-2, -1) if i != j]
resultados['E4'] = (max(difs), None, max(difs) < 2.0)
print(f"  Max discrepancia entre t0=[{t0s[-3]:.0f},{t0s[-2]:.0f},{t0s[-1]:.0f}]: "
      f"{max(difs):.2f} sigma  {'PASA' if resultados['E4'][2] else 'FALLA'}")

# --- E5: estabilidad en rho ----------------------------------------------
print("\n--- E5: delta_psi/rho vs rho (esperado: constante = 0.5*w*dh = "
      f"{0.5 * W0 * DH0:.1f})")
rhos = [20.0, 50.0, 100.0]
norm, norm_s = [], []
print(f"{'rho':>6} {'medido':>10} {'SEM':>8} {'medido/rho':>11}")
for rho in rhos:
    m, s = medir(rho=rho)
    norm.append(m / rho); norm_s.append(s / rho)
    print(f"{rho:>6.0f} {m:>10.1f} {s:>8.2f} {m/rho:>11.4f}")
difs5 = [abs(norm[i] - norm[j]) / np.hypot(norm_s[i], norm_s[j])
         for i in range(3) for j in range(i + 1, 3)]
resultados['E5'] = (max(difs5), None, max(difs5) < 2.0)
print(f"  Max discrepancia: {max(difs5):.2f} sigma  "
      f"{'PASA' if resultados['E5'][2] else 'FALLA'}")

# --- N1: control nulo sin masa -------------------------------------------
print("\n--- N1: control nulo (sin masa): delta_psi = 0 exacto")
m, s = medir(sin_masa=True)
resultados['N1'] = (m, s, m == 0.0)
print(f"  delta_psi = {m:.4f} +- {s:.4f}  "
      f"{'PASA' if resultados['N1'][2] else 'FALLA'}")

# --- N2: control simetrico -------------------------------------------------
print("\n--- N2: control simetrico (base=-r, cima=+r): delta_psi = 0 +- 2sigma")
m, s = medir(simetrico=True)
resultados['N2'] = (m, s, abs(m) < 2 * s)
print(f"  delta_psi = {m:.3f} +- {s:.3f}  ({abs(m)/s:.2f} sigma)  "
      f"{'PASA' if resultados['N2'][2] else 'FALLA'}")

# --- VEREDICTO -------------------------------------------------------------
print("\n" + "=" * 72)
print("VEREDICTO PRE-REGISTRADO")
print("=" * 72)
todos = all(v[2] for v in resultados.values())
for k, v in resultados.items():
    print(f"  {k}: {'PASA' if v[2] else 'FALLA'}")
print()
print(f"RESULTADO GLOBAL: {'EXITO en 2D' if todos else 'FRACASO'}")
print("""
RECORDATORIO (clausula critica del pre-registro):
Exito en 2D valida el pipeline y el conteo causal como solucion
retardada en 1+1D. NO valida Pound-Rebka en 3+1D: en 4D la funcion
de Green vive SOBRE el cono (kernel 1/r), no en su interior, y el
conteo crudo del interior no la reproduce. Fase 4D pendiente.
""")
print("DONE")
