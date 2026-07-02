# El TODO en vez del infinito

**Estado: nota de fundamentos — lenguaje, no mecanismo.** Nada de lo que
sigue predice un número nuevo. Su función es identificar qué matemática
*ya existente y con nombre* está usando (a veces sin saberlo) cada
pieza de Render, para heredar teoremas en vez de reinventar — y para
prevenir la próxima generación de errores de categoría, que ya nos
costaron los experimentos 06–09. Las bases muertas (3, 6, 7) siguen
muertas; esta nota no las resucita.

---

## 1. La pantalla que se prende (la singularidad no es un punto ni un cero)

Dos correcciones de relatividad de libro a la imagen popular:

- **La singularidad del Big Bang es espacial: ocurre en todas partes a
  la vez.** Si el universo es infinito hoy, era infinito en t→0. Lo que
  tiende a cero es el factor de escala (las distancias relativas), no
  el "tamaño del universo". La "singularidad enorme" es la lectura
  correcta del formalismo; "el universo era un puntito", no.
- **"Infinitamente caliente" es una etiqueta de extrapolación, no una
  medición.** La singularidad es la frontera de validez de la teoría.
  Además, la temperatura es un concepto estadístico: requiere muchos
  grados de libertad. Un estado de una sola distinción (ℛ=1) no tiene
  temperatura — la pregunta no aplica.
- **Lo innegociable (base 6 muerta):** desde t ~ 1 s el universo estaba
  a ~10¹⁰ K. BBN (abundancias de He/D) y FIRAS (cuerpo negro perfecto)
  lo fijan como dato. "El estado inicial no tiene temperatura definida"
  y "el universo temprano medible fue caliente" son compatibles; lo que
  está refutado es extender el frío hacia donde hay datos.

Lectura Render: t=0 no es un cero — es el **post** (Sorkin 2000;
Dowker & Zalel 2017): ℛ=1, la pantalla en el instante previo al primer
refresco. En el rango de ℛ ∈ [1, ∞), el cero no existe: cero sería el
conjunto causal vacío (la pantalla apagada), y de eso no hay física.

## 2. Meter el infinito dentro de la pantalla: compactificación

- **Alexandroff (un punto):** ℝⁿ + {∞} = esfera. El infinito pasa a ser
  un punto ordinario. La esfera de Riemann hace esto para ℂ y ahí
  1/0 = ∞ es aritmética legal.
- **Compactificación conforme de Penrose:** el espacio-tiempo infinito
  entero dibujado en un diamante finito; el infinito es el *borde del
  dibujo* (𝒥±, i⁰, i±). "El infinito está fuera de la pantalla" es
  literalmente cómo trabajan los relativistas.
- **El Postulado 1 de Render ("variedad de tamaño total 1 en unidades
  conformes") ES una compactificación conforme.** No hay que inventar
  la matemática del canvas: hay que citarla. Los conos de luz son
  invariantes conformes, por eso este movimiento es honesto — y por
  eso, también, no regala la solución del horizonte (§ pendiente en el
  paper).

## 3. La aritmética nativa de pantallas: geometría proyectiva

Inventada por pintores para el problema exacto de este proyecto: meter
el infinito en un lienzo. El punto de fuga es el punto en el infinito
*sobre* el cuadro. Formalizada en **coordenadas homogéneas** (los
puntos en el infinito son los de w=0 — coordenadas normales, cero casos
especiales), es la aritmética en la que corre todo pipeline gráfico
moderno. La matemática de las pantallas trata al infinito como una
carta coordenada más desde hace siglos.

## 4. El TODO como completitud (no como cardinal)

"∞=1 no es ℵ₀ — es totalidad" tiene nombre técnico:

- **Compacidad:** la propiedad "el todo se comporta como un objeto
  finito" (todo cubrimiento infinito se reduce a uno finito).
- **Completación / teoría de dominios (Scott):** el TODO de un proceso
  de refinamiento es su elemento límite ⊤. π no es una cosa de
  infinitos dígitos: es el *ideal* de sus aproximaciones finitas — la
  totalidad de la torre, como objeto.
- **La fórmula del producto de Artin** |x|_∞ · Π_p |x|_p = 1: el
  producto sobre TODOS los lugares (el ∞ incluido) es exactamente 1.
  Rima estructural legítima con ∞=1; sigue siendo rima hasta que derive
  algo.

## 5. Vectores y raster (la mejor distinción del proyecto)

- **Capa vectorial = lo exacto por simetría, no muestreado:** carga
  1/3, spin 1/2, números cuánticos. Vienen de teoría de grupos; son
  razones exactas a cualquier resolución. Por eso 1/3 no tiene
  expansión finita en dígitos ni cumpleaños finito en los surreales:
  no es un objeto rasterizado. (En fracciones continuas, 1/3 = [0;3]
  — finito: la única representación donde todos los racionales medidos
  son objetos completos de resolución finita.)
- **Capa raster = lo muestreado con resolución:** masas, acoplamientos.
  Y la física de "los valores dependen de la resolución de muestreo"
  ya existe, está confirmadísima y se llama **grupo de
  renormalización**: α corre de 1/137 a ~1/128 según la escala a la que
  se la mira. El RG es la teoría de los valores raster en función del
  zoom.

## 6. El cero, el uno y el TODO

- **El cero con pedigrí:** el 0 de Conway es { | } — el corte vacío, un
  número hecho de nada. El cero es la pantalla apagada; ℛ=1 es la
  pantalla prendida sin distinciones. Son estados distintos, y Render
  vive en el segundo.
- **El pixel de tres atributos existe y es el agujero negro (teorema de
  no-pelo):** un BH estacionario queda descrito por exactamente masa,
  carga y spin. El objeto de máxima compresión informacional del
  universo, descrito por tres números. (La versión para partículas —
  base 3 — sigue muerta; el anfitrión correcto de la intuición era
  este.)
- **"¿Puede el cero ser enorme?" — profundidad vs extensión:** el
  interior de un BH es profundidad-de-resolución mínima (Postulado 7:
  ℛ=1) con área de horizonte gigantesca, contada en píxeles de Planck:
  S = A/4ℓ_P². En jerga de motores gráficos: el billboard/impostor
  LOD-0 del universo — resolución interna mínima, área de pantalla
  enorme.
- **Temperatura:** T_Hawking ∝ 1/M — los agujeros negros son los
  objetos más fríos del universo (10⁻¹⁴ K un supermasivo). La
  compresión máxima es gélida, no caliente.
- **"Universo = agujero negro":** la coincidencia real es que
  R_Schwarzschild(M_universo) ≈ R_Hubble — y su traducción exacta es
  Ω ≈ 1: la planitud (densidad crítica). Es planitud con otro disfraz,
  no magia. Y la versión seria de "el BH como semilla de universo" ya
  está publicada y citada en el paper: Dowker & Zalel 2017 modelan la
  singularidad de un BH como evento de creación de un universo nuevo
  (selección natural cosmológica de Smolin).
- **Cero e infinito en la pantalla total:** en la esfera de Riemann son
  los dos polos, intercambiados por la inversión z ↦ 1/z. Puntos
  ordinarios, conformemente equivalentes; "cuál es el chico" es un
  artefacto de la carta de coordenadas. (Acá vive legítimamente la rima
  R ↔ 1/R que el exp 09 usó mal: en geometría conforme, no en cuerdas.)

## Cierre

Render no necesita un sistema numérico nuevo. Necesita reconocer cuál
de estos —compactificación conforme, geometría proyectiva, completitud,
fracciones continuas, grupo de renormalización— está usando cada
postulado, y decirlo con el nombre que ya tiene. El día que alguna de
estas estructuras *derive* un resultado del marco (en vez de rimarlo),
pasará de lenguaje a mecanismo. Hasta entonces: este es el idioma; la
física sigue debiéndose en los experimentos.
