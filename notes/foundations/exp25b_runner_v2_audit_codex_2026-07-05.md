# Codex audit: Exp 25b runner v2

Date: 2026-07-05

Target:

- Commit: `59acb3c`
- Runner: `code/analysis/25b_disformal_validation.py`
- Prereg: `notes/foundations/exp25b_prereg_2026-07-06.md`

Scope: re-audit runner v2 against Amendments 2, 3, and 4 before author approval for `--run`.

## Summary verdict

Do not unlock `--run` yet without one small correction or explicit author waiver:

1. V0 is now materially fixed and passes in V0-only mode.
2. The C5 positive-control construction matches the analytic `(+0.5,+1.5)` expectation under the stated flat-metric, density-proportional-to-R^2 control.
3. `verdict()` combines the two frozen-cell errors too loosely: it uses RMS error instead of the standard error of the average. This inflates sigma by `sqrt(2)` for the two-cell verdict and makes the 3-sigma criteria easier to pass.
4. C3/C4/C6 are run and stored, but their categories are not compared automatically against the primary verdict. The prereg says the verdict category should not change.

## V0 audit

V0-only command executed in the mirror:

```text
python code/analysis/25b_disformal_validation.py
```

Observed:

```text
V0a Minkowski exacto (1e4 pares): PASA
V0b simetria ida/vuelta (alpha=0.4): PASA
V0c GL16x8 compuesta vs Simpson adaptativo indep.: max rel err 6.90e-08 PASA
V0d pipeline real con R=1.3 == Minkowski reescalado: PASA
```

Assessment:

- V0c now compares the production quadrature against an independent adaptive Simpson integrator, not against the same quadrature family. This resolves the earlier blocker.
- The production quadrature is composite `8 x GL16`, i.e. 128 nodes over the segment. The old simple GL16 failure mode is plausibly fixed.
- V0d now exercises the real pipeline through `R_CONST`, `R_field`, `optical_time`, and `causal_matrix`. This resolves the earlier tautological-control blocker.

Minor non-blocking cleanup: the `optical_time()` docstring still says "Gauss-Legendre 16"; the code actually uses composite `8 x GL16`.

## C5 audit

Implementation:

- `sprinkle(n, alpha, rng)` samples positions with acceptance proportional to `R(x)^2`.
- `flat_metric_biased_density=True` sets `a_metric = 0.0`, so causal relations use flat Minkowski cones.
- `Rv = R_field(x, alpha)` remains the fit variable.
- The window becomes flat/proper with `proper_window_pairs(x, a_metric=0.0, W_PHYS)`.

Analytic check:

In flat 3+1 Minkowski with local density `rho(x) proportional R(x)^2`:

- longest-chain depth scales as `h ~ rho^(1/4) ~ R^(1/2)`;
- the BK width estimator is a local spatial-layer count, scaling as `w ~ rho^(3/4) ~ R^(3/2)`;
- therefore `(p_h, p_w) = (+0.5, +1.5)`.

So the C5 prediction is correctly derived for the control as implemented.

Remaining issue: C5 is printed and stored, but no automatic pass/fail check is attached to the `(+0.5,+1.5)` target.

## `verdict()` audit

Current code:

```python
mh = np.mean([c["p_h"][0] for c in cells])
sh = np.sqrt(np.mean([c["p_h"][1] ** 2 for c in cells]))
mw = np.mean([c["p_w"][0] for c in cells])
sw = np.sqrt(np.mean([c["p_w"][1] ** 2 for c in cells]))
```

For two independent frozen cells, the uncertainty of the mean should be:

```python
sh = np.sqrt(np.sum([c["p_h"][1] ** 2 for c in cells])) / len(cells)
sw = np.sqrt(np.sum([c["p_w"][1] ** 2 for c in cells])) / len(cells)
```

The current RMS formula is larger by `sqrt(n_cells)` when the two errors are comparable. For `n_cells=2`, it inflates sigma by `sqrt(2)`.

Consequence: because S1/F1/F2 use 3-sigma thresholds, inflated sigma makes pass/fail criteria more permissive. This is not a conservative implementation of the preregistered decision rule.

## Control-category audit

Implemented controls:

- C1 ghost
- C2 shuffle
- C3 theta robustness
- C4 W robustness
- C5 positive flat-metric density control
- C6 coordinate-window systematic

Remaining issue:

- C3/C4/C6 are run and serialized, but the runner does not compute their verdict category and compare it to the primary category.
- The preregistered language says the category should not change. That check is currently manual.

Suggested minimum before unlock:

1. Fix `verdict()` uncertainty propagation.
2. Either add automatic category checks for C3/C4/C6 or explicitly record that these are manual post-run checks in the prereg/commit.

