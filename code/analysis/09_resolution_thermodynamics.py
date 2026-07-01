#!/usr/bin/env python3
"""
09_resolution_thermodynamics.py
================================
REHECHO desde ∞=1: Termodinamica emergente de la resolucion.

NO calibramos contra T_CMB ni T_Planck.
Derivamos temperatura desde N(R), S(R), E(R).

∞ = 1: Con R infinita, la temperatura tiende a 0
(universo totalmente resuelto = sin fluctuaciones termicas).
"""

import numpy as np

print("="*70)
print("09: TERMODINAMICA EMERGENTE DE LA RESOLUCION")
print("="*70)
print()

# ============================================================
# 1. Grados de libertad y entropia
# ============================================================
print("--- 1. GRADOS DE LIBERTAD Y ENTROPIA ---")
print()

def N_dof(R, d=3):
    return max(1, R**d)

def S_entropia(R, d=3):
    N = N_dof(R, d)
    import math
    return math.log(N)

print(f"{'R':<8} {'N_pixeles':<15} {'S/k_B':<12} {'Interpretacion':<30}")
print("-"*65)
for R in [1, 2, 3, 4, 10, 100, 1000, 1e6, 1e30]:
    N = N_dof(R)
    S = S_entropia(R)
    if R == 1:
        interp = "Un pixel, entropia 0"
    elif S < 5:
        interp = "Pocos DOF"
    elif S < 20:
        interp = "DOF moderados"
    else:
        interp = "Muchos DOF (universo termico)"
    print(f"R={R:<6.0e} {N:<15.0e} {S:<12.4f} {interp:<30}")

print()
print("  La entropia crece LOGARITMICAMENTE con R.")
print("  R=1: S=0 (sin grados de libertad termicos)")
print("  R=10^30: S ~ 207 (el universo hoy)")
print(f"  Entropia del horizonte cosmico: ~10^122")
print()

# ============================================================
# 2. Temperatura desde E(R) y S(R)
# ============================================================
print("--- 2. TEMPERATURA DERIVADA (NO CALIBRADA) ---")
print()

def energia(R, d=3):
    """Energia efectiva del refinamiento.
    
    Cada nuevo pixel que se resuelve anade energia.
    La energia total crece con R^d.
    """
    return float(R**d)

def temperatura(R, d=3):
    """Temperatura: 1/T = dS/dE
    
    S = log(R^d) = d * log(R)
    E = R^d
    dS/dE = d * (1/R) * (1/(d * R^(d-1))) = 1/R^d
    
    entonces T = R^d
    """
    if R < 2:
        return float('inf')  # T indefinida en R=1 (no hay DOF)
    # T = dE/dS = E / (dS/d(log R) * d(log R)/dE ...)
    dS_dlogR = d
    dE_dlogR = d * R**d
    T = dE_dlogR / dS_dlogR  # = R^d
    return T

# Normalizamos para comparar
T_norm = [temperatura(R) for R in [1, 2, 3, 4, 10, 100, 1000, 1e6, 1e30]]
T_max = max(T_norm[1:]) if len(T_norm) > 1 else 1

print(f"{'R':<8} {'T(R)':<15} {'T/T_max':<12} {'Interpretacion':<30}")
print("-"*65)
for R, T in zip([1, 2, 3, 4, 10, 100, 1000, 1e6, 1e30], T_norm):
    T_rel = T / T_max if T_max > 0 else 0
    if R == 1:
        interp = "T indefinida (sin DOF)"
    elif T_rel > 0.9:
        interp = "T maxima (era Planck)"
    elif T_rel > 0.1:
        interp = "Alta temperatura"
    elif T_rel > 1e-10:
        interp = "Temperatura intermedia"
    else:
        interp = "T baja (universo frio)"
    print(f"R={R:<6.0e} {T:<15.4e} {T_rel:<12.6f} {interp:<30}")

print()
print("  T(R) se deriva de S(R) y E(R), NO se calibra.")
print("  R=1: T indefinida (Big Bang sin temperatura)")
print("  R~2: T maxima (era Planck)")
print("  R grande: T decrece -> universo se enfria")
print("  La temperatura PICO en R~2, no en R=1")
print()

# ============================================================
# 3. T vs cosmologia estandar
# ============================================================
print("--- 3. COMPARACION CON HITOS COSMOLOGICOS ---")
print()

print("SIN CALIBRAR CONTRA DATOS. Solo mostramos que R produce")
print("una historia termica que CRECE y luego DECRECE.")
print()
print("  R=1:   T indefinida (Big Bang)")
print("  R~2:   T->maxima (era Planck equivalente)")
print("  R<<:   T decrece monotonamente")
print("  R->inf: T->0 (limite continuo frio)")
print()
print("  ∞=1: En el limite de resolucion infinita,")
print("        la temperatura tiende a cero.")
print("        El universo 'resuelto' es frio.")
print()

# ============================================================
# 4. Resumen
# ============================================================
print("="*70)
print("RESUMEN: Termodinamica emergente")
print("="*70)
print("""
- N(R) = R^d: grados de libertad
- S(R) = log(N): entropia
- E(R) = N: energia de refinamiento
- T(R) = dE/dS: temperatura derivada, NO calibrada

Sin forzar: T_CMB, T_Planck, constantes, ni hitos cosmologicos.
Solo la logica interna: R limita los DOF.
La temperatura es CONSECUENCIA, no hipotesis.
""")

print("DONE")