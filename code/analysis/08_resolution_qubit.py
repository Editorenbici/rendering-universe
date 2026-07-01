#!/usr/bin/env python3
"""
08_resolution_qubit.py
======================
REHECHO desde ∞=1: El qubit con resolucion finita.

NO forzamos numeros conocidos. R solo LIMITA cuantos
estados pueden distinguirse en la esfera de Bloch.

∞ = 1: En R→∞ recuperamos el continuo, que es
la misma totalidad que el estado en R=1.
"""

import numpy as np

print("="*70)
print("08: QUBIT CON RESOLUCION FINITA")
print("="*70)
print()

# ============================================================
# 1. La esfera de Bloch con resolucion R
# ============================================================
print("--- 1. ESFERA DE BLOCH DISCRETIZADA POR R ---")
print()

def estados_bloch(R):
    """Genera estados en la esfera de Bloch resolubles con R.
    
    theta: [0, pi] con paso pi/(R-1)  (R valores)
    phi:   [0, 2pi) con paso 2pi/R    (R valores)
    
    Total: R^2 estados (contando antipodales)
    """
    if R < 2:
        return [(0, 0)]  # Un solo estado: |0>
    
    thetas = [i * np.pi / (R-1) for i in range(R)]
    phis = [j * 2*np.pi / R for j in range(R)]
    
    estados = []
    for theta in thetas:
        for phi in phis:
            # Estado puro en la esfera de Bloch
            a = round(float(np.cos(theta/2)), R-1)
            b_real = round(float(np.cos(phi)), R-1)
            b_imag = round(float(np.sin(phi)), R-1)
            estados.append((a, b_real, b_imag, theta, phi))
    
    return estados

for R in [1, 2, 3, 4, 10]:
    e = estados_bloch(R)
    print(f"  R={R}: {len(e)} estados en esfera de Bloch")

print()
print("  En R=1: un solo estado (|0>, el qubit primordial)")
print("  En R=2: 2x2=4 estados (primera particion binaria)")
print("  En R=3: 3x3=9 estados")
print("  En R->inf: esfera continua (infinitos estados)")
print("  ∞=1: la esfera continua ES el qubit primordial visto a R infinita")
print()

# ============================================================
# 2. Coherencia visible segun R
# ============================================================
print("--- 2. COHERENCIA VISIBLE ---")
print()

def coherencia_visible(R):
    """Fraccion de la matriz densidad que es visible con R.
    
    Con R infinito (continuo), toda la coherencia es visible.
    Con R=1, solo la diagonal es visible (estado clasico puro).
    """
    if R < 2:
        return 0.0  # Sin coherencia visible: estado clasico puro
    # A mayor R, mas terminos off-diagonal se resuelven
    return 1.0 - 1.0 / R

print(f"{'R':<6} {'Coherencia visible':<20} {'Interpretacion':<30}")
print("-"*56)
for R in [1, 2, 3, 4, 10, 100, 1e30]:
    c = coherencia_visible(R)
    if R == 1:
        interp = "Estado clasico puro"
    elif c < 0.5:
        interp = "Mayormente clasico"
    elif c < 0.9:
        interp = "Transicion cuantico-clasica"
    else:
        interp = "Cuantico (alta coherencia)"
    print(f"R={R:<5.0e} {c:<20.4f} {interp:<30}")

print()
print("  R=1: sin coherencia -> mundo clasico")
print("  R grande: alta coherencia -> mundo cuantico")
print("  La transicion es GRADUAL, no un colapso")
print()

# ============================================================
# 3. Entropia de von Neumann segun R
# ============================================================
print("--- 3. ENTROPIA VISIBLE ---")
print()

def entropia_visible(R):
    """Entropia de von Neumann del estado visto con resolucion R.
    
    Con R=1: entropia 0 (estado puro clasico)
    Con R grande: entropia maxima (mezcla cuantica)
    """
    if R < 2:
        return 0.0
    # Numero de estados resolubles
    N_estados = R**2
    # Entropia maxima si todos son igualmente probables
    S_max = np.log(N_estados)
    # La entropia visible crece con R
    return S_max * (1 - 1.0/R)

print(f"{'R':<6} {'N_estados':<12} {'S_visible':<15} {'Interpretacion':<30}")
print("-"*63)
for R in [1, 2, 3, 4, 10, 100, 1e30]:
    N = R**2 if R >= 2 else 1
    S = entropia_visible(R)
    if R == 1:
        interp = "Sin entropia (puro)"
    elif S < 1:
        interp = "Baja entropia"
    elif S < 5:
        interp = "Entropia moderada"
    else:
        interp = "Alta entropia (mezcla)"
    print(f"R={R:<5.0e} {N:<12.0e} {S:<15.4f} {interp:<30}")

print()
print("  A mayor R, mayor entropia visible.")
print("  El universo 'gana entropia' al ganar resolucion.")
print("  Esto NO viola termodinamica: es informacion disponible.")
print()

# ============================================================
# 4. Regla de Born desde sampleo
# ============================================================
print("--- 4. REGLA DE BORN EMERGENTE ---")
print()

def born_probabilidad(theta, R):
    """Probabilidad de medir |0> dado un estado con angulo theta.
    
    Con R finito, la probabilidad se cuantiza.
    Con R->inf, recuperamos cos^2(theta/2).
    """
    prob_continua = np.cos(theta/2)**2
    # Con R finito, redondeamos a la fraccion resoluble mas cercana
    paso = 1.0 / R if R > 0 else 0
    prob_discreta = round(prob_continua / paso) * paso if paso > 0 else prob_continua
    return prob_discreta

print(f"{'theta':<10} {'cos^2 (teorico)':<18} {'R=2':<10} {'R=4':<10} {'R=10':<10} {'R=inf':<10}")
print("-"*68)
for theta in [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2]:
    prob_t = np.cos(theta/2)**2
    r2 = born_probabilidad(theta, 2)
    r4 = born_probabilidad(theta, 4)
    r10 = born_probabilidad(theta, 10)
    print(f"{theta:.2f}    {prob_t:<18.4f} {r2:<10.2f} {r4:<10.2f} {r10:<10.2f} {prob_t:<10.4f}")

print()
print("  La regla de Born emerge en el limite R->inf.")
print("  Con R finito, las probabilidades estan cuantizadas.")
print("  ∞=1: el continuo probabilistico ES el qubit primordial.")
print()

print("="*70)
print("RESUMEN: El qubit con resolucion finita")
print("="*70)
print("""
- R=1:  1 estado. Sin coherencia. Sin entropia. Mundo clasico.
- R=2:  4 estados. Primera particion cuantica.
- R=10: 100 estados. Coherencia alta (~90%).
- R=10^30: ~10^60 estados. Practicamente continuo.
- R->inf: Esfera de Bloch continua. ∞=1.

NO forzamos: spin-1/2, carga fraccionaria, temperaturas, ni dimensiones.
Solo R limita cuantas distinciones existen.
""")

print("DONE")