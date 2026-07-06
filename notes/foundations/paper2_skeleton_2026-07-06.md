# Paper 2 — Esqueleto (Fable, 2026-07-06, último bloque antes del traspaso)

**Título de trabajo:** *The falsifier that fired twice: pre-registration,
a coordinate-frame bug, and instrument-limited estimators in causal-set
phenomenology*

**Audiencia:** doble — la comunidad CST (companion del Paper 1) y la
comunidad de metodología/reproducibilidad. **Vehículo:** Zenodo,
2-4 semanas después del P1, citando su DOI + el erratum v2.1 del marco.
**Longitud:** 5-7 páginas. **Regla editorial:** cero cosmología; el
marco Render se menciona solo como el programa que motivó las
mediciones. Los protagonistas son los ERRORES y el sistema que los cazó.

## Tesis (una frase)

En fenomenología computacional, el instrumento se disfraza de objeto
sistemáticamente; el pre-registro con controles de respuesta-conocida y
fantasma convierte esa clase de error de invisible en diagnosticable —
lo demostramos con nuestros propios fracasos, timestamped en git.

## Estructura

1. **Introduction** — la crisis de replicación llegó tarde a la física
   computacional; el pre-registro es estándar en ensayos clínicos y
   LIGO (blind injections — VERIFICAR cita con Grok) pero raro en
   gravedad cuántica numérica. Este paper documenta un año de aplicarlo
   con disciplina dura, incluyendo lo que salió mal.
2. **The protocol** — las reglas relevantes con su origen: prereg
   commiteado antes de correr (git como notario); candados verificados
   ejecutando; ensambles no mejores-seeds; datos de chat en cuarentena;
   resultado publicado salga como salga. Cada regla nació de un fallo
   concreto (tabla regla→cicatriz).
3. **Act I: the falsifier fires** — Exp 17: predicción ISW
   pre-registrada del marco, medición sobre 1454 voids DESIVAST×Planck,
   "refutación" a >13σ. Celebramos la falsación. [RESULTS_17]
4. **Act II: the bug** — el diagnóstico de atrición: la fracción de
   parches válidos como test forense (0.009 posiciones erróneas vs
   1.000 correctas); el bug ecuatorial/galáctico; POR QUÉ los tests
   nulos son ciegos a errores de marco (el null se construye con el
   mismo marco roto). Confesión adicional: el candado UNBLIND que pasó
   por string-match → regla "los candados se verifican ejecutando".
   [RESULTS_17_atricion]
5. **Act III: the refutation stands** — 17b con validación astrométrica
   V0 de extremo a extremo (plano enmascarado, inyección sintética
   recuperada −10.58±0.89 sobre −10 esperado): ΔT=+0.37±0.93 µK,
   predicción excluida 20.7σ. La refutación sobrevivió a su propio bug
   — MÁS firme por haber sido re-derivada. [RESULTS_17b]
6. **The pattern** — "the raster instrument fallacy": medir estructura
   con las coordenadas del instrumento. Las 7 apariciones en tabla
   (bug 17; silencio asintótico de la adyacencia [Boguñá-Krioukov];
   escalera π=4; estimador soft del 18 [2.70 vs 2.95]; ventana
   coordenada del 25b cazada PRE-run; confound del diamante cazado
   IN-run por el fantasma; su supervivencia fiducial). El refinamiento
   no corrige el error: lo consolida con barras más chicas.
   [patron_instrumento_raster — actualizar a 7 entradas primero]
7. **The ghost-field discipline** — la contribución metodológica
   exportable: (a) control fantasma (el fit completo sobre un objeto
   TRIVIAL con el perfil del instrumento: todo lo que devuelva es
   instrumento por definición); (b) control positivo con respuesta
   analítica conocida (la pesa certificada); (c) shuffle (rompe la
   alineación, aísla la geometría); (d) la pregunta de diseño: "¿qué
   mide esto si el objeto es trivial?". Demostración: el arco completo
   del 25b (dos diseños muertos en revisión, dos corridas diagnosticadas
   en vivo, límite instrumental declarado sin rescate). [RESULTS_25b]
8. **Lessons** — (i) el ensamble es el modelo; (ii) la velocidad de
   producción asistida por IA hace MÁS necesario el gate de revisión de
   ideas en prosa antes de código (regla 15); (iii) auditoría cruzada
   entre modelos con modos de falla distintos caza lo que uno solo no
   ve (tabla: qué cazó cada auditor este año); (iv) publicar los
   negativos convierte los fracasos en infraestructura.
9. **Coda honesta** — qué NO afirma este paper: el método no garantiza
   verdad, garantiza diagnosticabilidad; nuestro marcador contra el
   universo real sigue siendo una refutación, un empate y una
   coincidencia etiquetada.

## Figuras

F1: línea de tiempo del arco 17→bug→17b con hashes de git y fechas
(la evidencia de que el orden es real). F2: el diagrama del control
fantasma (objeto trivial + perfil del instrumento → lo que salga es
instrumento). F3 (opcional): tabla-figura de las 7 apariciones del
patrón.

## Para SuperGrok (verificar TODO antes de citar)

- LIGO blind/hardware injections: la referencia canónica del método.
- Pre-registration en física de partículas (blind analyses en LHC/
  flavor physics: referencia de review).
- Lakatos (rescates exigen predicción nueva) — edición citable.
- Crisis de replicación: Nosek/OSF, la referencia estándar.
- ¿Existe algún paper previo de "pre-registration in numerical quantum
  gravity"? (anti-scoop del método).

## Qué falta tras este esqueleto

1. Actualizar patron_instrumento_raster a 7 entradas (10 min).
2. Prosa EN (5-7 pp) — puede escribirla cualquier miembro del equipo
   leyendo: este esqueleto + RESULTS_17/17_atricion/17b/25b + PROTOCOLO.
3. F1-F2 (Codex, desde el git log y un esquema).
4. Referencias verificadas (SuperGrok, lista arriba).
5. DOIs del P1 y del erratum v2.1 para las citas cruzadas.
6. Decisiones del autor: título final, y si la tabla de auditorías
   cruzadas nombra a los modelos (recomendación: sí — la transparencia
   ES el tema del paper).
