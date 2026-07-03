# Pre-registro Exp 22 — intervalos Bollobás-Brightwell / Boguñá-Krioukov

Fecha: 2026-07-03  
Estado: pre-registro completo en borrador. No correr nada antes de auditoría.  
Convención fija:

\[
[\mathcal R]=1.
\]

La eficiencia de links se define únicamente como fracción operacional:

\[
\epsilon_{\rm link}
\equiv
\frac{\langle N_{\rm links}\rangle}{\langle N_{\rm past}\rangle}.
\]

La valencia/abundancia de links se reporta por separado:

\[
v_{\rm link}\equiv\langle N_{\rm links}\rangle.
\]

---

## 1. Pregunta específica

¿Las estadísticas de intervalos de un causal set sprinklado recuperan las
leyes geométricas esperadas para intervalos manifold-like, y distinguen esos
intervalos de órdenes aleatorios/no geométricos?

El Exp 22 compara tres clases de observables:

1. Longitud de cadena máxima en intervalos.
2. Abundancias internas de intervalos/links.
3. Distancias geométricas cuando hay embedding disponible.

Referencias matemáticas de orientación:

- Bollobás-Brightwell: longest chains / height en órdenes aleatorios
  geométricos.
- Boguñá-Krioukov: reconstrucción/distancias en redes geométricas o
  hiperbólicas.
- Glaser-Surya: abundancias de intervalos \(N_m\) en causal sets
  manifold-like.

Estas referencias son baseline matemático. No se declara conexión física con
\(\mathcal R\) en este experimento.

---

## 2. Hipótesis nula

\[
H_0:
\]

Las estadísticas de intervalos medidas no distinguen de forma robusta entre
un sprinkling manifold-like y un orden aleatorio/no geométrico con el mismo
número de elementos.

Operacionalmente, \(H_0\) pasa si:

1. La dimensión inferida por cadenas no recupera la dimensión de embedding.
2. Las abundancias \(N_m\) no se separan del control no geométrico.
3. La eficiencia \(\epsilon_{\rm link}\) no muestra patrón reproducible entre
   geometrías.

---

## 3. Hipótesis alternativa

\[
H_1:
\]

Las estadísticas de intervalos sí recuperan estructura geométrica:

1. La longitud de cadena máxima escala como una potencia compatible con la
   dimensión de embedding.
2. Las abundancias \(N_m\) reproducen el baseline Glaser-Surya cuando se mide
   el mismo objeto.
3. \(\epsilon_{\rm link}\) y \(v_{\rm link}\) separan manifold-like de órdenes
   no geométricos en la grilla pre-registrada.

---

## 4. Datos necesarios

Para cada realización:

1. Lista de elementos.
2. Relación causal \(x\prec y\), como matriz booleana o lista de pares.
3. Relación de links \(x\prec^\ast y\), como transitive reduction o cálculo
   explícito de ausencia de intermediarios.
4. Si hay embedding:
   - coordenadas;
   - dimensión;
   - separación temporal/espacial;
   - distancia geodésica esperada o aproximada.
5. Para cada intervalo seleccionado \([x,y]\):
   - cardinalidad \(N_{\rm interval}\);
   - longitud de cadena máxima \(\ell_{\max}(x,y)\);
   - número de links internos;
   - \(N_m\), abundancias de subintervalos de cardinalidad \(m\), para un
     rango pequeño predefinido de \(m\).

---

## 5. Grilla pre-registrada

Dimensiones:

\[
d\in\{2,4\}.
\]

Tamaños aproximados:

\[
N\in\{256,512,1024\}
\]

por realización, sujeto a memoria/tiempo.

Realizaciones:

\[
N_{\rm real}=32
\]

por punto de grilla para el primer run.

Intervalos muestreados:

\[
N_{\rm intervals}=200
\]

por realización, elegidos uniformemente entre pares causales válidos,
descartando intervalos con cardinalidad menor que 8.

Controles:

1. Sprinkling plano manifold-like.
2. Orden aleatorio/no geométrico con el mismo \(N\).
3. Si existe en código local: diamante causal 4D compatible con
   `23_glaser_surya_check.py`.

---

## 6. Observables

### O1. Longitud de cadena máxima

\[
\ell_{\max}(x,y).
\]

Ajuste:

\[
\ell_{\max}
\sim
C_d\,N_{\rm interval}^{1/d_{\rm eff}}.
\]

Se reporta \(d_{\rm eff}\).

### O2. Abundancias \(N_m\)

Para cada intervalo \([x,y]\), medir:

\[
N_m([x,y])
=
\#\{\text{subintervalos internos con cardinalidad }m\}.
\]

Rango pre-registrado:

\[
m\in\{0,1,2,3\}.
\]

Aquí \(m=0\) corresponde a links/covers.

### O3. Valencia y eficiencia de links

\[
v_{\rm link}
=
\langle N_{\rm links}\rangle,
\]

\[
\epsilon_{\rm link}
=
\frac{\langle N_{\rm links}\rangle}
{\langle N_{\rm past}\rangle}.
\]

Ambos se reportan. Solo \(\epsilon_{\rm link}\) es una fracción.

### O4. Distancia geométrica

Si el embedding está disponible, comparar:

\[
\ell_{\max}
\]

contra separación temporal/geodésica esperada. Este observable es secundario
si el embedding no está disponible para todos los controles.

---

## 7. Métricas de comparación

M1. Error relativo de dimensión:

\[
\Delta_d
=
\frac{|d_{\rm eff}-d|}{d}.
\]

M2. Separación entre clases:

\[
Z_{\rm sep}
=
\frac{|\mu_{\rm manifold}-\mu_{\rm control}|}
{\sqrt{\sigma_{\rm manifold}^2+\sigma_{\rm control}^2}}.
\]

M3. Compatibilidad con Glaser-Surya:

Para geometrías donde se reproduzca exactamente su objeto \(N_m\), reportar
desviación en unidades de error combinado.

M4. Robustez de \(\epsilon_{\rm link}\):

Reportar si \(\epsilon_{\rm link}\) permanece en

\[
0<\epsilon_{\rm link}<1
\]

y si cambia sistemáticamente entre clases.

---

## 8. Criterios de éxito

S1. En sprinklings planos, la dimensión inferida cumple:

\[
\Delta_d<0.20
\]

para \(d=2\) y \(d=4\).

S2. El control manifold-like y el control no geométrico se separan en al
menos un observable primario con:

\[
Z_{\rm sep}>3.
\]

S3. Para el caso que reproduzca el setup Glaser-Surya, \(N_0\) queda dentro
de \(2\sigma\) del baseline ya validado por el pipeline local.

S4. La eficiencia de links está bien definida:

\[
0<\epsilon_{\rm link}<1
\]

en todos los puntos reportados.

S5. Los resultados son estables al duplicar \(N\) dentro de los errores del
run.

---

## 9. Criterios de falla

F1. \(d_{\rm eff}\) no recupera \(d=2\) o \(d=4\):

\[
\Delta_d\ge0.20.
\]

F2. No hay separación entre manifold-like y control:

\[
Z_{\rm sep}\le3
\]

para todos los observables primarios.

F3. \(N_0\) discrepa del baseline Glaser-Surya por más de \(2\sigma\) en el
setup comparable.

F4. \(\epsilon_{\rm link}\) sale fuera de rango:

\[
\epsilon_{\rm link}\le0
\quad \text{o}\quad
\epsilon_{\rm link}\ge1.
\]

F5. Los resultados cambian sistemáticamente al duplicar \(N\), sin tendencia
clara de convergencia.

---

## 10. Interpretación pre-registrada

Si S1-S5 pasan:

El conjunto de observables de intervalos sirve como baseline geométrico para
clasificar causal sets manifold-like y puede usarse como herramienta de
diagnóstico en experimentos posteriores.

Si S1 pasa pero S2 falla:

Las cadenas recuperan dimensión, pero no bastan para clasificar geometría;
se requieren observables adicionales.

Si S3 falla:

El pipeline no está reproduciendo el objeto Glaser-Surya correcto; no se debe
usar Exp 22 para claims.

Si F4 falla:

La definición de \(\epsilon_{\rm link}\) está mal normalizada o no aplica a
esta clase de intervalos.

Si F5 falla:

El experimento queda dominado por tamaño finito; se debe abrir una extensión
con finite-size scaling antes de interpretar.

---

## 11. No hacer en este experimento

1. No inferir dinámica de \(\mathcal R\).
2. No conectar con BAO/SNe.
3. No usar \(\epsilon_{\rm link}\) como \(G_{\rm eff}\).
4. No declarar nueva física.
5. No mezclar con Exp 24.

Exp 22 es un test geométrico/estadístico de intervalos, no una medición
cosmológica.
