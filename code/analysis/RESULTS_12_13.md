# Resultados pre-registrados: Experimentos 12 (2D) y 13 (4D)

Fecha: 2026-07-01. Pre-registro escrito y auditado ANTES de cada run.
Compromiso: publicar salga como salga. Salió como sigue.

## Experimento 12 — 2D (1+1): conteo causal como propagador de Johnston

Pipeline: sprinkling Poisson uniforme (BHS) + materia como elementos
marcados + ψ = ½·(conteo de fuentes en el pasado causal) = G_R·q con
G_R = ½C (Johnston 2D). 100 realizaciones/configuración.

| Criterio | Resultado |
|---|---|
| E1: δψ ∝ Δh | PASA — exponente 1.0015 ± 0.0030 |
| E2: δψ ∝ masa (w) | PASA — exponente 1.0017 ± 0.0026 |
| E3: independiente de r (firma 2D; NO 1/r en 1+1D) | PASA — exponente −0.0011 ± 0.0025; modelo 1/r excluido por 407σ |
| E4: meseta en t₀ | Fallo marginal (2.13σ) → réplica pre-declarada N=400, semillas frescas: PASA (máx 1.18σ) |
| E5: estabilidad en ρ | PASA (0.25σ) |
| N1/N2: controles nulos | PASAN |

**Veredicto 2D: ÉXITO.** Acuerdo con la solución retardada continua al
0.2–0.4%. Cláusula crítica: el éxito 2D NO valida 4D (la Green 2D es el
interior del cono; la 4D vive sobre su superficie).

## Experimento 13 — 4D (3+1): el test decisivo del kernel

Dos brazos sobre el mismo sprinkling: (a) conteo crudo del interior de
J⁻(e); (b) conteo de links (propagador de Johnston 4D,
K = √(ρ/6)/2π, arXiv:0806.3083). Bola estática a=3, ρ=1, 250
realizaciones por r ∈ {8, 12, 17, 24}.

**Brazo (b) — links: REPRODUCE NEWTON.**
- Potencial ∝ 1/r: exponente −0.984 ± 0.031 (0 excluido por 32σ)
- Fuerza ∝ 1/r²: exponente −2.03 ± 0.23
- Estático: plano en t₀ (máx 1.14σ)
- Normalización de Johnston verificada al 1–3% sin parámetros ajustados

**Brazo (a) — conteo crudo: NO ES NEWTON.**
- Fuerza independiente de r: exponente −2 excluido por 523σ
- Sin límite estático: ψ_a crece como ρV·t₀ (pendiente 113.5 ± 0.4;
  teoría ρV = 113.1)
- Residuo r-dependiente (exponente +0.019 ± 0.004) verificado como la
  corrección exacta de bola finita (ley de distancia media,
  d̄ = r + a²/5r): los 4 puntos dentro de 2σ de la integral exacta
  (13b, máx 1.92σ)

**Conclusión pre-registrada (4D):**
ℛ como conteo crudo del pasado causal FALLA como mecanismo
gravitacional en 3+1D. ℛ como conteo de links (Johnston) reproduce el
kernel newtoniano cuantitativamente. El Postulado 6 se reformula en
términos de conteo de links.

**Honestidad de alcance:** esto confirma numéricamente un resultado
conocido de CST (Johnston 2008), no descubre física nueva; el aporte a
Render es reemplazar una narrativa por un mecanismo definido y testeado,
y descartar la versión original del postulado. Este resultado NO
resuelve SPARC ni el Bullet Cluster: links + bariones = Newton, por lo
que las curvas de rotación planas requieren física adicional aún no
derivada.

Scripts: `12_sprinkling_pound_rebka.py`, `12b_replica_E4.py`,
`13_sprinkling_4d_kernel.py`, `13b_verificacion_F3.py`.
