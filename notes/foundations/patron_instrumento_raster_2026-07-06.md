# El patrón del instrumento raster — nota de método (Fable, 2026-07-06)

**Estado: OBSERVACIÓN METODOLÓGICA (no es un claim físico).
Candidata a §método del Paper 2.**

## El patrón

Cuatro fallas independientes del proyecto, encontradas por caminos
distintos, resultan ser la MISMA falla:

| # | Falla | Dónde | Forma específica |
|---|---|---|---|
| 1 | Bug de coordenadas del Exp 17 | medición ISW | medimos el cielo con el marco del instrumento (ecuatorial) en vez del marco del dato (galáctico) |
| 2 | Silencio asintótico de la adyacencia | literatura CST (Boguñá-Krioukov 2024) | la distancia espacial medida por adyacencia del grafo no converge a la métrica; hay que medir con estructura (solapamientos causales) |
| 3 | Paradoja de la escalera (π=4) | doctrina raster/vector | el perímetro medido por adyacencia ortogonal de píxeles da 4, no π; el refinamiento no lo arregla — la MEDIDA está mal, no la resolución |
| 4 | Ventana coordenada del 25b (cazada por Codex pre-run) | diseño experimental propio | la bola |Δx|<W tiene tamaño físico W·ℛ: la ventana escala con la señal y el instrumento fabrica el exponente |

Y un quinto pariente cercano: el estimador soft e^(−ρV) del Exp 18
(2.95 vs 2.70) — reemplazar el conteo estructural exacto (bloqueadores)
por una aproximación local del instrumento sesga el exponente.

## El enunciado común

**Medir una cantidad estructural con las coordenadas/adyacencias del
instrumento, en vez de con la estructura del objeto, produce
resultados que parecen mediciones pero son propiedades del
instrumento.** Y el refinamiento (más resolución, más N, más
estadística) NO corrige el error — lo consolida con barras de error
más chicas. El 17 daba 20.7σ de "refutación" con astrometría rota; la
escalera da π=4 con precisión infinita.

## Por qué importa al proyecto (dos direcciones)

1. **Como método**: es nuestra clase de bug más recurrente y más
   peligrosa (pasa todos los tests nulos: los nulos son ciegos a
   errores de marco). Antídotos ya en protocolo: marcos leídos del
   header (regla 3), estimadores estructurales (Boguñá-Krioukov en
   25b), ventanas propias (Enmienda 3), controles positivos con
   predicción analítica (C5, V2 del 17b). Regla heurística nueva
   propuesta: **ante cualquier estimador nuevo, preguntar "¿qué mide
   esto si el objeto es trivial y solo el instrumento varía?"** — el
   control fantasma C1' del 25b es exactamente esa pregunta
   operacionalizada.

2. **Como consistencia informal del marco**: la distinción
   raster/vector del proyecto (cantidades muestreadas vs datos
   estructurales exactos) predice que esta clase de error EXISTE y es
   sistemática. Que nuestros propios experimentos tropiecen
   repetidamente con ella, y que la literatura CST haya tropezado con
   la versión #2 durante años (distancia espacial), es evidencia
   informal de que la distinción corta la realidad por una
   articulación verdadera. NO es evidencia de la cosmología del
   proyecto; es evidencia de que la epistemología del proyecto es
   operativa. Se dice así, con esa modestia exacta, o no se dice.

## Destino propuesto

- Paper 2 (marco/método): sección "The raster instrument fallacy" con
  la tabla de arriba — el arco 17→bug→17b como caso central y el
  cazado-pre-run del 25b como demostración de que el patrón, una vez
  nombrado, es prevenible.
- Wiki: página en El Método, después de aprobar esta nota.
- Video (Hermes, futuro): la escalera YA es el trailer de esta idea.
