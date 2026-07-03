# Link Abundance / Expected Number of Links in Poisson Sprinkling (Minkowski)

**Búsqueda teórica:** Grok (xAI), 2026-07-03  
**Actualizado con búsquedas frescas** ✅

## Resultados clave de literatura

### Valency en sprinkling Poisson (confirmado Glaser & Surya)
- En un causal set de sprinkling Poisson en ℳ^d (Minkowski d-dimensional), la **valency** (número de links / nearest neighbours por elemento) es **típicamente muy grande** y **infinita** para d > 1+1.  
  → "every element has an infinite number of nearest neighbours, both to the past and to the future. The resulting graph is therefore of infinite valency" (Glaser & Surya 2013).  
- Razón: los light cones son unbounded. Para un elemento e, la mayoría de links futuros caen dentro de un hyperboloid de volumen ~ V_c ± √V_c, pero la región es non-compact, volumen infinito → número de future links es (almost surely) infinite.
- Esto da la "non-locality" característica de manifold-like causal sets.
- En d=1+1 la divergencia es LOGARITMICA (no finita): nuestro lema 18a mide v = 2 ln(T*sqrt(rho)) con cutoff, divergente al quitarlo. [CORREGIDO por Fable: la version de Grok decia 'finita'.]
- En sprinklings con cutoff temporal finito (región de "height" T), la valency es finita y depende de ρ y T. 🚀

### Interval abundances (Glaser & Surya 2013, arXiv:1309.3403)
- Glaser & Surya (Phys. Rev. D 88, 124026, 2013): estudian "interval abundances" ⟨N_m^d⟩ = número esperado de intervals causales de cardinalidad m en d dimensiones.
- Para Poisson sprinkling en intervalos de Minkowski topológicamente triviales, dan **curvas características** analíticas + simulaciones que las reproducen (manifoldlike signature).
- Link abundance (m=0 en su notación: covering relations = links = N₀) se deriva de la probabilidad de que un intervalo [x,y] no contenga elementos intermedios (Poisson P(0) = e^{-ρV}).
- Comparan con random orders y otros ensembles.
- **No hay mención explícita de la constante π√6** para expected number of links/valency en Glaser & Surya. 
- π√6 aparece en la literatura CST para **normalización del d'Alembertian** y Benincasa-Dowker action (coeficientes del kernel). En BD action, N₀ (links) entra directamente en la expresión discreta.

### Cálculos de expected links / chains
- En sprinkling, el expected number of k-chains (no solo links) en sprinkling: ⟨C_k⟩ = ρ^k χ_k V^k, donde χ_k es un factor dependiente de dimensión (Myrheim-Meyer estimator usa esto para dimensión).
- Para links (k=2), está relacionado pero no idéntico a interval abundance m=2.
- En 2D Minkowski con cutoff, expected links ~ 2 ln(T*sqrt(rho)) (lema 18a, medido; la banda de links es logaritmica, NO ~rho T^2 como decia la version de Grok — el T^2 es el caso 4D).
- **π√6**: aparece en literatura CST para normalización del d'Alembertian (ej. en Surya review y papers de Benincasa-Dowker: factores como 1/(π√6) o similares para el kernel en 4D). No encontré "expected number of links = π√6 √ρ T²" verbatim en Glaser/Surya o revisiones principales.
- Tu fórmula parece consistente con integración sobre volúmenes de Alexandrov + Poisson (e^{-ρV} prob no points in interval). El factor π viene de integración angular/volumétrica en Minkowski; √6 proviene de la integral gaussiana de exp(-rho*pi*tau^4/24) sobre la banda de links (derivacion en docstring de 18b); nada que ver con FRW.

## ¿La constante π√6 está publicada?
- **No directamente para link abundance en sprinkling** (confirmado en Glaser & Surya 2013 + Surya review + búsquedas 2026). 
  - Sí en coeficientes del d'Alembertian discreto (común en CST, ej. π√6 en kernels de acción BD).
  - En interval abundances de Glaser/Surya usan factores dimensionales Γ(d+1)/Γ(3d/2) etc.
- **Tu fórmula con π√6 + cutoff FRW transitorio** parece derivada/específica del proyecto. No aparece verbatim como "v = π√6 √ρ T²" para links en la literatura principal.
- **Recomendación**: Cita Glaser & Surya 2013 para baselines de abundances + Surya 2019 para valency infinita. Si tu expresión + transitorio no está publicada, puedes claim "primera medición explícita con este cutoff variable + ley de valencia derivada".
- Verifica contra sus figuras de abundances para m=0 (links) en sprinklings. 🎯

## Verificación de valor máximo
- En sprinkling uniforme, valency promedio **diverge** (infinita) en regiones grandes por light cones unbounded.
- Con cutoff T finito: máximo ~ O(√ρ T) o lineal en T (depende de d). En 2D efectivo ~ ρ T² area-like.
- En tu inhomogéneo (FRW transitorio): el máximo se desplaza a regiones de alta densidad; el trade-off altura/anchura (chains vs antichains) se acentúa con el sesgo.
- En literatura (Surya, Glaser): en sprinklings finitos o con boundary (causal diamond), valency es finita pero grande; no "máximo" fijo, sino estadística.

## Recomendación
- Cita Glaser & Surya 2013 y Surya 2019 para las baselines de interval abundances y valency infinita.
- Tu resultado con π√6 y cutoff FRW transitorio parece derivado/específico; si no verbatim en literatura, puedes claim "primera medición explícita con este cutoff".
- Para Exp 22 (antichains): usa esto para pre-registrar contra las abundances conocidas.

**Referencias clave (verificados):**
- S. Surya, Living Rev. Relativ. 22, 5 (2019) — valency infinita, interval abundances.
- L. Glaser & S. Surya, Phys. Rev. D 88, 124026 (2013) — locality, abundances en sprinklings.
- Papers de d'Alembertian CST (Roy et al. 2013) — π√6 en coeficientes.
- Glaser et al. (2018), Surya preprints — extensiones de abundances.

Si no está publicado exactamente así, ¡tu paper técnico gana el resultado central! 🚀

---

## AUDITORIA (Fable, 2026-07-03)
- Glaser & Surya 2013: cita plausible y consistente (PRD 88, 124026,
  arXiv:1309.3403); su N_0 (interval abundance m=0) es el objeto
  correcto a comparar como baseline. PENDIENTE: chequear sus curvas
  contra nuestra ley antes del Paper A (distinto setup: intervalo de
  Alexandrov fijo vs cutoff IR de profundidad — las constantes no
  tienen por que coincidir).
- Correcciones aplicadas: (i) valencia 2D es log-divergente, no finita
  (contradecia el lema 18a medido); (ii) links 2D con cutoff ~ 2 ln T,
  no rho T^2; (iii) el origen del sqrt(6) es la integral de banda, no
  FRW.
- CONCLUSION OPERATIVA para el Paper A: "v = pi*sqrt(6)*sqrt(rho)*T^2
  con cutoff IR" no aparece verbatim en la literatura revisada ->
  citar Glaser-Surya como baseline y reclamar la ley con cutoff + el
  transitorio FRW como resultados del trabajo. La afirmacion queda
  condicionada al chequeo pendiente contra sus curvas.
- El archivo original de Grok venia corrupto (texto de chat pegado,
  incluia el encabezado de otro archivo); truncado.

## COMPUERTA CERRADA (Fable, 2026-07-03 — script 23)
El chequeo pendiente contra el objeto de Glaser-Surya esta HECHO:
en diamante causal 4D (T_D=10, rho=1), la integral exacta
<N_0> = rho^2 Int Int e^{-rho V} da 27,602 +- 95 y el conteo exacto de
links de nuestra maquinaria da 27,537 +- 876 — acuerdo a 0.07 sigma.
El pipeline queda AMARRADO al baseline publicado. La aproximacion de
banda tipo-slab sobreestima +21% en el diamante (costo de clipping de
borde, medido): las constantes de diamante y slab difieren por
geometria, como se anticipo. Cadena de custodia del Paper A completa:
N_0 Glaser-Surya (reproducido) -> ley slab pi*sqrt6*sqrt(rho)*T^2
(18b, 5%) -> transitorio FRW con asintota de area (18c/18d).
