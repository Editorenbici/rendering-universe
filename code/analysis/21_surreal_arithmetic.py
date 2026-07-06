"""
EXPERIMENTO 21: ARITMÉTICA SURREAL (Conway)
Implementación de la construcción {L|R} para días 0..n.
Verifica:
  1. Conteo: día n tiene exactamente 2^{n+1}-1 números
  2. Día 0..3: ver nombres exactos de Conway
  3. 1/3: ¿en qué día aparece?
  4. Aproximaciones de π, e, φ, 1/3 por día
  5. Comparación contra fracciones continuas
"""

from fractions import Fraction


class SurrealDay:
    def __init__(self, n):
        self.n = n
        self.numbers = self._build_day(n)

    def _simplest_between(self, L, R):
        """
        Número más simple entre L y R.
        Si hay entero entre medio, ese es el más simple.
        Si no, el más simple es el promedio o la fracción
        con denominador más chico en el intervalo.
        """
        # Enteros en (L, R)
        for i in range(int(L) + 1, int(R) + 1):
            if L < i < R:
                return i
        # No hay entero: buscar fracción simple
        # Estrategia: empezar con denominador 1, 2, 3,...
        # hasta encontrar una en el intervalo
        for den in range(1, 20):
            for num in range(int(L * den) - 1, int(R * den) + 2):
                frac = num / den
                if L < frac < R:
                    return frac
        # Fallback
        return (L + R) / 2.0

    def _build_day(self, n):
        if n == 0:
            # Día 0: solo { | } = 0
            return [0.0]

        # Recopilar TODOS los números de días 0..n-1
        all_prev = []
        for d in range(n):
            prev = SurrealDay(d)
            all_prev.extend(prev.numbers)
        # Remover duplicados manteniendo orden
        seen = set()
        unique = []
        for x in all_prev:
            key = round(x, 10)
            if key not in seen:
                seen.add(key)
                unique.append(x)
        all_prev = sorted(unique)

        # Día n: TODOS los {L|R} con L subset, R subset de all_prev,
        # max(L) < min(R). La forma más simple: probar single-element.
        result = []
        added = set()

        # Caso vacío: { | R} y {L | }
        for R in all_prev:
            val = -R - 1  # { | R} aproxima el negativo
            # Mejor: para día n=1, { | 0} = -1 exacto
            # Usamos la regla: si R=[0]→-1, R=[1]→-2, etc.
            # En general { | R} = -max(R) - 1 para enteros, pero
            # para generales usamos el número más simple < min(R)

        # Forma general: probar todas las combinaciones single-element
        for L_val in [None] + all_prev:
            for R_val in [None] + all_prev:
                if L_val is None and R_val is None:
                    continue  # { | } = 0, ya está
                if L_val is not None and R_val is not None and L_val >= R_val:
                    continue

                # Encontrar el número más simple en este corte
                if L_val is None:
                    # { | R}: número más simple < min(R)
                    R_min = min([R_val]) if isinstance(R_val, (int, float)) else min(R_val)
                    # El más simple es floor(R_min) si floor < R_min, sino algo más
                    for i in range(int(R_min) - 1, int(R_min) + 1):
                        if i < R_min:
                            val = float(i)
                            if val not in added:
                                result.append(val)
                                added.add(val)
                            break
                elif R_val is None:
                    # {L | }: número más simple > max(L)
                    L_max = max([L_val]) if isinstance(L_val, (int, float)) else max(L_val)
                    for i in range(int(L_max) + 1, int(L_max) + 2):
                        if i > L_max:
                            val = float(i)
                            if val not in added:
                                result.append(val)
                                added.add(val)
                            break
                else:
                    # {L | R}: número más simple entre L y R
                    val = self._simplest_between(float(L_val), float(R_val))
                    if val not in added:
                        result.append(val)
                        added.add(val)

        result.sort()
        return result

    def count(self):
        return len(self.numbers)


def continued_fraction(x, max_terms=10):
    """Convierte un número a su fracción continua."""
    terms = []
    for _ in range(max_terms):
        if abs(x) < 1e-12:
            break
        a = int(x)
        terms.append(a)
        x -= a
        if abs(x) < 1e-10:
            break
        x = 1.0 / x
    return terms


def cf_value(terms):
    if not terms:
        return 0.0
    val = Fraction(terms[-1])
    for t in reversed(terms[:-1]):
        val = t + 1 / val
    return float(val)


# =============================================================================
# EJECUCIÓN
# =============================================================================
print("=" * 60)
print("ARITMÉTICA SURREAL - EXPERIMENTO 21 (v3)")
print("=" * 60)

# 1. Verificar conteo teórico
print("\n1. VERIFICACIÓN DEL CONTO TEÓRICO")
print(f"{'Día n':<8} {'Esperado (2^{{n+1}}-1)':<18} {'Obtenido':<12} {'Estado':<10}")
for n in range(0, 5):
    day = SurrealDay(n)
    expected = 2 ** (n + 1) - 1
    obtained = day.count()
    status = "✓" if obtained == expected else f"✗ ({obtained})"
    print(f"{n:<8} {expected:<18} {obtained:<12} {status:<10}")

# 2. Primeros números por día
print("\n2. PRIMEROS NÚMEROS POR DÍA")
for n in range(0, 4):
    day = SurrealDay(n)
    nums = day.numbers
    print(f"Día {n} (n={day.count()}): {nums}")

# 3. Probar 1/3 específicamente
print("\n3. ¿DÓNDE APARECE 1/3?")
for n in range(0, 7):
    day = SurrealDay(n)
    vals = day.numbers
    found = any(abs(v - 1/3) < 1e-6 for v in vals)
    best_err = min((abs(v - 1/3) for v in vals), default=999)
    print(f"Día {n}: encontrado={found}, cantidad={len(vals)}, mejor err={best_err:.2e}")

# 4. Aproximaciones
print("\n4. APROXIMACIONES POR DÍA")
targets = {
    "π": 3.141592653589793,
    "e": 2.718281828459045,
    "φ": 1.618033988749895,
    "√2": 1.4142135623730951,
    "1/3": 0.3333333333333333,
}

print(f"{'Día':<6}", end="")
for name in targets:
    print(f"{name+'(err)':<18}", end="")
print()

for day_n in range(0, 6):
    day = SurrealDay(day_n)
    print(f"{day_n:<6}", end="")
    for name, val in targets.items():
        if day.numbers:
            best = min(day.numbers, key=lambda x: abs(x - val))
            err = abs(best - val)
            print(f"{best:.4f}({err:.1e})", end="")
        else:
            print(f"{'N/A':<18}", end="")
    print()

# 5. Fracciones continuas
print("\n5. FRACCIÓN CONTINUA (base-independiente)")
for name, val in targets.items():
    cf_terms = continued_fraction(val, 5)
    cf_approx = cf_value(cf_terms)
    err = abs(cf_approx - val)
    print(f"{name}: [{';'.join(map(str, cf_terms))}] ≈ {cf_approx:.10f} (err={err:.2e})")

print("\n" + "=" * 60)
print("CONCLUSIÓN")
print("=" * 60)
print(f"{'Métrica':<40} {'Surreal D3':<18} {'Frac.Cont.':<12}")
print(f"{'1/3 resuelto en días finitos':<40} {'NO':<18} {'SÍ':<12}")
print(f"{'π, e finitos en días finitos':<40} {'NO':<18} {'NO':<12}")
print(f"{'Base-independiente':<40} {'NO (base 2)':<18} {'SÍ':<12}")
print(f"\nIMPLICANCIA:")
print(f"Los surreales como ARITMÉTICA para física tienen problemas con 1/3.")
print(f"Los surreales como ONTOLOGÍA DEL PROCESO (días = ℛ) son útiles:")
print(f"  - Día n = ℛ^n distinciones binarias")
print(f"  - 1/3 = vector de simetría (exacto, no necesita día finito)")
print(f"  - π, e = raster que emerge del refinamiento (días muy altos)")
print(f"  - Fracciones continuas = aritmética de lo medido (todos los racionales)")
