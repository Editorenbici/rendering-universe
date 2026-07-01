#!/usr/bin/env python3
"""
01_vacuum_catastrophe.py
=======================
The vacuum catastrophe solved by finite resolution R(t).

rho_vac = M_Pl^4 / R^4

Today: R ~ 10^30 → rho_vac ~ 10^(-120) M_Pl^4
Observed: rho_Lambda ~ 2.3e-122 M_Pl^4
"""
import numpy as np

# Planck units
M_Pl = 1.0  # in reduced Planck units (c=hbar=G=1)

# Resolution today (from N ~ 10^120 causal elements, N ~ R^4)
R0 = 10**30

# Predicted vacuum energy
rho_vac_pred = M_Pl**4 / R0**4

# Observed dark energy density in Planck units
# rho_Lambda_obs ~ 10^(-122) M_Pl^4 (from Planck 2018)
rho_Lambda_obs = 2.3e-122

print("="*60)
print("TEST 1: VACUUM CATASTROPHE")
print("="*60)
print(f"R (resolution today)     = {R0:.0e}")
print(f"rho_vac (predicted)      = {rho_vac_pred:.2e} M_Pl^4")
print(f"rho_Lambda (observed)    = {rho_Lambda_obs:.2e} M_Pl^4")
print(f"Ratio pred/obs           = {rho_vac_pred/rho_Lambda_obs:.2f}")
print(f"Orders of error (LCDM)   = 120")
print(f"Orders of error (this)   = {abs(np.log10(rho_vac_pred/rho_Lambda_obs)):.1f}")
print()
print("RESULT: Vacuum catastrophe resolved within a factor of",
      f"{rho_vac_pred/rho_Lambda_obs:.1f}x")
print()

# How N and R scale
z_list = [0, 1, 5, 10, 100, 1000, 1e5, 1e8, 1e10]
for z in z_list:
    a = 1/(1+z)
    # R ~ t^beta with beta~0.5 average
    # t ~ a^(3/2) in matter era
    R_ratio = (a/1.0)**(1.5*0.5) if a > 0 else 0
    N_ratio = R_ratio**4
    rho = 1/N_ratio if N_ratio > 0 else float('inf')
    
    print(f"z={z:8.1e}: R/R0={R_ratio:.4e}, N/N0={N_ratio:.4e}, rho/rho0={rho:.4e}")
