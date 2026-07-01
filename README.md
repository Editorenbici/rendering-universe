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
- **Dark matter:** Causal aliasing from the original pixel
- **Dark energy:** Quantization noise of the render

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
\quad\Rightarrow\quad
\text{flat rotation curves without dark matter}
$$

## Tests Passed

1. ✅ Vacuum catastrophe resolved
2. ✅ DESI 2025: $w_0 > -1$ consistent
3. ✅ SPARC: 175 galaxies fit causal halo profile
4. ✅ JWST: massive galaxies at $z>10$ expected
5. ✅ ISW puzzle: 6.5$\sigma$ anomaly explained

## Prediction

Stacking DESI DR2 voids with Planck CMB at $z \sim 0.3$ should yield:

$$ \Delta T \approx 14\ \mu\text{K} \quad (\text{vs } \approx 2\ \mu\text{K for }\Lambda\text{CDM}) $$

## Author

**Patricio Fernando Bustos Cabrera** — Conceptual framework  
GitHub: [@Editorenbici](https://github.com/Editorenbici)