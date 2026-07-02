# Resultados pre-registrados: Experimento 19 — Λ everpresent vs DESI DR2

Fecha: 2026-07-02. Pre-registro commiteado antes del run (6e1a66f).
Compromiso: publicar salga como salga.

## Resultado

**DESFAVORECIDA en esta forma de juguete** (veredicto congelado: R1 < 1%
en todos los α y tiempos de correlación).

| dlnz corr | α | R1 (≤ΛCDM) | mediana χ² | inválidas (E²≤0) |
|---|---|---|---|---|
| 0.3 | 0.25–2.0 | 0.0% | 868–1440 | 26–92% |
| 0.6 | 0.25–2.0 | 0.1–0.8% | 635–1188 | 20–77% |

Referencias: χ²_ΛCDM = 10.29, χ²_t^β = 9.16 (dof=10).

## Lectura

1. **Los BAO de DESI DR2 exigen H(z) SUAVE.** Una Λ que deambula con
   tiempo de correlación ~Hubble produce ondulaciones de orden
   ±0.9·α en Ω_Λ dentro de z<2.4, y los datos (precisión ~1-2% por
   punto) las aniquilan: mediana χ² ~100× peor que ΛCDM. Además las
   excursiones negativas de Λ invalidan 20-92% de las realizaciones
   (E²≤0 — riesgo de recolapso, reconocido por el propio programa
   ADGS).
2. **Para el problema de las dos ℛ (árbol de ramas):** la rama B
   (ρ_DE como fluctuación del conteo) queda desfavorecida en su forma
   simple. Para sobrevivir necesita tiempos de correlación >> Hubble
   a z<2.4 — es decir, efectivamente suave hoy — con lo cual converge
   fenomenológicamente a las ramas A (ℛ_ref logarítmica, β~0.01) o C
   (Λ exacta, β=0). El discriminador A/B-suave/C pasa a ser la
   precisión futura sobre β (DESI DR3 + SNe): 0.055 vs 0.01 vs 0.
3. **Caveat honesto sobre el alcance:** esto testea UNA implementación
   de juguete (ξ gaussiano por tramos en ln(1+z), envolvente
   (t₀/t)², forma de H(z) solamente). Zwane-Afshordi-Sorkin 2018
   exploraron variantes más elaboradas contra datos anteriores con
   resultados más matizados; una implementación fiel a sus Tipos
   A/B contra DR2 queda como extensión posible. El veredicto aplica
   a la forma de juguete pre-registrada, no al programa everpresent
   completo.

## Estado del árbol de las dos ℛ tras los Exps 15, 17 y 19

- Rama A (ℛ_ref ~ log del conteo; Gisin/dígitos): **viva**, predice
  β ≈ 0.007–0.015 (dentro del 68% del Exp 15), testeable.
- Rama B (fluctuación/everpresent): **desfavorecida** en forma simple
  (este experimento).
- Rama C (Λ exacta, β=0): **viva** (Δχ²≈1 del Exp 15 no la excluye).
- Exp 18 (ley de crecimiento de la valencia) sigue pendiente y
  alimenta la rama A/B con su exponente medido.
