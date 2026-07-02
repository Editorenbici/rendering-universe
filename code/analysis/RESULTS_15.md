# Resultados pre-registrados: Experimento 15 — Likelihood directo de ℛ(t)

Fecha: 2026-07-01. Pre-registro en el docstring de `15_rt_likelihood.py`,
escrito antes del run. Compromiso: publicar salga como salga.

## Hallazgo previo obligatorio: corrupción de datos en script 02

Los D_H/r_d del script 02 habían sido reemplazados en un commit previo
("Fix: DESI DR2 data values") por valores **físicamente imposibles**
(crecientes con z, lo que implica H(z=2.33) < H0). Se verificaron los
valores contra el release oficial de likelihood de DESI DR2
(github.com/CobayaSampler/bao_data/desi_bao_dr2) y se restauraron.
Todo resultado derivado de la tabla corrupta entre esos commits debe
considerarse inválido.

## Modelo y datos

- ℛ(t) ∝ t^β (monótono), ρ_DE ∝ ℛ⁻⁴, E²(z) autoconsistente por iteración.
- β = 0 ⇔ ΛCDM exacto (anidado).
- Datos: 13 mediciones oficiales DESI DR2 (D_V, D_M, D_H sobre r_d,
  7 tracers) + covarianza oficial completa. Parámetros: Ωm, β; la
  escala c/(H0·r_d) perfilada analíticamente.

## Resultados

| Run | β̂ | 68% | 95% | χ²/dof | Δχ² vs ΛCDM |
|---|---|---|---|---|---|
| BAO solo | +0.055 | [+0.005, +0.100] | [−0.045, +0.145] | 9.16/10 | 1.14 |
| + prior Ωm=0.3111±0.0056 | +0.040 | [0.000, +0.080] | [−0.045, +0.120] | 11.25/10 | 0.84 |

w₀_eff (conversión exacta −1 + (4/3)β/(H₀t₀), con H₀t₀=0.954) = **−0.92**.

## Veredicto del árbitro (R4, pre-registrado)

- Reconstrucción por bins (0.02–0.07): **DENTRO del 68%** en ambos runs.
- β = 0.14 (del fit w₀wₐCDM de DESI vía w₀=−1+2β): al borde del 95%
  (BAO solo) y **EXCLUIDO al 95%** con el prior de Ωm (Δχ²=6.2).
- Conclusión: **la tensión era un artefacto** de traducir un fit de otro
  modelo (w₀wₐCDM) sobre otra combinación de datos (BAO+CMB+SNe) mediante
  la conversión de era de materia. La restricción nativa del marco es
  β₀ = 0.055 (+0.045/−0.050).

## Caveats honestos

1. BAO solo prefiere β>0 sobre ΛCDM por apenas Δχ²≈1: el marco es
   consistente con los datos, **no preferido** por ellos.
2. Monotonicidad (R3): sin hallazgo adverso; β≥0 dentro del 95%.
3. El test pendiente del falsador #4 es el likelihood combinado BAO+SNe.

Perfiles χ²(β): `paper/tables/exp15_beta_profile.npz`.
