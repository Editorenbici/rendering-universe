# Resultados pre-registrados: Experimento 18 — Ley de crecimiento de la valencia

Fecha del unblinding: 2026-07-04 (wrapper ejecutado una sola vez tras
autorización del autor; JSON: `outputs/exp18c/exp18_audit_20260702_223954.json`).
Pre-registro y enmiendas commiteados ANTES del run (00bf25f, 15bcbcf).
Compromiso: publicar salga como salga. Salió como sigue.

## Controles (pre-requisito del unblinding)

| Control | Predicción analítica | Medido | Estado |
|---|---|---|---|
| 2D (18a) | v = 2·ln(depth) + c | pendiente 2.01±0.12; plana en N | ✅ |
| 4D Minkowski (18b) | v = π√6·√ρ·T² ≈ 7.695·T² | p = 2.089±0.025; amplitud al 5% | ✅ |

## FASE FRW — VEREDICTO: F1 FALLÓ (la predicción de Fable refutada)

Predicción congelada: v ∝ t² (exponente 2, amplitud 3/5 de Minkowski).

**Medido: p_η = 2.700 ± 0.071** — a 10σ del 2 predicho.

| η_e | ⟨v⟩ | teoría (0.513·η²) | ratio |
|---|---|---|---|
| 6 | 2.7±0.3 | 18.5 | 0.146 |
| 9 | 9.9±0.6 | 41.6 | 0.238 |
| 12 | 21.2±0.8 | 73.9 | 0.288 |
| 16 | 46.4±1.5 | 131.3 | 0.353 |
| 20 | 79.5±3.4 | 205.2 | 0.387 |

F1: FALLA | F2: FALLA | F2' (convergencia monótona): PASA.
Veredicto pre-registrado aplicable: *"la expansión SÍ reforma la ley de
links; se publica el exponente medido y se recalcula la rama."*

## Caveat honesto (registrado junto al veredicto, no en su lugar)

Los ratios crecen monótonamente (0.146→0.387): los datos son
consistentes con DOS lecturas que este rango de η no puede separar:
(a) exponente asintótico genuinamente ≈2.7, o (b) exponente 2 con una
amplitud que converge lento (transitorio de tamaño finito, que
contamina el fit: 2 + dln f/dln η ≈ 2.8 con los ratios medidos).
Separarlas requiere η mayor o un fit con modelo de convergencia — eso
sería un 18d PRE-REGISTRADO, no una reinterpretación de este veredicto.
El veredicto del pre-registro se mantiene tal como disparó.

## Implicaciones para el árbol de las dos ℛ (lo robusto)

Lo notable: las conclusiones de rama son ROBUSTAS frente a la
incertidumbre entre p=2 y p=2.7:

1. **Rama A (Hartley, log₂v ~ p·ln t): VIVA con cualquier p ∈ [2,3]** —
   el logaritmo de una ley de potencias es logarítmico sea cual sea el
   exponente. El sector refinamiento-DE logarítmico no depende de
   resolver el caveat.
2. **Rama B (ρ_DE ∝ 1/v): MUERTA con más fuerza** — v ∝ t^2.7 decae
   incluso más rápido que el tracker t². Segunda muerte de la rama B
   (tras el Exp 19), ahora robusta al caveat.
3. **La "triple coincidencia de área" (valencia ~ horizonte ~ Lloyd) se
   DEBILITA**: en FRW, a este rango, la valencia NO escala como el área
   (2.7 ≠ 2). Si la lectura (a) se confirma, esa coincidencia era un
   artefacto del caso Minkowski. Honestidad: una coincidencia menos.

## Incidentes operativos (lección para el protocolo)

Dos crashes previos al run real, ambos por ediciones cosméticas al
wrapper POSTERIORES a la auditoría (docstring sin comillas de apertura;
carácter ✔ no-cp1252). Ninguno ejecutó medición alguna (blinding
intacto, verificado por la naturaleza de los errores: parseo y print
del paso 1). Lección adoptada: **el wrapper se congela junto con el
experimento en la auditoría** — ninguna edición post-auditoría, ni
cosmética.

## Nota de crédito

La servilleta refutada era de Fable (predicción v ∝ t², amplitud 3/5).
El experimento la mató a 10σ. Así debe ser: las predicciones de la
herramienta se someten al mismo régimen que las del autor.

## Anexo de reproducibilidad (Opción A del autor, 2026-07-04)

**Reproducción determinista verificada (Fable):**
- Commit: `a192ad1` | SHA256 del script: `14f6a0650da1fe76`
- Entorno: Python 3.11.9, numpy 2.4.4
- Re-ejecución del script commiteado (UNBLIND=True en copia temporal,
  mismas semillas deterministas `[seed, int(eta*10), 18]`, seeds 0–19):
  **p_eta = 2.700 ± 0.071**, stdout SHA256 `15ea1f1d7fa7273d`.

**Protocolo para Codex:** correr el archivo EXACTO del commit
`a192ad1` (verificar SHA del script), mismo numpy si es posible, y
comparar el hash del stdout. El script es determinista: cualquier
desviación de 2.700 indica código distinto o entorno distinto, no azar.

**Diagnóstico de la discrepancia 2.700 vs 2.950 (pendiente de la
corrida de Codex):** el error de Codex (±0.003) es ~24× menor que el
que la estadística del script commiteado permite (con v(η=6)=2.7±0.3
sobre 20 realizaciones, ningún fit puede dar σ_p=0.003; harían falta
~10⁴ realizaciones). Eso indica un ESTIMADOR distinto, no las mismas
cuentas con otra suerte — consistente con el "importance sampling"
anunciado: si estima links con la probabilidad blanda
exp(−ρ_local·V) en lugar del chequeo exacto de bloqueadores, mide la
APROXIMACIÓN LOCAL (la misma que usaba la servilleta refutada), no el
conteo de links del pre-registro. La cantidad pre-registrada es el
link exacto (sin elemento intermedio): **el resultado del Exp 18 es
p = 2.700 ± 0.071**; el 2.95 quedará documentado, si se confirma su
origen, como el sistemático de usar la aproximación local en FRW.
