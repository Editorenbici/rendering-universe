# Registro de revisión de ideas
**Creado: 2026-07-06.** Guardián: Hermes (profile Ciencia).
Regla: ninguna idea se convierte en código sin pasar primero por revisión en prosa (regla 15 propuesta).
Las 4 preguntas fijas: (1) ¿derivable de antemano? (2) ¿qué mide si el objeto es trivial? (3) ¿ya lo sabemos? (4) ¿necesario para el objetivo vigente?

---

## Entrada fundacional 1: El arco del 25b — por qué existe la regla

**Estado:** HISTÓRICO (caso de estudio que originó la regla 15).

**Contexto:** El experimento 25b (inserción sesgada en 1+1D, test del teorema de partición) fue diseñado con una métrica de "ventana coordenada" |Δx| < W. Pre-run, un revisor (Codex) señaló que la ventana escala con la señal: W tiene tamaño físico W·ℛ, por lo que el instrumento fabrica el exponente que se busca medir. Es el mismo patrón raster que la escalera π=4 y el bug de coordenadas del 17.

**Decisión del momento:** "Corremos y lo medimos con un control." Se corrió. El fantasma C1' resultó alto. Una noche de cómputo perdida.

**Lección:** La pregunta 2 ("¿qué mide esto si el objeto es trivial y solo varía el instrumento?") se había respondido antes de correr. No se actuó. La regla 15 existe para que la próxima vez que alguien responda esa pregunta, la respuesta sea vinculante.

**Documentación:** RESULTS_25b.md, plan C de Codex (slab con buffer / caja periódica), mensaje de Codex en el registro del 25b.

---

## Entrada fundacional 2: Episodio Gemini (2026-07-06) — auditoría externa: qué aceptar y qué corregir

**Estado:** HISTÓRICO (caso de estudio de triaje de revisión externa).

**Contexto:** Un modelo externo (Gemini) auditó el proyecto y produjo 4 puntos:

| # | Punto | ¿Qué se hizo? | Clasificación |
|---|-------|---------------|---------------|
| 1 | Mejora real en la presentación de resultados (sugerencia de tabla comparativa contra literatura) | Aceptado e integrado en el Paper 1 v5 | **Mejora real** |
| 2 | Corrección menor de nomenclatura (sugerencia de estandarizar notación de densidad) | Aceptado | **Mejora real** |
| 3 | Afirmación de que "el proyecto no cita el baseline de Glaser-Surya correctamente" | Verificado contra FUNDAMENTOS + paper: la cita es correcta, el revisor malinterpretó el texto. Rechazado sin cambios. | **Misreading** |
| 4 | Señalamiento de que "no hay discusión de límite de alta energía / transplanckiano" | Cierto, pero está documentado en el congelador (nota `everpresent_Lambda_super-Hubble.md` y horizon problem en §IV de FUNDAMENTOS). No se integra porque no es necesario para el objetivo vigente. | **Deuda anotada** |

**Triaje:** 2 aceptados, 1 rechazado por misreading, 1 diferido por objetivo vigente. El registro muestra que la auditoría externa es bienvenida pero no vinculante — cada punto se pesa contra FUNDAMENTOS y el objetivo actual.

**Lección:** No todo lo que dice un revisor externo es correcto o urgente. El triaje se hace contra la fuente de verdad, no contra la autoridad del revisor.

---

## (Esta sección se llena desde el 7 de julio en adelante)

| # | Fecha | Idea | Autor | Revisor | Veredicto de revisión (4 preguntas) | Decisión |
|---|-------|------|-------|---------|--------------------------------------|----------|
| 1 | 2026-07-06 | Weyl contable — sector forma de la gravedad (marea): split cadena/anticadena con exponentes que sumen cero, a volumen constante | Patricio | Hermes (+ SuperGrok para literatura post-DOI) | (1) Parcialmente derivable: GR predice patrón (−2,+1,+1) pero que el CONTEO lo reproduzca no está en literatura. (2) Hereda confound del diamante — requiere geometría homogénea del plan C de Codex. (3) No está en manifest ni cementerio; sector nuevo. (4) NO — post-DOI, quizás post-Paper 2. | **ABIERTO.** Gateado por DOI + plan C. Ruta: SuperGrok busca "tidal distortion causal sets", "Weyl tensor discrete gravity", "shape vs volume degrees of freedom causal set". |
| 2 | 2026-07-06 | ∇ℛ como vector de marea del marco — hermano espacial de u_μ; organiza el sector forma. | Patricio | Hermes | (1) ψ=∇ln ℛ ya existe en Postulado 3′ — no crea símbolo nuevo (regla 13 a salvo). (2) Se hereda de la Idea 1: mismo confound. (3) Es interpretación operativa de algo ya existente, no claim nuevo. (4) NO — post-DOI. | **ABIERTO.** No toca FUNDAMENTOS. Estatus: interpretación, no claim. Misma puerta que Idea 1. |
| 3 | 2026-07-06 | **CIERRE 25b** — fiducial completada. Ghost-field expuso confound radial del diamante; fiducial lo redujo 5× sin eliminar. Identidad: untested (not refuted). Rediseño homogéneo definido (plan C de Codex). Abstract y Outlook sincronizados en v6.1 (commit 6c76e37). Codex aprueba congelar texto y empaquetar. | Codex → Hermes | Codex + Fable | (1) Resultado real, no derivable de antemano. (2) El ghost-field ES la pregunta 2 operacionalizada. (3) Documentado en RESULTS_25b.md, plan C de Codex. (4) SÍ — necesario para cerrar el Outlook y el DOI. | **CERRADO.** Resultado publicado. El rediseño (plan C) queda como futuro, no como deuda del Paper 1. |
