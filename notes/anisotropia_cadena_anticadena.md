# Anisotropía (1/ℛ, ℛ) desde cadenas y anticadenas: teorema de consistencia, regla microscópica requerida y u_μ operativo

**Nota técnica (lápiz). Fable, 2026-07-03.** Origen: problema abierto
definido en `sector_fotonico_metrica_disforme.md` §6.

## 1. El teorema de consistencia (derivado, no conjeturado)

Sea la métrica disforme del Postulado 3′:
$$ds^2 = -e^{-2\psi}c^2dt^2 + e^{+2\psi}d\mathbf{x}^2.$$

Su elemento de volumen: $\sqrt{-g} = \sqrt{e^{-2\psi}\cdot e^{6\psi}}
= e^{2\psi} = \mathcal{R}_{\rm rel}^2$.

Con sprinkling uniforme en volumen FÍSICO (Bombelli-Henson-Sorkin, 1
elemento por $\ell_P^4$), los conteos por unidad de volumen del CANVAS
quedan fijados:

| Cantidad del poset | Escala con $\mathcal{R}_{\rm rel}$ | Vía |
|---|---|---|
| Elementos por $d^4x$ de canvas | $\mathcal{R}^{+2}$ (¡EXCESO cerca de masa!) | $\sqrt{-g}$ |
| Pasos de cadena por $dt$ de canvas (tiempo propio) | $\mathcal{R}^{-1}$ | $d\tau/dt = e^{-\psi}$, Brightwell-Gregory |
| Pasos de anticadena por $d^3x$ de canvas (longitud propia) | $\mathcal{R}^{+3}$ | $d\ell/dx = e^{+\psi}$ |

Chequeo: $\mathcal{R}^{-1}\cdot\mathcal{R}^{+3} = \mathcal{R}^{+2}$ ✓
— la partición cadena/anticadena reproduce exactamente el volumen.

**Contraste con la métrica conforme (la refutada):**
$\sqrt{-g}_{\rm conf} = e^{-4\psi} = \mathcal{R}^{-4}$ — cerca de masa
habría DÉFICIT de elementos, con cadenas Y anticadenas contraídas
($\mathcal{R}^{-1}\times\mathcal{R}^{-3}$). **Signo opuesto.** Las dos
métricas hacen predicciones microscópicas contables y contrarias:

> Conforme: la masa borra elementos del canvas ($\mathcal{R}^{-4}$).
> Disforme: la masa AGREGA elementos ($\mathcal{R}^{+2}$), todos al
> sector espacial (anticadenas $\times\mathcal{R}^3$, cadenas
> $\div\mathcal{R}$).

## 2. La lectura física (y por qué el signo disforme es el correcto)

$\gamma_{\rm PPN}=1$ significa literalmente que hay *distancia propia
extra* alrededor del Sol — eso ES el retardo de Shapiro: el camino es
más largo cerca de masa. En lenguaje de poset: **la masa crea espacio
— elementos extra en las anticadenas — no tiempo.** El retardo de
Shapiro, contado en el causal set, es el excedente de elementos
espaciales que la luz debe atravesar. La deflexión de Eddington y el
γ=1 de Cassini son, microscópicamente, un censo de anticadenas.

## 3. La regla microscópica requerida (enunciada, NO derivada)

Para que el crecimiento del conjunto causal produzca este patrón, la
inserción de elementos inducida por materia debe ser **sesgada hacia
lo espacial**: los elementos nuevos cerca de masa deben nacer
espacialmente-relacionados con el flujo local (ensanchando anticadenas)
y no encadenados a él (que alargaría cadenas y aceleraría relojes — el
signo prohibido por Pound-Rebka). En términos de Bollobás-Brightwell:
la materia inclina el trade-off altura/anchura del orden aleatorio
hacia la anchura. Derivar los exponentes exactos (−1, +3) desde una
dinámica CSG con este sesgo es EL problema abierto que esta nota deja
definido — junto con su test numérico:

**Exp 22 (diseño, sin correr):** sprinkling con inserción sesgada
(probabilidad de relación espacial vs causal modulada por materia
local, un parámetro de sesgo b); medir altura local h(x) y anchura
local w(x) alrededor del tubo de masa; criterio pre-registrable: ¿existe
b tal que h ∝ ℛ^{-1} y w ∝ ℛ^{+3} con el MISMO ℛ(x) del conteo de
links del Exp 13? Si sí, la métrica disforme queda derivada del poset;
si ningún b lo logra, el Postulado 3′ es fenomenológico sin
microfundamento y se declara.

## 4. u_μ operativo (candidato con ecuación, para decisión del autor)

El frame del render admite ahora definición computable sobre cualquier
conjunto causal, con la maquinaria ya existente (18a):

$$u_\mu \;\equiv\; \frac{\partial_\mu h}{\sqrt{-\,\partial_\nu h\,\partial^\nu h}},
\qquad h(x) = \text{longitud de la cadena más larga desde el post hasta } x.$$

h es el campo de profundidad de cadena (calculado por DP en 18a); su
gradiente normalizado es timelike donde el poset es manifoldlike
(Brightwell-Gregory garantiza h ∝ tiempo propio en sprinklings). Esto
cumple la condición del autor ("u_μ no entra al paper sin ecuación
operativa"): la ecuación existe y es ejecutable. Si entra al paper es
decisión editorial del autor; esta nota la deja lista.

## 5. Estado

- Teorema de consistencia: DERIVADO (álgebra arriba; chequeo cerrado).
- Discriminador microscópico conforme-vs-disforme: DEFINIDO y contable.
- Regla de inserción sesgada: REQUERIDA, no derivada (abierto).
- Exp 22: diseñado, pendiente de pre-registro formal.
- u_μ: ecuación operativa disponible.
