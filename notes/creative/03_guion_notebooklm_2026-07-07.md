# 03 — Guion NotebookLM: "El falsador" (~12 min)
**Revisión 2026-07-07.** 3 actos + patrón de cierre. Companion del Paper 2.
Audiencia general. Sin ecuaciones. Sin jerga técnica.

**Claims fuente:** FUNDAMENTOS §I #9 (REFUTADO-FIRME), PROTOCOLO reglas 3, 5.
**Patrón:** notes/foundations/patron_instrumento_raster_2026-07-06.md.

---

# ACTO 1 — EL CIELO DIJO QUE NO

## Segmento 1 — Pre-registrar (2:00)

**Hook:** "Hay una forma de hacer ciencia que casi nadie practica: escribir el resultado ANTES de medir. No la hipótesis. El resultado. Con el número. Y publicarlo pase lo que pase."

*Narrativa:* En 2024, un equipo en Ecuador escribió un manifiesto. No en un paper, no en una pizarra — en un commit de git. "Predecimos que el stacking ISW dará −19 microkelvin. Publicamos salga como salga." Lo firmaron con el hash del commit.

*Contexto:* La predicción no era vaga. Era un número concreto, falsable, con un rango de hasta −61 microkelvin. El telescopio (Planck), el catálogo (DESI), todo público. Sin cocina.

**Cierre:** "Eso es un pre-registro. No es heroico. Es una regla que te pones para no mover el arco después de disparar."

## Segmento 2 — La medición (2:30)

*Narrativa:* Planck contra DESI. 752 voids. El stacking cayó en +1.2 microkelvin. No −19. No −61. +1.2. La barra de error era de ±1.5.

*Pausa.* "Por 13 desviaciones estándar, la predicción estaba fuera."

*Tono:* La predicción estaba muerta. No "desfavorecida", no "tensionada". Muerta. El equipo publicó el resultado. Tal cual. Sin "peros". Sin reinterpretaciones. El manifiesto original está en el repositorio, sin tocar una coma.

**Frase:** "El cielo dijo que no. Y ellos lo publicaron."

---

# ACTO 2 — EL INSTRUMENTO

## Segmento 3 — El bug (2:30)

*Narrativa:* Semanas después, una revisora externa (Fable) encontró algo. Las coordenadas de los voids no estaban en el marco que todos asumían. El equipo había medido en coordenadas ecuatoriales... pero el catálogo DESI estaba en galácticas. La diferencia era de ~2 grados.

*Pausa.* "El stacking no estaba midiendo el cielo. Estaba midiendo el instrumento."

*Tono forense:* "No fue un error humano descuidado. Fue un error de clase: medir la estructura del objeto con las coordenadas del instrumento. El mismo error que hace que un círculo pixelado mida π=4 en vez de 3.14. La medida no estaba mal porque faltaran datos — estaba mal porque la herramienta y el objeto hablaban idiomas distintos."

*Dilema:* Dos caminos. Ocultar el bug (nadie iba a re-medir 752 voids) o publicarlo. El equipo publicó el bug antes de tener la corrección.

**Cierre:** "Publicar un error propio no es fracaso. Es el único acto que convierte un error en ciencia."

## Segmento 4 — La regla (1:30)

*Narrativa:* El bug no era nuevo. El proyecto ya había chocado con la misma pared antes: una discrepancia 2.70 vs 2.95 por usar un estimador suave en vez del conteo exacto de bloqueadores. Y la literatura CST llevaba años con el mismo problema: la distancia espacial medida por adyacencia no converge a la métrica.

*Tono:* "Cuatro fallas. Un mismo patrón: medir estructura con coordenadas del instrumento. Y lo peor: el refinamiento no lo corrige. Lo consolida con barras de error más chicas."

*Transición:* "De ese patrón nació una regla nueva: ante cualquier estimador, preguntar: ¿esto mediría algo si el objeto fuera trivial y solo el instrumento variara?"

---

# ACTO 3 — LA REFUTACIÓN QUE SE SOSTIENE

## Segmento 5 — Corregir (2:30)

*Narrativa:* El equipo corrigió la astrometría. Validación de extremo a extremo: los marcos se leen del header, no se asumen. 1454 voids esta vez (el catálogo completo, no una submuestra). El stacking volvió a caer...

*Pausa.* "...en +0.37 microkelvin. ±0.93. A 20.7σ de la predicción. A 67σ del modelo de la competencia."

*El clímax:* "La refutación NO era el bug. El bug solo hizo que la refutación fuera ligeramente menos precisa. La refutación se sostuvo. Corregida, la historia era más verdadera, no menos."

*Visual mental:* El manifiesto original, intacto, al lado del resultado corregido.

## Segmento 6 — Publicar dos veces (1:30)

*Narrativa:* El equipo publicó dos veces. Primero el resultado con el bug (13σ). Después la corrección (20.7σ). Los dos commits están en el repositorio, visibles, fechados, ordenados.

*Tono:* "Publicar un resultado equivocado duele. Publicar la corrección y que la refutación se sostenga — eso no duele. Eso es el método funcionando."

**Frase:** "Perder bien también es ganar."

---

# CIERRE — EL PATRÓN

## Segmento 7 — El mismo error (1:00)

*Narrativa:* "La escalera, el bug del 17 y la ventana del 25b son la misma historia. En los tres casos, alguien midió estructura con las coordenadas del instrumento. En los tres casos, el refinamiento no arregló nada. En los tres casos, la solución no fue más resolución — fue cambiar la pregunta."

*Tono:* Plano, sin énfasis dramático.

**Última línea:** "El antídoto no es más precisión. Es preguntar: ¿esto mediría algo si el objeto fuera trivial y solo el instrumento variara?"

*Silencio de 3 segundos.*

---

## Notas de producción

- **Tono general:** Forense, no dramático. Sin música épica. Sin villanos. El error no es de nadie — es de clase.
- **Música:** Ninguna en los momentos clave (medición, bug, corrección). Ambiente mínimo en transiciones.
- **Duración total:** ~12 min.
- **Voz:** Neutra, pausada. Como quien lee un parte meteorológico que no le gusta pero está correcto.
- **Referencias:** escalera π=4 (video existente en media/manim/renders/), patrón en foundation/, bug del 17 en PROTOCOLO regla 3.
- **No producir audio/video** hasta que Patricio apruebe guion completo.

## Claims cross-check

| Segmento | Claim FUNDAMENTOS | Estado |
|----------|------------------|--------|
| 1. Pre-registrar | #9 (ISW), reglas 1, 5 | REFUTADO-FIRME |
| 2. Medición | #9 (ΔT=+1.2±1.5) | REFUTADO-FIRME |
| 3. Bug | regla 3 (validación astrométrica) | PROTOCOLO |
| 4. Regla | patrón instrumento/raster | OBSERVACIÓN METODOLÓGICA |
| 5. Corregir | #9 (ΔT=+0.37±0.93, 20.7σ) | REFUTADO-FIRME |
| 6. Publicar dos veces | reglas 2, 3, 5 | PROTOCOLO |
| 7. Patrón | patrón_instrumento_raster.md | OBSERVACIÓN METODOLÓGICA |
