# Ascensor: ℛ̈/ℛ como fuente de gravedad artificial

**Nota interna — no para el paper todavía**  
Autoría: Patricio Bustos + asistente  
Revisión CST: pendiente de Fable  
Fecha: 2026-07-02

---

## La analogía

En GR, un ascensor que acelera hacia arriba en Minkowski genera un campo gravitatorio artificial hacia abajo: la métrica pasa de Minkowski a Rindler.

En Render, el "canvas" es Minkowski fijo (Postulado 1). Lo que cambia es la resolución del render, $\mathcal{R}(t)$. Si $\mathcal{R}$ crece exponencialmente, la métrica efectiva (Postulado 3) se convierte en:

$$g_{\mu\nu}^{(\text{eff})}(t) = \eta_{\mu\nu} \left(\frac{\ell_P}{\mathcal{R}(t)}\right)^2$$

con $\mathcal{R}(t) = \mathcal{R}_0 e^{Ht}$. Entonces:

$$g_{tt}^{(\text{eff})} = -\left(\frac{\ell_P}{\mathcal{R}_0}\right)^2 e^{-2Ht}$$

En coordenadas conformes, esto es **de Sitter conforme**. No es Rindler exacto, pero el parche estático de de Sitter cerca de su horizonte se parece a Rindler — un teorema real, no una reparametrización del tiempo. La termalidad de ese parche es exactamente **Gibbons-Hawking**, $T = \hbar H / 2\pi k_B$.

---

## Equivalencia

| GR (Einstein) | Render |
|:--------------|:-------|
| Ascensor acelera $\to$ gravedad artificial | $\mathcal{R}$ acelera $\to$ métrica conforme no-Minkowski |
| Métrica Rindler: $ds^2 = -(1+az/c^2)^2 c^2dt^2 + dx^2$ | Métrica Render: $ds^2 = -(\ell_P/\mathcal{R})^2 dt^2 + (\ell_P/\mathcal{R})^2 dx^2$ |
| Aceleración $a = \text{cte}$ | "Aceleración del render" $\ddot{\mathcal{R}}/\mathcal{R} = H^2 = \text{cte}$ |
| Temperatura de Unruh: $T_U = \hbar a / 2\pi k_B c$ | Temperatura de Gibbons-Hawking: $T_{GH} = \hbar H / 2\pi k_B$ |

El signo importa: cerca de masa, $\mathcal{R}$ sube $\to$ tiempo se frena (Pound-Rebka). Eso significa que el "piso" del ascensor es el lado de $\mathcal{R}$ **alto**. Si un void tiene $\mathcal{R}$ bajo, el tiempo pasa más rápido ahí → el observador en el void ve el entorno como "más ligero".

---

## Unruh desde $\mathcal{R}$

### 1. Versión homogénea / cosmológica

Si usamos $\ddot{\mathcal{R}}/\mathcal{R} = H^2$ (que tiene unidades $1/T^2$), la fórmula dimensionalmente correcta es:

$$T = \frac{\hbar}{2\pi k_B} \sqrt{\frac{\ddot{\mathcal{R}}}{\mathcal{R}}}$$

Esto es dimensionalmente exacto y coincide con la temperatura de Gibbons-Hawking para de Sitter. No necesita $\ell_P$ insertado a mano.

### 2. Versión inhomogénea / local

En un gradiente espacial de $\mathcal{R}$, la aceleración propia es $a_{\text{proper}} = c^2 \nabla \ln \mathcal{R}$. Entonces:

$$T = \frac{\hbar c}{2\pi k_B} |\nabla \ln \mathcal{R}|$$

Esta forma es la que conecta con la gravedad local (Postulado 6): con $\psi = \nabla \ln \mathcal{R}$, tenemos $a_{\text{proper}} = c^2 \psi = -\nabla \Phi$, que es la aceleración newtoniana exacta. Tu fórmula de Unruh-Render es el Unruh estándar de un observador estático en el campo gravitatorio, derivado desde $\mathcal{R}$.

**Caveat CST:** el vacío nativo de CST (Sorkin-Johnston) en de Sitter no es el Bunch-Davies térmico estándar — es un $\alpha$-vacuum. La respuesta térmica en el marco CST-nativo podría diferir de la estándar ([Aslanbeigi & Buck, arXiv:1306.3231](https://arxiv.org/pdf/1306.3231); [Surya et al., JHEP 07 (2019) 009](https://link.springer.com/article/10.1007/JHEP07(2019)009)).

---

## Predicción concreta

En un void profundo, $\mathcal{R}$ es menor que el promedio. Si $\mathcal{R}$ varía espacialmente, $\nabla \ln \mathcal{R}$ es no-cero. Un observador en el centro del void ve una temperatura tipo-Unruh apuntando **hacia afuera** (porque $\mathcal{R}$ aumenta al alejarse del centro).

**Magnitud con sector vivo:** con $|\psi| \sim 3\times10^{-6}$ del Exp 16 (sector vivo, no el déficit acumulado ISW):

$$\nabla \ln \mathcal{R} \sim \frac{3\times10^{-6}}{R_{\rm void}}$$

Para $R_{\rm void} \sim 20$ Mpc ($\approx 6.2\times10^{23}$ m):

$$\nabla \ln \mathcal{R} \sim 5\times10^{-30} \text{ m}^{-1}$$

$$T_U \sim \frac{1.05\times10^{-34} \text{ J s} \cdot 3\times10^8 \text{ m/s}}{2\pi \cdot 1.38\times10^{-23} \text{ J/K}} \cdot 5\times10^{-30} \text{ m}^{-1}$$

$$T_U \sim 3\times10^{-33} \text{ K}$$

Eso es 5 órdenes menos que la estimación anterior ($10^{-29}$ K). Igual de imedible, pero consistente con el sector vivo.

**Nota:** es la temperatura que vería un *detector ideal* en esa aceleración efectiva, no una emisión térmica del void.

---

## Signo revisitado

El signo del "peso" en el ascensor de $\mathcal{R}$:

| Región | $\mathcal{R}$ | Tiempo | "Abajo" del ascensor |
|:-------|:-------------|:-------|:---------------------|
| Cerca de masa | Alto | Lento | $\mathcal{R}$ alto |
| Void profundo | Bajo | Rápido | $\mathcal{R}$ bajo |
| Ascensor acelera hacia arriba | $\mathcal{R}$ sube | Localmente lento | Piso = $\mathcal{R}$ alto |

**Conclusión:** el piso del ascensor es el lado de $\mathcal{R}$ alto. Si el ascensor acelera hacia arriba, el observador siente que el "piso" está hacia donde $\mathcal{R}$ crece.

Esto es consistente con el signo ya verificado de Pound-Rebka: cerca de masa ($\mathcal{R}$ alto), los relojes van más lento.

---

## Tres errores de CST a evitar (checklist Fable)

1. **Signo:** no invertir el peso. $\mathcal{R}$ alto = reloj lento = "abajo" en el ascensor. (Ya nos quemamos con esto en Exp 09.)
2. **No mezclar sectores:** $\ddot{\mathcal{R}}/\mathcal{R}$ cosmológico (fondo) no produce gravedad *local*. La gravedad local es $\psi(x)$ del Postulado 6. La analogía es entre estructuras (parche de Sitter cerca del horizonte vs. métrica conforme de Render), no entre mecanismos.
3. **Citar Unruh:** el efecto Unruh en causal sets existe (Alkofer 2016, detector Unruh-DeWitt sobre vacío de Sorkin-Johnston). No inventar una versión propia sin citar.

---

## Estado

- Derivación corregida: usando $\sqrt{\ddot{\mathcal{R}}/\mathcal{R}}$ para la versión homogénea.
- Versión inhomogénea: $T = (\hbar c / 2\pi k_B) |\nabla \ln \mathcal{R}|$, consistente con Newton.
- Gibbons-Hawking insertado como cita ancla.
- Signo: consistente con Pound-Rebka.
- Predicción numérica corregida: $T_U \sim 3\times10^{-33}$ K en voids profundos (sector vivo, $|\psi|\sim3\times10^{-6}$).
- Próximo paso: revisión final de Fable contra los 3 checks.
