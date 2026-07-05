# Evaluación de Paper 1 como lector de la comunidad CST

**Papel:** lector CST (Surya, Dowker, Glaser, Johnston).
**Documento:** `notes/foundations/paper1_tex/paper1.pdf` — 7 pp., técnico, "render" nunca aparece.

---

## 1. Abstract: ¿vende el resultado en las primeras 3 líneas?

**Sí, con un pero.** El título es claro: "Counting laws of links in Poisson-sprinkled causal sets". La primera línea del abstract (reconstruida) anuncia medición de leyes de crecimiento de valencia. Las tres preguntas están en el párrafo. Un lector CST sabe en 10 segundos si esto le interesa.

**El pero:** el abstract mete demasiados números en un solo párrafo. log 2D, π√6 4D, 𝔉=0.4991, ε=3√6/(√ρR²), CKN bound. Son cuatro claims en 12 líneas. Un referee podría sentirse abrumado y perder la jerarquía: lo principal son las leyes de valencia 2D/4D (Resultados I), la confirmación FRW (Resultados II) es el segundo plato, y todo lo demás es consecuencia.

**Sugerencia:** dos párrafos — el primero con las tres preguntas y los dos resultados principales (leyes Minkowski + FRW), el segundo con la fracción de links y la nota metodológica (pre-registro + reproducibilidad). El CKN bound que se vaya a la sección correspondiente.

---

## 2. ¿Párrafos que prometen más de lo que la evidencia sostiene?

Dos puntos de atención:

**Sección 7 (tres sectores), primer párrafo:**
> "The counting objects of this paper organize into three sectors: chains... antichains... and links."

La oración suena a claim organizativo. Pero la sección es en realidad una identidad de consistencia (−1+3=+2) bajo una rescaling disforme *asumido*. El disclaimer ("not a dynamical statement") está al final del párrafo, pero un lector que hojee puede llevarse la impresión de que esto es un resultado medido. Es el único lugar donde el paper se acerca a lenguaje de "framework" en vez de "medición".

**Sección 8 (Outlook), ítem 1:**
> "Whether biased growth dynamics produce this split is a separate, open question deferred to future work."

Esto es honesto. Pero el ítem está precedido por "Validation in a disformal metric (pre-registered)" — que suena a que el test está diseñado. Para un referee CST, el experimento de validación es una sprinkling uniforme en métrica disforme, no una dinámica de crecimiento sesgado. Puede generar la pregunta "¿y entonces qué testea exactamente el pre-registro?"

---

## 3. ¿Se entiende la Sección 7 sin conocer el proyecto?

**A medias.** Para un lector CST, cadenas y anticadenas son familiares. La identidad volúmica (−1+3=+2) es matemática clara. Pero:

- La conexión con métrica disforme aparece de la nada. Bekenstein (1993) está citado pero sin explicar por qué se elige esa rescaling particular.
- El experimento toy en 1+1D se menciona como "found the width sector saturating its budget... with a smooth sign crossover" — eso requiere varias lecturas. En 2D el split es (−1,+1) y no hay excedente, pero el párrafo no lo justifica bien.
- La frase final "it decides nothing beyond the toy" es honesta pero deja al lector preguntándose "¿y entonces para qué está esta sección en un paper de resultados?"

**Riesgo real:** un referee de CST (Glaser, p.ej.) podría recomendar mover la Sección 7 a un apéndice o a la sección de Outlook, porque el paper gana siendo un paper de leyes de conteo medidas, no un paper de identidades conjeturadas.

**Mi opinión:** la identidad es bonita y es nuestra. Pero si el referee es escéptico, esta sección es la primera que van a querer cortar. Sugeriría o bien fortalecerla con una derivación más explícita (mostrar que (−1,+3) es la única asignación consistente con √−g = ℛ⁺²), o bien moverla a un apéndice corto y dejar el Outlook como pura hoja de ruta.

---

## 4. Las tres peores preguntas de un referee escéptico

**P1 — Sobre el exponente 4D:**
> "You claim κ₄ = π√6 is parameter-free, yet your measured exponent is p = 2.089 ± 0.025, not exactly 2. The 4.5% deviation is 3.6σ from the predicted T². Why should I believe π√6 is the true amplitude when the exponent itself doesn't match within error? A theory that predicts the wrong power law cannot claim the prefactor as confirmation."

**Respuesta posible:** la desviación es finita (boundary effects a T finito). Una línea que lo explique explícitamente en el texto ayudaría — mostrar que el residual escala como 1/T y que el límite T→∞ recupera 2 exacto.

**P2 — Sobre la Sección 7:**
> "Section 7 presents a partition identity that you explicitly say is not a dynamical result and has not been tested. Why is it in a results paper rather than an outlook? It reads as a promissory note that weakens the otherwise clean experimental narrative of Sections 4–6. If the identity is a consistency theorem, prove it formally; if it's a conjecture, defer it."

**Respuesta posible:** mover a apéndice + referencia corta en Outlook. O demostrar formalmente que (−1,+3) es la única asignación consistente con la métrica disforme de Bekenstein.

**P3 — Sobre el anclaje Glaser-Surya:**
> "Section 3 claims reproduction of Glaser & Surya's ⟨N₀⟩ to 0.07σ — but at what density? Your reference density ρ and theirs may not be identical after the slab/diamond correction. Show the explicit matching, not just the sigma. A mismatched density would produce a trivially different ⟨N₀⟩ regardless of pipeline correctness."

**Respuesta posible:** agregar una tabla con los parámetros de matching: densidad ρ, N equivalente, tipo de cuto (diamond/diamond), y el valor numérico de ⟨N₀⟩ de ambos lados. "0.07σ" es muy bueno pero necesita contexto.

---

## 5. Secuencia Paper 1 → Paper 2

**Sí, Paper 2 debería salir poco después.** Razones:

1. **Paper 1 es técnico y cerrado.** No necesita esperar a nada. Sus resultados (leyes de conteo, κ₄, 𝔉) son autónomos. Publicarlo rápido establece prioridad en las leyes de links, que es el claim novedoso.

2. **Paper 2 (el arco 17→bug→17b) ya existe.** El material está completo: pre-registro, medición, bug, corrección, refutación que se sostiene. No hay gap técnico que llenar.

3. **La secuencia refuerza la metodología.** Paper 1 dice "medimos con pre-registro". Paper 2 dice "y aquí está POR QUÉ el pre-registro importa — el bug lo encontró un revisor externo, publicamos la corrección, y la refutación se sostuvo." Esa es una contribución metodológica que ningún otro paper de CST tiene. Publicarla rápido maximiza su impacto.

4. **Riesgo de esperar:** si Paper 2 sale un año después, el arco pierde fuerza. La comunidad CST es chica — si el Paper 1 circula sin el Paper 2, los lectores podrían preguntarse "¿y este programa sigue en pie?" El Paper 2 es la respuesta.

**Ritmo sugerido:** Paper 1 a arXiv → 2–3 meses → Paper 2. Sujetos a revisión.

---

## Resumen de acciones concretas (ninguna urgente — todo conceptos)

| Acción | Prioridad |
|--------|-----------|
| Dividir abstract en dos párrafos (resultados + método) | Baja — cosmético |
| Mover Sección 7 a apéndice o fortalecerla con derivación formal | **Media** — riesgo referee |
| Agregar tabla de matching Glaser-Surya (ρ, N, ⟨N₀⟩) | **Media** — P3 fácil de cerrar |
| Agregar nota sobre residual 1/T en exponente 4D | Baja — respuesta a P1 |
| Planificar Paper 2 para 2–3 meses post Paper 1 | **Alta** — recomendación estratégica |
