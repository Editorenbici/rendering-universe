# Paper 1 technical referee audit — Codex

Date: 2026-07-05

Target:

- `notes/foundations/paper1_tex/paper1.tex`
- `notes/foundations/paper1_tex/paper1.pdf`
- Mirror synchronized to master `66f9659`

Scope: hostile technical audit of numbers, derivations, figures, and internal claim hygiene. I did not edit the paper.

## Executive Verdict

The paper is much stronger than the older broad Render draft, but I would not submit this exact version yet. I found four referee-facing issues that are easy to fix now and annoying if discovered externally:

1. Exp 23 numbers (`0.07 sigma`, `+21%`) are not traceable to a committed `RESULTS_23.md` or JSON output.
2. Figure F1 says "parameter-free theory curves" but the 2D inset curve uses an arbitrary additive offset `+5.0`.
3. Figure F3 labels the `0.21` point as "Exp 22 manifoldlike", but I cannot reproduce `0.21` from the Exp 22 JSON; it is closer to the Exp 24/theory reference near `sqrt(rho) R^2 ~= 35`.
4. Equation (epsilon) is written as an equality even though the same section admits finite-boundary corrections of order 10%.

There is also one conceptual-derivation ambiguity in the conformal comparison inside the three-sector identity.

## Findings

### [P1] Exp 23 anchor numbers are not result-file traceable

Paper lines:

- `paper1.tex:131-140`: Glaser-Surya anchor agrees at `0.07 sigma`; slab inflates by `+21%`.

Repo trace:

- Found script: `code/analysis/23_glaser_surya_check.py`
- Did not find: `code/analysis/RESULTS_23.md`, committed Exp23 JSON/stdout, or table containing the measured `(a),(b),(c)` values.
- `FUNDAMENTOS.md` contains `0.07 sigma`, but that is a truth ledger, not the raw result.
- `+21%` was not found in a committed result file by text search.

Why this matters:

A referee can accept the script only as a method, not as evidence that the quoted run happened with those numerical outputs. This is the one number pair in the paper that currently lacks a proper audit trail.

Minimum fix:

Commit `RESULTS_23.md` or JSON/stdout with:

- Glaser-Surya MC integral value and error.
- Exact-link sprinkling mean and SEM.
- Combined sigma = `0.07`.
- Slab/diamond ratio yielding `+21%`.

### [P1] F1 2D inset is not parameter-free as drawn

Paper/caption:

- `paper1.tex:184-188`: caption says "parameter-free theory curves".

Figure generator:

- `make_paper1_figures.py:121-123` draws the 2D inset curve as `2*log(T) + 5.0`.

Source data:

- `RESULTS_18.md`: slope `2.01 +/- 0.12`, flat in `N`.
- Exp18 audit JSON stdout: `v(T)=8.3/9.3/10.6/12.9` for `T=5/10/20/40`.

Why this matters:

The coefficient `2` is parameter-free; the additive constant is explicitly `O(1)` in the paper and is not predicted by the asymptotic expression. The plotted `+5.0` is visually reasonable but is a fitted/hand-chosen vertical offset. A hostile referee will object to calling that entire curve parameter-free.

Minimum fix:

Change the caption wording to "theory scalings" or "parameter-free slopes/coefficient", or label the inset line as `2 ln T + const.` rather than a parameter-free curve.

### [P1] F3 `0.21` point is mislabeled / insufficiently sourced

Paper:

- `paper1.tex:252-256`: manifoldlike `epsilon ~= 0.21`, random order `epsilon ~= 0.017`.
- `paper1.tex:270-273`: F3 caption says manifoldlike vs transitively-closed random orders separate by an order of magnitude.

Figure generator:

- `make_paper1_figures.py:163-165` hardcodes:
  - `(x=35, epsilon=0.21, error=0.015)` labeled `Exp 22 manifoldlike`.
  - `(x=35, epsilon=0.017, error=0.006)` labeled `random orders`.

Exp 22 JSON reconstruction:

- `outputs/exp22_interval_geometry_background/exp22_formal_run_2026-07-03.json`
- `random_order`: mean `0.01703`, SEM `0.00475` — this supports `0.017`.
- `minkowski_4d`: mean `0.38498`, SEM `0.00834` across its cases — not `0.21`.
- `minkowski_2d`: mean `0.03982`, SEM `0.00180` — also not `0.21`.

Exp 24/theory nearby:

- Exp24 at `(rho=1, R=6)`: `sqrt(rho)R^2=36`, measured `epsilon=0.18294`, theory `0.20412`.
- So `0.21` is defensible as a reference/theory-scale manifoldlike number, but not as a direct Exp22 JSON mean.

Minimum fix:

Relabel F3 point to something like `manifoldlike reference (Exp24/theory scale)` or replace the hardcoded point with an actual Exp24 data point. If the intent is Exp22, add a result note explaining which subset/case produces `0.21`.

### [P1] Epsilon equation should be asymptotic, not exact equality

Paper:

- `paper1.tex:243-248` writes
  `epsilon(rho,R) = N_links/N_past = 3sqrt(6)/(sqrt(rho) R^2)`,
  then says measured values track with `~10%` boundary corrections.

Repo source:

- `notes/foundations/exp24_results_2026-07-03.md` explicitly says the formula is from `N_past = rho (pi/3)R^4` and `v = pi sqrt6 sqrt(rho) R^2`, with measured deficits around 10% at reference points.
- The Exp24 table shows finite-scale deviations, e.g. `(rho=1,R=6)` measured `0.18294` vs theory `0.20412`; `(rho=1,R=8)` measured `0.10404` vs theory `0.11482`.

Why this matters:

The equality is true for the idealized/asymptotic slab/cone calculation, not for the finite causal interval values shown in the same paragraph and figure. A referee may call this a contradiction.

Minimum fix:

Write

```tex
\varepsilon(\rho,R) \sim \frac{3\sqrt{6}}{\sqrt{\rho}R^2}
```

or

```tex
\varepsilon(\rho,R) =
\frac{3\sqrt{6}}{\sqrt{\rho}R^2}\,[1+O_{\partial}(R^{-1})]
```

depending on what correction term you want to defend.

### [P2] Three-sector conformal comparison is ambiguous / likely wrong as phrased

Paper:

- `paper1.tex:281-296`.

The disformal accounting itself is consistent:

- Metric: `ds^2 = -lambda^{-2}dt^2 + lambda^2 dx^2`.
- Determinant in 3+1: `sqrt(-g)=lambda^2`.
- Sectors: chain/proper-time `lambda^-1`, spatial width/volume `lambda^+3`, product `lambda^+2`.

The problematic sentence is the conformal aside:

> "A conformal rescaling (clocks and rulers both lambda^+1) requires the chain sector to absorb lambda^-4 for the same volume budget..."

For an ordinary conformal metric `g = lambda^2 eta` in 3+1 dimensions, one gets `sqrt(-g)=lambda^4`, chain scale `lambda^1`, antichain volume `lambda^3`, product `lambda^4`. That closes, not `lambda^-4`.

Maybe the intended comparison is "if one forces the disformal `lambda^2` volume budget while using conformal ruler scaling", but that is not what the sentence says.

Minimum fix:

Either remove the conformal aside or spell out the counterfactual budget being held fixed. As written, it is an easy target because ordinary conformal scaling does not imply the stated `lambda^-4` burden.

### [P2] Figure F2 says "transient fit" but only shows points plus asymptote

Paper:

- `paper1.tex:234-235`: caption says "with the `1/eta` transient fit."

Figure generator:

- `make_paper1_figures.py:133-139` plots Exp18c ratios, a hardcoded `eta=40` point at `0.442`, and a horizontal asymptote `0.4991`.
- It does not plot the actual `A eta^2(1-B/eta)` or ratio-space `F(1-B/eta)` fit curve.

This is not fatal, but the caption promises more than the figure shows. Either draw the fit curve or change the caption to "showing convergence toward...".

### [P2] Visible placeholder remains in the "definitive" paper

Paper:

- `paper1.tex:311-312`: `\figplaceholder{4}{...}`.
- `paper1.tex:11-13`: placeholder macro visibly prints "Figure 4 (placeholder)".

If this PDF is meant as a final technical paper, a visible placeholder is not acceptable. If Figure 4 is intentionally absent, remove the placeholder or make it a text paragraph.

## Number Trace Table

| Paper number | Status | Source found |
|---|---|---|
| `2.01 +/- 0.12` | OK | `code/analysis/RESULTS_18.md`; Exp18 audit stdout |
| `2.089 +/- 0.025` | OK | `code/analysis/RESULTS_18.md`; Exp18 audit stdout |
| 4D amplitude `5%` | OK | `code/analysis/RESULTS_18.md`; Exp18 audit stdout: amplitude effective 7.285 vs 7.695 |
| `2.70 +/- 0.07` | OK rounded | `code/analysis/RESULTS_18.md` has `2.700 +/- 0.071` |
| `Delta AIC = +40.7` | OK | `code/analysis/RESULTS_18d.md` |
| `mathfrak F = 0.4991` | OK | `code/analysis/RESULTS_18d.md` |
| measured `0.4990` | OK | `code/analysis/RESULTS_18d.md` |
| Glaser-Surya `0.07 sigma` | NOT TRACEABLE TO RESULT FILE | Found in `FUNDAMENTOS.md`; script exists; no committed result/stdout found |
| slab `+21%` | NOT TRACEABLE TO RESULT FILE | Script exists; no committed result/stdout found |
| manifoldlike `0.21` | PARTIAL / mislabeled | Exp24/theory scale supports ~0.20; Exp22 JSON does not give 0.21 as mean |
| random order `0.017` | OK | Exp22 JSON `random_order` mean `0.01703` |
| `epsilon = 3sqrt6/(sqrt(rho)R^2)` | DERIVATION OK asymptotically | `exp24_results`; should not be written as exact finite-scale equality |

## Derivation Checks

### 2D coefficient 2

The stated asymptotic law

```tex
v(T) = 2 ln(T sqrt(rho)) + O(1)
```

is technically defensible. The coefficient `2` is the null-direction coefficient; the additive constant is not fixed by the sketched argument and should remain explicitly `O(1)`.

### 4D coefficient `pi sqrt6`

The narrative is terse but acceptable if the derivation exists elsewhere in notes/results. The coefficient is consistent with the Exp18b comparison and the Exp24 epsilon derivation:

```tex
v = pi sqrt6 sqrt(rho) T^2
N_past = rho (pi/3) T^4
epsilon = v/N_past = 3sqrt6/(sqrt(rho)T^2)
```

The paper should avoid implying the paragraph itself is a full derivation; it is a derivation sketch.

### FRW `mathfrak F`

The equation in `paper1.tex:219-220` is transcribed from `RESULTS_18d.md`:

```text
A_corr/A_napkin = 30 int_0^1 x(1-x)^8/sqrt(<a^4>) dx = 0.4991
```

No transcription error found. The only possible referee request is to define `<a^4>(x)` more explicitly in the paper rather than only saying "diamond-weighted average".

## Figure Checks

### F1

Data source is real:

- 18b table parsed from `code/analysis/outputs/exp18c/exp18_audit_20260702_223954.json`.
- 18a cached control parsed from the same JSON.

Issue: the 2D inset line uses arbitrary `+5.0`, so do not call it parameter-free.

### F2

Data source is real:

- Exp18c ratio points from audit JSON.
- `eta=40`, `0.442`, late slope `2.075 +/- 0.078`, and asymptote `0.4991` from `RESULTS_18d.md`.

Issue: caption says transient fit; the fit curve is not actually shown.

### F3

Exp24 scatter and theory curve are correctly drawn from `outputs/exp24_epsilon_link_scaling_summary.json` and `3sqrt6/x`.

Issue: the two comparison points are hardcoded. The `random_order` value is reproducible from Exp22 JSON; the `0.21` "Exp 22 manifoldlike" label is not.

## Claim Hygiene Against FUNDAMENTOS

Mostly clean:

- No cosmological use is made of epsilon; the text explicitly says "not a discovery" and "no cosmological use here".
- The disformal partition is labeled as a consistency theorem, not a dynamics claim.
- Exp25/25b is framed as validation/future work rather than a completed dynamical result.
- The dead `2.70/2.95` estimates are described as estimator/range artifacts.

Main hygiene risk:

- The conformal comparison sentence may overstate or misstate what the counting theorem proves.
- The "all exact seeds behind every number" closing sentence is too strong unless Exp23 outputs/seeds are committed alongside a `RESULTS_23.md`.

