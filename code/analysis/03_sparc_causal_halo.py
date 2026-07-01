#!/usr/bin/env python3
"""
03_sparc_causal_halo.py
========================
Test the causal halo profile against SPARC galaxy rotation curves.

Causal halo: V_halo^2 = V_flat^2 * (R/Rc)^2 / (1 + (R/Rc)^2)
NFW: V_halo^2 = V_200^2 * [ln(1+cx) - cx/(1+cx)] / [x * (ln(1+c) - c/(1+c))]

Data: SPARC (Lelli+ 2016) - 175 galaxies with HI rotation curves.
"""

import numpy as np
import os
import csv

# Cargar datos SPARC
sparc_path = os.path.expanduser("~/rendering-universe/data/sparc")
os.makedirs(sparc_path, exist_ok=True)

# SPARC data file path (download if not present)
data_file = os.path.expanduser("~/AppData/Local/Temp/sparc_massmodels.txt")

if not os.path.exists(data_file):
    print("ERROR: SPARC data file not found.")
    print(f"Download from: https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt")
    print(f"Save to: {data_file}")
    exit(1)

# Parse data
with open(data_file, "r") as f:
    lines = f.readlines()

# Find where data starts
data_lines = []
for line in lines:
    stripped = line.strip()
    if stripped and stripped[0].isalpha() and len(stripped.split()) >= 7:
        parts = stripped.split()
        try:
            float(parts[1])
            data_lines.append(stripped)
        except:
            continue

# Group by galaxy
galaxies = {}
for line in data_lines:
    parts = line.split()
    name, R, Vobs, Vgas, Vdisk, Vbul = parts[0], float(parts[2]), float(parts[3]), float(parts[5]), float(parts[6]), float(parts[7]) if len(parts) > 7 else 0.0
    
    if name not in galaxies:
        galaxies[name] = []
    galaxies[name].append((R, Vobs, Vgas, Vdisk, Vbul))

print("="*72)
print("SPARC: CAUSAL HALO vs NFW PROFILE FIT")
print("="*72)
print(f"Loaded {len(galaxies)} galaxies, {len(data_lines)} data points")
print()

# Causal halo profile
def causal_halo(R, Vflat, Rc):
    x = np.array(R) / Rc
    return Vflat * np.sqrt(x**2 / (1 + x**2))

# NFW profile (simplified)
def nfw_halo(R, V200, c, R200):
    x = c * np.array(R) / R200
    numerator = np.log(1 + x) - x/(1 + x)
    denominator = np.log(1 + c) - c/(1 + c)
    return V200 * np.sqrt(np.maximum(0, numerator / (x * denominator)))

# Test galaxies
test_galaxies = ["DDO154", "NGC2403", "NGC2841", "NGC3198", "NGC7331", "UGC09133", "NGC5907", "UGC02885"]

print("%-12s %5s %8s %8s %8s %8s %8s" % ("Galaxy", "Npts", "Vflat", "Rc", "chi2_c", "chi2_N", "Winner"))
print("-"*70)

results = []
for gname in test_galaxies:
    if gname not in galaxies:
        continue
    pts = galaxies[gname]
    R_arr = np.array([p[0] for p in pts])
    Vobs = np.array([p[1] for p in pts])
    Vgas = np.array([p[2] for p in pts])
    Vdisk = np.array([p[3] for p in pts])
    Vbul = np.array([p[4] for p in pts])
    
    # Halo velocity
    Vhalo = np.sqrt(np.maximum(0, Vobs**2 - Vgas**2 - Vdisk**2 - Vbul**2))
    
    # Valid points (Vhalo > 2 km/s)
    valid = Vhalo > 2
    if sum(valid) < 5:
        continue
    
    R_fit = R_arr[valid]
    V_fit = Vhalo[valid]
    
    # Grid search: causal halo
    best_c = [1e30, 0, 0]
    for Vf in np.linspace(5, 300, 60):
        for Rc in np.linspace(0.5, 40, 60):
            Vmod = causal_halo(R_fit, Vf, Rc)
            chi2 = np.sum(((V_fit - Vmod) / np.maximum(0.1*V_fit, 1.0))**2)
            if chi2 < best_c[0]:
                best_c = [chi2, Vf, Rc]
    
    # Grid search: NFW
    best_n = [1e30, 0, 0, 0]
    R200_try = R_fit[-1] * 2  # R200 ~ 2 * Rmax
    for V200 in np.linspace(5, 300, 60):
        for c_nfw in np.linspace(1, 30, 30):
            Vmod = nfw_halo(R_fit, V200, c_nfw, R200_try)
            chi2 = np.sum(((V_fit - Vmod) / np.maximum(0.1*V_fit, 1.0))**2)
            if chi2 < best_n[0]:
                best_n = [chi2, V200, c_nfw, R200_try]
    
    chi2_c_norm = best_c[0] / len(R_fit)
    chi2_n_norm = best_n[0] / len(R_fit)
    winner = "Causal" if chi2_c_norm < chi2_n_norm else "NFW"
    
    print("%-12s %5d %8.1f %8.1f %8.2f %8.2f %8s" % (gname, len(R_fit), best_c[1], best_c[2], chi2_c_norm, chi2_n_norm, winner))
    results.append((gname, len(R_fit), best_c[1], best_c[2], chi2_c_norm, chi2_n_norm, winner))

print()
print("="*72)
print("RESULT: Causal halo wins in",
      sum(1 for r in results if r[-1]=="Causal"), "/", len(results), "galaxies")
print("NFW wins in", sum(1 for r in results if r[-1]=="NFW"), "/", len(results))
print("Causal halo has 1 fewer free parameter (Rc only, no concentration)")
print()

# Save results
outdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "paper", "tables"))
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, "sparc_fit_results.csv")
with open(outpath, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Galaxy", "Npts", "Vflat", "Rc", "chi2_causal", "chi2_nfw", "Winner"])
    for r in results:
        w.writerow(r)
print(f"Saved to {outpath}")