# 02d — Storyboard Manim: El falsador (Exp 17 → 17b)
**Revisión 2026-07-06 contra FUNDAMENTOS §I #9 y §III #6.** Tres actos. La pieza central.

**Claims fuente:** FUNDAMENTOS §I #9 (REFUTADO-FIRME, 20.7σ/67σ), PROTOCOLO reglas 2, 3, 5.
**Novelty:** el arco de 3 actos incluye el bug de coordenadas → la honestidad de corregirlo → la refutación que se sostiene. Esa es LA historia.

---

# ACTO I — La predicción (Escenas 1–4, ~30 s)

## Escena 1 — Pre-registro (8 s)

*Visual:* Terminal. Fecha UTC-5. `git commit --allow-empty -m "Exp 17: ISW stacking prediction"`. Aparece hash `[a1b2c3d]`.

*Manifiesto:* "Predecimos ΔT ≈ −19 μK sobre voids DESIVAST DR1 (rango hasta −61.7 μK). Publicamos salga como salga."

*Luz:* Azul BAO `#3B82F6`.

## Escena 2 — Los telescopios (6 s)

Planck (mapa CMB) + DESI (puntos void) convergen → stacking plot, x=0 centro void, y=T(μK). Texto: "Datos públicos. Sin cocina."

## Escena 3 — La medición (10 s)

Puntos caen en y=+1.2 μK, error ±1.5. El −19 μK está a 13σ de distancia. Banda sombreada −18.5 a −61.7. Pausa de 1.5 s.

*Texto:*
```
ΔT_medido = +1.2 ± 1.5 μK
ΔT_predicho = −19 μK
Discrepancia > 13σ
```

La predicción vira a gris `#6B7280`. La medición queda blanca.

## Escena 4 — El commit (6 s)

La terminal vuelve. El manifiesto intacto. Debajo:

```
Falsifier 1: FIRED.
Sector ISW: RETRACTED AS CALIBRATED.
Publicado salga como salga.
```

Primer clímax aparente. El azul vira a gris.

---

# ACTO II — El bug (Escenas 5–6, ~15 s)

## Escena 5 — El error (8 s)

*Visual:* El stacking plot se pixela. Las coordenadas de los voids se desalinean — un frame ecuatorial se superpone a uno galáctico. Un texto aparece:

*Texto (en rojo `#DC2626`, no acusatorio, forense):*
```
BUG: marco de coordenadas no verificado.
COORDSYS = GALACTIC asumido.
COORDSYS real = ECLIPTIC (header).
~2° de desviación sistemática.
Exp 17: INVALIDADO.
```

*La medición de +1.2 μK desaparece. El stacking plot se reemplaza por un signo de interrogación.*

## Escena 6 — La decisión (7 s)

*Visual:* Dos caminos visuales, tipo bifurcación:
- **Izquierda:** "Ocultar el bug. Nadie va a re-medir."
- **Derecha:** "Publicar el error. Corrección con astrometría V0."

*Voz/superposición:* El manifiesto original reaparece en blanco: *"Publicamos salga como salga."* Sin animación. Es la respuesta.

*Transición:* Todo se va a negro. Pausa de 2 s. Luego, el texto:

```
PROTOCOLO REGLA 3:
Validación astrométrica de extremo a extremo.
Los marcos se leen del HEADER (assert COORDSYS).
No se asumen.
(Origen: este bug.)
```

*Luz:* Neutra. Forense. No hay juicio moral, solo un commit de protocolo.

---

# ACTO III — La verificación (Escenas 7–9, ~20 s)

## Escena 7 — La corrección (8 s)

*Visual:* El stacking plot se reconstruye. Nuevos puntos caen — 1454 voids esta vez, no 752. La barra de error es más angosta.

```
Exp 17b: stacking corregido.
Astrometría V0 verificada.
1454 voids (catálogo completo).
```

Los puntos se estabilizan alrededor de +0.37 μK.

## Escena 8 — La refutación que se sostiene (8 s)

*Visual:* Dos mediciones en paralelo:

```
17 (bug): ΔT = +1.2 ± 1.5 μK  →  13σ refutación
17b (V0): ΔT = +0.37 ± 0.93 μK →  20.7σ refutación (empírica)
                                67σ refutación (H2)
```

*El −19 y el −61.7 están en gris al fondo. Ambas mediciones, con y sin bug, caen lejísimos.*

*Texto:* "La refutación NO era el bug. El bug solo hizo que la refutación fuera ligeramente menos precisa. La refutación se sostiene."

## Escena 9 — El commit definitivo (4 s)

*Visual:* Terminal. `git commit -m "Exp 17b: ISW refutación firme (20.7σ, astrometría V0)"`. El hash `[c4d5e6f]` aparece junto al viejo `[a1b2c3d]`.

*Debajo, el manifiesto original, intacto.*

*Luz:* Gris `#6B7280` permanente. Pero esta vez no parece derrota. Parece integridad.

---

# EPÍLOGO — La lección (5 s, opcional)

*Visual:* Cuatro cajas secuenciales:
1. Pre-registraste → EXIGE
2. Refutaron → PUBLICA
3. Descubriste un error → PUBLICA LA CORRECCIÓN
4. La refutación se sostiene → ESO ES CIENCIA

*Silencio.* Sin música triunfal. Sin música triste. Solo el cursor parpadeando.

---

## Notas técnicas

- **Duración total (9 escenas + epílogo):** ~70 s.
- **Colores:** Los de FUNDAMENTOS + identidad visual ⊞. El rojo `#DC2626` solo para el bug — es forense, no acusatorio.
- **Sonido:** Cursor parpadeante (tic suave) durante los commits. En Escena 5 (bug), un tono bajo sostenido que sube 2 dB y se corta. En Escena 8, silencio absoluto.
- **Hash commits:** Placeholder `[a1b2c3d]` para el pre-registro real; `[c4d5e6f]` para 17b. Sustituir por hashes reales antes de render.
- **Claims usados:** FUNDAMENTOS §I #9 (REFUTADO-FIRME), §III #6 (muerto en cementerio), PROTOCOLO reglas 3 y 5.
- **No renderizar** hasta que Patricio apruebe el arco de 3 actos.
