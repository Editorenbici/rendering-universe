# Analysis Scripts — Status Guide

Not all scripts in this folder have the same standing. This guide states
which results support the paper and which are exploratory or superseded.

## Support the paper (cited or used)

| Script | Role |
|---|---|
| `01_vacuum_catastrophe.py` | Vacuum energy scaling (Section 2.4) |
| `02_desi_render.py` | R(z) reconstruction from DESI DR2 BAO (Section 4) |
| `03_sparc_causal_halo.py` | SPARC 8-galaxy pilot (Section 5; profile empirical, not derived) |
| `04_jwst_highz.py` | JWST SMD scaling (Section 6.1; fits only at z ≳ 10) |
| `05_isw_prediction.py` | ISW prediction, empirically calibrated (Sections 6.2, 7) |

## Pre-registered numerical experiments (validated, published pass/fail)

| Script | Result |
|---|---|
| `12_sprinkling_pound_rebka.py` + `12b_replica_E4.py` | 2D: causal-past counting = Johnston retarded solution, 0.2–0.4% agreement |
| `13_sprinkling_4d_kernel.py` + `13b_verificacion_F3.py` | 4D decisive test: **link counting reproduces Newton; raw causal-past counting refuted** |
| `15_rt_likelihood.py` | Direct R(t)~t^β likelihood vs official DESI DR2 BAO (13 pts + cov): **β₀ = 0.055 (+0.045/−0.050); estimator tension resolved; ΛCDM disfavored by only Δχ²≈1**. See `RESULTS_15.md` |
| `16_derive_isw_coupling.py` | ISW coupling A: **amplitude derived (A ≈ γβ²\|δ₀\|I/(H₀t₀); β_ISW=0.045 ≈ β_BAO=0.055, two independent datasets)**; z-dependence NOT derived (z₀=0.3 stays empirical); static link potential ruled out as the mechanism (4 orders short). See `RESULTS_16.md` |

See `RESULTS_12_13.md` for full pre-registrations, criteria and outcomes.
These experiments are the basis of the link-counting Postulate 6.

## Exploratory / superseded (NOT part of the paper's claims)

| Script | Status |
|---|---|
| `06_hierarchy_experiment.py` | **Superseded.** SI-unit numerology; the "R_min hierarchy" vanishes in Planck units. Kept for the record. |
| `07_dimensionless_hierarchy.py` | Exploratory follow-up to 06. |
| `08_resolution_qubit.py` | Exploratory toy model; coherence suppression is an ansatz, not derived. Known issue: Born-rule section does not demonstrate quantization. |
| `09_resolution_thermodynamics.py` | Exploratory; T(R) form is chosen, not derived. |
| `10_resolution_spectrum.py` | Exploratory; generic UV regulator, no string-theory claim. |
| `11_quantum_darwinism.py` | Exploratory; not independently reviewed. |
| `14_spectral_cutoff_render.py` | Exploratory; not independently reviewed. |

Negative results and superseded mechanisms are kept in the repository
deliberately: the framework's falsifiability discipline (paper Section 8.3)
requires publishing what failed alongside what worked.
