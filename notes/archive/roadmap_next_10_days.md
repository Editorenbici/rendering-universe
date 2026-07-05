# Roadmap Next 10 Days — Experimentos Formales

**Fecha:** 2026-07-03  
**Propósito:** Priorizar los próximos 3 experimentos formales post-auditoría de hoy. Basado en pre-regs committed.  
**Regla:** Todo con pre-reg auditado antes de run. Solo notes/ y code/analysis. Sin paper/, README, UNBLIND.

---

## 1. Exp 24 — escalamiento de ε_link (committed pre-reg → run)

**Por qué primero:** Background results + JSON ya listos (confirma ε_link scaling <<1 con tamaño, v_link ~ área). Pre-reg y results en Codex notes/ + outputs/. Símbolos Option D y kernel draft dependen de esto.

**Acción inmediata:**
- Sync/confirm pre-reg formal (exp24_prereg_2026-07-03.md) en main notes/.
- Correr `code/analysis/24_epsilon_link_scaling.py` con grilla completa (rhos, Rs, dims 2/4, n_real suficiente para SEM).
- Producir JSON full + summary.
- Actualizar symbol_table_new_conventions.md con benchmarks exactos.
- Validar contra [ℛ]=1 y ε_link = N_links/N_past.

**Entregables:** JSON + updated index + symbols_option_D refinement.
**Timeline:** Hoy/mañana (run + análisis ligero).

---

## 2. Exp 22 — intervalos en inhomogeneous box orders / sesgado (committed pre-reg → run)

**Por qué segundo:** Pre-reg completo (exp22_prereg_outline + referee_questions) ya en main + Codex. Baselines BB/BK/GS listos. Diseñado para medir impacto de bias en abundances, height/width, y separación manifold vs random orders.

**Acción:**
- Sync outline a main si hay diffs.
- Implementar/extender script de sprinkling sesgado (basado en 18a + bias param b modulado por "masa").
- Correr grilla (d=2/4, varios N, b values).
- Medir ℓ_max, N_m, ε_link, v_link vs homogéneo GS y box-order BB.
- Testear trade-off altura/anchura.

**Entregables:** Datos + update a inhomogeneous_box_orders.md + pre-reg results + cross con symbol table.
**Timeline:** 2-4 días.

---

## 3. Siguiente: Exp 17 atrición + factor 1/2 (decidido: integrar atrición con corrección de factor)

**Decisión:** En vez de "factor 1/2 puro" o "atrition Exp17" separado, el próximo es **Exp 17 atrición con factor 1/2**.

**Por qué esta elección:**
- Historia fuerte en atrición (mask >30% descartes en stacking pipeline, ver 17_isw_stacking_pipeline.py y RESULTS_17*).
- Factor 1/2 aparece en kernel 2D de Johnston (G_R = 1/2 C) y necesita validación cruzada con 4D.
- Cierra pipeline de stacking ISW antes de nuevos exps. Riesgo alto si se ignora (sesgo en delta T).

**Acción:**
- Commit pre-reg específico "Exp17+atrition+factor1/2".
- Actualizar 17_isw_stacking_pipeline.py (aplicar factor 1/2 explícito en conteo o kernel).
- Re-correr con controls de atrición (diferentes masks).
- Medir impacto en falsificación (ya ~13σ) y robustez.
- Update symbol_table si introduce nuevos observables (ej. corrected epsilon).

**Entregables:** Pipeline actualizado + resultados con/ sin factor + análisis de bias de atrición + update roadmap.
**Timeline:** 3-5 días después de Exp 22.

---

**Orden y reglas generales:**
1. Exp 24 (rápido, background ya listo)
2. Exp 22 (pre-reg maduro)
3. Exp17 atrición + factor 1/2 (cierre de pipeline existente)

Mantener index_master actualizado después de cada.
Usar pre_domingo_checks como template para auditoría.
Re-evaluar roadmap post cada run (depende de números).

**Después de estos 3:** Posible expansión de Exp18 (finite size) o nuevo con curvatura. Depende de falsificaciones/sobrevivientes.

Solo notas/. Listo.