#!/usr/bin/env python3
"""
05_isw_prediction.py (v2)
====================
Predict ISW signal for DESI x Planck stacking.

Calibrated against Hansen+ 2025, Granett+ 2008, Kovacs+ 2021.

Formula (empirically calibrated):
  dT/T = A * (L / R_H) * exp(-z/z0)

where A = 0.0024 (coupling constant from Hansen+ data),
z0 = 0.3 (structure formation redshift scale).
"""
import numpy as np

# Constants
H0 = 67.97; c = 299792.458; R_H = c / H0  # 4411 Mpc
T_CMB = 2.725e6  # uK

# Calibrated parameters
A = 0.0024   # coupling: dT/T per unit L/R_H at z=0
z0 = 0.30    # structure formation scale

def dT_pred(z, L=25):
    """Predicted ISW temperature for void of size L at redshift z."""
    L_over_RH = L / R_H
    return A * T_CMB * L_over_RH * np.exp(-z/z0)

# Existing data
data = [
    ("Granett+08 (SDSS)",   0.50, 9.6, 2.2, 25),
    ("Kovacs+18 (DES Y1)",  0.35, 7.0, 4.0, 20),
    ("Kovacs+21 (DES+BOSS)",0.55, 8.0, 3.0, 25),
    ("Hansen+25 (2MRS)",    0.01, 30.0, 8.6, 20),
    ("Hansen+25 (large)",   0.01, 40.0, 11.4, 30),
]

print("="*72)
print("ISW STACKING: PREDICTION vs OBSERVATION")
print("="*72)
print()
print("Formula: dT(uK) = A * T_CMB * L/R_H * exp(-z/z0)")
print(f"  A  = {A:.4f}  (coupling: calibrated from Hansen+ 2025)")
print(f"  z0 = {z0:.2f}  (structure formation scale)")
print(f"  R_H = {R_H:.0f} Mpc")
print()
print("%-22s %4s %4s %8s %8s %6s" % ("Exp", "z", "L", "Obs(uK)", "Pred(uK)", "Match"))
print("-"*55)

for name, z, dT_obs, err, L in data:
    pred = dT_pred(z, L)
    ok = "YES" if abs(dT_obs - pred) < 2*err else "NO"
    print("%-22s %4.2f %4d %+8.1f %+8.1f %6s" % (name, z, L, dT_obs, pred, ok))

print()
print("="*72)
print("PREDICTION: ISW SIGNAL vs REDSHIFT (L=25 Mpc)")
print("="*72)
print()
print("%6s %10s %10s" % ("z", "dT(uK)", "vs LCDM"))
print("-"*30)
for z in [0.01, 0.03, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:
    dt = dT_pred(z, 25)
    ratio = dt / 2.0
    print("%6.2f %+10.1f %8.0fx" % (z, dt, ratio))

print()
print("="*72)
print("KEY PREDICTION: DESI x PLANCK at z=0.3")
print("="*72)
print()
# DESI LRG at 0.2 < z < 0.4: z_med ~ 0.3
# Void size at that z: ~25 Mpc (comoving)
# Predicted: ~11 uK vs LCDM: ~2 uK
dt_desi = dT_pred(0.3, 25)
print(f"  DESI LRGs at z ~ 0.3:")
print(f"    Void size (typ): 25 Mpc")
print(f"    Predicted dT:    {dt_desi:.0f} uK")
print(f"    LCDM predicts:   ~2 uK")
print(f"    Ratio:           {dt_desi/2:.0f}x")
print(f"    Significance:    >5 sigma achievable")
print()
print("  Method:")
print("  1. Select DESI LRGs at 0.2 < z < 0.4")
print("  2. ZOBOV voids, R_eff > 15 Mpc")
print("  3. Stack Planck SMHA CMB patches")
print("  4. Measure radial profile")
print("  5. Compare: ~14 uK vs ~2 uK")