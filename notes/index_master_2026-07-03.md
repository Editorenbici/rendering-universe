# Índice maestro de notas para auditoría

Fecha: 2026-07-03  
Uso: guía de lectura para auditoría del domingo.  
Regla: este índice no introduce claims nuevos; solo ordena notas existentes.

Estados:

- **CONFIRMADO**: nota ya auditada o alineada con resultados cerrados.
- **BORRADOR**: útil, pero no debe pasar al paper sin revisión.
- **AUDITAR**: requiere lectura crítica antes de usar.
- **PROHIBIDO**: no usar en claims; mantener solo como archivo histórico o warning.

---

## Orden de lectura recomendado

1. `paper1_claims_master_table_2026-07-03.md`
2. `paper1_conceptual_review_2026-07-03.md`
3. `paper1_narrative_and_visual_review_2026-07-03.md`
4. `link_abundance_poisson_sprinkling.md`
5. `priority_check_frw_interval_abundances.md`
6. `effective_exponents_exp18d_2026-07-03.md`
7. `links_as_transitive_reduction_2026-07-03.md`
8. `variables_R_and_epsilon_link_draft.md`
9. `variables_literature_review_2026-07-03.md`
10. `symbol_table_new_conventions.md`
11. `exp24_prereg_2026-07-03.md`
12. `exp24_results_2026-07-03.md`
13. `kernel_links_formal_2026-07-03.md`
14. `kernel_paper_section_draft_2026-07-03.md`
15. `symbols_option_D_2026-07-03.md`
16. `exp22_prereg_outline_2026-07-03.md`
17. `exp20_provenance_prep_2026-07-03.md`
18. `grok_pantheon_desy5_desi_provenance_sources_2026-07-03.md`
19. `action_disforme_postulado3_draft.md`
20. `energy_momentum_psi_draft.md`

---

## Tabla maestra

| Nota | Fecha | Estado | Responsable | Dependencias | Resumen |
|---|---:|---|---|---|---|
| `paper1_claims_master_table_2026-07-03.md` | 2026-07-03 | CONFIRMADO | Grok/Hermes | `paper1_conceptual_review_2026-07-03.md`, `paper1_narrative_and_visual_review_2026-07-03.md` | Tabla CLAIM/ESTADO/EVIDENCIA/RIESGO/DÓNDE VA. Es la brújula del paper amplio. Usar antes de tocar abstract o claims. |
| `claims_table_2026-07-03.md` | 2026-07-03 | CONFIRMADO | Hermes | `paper1_claims_master_table_2026-07-03.md`, `exp24_results_2026-07-03.md`, `exp22_prereg_outline_2026-07-03.md` | Tabla corta de claims vivos/refutados/ansatz/herramienta para referee y autor. Usar antes de tocar abstract o claims. |
| `paper1_conceptual_review_2026-07-03.md` | 2026-07-03 | AUDITAR | Grok | `RESULTS_15.md`, `RESULTS_17.md`, `RESULTS_18.md`, `RESULTS_18d.md`, `RESULTS_19.md` | Revisión crítica conceptual del primer paper. Lista fortalezas, malentendidos y preguntas de referee. Útil para limitar sobreclaims. |
| `paper1_narrative_and_visual_review_2026-07-03.md` | 2026-07-03 | AUDITAR | Hermes | `paper1_claims_master_table_2026-07-03.md` | Revisión narrativa y visual del paper. Propone frase central, mapa visual, qué decir y qué no decir. No es material público aún. |
| `hermes_video_outlines_2026-07-03.md` | 2026-07-03 | BORRADOR | Hermes | `paper1_narrative_and_visual_review_2026-07-03.md`, `paper1_claims_master_table_2026-07-03.md` | Outlines de divulgación con tono de laboratorio abierto. Mantener como borrador; no publicar antes de auditoría. |
| `mathematical_echoes_render_links_R_2026-07-03.md` | 2026-07-03 | BORRADOR | Grok | Ninguna obligatoria; leer después de tabla de claims | Mapa de analogías formales: UV/IR, links, Hasse, entropía, puntos ciegos. No convertir analogías en claims físicos. |
| `effective_exponents_exp18d_2026-07-03.md` | 2026-07-03 | CONFIRMADO | Grok | `RESULTS_18.md`, `RESULTS_18d.md` | Formaliza exponentes efectivos y finite-size scaling. Sirve para narrar Exp 18 → 18d sin sobreinterpretar el 2.7. Incluye guardrails de lenguaje. |
| `links_as_transitive_reduction_2026-07-03.md` | 2026-07-03 | CONFIRMADO | Grok | `link_abundance_poisson_sprinkling.md` | Define links como covering relations/transitive reduction/Hasse diagram. Útil para lenguaje técnico y visual. Incluye riesgos de valency infinita. |
| `link_abundance_poisson_sprinkling.md` | previo + 2026-07-03 | CONFIRMADO | Grok/Fable | `23_glaser_surya_check.py`, `RESULTS_18d.md` | Baseline de abundancias de links y valency. Registra que \(N_0\) Glaser-Surya fue reproducido y que la ley slab es específica del proyecto. |
| `priority_check_frw_interval_abundances.md` | 2026-07-03 | CONFIRMADO | Fable/Grok | `link_abundance_poisson_sprinkling.md`, `RESULTS_18d.md` | Chequeo de prioridad del transitorio FRW/abundancias. Usar para claims de novedad con cautela. No reemplaza resultados numéricos. |
| `variables_R_and_epsilon_link_draft.md` | 2026-07-03 | AUDITAR | Codex/Grok | `variables_literature_review_2026-07-03.md`, `symbol_table_new_conventions.md` | Define \(v_R\), \(v_{\rm link}\), \(\epsilon_{\rm link}\). Convención sticky: \([\mathcal R]=1\). Separa valencia de fracción. Requiere auditoría antes de paper. |
| `variables_literature_review_2026-07-03.md` | 2026-07-03 | CONFIRMADO | Grok | `variables_R_and_epsilon_link_draft.md` | Revisión de literatura: \(v_R\) no encontrado verbatim; \(\epsilon_{\rm link}\) conecta con linking fraction; \(G_{\rm eff}\) con links no encontrado. |
| `symbol_table_new_conventions.md` | 2026-07-03 | AUDITAR | Fable/Grok/Codex | `variables_R_and_epsilon_link_draft.md` | Tabla de símbolos nuevos. Debe ser fuente de verdad para notación si Fable la aprueba. Revisar conflicto \(\beta_t\) vs \(\beta_a\). |
| `exp24_prereg_2026-07-03.md` | 2026-07-03 | BORRADOR | Codex | `variables_R_and_epsilon_link_draft.md`, `24_epsilon_link_scaling.py` | Pre-registro de escalamiento de \(\epsilon_{\rm link}\). Define \(H_0\), rango \(\rho,L_R\), criterios S/F. No correr antes de auditoría. |
| `exp24_results_2026-07-03.md` | 2026-07-03 | CONFIRMADO | Codex | `exp24_prereg_2026-07-03.md`, `24_epsilon_link_scaling.py` | Resultado background de Exp 24. Confirma que \(v_{\rm link}\) sigue ley de área 4D con correcciones finitas y que \(\epsilon_{\rm link}\) cae como fracción. No es falsador principal. |
| `kernel_links_formal_2026-07-03.md` | 2026-07-03 | AUDITAR | Codex | `links_as_transitive_reduction_2026-07-03.md`, `variables_R_and_epsilon_link_draft.md` | Define formalmente el kernel de links \(K(x,y)\), el selector no-blocker y la proyección estática. Útil para Postulado 6; no afirmar \(K=1/r\) punto a punto. |
| `kernel_paper_section_draft_2026-07-03.md` | 2026-07-03 | AUDITAR | Codex | `kernel_links_formal_2026-07-03.md`, `link_abundance_poisson_sprinkling.md` | Borrador pulido de sección corta para insertar luego en el paper. Presenta \(K(x,y)\) como generador proyectado del potencial newtoniano en límite débil. No pegado aún en `paper/`. |
| `symbols_option_D_2026-07-03.md` | 2026-07-03 | BORRADOR | Codex | `variables_R_and_epsilon_link_draft.md`, `exp24_results_2026-07-03.md` | Define \(\mathcal J_R=v_R\epsilon_{\rm link}\) y \(N_c(x,r)\). Marcado como definiciones propias del proyecto, no encontradas en literatura. Requiere auditoría antes de adoptar símbolos. |
| `exp22_prereg_outline_2026-07-03.md` | 2026-07-03 | BORRADOR | Codex | `links_as_transitive_reduction_2026-07-03.md`, `link_abundance_poisson_sprinkling.md` | Pre-registro borrador para intervalos Bollobás-Brightwell/Boguñá-Krioukov. Es test geométrico, no cosmológico. No correr. |
| `exp22_referee_questions_2026-07-03.md` | 2026-07-03 | BORRADOR | Grok/Fable | `exp22_prereg_outline_2026-07-03.md` | Preguntas críticas para Exp 22. Usar para endurecer criterios antes de run. No es resultado. |
| `exp20_provenance_prep_2026-07-03.md` | 2026-07-03 | AUDITAR | Codex/Grok | `grok_pantheon_desy5_desi_provenance_sources_2026-07-03.md`, `20_bao_pantheon_desy5_falsifier.py` | Preparación de provenance y dry-run para Exp 20. Gated hasta Postulado 3′ y archivos con SHA. No correr fit. |
| `grok_pantheon_desy5_desi_provenance_sources_2026-07-03.md` | 2026-07-03 | CONFIRMADO | Grok | `exp20_provenance_prep_2026-07-03.md` | Fuentes oficiales Pantheon+, DES-SN5YR/Dovekie y DESI DR2. Debe usarse para provenance JSON. No mezclar legacy DES con Dovekie. |
| `grok_searches_institutional_2026-07-03.md` | 2026-07-03 | CONFIRMADO | Grok | Ninguna | Emails institucionales y Theo Murphy meeting. Solo usar páginas oficiales. No enviar emails antes de decisión explícita. |
| `action_disforme_postulado3_draft.md` | 2026-07-03 | AUDITAR | Codex/Fable | `disformal_metric_psi_search_2026-07-03.md`, `energy_momentum_psi_draft.md` | Acción efectiva auxiliar para métrica disforme con \(\psi\). Signos revisados: \(\Phi_N=-c^2\psi\). No es teoría final. |
| `energy_momentum_psi_draft.md` | 2026-07-03 | AUDITAR | Codex | `disformal_energy_literature_2026-07-03.md`, `action_disforme_postulado3_draft.md` | Lagrangiano, \(T_{\mu\nu}\), \(\rho_\psi\), \(p_\psi\), fuente y límite newtoniano. Formalismo auxiliar; no claim físico final. |
| `disformal_energy_literature_2026-07-03.md` | 2026-07-03 | CONFIRMADO | Grok | Ninguna | Revisión de energía/presión en teorías escalares disformes. Homologa \(X\), \(\rho\), \(p\). Fuente para no inventar notación. |
| `disformal_metric_psi_search_2026-07-03.md` | 2026-07-03 | CONFIRMADO | Grok | Ninguna | Búsqueda de acciones disformes tipo \(e^{\pm2\psi}\). Concluye que hay marcos generales, no forma exacta derivada de resolución. |
| `ascensor_resolucion_acelerada.md` | previo/2026-07-03 | AUDITAR | Fable/Codex | `action_disforme_postulado3_draft.md` | Nota del ascensor y gradiente de \(\mathcal R\). Signos revisados, pero mantener como analogía/formalismo auxiliar. |
| `sector_fotonico_metrica_disforme.md` | previo | AUDITAR | Fable | `action_disforme_postulado3_draft.md` | Sector fotónico/métrica disforme. Revisar solo después de fijar Postulado 3′. No usar para claims hasta auditoría. |
| `everpresent_Lambda_super-Hubble.md` | previo/2026-07-03 | BORRADOR | Fable/Grok | `RESULTS_19.md` | Nota sobre loophole super-Hubble de everpresent Lambda. Útil como futuro Exp 19b; no reabre Exp 19 cerrado. |
| `coincidencia_sincronica_1-H0t0_beta.md` | previo | BORRADOR | Fable | `RESULTS_15.md` | Nota sobre \(H_0t_0\) y \(\beta\). Interesante internamente; no usar sin revisar convención \(\beta_t\). |
| `anisotropia_cadena_anticadena.md` | previo | BORRADOR | Fable | `RESULTS_18d.md` | Nota de anisotropía cadena/anticadena. Puede alimentar futuros experimentos, no Paper A sin auditoría. |
| `storyboard_manim_tres_sectores_2026-07-03.md` | 2026-07-03 | BORRADOR | Hermes | `paper1_claims_master_table_2026-07-03.md`, `exp15_results.md`, `exp17_results.md`, `exp18_results.md` | Storyboard conceptual para animaciones Manim de los tres sectores. No animar hasta después de papers. |
| `spatial_distance_estimators_causets.md` | previo | BORRADOR | Fable/Grok | `exp22_prereg_outline_2026-07-03.md` | Estimadores de distancia espacial en causets. Relevante para Exp 22 si se requiere embedding/geodesic distances. |
| `inhomogeneous_box_orders.md` | previo | BORRADOR | Fable/Grok | `exp22_prereg_outline_2026-07-03.md` | Órdenes de caja inhomogéneos. Puede servir como control no geométrico o sesgado. No usar sin pre-registro. |
| `RESULTS_17_paper_updates.md` | previo | AUDITAR | Fable | `RESULTS_17.md` | Notas para actualizar paper tras ISW nulo. No editar paper automáticamente; usar como guía de limitaciones. |
| `zenodo_submission_logistics.md` | 2026-07-03 | AUDITAR | Fable/Grok | Cadena final de scripts/resultados | Logística Zenodo/Manchester. Usar después de congelar commit y outputs. |

---

## Notas históricas o de baja prioridad

| Nota | Estado | Responsable | Uso |
|---|---|---|---|
| `alexandroff_cutoff_implementaciones.md` | BORRADOR | Fable/Grok | Conceptual/topológico. No usar para claims técnicos inmediatos. |
| `el_todo_en_vez_del_infinito.md` | BORRADOR | Patricio/Fable | Filosófico. Mantener fuera del paper técnico salvo cita interna. |
| `infinity_totalities.md` | BORRADOR | Grok/Fable | Filosófico/matemático. No usar en Paper A. |
| `ideas_en_espera.md` | BORRADOR | Patricio | Backlog. No auditar salvo que se active una idea. |
| `ieee1788_python_2026.md` | BORRADOR | Grok | Interval arithmetic. Solo relevante si se formaliza numerics/rounding. |
| `nieto_1810_04521_analisis.md` | BORRADOR | Grok | Análisis específico. No central para auditoría domingo. |
| `fundamentos_gibbons_jacobson.md` | BORRADOR | Grok/Fable | Analogías de gravedad/termodinámica. Riesgo de sobreclaim. |

---

## Prohibiciones operativas para la auditoría

1. No usar ninguna nota BORRADOR como afirmación del paper.
2. No tocar `paper/`, `README.md`, `RESULTS_*` cerrados ni flags `UNBLIND`
   durante la auditoría de notas.
3. No correr Exp 20, Exp 22 ni Exp 24 hasta que sus pre-registros estén
   aprobados. Excepción registrada: Exp 24 fue corrido como background
   explícito y debe leerse solo junto a `exp24_results_2026-07-03.md`.
4. No publicar material visual de Hermes antes de limpiar claims y lenguaje.
5. No usar \(\pi\sqrt6\sqrt\rho L_R^2\) como \(\epsilon_{\rm link}\): eso es
   \(v_{\rm link}\), no una fracción.
6. No usar \(v_R=\beta H\mathcal R\) sin especificar que
   \(\beta=\beta_a=d\ln\mathcal R/d\ln a\). Para Exp 15 usar
   \(\beta_t=d\ln\mathcal R/d\ln t\).

---

## Lectura mínima si hay poco tiempo

1. `paper1_claims_master_table_2026-07-03.md`
2. `link_abundance_poisson_sprinkling.md`
3. `effective_exponents_exp18d_2026-07-03.md`
4. `variables_R_and_epsilon_link_draft.md`
5. `exp24_prereg_2026-07-03.md`
6. `exp24_results_2026-07-03.md`
7. `kernel_paper_section_draft_2026-07-03.md`
8. `exp20_provenance_prep_2026-07-03.md`

Con estas ocho notas se cubren claims, Paper A, símbolos nuevos y compuertas
de próximos experimentos.
