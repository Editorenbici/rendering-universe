# 06 — Storyboard: "La gravedad convierte tiempo en espacio"
**Prioridad: después del falsador. NO RENDERIZAR hasta veredicto del Exp 25b.**

**Concepto:** El teorema de partición — cerca de masa, el diamante causal se vuelve más ancho y menos profundo. El volumen total √−g = ℛ⁺² se conserva: −1 al tiempo, +3 al espacio, +2 en total.

**Claims fuente:** FUNDAMENTOS §I #12 (TEOREMA de partición), §I #11 (ENMIENDA ADOPTADA, métrica disforme).

**Etiqueta condicional:**
- Si 25b sale S1': `"MEDIDO (Exp 25b)"` + números de outputs/exp25b_results.json
- Si 25b sale F1'/F2': preguntar antes de publicar

---

## Escena única (~20 s), partición en 3 fases

---

### Fase 1 — Dos relojes (0–5 s)

*Visual:* Dos diamantes causales idénticos, lado a lado, en un canvas Minkowski vacío. Ambos se llenan de puntos al mismo ritmo (sprinkling uniforme). Un contador numérico debajo de cada uno muestra el mismo número.

*Etiqueta:* "Dos relojes. Sin gravedad. Tictaquean igual."

*Sonido:* Tic-tic-tic sincronizado, sutil.

---

### Fase 2 — Aparece la masa (5–15 s)

*Visual:* Un círculo gris (la masa) aparece bajo el diamante derecho. El diamante derecho se **deforma en cámara lenta**:
- Se comprime verticalmente (menos profundidad → tiempo más lento).
- Se expande horizontalmente (más anchura → más espacio).
- El contador de puntos sube: el número total de eventos crece ×ℛ².

*Paneo/lupa:* La cámara hace un zoom suave a la derecha para que se vea la deformación.

*Tres números aparecen secuencialmente al costado:*
```
tiempo: −1
espacio: +3
total:   +2  (×ℛ²)
```

*Etiqueta condicional (esquina inferior derecha):* 
- Si S1': `"MEDIDO (Exp 25b)"` + p_h/p_w de outputs/exp25b_results.json
- Si F1'/F2': `"PREDICCIÓN — pendiente de verificación"`

---

### Fase 3 — El cierre (15–20 s)

*Visual:* Los dos diamantes se funden en una sola imagen. El de la izquierda (plano) se desvanece. El de la derecha (con masa) queda, con sus −1 y +3.

*Texto, línea por línea:*
```
"La gravedad no atrae.
Reparte:
−1 al tiempo,
+3 al espacio,
+2 en total."
```

*Pausa de 2 segundos.*

*Última línea (física estándar, ancla pública):*
```
"Por eso tu cabeza envejece más rápido que tus pies.
(GPS lo corrige a diario.)"
```

*Fundido a negro.*

---

## Notas técnicas

- **Duración:** ~20 s.
- **Colores:** Paleta identidad visual 01 (`#0F0F12` canvas, `#00FFC8` cursor/acento, `#6B7280` para los números, `#F8F9FA` para el texto de cierre).
- **Masa:** Círculo gris `#6B7280` con opacidad 0.6. Sin textura — es una masa genérica.
- **Deformación del diamante:** Animación suave de 5 s. El diamante original tiene altura~T y anchura~T. Con masa, altura→T·e⁻ψ ≈ T·(1−ψ), anchura→T·e⁺ψ ≈ T·(1+ψ). El área del diamante (en corte 2D) se conserva aproximadamente: (T·e⁻ψ)×(T·e⁺ψ) = T².
- **Puntos:** ~100 puntos en cada diamante, rojos `#00FFC8` con opacidad 0.5. No hace falta contarlos exactamente — la impresión visual de "más puntos" en el diamante deformado es suficiente.
- **Solo ℛ como símbolo público:** `×ℛ²` es la única fórmula. Sin u_μ, sin κ₄, sin 𝔉.
- **Sin renderizar** hasta veredicto del Exp 25b (Fable avisa). Después del veredicto y con aprobación de Patricio.

## Anti-slop check
1. ¿Funciona para otro proyecto? → No. El teorema de partición (−1,+3)→+2 es específico de Render.
2. ¿Nombra mecanismos? → Sí: diamante causal, deformación, sprinkling.
3. ¿Algo sorprendente? → "La gravedad no atrae. Reparte." — una reformulación que contradice la intuición pero es matemática.
4. ¿Experiencia sensorial? → Dos relojes sincronizados, uno se deforma, números aparecen.
5. ¿Da vergüenza? → No. El ancla GPS es física estándar.
