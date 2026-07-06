# The Rendering Universe

**Causal-set phenomenology with pre-registered experiments, published
negatives, and a resolution-native arithmetic.**

**Author:** Patricio Fernando Bustos Cabrera · Maya Educación, Ecuador
**License:** MIT (code) · CC-BY 4.0 (papers)
🇪🇸 [Versión en español](README.es.md) · 🌐 [Interactive demo](https://editorenbici.github.io/rendering-universe/)

---

## What this is

A research programme built on one austere hypothesis: the universe is a
causal set whose **resolution** ℛ grows — and the physics is what the
counting conserves. Chains (sequences of cause→effect) are clocks;
antichains are space; links (covering relations) are the irreducible
causal bonds. We measure what these counts do, we pre-register every
measurement before running it, and we publish the results **whatever
they turn out to be** — including our refutations and our own bugs.

> *The universe is a count completing itself; physics is what the count
> conserves.*

## The honest scoreboard

This project grades its own claims. Current state (single source of
truth: [FUNDAMENTOS.md](FUNDAMENTOS.md)):

| Result | Status |
|---|---|
| Link counting reproduces the Newtonian kernel (1/r potential, Johnston normalization to 1–3%) | **MEASURED** |
| 2D valency law: v = 2·ln(T√ρ) — slope measured 2.01 ± 0.12, insensitive to N | **MEASURED + DERIVED** |
| 4D area law: v = π√6·√ρ·T² — amplitude parameter-free, matched at 5% | **MEASURED + DERIVED** |
| FRW blocking factor 𝔉 = 0.4991 derived vs 0.4990 measured (4 figures) | **MEASURED + DERIVED** |
| Glaser–Surya ⟨N₀⟩ baseline reproduced to 0.07σ | **REPRODUCED** |
| Link fraction ε = 3√6/(√ρR²); separates manifoldlike (0.21) from random orders (0.017) | **MEASURED + DERIVED** |
| Chain/antichain partition identity (−1,+3) → +2 for weakly disformal metrics | **THEOREM — first quantitative test running (Exp 25b)** |
| ℕ_R graded arithmetic (dyadic exact, min-law, grade-relative ∞, ⊤_R) | **IMPLEMENTED** — [`packages/rendernum`](packages/rendernum), 14/14 tests |
| Variable-ℛ ISW sector | **REFUTED** (Exp 17b: ΔT = +0.37 ± 0.93 µK over 1454 voids; our prediction excluded at 20.7σ). Kept public, told in full — including the coordinate-frame bug we found and fixed along the way |
| ℛ ∝ t^β from BAO | **TIE** with ΛCDM (β = 0.055 +0.045/−0.050) — a tie is cited, not celebrated |
| ε(t₀) ~ 10⁻¹²¹ ~ Λℓ_P² | **Reformulation** within the known T⁻² family (Cohen–Kaplan–Nelson); not a discovery. Its exam: does it survive expansion? (Exp 24b, pending) |

Nine ideas live in the **graveyard** (FUNDAMENTOS §III) — refuted or
retired, irreversibly. We show our dead.

## Method (the part reviewers keep telling us is the real asset)

Every rule in [PROTOCOLO.md](PROTOCOLO.md) exists because violating it
already cost us something concrete:

- **Pre-registration committed before running** — git history certifies
  the ordering; success/failure criteria frozen in advance.
- **Deterministic seeds; bit-exact reproduction** of headline numbers
  from clean checkouts.
- **Locks are verified by executing them**, never by reading strings
  (we learned this the hard way).
- **Ensembles, not best seeds.** **Verified citations only.**
  **Chat-sourced data quarantined** until checked against official
  releases.
- **Results published as they come out** — a rescue requires a new
  pre-registered prediction, not a reinterpretation.

The recurring failure mode we found (and named): the **raster
instrument fallacy** — measuring structure with the instrument's
coordinates instead of the object's structure. It produced our Exp 17
bug, the field's spatial-distance problem, the π=4 staircase paradox,
and a design flaw we caught pre-run in Exp 25b. See
[notes/foundations/patron_instrumento_raster_2026-07-06.md](notes/foundations/patron_instrumento_raster_2026-07-06.md).

## Papers

1. **Counting laws of links in Poisson-sprinkled causal sets** —
   technical, zero cosmology. Draft:
   [notes/foundations/paper1_tex/paper1.pdf](notes/foundations/paper1_tex/paper1.pdf)
   (Zenodo release pending the Exp 25b verdict).
2. **The falsifier that fired twice** — the 17 → bug → 17b arc as a
   methodological contribution. In preparation, simultaneous release.
3. **ℕ_R: arithmetic at finite resolution** — the number system;
   artifact: [`rendernum`](packages/rendernum).

## Try it

```bash
git clone https://github.com/Editorenbici/rendering-universe.git
cd rendering-universe/packages/rendernum
pip install -e . && python -m pytest tests/   # 14 passed
```

```python
>>> from rendernum import from_float
>>> from_float(0.1)          # every IEEE float is a grade-52 dyadic citizen
```

Reproduce the headline laws: scripts in [`code/analysis/`](code/analysis/)
carry their pre-registration references and declared seeds in their
docstrings; per-experiment verdicts live in `code/analysis/RESULTS_*.md`.
An interactive demo page (grade-52 citizens, the min-law, IEEE 1788 vs
ℕ_R, the π=4 staircase, the (−1,+3) budget) is at
[notes/creative/web/nr_demo.html](notes/creative/web/nr_demo.html) —
self-contained HTML, open it in any browser.

## Repository map

```
FUNDAMENTOS.md        single source of truth: validated core, symbols,
                      graveyard, open tree, papers plan
PROTOCOLO.md          operating rules (each one traceable to a scar)
notes/
  experiments_manifest.md   every experiment with its status
  foundations/        pre-registrations, results notes, paper drafts
  literature/         verified references
  creative/           outreach: scripts, storyboards, web demo
code/analysis/        experiment runners + RESULTS_*.md verdicts
outputs/              committed evidence (JSON/stdout) behind every claim
packages/rendernum/   the ℕ_R arithmetic, pip-installable
media/manim/          rendered animations (π=4 staircase, Exp 25
                      crossover, sunflower vector/raster)
paper/                the original framework paper (author-maintained)
wiki/                 project wiki pages
```

## A note on how this was built

This project is developed by a single author working with AI systems
(Anthropic Claude, OpenAI Codex, xAI Grok, and local models) under the
protocol above: cross-audits, pre-registered gates, verified citations.
Every number in every claim traces to committed evidence with declared
seeds — check us.

---

*Contact: the repository issues, or the author.*
