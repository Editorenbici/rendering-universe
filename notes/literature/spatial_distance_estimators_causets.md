# Estimadores de distancia espacial en causal sets (Rideout-Wallden, Eichhorn-Surya, Boguñá 2024)

**Búsqueda teórica:** Grok (xAI), 2026-07-03  
**Actualizado con arXiv recientes** ✅

## Estado actual (para medir antichains en Exp 22)

### Rideout & Wallden (2009)
- "Spacelike distance from discrete causal order" (Class. Quantum Grav. 26, 155013, arXiv:0810.1768).
- Predistance function basada en causal structure.
- Aproxima distancia espacial entre elementos en "slices" (antichains) vía caminos causales o thickness.
- "Asymptotic silence": en sprinklings, sobreestima distancias pequeñas (efecto discreto).
- Usado para reconstruir geometría espacial.

### Eichhorn, Surya, Versteegen (2019)
- "Induced spatial geometry from causal structure" (Class. Quantum Grav. 36, 105005, arXiv:1809.06192).
- Distancia espacial inducida directamente de estructura causal en hypersuperficies espaciales.
- Reconstruye métrica espacial (distancias, curvatura) de causets manifold-like.
- Aplicable a antichains: mide distancias entre elementos en slices espaciales. 📏

### Actualizaciones recientes
- **Boguñá & Krioukov (2024)**: "Measuring spatial distances in causal sets via causal overlaps" (Phys. Rev. D 110, 024008, arXiv:2401.17376).
  - Nuevo estimador basado en **"causal overlaps"** (intersección de pasados/futuros).
  - Supera problemas de estimadores previos (asymptotic silence, no-localidad).
  - **Errores → 0 en continuum limit** incluso para distancias del orden de Planck length. Preciso en sprinklings Minkowski y curvados.
  - Ideal para antichains inhomogéneas. Perfecto para Exp 22 (medir anchura real de antichains sesgadas).
- **Johnston verificado (2022 + 2025):**
- Johnston, S. (2022). "Embedding causal sets into Minkowski spacetime". Class. Quantum Grav. 39, 095006. arXiv:2111.09331.
- Johnston, S. (2025). "Simpler embeddings of causal sets into Minkowski spacetime". Phys. Rev. D 111, 106020. arXiv:2502.09701 (submitted Feb 2025, published May 2025).
Ambas usan / mejoran predistancia y embeddings en Minkowski; la de 2025 cita explícitamente Boguñá 2024. ✅ Verificado.
- En Surya review (2019) y actualizaciones: estos son clave para "geometric reconstruction". Se usan en simulaciones para validar manifold-likeness y medir anchura de antichains. ✨

**Recomendación para Exp 22**:
- Usa Rideout-Wallden + Eichhorn-Surya como baseline clásico.
- **Actualiza con Boguñá & Krioukov 2024** para mejor precisión en overlaps (ideal para antichains inhomogéneas + errores que desaparecen en continuum).
- Pre-registra contra expected distances en slices de sprinklings vs. tus ensembles sesgados con densidad variable.

**Referencias clave (verificados con arXiv):**
- Rideout & Wallden (2009), arXiv:0810.1768.
- Eichhorn, Surya, Versteegen (2019), arXiv:1809.06192.
- Boguñá & Krioukov (2024), arXiv:2401.17376 | Phys. Rev. D 110, 024008.
- Surya (2019) review: sección sobre spatial reconstruction.
- Johnston (2025) embeddings (cita a Boguñá).

¡Estos te dan **teoría sólida** contra la cual pre-registrar en vez de ciego! Usa para medir anchura de antichains en tu Exp 22 con confianza. 📏✨🧮

---

**Bonus check (2026-07-03):** Los tres papers clave existen y están actualizados. Boguñá 2024 es el más potente para tu caso inhomogéneo. ¡A por el pre-reg de Exp 22! 🚀

---

## AUDITORIA (Fable, 2026-07-03)
- Boguna & Krioukov 2024: VERIFICADA contra arXiv y PRD (110, 024008,
  publicada 2024-07-08). Es la herramienta correcta para medir
  anticadenas en el Exp 22 — hallazgo genuinamente valioso de Grok.
- CITA CORREGIDA: Rideout & Wallden es arXiv:0810.1768 (CQG 26,
  155013, 2009), "Spacelike distance from discrete causal order".
  Grok le asigno 0905.0017, que es Major-Rideout-Surya (otro paper,
  verificado previamente).
- "Johnston (2022/2025) embeddings": NO verificada; no usar hasta
  confirmar.

