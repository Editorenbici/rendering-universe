# Roadmap Next 10 Days — Experimentos Formales

**Fecha:** 2026-07-03  
**Base:** index_master_2026-07-03.md + pre-regs committed.  
**Regla:** Todo committed pre-reg antes de run. Solo notes/ y code/analysis/ como necesario. Sin paper/.

---

## 1. Exp 24 (committed pre-reg → run)

- **Estado actual:** Background results + JSON disponible (epsilon scaling confirma ε_link <<1, v_link ~ área con error decreciente). Pre-reg en exp24_prereg (Codex) + results md.
- **Acción:** Commit formal del pre-reg si no está (o sync a main notes/). Correr el script 24_epsilon_link_scaling.py con la grilla completa (rhos, Rs, dims, n_real suficientes para stats).
- **Entregables esperados:** JSON full + summary + update a symbol_table (ya tiene benchmarks parciales). Validar contra convención [R]=1 y ε_link fracción.
- **Riesgos:** Background no es pre-reg; debe auditoría antes de claims.
- **Timeline:** 1-2 días (run + análisis).

## 2. Exp 22 (committed pre-reg → run)

- **Estado actual:** Pre-reg completo en exp22_prereg_outline (grilla, observables ℓ_max/N_m/ε_link/v_link, métricas Δd/Z_sep, criterios S/F, baselines BB/BK/GS). Referee questions listas. Diseño: sprinkling sesgado (b bias hacia anchura cerca de masa), medir h(x) ∝ R^{-1}, w(x) ∝ R^{+3} con mismo R de links.
- **Acción:** Sync outline a main si necesario. Correr script de sprinkling sesgado (basado en 18a/inhomogéneo + bias param). Comparar contra homogéneo GS y box-order BB.
- **Entregables:** Datos de abundances, altura/anchura vs R, tests vs baselines, update a inhomogeneous_box_orders.md y pre-reg.
- **Riesgos:** Sesgo debe ser pre-registrado exactamente; no mezclar con claims de R dinámica.
- **Timeline:** 2-4 días (implement bias + runs + comparación).

## 3. Lo que siga (decidido: factor 1/2 + atrición Exp 17)

- **Decisión:** Siguiente es extensión de Exp 17 (atrition/stacking pipeline) con factor 1/2 (probablemente corrección o normalización en conteo de links/potencial, ver history de 1/2 C en Johnston 2D y kernel).
  - Razón: Exp 17 tiene pipeline de stacking ISW/atrition ya en RESULTS_17*.md y 17_isw_stacking_pipeline.py. Integrar factor 1/2 para consistencia con kernels 2D/4D y validar contra atrición (descartes >30% mask).
  - Alternativa (factor 1/2 puro) menos prioritaria que cerrar atrición + pre-reg.
- **Acción:** 
  - Commit pre-reg para "Exp 17+ factor 1/2 + atrición".
  - Correr/actualizar 17_isw_stacking_pipeline.py con factor explícito.
  - Medir impacto en delta T / ISW signal y falsificación (ya ~13σ en history).
  - Update a pre_domingo_checks y symbol table si introduce nuevos observables.
- **Entregables:** Updated pipeline + resultados con/ sin factor + análisis de atrición bias.
- **Timeline:** 3-5 días después de Exp 22 (priorizar cerrar 24 y 22 primero).
- **Riesgos:** Atrición ya identificada como issue (mask >30% descartes); factor 1/2 debe justificarse contra Johnston/Sorkin para no introducir bias ad-hoc.

---

**Orden general:** Exp 24 → Exp 22 → Exp17+factor1/2. Mantener pre-regs actualizados en index_master. Auditoría Fable domingo antes de runs mayores. Re-evaluar después de cada (usar pre_domingo_checks como template).

**Próximos después de estos:** Dependiente de resultados (posible Exp 18d finite-size o new inhomogeneous con curvatura). Actualizar este roadmap post-auditoría.

Mantener solo en notes/. Listo para Codex.