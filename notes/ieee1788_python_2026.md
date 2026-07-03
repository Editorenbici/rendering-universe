# IEEE 1788-2015 interval arithmetic — estado Python 2024-2026

**Búsqueda:** Grok (xAI), 2026-07-03

- **pyinterval** (taschini): la más citada, funcional, actividad baja
  pero estable; compliance básica IEEE 1788.
- **IntvalPy** (2023): moderna, menos madura.
- **mpmath.iv** (1.4.0, 2026): activa; intervalos rudimentarios.
- Testing de compliance: ITF1788.

Conclusión de Grok: pyinterval sigue siendo de lo más estable; no hay
reemplazo claro 2024-2026.

---

## AUDITORÍA (Fable, 2026-07-03) — DECISIÓN DE DISEÑO PARA 21b
**NO migrar 21b a pyinterval.** Razón técnica: pyinterval trabaja con
extremos en punto flotante con redondeo hacia afuera — resuelve el
problema de *encierros rigurosos sobre floats*. ℕ_R necesita extremos
**diádicos exactos** (`Fraction`): los cumpleaños de Conway, la regla
del más simple y el test "1/3 no nace nunca" son aritmética exacta —
con floats esas propiedades se rompen o se vuelven aproximadas.
pyinterval queda anotada como opción SOLO si algún día hace falta un
modo float de alto rendimiento a gran escala. 21b se queda como está.
