#!/usr/bin/env python3
"""
09_quantum_strings_render.py
============================
EXPERIMENTO 09: Conectando Render con Mecanica Cuantica y Teoria de Cuerdas.

Desde el experimento 08 (el pixel como cuanto), exploramos:
1. Mecanica Cuantica: superposicion, colapso, entrelazamiento como sampleo
2. Teoria de Cuerdas: dimensiones extra, espectro truncado, dualidades
3. Unificacion: R como unico parametro
"""

import numpy as np

print("="*70)
print("EXPERIMENTO 09: RENDER + CUANTICA + CUERDAS")
print("="*70)
print()

# ============================================================
# 1. MECANICA CUANTICA COMO SAMPLEO
# ============================================================
print("--- 1. MECANICA CUANTICA COMO EFECTO DE RESOLUCION FINITA ---")
print()

# La superposicion cuantica es un estado NO RESUELTO
# En R=1, el qubit solo puede ser |0> o |1>
# En R>1, puede ser superposicion porque "no se distingue"
print("Superposicion cuantica como limite de resolucion:")
print()
print("  En R=1:  |psi> = |0> o |1>  (colapsado, binario)")
print("  En R=2:  |psi> = a|0> + b|1>  (superposicion posible)")
print("           porque a y b tienen 1 decimal de precision")
print("           a=0.5, b=0.5  -> 50% cada estado")
print("  En R=10: |psi> con precision de 9 decimales")
print("           -> interferencia cuantica fina")
print()

# La funcion de onda se "colapsa" cuando R es suficiente
def colapso(R, n_estados):
    """El colapso ocurre cuando R es suficiente para resolver los estados."""
    if R < np.log10(n_estados) + 1:
        return "superposicion (no resuelta)"
    else:
        return "colapsado (resuelto)"

print("Colapso de la funcion de onda como aumento de R:")
ejemplos = [
    (2, 2, "spin arriba/abajo"),
    (5, 4, "4 estados de polarizacion"),
    (10, 8, "8 caminos en interferometro"),
    (100, 16, "16 historias de Feynman"),
]
for R, n_estados, desc in ejemplos:
    resultado = colapso(R, n_estados)
    print(f"  R={R:<4} {n_estados} estados ({desc}): {resultado}")

print()
print("IMPLICACION: La funcion de onda NO colapsa por 'observacion'.")
print("Colapsa porque la resolucion del sistema es suficiente")
print("para distinguir los estados como separados.")
print()

# ============================================================
# 2. ENTRELAZAMIENTO COMO CORRELACION DE SAMPLEO
# ============================================================
print("--- 2. ENTRELAZAMIENTO CUANTICO ---")
print()
print("Dos pixeles en R=1 comparten el mismo tick de tiempo.")
print("Si un pixel cambia, el otro lo 'sabe' porque estan")
print("en el mismo instante de sampleo.")
print()
print("  |psi_AB> = |0>_A|1>_B + |1>_A|0>_B  (entrelazado)")
print("  EPR = dos pixeles que compartieron el mismo R=1")
print("        y quedaron correlacionados para siempre.")
print()

# ============================================================
# 3. TEORIA DE CUERDAS: DIMENSIONES EXTRA
# ============================================================
print("--- 3. TEORIA DE CUERDAS: DIMENSIONES EXTRA ---")
print()

# En teoria de cuerdas, hay 10 o 11 dimensiones.
# En Render, las dimensiones 'extra' no estan en el espacio,
# sino en la RESOLUCION: cada cifra decimal de R es una
# 'dimension' adicional de libertad.
print("Dimensiones extra como decimales de R:")
print()
print(f"{'R':<10} {'Dimensiones efectivas':<25} {'Teoria':<25}")
print("-"*60)
dims = [
    (1,  "1 (solo tiempo)", "Universo binario"),
    (2,  "1+1 (tiempo+espacio 1D)", "Cuerda en 1D"),
    (3,  "2+1 (espacio 2D)", "Cuerda en 2D"),
    (4,  "3+1 (espacio 3D)", "NUESTRO UNIVERSO"),
    (5,  "4+1 (1 extra)", "Kaluza-Klein"),
    (10, "9+1 (6 extra)", "Supercuerdas"),
    (11, "10+1 (7 extra)", "M-theory"),
    (26, "25+1 (22 extra)", "Bosonic strings"),
]
for R, dims_str, teoria in dims:
    print(f"R={R:<6} {dims_str:<25} {teoria:<25}")

print()
print("INTERPRETACION: Las dimensiones extra de la teoria de cuerdas")
print("NO estan en el espacio. Son los DIGITOS de precision de R.")
print("Cada decimal adicional de R es una 'dimension' que las cuerdas")
print("necesitan para vibrar.")
print()
print("  R=1:   el universo tiene 1 dimension (tiempo puro)")
print("  R=2:   tiempo + 1 dimension espacial")
print("  R=4:   tiempo + 3 dimensiones espaciales (aqui estamos)")
print("  R=10:  tiempo + 9 dimensiones (supercuerdas)")
print("  R=26:  tiempo + 25 dimensiones (cuerdas bosonicas)")
print()

# ============================================================
# 4. ESPECTRO DE CUERDAS TRUNCADO POR R
# ============================================================
print("--- 4. ESPECTRO DE CUERDAS CON RESOLUCION FINITA ---")
print()

def masa_cuerda(n, R):
    """Masa de una cuerda en el modo n, truncada por R.
    
    M_n^2 = n / alpha'   (teoria)
    M_n^2 = n / alpha' * R^2 / (R^2 + n^2)   (truncado por R)
    """
    if n >= R:  # Modos no resolubles
        return float('inf')
    return np.sqrt(n) / (1.0 + n/R)  # Aproximacion

print(f"{'Modo n':<10} {'M_n (R=1)':<15} {'M_n (R=4)':<15} {'M_n (R=10)':<15} {'M_n (R=inf)':<15}")
print("-"*70)
for n in range(0, 12):
    m1 = masa_cuerda(n, 1)
    m4 = masa_cuerda(n, 4)
    m10 = masa_cuerda(n, 10)
    minf = masa_cuerda(n, 1e6)
    print(f"n={n:<5} {m1:<15.4f} {m4:<15.4f} {m10:<15.4f} {minf:<15.4f}")

print()
print("SOLO LOS MODOS n < R EXISTEN.")
print("  R=1:   solo el modo cero (sin cuerdas)")
print("  R=4:   modos n=0,1,2,3 (las primeras 4 cuerdas)")
print("  R=10:  modos n=0..9 (cuerdas del modelo estandar)")
print("  R->inf: infinitos modos (teoria de cuerdas completa)")
print()

# ============================================================
# 5. DUALIDADES COMO CAMBIO DE SAMPLEO
# ============================================================
print("--- 5. DUALIDADES COMO CAMBIO DE RESOLUCION ---")
print()

# T-duality: R <-> 1/R en cuerdas
# En Render: R_A * R_B = R_0^2
# donde A y B son dos descripciones duales
print("T-duality como dualidad de sampleo:")
print("  R_A * R_B = R_0^2")
print("  donde R_A es la resolucion de una descripcion")
print("  y R_B es la resolucion de la descripcion dual")
print()
print(f"  Si R_0 = 10^30 (hoy):")
for Ra in [1, 10, 100, 1000]:
    Rb = 1e60 / Ra
    print(f"    R_A = {Ra:<6} -> R_B = {Rb:.0e}  (escala inversa)")

print()
print("S-duality (acoplamiento fuerte/debil):")
print("  g_s <-> 1/g_s  es un cambio de R en el sampleo")
print("  Acoplamiento fuerte = baja resolucion")
print("  Acoplamiento debil  = alta resolucion")
print()

# ============================================================
# 6. HACIA LA UNIFICACION
# ============================================================
print("="*70)
print("6. UNIFICACION: R COMO UNICO PARAMETRO")
print("="*70)
print()
print("Si R es el unico parametro, entonces:")
print()
print("  R=1:   Cuanto (qubit primordial)")
print("  R=2:   Spin-1/2, primera interaccion")
print("  R=3:   alpha_EM, estructura fina")
print("  R=4:   3+1 dimensiones espaciales")
print("  R=10:  Supercuerdas (10 dimensiones)")
print("  R=11:  M-theory (11 dimensiones)")
print("  R=26:  Cuerdas bosonicas")
print("  R=10^30: HOY - todas las fuerzas, QM, gravedad")
print("  R->inf: Teoria del Todo clasica (limite continuo)")
print()
print("La unificacion NO es a alta energia.")
print("La unificacion es a ALTA RESOLUCION.")
print("Cada fuerza 'aparece' cuando R es suficiente")
print("para resolver sus grados de libertad.")
print()

print("DONE")