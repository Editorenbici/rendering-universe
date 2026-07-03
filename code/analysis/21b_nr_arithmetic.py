#!/usr/bin/env python3
"""
21b: N_R — aritmetica de resolucion finita (diseno aprobado 2026-07-03)
========================================================================
Un numero a resolucion R es un INTERVALO DIADICO [lo, hi] (Fractions
exactos, denominadores potencia de 2). El "par (mantisa, R)" del spec
es la vista externa: mantisa = representante mas simple (regla de
cumpleanos de Conway), R = -log2(ancho).

Dos capas (nota "El TODO en vez del infinito", seccion 5):
  - RASTER: NR con ancho 2^-R (lo medido).
  - VECTORIAL: NR.exact(q) con ancho 0, R=inf (numeros cuanticos,
    razones de simetria; 1/3 vive aca, exacto, sin dia finito).

LEYES:
  - Suma/resta: R_efectivo ~ min(R1,R2). El grueso manda (ley del
    minimo = propagacion de errores).
  - Multiplicacion: propagacion EXACTA de intervalos. NOTA DE SPEC:
    la regla propuesta R = R1+R2 fabricaria precision (test
    test_mul_spec_check lo demuestra); se implementa la verdad
    interval-aritmetica, R_efectivo ~ min en precision relativa.
  - Division: divisor cuyo intervalo contiene 0 -> TOP(R) (pantalla
    completa, ignorancia maxima; no un error). [El spec decia
    "dividendo"; el caso patologico es el divisor: 0/x = 0 ordinario.]
  - Infinito RELATIVO al grado: fuera de pantalla en R1 puede ser
    numero ordinario en R2>R1. INF(R1) comparado con y solo es
    decidible si |y| cabe en la pantalla de R1 (|y| < 2^R1).
  - Refinamiento monotono: los intervalos solo se anidan; el render
    nunca se retracta (como el crecimiento del causal set).
  - Tiempo = R: el reloj global es el dia de Conway; Day(n) se
    construye por PUNTOS MEDIOS del dia n-1 (no por enumeracion de
    cortes; el bug 1/3 del script 21 queda estructuralmente excluido).

Casos especiales por grado (IEEE 1788-like): +INF_R, -INF_R (fuera de
pantalla) y TOP_R (toda la pantalla).
"""

from fractions import Fraction
from math import inf, log2

FIN, PINF, NINF, TOP = "fin", "+inf", "-inf", "top"


class NR:
    __slots__ = ("kind", "lo", "hi", "R")

    def __init__(self, kind, lo=None, hi=None, R=None):
        self.kind, self.lo, self.hi, self.R = kind, lo, hi, R

    # ---------- constructores ----------
    @classmethod
    def measure(cls, value, R):
        """Medicion a resolucion R: intervalo de ancho 2^-R centrado
        en el diadico de grado R mas cercano a value."""
        q = Fraction(value).limit_denominator(10**12)
        step = Fraction(1, 2 ** R)
        m = Fraction(round(q / step), 1) * step
        x = cls(FIN, m - step / 2, m + step / 2)
        return x._check_screen(R)

    @classmethod
    def exact(cls, value):
        """Capa vectorial: racional exacto (ancho 0, R = inf)."""
        q = Fraction(value)
        return cls(FIN, q, q)

    @classmethod
    def interval(cls, lo, hi):
        assert lo <= hi
        return cls(FIN, Fraction(lo), Fraction(hi))

    @classmethod
    def pos_inf(cls, R):
        return cls(PINF, R=R)

    @classmethod
    def neg_inf(cls, R):
        return cls(NINF, R=R)

    @classmethod
    def top(cls, R):
        return cls(TOP, R=R)

    # ---------- propiedades ----------
    def width(self):
        return self.hi - self.lo if self.kind == FIN else None

    def grade(self):
        """R efectivo = -log2(ancho); inf para exactos."""
        if self.kind != FIN:
            return self.R
        w = self.width()
        return inf if w == 0 else -log2(float(w))

    def mantissa(self):
        """Representante mas simple del intervalo (cumpleanos minimo:
        el diadico con menor denominador 2^k dentro de [lo, hi])."""
        if self.kind != FIN:
            return self.kind
        if self.lo == self.hi:
            return self.lo
        k = 0
        while True:
            step = Fraction(1, 2 ** k)
            n_lo = -(-self.lo / step)      # ceil
            n_lo = Fraction(n_lo).__ceil__()
            cand = Fraction(n_lo, 1) * step
            if cand <= self.hi:
                return cand
            k += 1

    def _check_screen(self, R):
        """Fuera de pantalla en grado R: |x| >= 2^R -> INF relativo."""
        bound = Fraction(2 ** R)
        if self.kind == FIN:
            if self.lo >= bound:
                return NR.pos_inf(R)
            if self.hi <= -bound:
                return NR.neg_inf(R)
        return self

    def __repr__(self):
        if self.kind == FIN:
            g = self.grade()
            gs = "inf" if g == inf else f"{g:.1f}"
            return f"NR({self.mantissa()}, R={gs})"
        return f"NR({self.kind}, R={self.R})"

    # ---------- aritmetica (propagacion exacta de intervalos) ----------
    def _grade_int(self):
        g = self.grade()
        return g if g is not None else 0

    def __add__(self, o):
        ks = {self.kind, o.kind}
        if TOP in ks:
            return NR.top(min(x.R for x in (self, o) if x.kind == TOP))
        if PINF in ks and NINF in ks:
            return NR.top(min(self.R or inf, o.R or inf))
        for x, y in ((self, o), (o, self)):
            if x.kind in (PINF, NINF) and y.kind == FIN:
                return NR(x.kind, R=x.R)  # absorbente en su grado
        if self.kind == PINF:
            return NR.pos_inf(min(self.R, o.R))
        if self.kind == NINF:
            return NR.neg_inf(min(self.R, o.R))
        return NR(FIN, self.lo + o.lo, self.hi + o.hi)

    def __neg__(self):
        if self.kind == FIN:
            return NR(FIN, -self.hi, -self.lo)
        if self.kind == PINF:
            return NR.neg_inf(self.R)
        if self.kind == NINF:
            return NR.pos_inf(self.R)
        return self

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        if TOP in (self.kind, o.kind):
            return NR.top(min(x.R for x in (self, o) if x.kind == TOP))
        if self.kind != FIN or o.kind != FIN:
            # inf * intervalo que contiene 0 -> TOP; sino inf con signo
            fin = o if self.kind != FIN else self
            infx = self if self.kind != FIN else o
            if fin.kind == FIN and fin.lo <= 0 <= fin.hi:
                return NR.top(infx.R)
            sign = 1 if (infx.kind == PINF) == (fin.lo > 0) else -1
            return NR.pos_inf(infx.R) if sign > 0 else NR.neg_inf(infx.R)
        ps = [self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi]
        return NR(FIN, min(ps), max(ps))

    def __truediv__(self, o):
        if o.kind == FIN and o.lo <= 0 <= o.hi and o.lo != o.hi:
            # divisor indistinguible de cero -> pantalla completa
            return NR.top(round(min(self._grade_int(), o._grade_int())))
        if o.kind == FIN and o.lo == o.hi == 0:
            return NR.top(round(self._grade_int()))
        if o.kind == FIN:
            inv = NR(FIN, min(1 / o.lo, 1 / o.hi), max(1 / o.lo, 1 / o.hi))
            return self * inv
        # dividir por infinito -> cero del grado del infinito
        step = Fraction(1, 2 ** o.R)
        return NR(FIN, -step / 2, step / 2)

    # ---------- comparacion (decidible o no) ----------
    def cmp(self, o):
        """'<', '>', '=', o None si indistinguibles a la resolucion comun."""
        if TOP in (self.kind, o.kind):
            return None
        if self.kind in (PINF, NINF) and o.kind == FIN:
            bound = Fraction(2 ** self.R)
            if max(abs(o.lo), abs(o.hi)) < bound:   # y cabe en pantalla R1
                return ">" if self.kind == PINF else "<"
            return None                              # indistinguibles en R1
        if o.kind in (PINF, NINF):
            r = o.cmp(self)
            return None if r is None else ("<" if r == ">" else ">")
        if self.hi < o.lo:
            return "<"
        if self.lo > o.hi:
            return ">"
        if self.lo == o.lo and self.hi == o.hi and self.lo == self.hi:
            return "="
        return None

    def refine_with(self, other):
        """Interseccion (nueva medicion del mismo objeto): solo anida."""
        assert self.kind == FIN and other.kind == FIN
        lo, hi = max(self.lo, other.lo), min(self.hi, other.hi)
        assert lo <= hi, "mediciones incompatibles: el render no se retracta"
        return NR(FIN, lo, hi)


# ---------- dias de Conway por puntos medios ----------
def conway_day(n):
    """Dia n: dia(n-1) + puntos medios adyacentes + extremos +-(max+1).
    Estructuralmente imposible generar 1/3 (solo diadicos)."""
    nums = [Fraction(0)]
    for _ in range(n):
        new = [nums[0] - 1]
        for a, b in zip(nums, nums[1:]):
            new.append((a + b) / 2)
        new.append(nums[-1] + 1)
        nums = sorted(set(nums) | set(new))
    return nums


# ============================ TESTS ============================
if __name__ == "__main__":
    ok = lambda c, msg: print(("  [OK] " if c else "  [FALLA] ") + msg)
    print("=" * 64)
    print("21b: N_R - tests")
    print("=" * 64)

    print("\n1. Dias de Conway (puntos medios)")
    for n in range(9):
        d = conway_day(n)
        assert len(d) == 2 ** (n + 1) - 1
    ok(True, "conteo 2^(n+1)-1 verificado, dias 0..8")
    third = Fraction(1, 3)
    ok(all(third not in conway_day(n) for n in range(9)),
       "1/3 NO aparece en ningun dia finito (bug del script 21 excluido)")
    ok(Fraction(3, 8) not in conway_day(3) and Fraction(3, 8) in conway_day(4),
       "3/8 nace exactamente el dia 4 (punto medio de 1/4 y 1/2)")

    print("\n2. Ley del minimo (suma)")
    x = NR.measure(1.0, 3)          # 1 +- 2^-4
    y = NR.measure(1.0, 10)         # 1 +- 2^-11
    s = x + y
    ok(abs(s.grade() - 3) < 1.2, f"grado(x3 + y10) = {s.grade():.2f} ~ min=3")

    print("\n3. NOTA DE SPEC: multiplicacion R1+R2 fabricaria precision")
    p = x * x                        # x = 1 +- 2^-4, R=3
    ok(abs(p.grade() - 2) < 1.2,
       f"grado(x3 * x3) = {p.grade():.2f} ~ 2 (NO 6=R1+R2): "
       f"ancho real {float(p.width()):.4f} vs 2^-6={2**-6:.4f}")

    print("\n4. Division")
    z = NR.measure(0.0, 4)           # cero raster: intervalo que contiene 0
    t = NR.measure(1.0, 8) / z
    ok(t.kind == TOP, f"1 / (0 raster) = {t!r} (TOP, no error)")
    q = NR.exact(1) / NR.exact(3)
    ok(q.lo == Fraction(1, 3), "capa vectorial: 1/3 exacto via NR.exact")

    print("\n5. Infinito relativo al grado")
    big = NR.measure(10.0, 3)        # 10 > 2^3: fuera de pantalla en R=3
    ok(big.kind == PINF and big.R == 3, f"10 medido en R=3 -> {big!r}")
    small = NR.measure(2.0, 10)
    ok(big.cmp(small) == ">", "INF_3 > 2 (2 cabe en pantalla de R=3)")
    huge = NR.measure(500.0, 10)     # 500 no cabe en pantalla de R=3
    ok(big.cmp(huge) is None,
       "INF_3 vs 500_10: indistinguibles en R=3 (re-medir, no operar)")
    ok((big + small).kind == PINF, "INF absorbente en su grado")
    ok((big + NR.neg_inf(5)).kind == TOP, "(+INF) + (-INF) = TOP")

    print("\n6. Refinamiento monotono (el render no se retracta)")
    a = NR.measure(3.14, 4)
    b = NR.measure(3.141593, 12)
    r = a.refine_with(b)
    ok(r.width() <= b.width() and r.lo >= a.lo and r.hi <= a.hi,
       "nuevas mediciones solo anidan el intervalo")

    print("\n7. Mantisa = representante mas simple (cumpleanos minimo)")
    m = NR.interval(Fraction(3, 10), Fraction(2, 5)).mantissa()
    ok(m == Fraction(3, 8), f"simplest en (0.3, 0.4) = {m} (diadico, NO 1/3)")

    print("\nDONE")
