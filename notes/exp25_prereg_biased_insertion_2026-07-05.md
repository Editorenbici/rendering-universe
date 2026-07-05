# Pre-registro Exp 25 — insercion sesgada cadena/anticadena

Fecha: 2026-07-05  
Estado: BORRADOR GATED. No correr medicion antes de auditoria.  
Origen: `notes/anisotropia_cadena_anticadena.md`.

Este experimento separa el antiguo diseño de "Exp 22" de la nota de
anisotropia. Exp 22 queda reservado para geometria de intervalos
Bollobas-Brightwell / Boguna-Krioukov. Exp 25 prueba otra cosa: si una regla
microscopica de insercion sesgada puede reproducir el patron disforme
cadena/anticadena.

---

## Pregunta especifica

Existe una dinamica simple de insercion sesgada que, alrededor de una region
marcada como masa, produzca simultaneamente:

\[
h \propto \mathcal R^{-1},
\qquad
w \propto \mathcal R^{+3},
\]

donde \(h\) mide altura/cadenas locales y \(w\) mide anchura/anticadenas
locales?

La condicion de consistencia es

\[
h\,w \propto \mathcal R^{+2},
\]

compatible con el factor de volumen disforme
\(\sqrt{-g}=e^{2\psi}=\mathcal R_{\rm rel}^2\).

---

## Hipotesis nula

\[
H_0:
\]

Ningun parametro de sesgo \(b\) en la grilla pre-registrada produce los
exponentes \(-1\) para cadenas y \(+3\) para anticadenas con el mismo campo
\(\mathcal R(x)\).

Operacionalmente, \(H_0\) pasa si:

1. El mejor ajuste de \(h\) no es compatible con \(-1\) dentro de \(2\sigma\).
2. El mejor ajuste de \(w\) no es compatible con \(+3\) dentro de \(2\sigma\).
3. Los signos salen invertidos: masa aumenta cadenas o reduce anticadenas.
4. El producto \(h\,w\) no escala cerca de \(+2\).

---

## Hipotesis alternativa

\[
H_1:
\]

Existe al menos un valor de sesgo \(b\) que produce simultaneamente:

\[
p_h=-1\pm2\sigma,
\qquad
p_w=+3\pm2\sigma,
\qquad
p_{hw}=+2\pm2\sigma.
\]

El mismo \(\mathcal R(x)\) debe usarse para los tres fits. No se permite
ajustar una \(\mathcal R\) para cadenas y otra para anticadenas.

---

## Modelo toy pre-registrado

Se construye un poset por crecimiento secuencial en capas.

Variables:

- \(N\): numero total de elementos.
- \(d\): dimension efectiva del embedding toy, solo para diagnostico.
- \(M(x)\): campo de masa marcado, normalizado en \([0,1]\).
- \(b\): parametro de sesgo espacial.
- \(\mathcal R(x)=1+\alpha M(x)\): resolucion relativa usada para medir
  exponentes.

Regla de insercion:

1. Cada nuevo elemento elige una posicion toy \(x\).
2. La probabilidad de relacion causal con elementos previos se reduce cerca
   de masa por un factor temporal:

\[
P_{\rm chain}(x)=P_0\,\mathcal R(x)^{-b}.
\]

3. La probabilidad de quedar incomparable con elementos cercanos aumenta como
   canal espacial efectivo:

\[
P_{\rm anti}(x)=1-P_{\rm chain}(x)
\]

dentro de la ventana local.

4. Se aplica cierre transitivo despues de cada batch.

Esta regla no se declara fisica; es el toy minimal para preguntar si existe
un sesgo de orden con los signos requeridos.

---

## Grilla pre-registrada

\[
b\in\{0,0.5,1,1.5,2,2.5,3,3.5,4\}.
\]

\[
\alpha\in\{0.05,0.10,0.20\}.
\]

\[
N\in\{256,512,1024\}.
\]

Realizaciones:

\[
N_{\rm real}=32
\]

por punto de grilla para un run formal. El esqueleto puede hacer dry-run
con \(N\le64\), pero eso no cuenta como medicion.

Seeds:

\[
{\rm seed}=250000 + 1000\,i_b + 100\,i_\alpha + i_N + r.
\]

---

## Observables

Para cada region radial/local alrededor de la masa marcada:

1. Altura local:

\[
h(x)=\ell_{\max}({\rm past}(x)),
\]

longitud de cadena maxima.

2. Anchura local:

\[
w(x)=\max_t |A_t(x)|,
\]

tamano maximo de una anticadena local aproximada por capas de altura.

3. Producto:

\[
q(x)=h(x)\,w(x).
\]

4. Resolucion relativa:

\[
\mathcal R(x)=1+\alpha M(x).
\]

Fits:

\[
h\propto\mathcal R^{p_h},
\qquad
w\propto\mathcal R^{p_w},
\qquad
q\propto\mathcal R^{p_{hw}}.
\]

---

## Criterios de exito

S1. Existe al menos un \(b\) estable en \(N\) tal que:

\[
p_h=-1\pm2\sigma.
\]

S2. El mismo \(b\) produce:

\[
p_w=+3\pm2\sigma.
\]

S3. El producto satisface:

\[
p_{hw}=+2\pm2\sigma.
\]

S4. Los signos son robustos en las tres \(\alpha\).

S5. La tendencia mejora o se estabiliza al aumentar \(N\).

---

## Criterios de falla

F1. Ningun \(b\) reproduce simultaneamente \(-1,+3,+2\) dentro de \(2\sigma\).

F2. El mejor \(b\) cambia de forma no convergente con \(N\).

F3. Los signos son opuestos a la metrica disforme.

F4. El resultado depende de un unico seed o de un unico \(N\).

F5. El cierre transitivo destruye el sesgo inicial y devuelve un orden
indistinguible del control \(b=0\).

---

## Controles

1. \(b=0\): control sin sesgo.
2. Masa uniforme \(M(x)=\mathrm{const}\): no debe producir gradiente local.
3. Shuffle de etiquetas de masa: debe borrar correlacion espacial.
4. Comparacion con orden aleatorio de igual \(N\) y densidad de relaciones.

---

## Compromiso

Si Exp 25 falla, la regla de insercion sesgada queda descartada como
microfundamento simple de la metrica disforme. En ese caso, Postulado 3'
permanece fenomenologico hasta encontrar otra dinamica microscópica.

Si pasa, el resultado habilita un experimento posterior con sprinkling
geométrico mas realista. No habilita por si solo claims cosmologicos.
