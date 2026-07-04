# Index Master — Producción 2026-07-03

**Fecha:** 2026-07-03  
**Propósito:** Registro central de toda la producción del día para auditoría y tracking. Solo notas/.  
**Convenciones:** Todos usan \([\mathcal{R}]=1\) (adimensional), \(\epsilon_{\rm link} = \langle N_{\rm links}\rangle / \langle N_{\rm past}\rangle\) (fracción), \(v_{\rm link}\) separado.  

---

## Archivos producidos / actualizados hoy

### 1. kernel_paper_section_draft_2026-07-03.md
- **Ubicación principal:** Documents/Codex/2026-07-01/hola-claude-necesito-que-revises-el/notes/kernel_paper_section_draft_2026-07-03.md (17:32)
- **Estado:** BORRADOR para auditoría. No insertar en paper/ sin revisión.
- **Responsable:** Codex (borrador) + Grok (revisión de consistencia con Johnston)
- **Fecha:** 2026-07-03
- **Dependencias:** symbol_table_new_conventions.md, kernel_links_formal_2026-07-03.md, Johnston 2008/2009/2010 (link matrix), action_disforme drafts
- **Contenido clave:** K(x,y) vía covering + Poisson. Static projection para 1/r. Precedentes + safe phrases. Revisión OK (consistente con link matrix de Johnston; uso newtoniano es project-specific).

### 2. symbols_option_D_2026-07-03.md
- **Ubicación principal:** Documents/Codex/.../notes/symbols_option_D_2026-07-03.md (17:55, también en rendering-universe/notes/ 17:35)
- **Estado:** BORRADOR técnico interno.
- **Responsable:** Grok
- **Fecha:** 2026-07-03
- **Dependencias:** kernel_links_formal, variables_literature_review, búsquedas (NO ENCONTRADO para _R y N_c)
- **Contenido clave:** NO ENCONTRADO. Cercanos: linking fraction (Carlip), valency (GS), n(x,y) interval, overlaps (BK). Resumen Opción D.

### 3. exp24_results_2026-07-03.md + JSONs
- **Ubicación principal:** Documents/Codex/2026-07-01/hola-claude-necesito-que-revises-el/notes/exp24_results_2026-07-03.md (17:55)
- **JSONs:** .../outputs/exp24_epsilon_link_scaling.json (17:33) + summary.json
- **Estado:** CONFIRMADO_BACKGROUND / DRAFT_NOT_PREREGISTERED. Warning explícito: no usar como medición sin committed pre-reg.
- **Responsable:** Codex
- **Fecha:** 2026-07-03
- **Dependencias:** 24_epsilon_link_scaling.py (o mirror), symbol_table_new_conventions.md, \([\mathcal{R}]=1 + \epsilon_{\rm link} = N_{\rm links}/N_{\rm past}\)
- **Contenido clave:** v_link y ε_link separados. Scaling data (epsilon_mean decrece con R, ~0.07 en casos grandes). Rel error vs área law. Confirma fracción <<1.

### 4. exp22_prereg_outline_2026-07-03.md
- **Ubicación principal:** rendering-universe/notes/exp22_prereg_outline_2026-07-03.md (sync con Codex)
- **Estado:** pre-registro completo en borrador. No correr nada antes de auditoría.
- **Responsable:** Grok / Codex
- **Fecha:** 2026-07-03
- **Dependencias:** inhomogeneous_box_orders.md, literature (Bollobás-Brightwell 1991, Boguñá-Krioukov arXiv:2401.17376, Glaser-Surya 2013), symbol_table_new_conventions.md, exp22_referee_questions
- **Contenido clave:** Convención \([\mathcal{R}]=1\), \(\epsilon_{\rm link}\) fracción. Hipótesis, grilla (d=2/4, N=256..), observables (ℓ_max, N_m m=0-3, ε_link, v_link), métricas (Δd, Z_sep), criterios S/F explícitos, baselines, "No hacer".

### 5. exp22_referee_questions_2026-07-03.md
- **Ubicación principal:** rendering-universe/notes/exp22_referee_questions_2026-07-03.md
- **Estado:** listo (3 preguntas específicas)
- **Responsable:** Grok
- **Fecha:** 2026-07-03
- **Dependencias:** exp22_prereg_outline, literatura baselines
- **Contenido clave:** 3 preguntas referee sobre distinción BB vs geométrico, confounds con BK overlaps, deformación curva GS bajo bias. Citas incluidas.

### 6. symbol_table_new_conventions.md
- **Ubicación principal:** rendering-universe/notes/symbol_table_new_conventions.md
- **Estado:** actualizado / CONFIRMADO para \(\epsilon_{\rm link}\) y \(v_{\rm link}\) (benchmark de exp24)
- **Responsable:** Grok
- **Fecha:** 2026-07-03
- **Dependencias:** variables_R_and_epsilon_link_draft.md, exp22/24, literatura (Carlip, GS, etc.), pre_domingo_checks
- **Contenido clave:** Tabla símbolos nuevos (v_R, ε_link, v_link, η_E, ψ) con estados (CONFIRMADO para ε/v_link, PROHIBIDO para η_E como frac). Anti-símbolos. Equivalencias código/paper/lit. Columna Valor benchmark. Convención \([\mathcal{R}]=1\) cerrada.

### 7. variables_R_and_epsilon_link_draft.md
- **Ubicación principal:** rendering-universe/notes/variables_R_and_epsilon_link_draft.md
- **Estado:** borrador técnico interno. Revisión de convención Codex.
- **Responsable:** Grok (revisión)
- **Fecha:** 2026-07-03
- **Dependencias:** symbol_table_new_conventions.md, link_abundance_poisson_sprinkling.md
- **Contenido clave:** Convención \([\mathcal{R}]=1\) adoptada. \(\epsilon_{\rm link} = N_{\rm links} / N_{\rm past}\) (corregida). Pruebas numéricas (valencia cruda no es fracción). Conflictos β_t vs β_a. Búsqueda CST effective action (NO ENCONTRADO para disforme).

### 8. action_disforme_postulado3_draft.md
- **Ubicación principal:** rendering-universe/notes/action_disforme_postulado3_draft.md
- **Estado:** nota técnica interna, no paper.
- **Responsable:** (Codex/Grok contexto disforme)
- **Fecha:** 2026-07-03
- **Dependencias:** disformal searches, symbol table, energy_momentum_psi_draft
- **Contenido clave:** Acción efectiva mínima para ψ adimensional produciendo métrica disforme Postulado 3.

### 9. energy_momentum_psi_draft.md
- **Ubicación principal:** rendering-universe/notes/energy_momentum_psi_draft.md
- **Estado:** borrador técnico interno. No claim físico final.
- **Responsable:** (contexto disforme)
- **Fecha:** 2026-07-03
- **Dependencias:** action_disforme, disformal_energy_literature, symbol table
- **Contenido clave:** Tensor energía-momento efectivo para ψ en Postulado 3'. Métrica efectiva de materia.

### 10. disformal_energy_literature_2026-07-03.md
- **Ubicación principal:** rendering-universe/notes/disformal_energy_literature_2026-07-03.md
- **Estado:** literature note (fuentes exactas arXiv).
- **Responsable:** Grok
- **Fecha:** 2026-07-03
- **Dependencias:** disformal papers (Sakstein 1409.1734, Zumalacarregui 1004.2684, Bettoni-Liberati 1306.6724, etc.)
- **Contenido clave:** Definiciones ρ/p para campos escalares en teorías disformes. Frame transforms. NO E=mc² para el campo.

---

**Notas generales:**
- Todos los archivos respetan convenciones de symbol_table ( \([\mathcal{R}]=1\) , \(\epsilon_{\rm link}\) fracción, no claims excesivos).
- Producción cruzada con exp18/23 pipelines existentes para baselines.
- Archivos en Codex path son working copies; canonical en rendering-universe/notes/ donde aplicable.
- Listo para pre-domingo checks y auditoría Fable.

Actualizado con producción de hoy.