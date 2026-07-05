# Tensor energía-momento efectivo para \(\psi\) en Postulado 3'

Fecha: 2026-07-03  
Estado: borrador técnico interno. No es claim físico final.  
Uso previsto: formalismo auxiliar para ordenar el acoplamiento disforme de
\(\psi\) en el paper.

---

## 1. Métrica efectiva de materia

Sea $\eta_{\mu\nu}$ la métrica de fondo con firma $(-+++)$. Definimos
\[
u_\mu \equiv \frac{\partial_\mu h}{\sqrt{-\,\partial_\nu h\,\partial^\nu h}},
\qquad
h(x) = \text{longitud de la cadena más larga desde el post hasta } x,
\]
donde $h$ es el campo de profundidad de cadena (DP 18a). Su gradiente normalizado es timelike donde el poset es manifoldlike (Brightwell–Gregory; véase `anisotropia_cadena_anticadena.md`, sección 4).

El proyector espacial es
\[
h_{\mu\nu} = \eta_{\mu\nu} + u_\mu u_\nu .
\]

El campo escalar adimensional $\psi$ define la métrica efectiva que ve la materia:
\[
\tilde g_{\mu\nu}(\psi)
= e^{2\psi} h_{\mu\nu} - e^{-2\psi} u_\mu u_\nu .
\]

En el frame de reposo de $u^\mu = (1,0,0,0)$,
\[
d\tilde s^2 = -e^{-2\psi} c^2 dt^2 + e^{2\psi} d\mathbf{x}^2 .
\]

En el límite $\psi\to0$,
\[
\tilde g_{\mu\nu} \to \eta_{\mu\nu}.
\]

---

## 2. Acción y lagrangiano

La acción efectiva mínima es

\[
S=S_\psi+S_m[\chi,\tilde g_{\mu\nu}(\psi)] ,
\]

con

\[
S_\psi=\int d^4x\,\mathcal L_\psi ,
\]

\[
\mathcal L_\psi
=
-\frac{c^4}{8\pi G}
\eta^{\alpha\beta}\partial_\alpha\psi\,\partial_\beta\psi
-V(\psi).
\]

Definimos

\[
A\equiv \frac{c^4}{8\pi G}.
\]

Entonces

\[
\mathcal L_\psi=-A(\partial\psi)^2-V(\psi),
\]

donde

\[
(\partial\psi)^2
\equiv
\eta^{\alpha\beta}\partial_\alpha\psi\,\partial_\beta\psi .
\]

El acoplamiento disforme a materia entra solo por

\[
S_m[\chi,\tilde g_{\mu\nu}(\psi)].
\]

Para materia no relativista en reposo,

\[
S_m\simeq-\int dt\,d^3x\,\rho c^2 e^{-\psi}.
\]

---

## 3. Tensor energía-momento de \(\psi\)

El tensor energía-momento efectivo del campo \(\psi\), variando respecto del
fondo métrico, es

\[
T_{\mu\nu}^{(\psi)}
=
2A\,\partial_\mu\psi\,\partial_\nu\psi
+\eta_{\mu\nu}\mathcal L_\psi .
\]

Es decir,

\[
T_{\mu\nu}^{(\psi)}
=
\frac{c^4}{4\pi G}
\partial_\mu\psi\,\partial_\nu\psi
+\eta_{\mu\nu}
\left[
-\frac{c^4}{8\pi G}(\partial\psi)^2
-V(\psi)
\right].
\]

Este tensor describe solo la energía-momento efectiva asociada al campo
\(\psi\). La materia tiene su propio tensor definido respecto de
\(\tilde g_{\mu\nu}\).

---

## 4. Energía y presión en fondo plano

Usamos coordenadas \(x^0=ct\), de modo que

\[
\partial_0\psi=\frac{1}{c}\dot\psi .
\]

Entonces

\[
(\partial\psi)^2
=
-\frac{\dot\psi^2}{c^2}
+|\nabla\psi|^2 .
\]

La densidad de energía efectiva es

\[
\rho_\psi c^2=T_{00}^{(\psi)}
=
A\frac{\dot\psi^2}{c^2}
+A|\nabla\psi|^2
+V(\psi).
\]

Para un fondo homogéneo, \(\nabla\psi=0\):

\[
\rho_\psi c^2
=
A\frac{\dot\psi^2}{c^2}
+V(\psi).
\]

La presión isotrópica se obtiene de

\[
p_\psi=\frac13\delta^{ij}T_{ij}^{(\psi)}.
\]

En general,

\[
p_\psi
=
A\frac{\dot\psi^2}{c^2}
-\frac{A}{3}|\nabla\psi|^2
-V(\psi).
\]

Para un fondo homogéneo:

\[
p_\psi
=
A\frac{\dot\psi^2}{c^2}
-V(\psi).
\]

Por tanto,

\[
w_\psi
=
\frac{p_\psi}{\rho_\psi c^2}
=
\frac{A\dot\psi^2/c^2-V}
{A\dot\psi^2/c^2+V}
\qquad
(\nabla\psi=0).
\]

---

## 5. Fuente efectiva de materia

La variación del acoplamiento de materia respecto de \(\psi\) genera la fuente.
En el régimen no relativista,

\[
\frac{\delta S_m}{\delta\psi}
\simeq
\rho c^2 e^{-\psi}.
\]

La ecuación de campo, sin términos extra, es

\[
\frac{c^4}{4\pi G}\Box_\eta\psi
-V'(\psi)
+\rho c^2 e^{-\psi}
=0.
\]

Para \(V=0\) y \(|\psi|\ll1\),

\[
\Box_\eta\psi
\simeq
-\frac{4\pi G}{c^2}\rho .
\]

En el límite estático:

\[
\nabla^2\psi
=
-\frac{4\pi G}{c^2}\rho .
\]

Con la identificación

\[
\Phi_N=-c^2\psi,
\]

se recupera

\[
\nabla^2\Phi_N=4\pi G\rho.
\]

Esta identificación fija el signo: una masa positiva tiene
\(\Phi_N<0\), por tanto \(\psi>0\), y entonces
\(e^{-\psi}<1\), es decir, relojes más lentos cerca de la fuente.
