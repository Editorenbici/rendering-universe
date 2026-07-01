#!/usr/bin/env python3
"""
10_resolution_spectrum.py
==========================
REHECHO desde ∞=1: Espectros truncados por resolucion finita.

NO decimos "R=10 -> supercuerdas". Solo mostramos:
R finito limita cuantos modos de un espectro infinito
son resolubles.

∞ = 1: En R->inf, el espectro completo converge,
y esa totalidad es equivalente al estado fundamental.
"""

import numpy as np

print("="*70)
print("10: ESPECTROS TRUNCADOS POR RESOLUCION")
print("="*70)
print()

# ============================================================
# 1. Modelo generico de espectro truncado
# ============================================================
print("--- 1. ESPECTRO GENERICO CON CORTE POR R ---")
print()

def espectro(R, n_max=20, a=0):
    """Espectro de modos truncado por resolucion R.
    
    Solo los modos n < R son resolubles.
    La masa del modo n es sqrt(n - a) en unidades naturales.
    """
    modos = []
    for n in range(n_max + 1):
        if n < R:
            m2 = max(0, n - a)  # n - a, con intercepto
            modos.append((n, np.sqrt(m2)))
        else:
            modos.append((n, float('inf')))
    return modos

print(f"{'R':<6} {'Modos totales':<15} {'Modos visibles':<16} {'Primeros visibles':<20}")
print("-"*57)
for R in [1, 2, 3, 4, 5, 10]:
    e = espectro(R, n_max=15)
    visibles = [(n, m) for n, m in e if m != float('inf')]
    primeros = [f"n={n}" for n, m in visibles[:4]]
    print(f"R={R:<4} {len(e):<15} {len(visibles):<16} {', '.join(primeros):<20}")

print()
print("  R=1: solo n=0 (modo fundamental, sin torre)")
print("  R=2: modos n=0,1 (primeros 2)")
print("  R=10: modos n=0..9")
print("  R->inf: todos los modos (espectro continuo)")
print("  ∞=1: el espectro completo converge al modo fundamental")
print()

# ============================================================
# 2. Densidad de estados
# ============================================================
print("--- 2. DENSIDAD DE ESTADOS VISIBLE ---")
print()

def densidad_estados(R, E_max=10):
    """Numero de estados con energia < E_max, truncado por R."""
    count = 0
    for n in range(int(R)):
        E = np.sqrt(n)
        if E < E_max:
            count += 1
    return count

print(f"{'R':<8} {'Estados visibles':<20} {'Densidad':<15}")
print("-"*43)
for R in [1, 2, 3, 4, 5, 10, 100, 1000]:
    d = densidad_estados(R)
    print(f"R={R:<5.0e} {d:<20} {d/max(1,R):<15.4f}")

print()
print("  A mayor R, mayor densidad de estados visibles.")
print("  El espectro se 'puebla' a medida que R crece.")
print()

# ============================================================
# 3. Convergencia al continuo
# ============================================================
print("--- 3. CONVERGENCIA AL CONTINUO (R->inf) ---")
print()

def masa_promedio(R):
    """Masa promedio de los modos visibles."""
    masas = [np.sqrt(n) for n in range(int(R))]
    return np.mean(masas) if masas else 0

def masa_integral_inf(R):
    """Masa promedio teorica si el espectro fuera completo hasta R."""
    if R <= 0:
        return 0
    # Integral de sqrt(n) dn de 0 a R, dividido por R
    return (2/3) * R**0.5  # ~ (2/3) * sqrt(R)

print(f"{'R':<8} {'<m> discreto':<15} {'<m> continuo':<15} {'Diferencia':<15}")
print("-"*53)
for R in [2, 3, 4, 10, 100, 1000]:
    md = masa_promedio(R)
    mc = masa_integral_inf(R)
    diff = abs(md - mc) / mc if mc > 0 else 0
    print(f"R={R:<5.0e} {md:<15.4f} {mc:<15.4f} {diff:<15.4f}")

print()
print("  La diferencia entre el espectro discreto y el continuo")
print("  decrece a medida que R crece.")
print("  En R->inf, la diferencia tiende a 0 (∞=1).")
print()

# ============================================================
# 4. Simulacion de cutoff
# ============================================================
print("--- 4. FUNCION DE CORTE (CUTOFF POR R) ---")
print()

def cutoff_fermi(n, R, T=1):
    """Funcion de corte tipo Fermi-Dirac.
    
    Modos con n << R: sin supresion (transmisibles)
    Modos con n >> R: fuertemente suprimidos (no resolubles)
    """
    return 1.0 / (1.0 + np.exp((n - R) / T))

print(f"{'n':<6} {'cutoff(R=2)':<15} {'cutoff(R=5)':<15} {'cutoff(R=10)':<15} {'cutoff(R=100)':<15}")
print("-"*60)
for n in range(0, 15):
    c2 = cutoff_fermi(n, 2)
    c5 = cutoff_fermi(n, 5)
    c10 = cutoff_fermi(n, 10)
    c100 = cutoff_fermi(n, 100)
    print(f"n={n:<3} {c2:<15.4f} {c5:<15.4f} {c10:<15.4f} {c100:<15.4f}")

print()
print("  El corte es SUAVE (tipo Fermi), no abrupto.")
print("  Modos cerca de R estan parcialmente resueltos.")
print("  Esto es mas fisico que un corte brusco.")
print()

# ============================================================
# 5. Resumen
# ============================================================
print("="*70)
print("RESUMEN: Espectros truncados por resolucion")
print("="*70)
print("""
- R finito: solo modos n < R son resolubles
- Corte suave: los modos cerca de R estan parcialmente resueltos
- R->inf: todos los modos, espectro continuo
- ∞=1: el espectro completo y el modo fundamental son
        la misma totalidad vista a distinta resolucion

Sin forzar: supercuerdas, dimensiones extra, ni numeros famosos.
Solo mostramos que R actua como regulador fisico del espectro.
""")

print("DONE")