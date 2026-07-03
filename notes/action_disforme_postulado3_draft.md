# Acción efectiva para una métrica disforme del Postulado 3

Fecha: 2026-07-03  
Estado: nota técnica interna, no paper.  
Objetivo: escribir una acción efectiva mínima para un escalar adimensional
\(\psi\) cuyo acoplamiento métrico produzca, en fondo plano,

\[
ds^2=-e^{-2\psi}c^2dt^2+e^{+2\psi}d\mathbf{x}^2 .
\]

La nota usa una formulación efectiva con un frame temporal preferido. No se
declara como teoría covariante final. Para volverla covariante habría que
dinamizar el vector temporal \(u^\mu\) o reemplazarlo por un campo reloj.

---

## 1. Métrica efectiva

Sea \(\eta_{\mu\nu}\) la métrica de Minkowski con firma \((-+++)\), y sea
\(u^\mu\) un vector unitario temporal fijo,

\[
\eta_{\mu\nu}u^\mu u^\nu=-1 .
\]

Definimos el proyector espacial

\[
h_{\mu\nu}=\eta_{\mu\nu}+u_\mu u_\nu .
\]

La métrica que ve la materia es

\[
\tilde g_{\mu\nu}(\psi)
=e^{2\psi}h_{\mu\nu}-e^{-2\psi}u_\mu u_\nu .
\]

En el frame de reposo de \(u^\mu=(1,0,0,0)\), esto da

\[
d\tilde s^2=-e^{-2\psi}c^2dt^2+e^{2\psi}d\mathbf{x}^2 .
\]

Límite plano:

\[
\psi\to 0
\quad\Rightarrow\quad
\tilde g_{\mu\nu}\to h_{\mu\nu}-u_\mu u_\nu=\eta_{\mu\nu}.
\]

Por lo tanto,

\[
d\tilde s^2\to -c^2dt^2+d\mathbf{x}^2 .
\]

---

## 2. Acción efectiva

Tomamos \(\psi\) adimensional. Una acción mínima es

\[
S=S_\psi+S_m[\chi,\tilde g_{\mu\nu}(\psi)] ,
\]

con

\[
S_\psi
=\int d^4x\,
\left[
-\frac{c^4}{8\pi G}\,
\eta^{\mu\nu}\partial_\mu\psi\,\partial_\nu\psi
-V(\psi)
+\mathcal L_{\rm gal}
\right].
\]

El término galileónico opcional puede elegirse como

\[
\mathcal L_{\rm gal}
=-\frac{\alpha c^4}{8\pi G\Lambda^3}
\left(\eta^{\mu\nu}\partial_\mu\psi\partial_\nu\psi\right)
\Box_\eta\psi ,
\]

donde \(\Lambda\) es una escala de no-linealidad. Para el límite newtoniano
básico se puede tomar \(\alpha=0\). El término está escrito solo como
posible mecanismo de apantallamiento; no es necesario para recuperar
Minkowski ni la ecuación de Poisson.

La materia se acopla métricamente a \(\tilde g_{\mu\nu}\), no directamente a
\(\eta_{\mu\nu}\). Para partículas puntuales,

\[
S_m=-\sum_a m_a c^2\int d\tilde\tau_a .
\]

Para una partícula no relativista en reposo,

\[
d\tilde\tau=e^{-\psi}dt,
\]

y por tanto

\[
S_m\simeq-\int dt\,d^3x\,\rho(\mathbf{x})c^2e^{-\psi}.
\]

---

## 3. Ecuación de campo

Variando la acción respecto de \(\psi\), e ignorando por ahora el término
galileónico, se obtiene

\[
\frac{c^4}{4\pi G}\Box_\eta\psi
-V'(\psi)
+\frac{\delta S_m}{\delta\psi}=0 .
\]

En el régimen no relativista,

\[
\frac{\delta S_m}{\delta\psi}
\simeq
\rho c^2 e^{-\psi}.
\]

Luego,

\[
\frac{c^4}{4\pi G}\Box_\eta\psi
-V'(\psi)
+\rho c^2e^{-\psi}=0 .
\]

Si \(V=0\), esto queda como

\[
\Box_\eta\psi
=-\frac{4\pi G}{c^2}\rho e^{-\psi}.
\]

En el límite débil \(|\psi|\ll 1\),

\[
\Box_\eta\psi
\simeq
-\frac{4\pi G}{c^2}\rho .
\]

Para fuentes estáticas,

\[
\nabla^2\psi
=-\frac{4\pi G}{c^2}\rho .
\]

La variable \(\psi\) se relaciona con el potencial newtoniano usual por

\[
\Phi_N=-c^2\psi .
\]

Así,

\[
\nabla^2\Phi_N=4\pi G\rho .
\]

El signo es consistente: una masa positiva tiene \(\Phi_N<0\) y por tanto
\(\psi>0\), lo que hace que \(e^{-\psi}<1\) y ralentiza el tiempo propio
cerca de la masa.

---

## 4. Fuente puntual

Para una masa puntual \(M\) en el origen,

\[
\rho(\mathbf{x})=M\delta^{(3)}(\mathbf{x}).
\]

La ecuación linealizada es

\[
\nabla^2\psi
=-\frac{4\pi GM}{c^2}\delta^{(3)}(\mathbf{x}).
\]

Usando

\[
\nabla^2\left(\frac{1}{r}\right)
=-4\pi\delta^{(3)}(\mathbf{x}),
\]

la solución con \(\psi\to0\) en infinito es

\[
\psi(r)=\frac{GM}{c^2r}.
\]

Entonces

\[
\Phi_N(r)=-c^2\psi(r)=-\frac{GM}{r}.
\]

La métrica efectiva queda

\[
d\tilde s^2
=
-e^{-2GM/(c^2r)}c^2dt^2
+e^{2GM/(c^2r)}d\mathbf{x}^2 .
\]

En el límite débil,

\[
e^{-2\psi}\simeq1-2\psi,
\qquad
e^{2\psi}\simeq1+2\psi,
\]

y por tanto

\[
d\tilde s^2
\simeq
-\left(1-\frac{2GM}{c^2r}\right)c^2dt^2
+\left(1+\frac{2GM}{c^2r}\right)d\mathbf{x}^2 .
\]

Como \(\Phi_N=-GM/r\), esto también puede escribirse como

\[
d\tilde s^2
\simeq
-\left(1+\frac{2\Phi_N}{c^2}\right)c^2dt^2
+\left(1-\frac{2\Phi_N}{c^2}\right)d\mathbf{x}^2 .
\]

Esta es la forma débil isotrópica con \(\gamma=1\) a primer orden.

---

## 5. Con potencial de masa opcional

Si se agrega

\[
V(\psi)=\frac{c^4}{8\pi G\lambda^2}\psi^2 ,
\]

la ecuación estática linealizada se vuelve

\[
\left(\nabla^2-\lambda^{-2}\right)\psi
=-\frac{4\pi G}{c^2}\rho .
\]

Para una fuente puntual,

\[
\psi(r)=\frac{GM}{c^2r}e^{-r/\lambda}.
\]

El caso \(\lambda\to\infty\) recupera la solución newtoniana.

---

## 6. Lectura técnica

Lo logrado por esta nota:

1. Escribe una acción efectiva explícita para \(\psi\).
2. La materia se acopla métricamente a \(\tilde g_{\mu\nu}(\psi)\).
3. En \(\psi\to0\), la métrica efectiva recupera Minkowski.
4. En fondo plano y límite estático, la ecuación de campo reduce a Poisson.
5. Una masa puntual produce \(\psi=GM/(c^2r)\), equivalente a
   \(\Phi_N=-GM/r\).

Limitaciones:

1. La formulación usa un frame temporal preferido \(u^\mu\).
2. No deriva \(u^\mu\), ni lo hace dinámico.
3. El término galileónico queda como opción, no como necesidad.
4. Esto no reemplaza una teoría relativista completa; es una acción
   efectiva para estudiar el Postulado 3 en fondo plano.

## Comparación con literatura (destilado de búsqueda previa)

Coincide exactamente con la transformación disformal general de Bekenstein (1993) y con el acoplamiento conformal+disformal a materia estudiado en Sakstein (2014) y Bettoni-Liberati (2013), donde factores A(φ), B(φ) generan métricas con signos opuestos en componentes temporal y espacial. Se separa en la definición específica \(\psi = \nabla \ln \mathcal{R}(t)\) motivada por resolución variable sobre canvas fijo Minkowski (ninguna de las cinco fuentes usa esta motivación ni la forma exacta con \(\psi = \nabla \ln R(t)\)). Sakstein (2014) deriva el límite newtoniano para acoplamientos disformales y discute screening para fuentes puntuales en el sistema solar, lo que puede citarse como precedente formal sin reclamar novedad en la solución estática linealizada \(\psi = GM/(c^2 r)\).
