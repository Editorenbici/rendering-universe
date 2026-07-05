# Variables Literature Review: v_R, ε_link, G_eff — Homologation and Validation

**Date:** 2026-07-03  
**Author:** Grok (full task execution per instructions)  
**Scope:** Strict literature search, comparison, homologation. No edits to paper/ or README/. All claims backed by searches (web/arXiv). Deliverable only in notes/.  
**Draft reference:** notes/variables_R_and_epsilon_link_draft.md not located (targeted grep/ripgrep + PS recursive *.md searches in rendering-universe and broad C:\Users\pc1 scan returned none in project context; only unrelated .codex\.tmp plugin skill drafts). Comparison uses inferred definitions from project code (18a_lema_valencia.py, 18b_control_4d.py, 13_sprinkling_4d_kernel.py) and notes (link_abundance_poisson_sprinkling.md, links_as_transitive_reduction_2026-07-03.md, RESULTS_12_13.md, RESULTS_18*.md).  

**Core variable definitions (inferred from codebase + notes):**  
- ℛ(t): resolution scale (e.g., R0 ~ 10^30 today; N ~ ℛ^4; redshift via Postulate 3: R(z)/R0 = 1/(1+z)).  
- v_R := dℛ/dt (rate of resolution change; related to β = d ln ℛ / d ln t via v_R = β ℛ / t).  
- ε_link := ⟨N_links⟩ / ⟨N_total⟩ (link fraction / efficiency; N_links = covering relations count = N_0 in CST notation; N_total = number of elements N; equivalently ~ ⟨valency⟩ / N or p linking fraction in literature usage).  
- G_eff := G * ε_link * f(ψ) (ψ = link-counted potential from transitive reduction/Hasse; factorizes effective coupling).  
- Valency v(e): number of past links (covering relations) to element e (exact count via blocker check on causal candidates near light-cone). In 4D Minkowski cutoff: v(T) ≈ π√6 √ρ T².  

---

## 1) BUSCAR

**"velocidad de refinamiento de resolución" or "rate of change of discreteness scale" (CST, CDT, emergent gravity, lattice theories):**  
- NO ENCONTRADO verbatim for v_R = dℛ/dt or equivalent "resolution refinement velocity" / "discreteness scale rate".  
- Related concepts: discreteness scale ℓ = ρ^{-1/d} is fixed per sprinkling (Poisson density ρ) in CST (Surya 2019; Glaser & Surya 2013). Sequential growth models (Rideout-Sorkin) add elements stochastically; no continuous dℓ/dt or dℛ/dt defined.  
- In CDT (Ambjørn et al.): lattice spacing a is a parameter; simulations study fixed-a ensembles or a→0 continuum limit; no "refinement rate" of a(t) as dynamical variable in core papers. Running couplings appear in asymptotic safety / RG flows (e.g., beta functions for G(k)), but not resolution rate per se.  
- Sources checked: arXiv searches for "rate of change of discreteness", "resolution refinement", dR/dt + causal set / CDT yielded no matches; mentions of "discreteness scale" are static.  

**"eficiencia de linking" or "link fraction" in causal sets, posets, or DAGs:**  
- ENCONTRADO (partial match): "linking fraction" p explicitly defined.  
  - Carlip (2024), arXiv:2405.14059: "An n-point causal set must have fewer than N_max = n²/2 links, and can be characterized by a linking fraction 0 ≤ p ≤ 1, where N_0 = p N_max." Discusses two-layer and path-integral suppression.  
  - Related: Mathur et al. (2020), arXiv:2009.07623 uses linking fraction p̃ in entropy/link action for KR orders vs sprinklings (p̃ ~ 1/2 typical for KR).  
  - Glaser & Surya (2013), arXiv:1309.3403 and Surya (2019) Living Rev. Relativ. 22, 5: use N_0 (link abundance) and valency (infinite in continuum-like sprinklings d>1+1); "the nearest neighbours of an element are the links or irreducible relations." Probability a pair is a link = e^{-ρ V([x,y])}. No "fraction" normalized by N_total as primary observable, but N_0 enters BD action directly.  
- "link density" appears in theses (e.g., Schmitzer 2010: "future link density of x").  

**Constantes adimensionales del tipo π√6 o similares en abundancias de sprinklings:**  
- NO ENCONTRADO for link/valency abundance. π√6 (or 1/(π√6)) appears in CST for d'Alembertian kernel / Benincasa-Dowker action normalization (Roy et al. 2013; Surya review), not for ⟨N_links⟩ or interval m=0 abundance.  
- Glaser & Surya 2013: analytic ⟨N_m^d⟩ involve Gamma(d+1), χ factors from Minkowski volumes; scale-invariant ratios in large N. No π√6.  
- Project-specific: π√6 arises from 4D link-band volume integral (exp(-ρ π τ^4 /24) Gaussian-like over hyperboloid shell) in cutoff sprinklings (see 18b docstring + audit in link_abundance_poisson_sprinkling.md). Matches exact integral for N_0 in diamond (27.6k theory vs 27.5k measured).  

---

## 2) INVESTIGAR (0-3 sources per variable; alternate names)

**v_R = dℛ/dt**  
- NO ENCONTRADO as named quantity.  
- Analog names in literature: "running of discreteness scale" (static ℓ only); "scale factor evolution" da/dt in CDT (but a fixed); "beta function for cutoff" in RG-improved gravity. No direct "resolution velocity".  
- Sources: 0 primary. (Henson 2006 arXiv:gr-qc/0601121 mentions discreteness scale setting but static.)  

**ε_link = ⟨N_links⟩/⟨N_total⟩**  
- Partial: "linking fraction" p (N_0 / [n(n-1)/2]) — Carlip 2024 arXiv:2405.14059 (1 source).  
- "valency" (links per element) — Glaser & Surya 2013 arXiv:1309.3403; Surya 2019 (infinite in continuum sprinklings).  
- "covering relation density" / "link density" — mentioned in order-theory translations and Schmitzer 2010 thesis (not normalized exactly as /N).  
- Alternate names found: valency per element, branching ratio (rare), covering density (poset lit.), link degree distribution (recent graph observables, e.g. arXiv:2605.27514). No exact "link fraction = ⟨N_links⟩/⟨N_total⟩" for Poisson sprinklings as primary var.  
- 3 sources max: Carlip (linking fraction p), Glaser/Surya (N_0/valency), Surya review.  

**G_eff = G * ε_link * f(ψ)**  
- NO ENCONTRADO exact factorization with ε_link (link fraction).  
- Similar: effective Newton's constant modulated by scalar/disformal factors.  
  - Sakstein arXiv:1409.1734: G_eff variations via conformal/disformal A(φ), B; ΔG/G terms.  
  - Zumalacárregui et al. arXiv:1004.2684 and Koivisto 2012: screening, G_eff(φ,X) in disformal matter coupling.  
  - General: G_eff = G * f(A(φ),B,X) common in scalar-tensor (no link-count or ε_link).  
- 2 sources: Sakstein 2014; Zumalacárregui 2010.  

---

## 3) COMPARAR

**v_R vs Codex draft (inferred):**  
Draft (via code/notes) defines resolution growth via β = d ln ℛ / d ln t (e.g., β≈1/3 matter, ~0 today from DESI). v_R = dℛ/dt not explicitly symbolized but implied (R(t) evolution in 01_vacuum..., 02_desi...). No dimensional error found: ℛ dimensionless or length^{-1} scale (consistent with N~ℛ^4, cutoff k_max ~ M_Pl ℛ). Equivalence: v_R = (β / t) ℛ. Codex notation (β-centric) matches continuum FRW limit of project.

**ε_link vs Codex draft (inferred):**  
Codex/Code uses link counting (N_0 / valency) for ψ in 12-13 (Johnston kernel reproduces Newton with links; raw count fails). ε_link = ⟨N_links⟩/⟨N_total⟩ appears as proposed modulator (fractional "efficiency"). In 4D control (18b): for cutoff diamond-like T=10, ρ=1, ⟨v⟩≈770, N≈72k → ε_link ~ ⟨v⟩/N ≈0.0106 (if /N) or p≈0.021 (if / (N^2/2)). Codex draft likely treats ε_link as small dimensionless <1 factor (consistent).  
Dimensional: ε_link dimensionless (good). No error. Notation Codex: ε_link; equiv to p in Carlip or N_0/N in some usages.

**G_eff vs draft:**  
Draft introduces factorization for effective coupling (links provide "local" G modulated by ψ). Matches project use of link-counted ψ for Newton in 12-13. No draft errors found.

---

## 4) DAR VUELTA (invert relations if similar found)

**For ε_link:**  
Literature: p = N_0 / (n²/2) ; N_0 = total links.  
Project measures ⟨v⟩ = 2 N_0 / n (directed avg), so ε_link_project ≈ ⟨v⟩ / n = 2p (if p definition). Or if project ε_link := ⟨N_links⟩/⟨N_total⟩ with N_links=N_0, N_total=n then ε_link = N_0/n = p n /2 .  
Explicit transform: p_lit = (⟨v⟩ / 2) * (⟨ε_link⟩)   [assuming ε_link = ⟨v⟩/n ].  
For Poisson sprinkling (cutoff): recover project v from lit p via v = 2 p n (finite-N). In infinite-N continuum limit p→0 (valency diverges slower than n).  

**For v_R:**  
No direct analog. If discreteness ℓ(t) = 1/ℛ(t), then dℓ/dt = - (1/ℛ²) v_R . Recovery: project v_R →0 when ℓ fixed (standard CST sprinkling).  

**G_eff:**  
Lit: G_eff = G * f(φ, X) (disformal A,B factors).  
Invert: project ε_link = G_eff / (G f(ψ)) . If lit f(ψ) known, ε_link extracted as residual. NO exact match.

---

## 5) RESOLVER (conflict on ε_link def for Poisson Minkowski sprinklings)

No direct conflict in sources. Carlip p is combinatorial (global fraction of possible pairs). CST standard uses local N_0 or per-element valency (Glaser/Surya).  

Most appropriate for Poisson sprinklings in Minkowski: local valency / link abundance N_0 per element or total, normalized carefully with volume (or cutoff T). Global p = N_0 / (n²/2) →0 trivially for large n; valency (or band-integrated prob e^{-ρV}) better captures the "thin shell" non-locality and continuum limit. Justification: Poisson + Lorentz invariance makes relevant contributions from infinite-volume hyperboloid near light-cone (Surya 2019); p global washes out the geometry that produces the characteristic abundances. Use N_0(ρ,T,d) or v(T) for direct comparison to sprinklings (as validated vs Glaser/Surya integrals).

---

## 6) HOMOLOGAR (unify notation)

**Current mismatch:** Codex draft (inferred) uses ε_link, v_R; code uses valency/v, N_0, β (d ln R/d ln t), no ε_link symbol yet. Lit uses: N_0 (links count), valency, linking fraction p.  

**Canonical proposal:**  
- In paper (formal): use η_link (or p_link) for the dimensionless linking fraction ε_link = ⟨N_0⟩ / ⟨N_max⟩ or ⟨v⟩/⟨N⟩ normalized appropriately; v_R → \dot{\mathcal{R}} or \beta_{\mathcal{R}} (rate of resolution). Cite Carlip for p.  
- In code: keep ε_link, v_R (or v_R = dR_dt) for scripts; document mapping η_link = ε_link (paper = code var when normalized same).  
- For G_eff: keep G_eff = G ⋅ η_link ⋅ f(ψ) in both (unify on η_link).  
- Example: Codex wrote ε_link → literature p or η; propose use η_link in paper, ε_link (or link_frac) in code. Unify on \eta_{\rm link} = \langle N_{\rm links} \rangle / \langle N_{\rm tot} \rangle (with explicit normalization footnote).  

---

## 7) FACTORIZAR

**G_eff = G * ε_link * f(ψ) in disformal theories:**  
NO ENCONTRADO.  

Literature factorizations (exact examples):  
- Sakstein arXiv:1409.1734: effective G modified by conformal/disformal; e.g. ΔG/G ≡ 2Q² (coupling strength); G_eff appears via A(φ), B(φ,X) in geodesic deviation or Newtonian limit. No ε_link.  
- Zumalacárregui et al. / Koivisto: G_eff(φ) or direction-dependent from disformal D term; screening factors like (1 + deriv terms in X).  
- General disformal: T_m transformed by A^6 √(1-2B²X/Λ²) factors (from earlier energy search). No product with link fraction.  

No exact G * (link fraction) * f(ψ).

---

## 8) SIMULAR (literatura)

**Reported numerical values of "link fraction" / "covering relation density" in sprinklings:**  
- Carlip 2024 / related: for two-layer (not pure Poisson sprinkling) p varies 0 to 1/2; large-n treated continuously. For sprinkled manifold-like: not primary; valency infinite → effective p depends on cutoff.  
- Glaser & Surya 2013 (arXiv:1309.3403): figures/simulations for ⟨N_m^d⟩ (incl. m=0 = N_0 links) in Minkowski diamonds. Example validation (project audit): T_D=10, ρ=1, 4D diamond → ⟨N_0⟩ = 27,602 ±95 (integral) vs measured 27,537 ±876 (exact link count, 0.07σ). N not stated but vol ~ O(T^4) → p ~ O(1/T^2) small.  
- Surya 2019: qualitative "high degree of connectivity" + infinite valency; no exact p number for Poisson.  
- Project comparison (12-13 + 18b control): in 4D Minkowski cutoff T~10-16 ρ=1, ε_link inferred ~0.01 (v/N) or linking p~0.02; for smaller balls in 13 (cyl vol~O(10^4)), similar order. In FRW transient (18c/18d): exponent changes but ε_link still small, area-like scaling. Matches lit order-of-magnitude (small p for large-N cutoff sprinklings; valency >>1 but <<N).  

No exact "0.XX" for pure infinite Poisson; cutoff-dependent.

---

## 9) RECUPERAR (analogous but not equal; recovery conditions)

- Valency (lit) → project v: recover exactly in cutoff limit (finite T or diamond); v_lit(infinite) recovered as v_project → ∞ when T→∞ at fixed ρ (or ρ→∞). Condition: β→0 (no FRW transient) + uniform sprinkling → matches Glaser/Surya baseline.  
- Linking fraction p_lit → ε_link: p = (⟨v⟩ / n) roughly; recover project ε_link when n fixed and cutoff explicit. In limit β→0 (static resolution, constant ℛ) + Minkowski → v_R→0, ε_link → constant (cutoff dependent).  
- For G_eff factorization: recover standard disformal G_eff when ε_link → const (or 1); f(ψ)→ lit f(φ). Condition: link fraction fixed (no resolution evolution).  
- General: "in the limit T→∞ or ρ fixed large, project quantities approach continuum with infinite valency (non-local CST feature)."

---

## 10) REPLANTEAR (alternative names if no precedent)

Since v_R, ε_link, G_eff factorization largely novel in this combination:  

**v_R (dℛ/dt):**  
1. "tasa de refinamiento cósmico" — Advantage: intuitive, ties to ℛ(t) cosmic evolution; Disadv: vague (sounds like expansion rate).  
2. "velocidad de discretización variable" or "resolution flow rate" — Adv: emphasizes discreteness; Disadv: technical.  
3. "β-resolution derivative" or "escala de refinamiento temporal" — Adv: links to β; Disadv: not self-contained.  

**ε_link:**  
1. "densidad de vecinos causales directos" (covering neighbors fraction) — Adv: descriptive, matches "links = covering relations"; Disadv: long.  
2. "fracción de linking" or "eficiencia de cubrimiento" — Adv: matches lit "linking fraction"; Disadv: may confuse with p global.  
3. "abundancia relativa de links" / "link density" — Adv: aligns N_0 terminology; Disadv: "density" overloaded in CST (vs volume).  

Recommend: paper uses "fracción de enlaces η_link" (or linking fraction citing Carlip); code ε_link.

---

## 11) UNIR / SEPARAR

**Decision: SEPARAR v_R and ε_link (in distinct equations/sections), with optional coupling term.**  

Justification (2 lines): v_R governs global evolution of discreteness scale ℛ(t) (FRW transient, beta law, vacuum cutoff); ε_link is a local geometric observable of a given sprinkling (valency/N at fixed ρ,T). They are coupled indirectly (v_R changes effective cutoff → changes ε_link via T( t ) or ρ(t)), but not identical; unifying in one eq would obscure the separation between refinement dynamics and poset structure (links = Hasse / transitive reduction). G_eff can include both if needed: G_eff(t) = G ⋅ ε_link(ℛ(t)) ⋅ f(ψ).

---

## 12) IMAGINAR (analogies, pure math + concrete physical; no games)

**v_R = dℛ/dt:**  
- Analogía matemática pura: "la derivada temporal de la frecuencia de muestreo en una partición adaptativa de un espacio métrico; cuántos nuevos 'puntos de corte' se insertan por unidad de parámetro de evolución." (Como refinamiento de malla en PDE solvers adaptativos, donde Δx(t) decrece a tasa v_refine.)  
- Analogía física concreta: "la tasa a la que un detector de partículas de energía variable aumenta su granularidad con el envejecimiento del universo; cada 'tick' cósmico revela sub-estructura causal previamente irresoluble, como un osciloscopio cuya resolución de tiempo mejora linealmente mientras el universo expande."  

**ε_link = ⟨N_links⟩/⟨N_total⟩:**  
- Analogía matemática pura: "la densidad de aristas en la reducción transitiva (Hasse diagram) de un poset aleatorio Poisson-embedido; fracción de pares ordenados que son irreducibles (no transitivamente derivables)." (Equiv: 1 - densidad de caminos de longitud >1 en el DAG causal.)  
- Analogía física concreta: "la fracción de colisiones 'directas' (sin intermediarios) en una lluvia de partículas Lorentz-invariante dentro de un cono de luz; solo los pares sin 'screening' por puntos intermedios cuentan como vecinos causales inmediatos, análogo a caminos libres de scattering en un medio óptico turbio pero con umbral de visibilidad exacto."  

**G_eff = G * ε_link * f(ψ):**  
- Analogía matemática pura: "el acoplamiento efectivo en un grafo ponderado donde solo las aristas de la reducción transitiva contribuyen al kernel, escalado por una función del potencial acumulado en el vecindario causal inmediato."  
- Analogía física concreta: "la constante de gravitación newtoniana modulada por la fracción de 'interacciones directas' (links) versus todas las interacciones causales posibles, atenuada o amplificada por el potencial ψ generado por la distribución de vecinos inmediatos; como G visible en un fluido donde solo contactos de primera capa transmiten fuerza, filtrado por la 'viscosidad causal' ψ."  

---

## Resumen de hallazgos / claims de prioridad

- v_R: sin precedente directo → potencialmente nuevo (condicionado a no existir en growth models no buscados exhaustivamente).  
- ε_link ~ linking fraction: precedente parcial (Carlip 2024 p); project ε_link con uso en G_eff + sprinklings FRW cutoff es distintivo. Citar Carlip + Glaser/Surya.  
- Factorización G_eff con ε_link: sin precedente → nuevo.  
- π√6: nuevo para abundancia de links (literatura lo reserva para kernels de acción); derivación de banda de links + validación numérica vs Glaser/Surya es aporte.  
- Recomendación: en paper citar Glaser & Surya 2013 (arXiv:1309.3403), Surya 2019, Carlip 2024 para baselines; reclamar mediciones explícitas con cutoff variable + FRW transitorio + factorización en G_eff como resultados originales.  

**Fuentes primarias verificadas (arXiv IDs):**  
- 1309.3403 (Glaser & Surya)  
- 1903.11544 / Living Rev (Surya)  
- 2405.14059 (Carlip)  
- 1409.1734 (Sakstein disformal)  
- 1004.2684 (Zumalacárregui disformal)  

**Próximos:** Auditar contra curvas exactas de ⟨N_m⟩ de Glaser/Surya antes de claims fuertes. No pre-reg sin esto.  

DONE.