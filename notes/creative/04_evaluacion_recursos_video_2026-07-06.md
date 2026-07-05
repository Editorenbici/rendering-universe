# Evaluación de recursos para video (Tarea 3)
**2026-07-06.** Tres materiales nuevos para conceptos visuales. Evaluar y proponer, NO producir aún.

---

## 1. La paradoja de la escalera: π=4 en píxeles

### Qué es
Medís un círculo en una cuadrícula de píxeles contando adyacencia ortogonal → el perímetro da 4 diámetros, no π. Ese es el mismo problema de la distancia espacial en causal sets: medir por adyacencia da la métrica incorrecta. La solución: medir con estructura (overlaps, no adyacencia).

### Evaluación
- **Rigor científico:** 100%. Es un resultado conocido (discrete geometry) que se conecta sin forzar con la métrica de causal sets.
- **Animabilidad:** Alta. Una cuadrícula pixelada, un círculo que se dibuja, π=4 aparece, luego se refina y π emerge. Muy visual.
- **Riesgo:** Que parezca un chiste de "π=4" sin contexto. Necesita la etiqueta "este es el mismo problema de la distancia en causal sets" desde el principio.
- **Claim cross-check:** No toca ningún claim de FUNDAMENTOS. Es puramente pedagógico/visual.

### Propuesta
15 s. Una escena:
- Cuadrícula de píxeles. Círculo dibujado. Perímetro contado ortogonalmente = 4 diámetros.
- "π = 4? No. π = 4 solo si medís por adyacencia."
- Transición: el círculo se refina (más píxeles), el perímetro converge a π.
- "Medir con estructura (overlaps) da la métrica correcta. Lo mismo pasa en causal sets."

**Prioridad:** Alta. Perfecto para redes (30-60 s). No requiere claims del proyecto.

---

## 2. El girasol como apertura

### Qué es
Un girasol: la planta guarda el vector (ángulo áureo ≈ 137.5°) y renderiza raster (cada semilla, un evento). El marco entero en una imagen de la naturaleza: un vector (la regla de crecimiento) que genera un raster (las semillas). Análogo a: la métrica disforme (vector u_μ derivado de h) renderiza eventos (links, cadenas) en el canvas.

### Evaluación
- **Rigor científico:** Fuerte como analogía, débil como claim. No es una derivación. Usar solo como apertura/gancho visual para divulgación.
- **Animabilidad:** Hermosa. Time-lapse de girasol creciendo, las semillas apareciendo en espiral. Transición → el mismo patrón como causal set (puntos en cono de luz).
- **Riesgo:** Sobrevender la analogía. "El universo es un girasol" es New Age. Debe tener guardarraíl explícito: "es una analogía estructural, no un mecanismo".
- **Claim cross-check:** Ninguno. Es metáfora visual para la relación vector→raster.

### Propuesta
20 s. Una escena (apertura del NotebookLM):
- Girasol creciendo en time-lapse, semillas apareciendo en espiral áurea.
- "Cada semilla es un evento. La planta guarda un solo vector: el ángulo áureo. De ahí renderiza el raster completo."
- Transición: el girasol se disuelve en un causal set (puntos en cono de luz).
- "Render Universe: un vector (u_μ de h), un raster (ℛ), un canvas (⊞)."

**Prioridad:** Media. Usar como apertura del NotebookLM (segmento 2), no como pieza independiente.

---

## 3. Crossover del Exp 25: p_h(b) cruzando cero

### Qué es
La curva de inserción sesgada p_h(b) cruza cero en algún punto. "El sesgo convierte tiempo en espacio" — cuando el parámetro de sesgo cruza, la firma de la métrica cambia.

### Evaluación
- **Rigor científico:** Depende del estado del Exp 25. Es HIPÓTESIS / GATED en FUNDAMENTOS. No se puede presentar como resultado.
- **Animabilidad:** Media. Una curva que cruza cero es visualmente plana. Necesita una metáfora más fuerte: quizás una balanza que se inclina, o dos ejes (tiempo vs espacio) que intercambian etiquetas.
- **Riesgo:** Alto. Si el Exp 25 no se completa o se refuta, este material queda inservible. Además, el crossover es un punto matemático, no un resultado cosmológico.
- **Claim cross-check:** FUNDAMENTOS §IV — HIPÓTESIS / GATED. No se puede presentar como "descubrimiento".

### Propuesta
15 s. Solo si el Exp 25 pasa auditoría:
- Dos ejes: uno vertical (tiempo), uno horizontal (espacio). Una curva los cruza.
- En un lado: "sesgo → tiempo domina". En el otro: "sesgo → espacio domina".
- "El sesgo convierte tiempo en espacio. El crossover es donde la métrica cambia de firma."
- Texto al final: "HIPÓTESIS — pendiente de verificación."

**Prioridad:** Baja. Gated por el Exp 25. No producir hasta que el experimento esté completo.

---

## Resumen de prioridades (alineado con Fable)

| Recurso | Prioridad | Para qué | Claims involucrados | Estado |
|---------|-----------|----------|---------------------|--------|
| NotebookLM 3 actos | 1 | LA pieza | #9 (REFUTADO-FIRME), reglas 3,5 | Storyboard listo en creative/ |
| Escalera (π=4) | 2 | Short redes | Ninguno | Conceptual, listo para animar |
| Girasol | 3 | Apertura NotebookLM | Ninguno | Analógica, sin render |
| Crossover Exp 25 | 4 | Futuro | §IV (HIPÓTESIS/GATED) | Gated por Exp 25 |
| Manim tres sectores | 5 | Post-papers | §I completo | Storyboard previo en creative/ |

**Guardarraíles activos:**
- ε~Λ siempre con: "misma familia que CKN — reformulación, no descubrimiento"
- REFUTADO se cuenta como refutación, no como éxito disfrazado
- Cero claims nuevos
- Nada en paper/ o code/
