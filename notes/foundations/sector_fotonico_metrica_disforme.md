# El sector fotónico: por qué la métrica conforme no desvía la luz y cuál es la enmienda mínima

**Nota técnica (no especulativa). Para revisión del autor.**
Preparada por Fable, 2026-07-04. Objetivo: cerrar la enmienda al
Postulado 3 (métrica efectiva).

---

## 1. El problema, con números

La métrica efectiva actual es conforme:
$$g_{\mu\nu} = (\ell_P/\mathcal{R})^2\,\eta_{\mu\nu}.$$

Teorema estándar: las geodésicas nulas son invariantes bajo
transformaciones conformes. Consecuencia directa: en este marco la luz
viaja en línea recta del canvas — **cero deflexión gravitacional, cero
lensing, cero retardo de Shapiro**.

En lenguaje PPN, linearizando con $\psi=\ln(\mathcal{R}/\bar{\mathcal{R}})
= -\Phi/c^2$ (convención validada: ψ>0 cerca de masa):

| Componente | GR (γ=1) | Render conforme |
|---|---|---|
| $g_{tt}$ | $-(1-2\psi)$ | $-(1-2\psi)$ ✓ |
| $g_{ij}$ | $+(1+2\psi)\,\delta_{ij}$ | $+(1-2\psi)\,\delta_{ij}$ ✗ |

El sector temporal está bien (por eso Pound-Rebka y los Exps 12–13
pasaron: órbitas newtonianas y relojes solo ven $g_{tt}$). El sector
espacial tiene el **signo opuesto**: $\gamma_{\rm Render} = -1$.

- Deflexión de luz $\propto(1+\gamma)/2 = 0$. Falsificado desde
  Eddington 1919.
- Shapiro/Cassini: $\gamma - 1 = (2.1\pm2.3)\times10^{-5}$ medido;
  el conforme se desvía en $|\gamma-1| = 2$: excluido por un factor
  $\sim10^5$.

## 2. La enmienda mínima (disforme)

Lo que GR exige en campo débil es que tiempo y espacio respondan en
sentidos OPUESTOS al potencial. La enmienda mínima al Postulado 3:

$$ds^2 = -e^{-2\psi}\,c^2dt^2 + e^{+2\psi}\,d\mathbf{x}^2$$

equivalentemente, en forma disforme covariante con $u_\mu$ el campo de
observadores del render (la foliación que $\mathcal{R}(t)$ ya define):

$$g_{\mu\nu} = e^{2\psi}\,\eta_{\mu\nu} - 2\sinh(2\psi)\,u_\mu u_\nu
\;\xrightarrow{\text{lineal}}\; e^{2\psi}\eta_{\mu\nu} - 4\psi\,u_\mu u_\nu.$$

**Lectura Render natural:** cerca de masa (ℛ alto), los relojes marcan
$d\tau = dt/\mathcal{R}_{\rm rel}$ (más lento ✓ ya validado) y las
reglas miden $d\ell = \mathcal{R}_{\rm rel}\,dx$ (distancias propias
MÁS largas: más píxeles por intervalo de canvas). La versión conforme
asumía que tiempo y espacio se re-escalan juntos; la física dice que la
resolución **convierte profundidad temporal en extensión espacial** —
responden inversamente. Un pixel más fino = tick más lento Y regla más
densa.

Con esto, $\gamma = 1$ por construcción: deflexión de Eddington,
lensing y Shapiro correctos al orden lineal.

## 3. Qué NO cambia (verificado)

- **Exps 12–13 (links → Newton):** intactos. Validaron el sector
  $g_{tt}$/masivo, que la enmienda no toca.
- **Pound-Rebka / dilatación:** intacta (mismo $g_{tt}$).
- **Sector cosmológico (Exp 15):** el fit de β usó FRW estándar para
  los observables; el fondo homogéneo absorbe $\bar\psi$ en la
  redefinición del factor de escala. Sin cambios.

## 4. Restricciones que la enmienda satisface o hereda

| Test | Estado |
|---|---|
| Cassini ($\gamma=1\pm2.3\times10^{-5}$) | ✓ por construcción (lineal) |
| GW170817 ($c_{GW}=c$ a $10^{-15}$) | ✓ **si la enmienda es universal** (fotones, gravitones y materia ven la MISMA g). Si solo los fotones vieran el término disforme, GW170817+Cassini lo excluirían. Se postula universal. |
| Perihelio de Mercurio (PPN β) | **ABIERTO**: β=1 requiere los términos O(ψ²), que esta enmienda lineal no fija. Trabajo pendiente. |
| Nordtvedt/equivalencia fuerte | Abierto (depende de los O(ψ²)). |

## 5. El costo conceptual (dicho de frente)

Con el término disforme, los conos de luz de $g$ **ya no coinciden**
con los del canvas η. Muere la identidad ingenua "estructura causal
efectiva = estructura causal del canvas" — y tenía que morir: esa
identidad ES la afirmación de que la luz no se curva. El ingrediente
estructural nuevo es $u_\mu$ (el frame del render). No es ad-hoc dentro
del marco: $\mathcal{R}(t)$ ya define una foliación preferida (como el
frame del CMB), y el lema 18a le da un candidato microscópico concreto
— $u_\mu \propto \partial_\mu(\text{profundidad de cadena})$, el
gradiente de la altura del poset, que es exactamente la cantidad
"local, por elemento" del sector refinamiento.

## 6. Problema abierto que esta nota define (para el registro)

Derivar la respuesta ANISÓTROPA (tiempo ~ 1/ℛ, espacio ~ ℛ) desde el
conteo del conjunto causal. Pista direccional: en un poset sprinkleado,
los estimadores de duración temporal (cadenas largas, Brightwell-
Gregory) y de distancia espacial (construcciones sobre anticadenas)
escalan con potencias distintas del conteo local — es concebible que la
dupla (1/ℛ, ℛ) emerja de esa asimetría cadena/anticadena. Nadie lo ha
calculado. Sería el "Exp 20-teórico" natural.

---

**Estado:** técnica, lista para revisión del autor. Cierra la enmienda
al Postulado 3 al orden lineal; deja explícitos los O(ψ²) y la
derivación microscópica como abiertos.

---

## Adenda: el constraint GW170817 (2026-07-06, de la búsqueda de Grok)

**|c_GW − c_γ|/c ≲ 6×10⁻¹⁵** (GW170817+GRB170817A; Sakstein PRL 119
251303, DOI verificado). Mata la mayoría de los acoplamientos
disformes de dark energy PORQUE en esas teorías el campo escalar
acopla disformemente a la materia pero NO (o distinto) a la gravedad
→ fotones y gravitones ven métricas distintas → velocidades distintas.

**Requisito de diseño para 3′ (se registra como constraint, no como
logro):** en Render la métrica disforme no es un acoplamiento de un
campo extra — es LA métrica efectiva del conteo, la misma para todo
lo que se propaga. Si fotones y gravitones ven la MISMA métrica
efectiva, c_GW = c_γ automáticamente y GW170817 se satisface por
construcción. Esto es una restricción sobre cualquier completación
futura del postulado: **prohibido introducir sectores que vean
métricas distintas**. Si alguna versión covariante de 3′ (borrador
Hermes, en pausa) genera birrefringencia gravitacional, ese es su
falsador inmediato — a 10⁻¹⁵, sin apelación.
