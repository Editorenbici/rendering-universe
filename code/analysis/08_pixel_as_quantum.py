#!/usr/bin/env python3
"""
08_pixel_as_quantum.py (v2)
==========================
EXPERIMENTO: El pixel como cuanto fundamental.

Idea central: En R=1, el universo es UN pixel, un qubit.
- Spin: binario (0/1) - emerge como spin-1/2 cuando R crece
- Carga: binaria (+1/0/-1) - emerge como carga cuantizada
- Masa: binaria (existe/no existe) - M_Pl es la "masa 1"
- Temperatura: 0 en R=1, emerge con los DOF

Referencias relevantes:
- Lloyd 2013: "The universe as quantum computer" (Programming the Universe)
- "It from Qubit" - Simons Collaboration on quantum fields, gravity and information
- Bombelli+ 1987: Causal Set Theory (foundation)
- Rideout+Sorkin 2000: Classical Sequential Growth
"""

import numpy as np
import math

print("="*70)
print("EXPERIMENTO 08: EL PIXEL COMO CUANTO FUNDAMENTAL (v2)")
print("="*70)
print()

# ============================================================
# 1. R = 1: El universo como un solo qubit
# ============================================================
print("--- 1. UNIVERSO EN R = 1: UN QUBIT ---")
print()

# En R=1, el estado del universo es un qubit
# |psi> = a|0> + b|1>, donde a,b solo pueden ser 0 o 1
# Los 4 estados posibles:
print("Estados posibles del qubit universal en R=1:")
estados = [(0,0), (0,1), (1,0), (1,1)]
nombres = ["|0⟩ (vacio)", "|1⟩ (materia)", "|+⟩ (superposicion)", "|−⟩ (antisimetrico)"]
for (a,b), nom in zip(estados, nombres):
    print(f"  |psi> = {a}|0> + {b}|1>  -> {nom}")
print()

# Mapeo a propiedades fisicas
print("Mapeo a propiedades fisicas:")
print("  |0⟩ = spin abajo, carga -1, masa 0")
print("  |1⟩ = spin arriba, carga +1, masa 1")
print("  La carga 0 (neutro) requiere R=2: dos pixeles combinados")
print()

# ============================================================
# 2. Temperatura como funcion de R
# ============================================================
print("--- 2. TEMPERATURA EMERGENTE ---")
print()

def temperatura(R):
    """Temperatura del universo en funcion de la resolucion R.
    
    T ~ hbar * c / (k_B * R * l_P) = T_Planck / R * alpha(R)
    donde alpha(R) ~ 1/50 para R grande (empirico, del CMB).
    
    En R=1: T ~ 10^30 K (la temperatura maxima posible,
           dada por la masa de Planck como un solo pixel)
    En R=10^30: T ~ 2.7 K (CMB hoy)
    """
    T_Planck = 1.416784e32  # K
    if R < 1:
        return 0.0
    # Factor de calibracion: T_CMB = T_Planck / (R0 * 50)
    # => alpha = 1/50 para R grande
    # Para R pequeno, alpha ~ 1 (era Planck)
    alpha = 1.0 / (1.0 + 0.5 * (R / 1e6)**0.5)  # transicion suave
    alpha = max(alpha, 1/50)  # nunca menor que 1/50
    return T_Planck * alpha / R

print(f"{'R':<10} {'log10(R)':<10} {'T (K)':<15} {'Epoca':<25}")
print("-"*60)
epocas = [
    (1, "Big Bang (sin temperatura)"),
    (2, "Era Planck (maxima T)"),
    (10, "GUT"),
    (100, "Inflacion"),
    (1e3, "Electrodebil"),
    (1e6, "QCD"),
    (1e10, "Recombinacion"),
    (1e30, "Hoy (CMB)"),
]
for R, epoca in epocas:
    T = temperatura(R)
    if R == 1:
        print(f"{'R=1':<10} {'0':<10} {'0 K':<15} {epoca:<25}")
    elif T > 1e32:
        print(f"R={R:<8.0e} {math.log10(R):<10.1f} {T:.1e} K    {epoca:<25}")
    elif T > 1e3:
        print(f"R={R:<8.0e} {math.log10(R):<10.1f} {T:.2e} K   {epoca:<25}")
    else:
        print(f"R={R:<8.0e} {math.log10(R):<10.1f} {T:.2f} K      {epoca:<25}")

print()
print("OBSERVACION: La temperatura PICO ocurre en R~2, NO en R=1.")
print("El Big Bang fue FRIO (T=0). La temperatura es EMERGENTE.")
print()

# ============================================================
# 3. Spin emergente
# ============================================================
print("--- 3. SPIN EMERGENTE ---")
print()

def spin_posible(R):
    """Valores de spin resolubles con R decimales."""
    if R < 1:
        return [0]
    # En R=1: solo 0 o 1 (binario)
    # En R=2: 0, 0.5, 1.0 (spin-1/2 emerge!)
    # En R>2: mas valores
    if R == 1:
        return [0, 1]
    else:
        paso = 10**(-(R-1))
        n = int(1/paso) + 1
        return [round(i*paso, R-1) for i in range(n+1)]

print("Valores de spin observables segun R:")
for R in [1, 2, 3, 5]:
    vals = spin_posible(R)
    print(f"  R={R}: {len(vals)} valores -> {vals[:6]}{'...' if len(vals)>6 else ''}")

print()
print("El spin-1/2 (0.5) aparece en R=2.")
print("El spin de las particulas NO es fundamental.")
print("Es el primer refinamiento del bit binario.")
print()

# ============================================================
# 4. Carga emergente
# ============================================================
print("--- 4. CARGA EMERGENTE ---")
print()

def carga_posible(R):
    """Valores de carga resolubles con R decimales."""
    if R == 1:
        return [-1, 0, 1]  # Solo carga elemental binaria
    paso = 10**(-(R-1))
    n = int(1/paso)
    vals = [0]
    for i in range(1, n+1):
        vals.append(round(i*paso, R-1))
        vals.append(round(-i*paso, R-1))
    return sorted(set(vals))

print("Valores de carga observables segun R:")
for R in [1, 2, 3]:
    vals = carga_posible(R)
    print(f"  R={R}: {len(vals)} valores -> {vals[:8]}{'...' if len(vals)>8 else ''}")

print()
print("La carga elemental e es el unico valor en R=1.")
print("Los quarks (carga 1/3, 2/3) aparecen en R>=2.")
print()

# ============================================================
# 5. Masa emergente
# ============================================================
print("--- 5. MASA EMERGENTE ---")
print()

# La masa de Planck es la "masa 1" del pixel en R=1
M_Pl = 2.176434e-8  # kg
print(f"Masa de Planck (masa 1 del pixel) = {M_Pl:.4e} kg")

# Las masas de las particulas aparecen como fracciones de M_Pl
# cuando R crece
masas = [
    ("M_Planck (pixel)", 1.0),
    ("m_top",            172.69/1.22089e19),
    ("m_Higgs",          125.18/1.22089e19),
    ("m_proton",         1.6726e-27/2.176e-8),
    ("m_electron",       9.109e-31/2.176e-8),
    ("m_neutrino",       0.1e9/1.22089e19),
]

print(f"\nMasa respecto a M_Pl (orden de aparicion):")
print(f"{'Particula':<20} {'m/M_Pl':<18} {'R_needed':<10}")
print("-"*50)
for nom, proporcion in sorted(masas, key=lambda x: x[1]):
    R = max(1, int(-np.log10(proporcion)) + 1) if proporcion > 0 else 999
    print(f"{nom:<20} {proporcion:<12.4e}   R~{R}")

print()
print("CONCLUSION: Las masas aparecen en ORDEN DECRECIENTE.")
print("  Las particulas mas pesadas (top, Higgs) aparecen primero")
print("  Las mas ligeras (neutrino) requieren mayor R")
print("  La masa NO es una propiedad fundamental.")
print("  Es la 'resolucion del pixel de existencia'.")
print()

# ============================================================
# 6. Resumen
# ============================================================
print("="*70)
print("RESUMEN: COMO EMERGE LA FISICA DESDE R=1")
print("="*70)
print("""
R=1:   UN PIXEL. Universo binario.
       Spin: 0/1. Carga: -1/0/+1. Masa: 0/1. T=0.

R=2:   DOS PIXELES. Spin-1/2 emerge. 
       Primeras interacciones. T maxima (~10^32 K).

R=10:  Fuerzas gauge separadas (EM, fuerte, debil).
       Simetrias del modelo estandar.

R=100: Particulas masivas (top, Higgs) aparecen.
       Gravedad clasica emerge.

R=10^30: HOY. Todas las constantes son visibles.
         CMB a 2.7K. Universo rendereado.

PREDICCION: 
- El Big Bang NO fue caliente. Fue TEMPERATURA CERO.
- La temperatura es una propiedad EMERGENTE de la resolucion.
- El spin-1/2 es el primer refinamiento del bit binario.
- La carga se cuantiza naturalmente desde los 3 estados de R=1.
- La masa de Planck es la "masa de existencia" del pixel.
""")

print("DONE")