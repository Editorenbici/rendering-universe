#!/usr/bin/env python3
"""
EXP 17b: STACKING DESIVAST x PLANCK — CORREGIDO (marco de coordenadas)
=======================================================================
IDENTICO al Exp 17 commiteado (criterios pre-registrados CONGELADOS,
filtro, umbrales, hipotesis por void, splits) salvo DOS deltas:

DELTA 1 (el fix, una transformacion): DESIVAST da RA/DEC ecuatoriales
(ICRS); el mapa SMICA esta en coordenadas GALACTICAS. El Exp 17
original NO convertia (bug probado en RESULTS_17_atricion.md: mediana
de fraccion valida 0.009 en posiciones erroneas vs 1.000 en las
correctas). Aqui: ICRS -> galactico via astropy antes de todo uso.

DELTA 2 (validacion nueva): V0 ASTROMETRICO, obligatorio antes de V1:
  V0a: el centro galactico (l=0,b=0) debe estar ENMASCARADO y los
       polos galacticos LIMPIOS en TMASK (orientacion del mapa).
  V0b: >=95% de los parches de voids (posiciones corregidas) deben
       pasar el criterio de mascara (diagnostico dio 98.0%).
  V0c: |b| galactico de los voids: mediana en [35,50] grados.

UNBLIND=False hasta auditoria del diff por autor+Codex. La medicion
correra UNA vez. Compromiso: publicar salga como salga — otra vez.
"""

import os

import numpy as np
import healpy as hp
from astropy.io import fits
from astropy.coordinates import SkyCoord
import astropy.units as u

DATA = os.environ.get("EXP1DATA", "/root/exp1data")
UNBLIND = True           # APROBADO por autor + Codex (pre-registro de 6
                         # puntos, sesgo conservador declarado) 2026-07-01
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
    # === FIX 17b: ICRS -> galactico (el mapa SMICA es galactico) ===
    g = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs").galactic
    ra, dec = g.l.deg, g.b.deg   # en adelante (ra,dec) = (l,b) galacticos
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
def cosmo_exp15():
    """tau(z)=H0t e I(z) del mecanismo H2, cosmologia del exp 15."""
    om, beta = 0.295, BETA
    xg = np.linspace(0.0, np.log(1 + 3000.0), 800)
    zg2 = np.expm1(xg)
    dx = xg[1] - xg[0]
    ode = 1 - om - 9e-5
    e2 = om * (1 + zg2) ** 3 + 9e-5 * (1 + zg2) ** 4 + ode
    for _ in range(60):
        e = np.sqrt(e2)
        inv = 1 / e
        integ = np.concatenate((
            np.cumsum((inv[::-1][:-1] + inv[::-1][1:]) * 0.5 * dx)[::-1], [0]))
        tail = (2 / 3) / np.sqrt(om * (1 + zg2[-1]) ** 3)
        tau = integ + tail
        f = (tau / tau[0]) ** (-4 * beta)
        e2n = om * (1 + zg2) ** 3 + 9e-5 * (1 + zg2) ** 4 + ode * f
        if np.max(np.abs(np.log(e2n / e2))) < 1e-9:
            e2 = e2n
            break
        e2 = 0.5 * (e2 + e2n)
    e = np.sqrt(e2)
    # crecimiento D (RK4 en ln a)
    ys = -xg[::-1]
    ey = e[::-1]
    dle = np.gradient(np.log(ey), ys)
    oma = om * np.exp(-3 * ys) / ey ** 2
    n = len(ys)
    h = (ys[-1] - ys[0]) / (n - 1)
    st = np.array([np.exp(ys[0])] * 2)
    ds = [st[0]]
    for i in range(n - 1):
        def f_(k, s):
            y = ys[0] + (i + k) * h
            return np.array([s[1], -(2 + np.interp(y, ys, dle)) * s[1]
                             + 1.5 * np.interp(y, ys, oma) * s[0]])
        k1 = f_(0, st); k2 = f_(.5, st + .5 * h * k1)
        k3 = f_(.5, st + .5 * h * k2); k4 = f_(1, st + h * k3)
        st = st + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        ds.append(st[0])
    d_g = np.array(ds)[::-1]
    d_g /= d_g[0]
    integ2 = d_g / (e * tau)
    icum = np.concatenate((
        np.cumsum((integ2[::-1][:-1] + integ2[::-1][1:]) * 0.5 * dx)[::-1], [0]))
    return (lambda z: np.interp(np.log(1 + z), xg, tau),
            lambda z: np.interp(np.log(1 + z), xg, icum)
                      / np.interp(np.log(1 + z), xg, d_g))


def predictions(z, L):
    emp = -0.0024 * T_CMB * (L / R_H) * np.exp(-z / 0.30)
    tau_of, i_of = cosmo_exp15()
    h2 = -(BETA / tau_of(z)) * GAMMA * BETA * DELTA0 * i_of(z) \
        * (L / R_H) * T_CMB
    return emp, h2


if __name__ == "__main__":
    print("=" * 70)
    print("EXP 17: STACKING DESIVAST x PLANCK")
    print("=" * 70)
    ra, dec, z, L, theta_v = load_voids()
    print(f"\nVoids no-edge: {len(ra)} | z: {z.min():.3f}-{z.max():.3f} "
          f"(mediana {np.median(z):.3f})")
    print(f"L=R_EFF: mediana {np.median(L):.1f} Mpc | "
          f"theta_v mediana {np.degrees(np.median(theta_v)):.2f} deg")
    emp, h2 = predictions(z, L)
    print(f"H_EMP stack esperado: {emp.mean():.1f} uK | "
          f"H_H2 stack esperado: {h2.mean():.1f} uK | H_LCDM: ~-1.5 uK",
          flush=True)

    print("\nCargando mapa SMICA...")
    tmap = hp.read_map(f"{DATA}/COM_CMB_IQU-smica_2048_R3.00_full.fits",
                       field=0) * 1e6          # K -> uK
    mask = hp.read_map(f"{DATA}/COM_CMB_IQU-smica_2048_R3.00_full.fits",
                       field=3)                # TMASK

    # ---------------- V0: validacion ASTROMETRICA (nueva) ----------------
    print("\n--- V0: astrometria (obligatoria tras el bug del 17) ---")
    def fv_at(l, b, tv=np.radians(1.0)):
        vec = hp.ang2vec(np.radians(90 - b), np.radians(l))
        return mask[hp.query_disc(NSIDE, vec, tv)].mean()
    v0a = fv_at(0.0, 0.0) < 0.2 and fv_at(0.0, 90.0) > 0.95 and fv_at(0.0, -90.0) > 0.95
    fvs = np.array([fv_at(l, b, t) for l, b, t in zip(ra, dec, theta_v)])
    v0b = (fvs > 0.7).mean() >= 0.95
    v0c = 35.0 <= np.median(np.abs(dec)) <= 50.0
    print(f"  V0a plano enmascarado/polos limpios: {'PASA' if v0a else 'FALLA'}")
    print(f"  V0b parches validos: {100*(fvs>0.7).mean():.1f}% (>=95): {'PASA' if v0b else 'FALLA'}")
    print(f"  V0c |b| mediana: {np.median(np.abs(dec)):.1f} deg: {'PASA' if v0c else 'FALLA'}")
    if not (v0a and v0b and v0c):
        print("V0 FALLIDO - astrometria incorrecta, NO se continua.")
        raise SystemExit(1)

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
        if (i + 1) % 100 == 0:
            print(f"  nulos {i+1}/{n_sets}: sigma parcial "
                  f"{np.std(nulls):.3f} uK", flush=True)
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
        print("\n" + "=" * 70)
        print("MEDICION REAL (pre-registrada, una sola vez)")
        print("=" * 70, flush=True)
        vals = np.array([patch_dt(tmap, mask, r, d, t)
                         for r, d, t in zip(ra, dec, theta_v)])
        good = np.isfinite(vals)
        v = vals[good]
        sigma_null = nulls.std(ddof=1)
        dt_obs = v.mean()
        # bootstrap sobre voids (verificacion cruzada)
        boots = np.array([RNG.choice(v, len(v), replace=True).mean()
                          for _ in range(2000)])
        print(f"\ndT_stack = {dt_obs:+.2f} uK "
              f"(sigma_null = {sigma_null:.2f}, sigma_boot = {boots.std():.2f}; "
              f"{good.sum()} voids con parche valido)")
        print(f"Significancia de deteccion: {abs(dt_obs)/sigma_null:.1f} sigma")

        # hipotesis (medias congeladas, calculadas sobre voids validos)
        h_lcdm = -1.5
        h_emp = emp[good].mean()
        h_h2 = h2[good].mean()
        print(f"\n{'Hipotesis':<12} {'pred (uK)':>10} {'|obs-pred|/sigma':>17} {'veredicto':>12}")
        for name, p in [("LCDM", h_lcdm), ("EMPIRICA", h_emp), ("H2", h_h2)]:
            ns = abs(dt_obs - p) / sigma_null
            verdict = "COMPATIBLE" if ns < 3 else "EXCLUIDA"
            print(f"{name:<12} {p:>10.1f} {ns:>17.1f} {verdict:>12}")

        # robustez pre-registrada
        print("\n--- Robustez ---", flush=True)
        ngc = ra < 250  # NGC: RA ~110-270; SGC: RA <75 o >300 (mod 360)
        ngc = (ra > 90) & (ra < 280)
        for lbl, sel in [("NGC", ngc & good), ("SGC", (~ngc) & good),
                         ("R_EFF>mediana",
                          (theta_v * 0 + (L > np.median(L))) > 0.5)]:
            sel = sel & good
            if sel.sum() < 20:
                continue
            vv = vals[sel][np.isfinite(vals[sel])]
            scale = np.sqrt(good.sum() / sel.sum())
            print(f"  {lbl}: {vv.mean():+.2f} uK "
                  f"(sigma ~ {sigma_null*scale:.2f}, n={sel.sum()})")
    print("DONE")
