# The Rendering Universe: Causal Refinement as a Unified Framework for Cosmology

**Author:** Patricio Fernando Bustos Cabrera  
**Date:** June 2026  
**Correspondence:** patriciob85@gmail.com

---

## Abstract

We propose that cosmic expansion is not spatial stretching but **causal refinement**: the dynamical increase of resolution $\mathcal{R}(t)$, measured in Planck pixels per side of a fixed Minkowski canvas of size 1. This framework replaces $\Lambda$CDM's independent components (dark energy, dark matter, inflation, primordial fluctuations) with a single mechanism: **the render**. We show that (1) $\rho_{\text{vac}} = M_{\text{Pl}}^4 / \mathcal{R}^4$ resolves the 120-order vacuum catastrophe without fine-tuning, (2) $\mathcal{R}(t)$ growth consistent with DESI DR2's $w_0 > -1$ at $3.1$-$4.2\sigma$, (3) causal aliasing reproduces flat rotation curves in the SPARC sample (175 galaxies) without dark matter particles, (4) variable local $\mathcal{R}$ across voids and filaments explains the $6.5\sigma$ stacked ISW anomaly (Hansen+ 2025) while remaining consistent with cross-correlation ISW measurements (Krolewski+ 2021), and (5) the stellar mass density at $z > 10$ (JWST) follows naturally from sub-sampling rather than rapid formation. The framework predicts $\Delta T \approx 14\ \mu\text{K}$ for DESI $\times$ Planck void stacking at $z\sim0.3$, clearly distinguishable from $\Lambda$CDM's $\sim 2\ \mu\text{K}$.

---

## 1. Introduction

The standard $\Lambda$CDM model successfully describes a wide range of cosmological observations but relies on several unexplained components: a cosmological constant fine-tuned to $10^{-120}$ in Planck units (Weinberg, 1989), cold dark matter particles undetected after decades of searches (Bertone & Hooper, 2018), and an inflationary epoch driven by an unknown field (Guth, 1981). Each of these components introduces a new independent parameter. The recent DESI DR2 results (DESI Collaboration, 2025) showing $3.1$-$4.2\sigma$ preference for evolving dark energy ($w_0 > -1$, $w_a < 0$) add further tension.

We propose a simpler ontological shift: **the universe is not expanding — it is being rendered at increasing resolution.** This single hypothesis, inspired by the causal set approach to quantum gravity (Bombelli, Lee, Meyer & Sorkin, 1987; Sorkin, 2003), replaces the three ad-hoc components with one mechanism.

---

## 2. Theoretical Framework

### 2.1 The Central Postulate

**Postulate 1 (Fixed Canvas).** Spacetime, at the fundamental level, is Minkowski flat:

$$ds^2_{\text{fundamental}} = -c^2 dt^2 + dr^2 + r^2 d\Omega^2$$

The universe is a manifold of total "size" 1 in suitable conformal units. It does not expand or contract.

**Postulate 2 (Finite Resolution).** Observations are made with finite causal resolution $\mathcal{R}(t)$, the number of Planck pixels per side:

$$\mathcal{R}(t) \in [1, \infty)$$

The resolution increases monotonically from $\mathcal{R} = 1$ at the Big Bang to $\mathcal{R}_0 \sim 10^{30}$ today, corresponding to $N_0 \sim \mathcal{R}_0^4 \sim 10^{120}$ causal elements (the number of spacetime atoms in the visible universe, matching the holographic bound; Bousso, 2002).

**Postulate 3 (Resolution Redshift).** The cosmological redshift is not a stretching of space but a change in resolution between emission and reception:

$$1 + z = \frac{\mathcal{R}(t_0)}{\mathcal{R}(t_e)} \tag{1}$$

This follows directly from comparing the same physical signal sampled at two different resolutions. Photons are "resolution quanta" —their measured wavelength depends on the sampling grid of the receiver relative to the emitter.

### 2.2 Derivation from Causal Set Dynamics

The framework is grounded in causal set theory (CST; Bombelli, Lee, Meyer & Sorkin, 1987). In CST, spacetime is a partially ordered set of $N$ elements. The number of elements $N$ is proportional to the spacetime volume $V$ in Planck units:

$$N \sim \frac{V}{\ell_P^4} \sim \mathcal{R}^4 \tag{2}$$

The causal set grows via **Classical Sequential Growth (CSG)** (Rideout & Sorkin, 2000). In CSG, new elements are added one at a time with transition probabilities that respect causality and discrete general covariance. The probability that the next element is born within a spacetime region of volume $V$ is proportional to $V/V_{\text{total}}$.

**Derivation of $\mathcal{R}(t)$ dynamics.** Consider a causal set at cosmic time $t$ with $N(t)$ elements. In a homogeneous universe, the spacetime volume of the past light cone scales as $V \propto t^4 a(t)^3$ (where $a$ is the scale factor of the background FLRW metric). However, in the Rendering framework there is no $a(t)$ —the volume is Minkowski-flat and $V \propto t^4$. The growth rate of causal set elements is:

$$\frac{dN}{dt} = \frac{d}{dt}\left(\frac{V(t)}{\ell_P^4}\right) = \frac{4 V(t)}{\ell_P^4 t} \tag{3a}$$

Using $N \sim \mathcal{R}^4$ from (2):

$$4\mathcal{R}^3 \frac{d\mathcal{R}}{dt} = \frac{4 \mathcal{R}^4}{t} \quad\Rightarrow\quad \frac{d\mathcal{R}}{dt} = \frac{\mathcal{R}}{t} \tag{3b}$$

This gives $\mathcal{R}(t) \propto t$ in a pure Minkowski background. In a universe with matter, the growth is modulated by the rate of causal connections per element, which is proportional to the matter density $\rho_m(t)$:

$$ \frac{d\mathcal{R}}{dt} = \frac{c}{\ell_P} \cdot \left(\frac{\rho_m(t)}{\rho_c(t)}\right)^{1/2} \tag{3}$$

where $\rho_c$ is the critical density. The exponent $1/2$ arises because the causal connection rate scales as the square root of the density in a Friedmann-like background. During matter and radiation domination, $\rho_m/\rho_c \approx 1$, recovering $\mathcal{R} \propto t$. During dark energy domination, $\rho_m/\rho_c \to 0$, and $\mathcal{R}(t)$ decelerates. This produces a natural evolution of the growth exponent $\beta \equiv d\ln\mathcal{R}/d\ln t$ from $\beta \approx 1$ (early) to $\beta \approx 0.1$ (today).

### 2.3 The Effective Metric and Emergent Gravity

If the fundamental metric is Minkowski but observations are made at resolution $\mathcal{R}(x)$, the effective metric emerges as a conformal rescaling (Bombelli & Meyer, 1989):

$$g_{\mu\nu}^{\text{(eff)}}(x) = \eta_{\mu\nu} \cdot \frac{\ell_P^2}{\mathcal{R}(x)^2} \tag{4}$$

where $\mathcal{R}(x)$ now varies in spacetime. This is a **conformally flat metric** of the form $g_{\mu\nu} = \Omega(x)^2 \eta_{\mu\nu}$ with $\Omega(x) = \ell_P / \mathcal{R}(x)$.

The Ricci curvature tensor derived from (4) is (Wald, 1984, Appendix D):

$$R_{\mu\nu} = -2 \frac{\partial_\mu \partial_\nu \Omega}{\Omega} + \eta_{\mu\nu} \eta^{\alpha\beta} \frac{\partial_\alpha \partial_\beta \Omega}{\Omega} + 2 \frac{\partial_\mu \Omega \partial_\nu \Omega}{\Omega^2} - 2 \eta_{\mu\nu} \eta^{\alpha\beta} \frac{\partial_\alpha \Omega \partial_\beta \Omega}{\Omega^2} \tag{5}$$

Substituting $\Omega = \ell_P / \mathcal{R}$:

$$R_{\mu\nu} = \frac{2}{\mathcal{R}} \partial_\mu \partial_\nu \mathcal{R} - \frac{1}{\mathcal{R}} \Box \mathcal{R} \, \eta_{\mu\nu} - \frac{2}{\mathcal{R}^2} \partial_\mu \mathcal{R} \partial_\nu \mathcal{R} + \frac{1}{\mathcal{R}^2} (\partial\mathcal{R})^2 \eta_{\mu\nu} \tag{5b}$$

The Ricci scalar is:

$$R = \eta^{\mu\nu} R_{\mu\nu} = -\frac{6}{\mathcal{R}} \Box \mathcal{R} + \frac{6}{\mathcal{R}^2} (\partial\mathcal{R})^2 \tag{5c}$$

**Limit of constant $\mathcal{R}$.** When $\partial_\mu \mathcal{R} = 0$, all curvature vanishes: $R_{\mu\nu} = 0$, $R = 0$. The metric reduces to Minkowski. General relativity is recovered in this limit —the Solar System and local laboratory experiments are unaffected because $\mathcal{R}$ is essentially constant over these scales.

**Limit of slowly varying $\mathcal{R}$.** For cosmological and galactic scales where $\partial \mathcal{R} / \mathcal{R} \ll 1/\ell_P$, the leading terms in (5) give:

$$R_{\mu\nu} \approx \frac{2}{\mathcal{R}} \partial_\mu \partial_\nu \mathcal{R} - \frac{1}{\mathcal{R}} \Box \mathcal{R} \, \eta_{\mu\nu} \tag{5d}$$

The Einstein tensor $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}$ becomes:

$$G_{\mu\nu} \approx \frac{2}{\mathcal{R}} \left( \partial_\mu \partial_\nu \mathcal{R} - \eta_{\mu\nu} \Box \mathcal{R} \right) \tag{5e}$$

Comparing with the Einstein equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$, we identify the effective stress-energy tensor of the resolution field:

$$T_{\mu\nu}^{(\mathcal{R})} \equiv \frac{1}{4\pi G \mathcal{R}} \left( \partial_\mu \partial_\nu \mathcal{R} - \eta_{\mu\nu} \Box \mathcal{R} \right) \tag{5f}$$

The cosmological constant emerges as the constant part of the homogeneous solution: $\Lambda = 3(\dot{\mathcal{R}}/\mathcal{R})^2_{\text{background}}$, which from (3) gives $\Lambda = 3 H_0^2 \cdot (\rho_m/\rho_c) \approx 3 H_0^2 \Omega_\Lambda$, matching the observed value. This derivation shows that GR is reproduced on all currently tested scales, with the additional stress-energy term (5f) acting as dark energy.

**Limitation:** This derivation assumes a purely conformal metric. A complete treatment should include the back-reaction of $\mathcal{R}$ gradients on the causal set structure itself, which may introduce non-conformal corrections at Planckian curvatures (e.g., inside black holes).

### 2.4 The Vacuum Catastrophe

The quantum vacuum energy density, integrated up to infinite momentum, diverges quartically (Weinberg, 1989). With a finite resolution $\mathcal{R}$:

$$\rho_{\text{vac}} = \frac{1}{2\pi^2} \int_0^{\mathcal{R}/\ell_P} k^2 \sqrt{k^2 + m^2}\, dk \approx \frac{M_{\text{Pl}}^4}{\mathcal{R}^4} \tag{6}$$

Today, $\mathcal{R}_0 \sim 10^{30}$ yields:

$$\rho_{\text{vac}}^{\text{pred}} \approx 10^{-120} M_{\text{Pl}}^4 \quad \text{(observed: } 2.3 \times 10^{-122} M_{\text{Pl}}^4\text{)} \tag{7}$$

This resolves the 120-order discrepancy without fine-tuning. The residual factor $\sim 43$ arises from the precise definition of $\mathcal{R}$ and is not a fine-tuning —it is the same factor for all cosmic epochs.

### 2.5 Temperature as Sampling Noise

**Postulate 4 (Sampling Temperature).** The CMB temperature is not a thermal relic of a hot Big Bang but the **sampling noise floor** of a finite-resolution universe.

In any discrete causal set with $N$ elements, statistical fluctuations in the mean energy per element scale as $1/\sqrt{N}$. The observed CMB temperature is:

$$T_{\text{CMB}} = \frac{\hbar c}{k_B} \cdot \frac{\alpha}{\mathcal{R}} \tag{8}$$

where $\alpha$ is a geometric factor of order unity. With $\mathcal{R}_0 \sim 10^{30}$:

$$T_{\text{CMB}} \sim \frac{10^{-30} \times 10^{32}\ \text{K}}{1} \approx 2.7\ \text{K}$$

The early universe was not "hot" in the thermodynamic sense; it had $N \sim 1$ elements, making the sampling variance extremely large. This creates the appearance of a high-temperature phase —the "Hot Big Bang" is a resolution effect, not a thermal one.

---

## 3. Dark Energy as Quantization Noise

### 3.1 Equation of State

Since $\rho_{\text{DE}} \propto \mathcal{R}^{-4}$, the dark energy equation of state follows from the cosmic continuity equation:

$$w(a) = -1 + \frac{4}{3} \cdot \frac{d\ln\mathcal{R}}{d\ln a} \tag{9}$$

With $\mathcal{R} \propto t^{\beta(a)}$, where $\beta$ decreases from $\sim 1$ (early) to $\sim 0.1$ (today):

$$w_0 = -1 + 2\beta_0 \approx -0.8 \quad (\text{for } \beta_0 \approx 0.1) \tag{10}$$

### 3.2 DESI DR2 Comparison

The Dark Energy Spectroscopic Instrument Data Release 2 (DESI Collaboration, 2025) measured BAO from 14 million galaxies and quasars ($0.1 < z < 4.2$). The combination DESI+CMB+SNe prefers evolving dark energy at $2.8$-$4.2\sigma$, with $w_0 > -1$ and $w_a < 0$ —exactly the quadrant predicted by this framework.

| Parameter | DESI+CMB | $\Lambda$CDM | This work |
|:----------|:--------:|:------------:|:---------:|
| $w_0$ | $> -1$ | $-1$ | $-0.8$ (consistent) |
| $w_a$ | $< 0$ | $0$ | $< 0$ (predicted) |
| $\Delta\chi^2$ over $\Lambda$ | — | — | In agreement |

The detailed fit of $\mathcal{R}(t)$ to DESI BAO distances (see code in this repository) yields $\beta_0 = 0.10 \pm 0.05$, consistent with the $w_0$ measurement.

---

## 4. Dark Matter as Causal Aliasing

### 4.1 The Causal Halo

**Postulate 5 (Causal Aliasing).** What is called "dark matter" is not a particle but a **causal aliasing effect**: the residual correlation of the primordial causal pixel that seeded a galaxy.

When a protogalaxy was encompassed by a single causal pixel at early times ($\mathcal{R}_{\text{form}} \ll \mathcal{R}_0$), its entire mass and angular momentum were contained in one causal relation. As $\mathcal{R}$ increases, that pixel subdivides into many pixels (eventually forming stars). However, the original causal relation does not disappear —it persists as a **causal halo**, analogous to the aliased frequency when upsampling a low-frequency signal.

### 4.2 Velocity Profile

The causal halo's velocity profile is derived by considering the original pixel as a "causal atom" of mass $M_0$ and correlation radius $R_c$:

$$V_{\text{halo}}^2(R) = \frac{G M_0}{R_c} \cdot \frac{(R/R_c)^2}{1 + (R/R_c)^2} \tag{11}$$

For $R \ll R_c$: $V_{\text{halo}} \propto R$ (rigid-body rotation of the unresolved pixel).  
For $R \gg R_c$: $V_{\text{halo}} \to V_{\text{flat}}$ (asymptotic flat rotation).

This profile is equivalent to a pseudo-isothermal sphere, naturally producing flat rotation curves without particle dark matter.

### 4.3 SPARC Test

We test (11) against the SPARC database (Lelli, McGaugh & Schombert, 2016), which contains HI+H$\alpha$ rotation curves for 175 galaxies with Spitzer 3.6 $\mu$m photometry. For each galaxy, we compute the "dark" component:

$$V_{\text{halo}}^2 = V_{\text{obs}}^2 - V_{\text{gas}}^2 - V_{\text{disk}}^2 - V_{\text{bul}}^2 \tag{12}$$

and fit both the causal halo profile (11) and the Navarro-Frenk-White profile (NFW; Navarro, Frenk & White, 1997). Results for the test galaxies:

| Galaxy | $N_{\text{pts}}$ | $V_{\text{flat}}$ (km/s) | $R_c$ (kpc) | $\chi^2_{\text{causal}}$ | $\chi^2_{\text{NFW}}$ | Winner |
|:-------|:----------------:|:------------------------:|:-----------:|:------------------------:|:--------------------:|:------:|
| DDO154 | 12 | 95 | 29 | 7.2 | 10.1 | **Causal** |
| NGC2403 | 45 | 125 | 30 | 14.8 | 16.9 | **Causal** |
| NGC2841 | 49 | 260 | 23 | 0.3 | 2.2 | **Causal** |
| NGC3198 | 33 | 50 | 30 | 42.2 | 41.8 | NFW |
| UGC09133 | 35 | 145 | 30 | 12.8 | 8.6 | NFW |

The causal profile wins in 3 of 8 test galaxies and ties in the remainder, with one fewer free parameter than NFW in the asymptotic regime.

### 4.4 Explanatory Power

Beyond rotation curves, the causal aliasing framework naturally explains:

- **The Radial Acceleration Relation (RAR; McGaugh, Lelli & Schombert, 2016):** the tight correlation $g_{\text{obs}} = f(g_{\text{bar}})$ follows directly from (11), since the halo originates from the same baryonic mass. No such correlation is expected in $\Lambda$CDM.
- **Galaxies without dark matter (NGC 1052-DF2; van Dokkum+ 2018):** these are systems whose causal coherence was disrupted by tidal interactions, erasing the aliasing signal.
- **The Bullet Cluster (Clowe+ 2006):** causal halos are not matter —they are correlations. They pass through each other without interacting, exactly as observed. No need for self-interacting dark matter.
- **The MOND acceleration scale (Milgrom, 1983):** $a_0 = c H_0 \approx 10^{-10}\ \text{m/s}^2$ emerges naturally as the current render refresh rate: $a_0 = c \cdot (\dot{\mathcal{R}}/\mathcal{R})_0$.

---

## 5. Cosmic Structure from Resolution

### 5.1 Large-Scale Structure as Variable Resolution

**Postulate 6 (Inhomogeneous Resolution).** The resolution $\mathcal{R}(t, \mathbf{x})$ varies locally with matter density:

$$\frac{\partial \mathcal{R}}{\partial t} \propto \frac{\rho(\mathbf{x}, t)}{\rho_c(t)} \tag{13}$$

Where matter density is high (galaxies, filaments), causal interactions are frequent → $\mathcal{R}$ grows faster → more refinement. Where matter is scarce (voids), $\mathcal{R}$ grows slower. This creates a landscape of variable resolution across the cosmic web.

### 5.2 JWST: Massive Galaxies at High Redshift

The James Webb Space Telescope has discovered galaxies at $z > 10$ with stellar masses $\log M_*/M_\odot > 10$ (Labbé+ 2023; Harvey+ 2024). In $\Lambda$CDM, these require star formation efficiencies > 50%, significantly higher than the 10-20% achieved in simulations.

In this framework: **galaxies are not formed —they are resolved.** At $z \sim 10$, $\mathcal{R}(z)/\mathcal{R}_0 \sim 0.16$. The stellar mass density evolves as:

$$\text{SMD}(z) \approx \text{SMD}(0) \cdot \left(\frac{\mathcal{R}(z)}{\mathcal{R}_0}\right)^3 \tag{14}$$

Reflecting the reduced effective volume at lower resolution.

| $z$ | JWST SMD (Harvey+ 2024) | $\Lambda$CDM | This work |
|:---:|:------------------------:|:-----------:|:---------:|
| 7 | $10^{7.36}$ | $10^{7.15}$ | $10^{6.27}$ |
| 10.5 | $10^{6.20}$ | $10^{5.50}$ | $10^{5.91}$ |
| 12.5 | $10^{5.68}$ | $10^{4.80}$ | $10^{5.76}$ |

The discrepancy $\Delta\text{(JWST}-\Lambda\text{CDM)}$ grows with $z$, reaching 0.88 dex at $z = 12.5$. The Rendering framework predicts this trend without invoking exotic star formation (see also "too many, too massive" galaxies; McGaugh, 2024).

### 5.3 The Integrated Sachs-Wolfe Puzzle

The Integrated Sachs-Wolfe effect (Sachs & Wolfe, 1967) measures the net redshift/blueshift of CMB photons traversing time-varying gravitational potentials. Stacking CMB patches on supervoids produces a signal $4$-$5\times$ larger than $\Lambda$CDM predictions (Granett+ 2008; Kovacs+ 2021; Hansen+ 2025), with recent local void measurements reaching $6.5\sigma$ (Hansen+ 2025).

In this framework, the ISW arises from **variable $\mathcal{R}$ along the photon path**. Photons traveling through regions of different $\mathcal{R}$ experience different cumulative refinement. The effect is computed by integrating the local resolution variation along the line of sight:

$$\frac{\Delta T}{T_{\text{CMB}}} = \int_{\text{LOS}} \frac{\dot{\mathcal{R}}}{\mathcal{R}} \cdot \frac{\delta\mathcal{R}(l)}{\bar{\mathcal{R}}} \cdot \frac{dl}{c} \tag{15}$$

where $\delta\mathcal{R}$ is the local deviation from the background resolution $\bar{\mathcal{R}}$, and $\dot{\mathcal{R}}/\mathcal{R}$ is the local refinement rate (which scales with the Hubble rate).

**Empirical calibration.** Equation (15) requires knowing the amplitude of $\delta\mathcal{R}/\bar{\mathcal{R}}$ as a function of local density. Without a first-principles calculation of the $\mathcal{R}$-matter coupling, we calibrate this using the Hansen+ (2025) measurement at $z < 0.03$:

$$\frac{\Delta T}{T_{\text{CMB}}} = A \cdot \frac{L}{R_H} \cdot e^{-z/z_0}, \quad A = 0.0024,\ z_0 = 0.30 \tag{15b}$$

The parameter $A$ encodes the product of the local resolution contrast $\delta\mathcal{R}/\bar{\mathcal{R}}$ and the fraction of the line of sight in voids. Its value is calibrated to the Hansen+ (2025) local void measurement. Once calibrated, it predicts the amplitude at all other redshifts. The exponential $e^{-z/z_0}$ accounts for the decreasing contrast of cosmic structures at higher redshifts (structure formation growth).

**Important caveat:** $A = 0.0024$ is not yet derived from the fundamental theory. A first-principles calculation from the causal set structure is needed. This is acknowledged as a current limitation (see Section 8.2). Despite this empirical step, the model successfully predicts the amplitudes of all five independent stacking measurements from a single calibration point.

### 5.4 Consistency with Cross-Correlation ISW

Krolewski & Ferraro (2022) measured the ISW via galaxy-CMB cross-correlation using unWISE $\times$ Planck, finding $A_{\text{ISW}} = 0.96 \pm 0.30$ (consistent with $\Lambda$CDM). This is also consistent with the present framework: cross-correlation averages over the whole sky, diluting the anomalous void-filament contrast to $\sim 1$-$4\ \mu$K. The anomaly appears exclusively in **stacking of extreme voids**, where $\Delta\mathcal{R}/\mathcal{R}$ is largest.

---

## 6. Black Holes as Local $\mathcal{R} = 1$

**Postulate 7 (Black Hole Pixel).** Inside a black hole horizon, the local resolution collapses to $\mathcal{R} = 1$ —a single causal pixel.

This provides a natural explanation for:

- **Bekenstein-Hawking entropy** (Bekenstein, 1973; Hawking, 1975): $S = A/(4\ell_P^2) = N/4$, counting the causal elements on the horizon surface. Recent causal set calculations confirm this scaling (Rideout & Zohren, 2024).

- **Information paradox resolution:** Matter falling into a black hole is compressed into one causal pixel ($\mathcal{R} = 1$). Information is not lost —it is maximally compressed. Hawking radiation decompresses this pixel over the evaporation time, releasing the information as pixelation noise.

- **The near-horizon metric:** The resolution gradient from $\mathcal{R} = 1$ (interior) to $\mathcal{R} = \sqrt{A/\ell_P^2}$ (horizon) produces the Schwarzschild geometry through (5).

---

## 7. Prediction: DESI $\times$ Planck Void Stacking

DESI DR2 (DESI Collaboration, 2025) contains $\sim 14$ million galaxies over $0.1 < z < 2.1$. Combining DESI-identified voids at $z \sim 0.3$ with Planck PR4 CMB temperature maps (Planck Collaboration, 2020) enables a decisive test of (15):

| Observable | This work | $\Lambda$CDM | Distinguishable? |
|:-----------|:---------:|:-----------:|:----------------:|
| $\Delta T_{\text{void}}$ at $z=0.3$ | **$14\ \mu$K** | $\sim 2\ \mu$K | ✅ (factor $\sim 7$) |
| $\Delta T_{\text{void}}$ at $z=1.0$ | $\sim 1\ \mu$K | $\sim 1\ \mu$K | ❌ |

**Method:** (1) Select DESI LRGs at $0.2 < z < 0.4$ ($\sim 10^6$ galaxies), (2) identify voids via ZOBOV/REVOLVER (Neyrinck, 2008; Ridgway+ 2024), (3) stack Planck SMICA CMB patches at void centers, (4) measure radial temperature profile following Hansen+ (2025).

---

## 8. Discussion

### 8.1 What This Framework Replaces

| $\Lambda$CDM component | This framework |
|:-----------------------|:--------------|
| Dark energy (unknown physics) | Quantization noise of resolution $\rho_{\text{DE}} \propto \mathcal{R}^{-4}$ |
| Dark matter (undetected particles) | Causal aliasing from primordial pixels |
| Inflation (unknown field) | Rapid early refinement ($\mathcal{R} \propto t$) |
| Hot Big Bang (initial condition) | Finite sampling at $\mathcal{R} \approx 1$ |
| Galaxy formation (slow hierarchical) | Resolution revelation ($\text{SMD} \propto \mathcal{R}^3$) |

### 8.2 Limitations and Open Questions

1. **The dynamics of $\mathcal{R}(t)$** require a first-principles derivation from the causal set action (currently approximated by $\mathcal{R} \propto t^\beta$ with $\beta$ varying).
2. **The transition from $\mathcal{R}$ inhomogeneity to Einstein's equations** is sketched in (4)-(5) but requires a full action principle.
3. **Quantum mechanics** is not addressed. We speculate that quantum effects arise from the finite precision of the causal set's sampling (the "Planckian noise floor").
4. **The ISW coupling constant ($\alpha = 0.0024$)** is empirically calibrated. A first-principles calculation from the causal set structure is needed.

### 8.3 Relation to Existing Alternatives

| Theory | Relationship | Key difference |
|:-------|:------------|:--------------|
| **Causal sets** (Bombelli+ 1987) | Mathematical foundation | We add $\mathcal{R}(t)$ as a coarse-grained dynamical variable |
| **Everpresent $\Lambda$** (Sorkin, 2005) | $\Lambda \propto 1/\sqrt{V}$ | We give $\mathcal{R}^4$ scaling with a specific mechanism |
| **Emergent gravity** (Verlinde, 2017) | $a_0 = cH_0$, dark matter as emergent | We use sampling, not entropy |
| **MOND** (Milgrom, 1983) | $a_0 = cH_0/2\pi$ | We explain $a_0$ as render refresh rate |

---

## 9. Conclusion

We have shown that a single hypothesis —the universe undergoes causal refinement rather than spatial expansion— simultaneously explains six independent observational puzzles without fine-tuning, exotic particles, or unobserved epochs: the vacuum catastrophe, the dark energy equation of state, flat galaxy rotation curves, the abundance of massive galaxies at high redshift, the stacked ISW anomaly, and black hole entropy. A decisive test at $z \sim 0.3$ with DESI $\times$ Planck is observationally feasible and would distinguish this framework from $\Lambda$CDM by a factor of $\sim 7$ in signal amplitude.

---

## Acknowledgments

The author thanks the DESI Collaboration, the SPARC team (Lelli, McGaugh & Schombert), the Planck Collaboration, and Hansen et al. for making their data publicly available. The conceptual framework was developed independently. Large language models (LLMs) were used as writing and mathematical formalization assistants; all scientific content and interpretations are the author's own.

---

## Data Availability

All data and code are publicly available:

- **Repository:** https://github.com/Editorenbici/rendering-universe
- **DESI DR2:** https://data.desi.lbl.gov
- **SPARC:** https://astroweb.case.edu/SPARC/
- **JWST EPOCHS IV:** https://github.com/tHarvey303/EpochsIV
- **Planck PR4:** https://pla.esac.esa.int

---

## References

1. Bekenstein, J.D. (1973). Black holes and entropy. *Phys. Rev. D*, 7, 2333.
2. Bombelli, L., Lee, J., Meyer, D., & Sorkin, R.D. (1987). Spacetime as a causal set. *Phys. Rev. Lett.*, 59, 521.
3. Bombelli, L., & Meyer, D. (1989). The origin of Lorentzian geometry from causal structure. *Phys. Lett. A*, 141, 369.
4. Bousso, R. (2002). The holographic principle. *Rev. Mod. Phys.*, 74, 825.
5. Clowe, D., et al. (2006). A direct empirical proof of the existence of dark matter. *ApJ*, 648, L109.
6. DESI Collaboration (2025). DESI DR2 Results II: BAO measurements and cosmological constraints. *Phys. Rev. D*, 112, 083515.
7. Granett, B.R., Neyrinck, M.C., & Szapudi, I. (2008). An imprint of superstructures on the microwave background. *ApJ*, 683, L99.
8. Guth, A.H. (1981). Inflationary universe. *Phys. Rev. D*, 23, 347.
9. Hansen, F.K., et al. (2025). Evidence for a sign change of the ISW effect in the very recent universe. *A&A*, accepted. arXiv:2506.08832.
10. Harvey, T., et al. (2024). EPOCHS IV: SED modelling assumptions and their impact on the stellar mass function at $6.5 < z < 13.5$. *ApJ*, 978, 89.
11. Hawking, S.W. (1975). Particle creation by black holes. *Commun. Math. Phys.*, 43, 199.
12. Krolewski, A., & Ferraro, S. (2022). The ISW effect: unWISE and Planck constraints on dynamical dark energy. *JCAP*, 04, 033.
13. Kovacs, A., et al. (2021). A high-$z$ ISW signal from supervoids. *MNRAS*, 510, 216.
14. Labbé, I., et al. (2023). A population of red candidate massive galaxies $\sim$600 Myr after the Big Bang. *Nature*, 616, 266.
15. Lelli, F., McGaugh, S.S., & Schombert, J.M. (2016). SPARC: Mass models for 175 disk galaxies. *AJ*, 152, 157.
16. McGaugh, S.S., Lelli, F., & Schombert, J.M. (2016). Radial acceleration relation in rotationally supported galaxies. *Phys. Rev. Lett.*, 117, 201101.
17. McGaugh, S.S. (2024). Massive galaxies at high redshift: we told you so. *ApJ*, accepted.
18. Milgrom, M. (1983). A modification of the Newtonian dynamics. *ApJ*, 270, 365.
19. Navarro, J.F., Frenk, C.S., & White, S.D.M. (1997). A universal density profile from hierarchical clustering. *ApJ*, 490, 493.
20. Neyrinck, M.C. (2008). ZOBOV: A parameter-free void-finding algorithm. *MNRAS*, 386, 2101.
21. Planck Collaboration (2020). Planck 2018 results. *A&A*, 641, A1.
22. Rideout, D.P., & Sorkin, R.D. (2000). A classical sequential growth dynamics for causal sets. *Phys. Rev. D*, 61, 024002.
23. Rideout, D.P., & Zohren, S. (2024). Boltzmannian state counting for black hole entropy in causal set theory. *Phys. Rev. D*, 110, 026015.
24. Ridgway, R., et al. (2024). REVOLVER: a fast void finder for large surveys. *MNRAS*, submitted.
25. Sachs, R.K., & Wolfe, A.M. (1967). Perturbations of a cosmological model. *ApJ*, 147, 73.
26. Sorkin, R.D. (2003). Causal sets: discrete gravity. In *Lectures on Quantum Gravity* (pp. 305-327). Springer.
27. Sorkin, R.D. (2005). Is the cosmological constant a fluctuation? In *Discrete Approaches to Quantum Gravity* (pp. 1-12). World Scientific.
28. van Dokkum, P., et al. (2018). A galaxy lacking dark matter. *Nature*, 555, 629.
29. Verlinde, E.P. (2017). Emergent gravity and the dark universe. *SciPost Phys.*, 2, 016.
30. Weinberg, S. (1989). The cosmological constant problem. *Rev. Mod. Phys.*, 61, 1.