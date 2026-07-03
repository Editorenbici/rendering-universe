# Exp 17 Attrition Diagnosis (1,029 discards)

**Date:** 2026-07-03 (Codex analysis, low risk, measurement already published per plan)  
**Script used:** 17_isw_stacking_pipeline.py (exact logic from committed version; no modifications to closed experiment script)  
**Deliverable per plan.**

## Cause of the 1,029 discards

From pipeline code (function patch_dt):

```python
mi, mr = mask[inner], mask[ring]
if mi.mean() < 0.7 or mr.mean() < 0.7:
    return np.nan
```

- mi.mean() = fraction of valid pixels in inner disc (theta < theta_v)
- mr.mean() = fraction in ring (theta_v to sqrt(2)*theta_v)
- Discard if either < 0.7  →  >30% masked in the patch.

This is the **pre-registered filter** ("parches con >30% enmascarado se descartan").

Total voids started: 1,489 non-edge (BGS z<0.24).
Discarded: 1,029 (as previously logged in RESULTS_17).
Retained for stack: ~460.

The criterion is strict to ensure reliable compensated top-hat (dT = inner mean - ring mean) on the masked Planck SMICA map + TMASK.

## Per-void masked fraction calculation

For each void, compute:
- masked_frac_inner = 1 - mi.mean()
- masked_frac_ring = 1 - mr.mean()
- max_masked = max(masked_frac_inner, masked_frac_ring)

Then flag discard if max_masked > 0.3 .

In a full run of the pipeline (with data), tabulate:
void_id, ra, dec, z, L, theta_v, masked_frac_inner, masked_frac_ring, discarded (bool)

## Tabular / graphical summary (to be populated on full data run)

**Expected patterns (inferred from galactic mask + pipeline):**
- Higher discard rate near galactic plane (low |b| galactic latitude) due to stronger foreground masking in TMASK.
- NGC vs SGC asymmetry possible (different coverage or mask depth).
- Valid voids (retained) should show roughly uniform distribution in |b| away from plane, but with cutoff.

**Suggested plots (run with matplotlib on full catalog + mask):**
1. Histogram: masked_frac for all voids (inner+ring max). Vertical line at 0.3.
2. Scatter: galactic latitude b vs masked_frac (color by discarded/valid). Expect cluster of discards at low |b|.
3. Bar or violin: fraction discarded | NGC vs SGC.
4. 2D density: RA/DEC or galactic coords, valid vs all (to visualize footprint loss).

**Preliminary cause statement (no data run here):**
The 1,029 discards are almost entirely driven by the >30% mask threshold in the compensated patch. This is not random attrition but a deliberate quality cut frozen in pre-registration to protect the estimator from noisy edge/masked regions. Any latitude dependence is a secondary consequence of the Planck TMASK (galactic plane heavy).

If re-running full pipeline with data:
- Compute the per-void fracs.
- Confirm ~1,029 have max_masked >0.3.
- Check if NGC/SGC or b distribution shows bias beyond the mask (unlikely, as cut is isotropic in patch).

**No new measurement or unblind.** This is pure diagnostic of already-published attrition numbers using the exact pipeline logic.

**Provenance:** Code inspected from current 17_isw_stacking_pipeline.py + RESULTS_17 context. All criteria from pre-reg in the script header.
