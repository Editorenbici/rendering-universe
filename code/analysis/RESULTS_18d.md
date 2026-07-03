# Resultados pre-registrados: Exp 18d — el 2.7 era transitorio

Fecha: 2026-07-03. Pre-registro commiteado antes del run (acbf4f2).
Auditoría del autor waiveada por instrucción explícita; el orden
temporal criterios→datos lo prueba git.

## Veredicto: TRANSITORIO (D1 y D2 concuerdan, decisivos)

| Criterio | Resultado | Lectura |
|---|---|---|
| D1 — pendiente local η∈[26,40] | **2.075 ± 0.078** | consistente con 2 → T |
| D2 — selección de modelo | ΔAIC = **+40.7** a favor de M2a (η²·(1−B/η)); χ²: 8.4 vs 49.1 | T decisivo |
| D3 — amplitud asintótica | A = **0.256**, FUERA del ±30% de 0.513 | déficit real |

Datos (ratios v/(0.513η²) siguen convergiendo: 0.146 → 0.442 en η=6→40).

## Síntesis honesta con el Exp 18

- El veredicto del Exp 18 ("F1 falló en su rango") queda como disparó:
  sobre η∈[6,20] el fit ES 2.70. El 18d, con el rango duplicado,
  muestra que era **contaminación del transitorio 1/η**: el exponente
  asintótico es 2. **La ley de área sobrevive en FRW.**
- **PERO la amplitud es la mitad de la servilleta:** A_medido/A_teoría
  = 0.256/0.513 = **0.499** — un factor 2 casi exacto. La
  aproximación local (a constante sobre la banda de links) cuesta un
  factor ~2 en geometría en expansión. Que sea tan limpiamente ½
  sugiere un origen algebraico derivable (la variación de a a través
  de la banda); QUEDA COMO PROBLEMA ABIERTO — no se declara "resuelto
  por un factor bonito" (regla anti-numerología).

## Cascada de implicaciones (actualización del árbol)

1. **La coincidencia de área RESUCITA:** con exponente asintótico 2,
   la valencia sí escala como área también en FRW (RESULTS_18 la había
   debilitado; se restituye — la honestidad corre en ambas
   direcciones).
2. **Rama A (log₂v ~ 2 ln t):** viva, sin cambios.
3. **Rama B (ρ_DE ∝ 1/v ∝ t⁻²):** tracker — sigue muerta como DE
   (Exp 19 + el t^−0.22 medido del Exp 15).
4. **Nuevo abierto:** derivar el factor ½ de la variación de a en la
   banda (lápiz; si sale, la amplitud FRW queda cerrada).

## ABIERTO #4 CERRADO (Fable, 2026-07-03): el "factor ½" está derivado

La corrección que la servilleta omitía: P(link) depende de a⁴
PROMEDIADO sobre el intervalo candidato→sonda con el peso de volumen
del diamante 4D, w(s) = 32·min(s,1−s)³ — no de a⁴ en el candidato
(el extremo diluido, que subestima el bloqueo). Con eso:

  A_corr/A_napkin = 30·∫₀¹ x(1−x)⁸/√⟨a⁴⟩(x) dx = 0.4991
  Medido (18d):    0.256/0.513 = 0.4990
  Amplitud FRW corregida: 0.2560 vs 0.256 medida — acuerdo a 4 cifras.

Nota anti-numerología: el valor NO es exactamente ½ (es 0.4991...);
la cercanía a ½ era accidental. La amplitud FRW queda CERRADA
analíticamente: la cadena Minkowski (5%) → FRW asíntota (0.04%) →
transitorio está completa para el Paper A.
