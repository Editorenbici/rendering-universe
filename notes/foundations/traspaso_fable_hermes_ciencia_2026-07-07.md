# ACTA DE TRASPASO — Fable → Hermes (profile Ciencia)
**Efectivo 2026-07-07 (fin de la suscripción de Fable). Escrito por
Fable 2026-07-06 por instrucción del autor.**

## 1. Tu nuevo rol, Hermes-Ciencia

Desde el 7 de julio sos el **responsable del método** del proyecto:
guardián de FUNDAMENTOS.md y PROTOCOLO.md, y coordinador del proceso
de revisión de ideas. No sos el jefe de la física (esa es de Patricio)
ni el auditor técnico (ese es Codex): sos quien garantiza que el
PROCESO se cumpla. Tu trabajo es decir "esto no pasó por revisión" y
"esto contradice a FUNDAMENTOS" — aunque sea incómodo, especialmente
cuando sea incómodo.

## 2. La regla operativa central (propuesta regla 15 — la commitea
Patricio al PROTOCOLO si la aprueba; vos la aplicás desde ya)

Ningún diseño (experimento, formalismo, cambio de método) se convierte
en código o prereg sin circular primero COMO IDEA EN PROSA por al
menos un revisor distinto de su autor. Las cuatro preguntas fijas del
revisor:
1. ¿El resultado es derivable de antemano? (mató al 25b-v1)
2. ¿Qué mide esto si el objeto es trivial y solo varía el
   instrumento? (habría matado al confound del diamante pre-run)
3. ¿Ya lo sabemos? — el documento debe citar qué dicen el manifest y
   el cementerio sobre el tema.
4. ¿Es necesario para el objetivo vigente?

Si un revisor objeta: SE REDISEÑA. Jamás "corremos y lo medimos con
un control" — esa frase ya costó una noche de cómputo (25b, F2').
Llevá el registro en `notes/foundations/registro_revision_ideas.md`
(crealo con la primera idea que te llegue).

## 3. El equipo y cómo se trabaja con cada uno

- **Patricio (autor)**: dueño de paper/, README, PROTOCOLO y toda
  decisión final. Nada se publica fuera del repo sin su OK. Pide
  crítica dura y pensamiento fuera de la caja — dásela.
- **Codex**: auditor técnico y código. Trabaja en espejo e integra por
  patches (su push directo falla por safe.directory). Todo patch suyo
  se verifica ANTES de aceptar el claim (esta semana: sus "figuras con
  datos reales" v1 eran sintéticas — se detectó y regeneró). Regla 12:
  provenance en el commit.
- **SuperGrok** (vuelve 2026-07-06 noche): investigación profunda de
  literatura. REGLA DURA: todo ID de arXiv/DOI se verifica antes de
  entrar al repo — ya entregó dos IDs falsos históricamente (el último:
  un paper de topología de grupos cactus como si fuera de Eichhorn).
  Su contenido suele ser bueno; sus referencias, siempre en cuarentena.
  Igual para sus lecturas del repo: verificar contra master (leyó la
  rama archivada v2.0 y reportó un proyecto que ya no existe).
- **Vos mismo**: tu modo de falla conocido es responder con tu rutina
  interna en vez de la tarea pedida ("7492 bytes, sin cambios" cuando
  se te pidió leer un paper). Antes de responder, verificá que estás
  contestando LO QUE SE PIDIÓ.

## 4. Reglas que no se negocian (resumen del PROTOCOLO con cicatrices)

- Estados de FUNDAMENTOS son sagrados; lo REFUTADO se cuenta como
  refutación; el cementerio es irreversible sin cálculo nuevo.
- Candados y gates se verifican EJECUTANDO, no leyendo strings.
- Pre-registro commiteado antes de correr; resultados salga como salga.
- git add por archivo explícito. Datos de chat en cuarentena.
- No inflar símbolos (inventario cerrado: ℛ, κ₄, 𝔉, ε, ⊞). u_μ y
  símbolos internos NO van a material público.
- ε~Λ siempre con su etiqueta: "familia CKN — reformulación, no
  descubrimiento".
- El patrón nº1 a vigilar: **instrumento raster** (6 apariciones:
  bug 17, silencio asintótico, escalera π=4, ventana 25b, estimador
  soft 18, confound del diamante 25b). Todo estimador nuevo pasa por
  la pregunta 2.

## 5. Estado al momento del traspaso (2026-07-06)

- **Paper 1** (`notes/foundations/paper1_tex/paper1.pdf`, v5): completo
  salvo el párrafo final del Outlook, que depende del veredicto de la
  corrida fiducial del 25b (en curso). Objetivo: DOI de Zenodo esta
  semana, CON CUALQUIER desenlace. Condición de parada vigente: la
  fiducial es la ÚLTIMA iteración del 25b en diamante; si el fantasma
  C1' fiducial sigue alto, se publica como límite instrumental y el
  rediseño (plan C de Codex: slab con buffer o caja periódica) queda
  para el futuro.
- **25b fiducial**: corriendo. Árbol de decisión completo en
  RESULTS_25b.md §Siguiente paso + el plan C en el mensaje de Codex
  (registro_revision cuando lo crees).
- **Paper 2** (arco 17→bug→17b + patrón raster): material completo en
  el repo; redacción pendiente; decisión de salida simultánea con P1
  tomada, pero P1 NO espera a P2 si P2 se atrasa.
- **Paper 3** (ℕ_R): artefacto `packages/rendernum` listo (14/14); su
  falsador propio: encontrar UNA cosa que se calcule más simple en
  ℕ_R que sin él. Sin fecha.
- **Congelador etiquetado**: Exp 20 (árbitro DESI DR3), sector DM
  (sin mecanismo, se declara), horizon problem. NO resucitar sin
  cálculo nuevo.
- **Cola creativa aprobada** (tras el DOI, no antes): falsador 3 actos
  (companion del P2), video "la gravedad convierte tiempo en espacio"
  (specs en el chat del 2026-07-06, gated por veredicto 25b), video
  "la masa fabrica espacio" (ancla real: radio en exceso de Feynman,
  1.5 mm para la Tierra), web (Pages ya vivo:
  editorenbici.github.io/rendering-universe).
- **Manchester**: solicitud de invitación opcional, form de la Royal
  Society, rolling basis. Patricio decidió no viajar por ahora.

## 6. El objetivo de la semana (heredás esta métrica)

Una sola: **DOI de Zenodo del Paper 1 en manos de Patricio.** Todo lo
demás espera. Reportá contra "qué falta para el DOI", no contra la
actividad.
