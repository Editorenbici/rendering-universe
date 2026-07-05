# Paper 1 — Full prose draft (EN) — Fable, 2026-07-06

**Status: DRAFT for the author.** Every claim is traceable to
FUNDAMENTOS §I and the RESULTS files cited inline in [brackets].
The brackets are for Patricio's audit and must be removed before
Zenodo. Editorial rule enforced: zero speculative cosmology; the
word "render" does not appear.

---

# Counting laws of links in Poisson-sprinkled causal sets: IR-cutoff valency, FRW transients, and three-sector accounting

**Author:** Patricio Fernando Bustos Cabrera
*(affiliation/authorship note pending author's decision)*

## Abstract

In a causal set faithfully embedded in a continuum spacetime, the
valency of an element — its number of links, i.e. covering relations
— is infinite in the absence of a cutoff. We measure and derive the
growth laws of past valency under an explicit IR cutoff for three
geometries. (i) In 1+1 Minkowski the per-element past valency grows
logarithmically, v = 2 ln(T√ρ); the measured slope is 2.01 ± 0.12
and is insensitive to the sprinkling size (tested over an eightfold
range in N), confirming that valency is a local quantity controlled
by chain depth rather than by the global element count. (ii) In 3+1
Minkowski the valency obeys an area law, v = π√6 · √ρ T², with
measured exponent 2.089 ± 0.025 and amplitude agreeing with the
parameter-free prediction κ₄ = π√6 at the 5% level. (iii) In a
matter-dominated FRW interval the area law survives with a derived
blocking amplitude 𝔉 = 30∫₀¹ x(1−x)⁸/√⟨a⁴⟩ dx = 0.4991, against a
measured 0.4990 — four-figure agreement — preceded by an explicit
1/η transient that we fit and subtract. We further show that the
link fraction ε = N_links/N_past follows ε = 3√6/(√ρ R²) and
cleanly separates manifoldlike sprinklings (ε ≈ 0.21 at our
reference scale) from transitively-closed random orders (ε ≈
0.017). The pipeline is anchored to the literature by reproducing
the interval-abundance baseline ⟨N₀⟩ of Glaser & Surya in a 4D
diamond to 0.07σ. We close with a chain/antichain partition
identity for weakly disformal metrics — a counting consistency
statement, not a dynamical result — and the pre-registered
experiment that will test whether its exponents arise from biased
growth dynamics. All results are deterministic-seed reproducible;
code and pre-registrations are public.

## 1. Introduction

A causal set is a locally finite partial order (C, ≺) proposed as
the deep structure of spacetime [Bombelli, Lee, Meyer & Sorkin
1987]. Its kinematics are by now well charted: chains measure
proper time [Brightwell & Gregory; Bollobás & Brightwell 1991/92],
interval abundances measure dimension and curvature [Glaser & Surya
2013], and d'Alembertians and actions can be built from layered
counts [Benincasa & Dowker 2010; Surya 2019 for a review].

Among the order-theoretic primitives, the **link** — a covering
relation, x ≺ y with no z satisfying x ≺ z ≺ y — plays a special
role: links are the irreducible causal bonds from which every
relation is composed by transitivity, and they carry the
scalar-field propagator in Johnston's construction [Johnston 2008;
2022; 2025]. Yet the *counting laws* of links are less charted
than those of chains and intervals, for a structural reason: in a
faithful Poisson sprinkling the expected valency of an element
diverges — the past light cone has infinite volume within a
hyperboloidal shell of any proper-time thickness, so arbitrarily
remote elements can be linked to it [Surya 2019]. The valency is
therefore not a number but a *growth law*, defined only relative
to an IR cutoff.

This paper measures those growth laws. We regulate the divergence
with an explicit causal-interval cutoff of temporal extent T and
ask three questions. How does past valency grow with T in flat
2D and 4D? What happens to the law in an expanding
(matter-dominated FRW) interval? And what fraction of an element's
causal past consists of links rather than longer relations? The
answers turn out to be clean: a logarithm with slope exactly 2 in
2D, an area law with amplitude π√6 in 4D, the same area law in FRW
suppressed by a derived factor 𝔉 ≈ 0.4991 that encodes the
expansion history, and a link fraction ε = 3√6/(√ρ R²) usable as a
cheap manifoldlikeness discriminator.

Two methodological points are as much the subject of this paper as
the laws themselves. First, every measurement was pre-registered:
success/failure criteria were committed to a public repository
before the runs, and the git history certifies the ordering.
Second, all pipelines are deterministic — fixed, declared seeds —
and the headline numbers have been reproduced bit-exactly from a
clean checkout. We anchor the machinery to the literature by
reproducing a published interval-abundance baseline (Section 3)
before trusting it with anything new.

## 2. Methods

**Sprinkling.** We sprinkle N points by a Poisson process of
density ρ into a causal interval (Alexandrov set) of a given
geometry, using the standard uniform-in-volume construction in
conformal coordinates where applicable. Causal relations are
computed exactly from the metric; the causal matrix is closed
transitively. [Methods docstrings: 12/13/18b]

**Links.** x ≺ y is a link iff no sprinkled element lies in the
open interval ⟨x, y⟩. We test this exactly by blocker search, not
by the soft approximation P(link) ≈ e^{−ρV(x,y)}: the soft
estimator biases the count wherever the interval volume
fluctuates, and we document in Section 5 a concrete discrepancy it
produced before being retired. [RESULTS_18d systematic note] For
efficiency, link candidates are pre-filtered by a proper-time band
τ² < 6.8/ρ^{1/2-scaling}; the cut discards true links with
probability < e⁻⁶, measured to be negligible at our precision.

**Cutoff and observables.** The IR cutoff is the interval itself:
for an element near the top of an interval of temporal extent T,
the past valency v(T) counts links to elements within the
interval. In FRW runs, extents are quoted in conformal time η. The
link fraction ε(T) = N_links/N_past normalizes valency by the full
causal past.

**Statistics.** Ensembles, not best cases: every quoted number is
an ensemble mean over independent seeds with the standard error of
the mean; model comparison uses information criteria on the full
ensemble. Seeds are pre-declared functions of the grid indices, so
any run can be reproduced bit-exactly. Pre-registration documents
with frozen criteria precede every measurement in the repository
history. [PROTOCOLO rules 1, 4, 6]

## 3. Anchor: reproducing the Glaser–Surya baseline

Before measuring anything new, the pipeline must reproduce
something old. We chose the mean interval abundance ⟨N₀⟩ — the
expected number of links from the bottom element, in the notation
of Glaser & Surya [2013] — in a 4D causal diamond at matched
density. Our result agrees with the published value to 0.07σ.
[Exp 23]

The same exercise quantifies a systematic that matters for
everything downstream: measuring valency in a slab rather than a
diamond inflates the count by +21% at our reference scale, because
the slab's spatial boundary admits links that the diamond's causal
boundary forbids. All results below are therefore quoted for
causal-interval cutoffs, with slab numbers used only for
cross-checks. [Exp 23]

## 4. Results I: Minkowski

### 4.1 Two dimensions: a logarithm with slope 2

In 1+1 Minkowski the past valency of an element at depth T grows
as

  v(T) = 2 ln(T√ρ) + O(1).

The derivation is elementary: the linked region is a hyperbolic
shell of unit-density measure between the past cone boundary and
the first blocking layer, and its area grows logarithmically with
the cutoff; the coefficient 2 counts the two null directions.
The measurement gives slope 2.01 ± 0.12. [Exp 18a]

The same experiment establishes what we will lean on repeatedly:
valency is *local*. Holding T fixed and growing the sprinkling by
a factor of 8 in N leaves the per-element valency unchanged within
errors. Valency tracks chain depth — how deep an element sits in
its own past — not the global size of the causal set. We record
this as a lemma because it licenses per-element analyses in
inhomogeneous settings, where no global T exists. [Lemma 18a]

### 4.2 Four dimensions: an area law with amplitude π√6

In 3+1 Minkowski the logarithm steepens to a power:

  v(T) = κ₄ √ρ T²,  κ₄ = π√6 ≈ 7.6953.

The exponent is measured as 2.089 ± 0.025 and the amplitude
matches π√6 at the 5% level with no fitted parameters. [Exp 18b]
The T² is an *area* law: the linked shell hugs the past light
cone, whose intersection with the cutoff interval scales as the
cone's lateral area. The constant follows from integrating the
first-blocking-layer probability e^{−ρV} over the hyperboloidal
foliation of the cone neighborhood; π√6 collects the 4D interval
volume coefficient (π/24 in these conventions) through the layer
integral. [Derivation in RESULTS_18b]

Dimensional summary: valency is log-divergent in 2D and
power-divergent in 4D; in both cases the IR-cutoff law has a
derived, parameter-free coefficient that measurement confirms.

## 5. Results II: matter-dominated FRW

Expansion should suppress valency: comoving neighbours recede, and
the effective density in conformal coordinates is diluted by
powers of the scale factor. The question is whether the area law
survives and with what amplitude.

**Transient.** At small conformal extent η the valency is
dominated by a boundary transient. The ensemble is fit well by
v(η) = A η² (1 − B/η); against a free-power alternative the
transient model wins at ΔAIC = +40.7. [Exp 18c] We flag a warning
for future work: a naive short-range power-law fit to the same
data returns an exponent of 2.70 ± 0.07 — the transient
contaminates the exponent long before it is visually obvious. An
early soft-estimator run produced 2.95 for the same quantity;
both numbers are artifacts, of the fit range and of the
e^{−ρV} approximation respectively, and both are superseded by
the exact-blocker, transient-subtracted analysis. [RESULTS_18d
systematic note]

**Asymptote.** Once the transient is subtracted, the area law
reappears with a suppressed amplitude:

  v(η) → κ₄ 𝔉 √ρ_c η²,

where ρ_c is the comoving density and the blocking factor is a
definite integral over the interval's volume-weighted expansion
history. For matter domination (a ∝ η²) with the diamond weight
w(s) = 32 min(s, 1−s)³,

  𝔉 = 30 ∫₀¹ x(1−x)⁸ / √⟨a⁴⟩ dx = 0.4991,

with ⟨a⁴⟩ the diamond-weighted average of a⁴ along the interval.
The measured amplitude ratio is 0.4990 — agreement to four
figures, again with nothing fitted. [Exp 18d; derivation in
RESULTS_18d]

The physical reading is modest and exact: expansion does not
change the *form* of the valency law; it renormalizes the
amplitude by a computable average of the expansion history over
the causal interval. All the geometry enters through ⟨a⁴⟩.

## 6. Results III: the link fraction

Valency divided by the size of the causal past gives a
dimensionless, cutoff-dependent scarcity measure:

  ε(ρ, R) = N_links/N_past = 3√6 / (√ρ R²),

which follows from the area law and the R⁴ volume growth of the
past interval; the measured value tracks the prediction with ≈10%
boundary corrections at our scales. The headline reproduction is
bit-exact from a clean checkout (declared seeds). [Exp 24]

ε is also a cheap **manifoldlikeness discriminator**. At the
reference scale (√ρ R² such that ε_manifold ≈ 0.21), a
transitively-closed random order — a Kleitman–Rothschild-like
non-geometric poset — yields ε ≈ 0.017: an order of magnitude
below the sprinkled value, because transitive closure of random
relations manufactures long chains that de-link almost every pair.
One number, computable in O(N²) from the causal matrix, separates
the two classes without interval-abundance machinery. [Exp 22]

We note without further claim that ε(T) ∝ T⁻² places this quantity
in the well-known family of inverse-square horizon scalings
(Cohen–Kaplan–Nelson bounds, everpresent-Λ heuristics): any T⁻²
law evaluated at the Hubble scale returns a number of order
10⁻¹²². This is a reformulation within that family, not a
discovery, and we make no cosmological use of it here.

## 7. Three-sector accounting: a partition identity

The counting objects of this paper organize into three sectors:
chains (timelike depth h), antichains (spacelike width w), and
links (the bonds). For a weakly disformal rescaling of a metric —
clocks scaled by λ⁻¹ and rulers by λ⁺¹, i.e. ds² =
−λ⁻²c²dt² + λ⁺²dx² to first order — the sector counts of a
faithful sprinkling must respond as

  (chains × λ⁻¹) × (antichains × λ⁺³) = √−g = λ⁺²,

in 3+1 dimensions: the depth of maximal chains scales with proper
time (λ⁻¹), the width of maximal antichains with spatial volume
(λ⁺³), and their product must recover the volume element, which is
what a Poisson sprinkling actually samples. The identity closes:
−1 + 3 = +2. A *conformal* rescaling (clocks and rulers both
λ⁺¹) requires the chain sector to absorb λ⁻⁴ for the same volume
budget — the opposite sign, and countable. [Anisotropy note §1]

We stress the epistemic status: this is a **consistency theorem
about counting**, not a dynamical statement. It says that *if* a
poset's growth is biased so as to mimic a disformal metric, its
chain and antichain sectors must split the volume budget as
(−1, +3); it does not say any natural growth dynamics does so.
Whether biased sequential growth can produce these exponents is an
open, pre-registered question (Section 8). A first toy experiment
in 1+1 dimensions (where the disformal split is (−1, +1) and there
is no surplus to allocate) found the width sector saturating its
budget and the depth sector near zero, with a smooth sign
crossover as the bias increases — a susceptibility-like response,
not a phase transition — but its dimensional targets were mismatched
by design and it decides nothing beyond the toy. [Exp 25,
RESULTS_25]

## 8. Outlook

Three follow-ups are defined and, where marked, pre-registered.

1. **Biased insertion in 3+1 (Exp 25b, in preparation):** a real
   3+1 sprinkling with growth biased by a local resolution field,
   testing whether the (−1, +3) split of Section 7 emerges, with
   antichain widths estimated by the causal-overlap method of
   Boguñá & Krioukov [2024] rather than by raw adjacency — the
   spatial-distance estimators built on adjacency are known to be
   asymptotically silent.
2. **Link fraction in FRW (Exp 24b):** whether ε(T) and its T⁻²
   scaling survive expansion with the same 𝔉-type renormalization
   as the valency law.
3. **Estimator hygiene:** the 2.70/2.95 discrepancy of Section 5 is
   a reproducible case study in how soft link estimators and
   short-range fits bias growth exponents; we release both
   pipelines so the failure can be replayed.

All code, pre-registration documents, per-experiment RESULTS
files, and the exact seeds behind every number in this paper are
public in the project repository. Negative results and superseded
estimates are retained, not deleted.

## Acknowledgments

*(Author's call. Skeleton suggests at most one sentence on the
motivating framework, plus tooling acknowledgments per Zenodo
norms. Left empty by design.)*

## References

*(all verified against arXiv/journal in-repo; final formatting to
the author)*

- L. Bombelli, J. Lee, D. Meyer, R. Sorkin, *Space-time as a causal
  set*, PRL 59, 521 (1987).
- D. Rideout, R. Sorkin, *Classical sequential growth dynamics for
  causal sets*, PRD 61, 024002 (2000).
- R. Sorkin, *Causal sets: discrete gravity*, notes (2003).
- S. Johnston, *Particle propagators on discrete spacetime*,
  arXiv:0806.3083.
- D. Rideout, P. Wallden, *Spacelike distance from discrete causal
  order*, arXiv:0810.1768.
- D. Benincasa, F. Dowker, *The scalar curvature of a causal set*,
  arXiv:1001.2725.
- L. Glaser, S. Surya, *Towards a definition of locality in a
  manifoldlike causal set*, PRD 88, 124026, arXiv:1309.3403.
- S. Surya, *The causal set approach to quantum gravity*, Living
  Reviews in Relativity 22, 5 (2019).
- G. Brightwell, M. Łuczak, arXiv:1510.05612.
- B. Bollobás, G. Brightwell, *The height of a random partial
  order* / box spaces papers (1991/92).
- L. Glaser, arXiv:2306.09904.
- M. Boguñá, D. Krioukov, *Spatial distances in causal sets*,
  PRD 110, 024008, arXiv:2401.17376.
- S. Johnston, arXiv:2111.09331; arXiv:2502.09701.

---

## Notes for the author (not part of the paper)

1. §5 folds the 2.70 vs 2.95 story into a methods warning — it is
   our own systematic, told as such (PROTOCOLO rule 5).
2. §7 keeps Exp 25 as a toy with confessed limits; the paper makes
   no (−1,+3) claim. If 25b lands before submission, §7-8 update.
3. Figures F1-F3 are Codex's queue (from existing outputs); F4 is
   a hand schematic. Prose written so it survives without F4.
4. Johnston 2008 needs the journal ref added (CQG); Bollobás-
   Brightwell needs the exact titles split — flagged rather than
   guessed.
5. Word "render" count in paper body: zero, as per skeleton rule.
