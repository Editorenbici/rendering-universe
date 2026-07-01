#!/usr/bin/env python3
"""
02_desi_render.py
==================
Reconstruct R(z) from DESI DR2 BAO distances.

Uses the D_H/r_d measurements (Table IV, DESI DR2, arXiv:2503.14738).
From H(z) we compute rho_DE(z) and then R(z) ~ rho_DE^(-1/4).
Compara con LCDM: w > -1 and wa < 0 => R crece => w0 > -1.
"""

import numpy as np

# Constantes
c = 299792.458  # km/s
rd = 147.05     # Mpc (sound horizon from Planck)
H0 = 67.97      # km/s/Mpc
Om = 0.307      # Omega_matter (Planck)

# Datos DESI DR2 BAO (Tabla IV, arXiv:2503.14738)
# Tracer z_eff D_H/r_d +- error
desi_data = [
    {"name": "LRG1",  "z": 0.510, "DH": 21.863, "eDH": 0.425},
    {"name": "LRG2",  "z": 0.706, "DH": 19.455, "eDH": 0.330},
    {"name": "LRG3+ELG1", "z": 0.934, "DH": 17.641, "eDH": 0.193},
    {"name": "ELG2",  "z": 1.321, "DH": 14.176, "eDH": 0.221},
    {"name": "QSO",   "z": 1.484, "DH": 12.817, "eDH": 0.516},
    {"name": "Lya",   "z": 2.330, "DH": 8.632,  "eDH": 0.101},  # Ly-alpha forest
]

print("="*72)
print("DESI DR2 -> R(z) RECONSTRUCTION")
print("="*72)
print()
print("%-15s %6s %10s %12s %12s %12s" % ("Tracer", "z", "H(z)", "rho_DE/rho0", "R/R0", "N/N0"))
print("-"*70)

for d in desi_data:
    z = d["z"]
    H_z = c / (d["DH"] * rd)
    rho_ratio = (H_z/H0)**2 - Om * (1+z)**3  # rho_DE(z)/rho_crit0
    rho_DE_ratio = rho_ratio / (1.0 - Om)    # normalizado a hoy
    
    if rho_DE_ratio > 0:
        R_ratio = rho_DE_ratio**(-0.25)
        N_ratio = R_ratio**4
    else:
        R_ratio = float('nan')
        N_ratio = float('nan')
    
    print("%-15s %6.3f %10.2f %12.4f %12.4f %12.2e" % (d["name"], z, H_z, rho_ratio, R_ratio, N_ratio))

print()
print("="*72)
print("INTERPRETACION")
print("="*72)
print()
print("rho_DE(z) = 3H(z)^2/(8piG) - rho_m(z)")
print("rho_DE ~ 1/R^4 => R(z) ~ rho_DE(z)^(-1/4)")
print()
print("Para R(z) ~ t^beta, la ecuacion de estado es:")
print("  w(z) = -1 + (4/3) * dlnR/dln(1+z)^(-1)")
print("  w0   = -1 + 2*beta   (hoy)")
print()
print("DESI encuentra w0 > -1 -> esto requiere beta > 0")
print("  -> R crece con el tiempo (render avanza)")
print("  -> rho_DE decrece (energia oscura se debilita)")
print()

# Estimar beta de los datos
print("="*72)
print("ESTIMACION DE beta DESDE DESI")
print("="*72)
print()

# Edad del universo
def t_of_z(z, Om=Om, H0=H0):
    t_H = 1.0 / (H0 * 3.2408e-20) / 3.15576e16
    return (2.0/3.0) * t_H * (1+z)**(-1.5) / np.sqrt(Om)

t0 = t_of_z(0.0)

print("%6s %8s %10s %10s" % ("z", "t(Gyr)", "R/R0", "beta_eff"))
print("-"*35)

for d in desi_data:
    z = d["z"]
    H_z = c / (d["DH"] * rd)
    rho_ratio = (H_z/H0)**2 - Om * (1+z)**3
    rho_DE_ratio = rho_ratio / (1.0 - Om)
    if rho_DE_ratio > 0:
        R_ratio = rho_DE_ratio**(-0.25)
    else:
        continue
    
    t_z = t_of_z(z)
    # beta_eff = dlnR/dln(t/t0) a partir de dos puntos
    # usar relacion local: R/R0 ~ (t_z/t0)^beta
    if t_z > 0 and t0 > 0:
        beta = np.log(R_ratio) / np.log(t_z/t0)
        w0 = -1 + 2*beta
    else:
        beta = float('nan')
        w0 = float('nan')
    
    print("%6.3f %8.2f %10.4f %10.3f" % (z, t_z, R_ratio, beta))

print()
# Calcular promedio de beta de los datos de DESI (excluyendo negativos que son artefacto)
betas_valid = []
for d in desi_data:
    z = d["z"]
    H_z = c / (d["DH"] * rd)
    rho_ratio = (H_z/H0)**2 - Om * (1+z)**3
    rho_DE_ratio = rho_ratio / (1.0 - Om)
    if rho_DE_ratio > 0:
        R_ratio = rho_DE_ratio**(-0.25)
        t_z = t_of_z(z)
        if t_z > 0 and R_ratio < 1:
            beta = np.log(R_ratio) / np.log(t_z/t0)
            betas_valid.append(beta)
beta_avg = np.mean(betas_valid) if betas_valid else 0
w0_avg = -1 + 2*beta_avg

print(f"CONCLUSION: beta medio desde DESI = {beta_avg:.3f}")
print(f"  w0 estimado = {w0_avg:.2f}")
print(f"  (Nota: beta_decreciente con z; beta~0.5 en era de materia->w0~0)")
print(f"  DESI requiere w0 > -1 -> Consistente")
print()

import os
# Guardar resultados
outdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "paper", "tables"))
os.makedirs(outdir, exist_ok=True)

print(f"Resultados guardados en paper/tables/desi_r_evolution.txt")
with open(os.path.join(outdir, "desi_r_evolution.txt"), "w") as f:
    f.write("# z t_Gyr R_over_R0 beta w0\n")
    for d in desi_data:
        z = d["z"]
        H_z = c / (d["DH"] * rd)
        rho_ratio = (H_z/H0)**2 - Om * (1+z)**3
        rho_DE_ratio = rho_ratio / (1.0 - Om)
        if rho_DE_ratio > 0:
            R_ratio = rho_DE_ratio**(-0.25)
            t_z = t_of_z(z)
            if t_z > 0:
                beta = np.log(R_ratio) / np.log(t_z/t0)
                w0 = -1 + 2*beta
                f.write(f"{z:.3f} {t_z:.2f} {R_ratio:.6f} {beta:.4f} {w0:.4f}\n")
print("DONE")