# Diagnóstico de atrición Exp 17 — RESUELTO: bug de marco de coordenadas

Fecha: 2026-07-05. Script de Codex (17_isw_attrition_diagnosis.py) +
test decisivo de Fable. Outputs: outputs/exp17_attrition.{json,csv}.

## La causa, probada cuantitativamente

El pipeline del Exp 17 (17_isw_stacking_pipeline.py, líneas 85/209)
metió RA/DEC ECUATORIALES de DESIVAST directamente como (θ,φ) en el
mapa SMICA, que está en coordenadas GALÁCTICAS. Cero conversión.

Test decisivo (mismos voids, misma máscara TMASK):
- Posiciones erróneas (como se midió): 34.3% de parches válidos,
  mediana de fracción válida = 0.009 (parche mediano ~totalmente
  enmascarado — el "footprint" aparente cruzaba el plano galáctico).
- Posiciones correctas (ICRS→galáctico): 98.0% válidos, mediana 1.000.
  |b| real de los voids: 19°–64°, mediana 42° (cielo limpio).

La atrición del 69% nunca fue física ni de máscara: era el bug.

## Consecuencias (sin anestesia)

1. **La medición del Exp 17 es INVÁLIDA tal como se ejecutó.** El
   ΔT = +1.24 ± 1.46 µK corresponde a posiciones sin relación con los
   voids. La predicción de −19 µK NUNCA FUE TESTEADA.
2. **El falsador #1 pasa de "FIRED" a "INVALIDADO-POR-BUG / NO
   TESTEADO".** El paper necesita erratum (decisión del autor):
   abstract (4), sección 7, status del falsador, limitación 3.
3. **Vuelve a estar en juego toda la cascada que el nulo había
   matado:** el sector ISW como calibrado, la coincidencia
   β_ISW ≈ β_BAO (exp 16), y la lectura de efectos de selección.
   Ninguna está confirmada — están NO-TESTEADAS de nuevo.
4. **V1/V2 pasaron porque eran internamente consistentes en el mismo
   marco erróneo.** La validación nunca incluyó chequeo astrométrico.

## Responsabilidad

El pipeline lo diseñé y ejecuté yo (Fable). El test de inyección que
diseñé tampoco podía detectar el bug (inyectaba en el mismo marco).
El script de atrición de Codex destapó la inconsistencia; el test
decisivo la confirmó. Cuarta asignación de esta deuda: la que valió.

## Plan Exp 17b (pendiente de autorización del autor)

- Fix de UNA línea: transformar ICRS→galáctico (astropy SkyCoord o
  hp.Rotator) antes de extraer parches.
- CRITERIOS PRE-REGISTRADOS SIN CAMBIOS (siguen congelados y son el
  test correcto). Solo cambia la astrometría.
- Validación nueva obligatoria: V0 astrométrico (verificar que el
  plano galáctico del mapa cae donde la máscara dice; stack de
  control sobre posiciones de |b| conocido).
- Re-run con auditoría autor+Codex del diff del fix ANTES del
  unblinding, como siempre.
- Con datos ya en disco: ejecutable el mismo día de la autorización.

## Lección de protocolo (quinta del proyecto)

Toda medición sobre mapas del cielo requiere validación ASTROMÉTRICA
de extremo a extremo (posición conocida → píxel esperado), no solo
estadística. Los controles nulos no detectan errores de marco: son
ciegos exactamente en la dirección del bug.
