# The Rendering Universe

## Causal Refinement as a Unified Framework for Cosmology

**Author:** Patricio Fernando Bustos Cabrera  
**Date:** 2026  
**License:** MIT

---

## Core Idea

The universe is **1**. It did not expand. What increases is its **causal resolution** $\mathcal{R}(t)$ —the number of pixels per side of the cosmic render.

- **Big Bang:** $\mathcal{R} = 1$ (one pixel)
- **Today:** $\mathcal{R} \sim 10^{30}$ ($\sim 10^{120}$ pixels)
- **Vacuum energy:** $\rho_{\text{vac}} = M_{\text{Pl}}^4 / \mathcal{R}^4$
- **Redshift:** $1+z = \mathcal{R}_0 / \mathcal{R}_e$
- **Dark matter sector:** empirical cored profile (derivation from link counting: open problem)
- **Dark energy:** quantization noise of the render ($\rho_{DE} \propto \mathcal{R}^{-4}$)
- **Local $\mathcal{R}$ (Postulate 6):** sourced by causal **link counting** (Johnston 2008), validated numerically in pre-registered sprinkling experiments 12–13

## Repository Structure

```
rendering-universe/
├── README.md              ← This file
├── LICENSE
├── paper/
│   ├── render_universe.md ← Main paper
│   ├── figures/           ← All figures
│   └── tables/            ← Data tables
├── code/
│   ├── analysis/          ← Analysis scripts
│   │   ├── 01_vacuum_catastrophe.py
│   │   ├── 02_desi_render.py
│   │   ├── 03_sparc_causal_halo.py
│   │   ├── 04_jwst_highz.py
│   │   └── 05_isw_prediction.py
│   ├── stacking/          ← DESI × Planck ISW stacking
│   └── utils/             ← Helper functions
├── data/                  ← Data files (see sources below)
├── references/            ← Key papers
```

## Data Sources

| Dataset | Source | Paper |
|---------|--------|-------|
| DESI DR2 BAO | [DESI](https://data.desi.lbl.gov) | 2503.14738 |
| SPARC galaxy rotations | [SPARC](https://astroweb.case.edu/SPARC/) | Lelli+ 2016 |
| JWST EPOCHS IV | [GitHub](https://github.com/tHarvey303/EpochsIV) | Harvey+ 2024 |
| Planck 2018 CMB | [Planck Legacy](https://pla.esac.esa.int) | Planck 2018 |
| Hansen+ 2025 ISW | [arXiv](https://arxiv.org/abs/2506.08832) | Hansen+ 2025 |

## Key Equations

$$
ds^2 = -c^2 dt^2 + dr^2 \quad\text{(Minkowski: the universe is 1)}
$$

$$
\rho_{\text{vac}} = \frac{M_{\text{Pl}}^4}{\mathcal{R}^4}
\quad\Rightarrow\quad
\rho_{\Lambda}^{\text{obs}} \sim 10^{-120} M_{\text{Pl}}^4
$$

$$
\frac{\Delta T}{T_{\text{CMB}}} = \frac{H_0}{c} L \frac{\Delta\mathcal{R}}{\mathcal{R}}
\quad\Rightarrow\quad
\Delta T_{\text{voids}} \sim 30\ \mu\text{K}
$$

$$
V_{\text{halo}}^2(R) = V_{\text{flat}}^2 \frac{(R/R_c)^2}{1+(R/R_c)^2}
\quad\text{(empirical cored profile; NOT yet derived from Postulate 6)}
$$

## Status of the Tests

1. ✅ Vacuum catastrophe: reduced to a factor ~40 (IR/holographic ansatz, cf. Cohen–Kaplan–Nelson)
2. ✅ DESI 2025: $w_0 > -1$, $w_a < 0$ quadrant matches; factor 2–3 tension in $\beta_0$ open
3. ⚠️ SPARC: 8-galaxy pilot, cored profile beats NFW 7/8 — but cored profiles beat NFW independently of theory (core–cusp), and the profile is not derived
4. ⚠️ JWST: sub-sampling scaling fits at $z \gtrsim 10$, underpredicts at $z \approx 7$
5. ✅ ISW puzzle: calibrated DESI × Planck prediction generated (coupling $A$ empirical)

**Numerical results (pre-registered):** experiments 12–13 show that defining
$\mathcal{R}$ by **link counting** reproduces the Newtonian kernel ($1/r$
potential, $1/r^2$ force, Johnston normalization to 1–3%), while raw
causal-past counting fails (no static limit, distance-independent force).
See `code/analysis/RESULTS_12_13.md`.

**Falsifiers:** the paper states five explicit falsifiers (Section 8.3),
including DESI×Planck void stacking at $z\sim0.3$ and any confirmed
phantom $w_0 < -1$.

## Prediction

Stacking DESI DR2 voids with Planck CMB at $z \sim 0.3$ should yield:

$$ \Delta T \approx 14\ \mu\text{K} \quad (\text{vs } \approx 2\ \mu\text{K for }\Lambda\text{CDM}) $$

## Author

**Patricio Fernando Bustos Cabrera** — Conceptual framework  
GitHub: [@Editorenbici](https://github.com/Editorenbici)
