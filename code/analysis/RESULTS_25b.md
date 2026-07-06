# RESULTS — Exp 25b: validación disforme (corrida 2026-07-05/06)

**Prereg**: exp25b_prereg_2026-07-06.md (+ Enmiendas 2, 3, 4 — todas
commiteadas ANTES de la corrida). Runner v3 (3ed565a), V0 4/4 PASA.
Evidencia: `outputs/exp25b_results.json` + `outputs/exp25b_run_stdout.txt`.

## Veredicto congelado: **F2'**

Celdas de veredicto (N=4096, α∈{0.1,0.2}):

| Cantidad | Medido | Target |
|---|---|---|
| p_h | +9.968 ± 0.122 | −1 |
| p_w | +9.591 ± 0.118 | +3 |
| presupuesto p_h+p_w | +19.560 ± 0.169 | +2 |

Robustez: las 5 variantes (C3 θ=0.3/0.7, C4 W=0.15/0.35, C6 ventana
coordenada) dan la MISMA categoría F2'. El veredicto es robusto.

## Diagnóstico: confound radial del diamante (instrumento, no teorema)

Tres testigos independientes, todos pre-registrados:

1. **C1' fantasma** (sprinkling PLANO, fit contra perfil ℛ desacoplado;
   esperado ~0): p_h=+8.47, p_w=+7.02. El pipeline produce exponentes
   gigantes SIN física alguna — solo por la alineación del perfil con
   el centro del diamante, que geométricamente tiene más profundidad y
   más vecinos disponibles que el borde.
2. **C2 shuffle** (mismos valores ℛ, alineación espacial rota): −0.02 /
   +0.15 ≈ 0. El inflado requiere la alineación radial: es geometría,
   no correlación espuria.
3. **C5 positivo** (densidad ∝ℛ² en métrica plana; predicción ANALÍTICA
   +0.5/+1.5): dio +8.25/+7.94. El control con respuesta conocida
   falla por el mismo ~+8 del fantasma → el estimador está dominado
   por el confound; el teorema nunca llegó a ser interrogado.

Firma adicional consistente: en toda la grilla los exponentes escalan
como 1/α (p·α ≈ const) — el clásico brazo de palanca corto (rango de
log ℛ ~ α) dividiendo una variación geométrica fija.

## Qué significa y qué NO significa

- **El teorema de partición (−1,+3)→+2 NO fue refutado**: no llegó a
  medirse. La alarma F2' es sobre la construcción, con causa
  identificada y cuantificada por los controles diseñados para eso.
- La firma (−1,+3) **sigue siendo HIPÓTESIS** (sin cambio de estado en
  FUNDAMENTOS §II).
- Sexta aparición del patrón del instrumento raster — esta vez
  diagnosticada EN VIVO por controles pre-firmados
  (patron_instrumento_raster_2026-07-06.md se actualiza).
- Anécdota con pinzas (SIN derecho interpretativo — el prereg no
  autoriza restas post-hoc): la celda real comparable quedó ~1.3 POR
  DEBAJO del fantasma en p_h; el target era −1. Sugestivo; la vía
  legítima para saberlo es la fiducial.

## Siguiente paso (YA pre-registrado en la Enmienda 2)

> "decisión pre-registrada: región |x⃗|<0.5, |t|<0.5 si C1' falla en
> el diamante completo"

C1' falló → corresponde la re-medición **25b-fiducial**: mismos seeds,
misma grilla, fit restringido a la región fiducial donde el borde del
diamante no domina. Requiere un cambio mínimo del runner (filtro
fiducial en el fit) → re-auditoría exprés de Codex del diff → corrida.
El criterio de éxito NO cambia: S1'/F1'/F2' sobre las mismas celdas.

Publicado salga como salga (regla 5). Este resultado se publica así.
