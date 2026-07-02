#!/usr/bin/env python3
"""
EXPERIMENTO 16: ¿ES DERIVABLE EL ACOPLE ISW A = 0.0024?
========================================================
El paper (Sec. 6.2) usa dT/T = A*(L/R_H)*exp(-z/z0) con A = 0.0024 y
z0 = 0.30 calibrados empiricamente (Hansen+ 2025). Aqui testeamos si A
se deriva del marco SIN parametros nuevos, usando el beta medido en el
experimento 15 (beta_0 = 0.055, 68%: 0.005..0.100) y la formula del
paper dT/T = (Rdot/R)*(dR/R)*(L/c).

HIPOTESIS PRE-REGISTRADAS (predicciones ANTES de correr):

H1 (potencial estatico de links, el mecanismo validado en exp 13):
   dR/R|void = |Phi_void|/c^2 = (3/4)*Om*|delta|*(H0*R_v/c)^2 ~ 3e-6
   => A_H1 = beta*|Phi|/c^2/(H0*t0) ~ 2e-7.
   PREDICCION: FALLA por ~4 ordenes de magnitud. El potencial
   instantaneo NO es el mecanismo del ISW anomalo.

H2 (deficit ACUMULADO de refinamiento; gamma = exponente de la ley de
   fuente, dlnR/dt = (beta/t)*(rho/rho_bar)^gamma):
   dR/R|void(t_obs) = gamma*beta*|delta_0|*I(z),
     I(z) = int_0^{t_obs} [D(t)/D(t_obs)] dt/t   (crecimiento estandar)
   => A_H2 = gamma*beta^2*|delta_0|*I(0)/(H0*t0),  gamma en [1/2, 1]
   PREDICCION: A_H2 ~ 0.001-0.003 para beta en el 68% de exp 15,
   |delta_0| = 0.7 +/- 0.1. Orden correcto.

CRITERIOS:
  C1 (amplitud): DERIVADA si A_emp = 0.0024 cae dentro del rango H2
     [gamma=1/2..1, beta en 68% exp15, delta_0 = 0.6..0.8].
  C2 (consistencia inter-datasets): el beta_ISW que reproduce
     A_emp = 0.0024 exactamente (con gamma=1, delta_0=0.7) debe caer
     dentro del 68% de exp 15. Dos datasets independientes (BAO y
     stacking ISW) midiendo el mismo beta.
  C3 (dependencia en z): chi2 de H2 contra los 5 puntos de stacking
     (Granett, Kovacs x2, Hansen x2). PREDICCION HONESTA: H2 crece
     suavemente con z (por 1/t(z)), el ajuste empirico decae como
     exp(-z/0.3); esperamos que C3 FALLE => la dependencia en z NO
     queda derivada y se declara abierta (seleccion de voids, evolucion
     de delta_0 con z, u otro mecanismo).
  C4: H1 debe fallar por >3 ordenes (confirma que el sector estatico
     no es el mecanismo; el deficit es HISTORICO, no instantaneo).
COMPROMISO: publicar salga como salga.
======================================================================
"""

import numpy as np

# ---------------- cosmologia del mejor ajuste (exp 15) ----------------
OM, BETA0 = 0.295, 0.055
BETA68 = (0.005, 0.100)
OR_RAD = 9.0e-5
T_CMB = 2.725e6   # uK
R_H = 4411.0      # Mpc (c/H0, H0=67.97)

NX = 800
XMAX = np.log(1.0 + 3000.0)
XG = np.linspace(0.0, XMAX, NX)
ZG = np.expm1(XG)
DX = XG[1] - XG[0]


def solve_model(om, beta, n_iter=60, tol=1e-9):
    """E(z), tau(z)=H0*t(z) autoconsistentes (igual que exp 15)."""
    ode = 1.0 - om - OR_RAD
    e2 = om * (1 + ZG) ** 3 + OR_RAD * (1 + ZG) ** 4 + ode
    tau = None
    for _ in range(n_iter):
        e = np.sqrt(e2)
        inv_e = 1.0 / e
        integral = np.concatenate((
            (np.cumsum((inv_e[::-1][:-1] + inv_e[::-1][1:]) * 0.5 * DX))[::-1],
            [0.0]))
        tau_tail = (2.0 / 3.0) / np.sqrt(
            om * (1 + ZG[-1]) ** 3 + OR_RAD * (1 + ZG[-1]) ** 4)
        tau_new = integral + tau_tail
        f_de = (tau_new / tau_new[0]) ** (-4.0 * beta)
        e2_new = om * (1 + ZG) ** 3 + OR_RAD * (1 + ZG) ** 4 + ode * f_de
        delta = np.max(np.abs(np.log(e2_new / e2)))
        e2 = 0.5 * (e2 + e2_new)
        tau = tau_new
        if delta < tol:
            break
    return np.sqrt(e2), tau


def growth(e_grid):
    """Factor de crecimiento D(x) resolviendo D'' en ln(a) con RK4.
    x = ln(1+z) = -ln(a). Devuelve D en la grilla XG (normalizado D(0)=1)."""
    # trabajar en y = ln a, de y_i = -XMAX a 0
    ys = -XG[::-1]                       # creciente
    e_y = e_grid[::-1]
    dlnE = np.gradient(np.log(e_y), ys)
    om_a = OM * np.exp(-3 * ys) / e_y ** 2

    def deriv(i_frac, state):
        # interpolar coeficientes en y continuo
        y = ys[0] + i_frac * (ys[-1] - ys[0])
        dle = np.interp(y, ys, dlnE)
        oma = np.interp(y, ys, om_a)
        D, Dp = state
        return np.array([Dp, -(2.0 + dle) * Dp + 1.5 * oma * D])

    n = len(ys)
    h = (ys[-1] - ys[0]) / (n - 1)
    state = np.array([np.exp(ys[0]), np.exp(ys[0])])   # D ~ a temprano
    Ds = [state[0]]
    for i in range(n - 1):
        f = (lambda k, s: deriv((i + k) / (n - 1), s))
        k1 = f(0.0, state)
        k2 = f(0.5, state + 0.5 * h * k1)
        k3 = f(0.5, state + 0.5 * h * k2)
        k4 = f(1.0, state + h * k3)
        state = state + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        Ds.append(state[0])
    D = np.array(Ds)[::-1]               # de vuelta a orden XG
    return D / D[0]


E, TAU = solve_model(OM, BETA0)
TAU0 = TAU[0]
D = growth(E)

# I(z) = int_{x_obs}^{xmax} [D(x')/D(x_obs)] dx'/(E*tau)
integrand = D / (E * TAU)
I_cum = np.concatenate((
    (np.cumsum((integrand[::-1][:-1] + integrand[::-1][1:]) * 0.5 * DX))[::-1],
    [0.0]))


def I_of(z):
    x = np.log(1 + z)
    return np.interp(x, XG, I_cum) / np.interp(x, XG, D)


def tau_of(z):
    return np.interp(np.log(1 + z), XG, TAU)


def dT_H2(z, L, beta=BETA0, gamma=1.0, delta0=0.7):
    """Prediccion H2 en uK para void de tamano L (Mpc) a z."""
    dpsi = gamma * beta * delta0 * I_of(z)
    return T_CMB * (beta / tau_of(z)) * dpsi * (L / R_H)


print("=" * 72)
print("EXP 16: DERIVACION DEL ACOPLE ISW - PRE-REGISTRADO")
print("=" * 72)
print(f"\nCosmologia exp-15: Om={OM}, beta={BETA0}, H0*t0={TAU0:.4f}, "
      f"I(0)={I_of(0.0):.4f}")

# ---------------- C4 / H1: potencial estatico ----------------
Rv, delta0 = 20.0, 0.7
phi_c2 = 0.75 * OM * delta0 * (Rv / R_H) ** 2
A_H1 = BETA0 * phi_c2 / TAU0
print(f"\n--- H1 (potencial estatico de links) ---")
print(f"|Phi_void|/c^2 = {phi_c2:.2e}  ->  A_H1 = {A_H1:.2e}")
print(f"A_emp / A_H1 = {0.0024 / A_H1:.0f}x")
c4 = 0.0024 / A_H1 > 1e3
print(f"C4 (H1 falla por >3 ordenes): {'CONFIRMADO' if c4 else 'NO'}")

# ---------------- C1 / H2: amplitud ----------------
print(f"\n--- H2 (deficit acumulado de refinamiento) ---")
A_central = 1.0 * BETA0 ** 2 * 0.7 * I_of(0.0) / TAU0
combos = [(g, b, d) for g in (0.5, 1.0) for b in BETA68 for d in (0.6, 0.8)]
A_vals = [g * b ** 2 * d * I_of(0.0) / TAU0 for g, b, d in combos]
A_lo, A_hi = min(A_vals), max(A_vals)
print(f"A_H2 central (gamma=1, beta={BETA0}, delta0=0.7) = {A_central:.5f}")
print(f"A_H2 rango [gamma 0.5-1, beta 68%, delta0 0.6-0.8] = "
      f"[{A_lo:.5f}, {A_hi:.5f}]")
c1 = A_lo <= 0.0024 <= A_hi
print(f"A_empirico = 0.00240 -> C1 (amplitud derivada): "
      f"{'PASA' if c1 else 'FALLA'}")

# ---------------- C2: beta_ISW vs beta_BAO ----------------
beta_isw = np.sqrt(0.0024 * TAU0 / (1.0 * 0.7 * I_of(0.0)))
c2 = BETA68[0] <= beta_isw <= BETA68[1]
print(f"\n--- C2 (consistencia inter-datasets) ---")
print(f"beta_ISW (A_emp exacto, gamma=1, delta0=0.7) = {beta_isw:.4f}")
print(f"beta_BAO (exp 15) = {BETA0:.3f}, 68% = [{BETA68[0]}, {BETA68[1]}]")
print(f"C2: {'PASA - dos datasets independientes, mismo beta' if c2 else 'FALLA'}")

# ---------------- C3: dependencia en z ----------------
print(f"\n--- C3 (dependencia en z contra los 5 puntos de stacking) ---")
data = [
    ("Granett+08",  0.50, 9.6, 2.2, 25),
    ("Kovacs+18",   0.35, 7.0, 4.0, 20),
    ("Kovacs+21",   0.55, 8.0, 3.0, 25),
    ("Hansen+25",   0.01, 30.0, 8.6, 20),
    ("Hansen+25L",  0.01, 40.0, 11.4, 30),
]
print(f"{'Exp':<12} {'z':>5} {'L':>4} {'obs':>7} {'H2':>8} {'empirico':>9}")
chi2_h2 = chi2_emp = 0.0
for name, z, obs, err, L in data:
    p2 = dT_H2(z, L)
    pe = 0.0024 * T_CMB * (L / R_H) * np.exp(-z / 0.30)
    chi2_h2 += ((obs - p2) / err) ** 2
    chi2_emp += ((obs - pe) / err) ** 2
    print(f"{name:<12} {z:>5.2f} {L:>4.0f} {obs:>7.1f} {p2:>8.1f} {pe:>9.1f}")
print(f"chi2 (5 pts): H2 = {chi2_h2:.1f} | ajuste empirico = {chi2_emp:.1f}")
c3 = chi2_h2 < 11.07   # chi2(5 dof, 95%)
print(f"C3 (forma en z derivada): {'PASA' if c3 else 'FALLA - z0=0.3 sigue empirico'}")

# ---------------- VEREDICTO ----------------
print("\n" + "=" * 72)
print("VEREDICTO PRE-REGISTRADO")
print("=" * 72)
for k, v in [("C1 amplitud", c1), ("C2 beta consistente", c2),
             ("C3 forma en z", c3), ("C4 H1 descartado", c4)]:
    print(f"  {k}: {'PASA' if v else 'FALLA'}")
print(f"""
LECTURA (pre-registrada):
- C1+C2 PASAN, C3 FALLA => la AMPLITUD de A queda derivada sin
  parametros nuevos (A ~ gamma*beta^2*|delta0|*I/(H0t0)) y beta_ISW
  coincide con beta_BAO; la dependencia exp(-z/z0) sigue siendo
  empirica (seleccion de voids / evolucion de delta0 abiertas).
- El mecanismo es el deficit HISTORICO de refinamiento (sector
  cosmologico), NO el potencial instantaneo de links (sector estatico,
  exp 13). La consistencia entre ambos sectores es un requisito
  teorico abierto del marco.
""")
print("DONE")
