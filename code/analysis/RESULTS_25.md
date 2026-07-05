# Resultados pre-registrados: Exp 25 — reparto del presupuesto ℛ²

Fecha: 2026-07-06. Prereg + Enmienda 1 commiteados antes del run
(8da69e6, 2445cc4). Output: outputs/exp25_formal_results.json.

## Veredicto por la letra: H0 (dentro de la grilla congelada)

Ningún b ∈ [0,4] produce simultáneamente (−1, +3, +2). En la celda de
máxima palanca (N=1024, α=0.2): p_w = +2.99±0.11 (S2 ✓ clava el +3),
pero p_h = −0.11±0.08 (lejos de −1) y p_hw = +2.88±0.12 (≠ +2).

## El hallazgo cualitativo (real, robusto en α y N)

**Crossover suave conducido por el sesgo, con los signos disformes:**
p_h desciende monótonamente con b — cruza CERO en b≈2.5-3 y se vuelve
negativo — mientras p_w sube. Sin salto: es respuesta tipo
susceptibilidad, NO transición de fase (responde la pregunta de
simetría del autor: crossover, no ruptura espontánea). En b=0 el
reparto es "isótropo-ish" y el sesgo lo migra hacia el patrón
disforme. La dirección es la correcta; la magnitud no llega en esta
grilla. Control shuffle: p_w = −0.00±0.13 ✓ (p_h = +0.39±0.22, 1.8σ,
compatible con 0).

## Dos defectos de diseño, confesados (descubiertos post-run)

1. **Desajuste dimensional (de ambos: Codex en el prereg, Fable en la
   auditoría):** el toy es 1+1D (x escalar) pero los targets (−1,+3)
   con presupuesto +2 son de 3+1D. En 1+1D la métrica disforme tiene
   √−g = 1 (¡sin excedente!) y el reparto esperado sería (−1,+1,0).
   La Enmienda 1 impuso además el presupuesto ℛ² de 4D sobre el toy
   1D. Los criterios S1/S3 estaban mal calibrados para la geometría
   del toy.
2. **La grilla termina a mitad de tendencia:** p_h sigue bajando en
   b=4 (borde). "Mejor b" no convergió dentro de la grilla (cercano a
   F2). Extender b es territorio NUEVO: exige prereg 25b, no
   reinterpretación de este run.

## Consecuencia y siguiente paso (25b, cuando se autorice)

El Postulado 3′ SIGUE fenomenológico (H0). Pero el crossover con
signos correctos justifica el 25b bien hecho: **geometría 3+1 real**
(sprinkling, no toy 1D), targets dimensionalmente correctos, w medida
con el estimador de Boguñá-Krioukov (instrumento del Exp 22), y b
extendido. El compromiso del prereg original ya lo anticipaba.
