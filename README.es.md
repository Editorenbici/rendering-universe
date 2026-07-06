# El Universo que se Renderiza

**Fenomenología de conjuntos causales con experimentos pre-registrados,
negativos publicados y una aritmética nativa de resolución.**

**Autor:** Patricio Fernando Bustos Cabrera · Maya Educación, Ecuador
**Licencia:** MIT (código) · CC-BY 4.0 (papers)
🇬🇧 [English version](README.md) · 🌐 [Demo interactiva](https://editorenbici.github.io/rendering-universe/)

---

## Qué es esto

Un programa de investigación construido sobre una hipótesis austera: el
universo es un conjunto causal cuya **resolución** ℛ crece — y la
física es lo que el conteo conserva. Las cadenas (secuencias
causa→efecto) son relojes; las anticadenas son espacio; los links
(relaciones de cobertura) son los vínculos causales irreducibles.
Medimos qué hacen esos conteos, pre-registramos cada medición antes de
correrla, y publicamos los resultados **salgan como salgan** —
incluidas nuestras refutaciones y nuestros propios bugs.

> *El universo es un conteo que se completa; la física es lo que el
> conteo conserva.*

## El marcador honesto

Este proyecto califica sus propios claims. Estado actual (fuente única
de verdad: [FUNDAMENTOS.md](FUNDAMENTOS.md)):

| Resultado | Estado |
|---|---|
| El conteo de links reproduce el kernel newtoniano (potencial 1/r, normalización de Johnston al 1–3%) | **MEDIDO** |
| Ley 2D: v = 2·ln(T√ρ) — pendiente 2.01 ± 0.12, insensible a N | **MEDIDO + DERIVADO** |
| Ley de área 4D: v = π√6·√ρ·T² — amplitud sin parámetros, al 5% | **MEDIDO + DERIVADO** |
| Factor FRW 𝔉 = 0.4991 derivado vs 0.4990 medido (4 cifras) | **MEDIDO + DERIVADO** |
| Baseline ⟨N₀⟩ de Glaser–Surya reproducido a 0.07σ | **REPRODUCIDO** |
| Fracción de links ε = 3√6/(√ρR²); separa manifoldlike (0.21) de órdenes aleatorios (0.017) | **MEDIDO + DERIVADO** |
| Identidad de partición cadena/anticadena (−1,+3) → +2 en métrica débilmente disforme | **TEOREMA — primer test cuantitativo corriendo (Exp 25b)** |
| Aritmética graduada ℕ_R (diádicos exactos, ley del mínimo, ∞ relativo al grado, ⊤_R) | **IMPLEMENTADA** — [`packages/rendernum`](packages/rendernum), 14/14 tests |
| Sector ISW de ℛ variable | **REFUTADO** (Exp 17b: ΔT = +0.37 ± 0.93 µK sobre 1454 voids; nuestra predicción excluida a 20.7σ). Público y contado completo — incluido el bug de marcos de coordenadas que encontramos y corregimos en el camino |
| ℛ ∝ t^β desde BAO | **EMPATE** con ΛCDM (β = 0.055 +0.045/−0.050) — un empate se cita, no se celebra |
| ε(t₀) ~ 10⁻¹²¹ ~ Λℓ_P² | **Reformulación** dentro de la familia T⁻² conocida (Cohen–Kaplan–Nelson); no un descubrimiento. Su examen: ¿sobrevive a la expansión? (Exp 24b, pendiente) |

Nueve ideas viven en el **cementerio** (FUNDAMENTOS §III) — refutadas o
retiradas, irreversiblemente. Mostramos nuestros muertos.

## El método (lo que los revisores insisten en que es el activo real)

Cada regla de [PROTOCOLO.md](PROTOCOLO.md) existe porque violarla ya
nos costó algo concreto:

- **Pre-registro commiteado antes de correr** — el historial de git
  certifica el orden; criterios de éxito/fracaso congelados.
- **Seeds deterministas; reproducción bit-exacta** de los números
  principales desde checkouts limpios.
- **Los candados se verifican ejecutándolos**, nunca leyendo strings
  (lo aprendimos por las malas).
- **Ensambles, no mejores corridas.** **Solo citas verificadas.**
  **Datos de chat en cuarentena** hasta chequearse contra releases
  oficiales.
- **Resultados publicados salga como salga** — un rescate exige una
  predicción nueva pre-registrada, no una reinterpretación.

El modo de falla recurrente que encontramos (y nombramos): la **falacia
del instrumento raster** — medir estructura con las coordenadas del
instrumento en vez de con la estructura del objeto. Produjo nuestro bug
del Exp 17, el problema de distancia espacial del campo entero, la
paradoja de la escalera (π=4), y un defecto de diseño que cazamos
pre-run en el Exp 25b. Ver
[notes/foundations/patron_instrumento_raster_2026-07-06.md](notes/foundations/patron_instrumento_raster_2026-07-06.md).

## Los papers

1. **Leyes de conteo de links en sprinklings de Poisson** — técnico,
   cero cosmología. Draft:
   [notes/foundations/paper1_tex/paper1.pdf](notes/foundations/paper1_tex/paper1.pdf)
   (release en Zenodo pendiente del veredicto del Exp 25b).
2. **El falsador que disparó dos veces** — el arco 17 → bug → 17b como
   contribución metodológica. En preparación, salida simultánea.
3. **ℕ_R: aritmética a resolución finita** — el sistema numérico;
   artefacto: [`rendernum`](packages/rendernum).

## Probalo

```bash
git clone https://github.com/Editorenbici/rendering-universe.git
cd rendering-universe/packages/rendernum
pip install -e . && python -m pytest tests/   # 14 passed
```

```python
>>> from rendernum import from_float
>>> from_float(0.1)   # todo float IEEE es un ciudadano diádico de grado 52
```

Para reproducir las leyes principales: los scripts de
[`code/analysis/`](code/analysis/) llevan su pre-registro y seeds
declarados en los docstrings; los veredictos por experimento están en
`code/analysis/RESULTS_*.md`. Hay una página demo interactiva
(ciudadanos de grado 52, la ley del mínimo, IEEE 1788 vs ℕ_R, la
escalera π=4 y el reparto (−1,+3)) en
[notes/creative/web/nr_demo.html](notes/creative/web/nr_demo.html) —
HTML autocontenido, se abre en cualquier navegador.

## Mapa del repositorio

```
FUNDAMENTOS.md        fuente única de verdad: núcleo validado, símbolos,
                      cementerio, árbol abierto, plan de papers
PROTOCOLO.md          reglas de operación (cada una con su cicatriz)
notes/
  experiments_manifest.md   cada experimento con su estado
  foundations/        pre-registros, notas de resultados, drafts
  literature/         referencias verificadas
  creative/           divulgación: guiones, storyboards, demo web
code/analysis/        runners de experimentos + veredictos RESULTS_*.md
outputs/              evidencia commiteada (JSON/stdout) de cada claim
packages/rendernum/   la aritmética ℕ_R, instalable con pip
media/manim/          animaciones renderizadas (escalera π=4, crossover
                      del Exp 25, girasol vector/raster)
paper/                el paper original del marco (mantenido por el autor)
wiki/                 páginas del wiki del proyecto
```

## Nota sobre cómo se construye esto

Este proyecto lo desarrolla un solo autor trabajando con sistemas de IA
(Anthropic Claude, OpenAI Codex, xAI Grok y modelos locales) bajo el
protocolo de arriba: auditorías cruzadas, gates pre-registrados, citas
verificadas. Cada número de cada claim se rastrea a evidencia
commiteada con seeds declarados — verifíquennos.

---

*Contacto: los issues del repositorio, o el autor.*
