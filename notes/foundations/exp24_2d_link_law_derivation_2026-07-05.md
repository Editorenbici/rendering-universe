# Exp 24 — ley 2D para links del cono pasado finito

Fecha: 2026-07-05  
Estado: BACKGROUND técnico. No reemplaza `exp24_results_2026-07-03.md`.

Objetivo: evitar comparar el caso 2D con la ley de área 4D

\[
v_{\rm link}^{(4D)}\simeq \pi\sqrt6\,\sqrt\rho\,R^2.
\]

En 1+1D la ley esperada para un probe con cono pasado truncado no es \(R^2\).

---

## Derivación

Para un punto candidato en el pasado del probe, usamos

\[
u=\Delta t-\Delta x,
\qquad
v=\Delta t+\Delta x.
\]

El cono pasado truncado por \(t\ge0\) queda

\[
u>0,\qquad v>0,\qquad u+v\le2R.
\]

El Jacobiano es

\[
dtdx=\frac12\,du\,dv.
\]

En 1+1D, el volumen del intervalo causal entre candidato y probe es

\[
V(I)=\frac12 uv.
\]

Para sprinkling Poisson de densidad \(\rho\), la probabilidad de que el par
sea link es la probabilidad no-blocker:

\[
P_{\rm link}(u,v)=\exp\!\left[-\rho\frac{uv}{2}\right].
\]

Entonces

\[
\mathbb E[N_{\rm link}^{(2D)}]
=
\frac{\rho}{2}
\int_0^{2R}du
\int_0^{2R-u}dv\,
\exp\!\left[-\rho\frac{uv}{2}\right].
\]

Integrando primero en \(v\):

\[
\mathbb E[N_{\rm link}^{(2D)}]
=
\int_0^{2R}
\frac{
1-\exp[-\rho u(2R-u)/2]
}{u}\,du.
\]

El integrando tiene limite finito en \(u\to0\):

\[
\lim_{u\to0}
\frac{1-\exp[-\rho u(2R-u)/2]}{u}
=
\rho R.
\]

Esta integral crece mucho mas lentamente que \(R^2\), con comportamiento
logaritmico/asintotico en ventanas grandes. Por eso el error de 2D contra la
ley 4D no debe leerse como fallo.

---

## Implementación

`code/analysis/24_epsilon_link_scaling.py` ahora reporta un bloque
`theory_comparison`.

Para `dim=2`, usa la integral 1+1D anterior por cuadratura de punto medio.

Para `dim=4`, mantiene la comparación

\[
\pi\sqrt6\,\sqrt\rho\,R^2.
\]

Uso: la próxima corrida de Exp 24 puede superponer `links_mean` contra
`expected_links` por dimensión sin mezclar leyes 2D y 4D.
