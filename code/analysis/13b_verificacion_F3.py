#!/usr/bin/env python3
"""
VERIFICACION PRE-DECLARADA DE F3 (exp 13).
El exponente medido del conteo crudo fue 0.019 +- 0.004 (4.9 sigma de 0,
fallo por la letra del pre-registro), con -2 excluido por 523 sigma.
HIPOTESIS DECLARADA ANTES DE CORRER: el 0.019 es la correccion
geometrica exacta de bola finita: el conteo crudo mide la DISTANCIA
MEDIA a la bola, d_bar(r) = r + a^2/(5r) + O(a^4/r^3), no r.
Prediccion exacta:  delta_Na(r) = rho * Int_bola (|y-x_t| - |y-x_b|) d3y
CRITERIO: los 4 valores medidos dentro de 2 sigma de la integral exacta.
Si PASA: el conteo crudo sigue la ley de conteo-distancia (no-Newton),
totalmente entendida. Si FALLA: hay un efecto no comprendido.
"""
import numpy as np

RHO, A, DH = 1.0, 3.0, 4.0
R_LIST = [8.0, 12.0, 17.0, 24.0]
MEDIDOS = [(441.6, 1.2), (449.4, 1.3), (448.6, 1.3), (450.8, 1.2)]

# Integral exacta por Monte Carlo de alta precision (10^7 puntos en bola)
rng = np.random.default_rng(42)
N_MC = 10_000_000
# muestreo uniforme en bola: rechazo desde el cubo
pts = rng.uniform(-A, A, (int(N_MC * 2.2), 3))
pts = pts[np.sum(pts ** 2, axis=1) <= A * A][:N_MC]
V = (4.0 / 3.0) * np.pi * A ** 3

print("VERIFICACION F3: conteo crudo vs integral exacta de bola finita")
print(f"{'r':>5} {'medido':>14} {'exacto (MC)':>12} {'sigma':>7}")
ok = True
for r, (m, s) in zip(R_LIST, MEDIDOS):
    db = np.sqrt((pts[:, 0] - r) ** 2 + pts[:, 1] ** 2 + pts[:, 2] ** 2)
    dt = np.sqrt((pts[:, 0] - (r + DH)) ** 2 + pts[:, 1] ** 2 + pts[:, 2] ** 2)
    diff = (dt - db).mean()
    err_mc = (dt - db).std() / np.sqrt(N_MC)
    exacto = RHO * V * diff
    err_ex = RHO * V * err_mc
    nsig = abs(m - exacto) / np.hypot(s, err_ex)
    ok &= nsig < 2.0
    print(f"{r:>5.0f} {m:>9.1f}+-{s:<4.1f} {exacto:>12.2f} {nsig:>7.2f}")

print(f"\nNaive rho*V*dh = {RHO*V*DH:.1f} (sin correccion de bola)")
msg = ("PASA - conteo crudo = ley de distancia media, no-Newton entendido"
       if ok else "FALLA - efecto no comprendido")
print(f"VERIFICACION: {msg}")
