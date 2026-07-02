# Resultados pre-registrados: Experimento 16 — Derivación del acople ISW

Fecha: 2026-07-01. Pre-registro en el docstring de
`16_derive_isw_coupling.py` (hipótesis y predicciones escritas antes
del run). Compromiso: publicar salga como salga.

## Veredicto

| Criterio | Resultado |
|---|---|
| C1 — amplitud derivable | **PASA**: A_emp=0.0024 dentro del rango H2 (nota: rango ancho por β²; el test discriminante es C2) |
| C2 — consistencia inter-datasets | **PASA**: β_ISW = 0.045 vs β_BAO = 0.055 (68%: 0.005–0.100) |
| C3 — forma en z derivada | **FALLA** (χ²=2111 vs 2.3 del fit empírico): el mecanismo predice crecimiento suave con z; los datos decaen como exp(−z/0.3) |
| C4 — H1 (potencial estático) descartado | **CONFIRMADO**: falla por ~13,000× |

## El hallazgo principal (C2)

La fórmula sin parámetros nuevos
`A = γ·β²·|δ₀|·I(0)/(H₀t₀)`, con I(0)=1.63 (integral de crecimiento en
la cosmología del mejor ajuste del exp 15), reproduce A=0.0024 para
**β = 0.045** — dentro del 68% del β medido con BAO (exp 15: 0.055).
Dos datasets completamente independientes (expansión BAO de DESI y
stacking ISW de voids) apuntan a la misma tasa de refinamiento. A ~ β²
era, hasta hoy, un número calibrado; ahora es una postdicción.

## Los dos resultados negativos (igual de importantes)

1. **C4**: el potencial estático de links (el mecanismo validado en el
   exp 13 para gravedad) da A ~ 2×10⁻⁷ — cuatro órdenes corto. El ISW
   anómalo NO viene del potencial instantáneo: viene del **déficit
   histórico de refinamiento** del void (sector cosmológico). La
   consistencia teórica entre ambos sectores (links para estática,
   déficit acumulado para evolución) es un requisito abierto del marco.
2. **C3**: la dependencia en z NO queda derivada. H2 sobrepredice ~10×
   en z=0.35–0.55. El z₀=0.30 sigue siendo empírico; candidatos a
   explicación: evolución de δ₀(z), selección de catálogos de voids,
   efectos de proyección fotométrica. Abierto.

## Implicación para el experimento 1 (stacking DESI×Planck)

La predicción de ~14 µK a z~0.3 usa el fit empírico (que ajusta los 5
puntos existentes con χ²=2.3). La derivación H2 respalda la AMPLITUD a
z≈0 pero no la extrapolación en z. El stacking a z~0.3 discrimina
también entre la forma empírica y H2 (que predice ~5× más señal ahí):
el test es doblemente informativo.
