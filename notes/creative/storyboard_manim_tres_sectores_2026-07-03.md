# Storyboard Manim — Tres sectores de Render Universe

Propósito: storyboard conceptual para animaciones Manim (no video, no Blender). Cada sector es una escena autónoma de ~30–60 s que cuenta su historia sin narración inflada. Los sectores se pueden animar en orden o por separado.

Convenciones visuales:
- Canvas Minkowski fijo (cuadrícula 2D + línea temporal vertical) en todas las escenas.
- ℛ(t) representado como resolución de píxeles en el borde del canvas.
- Colores: BAO=azul (#4FC3F7), ISW=rojo/gris (#E53935 / #BDBDBD), DM=ámbar (#FFB300).
- Tipografía: LaTeX para ecuaciones, sans-serif para etiquetas.

---

## Escena 1 — BAO (sector vivo, ~45 s)

### Concepto
Mostrar que el canvas es fijo y ℛ crece, y que el fit BAO reproduce datos reales.

### Plano 1.1 — Canvas fijo (5 s)
- Cuadrícula Minkowski 2D estática.
- Texto: "Canvas size = 1 (fixed)".
- Peak ℛ(t) en la esquina superior derecha creciendo: ℛ₀ → ℛ(t₁) → ℛ(t₂).
- Píxeles en el borde izquierdo se subdividen (resolución aumentando).

### Plano 1.2 — ℛ ∝ t^β (10 s)
- Ejes log-log: t vs ℛ.
- Línea recta β = 0.055 pasando por puntos rojos (DESI DR2, 13 puntos).
- Fórmula: ℛ(t) = ℛ₀ (t/t₀)^β.
- Banda de error ±0.045 (intervalo de confianza 68%).
- Transición suave a:

### Plano 1.3 — Comparación con ΛCDM (10 s)
- Dos paneles: izquierdo ℛ∝t^β, derecho ΛCDM.
- Misma data DESI DR2 superpuesta.
- Leyenda: "Δχ² ≈ 1 — ambos modelos son consistentes".
- Barra de compatibilidad. No hay ganador claro.

### Plano 1.4 — Takeaway (5 s)
- "BAO sector survives: ℛ(t) fit is viable."
- Canvas fijo, no hay expansión.
- No hay inflación ni constante cosmológica.

---

## Escena 2 — ISW (sector refutado, ~40 s)

### Concepto
Mostrar una predicción pre-registrada que fue falsificada. La lección científica: publicar el negativo.

### Plano 2.1 — Predicción (8 s)
- Void profundo en el canvas: zona de ℛ bajo (píxeles grandes).
- Gradiente ∇ℛ apuntando hacia afuera del void.
- Flecha "ΔT ≈ −19 μK (predicted)".
- Ecuación: ΔT/T₀ ∝ ∫ (dΦ_N/dℛ) dℛ.
- Sello: "Pre-registered (Exp 17)".

### Plano 2.2 — Medición DESIVAST + Planck (10 s)
- Stack de voids reales (catálogo DESIVAST DR1).
- Mapa de temperatura Planck superpuesto.
- Medición: ΔT = +1.2 ± 1.5 μK.
- La predicción está fuera de la barra de error por ~13σ.
- Animación: la flecha de predicción se encoge hasta caer dentro del error.
- Texto en rojo: "FALSO — falsifier 1 fired".

### Plano 2.3 — Lección (5 s)
- "ISW sector retracted as calibrated."
- "Publishing negative results is the discipline."
- Transición a blanco y negro (gris).

---

## Escena 3 — DM / SPARC (sector débil/abierto, ~50 s)

### Concepto
Mostrar que hay un indicio en SPARC pero sin mecanismo. Sector abierto, no cerrado.

### Plano 3.1 — Curvas de rotación SPARC (10 s)
- Galaxia espiral típica.
- Panel izquierdo: curva observada (puntos), fit NFW (línea discontinua), fit cored (línea sólida).
- Panel derecho: 8 galaxias piloto, 7/8 muestran mejor ajuste cored.
- "Two-parameter cored profile fits 7/8 galaxies."
- Letra pequeña: "Cored profiles outperform NFW independently of theory."

### Plano 3.2 — Sin mecanismo (8 s)
- Signo de interrogación sobre la galaxia.
- "No derivation from Postulate 6 yet."
- "DM aliasing: Bullet Cluster unsolved, SPARC limited to 8 galaxies."
- El signo de interrogación se agranda.

### Plano 3.3 — ¿Qué sigue? (7 s)
- Tres cajas en paralelo:
  1. "Bullet Cluster" → "pendiente"
  2. "SPARC full catalog" → "pendiente"
  3. "MOND-like scaling" → "pendiente"
- "Open: no unique mechanism. Sector classified as weak."
- Ámbar (no rojo, no azul).

---

## Resumen de cierre (opcional, 15 s)

Si se animan juntos:

- Tres paneles en pantalla: BAO (azul, "vivo"), ISW (gris, "refutado"), DM (ámbar, "débil").
- Transición a blanco.
- "Render Universe v2.0: one mechanism, three outcomes."
- "Effective framework, not theory."

---

## Notas técnicas

- Cada escena debe ser un script .py independiente que herede de Scene.
- No mezclar con Blender — Manim Cairo o OpenGL según disponibilidad del host.
- Tiempos estimados: 2–3 min total para los tres sectores + cierre.
- Sin voz en off ni música — texto + animación.
- Colores planos, sin gradientes complejos.
- Los números (valores de fit) deben tomarse de outputs/ corrientes, no inventados.
