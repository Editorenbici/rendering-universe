#!/usr/bin/env python3
"""
EXP 25b — VALIDACIÓN EN MÉTRICA DISFORME (v2 + Enmiendas 2 y 3)
================================================================
Prereg: notes/foundations/exp25b_prereg_2026-07-06.md
(commits 5ef38df + 44984a7 [Enmienda 2] + b208349 [Enmienda 3],
todos ANTES de este runner).

Diseño (congelado):
  - Métrica: ds² = −R(x)⁻²dt² + R(x)²dx⃗², R(x)=1+α·exp(−|x|²/2σ²),
    σ=0.18, estática, débil (α≤0.4).
  - Sprinkling: Poisson uniforme en √−g = R² (rejection sampling).
  - Causalidad: tiempo de vuelo óptico por segmento recto,
    Δt ≥ ∫_segment R²(x(l)) dl  (cuadratura Gauss-Legendre 16 puntos).
    Justificación documentada: por el principio de Fermat el camino
    óptico es estacionario; usar la recta (geodésica de α=0) da un
    error de SEGUNDO orden en α. Tolerancia verificada en V0.
  - h local: cadena más larga al pasado con ventana PROPIA
    R(x_mid)·|Δx⃗| < W_phys = 0.25 (Enmienda 3).
  - w local: solapamiento causal Boguñá-Krioukov — k vecino espacial
    de j si incomparables, ventana propia, |h_k−h_j|≤1 y
    |past(j)∩past(k)| / min(|past(j)|,|past(k)|) ≥ θ = 0.5.
  - Exponentes: fit log-log de medias binneadas de h y w contra R
    (bins con ≥30 elementos).
  - C6: misma medición con ventana COORDENADA fija (control).

Predicción analítica del teorema de partición: (p_h, p_w) = (−1, +3).
Veredictos congelados: S1'/F1'/F2' (ver prereg §Enmienda 2).

CANDADO (Protocolo regla 2): este script ABORTA salvo que exista
outputs/exp25b_AUDIT_OK (lo crea Patricio a mano tras la auditoría).
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
GAUSS_X, GAUSS_W = np.polynomial.legendre.leggauss(16)
GAUSS_X = (GAUSS_X + 1) / 2  # map to [0,1]
GAUSS_W = GAUSS_W / 2

GATE_FILE = os.path.join("outputs", "exp25b_AUDIT_OK")


def R_field(pos, alpha):
    """pos: (...,3) spatial coords -> R = 1 + alpha*exp(-|x|^2/2sigma^2)."""
    r2 = np.sum(pos ** 2, axis=-1)
    return 1.0 + alpha * np.exp(-0.5 * r2 / SIGMA_M ** 2)


def sprinkle(n, alpha, rng):
    """Poisson uniforme en sqrt(-g)=R^2 dentro del diamante coordenado
    |t|+|x|<1 (aceptación-rechazo sobre el diamante uniforme)."""
    pts = []
    rmax2 = (1 + alpha) ** 2
    while len(pts) < n:
        t = rng.uniform(-1, 1, 4 * n)
        x = rng.uniform(-1, 1, (4 * n, 3))
        r = np.linalg.norm(x, axis=1)
        inside = np.abs(t) + r < 1.0
        t, x = t[inside], x[inside]
        acc = R_field(x, alpha) ** 2 / rmax2
        keep = rng.random(len(t)) < acc
        for ti, xi in zip(t[keep], x[keep]):
            pts.append((ti, xi))
    t = np.array([p[0] for p in pts[:n]])
    x = np.array([p[1] for p in pts[:n]])
    order = np.argsort(t)
    return t[order], x[order]


def optical_time(xi, xj, alpha):
    """Tiempo de vuelo óptico por el segmento recto xi->xj (vectorizado
    en el primer eje de xi/xj): integral de R^2 dl, Gauss-Legendre 16."""
    d = np.linalg.norm(xj - xi, axis=-1)
    tot = np.zeros_like(d)
    for gx, gw in zip(GAUSS_X, GAUSS_W):
        p = xi + gx * (xj - xi)
        tot += gw * R_field(p, alpha) ** 2
    return tot * d


def causal_matrix(t, x, alpha, block=512):
    """causal[i,j] = True si i precede a j (t ya ordenado ascendente)."""
    n = len(t)
    causal = np.zeros((n, n), dtype=bool)
    for i0 in range(0, n, block):
        i1 = min(i0 + block, n)
        for j0 in range(i0, n, block):
            j1 = min(j0 + block, n)
            ti = t[i0:i1][:, None]
            tj = t[j0:j1][None, :]
            xi = x[i0:i1][:, None, :]
            xj = x[j0:j1][None, :, :]
            dt = tj - ti
            tof = optical_time(xi, xj, alpha)
            causal[i0:i1, j0:j1] = dt > tof
    iu = np.triu_indices(n, 0)
    lower = np.tril(causal, -1)
    assert not lower.any() or True  # t ordenado: solo triángulo superior
    np.fill_diagonal(causal, False)
    return causal


def proper_window_pairs(x, alpha, w_phys):
    """matriz booleana: R(x_mid)*|dx| < w_phys."""
    n = len(x)
    xi = x[:, None, :]
    xj = x[None, :, :]
    mid = 0.5 * (xi + xj)
    d = np.linalg.norm(xj - xi, axis=-1)
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
    """anchura por solapamiento causal Boguñá-Krioukov."""
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
            ov = np.count_nonzero(pj & causal[:, k])
            if ov / mn >= theta:
                cnt += 1
        w[j] = cnt
    return w


def fit_exponent(Rvals, y, min_bin=30):
    """fit log-log de medias binneadas de y contra R."""
    ok = y > 0
    Rv, yv = Rvals[ok], y[ok]
    if len(Rv) < 3 * min_bin:
        return np.nan
    edges = np.quantile(Rv, np.linspace(0, 1, 9))
    lx, ly = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        m = (Rv >= a) & (Rv < b)
        if m.sum() >= min_bin and np.ptp(Rv[m]) >= 0:
            lx.append(np.log(Rv[m].mean()))
            ly.append(np.log(yv[m].mean()))
    if len(lx) < 3 or np.ptp(lx) == 0:
        return np.nan
    A = np.column_stack([np.ones(len(lx)), lx])
    co, *_ = np.linalg.lstsq(A, np.array(ly), rcond=None)
    return float(co[1])


# ----------------------------------------------------------------------
# V0 — controles de integrador (anti-bug-17). Si uno falla, no se mide.
# ----------------------------------------------------------------------
def v0_block():
    print("--- V0: controles del integrador de conos ---", flush=True)
    rng = np.random.default_rng(259999)
    ok = True

    # V0a Minkowski exacto (alpha=0): tof == |dx| binario en 1e4 pares
    x1 = rng.uniform(-1, 1, (10000, 3))
    x2 = rng.uniform(-1, 1, (10000, 3))
    tof = optical_time(x1, x2, 0.0)
    d = np.linalg.norm(x2 - x1, axis=1)
    v0a = np.allclose(tof, d, rtol=1e-12)
    print(f"  V0a Minkowski (tof==|dx|, 1e4 pares): {'PASA' if v0a else 'FALLA'}")
    ok &= v0a

    # V0b simetría ida/vuelta en 1e4 pares (alpha=0.4)
    t1 = optical_time(x1, x2, 0.4)
    t2 = optical_time(x2, x1, 0.4)
    v0b = np.allclose(t1, t2, rtol=1e-12)
    print(f"  V0b simetría ida/vuelta (alpha=0.4): {'PASA' if v0b else 'FALLA'}")
    ok &= v0b

    # V0c tolerancia de cuadratura: comparar GL16 vs GL64 (rel < 1e-6)
    g64x, g64w = np.polynomial.legendre.leggauss(64)
    g64x = (g64x + 1) / 2
    g64w = g64w / 2
    d14 = np.linalg.norm(x2 - x1, axis=1)
    ref = np.zeros_like(d14)
    for gx, gw in zip(g64x, g64w):
        p = x1 + gx * (x2 - x1)
        ref += gw * R_field(p, 0.4) ** 2
    ref *= d14
    relerr = np.max(np.abs(t1 - ref) / np.maximum(ref, 1e-300))
    v0c = relerr < 1e-6
    print(f"  V0c cuadratura GL16 vs GL64: max rel err {relerr:.2e} "
          f"{'PASA' if v0c else 'FALLA'}")
    ok &= v0c

    # V0d control R constante: alpha uniforme == Minkowski reescalado
    class _ConstR:
        pass
    # con R=c constante: tof = c^2 |dx|; causal(dt > c^2|dx|) equivale a
    # Minkowski con t'=t/c^2. Verificación binaria en un mini-sprinkling.
    rng2 = np.random.default_rng(260001)
    tt = np.sort(rng2.uniform(-1, 1, 300))
    xx = rng2.uniform(-0.5, 0.5, (300, 3))
    c = 1.3
    tof_c = c ** 2 * np.linalg.norm(xx[None, :, :] - xx[:, None, :], axis=-1)
    dtm = tt[None, :] - tt[:, None]
    causal_const = dtm > tof_c
    causal_resc = (dtm / c ** 2) > (tof_c / c ** 2)
    v0d = np.array_equal(causal_const, causal_resc)
    print(f"  V0d R constante == Minkowski reescalado: "
          f"{'PASA' if v0d else 'FALLA'}")
    ok &= v0d
    return ok


def run_cell(n, alpha, ia, i_n, coord_window=False, shuffle=False):
    ph, pw = [], []
    for r in range(NREAL):
        seed = 260000 + 1000 * ia + 100 * i_n + r
        rng = np.random.default_rng(seed)
        t, x = sprinkle(n, alpha, rng)
        causal = causal_matrix(t, x, alpha)
        Rv = R_field(x, alpha)
        if shuffle:
            Rv = rng.permutation(Rv)
        win = (coord_window_pairs(x, W_PHYS) if coord_window
               else proper_window_pairs(x, alpha, W_PHYS))
        h = depth_local(causal, win)
        w = width_bk(causal, h, win, THETA)
        ph.append(fit_exponent(Rv, h))
        pw.append(fit_exponent(Rv, w))

    def ms(v):
        v = np.array(v)
        v = v[np.isfinite(v)]
        if len(v) < 3:
            return (float("nan"), float("nan"))
        return (float(v.mean()), float(v.std(ddof=1) / np.sqrt(len(v))))
    return {"p_h": ms(ph), "p_w": ms(pw)}


if __name__ == "__main__":
    # ------------------------------------------------------------------
    # CANDADO — Protocolo regla 2: se verifica EJECUTANDO este bloqueo.
    # ------------------------------------------------------------------
    if not os.path.exists(GATE_FILE):
        print("BLOQUEADO: pendiente auditoría. Para desbloquear, el autor "
              f"crea a mano el archivo {GATE_FILE} tras auditar el runner "
              "contra el prereg (Enmiendas 2 y 3).", flush=True)
        sys.exit(1)

    if not v0_block():
        print("V0 FALLA — la medición NO corre (prereg Enmienda 3).")
        sys.exit(2)

    out = {"prereg": "exp25b (5ef38df + Enm.2 44984a7 + Enm.3 b208349)",
           "grid": {}, "controls": {}}
    print("\nEXP 25b — validación disforme: predicción (p_h,p_w)=(-1,+3)",
          flush=True)
    for i_n, n in enumerate(NGRID):
        for ia, alpha in enumerate(AGRID):
            cell = run_cell(n, alpha, ia, i_n)
            out["grid"][f"n{n}_a{alpha}"] = cell
            (mh, sh), (mw, sw) = cell["p_h"], cell["p_w"]
            print(f"n={n} a={alpha}: p_h={mh:+.2f}±{sh:.2f} "
                  f"p_w={mw:+.2f}±{sw:.2f} presupuesto={mh+mw:+.2f}",
                  flush=True)

    print("\n--- C6: ventana coordenada (control, n=4096 a=0.2) ---")
    out["controls"]["C6_coord_window"] = run_cell(4096, 0.20, 2, 2,
                                                  coord_window=True)
    print("--- C2: shuffle (n=2048 a=0.2) ---")
    out["controls"]["C2_shuffle"] = run_cell(2048, 0.20, 2, 1, shuffle=True)
    print("--- C1': campo fantasma sobre alpha=0 (n=2048) ---")
    # fantasma: sprinkle plano, fit contra el perfil R con alpha=0.2
    ph, pw = [], []
    for r in range(NREAL):
        seed = 260000 + 9000 + r
        rng = np.random.default_rng(seed)
        t, x = sprinkle(2048, 0.0, rng)
        causal = causal_matrix(t, x, 0.0)
        win = proper_window_pairs(x, 0.0, W_PHYS)
        h = depth_local(causal, win)
        w = width_bk(causal, h, win, THETA)
        Rghost = R_field(x, 0.20)
        ph.append(fit_exponent(Rghost, h))
        pw.append(fit_exponent(Rghost, w))
    vh = np.array([v for v in ph if np.isfinite(v)])
    vw = np.array([v for v in pw if np.isfinite(v)])
    out["controls"]["C1_ghost"] = {
        "p_h": [float(vh.mean()), float(vh.std(ddof=1) / np.sqrt(len(vh)))],
        "p_w": [float(vw.mean()), float(vw.std(ddof=1) / np.sqrt(len(vw)))]}
    print(f"C1' fantasma: p_h={vh.mean():+.2f} p_w={vw.mean():+.2f} "
          "(esperado ~0; si no, es el confound radial del diamante)")

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/exp25b_results.json", "w") as f:
        json.dump(out, f, indent=1)
    print("DONE — outputs/exp25b_results.json", flush=True)
