# Simbolos nuevos - Opcion D

Fecha: 2026-07-03  
Estado: BORRADOR tecnico interno. No usar en `paper/` sin auditoria.

Objetivo: definir dos simbolos auxiliares que separan dinamica global de
resolucion y geometria local de links:

\[
\mathcal J_R = v_R\,\epsilon_{\rm link},
\qquad
N_c(x,r)=|\{y\in {\rm Past}(x):\tau(x,y)<r\}|.
\]

Convenciones:

- \([\mathcal R]=1\).
- \(v_R=d\mathcal R/dt\), por lo tanto \([v_R]=T^{-1}\).
- \(\epsilon_{\rm link}=\langle N_{\rm links}\rangle/
  \langle N_{\rm past}\rangle\), por lo tanto
  \([\epsilon_{\rm link}]=1\).
- \(r\) es una escala de tiempo propio o longitud causal, segun unidades.

---

## 1. \(\mathcal J_R\): resolution flux density

### Definicion formal

\[
\mathcal J_R
\equiv
v_R\,\epsilon_{\rm link}
=
\frac{d\mathcal R}{dt}\,
\frac{\langle N_{\rm links}\rangle}
{\langle N_{\rm past}\rangle}.
\]

Si se usa la convencion temporal del proyecto,

\[
\beta_t\equiv\frac{d\ln\mathcal R}{d\ln t},
\]

entonces

\[
v_R=\frac{\beta_t\mathcal R}{t},
\qquad
\mathcal J_R
=
\frac{\beta_t\mathcal R}{t}\,
\epsilon_{\rm link}.
\]

Si se usa la convencion alternativa
\(\beta_a=d\ln\mathcal R/d\ln a\), entonces

\[
v_R=\beta_a H\mathcal R,
\qquad
\mathcal J_R=\beta_a H\mathcal R\,\epsilon_{\rm link}.
\]

No mezclar ambas betas sin subindice.

### Analisis dimensional

\[
[\mathcal R]=1,
\qquad
[v_R]=T^{-1},
\qquad
[\epsilon_{\rm link}]=1,
\qquad
[\mathcal J_R]=T^{-1}.
\]

Entonces \(\mathcal J_R\) no es una densidad espacial en esta definicion
minimal; es una tasa efectiva de refinamiento que sobrevive el filtro de
links. Si se quisiera una densidad por volumen, haria falta definir

\[
j_R\equiv \rho_s\,\mathcal J_R,
\]

con \([j_R]=L^{-d}T^{-1}\) en \(d\) dimensiones espaciales/causales
efectivas.

### Rango esperado

Como

\[
0\le\epsilon_{\rm link}\le1,
\]

se espera

\[
0\le \mathcal J_R\le v_R
\]

si \(v_R\ge0\). Si el modelo permite coarse-graining o perdida de
resolucion, \(v_R<0\), entonces

\[
v_R\le \mathcal J_R\le0.
\]

En el uso cosmologico normal, donde \(\mathcal R\) crece,
\(\mathcal J_R\) deberia ser positiva.

### Como se mediria

1. Estimar \(v_R\) desde una parametrizacion cosmologica de
   \(\mathcal R(t)\), por ejemplo via \(\beta_t\):

\[
v_R=\frac{\beta_t\mathcal R}{t}.
\]

2. Medir \(\epsilon_{\rm link}\) en sprinklings:

\[
\epsilon_{\rm link}
=
\frac{\langle N_{\rm links}\rangle}
{\langle N_{\rm past}\rangle}.
\]

3. Multiplicar ambas cantidades:

\[
\mathcal J_R=v_R\epsilon_{\rm link}.
\]

Este simbolo combina dos niveles distintos: dinamica global de resolucion y
geometria local del poset. Por eso debe tratarse como variable diagnostica,
no como ley fundamental.

### Analogia matematica pura

\(\mathcal J_R\) es como una derivada filtrada: primero se mide la tasa de
cambio y luego se proyecta sobre el subespacio de relaciones irreducibles.

### Analogia fisica concreta

\(\mathcal J_R\) es como una tasa de conteo efectiva en un detector: eventos
por segundo antes del filtro, multiplicados por la eficiencia del filtro.

---

## 2. \(N_c(x,r)\): causal neighborhood function

### Definicion formal

\[
N_c(x,r)
\equiv
\left|
\{y\in{\rm Past}(x):\tau(x,y)<r\}
\right|.
\]

Aqui \(\tau(x,y)\) es la distancia temporal propia entre \(y\) y \(x\), solo
definida para pares timelike dentro del pasado causal. En una version
discreta pura, \(\tau\) puede reemplazarse por una distancia de cadena
calibrada:

\[
\tau(x,y)\ \longrightarrow\ \alpha_d\,\ell_s\,L_{\rm chain}(y,x),
\]

donde \(L_{\rm chain}\) es la longitud de la cadena maxima entre \(y\) y
\(x\), \(\ell_s\) es la escala de sprinkling, y \(\alpha_d\) es el factor de
calibracion dimensional.

### Analisis dimensional

\[
[N_c]=1,
\qquad
[r]=T
\]

si \(c=1\). En unidades SI, \(r\) puede escribirse como tiempo propio o como
longitud causal \(cr\).

Para sprinkling Poisson homogeneo,

\[
\mathbb E[N_c(x,r)]
=
\rho_s\,V_d(r),
\]

donde \(V_d(r)\) es el volumen del diamante/pasado truncado por
\(\tau<r\), segun la geometria de la ventana.

En 4D plano, para un intervalo causal completo de altura \(r\),

\[
V_4(r)\propto r^4.
\]

El coeficiente exacto depende de si se cuenta el diamante completo, solo el
pasado truncado, o una ventana slab/cilindrica.

### Rango esperado

\[
N_c(x,r)\in\{0,1,2,\ldots,N_{\rm past}(x)\}.
\]

Propiedades esperadas:

1. Monotonia:

\[
r_1<r_2
\quad\Rightarrow\quad
N_c(x,r_1)\le N_c(x,r_2).
\]

2. Limite pequeno:

\[
\lim_{r\to0}N_c(x,r)=0
\]

casi seguramente en un sprinkling Poisson continuo.

3. Saturacion:

\[
\lim_{r\to r_{\rm max}}N_c(x,r)=N_{\rm past}(x)
\]

dentro de una ventana finita.

### Como se mediria

1. Generar o cargar un causal set con relacion causal \(\prec\).
2. Para cada elemento \(x\), construir su pasado:

\[
{\rm Past}(x)=\{y:y\prec x\}.
\]

3. Estimar \(\tau(x,y)\):
   - por coordenadas de embedding si estan disponibles;
   - por longitud de cadena maxima si se trabaja solo con el poset.
4. Contar los elementos con \(\tau(x,y)<r\).
5. Promediar:

\[
\langle N_c(r)\rangle_x
=
\frac1N\sum_x N_c(x,r).
\]

El observable derivado util es la pendiente logaritmica:

\[
d_{\rm eff}(r)
=
\frac{d\ln\langle N_c(r)\rangle}{d\ln r},
\]

que puede funcionar como estimador local de dimension efectiva.

### Analogia matematica pura

\(N_c(x,r)\) es una funcion de crecimiento de bola, pero la bola esta
definida por el orden causal y no por una metrica euclidiana.

### Analogia fisica concreta

\(N_c(x,r)\) es como contar cuantos eventos podrian haber influido en un
detector dentro de una ventana de tiempo propio \(r\).

---

## 3. Relacion entre ambos simbolos

\(N_c(x,r)\) mide disponibilidad causal cruda:

\[
N_c \sim N_{\rm past}(r).
\]

\(\epsilon_{\rm link}\) mide que fraccion de esa disponibilidad sobrevive
como relacion irreducible:

\[
\epsilon_{\rm link}(r)
=
\frac{\langle N_{\rm links}(r)\rangle}
{\langle N_c(r)\rangle}.
\]

Entonces puede escribirse una version local de \(\mathcal J_R\):

\[
\mathcal J_R(x,r)
=
v_R(x)\,
\frac{N_{\rm links}(x,r)}{N_c(x,r)}.
\]

Esta forma es util para simulaciones, pero introduce dos dependencias
adicionales: posicion \(x\) y escala de vecindad \(r\). La version global
\(\mathcal J_R=v_R\epsilon_{\rm link}\) debe entenderse como promedio o
coarse-graining de esta expresion local.

---

## 4. Riesgos de notacion

1. No llamar a \(\mathcal J_R\) "energia" ni "flujo fisico" sin una ley de
   conservacion asociada.

2. No llamar a \(N_c(x,r)\) "volumen" sin aclarar que es conteo discreto. El
   volumen continuo seria \(N_c/\rho_s\).

3. No confundir \(N_c(x,r)\) con \(N_{\rm links}\). El primero cuenta pasado
   causal bruto dentro de una ventana; el segundo cuenta relaciones
   irreducibles.

4. No usar \(v_R=\beta H\mathcal R\) salvo que \(\beta=\beta_a\). Para la
   beta temporal del proyecto:

\[
v_R=\frac{\beta_t\mathcal R}{t}.
\]

5. No presentar \(\mathcal J_R\) como variable fundamental antes de demostrar
   que mejora una prediccion o reduce ambiguedad operacional.
---

NO ENCONTRADO en literatura — definiciones propias del proyecto.
