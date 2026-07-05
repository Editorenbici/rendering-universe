# Paper 1 — Esqueleto (Fable, 2026-07-06)

**Título de trabajo:** *Counting laws of links in Poisson-sprinkled
causal sets: IR-cutoff valency, FRW transients, and three-sector
accounting*

**Audiencia:** comunidad CST (Yazdi, Zalel, Surya, Dowker, Wallden).
**Vehículo:** Zenodo (PDF CC-BY 4.0, código MIT, DOI) → email a las
organizadoras del Theo Murphy meeting (Manchester, 7-8 sept 2026).
**Regla editorial:** CERO cosmología especulativa. Ni ℛ(t) como
"render", ni energía oscura, ni Postulados. Solo poset, conteos,
leyes, errores. El marco Render se menciona una sola vez en
Acknowledgments como motivación, si el autor quiere.

---

## Abstract (borrador de contenido, no de prosa)

Medimos y derivamos las leyes de crecimiento del conteo de links en
sprinklings de Poisson con cutoff IR: (i) en 2D la valencia pasada
crece como 2·ln(T√ρ) (medido por-elemento: pendiente 2.01±0.12);
(ii) en 4D, v = π√6·√ρ·T² (exponente 2.089±0.025, amplitud al 5%,
sin parámetros ajustados); (iii) en FRW de materia, la asíntota
conserva la ley de área con amplitud (π√6/15)·𝔉 donde el factor
𝔉 = 0.4991 se deriva del promedio de a⁴ sobre el intervalo con el
peso de volumen del diamante (medido: 0.4990 — acuerdo a 4 cifras),
con transitorio 1/η explícito; (iv) la fracción de links
ε = N_links/N_past sigue 3√6/(√ρR²) y separa sprinklings
manifoldlike (≈0.21) de órdenes aleatorios (≈0.017). El pipeline se
ancla al objeto estándar de la literatura reproduciendo ⟨N₀⟩ de
Glaser-Surya en diamantes a 0.07σ. Cerramos con la identidad de
partición cadena/anticadena para métricas débilmente disformes y su
test futuro (inserción sesgada).

## Estructura

1. **Introduction** — links como covering relations; valencia
   infinita sin cutoff (Surya 2019); qué falta en la literatura: las
   leyes con cutoff IR y el caso cosmológico. Baseline: Glaser-Surya
   2013.
2. **Methods** — sprinkling, definición exacta de link (bloqueadores),
   candidatos por banda (P(link)=e^{-ρV}, corte τ²<6.8 con sesgo
   <e⁻⁶), seeds deterministas, pre-registro y reproducciones
   (política del repo). [Fuentes: 12/13/18b docstrings]
3. **Anchor** — reproducción de ⟨N₀⟩ (Glaser-Surya) en diamante 4D a
   0.07σ; costo de borde slab-vs-diamante (+21%) medido. [exp 23]
4. **Results I: Minkowski** — 2D ley log por elemento (lema
   local-vs-global: valencia insensible a N, ×8 testado) [18a];
   4D ley de área con amplitud π√6 [18b].
5. **Results II: FRW** — transitorio (fit η²(1−B/η), ΔAIC=+40.7
   vs potencia libre), asíntota de área, amplitud derivada:
   𝔉 = 30∫x(1−x)⁸/√⟨a⁴⟩dx = 0.4991 vs 0.4990 medido. [18c/18d +
   RESULTS_18d]. Nota honesta: el fit de rango corto da 2.70±0.07 —
   el transitorio contamina; documentado como advertencia
   metodológica para trabajos futuros.
6. **Results III: fracción de links** — ε = 3√6/(√ρR²) (≈10% borde);
   discriminador manifoldlike 0.21 vs 0.017 [exp 24 + exp 22 Codex].
7. **Three-sector accounting** — el teorema de consistencia:
   para métrica débilmente disforme, cadenas ×𝓡⁻¹ × anticadenas
   ×𝓡⁺³ = √−g = 𝓡⁺²; el caso conforme exige 𝓡⁻⁴ (signo opuesto,
   contable). Enunciado como resultado matemático de posets, SIN
   física del render. [nota anisotropía §1]
8. **Outlook** — Exp 25 (inserción sesgada: ¿existen los exponentes
   −1/+3?), estimador Boguñá-Krioukov para anticadenas, ε_link en
   FRW (24b). Una línea calibrada: ε(T) ~ T⁻² pertenece a la familia
   de escalas H² conocida (CKN/everpresent) — sin claims.

## Claims table (versión corregida — reemplaza la del diff del paper)

| Claim | Estado | Evidencia |
|---|---|---|
| v_2D = 2ln(T√ρ), por elemento, insensible a N | MEDIDO | 18a (pendiente 2.01±0.12; N×8) |
| v_4D = π√6√ρT² | MEDIDO+DERIVADO | 18b (p=2.089±0.025, amp 5%) |
| FRW: área asintótica, amplitud 𝔉=0.4991 | MEDIDO+DERIVADO | 18c/d (0.4990, 4 cifras) |
| Anclaje ⟨N₀⟩ Glaser-Surya | REPRODUCIDO | 23 (0.07σ) |
| ε = 3√6/(√ρR²) | MEDIDO+DERIVADO | 24 (repro bit-exacta) + esta nota |
| ε separa manifoldlike/aleatorio | MEDIDO | 22 (0.21 vs 0.017) |
| Partición 𝓡⁻¹×𝓡⁺³=𝓡⁺² | TEOREMA (consistencia) | nota anisotropía |
| Exponentes −1/+3 desde dinámica sesgada | ABIERTO | Exp 25 |

## Figuras (a producir)

F1: v vs T, 2D (log) y 4D (T²) con teoría superpuesta. F2: FRW ratios
convergiendo + fit transitorio. F3: ε vs √ρR² colapsando a una curva
+ separación manifoldlike/aleatorio. F4: esquema de tres sectores
(cadena/anticadena/link — la figura que después se vuelve video).

## Referencias (todas verificadas contra arXiv en este repo)

Bombelli+87 · Rideout-Sorkin 2000 · Sorkin 2003 · Johnston 2008
(0806.3083) · Rideout-Wallden 2009 (0810.1768) · Benincasa-Dowker
2010 (1001.2725) · Glaser-Surya 2013 (1309.3403) · Surya 2019 (LRR)
· Brightwell-Łuczak (1510.05612) · Bollobás-Brightwell 1991/92 ·
Glaser 2023 (2306.09904) · Boguñá-Krioukov 2024 (2401.17376) ·
Johnston 2022/2025 (2111.09331, 2502.09701).

## Qué falta para el draft completo

1. Prosa (yo, próxima sesión — ~8-10 páginas).
2. Figuras F1-F3 (Codex puede generarlas de los outputs existentes;
   F4 esquema a mano).
3. Decisión del autor: autoría y afiliación (¿Bustos solo? ¿"with
   computational assistance de..."? — política de LLMs de Zenodo es
   laxa, pero la transparencia del repo ya lo documenta).
4. Verificar emails/deadline Manchester (Grok, pendiente).
