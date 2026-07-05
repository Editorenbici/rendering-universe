# HERMES Parallel Prep — Video / Divulgación Outlines (Honest Narrative)

**Date:** 2026-07-03  
**Rules followed:** No "teoría confirmada". Tono laboratorio abierto. Solo métodos + narrativa de experimentos ya auditados o pre-reg. Materiales para revisión domingo. No ecuaciones nuevas ni claims no auditados.

## Pieza 1: “Cómo se mata una predicción: Exp 17 ISW”

**Estructura sugerida (3-5 min):**
- Opening: "En ciencia, a veces la mejor forma de avanzar es demostrar que algo NO pasa."
- Contexto honesto: Pre-registramos un stacking de voids en Planck x DESI esperando señal ISW de ~ -1 a -2 μK (literatura LCDM). 
- Método (sin detalles nuevos): Top-hat compensado, máscara estricta, UNBLIND solo tras controles.
- Resultado: ~ +1.24 ±1.46 μK (nulo dentro de error). 
- Cómo se "mata": El dato refutó la predicción esperada. Se publica igual.
- Lección: Pre-reg + honestidad = claims que mueren públicamente. Esto fortalece lo que sobrevive (links → Newton en otros exps).
- Cierre: "Matar predicciones es parte del método. Exp 17 fue una de ellas."

**Recursos visuales:** Gráficos de stacking nulo (ya en repo/RESULTS), diagrama de pipeline, "antes/después" de la hipótesis.

## Pieza 2: “Qué significa pre-registrar un experimento”

**Estructura:**
- Analogía simple: Como escribir las reglas del juego ANTES de tirar los dados.
- En este proyecto: 
  - Criterios de éxito/falla congelados en git commit ANTES de correr.
  - Ej: Exp 18d (asymptotic vs transient) con D1/D2/D3 criteria.
  - Exp 20 skeleton pre-reg.
- Beneficios: Elimina "cherry picking", "mejor seed", p-hacking.
- Ejemplo real: Exp 17 – protocolo de máscara >30%, controles V1/V2, compromiso "publicar salga como salga".
- Riesgo: A veces duele (predicciones refutadas). Pero genera confianza.
- Cierre: "Pre-registrar no es para ganar. Es para que cuando ganes, se crea."

**Visuales:** Capturas de pre-reg commits, "antes de mirar datos", diagrama frozen criteria.

## Pieza 3: “Links causales: de conteo crudo a conteo de links”

**Estructura:**
- Problema inicial: En sprinkling, contar todo lo causal pasado da aproximación burda (importante para d'Alembertian pero no para Newton local).
- Distinción clave (de exps 12-13):
  - Conteo crudo (causal past) → no reproduce potencial 1/r.
  - Conteo de **links** (covering relations, nearest causal neighbors, chequeo de bloqueadores) → sí reproduce Newton a alto sigma.
- Por qué importa: Postulado 6 ("local R from link counting") se basa en el exacto.
- Animación conceptual: Diagrama 2D/4D de sprinkling → elementos → links vs chains largas.
- Honestidad: En FRW el crecimiento cambia (ver Exp 18/18d), pero el mecanismo de "links" sigue siendo el candidato fuerte.
- Cierre: "No todo lo causal es igual. Los links son los que cargan la información local."

**Visuales:** Animaciones simples de sprinklings, comparación raw vs links (usar figuras existentes de RESULTS_12_13 si disponibles).

## Pieza 4: “Exp 18: falló, después 18d mostró transitorio”

**Estructura:**
- Setup: Predicción servilleta (Fable): en FRW valencia ~ t² con amplitud 3/5 de Minkowski.
- Run pre-reg (commit a192ad1): midió p=2.700 ±0.071 (10σ del 2).
- Veredicto: "la expansión SÍ reforma la ley de links".
- Pero caveat honesto: ratios crecientes (0.146 → 0.387) → no separa aún "asintótico 2.7" de "2 + convergencia lenta".
- 18d: diseñado para discriminar (grid eta más grande, modelos M1 vs M2).
- Lección: Un experimento refuta, el siguiente refina. Transitorio es real; la amplitud exacta necesita más eta.
- Cierre: "Fallar no es el final. Es el mapa para el próximo experimento pre-registrado."

**Visuales:** Tabla de ratios en RESULTS_18, diagrama "transitorio vs asintótico", evolución de veredictos.

## Notas generales de tono y producción
- Siempre mencionar "pre-registrado", "publicar salga como salga", "falsificación honesta".
- Incluir secciones "lo que refutamos" junto a "lo que sobrevive".
- Evitar voz de "hemos demostrado". Usar "los datos mostraron...", "el experimento refutó...".
- Música/estilo: sobrio, laboratorio, como un diario de experimentos.
- Longitud ideal: 60-120s por pieza para redes/corto.
- Fuentes: solo material ya en repo o notas auditables.

**Material entregado como preparación. Listo para que Fable revise y decida si/ cómo producir.**
