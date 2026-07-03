# Borrador de seccion corta: kernel de links \(K(x,y)\)

Fecha: 2026-07-03  
Estado: BORRADOR para auditoria. No insertar en `paper/` sin revision.

Objetivo: proponer una forma breve de introducir el kernel de links en el
paper, sin inflar el claim. El enfasis narrativo es:

> \(K(x,y)\) es un kernel causal discreto que, en el limite debil y
> estacionario, debe generar el potencial newtoniano como kernel efectivo.

La frase fuerte debe ir condicionada por el limite:

> En el limite de fuente estatica, campo debil y proyeccion temporal, el
> kernel de links se calibra para recuperar \(K_{\rm stat}(r)\propto 1/r\).

---

## Texto propuesto

### Link kernel and the Newtonian weak-field limit

The local-density version of Postulate 6 is not sufficient to describe
gravitational redshift, because redshift is controlled by a potential rather
than by the local density alone. We therefore introduce a causal, non-local
link kernel \(K(x,y)\), defined from irreducible causal relations in the
underlying sprinkling.

Let \(y\prec x\) denote causal precedence and let \(I(y,x)\) be the open
causal interval between \(y\) and \(x\). A pair \((y,x)\) is a link when no
element of the causal set lies inside \(I(y,x)\). The microscopic selector is

\[
\chi_{\rm link}(x,y)
=
\mathbf 1[y\prec x]\,
\mathbf 1[N(I(y,x))=0].
\]

For a Poisson sprinkling with density \(\rho_s\), its expectation value is

\[
\langle\chi_{\rm link}(x,y)\rangle
=
\mathbf 1[y\prec x]\,
\exp[-\rho_s V(I(y,x))],
\]

or, for inhomogeneous sprinklings,

\[
\langle\chi_{\rm link}(x,y)\rangle
=
\mathbf 1[y\prec x]\,
\exp\!\left[-\int_{I(y,x)}\rho_s(u)\,dV_u\right].
\]

We define the retarded link kernel

\[
K_{\rm ret}(x,y)
=
\mathcal N_R\,
\mathbf 1[y\prec x]\,
\exp\!\left[-\int_{I(y,x)}\rho_s(u)\,dV_u\right]\,
W_R(x,y),
\]

where \(W_R\) is the finite-resolution window and \(\mathcal N_R\) is fixed
by the continuum normalization. The auxiliary potential is then

\[
\Psi(x)
=
\int K_{\rm ret}(x,y)\,\varrho(y)\,d^4y,
\]

with \(\varrho\) the physical source density and \(\rho_s\) the sprinkling
density.

For a static weak-field source, the relevant comparison with Newtonian
gravity is not the four-dimensional causal kernel itself, but its stationary
projection,

\[
K_{\rm stat}(\mathbf x,\mathbf y)
=
\int d\Delta t\,
K_{\rm sym}\!\left((t,\mathbf x),(t+\Delta t,\mathbf y)\right).
\]

The Newtonian limit is the condition

\[
K_{\rm stat}(\mathbf x,\mathbf y)
\longrightarrow
-\frac{G_{\rm eff}}{|\mathbf x-\mathbf y|}
\]

over the calibrated weak-field range. Equivalently, the numerical check is

\[
r\,K_{\rm stat}(r)\simeq \mathrm{constant}.
\]

In this sense, the link kernel is proposed as the causal-set generator of the
Newtonian potential in the weak-field limit.

---

## Nota de precedentes

Johnston introduced causal-set propagators in which continuum Green functions
are recovered from causal relations and link-like structures. The relevant
precedent is that a causal set can encode propagation kernels through
order-theoretic data rather than through a pre-existing continuum differential
operator.

The use here is narrower and more specific: \(K(x,y)\) is not introduced as a
generic scalar propagator, but as a candidate generator of the Newtonian
potential after static projection of link counts. That use should be labeled
as novel within this project unless a closer precedent is found.

**Validación vs Johnston 2009/2010 (arXiv:0806.3083, PRL 103, 180401):** 
La definición de \(K\) (selector de covering relations / link matrix + factor Poisson) coincide con el objeto matemático usado por Johnston para construir propagadores discretos que recuperan el límite continuo. No hay conflicto en el formalismo; el draft usa el mismo "link kernel" pero lo proyecta a potencial newtoniano (en lugar de propagador QFT). El draft ya distingue correctamente el uso.

**Búsqueda de kernels discretos para Newton en CST (no QFT):** 
NO ENCONTRADO. Búsquedas (web/arXiv: "causal set" (Newtonian OR "weak field" OR "1/r") (kernel OR "link matrix" OR covering OR Hasse) -propagator -Johnston) no arrojaron fuentes que usen kernels discretos basados en links/covering específicamente para generar potencial newtoniano en CST. La literatura usa link matrix principalmente para propagadores escalares (Johnston et al.) o acciones de curvatura (Benincasa-Dowker). Citar Johnston como precedente para kernels causales, pero la aplicación newtoniana parece específica del proyecto.

Citation placeholder:

- Johnston 2009: causal-set propagators / Green functions. Verify exact
  bibliographic metadata before inserting into the paper.

---

## Frases seguras

1. "The link kernel provides a non-local replacement for the local-density
   rule."
2. "The Newtonian comparison is made only after static projection."
3. "The \(1/r\) behavior is a weak-field target of the projected kernel, not a
   pointwise identity of the four-dimensional causal kernel."
4. "The Johnston construction is a precedent for extracting propagators from
   causal-set order; the present use as a Newtonian generator is project
   specific."

---

## Frases peligrosas

1. "Links prove Newtonian gravity."  
   Mejor: "The projected link kernel is tested against the Newtonian
   \(1/r\) form."

2. "\(K(x,y)=1/r\)."  
   Mejor: "The stationary projection \(K_{\rm stat}(r)\) is compared with
   \(1/r\)."

3. "This derives dark matter from links."  
   Mejor: "This provides a non-local weak-field kernel; galaxy-scale
   phenomenology remains a separate test."

4. "The kernel has compact support."  
   Mejor: "The kernel has causal support and compact support only after a
   finite window \(W_R\) or finite simulation domain is imposed."

---

## Insercion sugerida

Ubicacion natural:

1. Despues de reformular Postulado 6 como conteo de links.
2. Antes de discutir Pound-Rebka / limite newtoniano.
3. Antes de cualquier claim de rotacion galactica.

Extension recomendada:

Entre 5 y 8 parrafos, una ecuacion para \(\chi_{\rm link}\), una para
\(K_{\rm ret}\), una para \(\Psi\), y una para el limite proyectado
\(K_{\rm stat}\to -G_{\rm eff}/r\).

Etiqueta recomendada:

**Ansatz operacional / programa numerico**, no "derivacion completa".
