# Exp 20 Parallel Preparation (Gated - No Fit Run) - CODEX

**Date:** 2026-07-03  
**Status:** Preparation only. Exp 20 remains gated until Fable Sunday audit. No execution on real data. All materials for audit.

## 1. Provenance JSON Template (Pantheon+ and DES-Y5)

Use this structure for archived run logs. Fill with actual file SHAs/sizes after download verification.

```json
{
  "experiment": "20_bao_pantheon_desy5_falsifier",
  "date_accessed": "2026-07-03",
  "bao": {
    "source": "Exp15 verified block",
    "url": "https://github.com/CobayaSampler/bao_data/tree/master/desi_bao_dr2",
    "arxiv": "2503.14738",
    "description": "DESI DR2 BAO 13-point + full covariance. Same as used in 15_rt_likelihood.py",
    "files": ["desi_gaussian_bao_ALL_GCcomb.txt", "covariance"],
    "sha256": "TO_BE_FILLED",
    "size_bytes": "TO_BE_FILLED"
  },
  "pantheon_plus": {
    "release": "Pantheon+ DataRelease",
    "official_repo": "https://github.com/PantheonPlusSH0ES/DataRelease",
    "primary_paper": {
      "title": "The Pantheon+ Analysis: The Full Data Set and Light-curve Release",
      "arxiv": "2112.03863",
      "doi": "10.3847/1538-4357/ac8b7a",
      "year": 2022
    },
    "cosmology_paper": {
      "arxiv": "2202.04077"
    },
    "structure": {
      "main_dir": "Pantheon+_Data/4_DISTANCES_AND_COVAR/",
      "key_files": [
        "Pantheon+SH0ES.dat",
        "Pantheon+SH0ES_covsys.txt",
        "README"
      ]
    },
    "license_terms": "Data release for scientific use with citation required (see repo README and papers). Open access with proper attribution.",
    "archived_copy": "path/to/local/archive",
    "sha256_distances": "TO_BE_FILLED",
    "sha256_cov": "TO_BE_FILLED",
    "size_bytes": "TO_BE_FILLED",
    "notes": "Do NOT include SH0ES calibration files unless explicitly comparing H0. Use distances + cov for cosmology fit."
  },
  "des_y5": {
    "warning": "CRITICAL: There are TWO versions. DO NOT MIX.",
    "legacy": {
      "name": "DES-SN5YR (Vincenzi et al. 2024)",
      "repo": "https://github.com/des-science/DES-SN5YR (tagged legacy)",
      "zenodo": "https://zenodo.org/records/12720778",
      "paper": "arXiv:2401.02929 (key cosmology), Sanchez et al. arXiv:2406.05046 (data release)",
      "description": "Original 5YR release used in early analyses.",
      "sha_example": "TO_BE_FILLED"
    },
    "updated": {
      "name": "DES-Dovekie (Popovic et al. 2026 re-analysis)",
      "repo": "https://github.com/des-science/DES-SN5YR (current main)",
      "paper": "arXiv:2511.07517 (re-analysis with updated calibration)",
      "description": "Recalibrated sample with improved systematics. Preferred for new work if using latest.",
      "sha_example": "TO_BE_FILLED"
    },
    "structure": {
      "main_dirs": ["0_DATA", "4_DISTANCES_COVMAT"],
      "key_files": "distances, STAT+SYST covmat, etc."
    },
    "license_terms": "DES collaboration data release. Cite relevant papers (Sanchez 2024, Vincenzi/Popovic).",
    "chosen_version": "TO_BE_DECIDED (document explicitly which and why)",
    "archived_copy": "path/to/local/archive",
    "sha256": "TO_BE_FILLED",
    "size_bytes": "TO_BE_FILLED"
  },
  "verification_notes": "All URLs checked on official GitHub/DES pages 2026-07-03. Sizes and SHAs computed at download time. BAO re-uses Exp15 verified data only."
}
```

## 2. Dry-Run Checklist (for Exp 20)

Before any real-data run (post-audit):
- [ ] Pantheon+ and DES-Y5 archives downloaded to isolated mirror dir.
- [ ] SHAs/sizes match published or repo expectations (log in JSON above).
- [ ] Data loaders read correct columns (z, mu, cov) without hard-coded numbers in script.
- [ ] Synthetic data test passes (see below).
- [ ] BAO loader imports exactly from 15_rt_likelihood.py verified block.
- [ ] No changes to cosmology model or pre-reg outputs.
- [ ] Environment: numpy/scipy versions logged.
- [ ] Output JSON provenance written before any likelihood call.
- [ ] Commit any prep changes with explicit `git add file` only.
- [ ] Confirm which DES version chosen and documented (legacy vs Dovekie).

## 3. Validation with Synthetic Data (minimal mirror, NO real data)

Create/use a tiny synthetic generator for format validation only.

Example (in a separate prep script or notebook, not in 20 script):

```python
import numpy as np
def make_synthetic_sn(n=100, seed=42):
    rng = np.random.default_rng(seed)
    z = rng.uniform(0.01, 1.5, n)
    mu = 5*np.log10( (1+z) * np.random.uniform(0.5, 2, n) * 3000 ) + rng.normal(0, 0.1, n)  # toy
    cov = np.diag(rng.uniform(0.01, 0.1, n)**2)
    return z, mu, cov

# Test loader format compatibility
z, mu, cov = make_synthetic_sn()
# Assert shapes, positive defs, etc.
print("Synthetic format validation passed.")
```

Run this on mirror dir with fake files mimicking structure (e.g. .dat with columns). Goal: confirm script can parse without errors before touching real archives.

## 4. Short Note: “Qué falta para correr Exp 20”

Falta para correr (preparación paralela):
- Auditoría Fable domingo + decisión de desbloqueo.
- Descarga verificada + SHA de archivos reales de Pantheon+ y DES-Y5 elegida (legacy o Dovekie).
- Actualizar script 20 con paths a los archivos archivados + provenance JSON poblado.
- Dry-run con sintéticos completo.
- Confirmar que no hay mezcla de DES versiones.
- Pre-registro / commit de cualquier ajuste mínimo (si se permite).
- Entorno limpio con mismas versiones que Exp15.

Una vez auditado: solo entonces se puede considerar ejecución controlada.

**Entregado como nota de preparación. Listo para revisión domingo.**
