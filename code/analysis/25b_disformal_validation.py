#!/usr/bin/env python3
"""
EXP 25b — VALIDACIÓN EN MÉTRICA DISFORME (runner v2)
=====================================================
Prereg: notes/foundations/exp25b_prereg_2026-07-06.md
(5ef38df + Enm.2 44984a7 + Enm.3 b208349 + Enm.4 [este commit]).
Auditoría v1 de Codex: 3 bloqueadores — resueltos aquí:
  [P1-a] V0c ahora valida contra un integrador INDEPENDIENTE
         (Simpson adaptativo, tol 1e-9), no GL16 vs GL64 de la
         misma familia. El método congelado es segmento recto +
         Fermat (error O(alpha^2)); la Enmienda 4 lo documenta y
         supersede el boceto "radial" del prereg v1.
  [P1-b] V0d ejercita el PIPELINE REAL (R_field/optical_time/
         causal_matrix con R constante vía R_CONST) contra el cono
         de Minkowski reescalado exacto.
  [P1-c] C3 (theta), C4 (W) y C5 (control positivo: densidad R^2 en
         métrica plana -> predicción analítica (+0.5,+1.5))
         implementados. Veredicto S1'/F1'/F2' calculado explícito.

MODO DE EJECUCIÓN (Enmienda 4 — el candado por archivo se eliminó a
pedido del autor 2026-07-06; la disciplina se conserva así):
  python 25b_disformal_validation.py            -> corre SOLO V0
  python 25b_disformal_validation.py --run      -> medición completa
El --run solo se lanza tras las auditorías, con aprobación del autor
registrada en chat/commit.
"""

import json
import os
import sys

import numpy as np

SIGMA_M = 0.18
W_PHYS = 0.25
THETA = 0.5
AGRID = [0.05, 0.10, 0.20, 0.40]
NGRID = [1024, 2048, 4096]
NREAL = 24
VERDICT_CELLS = [(4096, 0.10), (4096, 0.20)]  # congelado (Enm. 2)
# Cuadratura compuesta: 8 subintervalos x GL16 = 128 nodos.
# GL16 simple FALLÓ V0c (err 7e-5): el bump sigma=0.18 es fino frente a
# segmentos de largo ~3. La compuesta resuelve la escala del bump.
_gx, _gw = np.polynomial.legendre.leggauss(16)
_gx = (_gx + 1) / 2
_gw = _gw / 2
_NSUB = 8
GAUSS_X = np.concatenate([(k + _gx) / _NSUB for k in range(_NSUB)])
GAUSS_W = np.concatenate([_gw / _NSUB for _ in range(_NSUB)])

R_CONST = None  # V0d: si se fija, R_field devuelve esa constante


def R_field(pos, alpha):
    if R_CONST is not None:
        return np.full(pos.shape[:-1], R_CONST)
    r2 = np.sum(pos ** 2, axis=-1)
    return 1.0 + alpha * np.exp(-0.5 * r2 / SIGMA_M ** 2)


def sprinkle(n, alpha_density, rng):
    """Poisson uniforme en sqrt(-g)=R^2 en el diamante |t|+|x|<1."""
    ts, xs = [], []
    rmax2 = (1 + alpha_density) ** 2
    while len(ts) < n:
        t = rng.uniform(-1, 1, 4 * n)
        x = rng.uniform(-1, 1, (4 * n, 3))
        r = np.linalg.norm(x, axis=1)
        m = np.abs(t) + r < 1.0
        t, x = t[m], x[m]
        acc = R_field(x, alpha_density) ** 2 / rmax2
        keep = rng.random(len(t)) < acc
        ts.extend(t[keep].tolist())
        xs.extend(x[keep].tolist())
    t = np.array(ts[:n])
    x = np.array(xs[:n])
    o = np.argsort(t)
    return t[o], x[o]


def optical_time(xi, xj, alpha):
    """Tiempo de vuelo óptico, segmento recto, Gauss-Legendre 16.
    Método CONGELADO (Enm. 4): por Fermat, usar la recta (geodésica
    óptica de alpha=0) da error O(alpha^2)."""
    d = np.linalg.norm(xj - xi, axis=-1)
    tot = np.zeros_like(d)
    for gx, gw in zip(GAUSS_X, GAUSS_W):
        p = xi + gx * (xj - xi)
        tot += gw * R_field(p, alpha) ** 2
    return tot * d


def optical_time_simpson(x1, x2, alpha, tol=1e-9):
    """Integrador INDEPENDIENTE (V0c): Simpson adaptativo escalar."""
    def f(s):
        p = x1 + s * (x2 - x1)
        return float(R_field(p[None, :], alpha)[0]) ** 2

    def rec(a, b, fa, fb, fm, whole, depth):
        m = 0.5 * (a + b)
        lm, rm = 0.5 * (a + m), 0.5 * (m + b)
        flm, frm = f(lm), f(rm)
        left = (m - a) / 6 * (fa + 4 * flm + fm)
        right = (b - m) / 6 * (fm + 4 * frm + fb)
        if depth > 40 or abs(left + right - whole) < 15 * tol:
            return left + right + (left + right - whole) / 15
        return (rec(a, m, fa, fm, flm, left, depth + 1)
                + rec(m, b, fm, fb, frm, right, depth + 1))

    fa, fb, fm = f(0.0), f(1.0), f(0.5)
    whole = (fa + 4 * fm + fb) / 6
    return rec(0.0, 1.0, fa, fb, fm, whole, 0) * float(
        np.linalg.norm(x2 - x1))


def causal_matrix(t, x, alpha, block=512):
    n = len(t)
    causal = np.zeros((n, n), dtype=bool)
    for i0 in range(0, n, block):
        i1 = min(i0 + block, n)
        for j0 in range(i0, n, block):
            j1 = min(j0 + block, n)
            dt = t[j0:j1][None, :] - t[i0:i1][:, None]
            tof = optical_time(x[i0:i1][:, None, :],
                               x[j0:j1][None, :, :], alpha)
            causal[i0:i1, j0:j1] = dt > tof
    np.fill_diagonal(causal, False)
    return causal


def proper_window_pairs(x, alpha, w_phys):
    mid = 0.5 * (x[:, None, :] + x[None, :, :])
    d = np.linalg.norm(x[None, :, :] - x[:, None, :], axis=-1)
    return R_field(mid, alpha) * d < w_phys


def coord_window_pairs(x, w):
    d = np.linalg.norm(x[None, :, :] - x[:, None, :], axis=-1)
    return d < w


def depth_local(causal, win):
    n = causal.shape[0]
    h = np.ones(n)
    for j in range(n):
        preds = np.flatnonzero(causal[:, j] & win[:, j])
        if len(preds):
            h[j] = 1 + h[preds].max()
    return h


def width_bk(causal, h, win, theta):
    n = causal.shape[0]
    past_count = causal.sum(axis=0)
    hr = np.rint(h).astype(int)
    w = np.zeros(n)
    for j in range(n):
        inc = ~(causal[:, j] | causal[j, :])
        cand = np.flatnonzero(inc & win[:, j] & (np.abs(hr - hr[j]) <= 1))
        cand = cand[cand != j]
        if not len(cand):
            continue
        pj = causal[:, j]
        cnt = 0
        for k in cand:
            mn = min(past_count[j], past_count[k])
            if mn == 0:
                continue
            if np.count_nonzero(pj & causal[:, k]) / mn >= theta:
                cnt += 1
        w[j] = cnt
    return w


def fit_exponent(Rvals, y, min_bin=30):
    ok = y > 0
    Rv, yv = Rvals[ok], y[ok]
    if len(Rv) < 3 * min_bin:
        return np.nan
    edges = np.quantile(Rv, np.linspace(0, 1, 9))
    lx, ly = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        m = (Rv >= a) & (Rv < b)
        if m.sum() >= min_bin:
            lx.append(np.log(Rv[m].mean()))
            ly.append(np.log(yv[m].mean()))
    if len(lx) < 3 or np.ptp(lx) == 0:
        return np.nan
    A = np.column_stack([np.ones(len(lx)), lx])
    co, *_ = np.linalg.lstsq(A, np.array(ly), rcond=None)
    return float(co[1])


def ms(v):
    v = np.array(v)
    v = v[np.isfinite(v)]
    if len(v) < 3:
        return (float("nan"), float("nan"))
    return (float(v.mean()), float(v.std(ddof=1) / np.sqrt(len(v))))


# ----------------------------------------------------------------------
# V0 — controles del integrador (anti-bug-17). Si uno falla, no se mide.
# ----------------------------------------------------------------------
def v0_block():
    global R_CONST
    print("--- V0: controles del integrador de conos ---", flush=True)
    rng = np.random.default_rng(259999)
    ok = True

    x1 = rng.uniform(-1, 1, (10000, 3))
    x2 = rng.uniform(-1, 1, (10000, 3))

    tof0 = optical_time(x1, x2, 0.0)
    d = np.linalg.norm(x2 - x1, axis=1)
    v0a = np.allclose(tof0, d, rtol=1e-12)
    print(f"  V0a Minkowski exacto (1e4 pares): {'PASA' if v0a else 'FALLA'}")
    ok &= v0a

    tA = optical_time(x1, x2, 0.4)
    tB = optical_time(x2, x1, 0.4)
    v0b = np.allclose(tA, tB, rtol=1e-12)
    print(f"  V0b simetría ida/vuelta (alpha=0.4): {'PASA' if v0b else 'FALLA'}")
    ok &= v0b

    # V0c: GL16 vs Simpson adaptativo INDEPENDIENTE, 200 pares, alpha=0.4
    errs = []
    for i in range(200):
        ref = optical_time_simpson(x1[i], x2[i], 0.4)
        got = float(optical_time(x1[i][None, :], x2[i][None, :], 0.4)[0])
        errs.append(abs(got - ref) / max(abs(ref), 1e-300))
    relmax = max(errs)
    v0c = relmax < 1e-6
    print(f"  V0c GL16x8 compuesta vs Simpson adaptativo indep.: max rel err "
          f"{relmax:.2e} {'PASA' if v0c else 'FALLA'}")
    ok &= v0c

    # V0d: PIPELINE REAL con R constante == Minkowski reescalado exacto
    rng2 = np.random.default_rng(260001)
    tt = np.sort(rng2.uniform(-1, 1, 400))
    xx = rng2.uniform(-0.5, 0.5, (400, 3))
    c = 1.3
    R_CONST = c
    try:
        got = causal_matrix(tt, xx, alpha=0.0)
    finally:
        R_CONST = None
    dtm = tt[None, :] - tt[:, None]
    dmat = np.linalg.norm(xx[None, :, :] - xx[:, None, :], axis=-1)
    expected = dtm > c ** 2 * dmat
    np.fill_diagonal(expected, False)
    v0d = np.array_equal(got, expected)
    print(f"  V0d pipeline real con R=1.3 == Minkowski reescalado: "
          f"{'PASA' if v0d else 'FALLA'}")
    ok &= v0d
    return ok


def run_cell(n, alpha, ia, i_n, *, coord_window=False, shuffle=False,
             theta=THETA, w_phys=W_PHYS, flat_metric_biased_density=False,
             seed_base=260000):
    """flat_metric_biased_density=True -> C5: densidad R(alpha)^2 pero
    métrica plana; fit contra el perfil R(alpha). Predicción analítica
    (+0.5, +1.5)."""
    ph, pw = [], []
    for r in range(NREAL):
        seed = seed_base + 1000 * ia + 100 * i_n + r
        rng = np.random.default_rng(seed)
        t, x = sprinkle(n, alpha, rng)
        a_metric = 0.0 if flat_metric_biased_density else alpha
        causal = causal_matrix(t, x, a_metric)
        Rv = R_field(x, alpha)
        if shuffle:
            Rv = rng.permutation(Rv)
        win = (coord_window_pairs(x, w_phys) if coord_window
               else proper_window_pairs(x, a_metric, w_phys))
        h = depth_local(causal, win)
        w = width_bk(causal, h, win, theta)
        ph.append(fit_exponent(Rv, h))
        pw.append(fit_exponent(Rv, w))
    return {"p_h": ms(ph), "p_w": ms(pw)}


def verdict(cells):
    """S1'/F1'/F2' congelados (Enm. 2) sobre las celdas de veredicto.
    Error del PROMEDIO: sqrt(sum se_i^2)/n — la versión RMS anterior
    inflaba sigma por sqrt(2) y ablandaba el criterio (audit Codex v2)."""
    n = len(cells)
    mh = np.mean([c["p_h"][0] for c in cells])
    sh = np.sqrt(np.sum([c["p_h"][1] ** 2 for c in cells])) / n
    mw = np.mean([c["p_w"][0] for c in cells])
    sw = np.sqrt(np.sum([c["p_w"][1] ** 2 for c in cells])) / n
    budget = mh + mw
    sb = np.hypot(sh, sw)
    s1 = abs(mh - (-1)) < 3 * sh and abs(mw - 3) < 3 * sw
    budget_ok = abs(budget - 2) < 3 * sb
    if s1:
        v = "S1' — (-1,+3) recuperado: estimadores validados, TEOREMA->MEDIDO"
    elif budget_ok:
        v = "F1' — presupuesto +2 pasa, split NO disforme: investigar estimadores"
    else:
        v = "F2' — presupuesto NO cierra: ALARMA, revisar construccion/teorema"
    return {"p_h": [mh, sh], "p_w": [mw, sw],
            "budget": [budget, sb], "verdict": v}


if __name__ == "__main__":
    v0_ok = v0_block()
    if "--run" not in sys.argv:
        print("\nModo V0-only (por defecto). Medición: --run tras "
              "auditorías, con aprobación del autor (Enmienda 4).")
        sys.exit(0 if v0_ok else 2)
    if not v0_ok:
        print("V0 FALLA — la medición NO corre.")
        sys.exit(2)

    out = {"prereg": "exp25b + Enm.2/3/4", "grid": {}, "controls": {}}
    print("\nEXP 25b — validación disforme: predicción (p_h,p_w)=(-1,+3)",
          flush=True)
    vcells = []
    for i_n, n in enumerate(NGRID):
        for ia, alpha in enumerate(AGRID):
            cell = run_cell(n, alpha, ia, i_n)
            out["grid"][f"n{n}_a{alpha}"] = cell
            if (n, alpha) in VERDICT_CELLS:
                vcells.append(cell)
            (mh, sh), (mw, sw) = cell["p_h"], cell["p_w"]
            print(f"n={n} a={alpha}: p_h={mh:+.2f}±{sh:.2f} "
                  f"p_w={mw:+.2f}±{sw:.2f} presupuesto={mh + mw:+.2f}",
                  flush=True)

    print("\n--- Controles ---", flush=True)
    out["controls"]["C1_ghost"] = run_cell(
        2048, 0.0, 0, 1, seed_base=269000)
    # C1': fit contra perfil fantasma — se recalcula con R(0.2) sobre flat:
    ph, pw = [], []
    for r in range(NREAL):
        rng = np.random.default_rng(269000 + r)
        t, x = sprinkle(2048, 0.0, rng)
        causal = causal_matrix(t, x, 0.0)
        win = proper_window_pairs(x, 0.0, W_PHYS)
        h = depth_local(causal, win)
        w = width_bk(causal, h, win, THETA)
        Rg = R_field(x, 0.20)
        ph.append(fit_exponent(Rg, h))
        pw.append(fit_exponent(Rg, w))
    out["controls"]["C1_ghost"] = {"p_h": ms(ph), "p_w": ms(pw)}
    print(f"C1' fantasma: p_h={ms(ph)[0]:+.2f} p_w={ms(pw)[0]:+.2f} (~0 o es "
          "el confound radial)", flush=True)
    out["controls"]["C2_shuffle"] = run_cell(2048, 0.20, 2, 1, shuffle=True)
    print(f"C2 shuffle: p_h={out['controls']['C2_shuffle']['p_h'][0]:+.2f} "
          f"p_w={out['controls']['C2_shuffle']['p_w'][0]:+.2f} (~0)",
          flush=True)
    for th in (0.3, 0.7):
        out["controls"][f"C3_theta{th}"] = run_cell(4096, 0.20, 2, 2,
                                                    theta=th)
        print(f"C3 theta={th}: listo", flush=True)
    for wp in (0.15, 0.35):
        out["controls"][f"C4_W{wp}"] = run_cell(4096, 0.20, 2, 2,
                                                w_phys=wp)
        print(f"C4 W={wp}: listo", flush=True)
    out["controls"]["C5_positive_flat"] = run_cell(
        2048, 0.20, 2, 1, flat_metric_biased_density=True)
    c5 = out["controls"]["C5_positive_flat"]
    print(f"C5 positivo (predicción +0.5,+1.5): p_h={c5['p_h'][0]:+.2f}"
          f"±{c5['p_h'][1]:.2f} p_w={c5['p_w'][0]:+.2f}±{c5['p_w'][1]:.2f}",
          flush=True)
    out["controls"]["C6_coord_window"] = run_cell(4096, 0.20, 2, 2,
                                                  coord_window=True)

    out["verdict"] = verdict(vcells)

    # Robustez automática (audit Codex v2): C3/C4/C6 sustituyen a la
    # celda de referencia (n4096, a0.2); la CATEGORÍA no debe cambiar.
    base_cat = out["verdict"]["verdict"].split("'")[0] + "'"
    out["robustness"] = {}
    for name in ("C3_theta0.3", "C3_theta0.7", "C4_W0.15", "C4_W0.35",
                 "C6_coord_window"):
        alt = verdict([vcells[0], out["controls"][name]])
        alt_cat = alt["verdict"].split("'")[0] + "'"
        same = alt_cat == base_cat
        out["robustness"][name] = {"category": alt_cat, "same": same}
        print(f"robustez {name}: {alt_cat} "
              f"{'== base OK' if same else '!= base — VEREDICTO NO ROBUSTO'}")
    out["robust_all"] = all(r["same"] for r in out["robustness"].values())
    if not out["robust_all"]:
        print("ATENCION: el veredicto cambia de categoria bajo controles "
              "de robustez — se reporta como NO ROBUSTO (prereg C3/C4).")

    print("\n=== VEREDICTO (celdas congeladas N=4096, alpha=0.1/0.2) ===")
    print(f"p_h = {out['verdict']['p_h'][0]:+.3f} ± "
          f"{out['verdict']['p_h'][1]:.3f}  (target -1)")
    print(f"p_w = {out['verdict']['p_w'][0]:+.3f} ± "
          f"{out['verdict']['p_w'][1]:.3f}  (target +3)")
    print(f"presupuesto = {out['verdict']['budget'][0]:+.3f} ± "
          f"{out['verdict']['budget'][1]:.3f}  (target +2)")
    print(out["verdict"]["verdict"])

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/exp25b_results.json", "w") as f:
        json.dump(out, f, indent=1)
    print("DONE — outputs/exp25b_results.json", flush=True)
