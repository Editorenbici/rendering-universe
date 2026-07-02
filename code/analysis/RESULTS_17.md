# RESULTS_17 — Stacking DESIVAST × Planck (Falsador #1)

**Fecha del run:** 2026-07-02 (madrugada).
**Script:** `17_isw_stacking_pipeline.py` | **Log completo:** `exp17_measurement_log.txt`
**Pre-registro:** 6 puntos aprobados por autor + Codex ANTES del unblinding
(commit b9d00e9, anterior al resultado — el timestamp de git lo prueba).
Compromiso: publicar salga como salga.

## Validación (antes de mirar cualquier posición real)

- V1 control nulo: 1,000 sets aleatorios → 0.00 ± 0.92 µK ✓
- V2 inyección −10 µK sintética → recuperada −9.12 ± 0.95 µK ✓

## Resultado

**ΔT_stack = +1.24 ± 1.46 µK** (460 voids con parche válido, de 1,489).

Error: bootstrap sobre voids. El σ de los nulos (0.92 µK) corresponde a
~1,000 parches válidos por set; el bootstrap corrige la atrición de la
muestra real: 0.92 × √(1050/460) ≈ 1.4 ✓ consistente.

| Hipótesis (congelada antes del run) | Predicción | Veredicto |
|---|---|---|
| ΛCDM | −1.5 µK | **COMPATIBLE** (~1.9σ) |
| Empírica (A=0.0024, z₀=0.30) | −18.5 µK | **EXCLUIDA (~13σ)** |
| H2 (mecanismo β² del exp 16) | −61.7 µK | **EXCLUIDA (~41σ)** |

Robustez: NGC solo +1.12 µK; R_EFF > mediana +1.00 µK — nulos ambos.
El resultado no depende de ningún corte.

## Veredicto pre-registrado

**EL FALSADOR #1 DEL PAPER DISPARÓ.** La cuenta de ℛ variable para el
ISW anómalo queda refutada tal como estaba calibrada.

### Cascada honesta

1. **La coincidencia β_ISW ≈ β_BAO (exp 16, C2) pierde su base
   evidencial.** A=0.0024 se calibró contra supervoids extremos
   seleccionados (Granett 2008, Hansen 2025); este nulo en un catálogo
   completo NO seleccionado respalda que aquellas anomalías eran
   efectos de selección a posteriori (cf. Nadathur et al.) — lectura
   registrada como guía de interpretación ANTES de conocer el número.
2. **Sobrevive:** el sector BAO (exp 15: β = 0.055 ± 0.05, consistente
   con ΛCDM aunque no preferido) y links→Newton (exps 12-13,
   matemática independiente de este resultado).
3. **Cláusula de Lakatos:** cualquier rescate del sector ISW exige una
   predicción nueva pre-registrada (p. ej. una muestra
   supervoid-selected independiente), no una reinterpretación. El
   split R_EFF > mediana ya salió nulo: ese camino arranca cuesta
   arriba.

## Diagnóstico pendiente (no afecta el veredicto)

Atrición 460/1489: el criterio de máscara (>30% del parche enmascarado
lo descarta) eliminó casi todo SGC y ~2/3 de NGC. Ambos splits de
robustez confirman el nulo; la geometría de la atrición queda anotada
para estudio.

## Nota final

Este experimento se diseñó, congeló, auditó y ejecutó exactamente como
exige la sección 8.3 del paper, y el resultado se publica sin ajustes.
Así se ve una teoría comportándose con honestidad cuando pierde.
