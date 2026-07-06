# Manifiesto de experimentos (documento vivo)

**Fuente de verdad de claims y estados: `FUNDAMENTOS.md` (raíz).**
Estados: los de FUNDAMENTOS + operativos {INVALIDADO_POR_BUG, GATED,
BLOQUEADO_ENTORNO, ARCHIVADO, CONGELADO}.

| Exp | Nombre | Estado | Evidencia | Próximo paso |
|---|---|---|---|---|
| 01-05 | Scripts fundacionales (vacío, DESI, SPARC, JWST, ISW) | ARCHIVADO (soporte paper marco) | code/analysis/README.md | — |
| 06-11 | Exploratorios/numerología | ARCHIVADO (Cementerio) | FUNDAMENTOS §III | no resucitan |
| 12/12b | Johnston 2D (conteo pasado causal) | MEDIDO | RESULTS_12_13 | — |
| 13/13b | Kernel newtoniano 4D por links | MEDIDO | RESULTS_12_13 | — |
| 15 | Likelihood ℛ(t) vs BAO DESI DR2 | MEDIDO (constraint; no preferencia vs ΛCDM) | RESULTS_15 | DESI DR3 |
| 16 | Derivación acople ISW | SIN BASE (cayó con 17b) | RESULTS_16 + 17b | — |
| 17 | Stacking DESIVAST×Planck | **INVALIDADO_POR_BUG** (marco coords) | RESULTS_17_atricion | — |
| 17b | Stacking corregido (astrometría V0) | **REFUTADO-FIRME** (ISW de ℛ variable) | RESULTS_17b | erratum paper (autor) |
| 18/18a-d | Leyes de valencia (2D/4D/FRW) + κ₄ + 𝔉 | MEDIDO+DERIVADO | RESULTS_18, RESULTS_18d | — |
| 19 | Λ everpresent (toy) | DESFAVORECIDA | RESULTS_19 | 19b (súper-Hubble) opcional |
| 20 | BAO+SNe (falsador 4) | CONGELADO (árbitro real: DESI DR3) | 20_bao_pantheon_desy5 + informe_estado_teoria_2026-07-06 | no correr hasta DESI DR3 / nueva orden |
| 21b | ℕ_R aritmética | IMPLEMENTADO (14/14) | 21b_nr_arithmetic | rendernum (Codex) |
| 22 | Geometría de intervalos (Codex) | MEDIDO (discriminador ε) | outputs/exp22_* | — |
| 23 | Anclaje Glaser-Surya ⟨N₀⟩ | REPRODUCIDO (0.07σ) | 23_glaser_surya_check | — |
| 24 | Escalamiento ε_link | REPRODUCIDO (bit-exacto) | RESULTS/outputs exp24 | 24b (FRW) |
| 25 | Inserción sesgada (−1,+3) | HIPÓTESIS / GATED | exp25_prereg (foundations/) | auditoría prereg → run |

## Congelador etiquetado

| Sector | Estado | Razón | Árbitro / condición de salida |
|---|---|---|---|
| Exp 20 / BAO+SNe | CONGELADO | BAO queda como constraint; correr ahora no decide entre rama A y ΛCDM con suficiente fuerza | DESI DR3 o instrucción explícita del autor |
| Sector materia oscura / SPARC | CONGELADO | No hay mecanismo dinámico ni respuesta Bullet Cluster/lensing; cargarlo debilita el Paper 1 | Mecanismo nuevo pre-registrable o dato/derivación que conecte links con lensing |
