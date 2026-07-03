# Preguntas referee específicas para Exp 22 (pre-reg)

**Fecha:** 2026-07-03  
**Contexto:** Exp 22 — sprinkling Poisson con inserción sesgada / inhomogeneous box orders (sesgo variable, densidad inhomogénea, comparación de abundances de intervalos / valencia vs baselines).  
**Objetivo:** Pre-registrar contra literatura de random posets y geometría emergente.  
**No claims de novedad sin pre-reg + baselines.**

---

## 3 Preguntas Referee Específicas

1. **Sobre confusión con modelos combinatorios de posets aleatorios (Bollobás-Brightwell):**  
   Dado que los "box orders" inhomogéneos de Bollobás-Brightwell (Trans. AMS 1991) ya predicen distribuciones específicas para el tamaño de intervalos en posets aleatorios generados por procesos de Poisson en box-spaces (con volúmenes de intervalos distribuidos según la medida del box), ¿cómo distinguirá experimentalmente el Exp 22 un "efecto geométrico" del sesgo FRW-transitorio de un simple "random poset sesgado" sin estructura Lorentziana? ¿Incluye el pre-reg un test estadístico que rechaza el modelo de box-space aleatorio (p. ej., usando la curva completa de abundances <N_m> vs m o el trade-off altura/anchura cuantitativo) a favor de la firma de sprinkling geométrico sesgado?

2. **Sobre la relación con estimadores de distancia en CST (Boguñá-Krioukov 2024):**  
   Boguñá-Krioukov (arXiv:2401.17376) muestran que el "causal overlap" (tamaño del pasado común o futuro común) permite estimar distancias espaciales en causal sets sprinkled, con error que desaparece en el límite continuo incluso a escalas Planck. En un sprinkling inhomogéneo (densidad variable), el overlap entre pares space-like se verá afectado por el sesgo local de densidad. ¿El Exp 22 mide también overlaps o sólo abundances puras de intervalos? Si sólo abundances, ¿cómo se justifica que la desviación observada en <N_m> no es simplemente un artefacto del overlap variable que el método de Boguñá-Krioukov ya predice y corrige? ¿Se incluye un baseline donde se aplica el estimador de distancia por overlap y se verifica si "recupera" una geometría efectiva a pesar del sesgo?

3. **Sobre diferenciación de Glaser-Surya 2013 en régimen inhomogéneo:**  
   Glaser & Surya (arXiv:1309.3403) dan fórmulas analíticas exactas para <N_m^d> en sprinklings Poisson homogéneos en intervalos de Minkowski, y usan la forma característica de la curva abundances vs m como test de "manifoldlikeness" y localidad. En el caso inhomogéneo (sesgo de densidad o cutoff variable tipo FRW transitorio), la curva se deformará. ¿El diseño de Exp 22 cuantifica explícitamente cómo se deforma la curva característica de Glaser-Surya bajo el sesgo (p. ej., shift del pico de m, cambio en la cola para m grande, o pérdida de la firma de dimensión d)? ¿Incluye un test que rechaza "es sólo un Glaser-Surya con densidad promedio" a favor de "el sesgo produce una firma nueva predecible por el modelo de box orders o por la geometría expandente"?

---

**Notas:**
- Estas preguntas están diseñadas para ser respondidas en el pre-reg y en el reporte de resultados (con figuras de curvas de abundances, tests estadísticos vs baselines, y límites de validez).
- Citar siempre:
  - Bollobás & Brightwell, Trans. Amer. Math. Soc. 324 (1991) 59–72 (box-spaces y random partial orders).
  - Boguñá, Krioukov et al., arXiv:2401.17376 (causal overlaps para distancias espaciales en CST).
  - Glaser & Surya, Phys. Rev. D 88, 124026 (2013) (abundances en sprinklings Minkowski y test de manifoldlikeness).
- Exp 22 debe pre-registrar contra estos tres, declarando explícitamente qué se espera diferente en el caso inhomogéneo geométrico vs combinatorio puro.

**Próximo:** Cuando aparezca notes/exp22_prereg_outline_2026-07-03.md, completar la sección de antecedentes literarios con los resúmenes detallados de estos tres y las diferencias.

DONE (preguntas referee listas).