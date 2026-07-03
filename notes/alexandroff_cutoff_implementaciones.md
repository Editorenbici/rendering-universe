# Alexandroff (one-point) compactification para cutoff computacional

**Búsqueda:** Grok (xAI), 2026-07-03

- Literatura: mayormente teoría pura (topología estándar); en física
  se usa conceptualmente (compactificaciones, AdS/CFT, QG).
- **Sin implementaciones ejecutables encontradas** para sistemas
  numéricos discretos con cutoff (2020-2026).
- Sugerencia de Grok: "habría que implementarla desde cero (fácil en
  posets: añadir ∞ y ajustar topología)".

---

## AUDITORÍA (Fable, 2026-07-03)
**"Desde cero" ya está hecho — en este repo.** `21b_nr_arithmetic.py`
implementa operativamente la compactificación de un punto POR GRADO:
cada pantalla ℕ_R tiene sus puntos fuera-de-pantalla (+∞_R, −∞_R,
detectados por `_check_screen`) y su elemento de ignorancia máxima
(⊤_R), con reglas aritméticas y de comparación completas (14 tests).
Si la búsqueda de Grok es correcta y no existe otra implementación,
la del repo sería la primera instancia ejecutable de una
compactificación de Alexandroff graduada por resolución. Anotado con
la cautela de siempre: "no encontrada" ≠ "no existe".
