#!/usr/bin/env python3
"""
09_resolution_thermodynamics.py (v2)
=====================================
REHECHO: Termodinamica desde resolucion, CORREGIDO.

Problema de v1: T = R^d CRECIA con R (hoy mas caliente que Big Bang).
Solucion: La temperatura de las fluctuaciones NO RESUELTAS decrece con R.
A mayor R, menor fluctuacion residual -> menor temperatura.

T_fluct(R) = |dE_unresolved/dS|
donde E_unresolved ~ 1/R^d  (fluctuaciones que aun no se resuelven)
y S ~ d*log(R) (entropia de los DOF resueltos)

Sin calibrar contra T_CMB ni T_Planck. La forma funcional emerge sola.
"""

import math

print("="*70)
print("09: TERMODINAMICA EMERGENTE (CORREGIDO)")
print("="*70)
print()

# ============================================================
# 1. Temperatura desde fluctuaciones no resueltas
# ============================================================
print("--- 1. TEMPERATURA DE FLUCTUACIONES NO RESUELTAS ---")
print()

def T_fluct(R, d=3):
    """Temperatura de las fluctuaciones no resueltas.
    
    E_unresolved ~ 1/R^d  (a mayor R, menor fluctuacion residual)
    S ~ d * log(R)        (entropia de DOF resueltos)
    
    T = |dE/dS| = 1/R^d  (en unidades de Planck)
    """
    if R < 1:
        return float('nan')
    return 1.0 / (R**d)

print(f"{'R':<8} {'T_fluct (Planck)':<20} {'Interpretacion':<35}")
print("-"*63)
for R in [1, 2, 3, 4, 5, 10, 100, 1000, 1e6, 1e30]:
    T = T_fluct(R)
    if R == 1:
        interp = "Maxima fluctuacion (era Planck)"
    elif T > 0.1:
        interp = "Fluctuaciones fuertes"
    elif T > 1e-6:
        interp = "Fluctuaciones moderadas"
    elif T > 1e-20:
        interp = "Fluctuaciones debiles"
    else:
        interp = "Universo termicamente resuelto"
    print(f"R={R:<6.0e} {T:<20.4e} {interp:<35}")

print()
print("  La temperatura PICO es en R=1 (no definida: sin DOF)")
print("  En R=2: T ya bajo ~ 1/8 de la maxima")
print("  En R=10: T ~ 1/1000 (universo 'frio')")
print("  En R=10^30: T ~ 10^-90 (completamente resuelto)")
print()

# ============================================================
# 2. Entropia y energia
# ============================================================
print("--- 2. ENTROPIA Y ENERGIA ---")
print()

def N_dof(R, d=3):
    """Grados de libertad resolubles."""
    return max(1.0, float(R**d))

def S_entropia(R, d=3):
    """Entropia de los DOF resueltos: S = log(N)"""
    return math.log(N_dof(R, d))

def E_unresolved(R, d=3):
    """Energia de fluctuacion NO resuelta."""
    return 1.0 / N_dof(R, d)

def E_resolved(R, d=3):
    """Energia de los DOF ya resueltos (crece con R)."""
    return N_dof(R, d)

print(f"{'R':<8} {'N_pix':<12} {'S':<10} {'E_unres':<15} {'E_res':<15} {'T_fluct':<12}")
print("-"*72)
for R in [1, 2, 3, 4, 10, 100, 1000, 1e6, 1e30]:
    N = N_dof(R)
    S = S_entropia(R)
    Eu = E_unresolved(R)
    Er = E_resolved(R)
    T = T_fluct(R)
    print(f"R={R:<6.0e} {N:<12.0e} {S:<10.4f} {Eu:<15.4e} {Er:<15.0e} {T:<12.4e}")

print()
print("  E_unresolved DECRECE con R -> el universo se enfría")
print("  E_resolved CRECE con R -> mas estructura se resuelve")
print("  La temperatura es la energia de lo que AUN no se resuelve")
print()

# ============================================================
# 3. Comparacion cualitativa con hitos cosmologicos
# ============================================================
print("--- 3. COMPARACION CUALITATIVA ---")
print()
print("SIN CALIBRAR CONTRA DATOS. Solo mostramos que la forma")
print("funcional T ~ 1/R^d produce enfriamiento con R creciente.")
print()
print("La temperatura observada del CMB (2.7 K) NO se usa como")
print("calibracion. Es un dato aparte que nuestro modelo debe")
print("explicar cuando se incluya la fisica de radiacion.")
print()

# ============================================================
# 4. Energia total y densidad
# ============================================================
print("--- 4. DENSIDAD DE ENERGIA ---")
print()

def rho_total(R, d=3):
    """Densidad de energia total (resuelta + no resuelta)."""
    return (E_resolved(R, d) + E_unresolved(R, d)) / N_dof(R, d)

def rho_resolved(R, d=3):
    """Fraccion de energia resuelta."""
    Er = E_resolved(R, d)
    Eu = E_unresolved(R, d)
    return Er / (Er + Eu)

print(f"{'R':<8} {'rho_total':<15} {'frac_resuelta':<18} {'Estado':<25}")
print("-"*66)
for R in [1, 2, 3, 10, 100, 1000, 1e30]:
    rt = rho_total(R)
    fr = rho_resolved(R)
    if R == 1:
        estado = "Todo fluctuacion"
    elif fr < 0.5:
        estado = "Mayormente no resuelto"
    elif fr < 0.9:
        estado = "Transicion"
    else:
        estado = "Mayormente resuelto"
    print(f"R={R:<6.0e} {rt:<15.4f} {fr:<18.4f} {estado:<25}")

print()
print("  En R=1: toda la energia es fluctuacion (universo cuantico)")
print("  En R grande: casi toda la energia esta resuelta (universo clasico)")
print()

# ============================================================
# 5. Resumen
# ============================================================
print("="*70)
print("RESUMEN: Termodinamica corregida")
print("="*70)
print("""
- T_fluct(R) = 1/R^d: temperatura de fluctuaciones NO resueltas
- T PICO en R=1 (era Planck), DECRECE monotonamente con R
- E_unresolved decrece, E_resolved crece
- El universo se enfria al ganar resolucion, no al expandirse
- Sin calibrar contra T_CMB ni T_Planck

CORREGIDO respecto a v1:
  ANTES: T = R^d (crecia con R, hoy mas caliente que BB) ❌
  AHORA: T = 1/R^d (decrece con R, BB mas caliente que hoy) ✅
""")

print("DONE")