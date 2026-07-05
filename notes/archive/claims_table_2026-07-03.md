# Claims — Render Universe v2.0 (estado 2026-07-03)

Propósito: una sola tabla que el referee y vos podés leer en 2 minutos.
Criterio:
- VIVO: respaldado por análisis/medición, no refutado.
- REFUTADO: negativ reject claro, sin rescate post-hoc.
- ANSATZ: supuesto fenomenológico, no derivado.
- HERRAMIENTA: formalismo/convención utilitaria, no claim físico.
- ABIERTO: pendiente de resultado o completación.

Cada claim incluye: dónde está, fuente, riesgo principal.

---

| # | Claim | Estado | Dónde/Archivo | Evidencia/Fuente | Riesgo / Nota |
|---:|-------|--------|--------------|------------------|---------------|
| 1 | Redshift = cambio de resolución: `1+z = R0/R(ze)` | VIVO | paper/render_universe.tex Postulado 3 | Postulado base; no refutado. | Depende de definir R(t). |
| 2 | `[R]=1` adimensional ; `L_R`, `E_R` para dimensionales | HERRAMIENTA | notes/symbol_table_new_conventions.md | Convención fija agreement cross-files. | Notación nueva, requiere consistencia total. |
| 3 | Crecimiento `dR/dt = R/t` en CSG Minkowski | VIVO | paper/render_universe.tex Sec. Derivation | Derivación algebraica directa. | Solo Minkowski; con materia es modulación empírica. |
| 4 | `rho_vac = M_Pl^4 / R^4` regulariza energía de vacío | ANSATZ | paper/render_universe.tex Vacuum Catastrophe | Coincide ~10^-122 M_Pl^4; factor ~40. | No es derivación QFT primera-principios. |
| 5 | DESI DR2 BAO: `β0 = 0.055^{+0.045}_{-0.050}` | VIVO | paper/render_universe.tex Sec. DE | Likelihood directo R(t) vs 13 BAO; chi2/dof=0.92. | BAO alone: Δχ2≈1 vs ΛCDM; no “preferido”. |
| 6 | Ecuación de estado efectiva `w0 ≈ -0.92` | VIVO | paper/render_universe.tex Sec. DE | Conversión desde β0 con factor `(4/3)/(H0 t0)`. | Necesita SNe+BAO combinado; falsifier 4 abierto. |
| 7 | SPARC pilot: perfil cored gana 7/8 vs NFW | ABIERTO | paper/render_universe.tex Sec. DM | 8 galaxias; χ² comparación simple. | No es muestra completa; perfiles cored no son exclusivos del marco. |
| 8 | Postulado 3′ métrica disforme con ψ | ANSATZ | notes/action_disforme_postulado3_draft.md, notes/energy_momentum_psi_draft.md | Signos revisados; límite Newtoniano definido. | Falta acción covariante completa y Tμν verificada. |
| 9 | Kernel `K(x,y)` selector irreducible de covering + Poisson | VIVO | paper/render_universe.tex Sec. kernel; notes/kernel_paper_section_draft_2026-07-03.md | Mismo objeto que Johnston 2008; aplicación Newton es novedad del proyecto. | Literatura no reporta uso como generador Newton; es nuestra novedad/testing pending. |
| 10 | Límite débil estático reproduce `ψ(r)∝1/r` y fuerza `∝1/r²` | VIVO | paper/render_universe.tex Sec. kernel; Exps 12-13 | Exponente -1.03±0.03; fuerza -2.03±0.23; K normalizado 1-3%. | 2D descartado; validación 4D completa. |
| 11 | Alternativa “causal past interior” sin selector descartada | REFUTADO | paper/render_universe.tex Sec. structure | Fuerza distance-independent; 1/r² excluido >500σ. | Buena validación negativa; mantener publicada. |
| 12 | ISW stacking DESI×Planck: predicción refutada | REFUTADO | paper/render_universe.tex Sec. prediction | ΔT_stack = +1.24±1.46 μK; marco predecía -18.5 μK y -61.7 μK. | Negativo explícito; sector retirado como calibrado. |
| 13 | JWST SMD sub-sampling `(1+z)^-3` | ABIERTO | paper/render_universe.tex Sec. structure | Mejor que ΛCDM solo a z>>10; underpredice en z~7. | Requiere modelo híbrido crecimiento jerárquico + sub-sampling. |
| 14 | Bullet Cluster / DM aliasing | ABIERTO | paper/render_universe.tex Limitations | No hay mecanismo para gas vs galaxias en mergeres. | Obstáculo fuerte para sector DM como único alias. |
| 15 | Exp 24: `ε_link ≈ 0.07` fracción y scaling ley de área 4D | VIVO | notes/exp24_results_2026-07-03.md | ε_link rango 0.05–0.49; error relativo baja a 2.6% en R=10. | Background numerico confirmado; no pre-reg formal committed. |
| 16 | Exp 24 fits: `rho_power≈0.55`, `R_power≈2.21` en 4D | ABIERTO | notes/exp24_results_2026-07-03.md | Ajuste log-rms ~0.018. | Requiere pre-reg formal committed para ser claim. |
| 17 | Exp 22: interval geometry distinguishes manifold-like vs random | ABIERTO | notes/exp22_prereg_outline_2026-07-03.md | Pre-reg completo; no corrido. | Resultado pendiente; baseline BB/BK/GS. |
| 18 | Símbolos nuevos `𝒥_R = v_R ε_link`, `N_c(x,r)` | HERRAMIENTA | notes/symbols_option_D_2026-07-03.md | Definiciones propias; no halladas en literatura. | No son claim físico todavía. |
| 19 | `ε_link` como fracción; `v_link` como valencia/abundancia | HERRAMIENTA | notes/symbol_table_new_conventions.md | Convención stickeada; `η_E` prohibido como fracción. | Confusión histórica ya documentada; usar con cuidado en texto. |
| 20 | ISW revival “solo reinterpretando” NO admisible | VIVO | paper/render_universe.tex Limitations + falsifiers | Política explícita del paper; no rescate post-hoc. | Cumplimiento metodológico. |

---

## Resumen ejecutivo

**Vivos fuertes:** 1, 3, 5, 10, 15
**Vivos débiles/condicionales:** 6, 7, 13, 16
**Refutados:** 11, 12
**Ansatz:** 4, 8
**Herramienta:** 2, 18, 19
**Abiertos pendientes:** 9, 14, 17

Nota: el kernel como generador Newton (9) es VIVO como formalismo, pero su novedad literaria requiere el paper ya insertado para ser claim con peso.
