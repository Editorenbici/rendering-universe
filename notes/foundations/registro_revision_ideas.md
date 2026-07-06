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
|   |       |      |       |         |                                      |          |
