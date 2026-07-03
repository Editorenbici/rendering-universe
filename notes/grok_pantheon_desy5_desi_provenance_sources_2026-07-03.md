# GROK — Verified Official Sources for Exp 20 Provenance

**Date:** 2026-07-03  
**Access date for all:** 2026-07-03  
**Method:** Direct from official GitHub repos, arXiv, Zenodo, Cobaya docs. NO unverified aggregators. All URLs + arXiv provided.

## 1. Pantheon+

**Official data release:**
- GitHub: https://github.com/PantheonPlusSH0ES/DataRelease
- Main data dir: Pantheon+_Data/4_DISTANCES_AND_COVAR/
- Key files examples (from repo structure): Pantheon+SH0ES.dat, covariance files, READMEs in subdirs.
- Structure: Separated Pantheon+ distances/cov + SH0ES calibration data. Cosmology inputs in Cosmology/ folder.

**Primary papers (must cite):**
- Scolnic et al. (2022): "The Pantheon+ Analysis: The Full Data Set and Light-curve Release". arXiv:2112.03863. (ApJ)
- Brout et al. (2022): Related cosmological analysis. arXiv:2202.04077.

**License/terms:** Data release intended for scientific use. Citation of the papers required. Check repo README for exact terms at time of use. Generally permissive for research with attribution.

**Notes for use:** Do not blindly mix SH0ES calibration files unless doing H0-specific work. For pure distance + cosmology fits use the distances + full covariance.

## 2. DES Y5: Legacy vs DES-Dovekie (CRITICAL DISTINCTION)

**Current active repo (2026):** https://github.com/des-science/DES-SN5YR
- This repo NOW hosts the **DES-Dovekie** results (updated calibration).

**Legacy DES-SN5YR (Vincenzi et al. 2024 original):**
- Still available via:
  - Zenodo: https://zenodo.org/records/12720778
  - Tagged version in the GitHub repo (see releases/tags).
- Key papers:
  - DES Collaboration (key cosmology): arXiv:2401.02929
  - Sanchez et al. (light curves + ancillary): arXiv:2406.05046 (ApJ)

**Updated DES-Dovekie (re-analysis):**
- Current main branch of https://github.com/des-science/DES-SN5YR
- Paper: Popovic et al. (2026) "The Dark Energy Survey Supernova Program: A Reanalysis... " arXiv:2511.07517
- Improved calibration, different systematics treatment. Changes Ωm and w0/wa preferences compared to legacy.
- Folders: 0_DATA, 4_DISTANCES_COVMAT (STAT+SYST covmat), etc.

**Explicit rule:** Choose ONE version and document it. Do NOT mix legacy and Dovekie files in the same fit. Dovekie is the recalibrated version.

**License:** DES collaboration release. Cite the relevant papers (Sanchez 2024 for data products, Vincenzi or Popovic for cosmology).

## 3. DESI DR2 BAO (already used in Exp 15)

**Confirmed source (matches Exp 15_rt_likelihood.py):**
- https://github.com/CobayaSampler/bao_data/tree/master/desi_bao_dr2
- 13-point vector + full covariance matrix.
- Primary reference: DESI DR2 BAO papers, commonly cited with arXiv:2503.14738 (or the main DESI DR2 cosmology release).

This is the exact block already verified and used in Exp 15. Reuse that loader / data exactly.

## Summary Table for Provenance

| Dataset     | Official Repo / Location                          | Key arXiv(s)          | Notes / Warnings                  |
|-------------|---------------------------------------------------|-----------------------|-----------------------------------|
| BAO DESI DR2| Cobaya bao_data/desi_bao_dr2                     | 2503.14738           | Already in Exp15. Reuse.         |
| Pantheon+   | PantheonPlusSH0ES/DataRelease                    | 2112.03863, 2202.04077 | Distances + cov. Cite both.      |
| DES Y5 Legacy | Zenodo + tagged DES-SN5YR                        | 2401.02929, 2406.05046 | Original Vincenzi.               |
| DES Y5 Dovekie| https://github.com/des-science/DES-SN5YR (main) | 2511.07517           | Recalibrated. Prefer one only.   |

**All verified 2026-07-03. Mark anything added later without re-check as NO VERIFICADO.**

**Entregado como material de preparación paralela. Para auditoría Fable.**
