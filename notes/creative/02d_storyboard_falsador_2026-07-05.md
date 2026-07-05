# 02d — Storyboard Manim: El falsador (Exp 17)
**Concepto para aprobación.** Prioridad 2d del brief de Fable. La pieza central.

**Claims fuente:** #12 (REFUTADO) y #20 (VIVO — política de no rescate post-hoc) de `notes/claims_table_2026-07-03.md`.

**Arco emocional:** El clímax no es la predicción audaz, sino publicar el negativo sin tocar una coma. La honestidad es el final, no la victoria.

---

## Escena 1 — Pre-registro (10 s)

*Visual:* Fecha en UTC-5 marcando en una terminal de pantalla negra, tipo `git commit --allow-empty -m "Exp 17 pre-reg: ISW stacking prediction"`. El hash del commit aparece. El texto se eleva y se convierte en la primera línea de un manifiesto:

*Manifiesto:* "Predecimos que el stacking ISW sobre voids DESIVAST DR1 dará ΔT ≈ −19 μK (rango permitido hasta −61.7 μK). Este es un test falsable. Publicaremos el resultado salga como salga."

*Luz:* El texto está en azul BAO (`#3B82F6`). No titila. Es un manifiesto, no un rezo.

## Escena 2 — Apuntar telescopios (8 s)

*Visual:* Dos paneles que se deslizan desde los bordes.
- **Panel izquierdo:** Planck (mapa de temperatura CMB, colores falsos fríos).
- **Panel derecho:** DESI (puntos de void, el catálogo DESIVAST DR1).
- En el centro, los dos conjuntos convergen → un gráfico de stacking, x=0 en el centro del void, y=T(μK).

*Texto:* "Telescopios públicos. Datos abiertos. Sin cocina."

*Luz:* Neutra, blanca. Es preparación.

## Escena 3 — La medición (12 s)

*Visual:* El gráfico de stacking se construye punto por punto (con efecto de render de escaneo CRT, barrido vertical). Los puntos caen alrededor de y = +1.2 μK. Barra de error horizontal en ±1.5 μK.

*Superposición:* La predicción aparece como una línea punteada en y = −19 μK. Está lejos. Muy lejos. Una banda sombreada se extiende desde −18.5 hasta −61.7. El "+1.2" está fuera de ella por ~13 desviaciones estándar.

*Pausa:* 1.5 segundos de silencio visual — los puntos ya cayeron, el ojo procesa la separación.

*Texto que aparece debajo, sin animación:*
```
ΔT_stack_predicted = −19 μK
ΔT_stack_measured  = +1.2 ± 1.5 μK
Discrepancia > 13σ
```

*Color:* La predicción se desvanece a gris (`#6B7280`). La medición permanece en blanco.

## Escena 4 — El commit (10 s)

*Visual:* La terminal de la Escena 1 vuelve desde el fondo. El mismo manifiesto, intacto. No se mueve. No se edita. No se añade "pero si excluimos X" ni "aunque corrigiendo Y".

*Debajo del manifiesto, un nuevo texto aparece:*
```
Resultado: +1.2 ± 1.5 μK. Consistente con ΛCDM.
Falsifier 1: FIRED.
Sector ISW: RETRACTED AS CALIBRATED.
```

*El hash del commit de pre-registro está presente. Esta es la misma pantalla de la Escena 1.*

*Último texto:* "Salga como salga."

*Luz:* El azul BAO de la Escena 1 vira lentamente a gris ISW (`#6B7280`). No se apaga. Permanece encendido en gris.

## Escena 5 — Lección (5 s, opcional)

*Visual:* Tres cajas en pantalla:
1. Pre-registraste → EXIGE
2. Refutaron → PUBLICA
3. No rescatas → CRECES

La caja 2 parpadea al mismo gris.

*Silencio.* Sin música de cierre.

---

## Notas técnicas

- **Colores:** Claims table exacta. BAO azul `#3B82F6`, ISW muerto `#6B7280`, DM ámbar `#F59E0B`. No hay música triunfal.
- **Sonido:** Solo el tic-tac de un cursor parpadeante en la terminal. Si hay música, que sea un loop de bajísimo volumen de un reloj que no llega a tictaquear — puro sustain.
- **Render:** Manim Cairo (sin audio por ahora, o con el sonido de terminal ambiente). Sin narración en off. El texto cuenta todo.
- **Provenance:** El hash del commit de pre-registro debe ser real. Si no existe el commit actual, que se vea un placeholder `[0000000]` para sustituir después.
- **Duración total (5 escenas):** ~45 s.
- **No renderizar** hasta que Patricio apruebe el arco narrativo.
