# Paper 2 — esqueleto de prosa
**Estado: BORRADOR. Arrancado 2026-07-06 tras cierre del Paper 1 (DOI ready).**
**Companion:** storyboard falsador 3 actos en notes/creative/02d_storyboard_falsador_2026-07-06.md.

**Título tentativo:** *The falsification arc: pre-registration, a coordinate bug, and the refutation that held*

---

## Estructura

### 1. Introducción (1 párrafo)
El Paper 1 midió leyes de conteo de links con pre-registro y reproducibilidad determinista. Este paper documenta por qué esa metodología es necesaria: cuenta la historia completa de una predicción pre-registrada que el cielo refutó, cómo un bug de marco de coordenadas se descubrió después de publicar, y cómo la corrección sostuvo la refutación más fuerte.

### 2. La predicción (1 párrafo)
Referencia al pre-registro del Exp 17. La predicción: ΔT ≈ −19 μK para el stacking ISW sobre voids DESIVAST DR1 (rango hasta −61.7 μK). Manifiesto: "Publicamos salga como salga."

### 3. La refutación (1 párrafo)
Resultado Exp 17: ΔT = +1.2 ± 1.5 μK. 13σ de la predicción. Publicado sin editar el manifiesto.

### 4. El bug (1 párrafo)
Revisión externa (Fable) detectó: los voids se midieron en coordenadas ecuatoriales, no galácticas — el header COORDSYS no se verificó. Desviación de ~2°. El stacking no medía el cielo, medía el instrumento. **Protocolo regla 3** nace de aquí.

### 5. La corrección (1 párrafo)
Exp 17b: astrometría V0 verificada, 1454 voids (catálogo completo). ΔT = +0.37 ± 0.93 μK. Refutación empírica: 20.7σ. Refutación H2: 67σ. La refutación se sostuvo, corregida y más fuerte.

### 6. El patrón del instrumento raster (2 párrafos — el método)
La misma falla aparece en 4 lugares del proyecto + 1 en literatura CST:
1. Bug de coordenadas del 17
2. Silencio asintótico de la adyacencia (Boguñá-Krioukov 2024)
3. Paradoja de la escalera π=4
4. Ventana coordenada del 25b
5. Estimador soft e^(−ρV) del 18

Enunciado: "Medir estructura con coordenadas del instrumento produce resultados que parecen mediciones pero son propiedades del instrumento. El refinamiento no lo corrige — lo consolida."

### 7. La regla (1 párrafo)
Pregunta heurística nueva: "¿Qué mide esto si el objeto es trivial y solo el instrumento varía?" — operacionalizada como el control fantasma C1' del 25b.

### 8. Conclusión (1 párrafo)
Pre-registrar no es heroico. Es una regla que te pones para no mover el arco después de disparar. Publicar el error propio no es fracaso — es lo único que convierte un error en ciencia.

---

## Notas

- **Claims usados:** FUNDAMENTOS §I #9 (REFUTADO-FIRME), PROTOCOLO reglas 2, 3, 5.
- **Referencia al patrón:** notes/foundations/patron_instrumento_raster_2026-07-06.md.
- **Storyboard:** 02d_storyboard_falsador_2026-07-06.md (3 actos: predicción → bug → corrección + patrón).
- **Video companion:** falsador 3 actos (cola creativa post-DOI).
- **Longitud estimada:** 5-7 páginas.

## Pendiente que no bloquea el esqueleto
- [ ] Verificar hashes de commits reales para citar en el texto
- [ ] Decidir si incluir tabla de patrones (sección 6) como figura
- [ ] Confirmar orden de autoría con Patricio
