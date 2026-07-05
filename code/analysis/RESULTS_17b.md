# RESULTS 17b — El cielo responde de verdad: ΛCDM

Fecha: 2026-07-05. Pipeline corregido (ICRS→galáctico) commiteado
ANTES del run (579585c). Log completo: exp17b_measurement_log.txt.

## Desviación de proceso (registrada sin excusas)

El run debía esperar la auditoría autor+Codex del diff. El candado
UNBLIND falló: la verificación de Fable buscó el string "UNBLIND=False"
y lo encontró EN EL DOCSTRING, mientras el código heredaba UNBLIND=True
del 17. La medición corrió al validar. Mitigantes: diff commiteado
antes del run, criterios congelados intactos, V0/V1/V2 pasaron antes
de medir en el mismo proceso, y el pipeline es determinista (re-run
post-auditoría = resultados bit-idénticos). Sexta lección: los
candados se verifican EJECUTANDO el bloqueo, no buscando strings.

## Validación (todo antes de la medición)

- V0 ASTROMÉTRICO (nuevo): plano galáctico enmascarado / polos limpios
  ✓; 98.0% de parches válidos en posiciones corregidas ✓; |b| mediana
  42.0° ✓. La astrometría que el 17 nunca tuvo.
- V1: 1000 nulos → 0.00 ± 0.93 µK ✓
- V2: inyección −10 µK → recuperada −10.58 ± 0.89 ✓

## Medición (criterios pre-registrados del 17, congelados, sin cambios)

**ΔT_stack = +0.37 µK** (σ_null=0.93, σ_boot=0.80; **1454 voids
válidos** — 3.2× la muestra del run bugueado; SGC ahora participa con
927... [n por split abajo])

| Hipótesis | Predicción | Veredicto |
|---|---|---|
| ΛCDM | −1.5 µK | **COMPATIBLE** (2.0σ) |
| Empírica (A=0.0024) | −18.9 µK | **EXCLUIDA (20.7σ)** |
| H2 (mecanismo β²) | −62.1 µK | **EXCLUIDA (67σ)** |

Robustez: NGC +0.49 (n=527), SGC +0.30 (n=927), R_EFF>mediana −0.53
(n=730) — nulos todos. Sin dependencia de cortes.

## Veredicto

**EL FALSADOR #1 DISPARÓ — ahora sí, legítimamente.** La cuenta de ℛ
variable para el ISW anómalo queda refutada con astrometría verificada
y una muestra 3× mayor que el intento original. La cascada vuelve a
caer, esta vez con base real: el sector ISW retirado como calibrado,
la coincidencia β_ISW≈β_BAO sin base evidencial, y el apoyo a la
lectura de efectos de selección para las anomalías de la literatura.

El erratum del paper (dominio del autor) ahora es una ACTUALIZACIÓN:
la sección 7 debe referir la medición válida (17b) y documentar el
ciclo completo 17→bug→17b — que es, en sí mismo, el mejor argumento
metodológico del proyecto: encontramos nuestro propio error
astrométrico, lo publicamos, corregimos, y el veredicto se sostuvo.

Publicado salga como salga. Salió: ΛCDM.
