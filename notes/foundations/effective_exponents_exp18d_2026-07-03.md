# Effective Exponents and Finite-Size Scaling (Prep for Exp 18 → 18d Narration)

**Date:** 2026-07-03  
**Sources (verified):**  
- Glaser, O’Connor, Surya, "Finite Size Scaling in 2d Causal Set Quantum Gravity", arXiv:1706.06432 (2018)  
- General statistical mechanics / critical phenomena literature on finite-size scaling, corrections-to-scaling, crossover (standard forms as in textbooks and reviews).  
- No new searches on cosmologies or experiments.

**Purpose:** Provide reusable formal language and analogies for describing how a measured growth law (e.g. valency ~ η^p) over finite range may differ from its asymptotic form. Strictly analogical / mathematical.

## 5 Technical Bullets

- In finite-size scaling, when an observable follows a power law O(L) ~ L^{-x} only asymptotically, over a finite range of system size L the local (effective) exponent extracted from a log-log fit or derivative is p_eff(L) = - d ln O / d ln L = x + correction term.
- A common form for the correction is O(L) = A L^{-x} (1 + B L^{-ω} + higher), leading to p_eff(L) ≈ x - (ω B L^{-ω}) / (1 + B L^{-ω}) ≈ x - ω B L^{-ω} for small correction. This is equivalent to p_eff = p + d ln f / d ln L where f(L) is the multiplicative correction factor.
- Corrections-to-scaling exponent ω > 0 controls how fast the effective exponent approaches the true asymptotic p as L increases. Typical values depend on the universality class (often ω ≈ 1 or smaller).
- Crossover scaling occurs when two regimes compete (e.g. finite-size vs infinite-volume, or different fixed points). The effective exponent drifts between two values over a window of L controlled by a crossover scale.
- In the Glaser et al. (arXiv:1706.06432) 2d causal set quantum gravity model, they introduce a rescaled inverse temperature β̄ = β N and show that ln Z scales as -β̄ F̄ N^ν±, with ν+ = 1 in the continuum-like phase and ν- = 0 in the non-continuum phase. They also find the critical βc scales as ~ 1/ε² in the large-N limit and that the asymptotic regime is reached already for N ≳ 65. This provides a concrete CST example where scaling exponents (here for the action/partition function) are extracted after rescaling with system size N and differ between phases.

## 3 Divulgable Phrases

- "Over a limited window of sizes, a power law can look steeper or shallower than its true long-distance form — the effective exponent is just a local slope on the log-log plot."
- "Corrections-to-scaling act like a slow drift term: the measured power slowly approaches the ideal one as the system gets bigger, following something like 1 + B / L^ω."
- "In some models, rescaling the control parameter by the system size (like β N) makes the effective behavior collapse onto a universal curve, revealing whether you are still in a transient or have reached the true scaling."

## 3 Risks of Misinterpretation

- Fitting an effective exponent over too small a range and claiming it is the new asymptotic law (the drift term B/L^ω can mimic a different power for limited data).
- Ignoring that the crossover or correction scale depends on microscopic parameters (e.g. non-locality cutoff ε); what looks like a new exponent may just be slow approach controlled by that scale.
- Treating the effective exponent as a fundamental property rather than a diagnostic of how far the simulation or sprinkling is from the asymptotic limit; this can lead to premature conclusions about phase or universality.

**No new claims.** This note only collects standard mathematical forms and one concrete CST reference as possible narrative tools for describing finite-range measurements versus asymptotic behavior. All usage must remain strictly analogical and subject to later audit.

## Appendix: Language guardrails

**Bad wording:** “18d demuestra que la teoría estaba bien desde el principio.”  
**Safer wording:** “Dentro del protocolo de 18d, el exponente medido en el rango finito de 18 se comporta como un transitorio que se acerca al valor esperado para escalas mayores.”  
**Why:** Atribuye una confirmación global a un experimento diseñado para discriminar transitorio vs asintótico dentro de un rango específico.

**Bad wording:** “Medimos un nuevo exponente 2.7 que reemplaza al 2.”  
**Safer wording:** “En el intervalo de η explorado, el exponente efectivo extraído es consistente con una corrección de tamaño finito sobre una ley subyacente de exponente 2 (o un crossover aún no resuelto).”  
**Why:** Confunde el exponente efectivo (dependiente del rango finito) con un nuevo exponente asintótico.

**Bad wording:** “Esto prueba que el modelo de valencia es correcto a todas las escalas.”  
**Safer wording:** “Los datos de 18 y el diseño de 18d ilustran cómo un ajuste de potencia sobre un rango limitado puede producir un p_eff distinto del límite de η → ∞.”  
**Why:** Sobrevende la validez universal a partir de un análisis de scaling finito.

**Bad wording:** “La teoría predijo 2 pero la naturaleza dio 2.7, así que ajustamos la predicción.”  
**Safer wording:** “El protocolo pre-registrado distinguía entre un exponente asintótico distinto de 2 y un transitorio con correcciones 1/L^ω; 18d está diseñado para separar esas dos lecturas.”  
**Why:** Presenta el resultado como un ajuste posterior en lugar de una prueba pre-especificada de transitorio vs asintótico.

**Bad wording:** “Con más datos el exponente se estabilizará en el valor correcto.”  
**Safer wording:** “En el lenguaje de finite-size scaling, para discriminar entre p = 2 con correcciones lentas y un p asintótico distinto se requiere explorar η significativamente mayor o incluir términos de correction-to-scaling explícitos en el modelo de ajuste.”  
**Why:** Da por sentado el resultado sin reconocer que el experimento actual puede no alcanzar aún el régimen que resuelve la ambigüedad.
