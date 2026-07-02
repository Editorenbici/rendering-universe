#!/usr/bin/env python3
"""
EXPERIMENTO 14: CUTOFF ESPECTRAL POR RESOLUCION R
====================================================

PRE-REGISTRO (escrito antes del primer run):

HIPOTESIS:
Una resolucion causal finita R introduce una ventana suave W(k; k_R, Delta)
en el espectro primordial P_R(k), que se manifiesta como supresion en
multipolos bajos (IR cutoff) o altos (UV cutoff) del CMB.

CRITERIOS DE EXITO:
1. El cutoff produce una firma monotona y distinguible en P(k)
2. Para cutoff IR: reduce potencia en l < 30 sin afectar l >> k_R * D_*
3. Para cutoff UV: reduce potencia a alto k de forma controlada
4. k_R y Delta son identificables, no degenerados con A_s y n_s

CRITERIOS DE FRACASO:
1. El cutoff es degenerado con tilt n_s o amplitud A_s
2. La firma requiere parametros ya excluidos por datos
3. La senyal desaparece al cambiar suavidad Delta
"""

import numpy as np

# Constantes cosmologicas de referencia
A_s = 2.1e-9
n_s = 0.965
k_star = 0.05  # Mpc^-1
D_star = 14000.0  # Mpc (distancia comovil hasta ultima dispersion)

def P_primordial(k):
    return A_s * (k / k_star)**(n_s - 1)

def W_uv(k, k_R, delta):
    return 1.0 / (1.0 + np.exp((k - k_R) / delta))

def W_ir(k, k_R, delta):
    return 1.0 / (1.0 + np.exp((k_R - k) / delta))

def P_render(k, k_R, delta, mode="ir"):
    W = W_ir(k, k_R, delta) if mode == "ir" else W_uv(k, k_R, delta)
    return P_primordial(k) * W

def Cl_ratio(ell, k_R, delta, mode="ir"):
    k = ell / D_star
    return P_render(k, k_R, delta, mode) / P_primordial(k)

if __name__ == "__main__":
    print("="*70)
    print("EXP 14: CUTOFF ESPECTRAL POR RESOLUCION")
    print("="*70)
    print()
    print("PRE-REGISTRO: Pendiente de implementacion completa")
    print()
    print("Estructura:")
    print("  1. P_primordial(k) = A_s * (k/k_star)^(n_s-1)")
    print("     W_ir(k) = 1/(1+exp((k_R-k)/delta))  (suprime l bajos)")
    print("     W_uv(k) = 1/(1+exp((k-k_R)/delta))  (suprime l altos)")
    print("  2. P_render(k) = P_primordial(k) * W(k)")
    print("  3. Cl_ratio(l) ~ W(l/D_star)")
    print()
    print("Proximo paso: Codex implementa el barrido de k_R y delta")
    print()
    print("DONE")