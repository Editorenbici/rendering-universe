# Pre-Domingo Checks — Auditoría Fable 2026-07-03

**Fecha:** 2026-07-03  
**Propósito:** Lista de 10 items que Fable debe revisar el domingo antes de cualquier avance a paper o Zenodo.  
**Regla:** Solo notas/. Sin correr experimentos. Sin claims nuevos.  

---

## 1. Convención [ℛ]=1 y definición de ε_link

**Archivos involucrados:**  
- notes/symbol_table_new_conventions.md  
- notes/exp22_prereg_outline_2026-07-03.md  
- notes/variables_R_and_epsilon_link_draft.md (si existe)  

**Pregunta concreta:**  
¿Todos los archivos usan consistentemente \([\mathcal{R}]=1\) (adimensional) y definen \(\epsilon_{\rm link} \equiv \langle N_{\rm links}\rangle / \langle N_{\rm past}\rangle\) como fracción operacional (y separan claramente \(v_{\rm link}\))? ¿No aparece \(\epsilon_{\rm link}\) como abundancia de escala o η_E?

**Riesgo si se omite:**  
Inconsistencia notacional lleva a errores dimensionales o uso incorrecto de ε_link como factor en G_eff. Pre-reg de Exp22 queda inválido.

---

## 2. Anti-símbolos en todos los borradores

**Archivos involucrados:**  
- notes/symbol_table_new_conventions.md  
- notes/exp22_prereg_outline_2026-07-03.md  
- notes/exp20_provenance_prep_2026-07-03.md  
- notes/variables_literature_review_2026-07-03.md  
- Cualquier otro *.md reciente en notes/  

**Pregunta concreta:**  
¿Se usa β sin subíndice, ℛ como escala de energía sin L_R/E_R, "fracción de enlaces" ambiguo, o claims de "teoría demostrada" / "reemplazo de GR"?

**Riesgo si se omite:**  
Violación de la tabla de convenciones. Auditoría Fable falla; riesgo de claims excesivos que luego hay que retractar.

---

## 3. Baselines literarios en Exp22

**Archivos involucrados:**  
- notes/exp22_prereg_outline_2026-07-03.md  
- notes/inhomogeneous_box_orders.md  
- notes/exp22_referee_questions_2026-07-03.md  

**Pregunta concreta:**  
¿Las tres referencias (Bollobás-Brightwell 1991 para box orders aleatorios, Boguñá-Krioukov arXiv:2401.17376 para overlaps/distances, Glaser-Surya 2013 para abundances manifold-like) están citadas con precisión y se usan como baselines matemáticos (no claims físicos)?

**Riesgo si se omite:**  
Pre-reg de Exp22 se apoya en literatura incompleta o malinterpretada. Referees detectan gap; claim de "primera medición" colapsa.

---

## 4. Consistencia de observables y métricas en pre-regs

**Archivos involucrados:**  
- notes/exp22_prereg_outline_2026-07-03.md  
- notes/exp20_provenance_prep_2026-07-03.md (si menciona observables)  
- notes/symbol_table_new_conventions.md (definiciones de v_link, ε_link, η_E)  

**Pregunta concreta:**  
¿Los observables (ℓ_max, N_m, ε_link, v_link) y métricas (Δd, Z_sep, etc.) están definidos de la misma forma en todos los documentos y respetan la distinción ε_link (fracción) vs η_E (abundancia)?

**Riesgo si se omite:**  
Inconsistencia entre pre-regs. Resultados de un exp no son comparables con otro; auditoría detecta contradicciones.

---

## 5. Criterios de éxito/falla claros y falsificables

**Archivos involucrados:**  
- notes/exp22_prereg_outline_2026-07-03.md  

**Pregunta concreta:**  
¿Los criterios S1-S5 y F1-F5 son numéricos, pre-registrados y falsificables (ej. Δd < 0.20, Z_sep > 3, ε_link estrictamente entre 0 y 1)?

**Riesgo si se omite:**  
Pre-reg se vuelve post-hoc. Si los números no salen, se pueden reinterpretar; pérdida de credibilidad.

---

## 6. "No hacer" y límites de alcance

**Archivos involucrados:**  
- notes/exp22_prereg_outline_2026-07-03.md  
- notes/exp22_referee_questions_2026-07-03.md  
- notes/symbol_table_new_conventions.md (anti-símbolos)  

**Pregunta concreta:**  
¿Está explícito qué NO se debe hacer/inferir en este experimento (no conectar con ℛ dinámica, no BAO/SNe, no G_eff, no nueva física, no mezclar con Exp24)?

**Riesgo si se omite:**  
Se cuelan claims indirectos. Fable o referees lo detectan como scope creep.

---

## 7. Referencias y citas verificables

**Archivos involucrados:**  
- notes/exp22_prereg_outline_2026-07-03.md  
- notes/exp22_referee_questions_2026-07-03.md  
- notes/variables_literature_review_2026-07-03.md  
- notes/inhomogeneous_box_orders.md  

**Pregunta concreta:**  
¿Todas las citas tienen arXiv/DOI exacto, año correcto y resumen preciso (no parafraseo que cambie el significado)?

**Riesgo si se omite:**  
Citas incorrectas o inventadas. Auditoría Fable falla; riesgo de retractación posterior.

---

## 8. Consistencia con symbol_table (anti-símbolos y estados)

**Archivos involucrados:**  
- notes/symbol_table_new_conventions.md  
- notes/exp22_prereg_outline_2026-07-03.md  
- Cualquier draft que mencione v_R, ε_link, β, η_E  

**Pregunta concreta:**  
¿Los estados (CONFIRMADO, PROHIBIDO_COMO_FRACCIÓN) y las prohibiciones de la tabla de anti-símbolos se respetan en el pre-reg de Exp22 y en otros borradores recientes?

**Riesgo si se omite:**  
La symbol table queda como documento huérfano. Se repiten errores que la tabla ya había identificado.

---

## 9. Finite-size y robustness implícitos

**Archivos involucrados:**  
- notes/exp22_prereg_outline_2026-07-03.md  
- notes/inhomogeneous_box_orders.md (si menciona concentración)  

**Pregunta concreta:**  
¿El pre-reg declara cómo se chequea robustez a N (duplicar N, ver convergencia) y a la elección de N_past / geometría del volumen?

**Riesgo si se omite:**  
Resultados dependen de tamaño finito o cutoff arbitrario. Auditoría pide más controles; el experimento queda incompleto.

---

## 10. Separación clara entre baseline matemático y claims físicos

**Archivos involucrados:**  
- notes/exp22_prereg_outline_2026-07-03.md  
- notes/exp22_referee_questions_2026-07-03.md  
- notes/variables_literature_review_2026-07-03.md  
- notes/symbol_table_new_conventions.md  

**Pregunta concreta:**  
¿En todo el material se mantiene explícitamente que las referencias (BB, BK, GS) son "baseline matemático" y "no se declara conexión física con ℛ" en Exp22?

**Riesgo si se omite:**  
Se filtra una narrativa de "derivación de la métrica disforme" antes de tener el experimento corrido y auditado. Pérdida de credibilidad y posibles retractaciones.

---

**Instrucciones para Fable (domingo):**  
Recorrer los 10 items en orden. Para cada uno, abrir los archivos listados, responder la pregunta concreta y registrar riesgo/acción. Si algún item falla, bloquear avance a paper/Zenodo hasta corrección.

**Próximo:** Después de auditoría, actualizar este archivo con resultados y firmas. Mantener solo en notes/.