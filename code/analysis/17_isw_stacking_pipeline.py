#!/usr/bin/env python3
"""
EXPERIMENTO 17: STACKING DESI(VAST) x PLANCK - EL TEST DECISIVO
================================================================
Falsador #1 del paper. Corre en WSL (healpy).

DATOS:
  - Planck SMICA R3.00 (Nside 2048) + TMASK del propio FITS.
  - DESIVAST DR1 VoidFinder (BGS, z<0.24): 1,489 voids no-edge.
    theta_v = R_EFF / R_comovil (adimensional, h se cancela).

FILTRO (congelado antes de mirar datos reales):
  Top-hat compensado: dT = <T>(theta < theta_v) - <T>(theta_v..sqrt(2)*theta_v)
  en el mapa enmascarado (TMASK y parches con >30% enmascarado se descartan).

=========================== PRE-REGISTRO (BORRADOR) ===========================
FASES:
  V1. Control nulo: stacking en N_rand=1000 conjuntos de posiciones
      aleatorias dentro del footprint (mismos theta_v) -> media 0,
      distribucion del estimador = barra de error empirica.
  V2. Inyeccion: senal sintetica de -10 uK con perfil top-hat en
      posiciones aleatorias -> el pipeline debe recuperar -10 +/- sigma.
  SOLO SI V1 y V2 PASAN se desbloquea la medicion (UNBLIND=True tras
  auditoria de pre-registro).

HIPOTESIS (calculadas VOID POR VOID con su z y L=R_EFF/h Mpc):
  H_LCDM:   dT_stack ~ -1 a -2 uK (literatura; signo: voids = frios)
  H_EMP:    dT_i = -0.0024 * T_CMB * (L_i/R_H) * exp(-z_i/0.30)
  H_H2:     dT_i = -(beta/tau(z_i)) * gamma*beta*|delta0|*I(z_i) * (L_i/R_H) * T_CMB
            (mecanismo exp 16; gamma=1, delta0=0.7, beta=0.055)
  AMBIGUEDAD DECLARADA: la calibracion de A uso "L" con definicion laxa
  (L = R_eff aqui; factor <=2 de sistematico si fuera diametro).

CRITERIOS (se congelan en la auditoria; borrador):
  - Deteccion: |dT_stack| > 3*sigma_boot.
  - Discriminacion: la hipotesis H con menor |dT_obs - dT_H| en unidades
    de sigma; una H queda EXCLUIDA si |dT_obs - dT_H| > 3 sigma.
  - Robustez: el resultado debe mantenerse (dentro de 2 sigma) al
    partir NGC/SGC y al usar solo voids con R_EFF > mediana.
COMPROMISO: publicar salga como salga.
==============================================================================
"""

import numpy as np
import healpy as hp
from astropy.io import fits

DATA = "/home/hermes/exp1data"
UNBLIND = False          # <- solo True tras auditoria del pre-registro
NSIDE = 2048
T_CMB = 2.725e6          # uK
R_H = 4411.0             # Mpc
H_LITTLE = 0.6797
BETA, GAMMA, DELTA0 = 0.055, 1.0, 0.7
RNG = np.random.default_rng(170)

# ---------------- catalogo ----------------
def load_voids():
    rows = []
    for gc in ("NGC", "SGC"):
        with fits.open(f"{DATA}/DESIVAST_BGS_VOLLIM_VoidFinder_{gc}.fits",
                       memmap=False) as f:
            d = f["MAXIMALS"].data
            ok = d["EDGE"] == 0
            rows.append(np.array([d["RA"][ok] % 360.0, d["DEC"][ok],
                                  d["R"][ok], d["R_EFF"][ok]]).T)
    cat = np.vstack(rows)
    ra, dec, rcom, reff = cat.T
    theta_v = reff / rcom                    # rad
    # z desde distancia comovil (fiducial Planck18, Om=0.315)
    zg = np.linspace(0.0, 0.35, 400)
    om = 0.315
    ez = np.sqrt(om * (1 + zg) ** 3 + 1 - om)
    dc = np.concatenate(([0.0], np.cumsum(
        (1 / ez[:-1] + 1 / ez[1:]) * 0.5 * np.diff(zg)))) * (299792.458 / 67.36)
    z = np.interp(rcom / H_LITTLE, dc, zg)   # rcom en Mpc/h -> Mpc
    L = reff / H_LITTLE                      # Mpc
    return ra, dec, z, L, theta_v


# ---------------- filtro compensado ----------------
def patch_dt(tmap, mask, ra, dec, theta_v):
    """dT compensado (uK) o nan si el parche esta muy enmascarado."""
    vec = hp.ang2vec(np.radians(90 - dec), np.radians(ra))
    inner = hp.query_disc(NSIDE, vec, theta_v)
    outer = hp.query_disc(NSIDE, vec, theta_v * np.sqrt(2.0))
    ring = np.setdiff1d(outer, inner, assume_unique=True)
    mi, mr = mask[inner], mask[ring]
    if mi.mean() < 0.7 or mr.mean() < 0.7:
        return np.nan
    return (tmap[inner][mi > 0.5].mean() - tmap[ring][mr > 0.5].mean())


def stack(tmap, mask, ras, decs, thetas):
    vals = np.array([patch_dt(tmap, mask, r, d, t)
                     for r, d, t in zip(ras, decs, thetas)])
    vals = vals[np.isfinite(vals)]
    return vals.mean(), vals.std(ddof=1) / np.sqrt(len(vals)), len(vals)


# ---------------- predicciones por void ----------------
def predictions(z, L):
    emp = -0.0024 * T_CMB * (L / R_H) * np.exp(-z / 0.30)
    # H2: usar tau(z), I(z) del exp 16 (aprox. con la cosmologia fiducial)
    # implementacion completa al congelar el pre-registro
    return emp


if __name__ == "__main__":
    print("=" * 70)
    print("EXP 17: STACKING DESIVAST x PLANCK")
    print("=" * 70)
    ra, dec, z, L, theta_v = load_voids()
    print(f"\nVoids no-edge: {len(ra)} | z: {z.min():.3f}-{z.max():.3f} "
          f"(mediana {np.median(z):.3f})")
    print(f"L=R_EFF: mediana {np.median(L):.1f} Mpc | "
          f"theta_v mediana {np.degrees(np.median(theta_v)):.2f} deg")
    emp = predictions(z, L)
    print(f"H_EMP por void: mediana {np.median(emp):.1f} uK "
          f"(stack esperado ~{emp.mean():.1f} uK)")

    print("\nCargando mapa SMICA...")
    tmap = hp.read_map(f"{DATA}/COM_CMB_IQU-smica_2048_R3.00_full.fits",
                       field=0) * 1e6          # K -> uK
    mask = hp.read_map(f"{DATA}/COM_CMB_IQU-smica_2048_R3.00_full.fits",
                       field=3)                # TMASK

    # ---------------- V1: control nulo ----------------
    print("\n--- V1: control nulo (posiciones aleatorias en footprint) ---")
    nulls = []
    n_sets = 60 if not UNBLIND else 1000
    for i in range(n_sets):
        rr = RNG.uniform(0, 360, len(ra))
        dd = np.degrees(np.arcsin(RNG.uniform(np.sin(np.radians(dec.min())),
                                              np.sin(np.radians(dec.max())),
                                              len(ra))))
        m, s, n = stack(tmap, mask, rr, dd, theta_v)
        nulls.append(m)
    nulls = np.array(nulls)
    print(f"nulos: media {nulls.mean():+.2f} uK, sigma {nulls.std():.2f} uK "
          f"({n_sets} sets)")
    v1 = abs(nulls.mean()) < 2 * nulls.std() / np.sqrt(n_sets)
    print(f"V1: {'PASA' if v1 else 'FALLA'}")

    # ---------------- V2: inyeccion ----------------
    print("\n--- V2: inyeccion de -10 uK sintetica ---")
    rr = RNG.uniform(0, 360, len(ra))
    dd = np.degrees(np.arcsin(RNG.uniform(np.sin(np.radians(dec.min())),
                                          np.sin(np.radians(dec.max())),
                                          len(ra))))
    tinj = tmap.copy()
    for r, d, t in zip(rr, dd, theta_v):
        pix = hp.query_disc(NSIDE, hp.ang2vec(np.radians(90 - d),
                                              np.radians(r)), t)
        tinj[pix] -= 10.0
    m, s, n = stack(tinj, mask, rr, dd, theta_v)
    print(f"recuperado: {m:+.2f} +/- {s:.2f} uK (esperado ~-10; "
          f"n_parches={n})")
    v2 = abs(m + 10.0) < 3 * s + 1.5   # tolerancia por dilucion del anillo
    print(f"V2: {'PASA' if v2 else 'FALLA'}")

    if not (v1 and v2):
        print("\nPIPELINE NO VALIDADO - no se mide nada real.")
    elif not UNBLIND:
        print("\nPipeline VALIDADO. Medicion real BLOQUEADA hasta auditoria "
              "del pre-registro (UNBLIND=False).")
    else:
        print("\n--- MEDICION REAL (pre-registrada) ---")
        m, s, n = stack(tmap, mask, ra, dec, theta_v)
        print(f"dT_stack = {m:+.2f} +/- {s:.2f} uK ({n} voids)")
    print("DONE")
