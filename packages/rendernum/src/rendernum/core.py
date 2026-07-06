"""Core finite-resolution arithmetic.

A finite value at grade R is a dyadic interval. Exact rationals are represented
as zero-width intervals. The implementation follows the 21b experiment:
interval arithmetic is the source of truth, and special values are relative to
the grade.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import inf, log2
from typing import Optional, Union

NumberLike = Union[int, float, Fraction, "RenderNum"]

FIN = "fin"
PINF = "+inf"
NINF = "-inf"
TOP = "top"


def _as_fraction(value: Union[int, float, Fraction]) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, float):
        return Fraction(value).limit_denominator(10**12)
    return Fraction(value)


def _coerce(value: NumberLike) -> "RenderNum":
    return value if isinstance(value, RenderNum) else exact(value)


@dataclass(frozen=True)
class RenderNum:
    """Finite-resolution number or relative special value."""

    kind: str
    lo: Optional[Fraction] = None
    hi: Optional[Fraction] = None
    R: Optional[int] = None

    @classmethod
    def measure(cls, value: Union[int, float, Fraction], R: int) -> "RenderNum":
        """Measure ``value`` at grade ``R`` with interval width ``2^-R``."""
        q = _as_fraction(value)
        step = Fraction(1, 2**R)
        m = Fraction(round(q / step), 1) * step
        return cls(FIN, m - step / 2, m + step / 2)._check_screen(R)

    @classmethod
    def exact(cls, value: Union[int, float, Fraction]) -> "RenderNum":
        """Exact rational in the vector layer."""
        q = _as_fraction(value)
        return cls(FIN, q, q)

    @classmethod
    def interval(cls, lo: Union[int, float, Fraction],
                 hi: Union[int, float, Fraction]) -> "RenderNum":
        lo_q, hi_q = _as_fraction(lo), _as_fraction(hi)
        if lo_q > hi_q:
            raise ValueError("lo must be <= hi")
        return cls(FIN, lo_q, hi_q)

    @classmethod
    def pos_inf(cls, R: int) -> "RenderNum":
        return cls(PINF, R=R)

    @classmethod
    def neg_inf(cls, R: int) -> "RenderNum":
        return cls(NINF, R=R)

    @classmethod
    def top(cls, R: int) -> "RenderNum":
        return cls(TOP, R=R)

    def width(self) -> Optional[Fraction]:
        return self.hi - self.lo if self.kind == FIN else None

    def grade(self) -> Union[float, int, None]:
        if self.kind != FIN:
            return self.R
        w = self.width()
        return inf if w == 0 else -log2(float(w))

    def mantissa(self) -> Union[Fraction, str]:
        """Simplest dyadic representative inside the interval."""
        if self.kind != FIN:
            return self.kind
        if self.lo == self.hi:
            return self.lo
        k = 0
        while True:
            step = Fraction(1, 2**k)
            n_lo = Fraction(self.lo / step).__ceil__()
            cand = Fraction(n_lo, 1) * step
            if cand <= self.hi:
                return cand
            k += 1

    def _check_screen(self, R: int) -> "RenderNum":
        bound = Fraction(2**R)
        if self.kind == FIN:
            if self.lo >= bound:
                return RenderNum.pos_inf(R)
            if self.hi <= -bound:
                return RenderNum.neg_inf(R)
        return self

    def _grade_int(self) -> int:
        g = self.grade()
        if g in (None, inf):
            return 0
        return round(g)

    def __repr__(self) -> str:
        if self.kind == FIN:
            g = self.grade()
            gs = "inf" if g == inf else f"{g:.1f}"
            return f"RenderNum({self.mantissa()}, R={gs})"
        return f"RenderNum({self.kind}, R={self.R})"

    def __add__(self, other: NumberLike) -> "RenderNum":
        o = _coerce(other)
        kinds = {self.kind, o.kind}
        if TOP in kinds:
            grades = [x.R for x in (self, o) if x.kind == TOP]
            return RenderNum.top(min(grades))
        if PINF in kinds and NINF in kinds:
            return RenderNum.top(min(self.R or 0, o.R or 0))
        for x, y in ((self, o), (o, self)):
            if x.kind in (PINF, NINF) and y.kind == FIN:
                return RenderNum(x.kind, R=x.R)
        if self.kind == PINF:
            return RenderNum.pos_inf(min(self.R, o.R))
        if self.kind == NINF:
            return RenderNum.neg_inf(min(self.R, o.R))
        return RenderNum(FIN, self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self) -> "RenderNum":
        if self.kind == FIN:
            return RenderNum(FIN, -self.hi, -self.lo)
        if self.kind == PINF:
            return RenderNum.neg_inf(self.R)
        if self.kind == NINF:
            return RenderNum.pos_inf(self.R)
        return self

    def __sub__(self, other: NumberLike) -> "RenderNum":
        return self + (-_coerce(other))

    def __rsub__(self, other: NumberLike) -> "RenderNum":
        return _coerce(other) - self

    def __mul__(self, other: NumberLike) -> "RenderNum":
        o = _coerce(other)
        if TOP in (self.kind, o.kind):
            grades = [x.R for x in (self, o) if x.kind == TOP]
            return RenderNum.top(min(grades))
        if self.kind != FIN or o.kind != FIN:
            fin = o if self.kind != FIN else self
            infx = self if self.kind != FIN else o
            if fin.kind == FIN and fin.lo <= 0 <= fin.hi:
                return RenderNum.top(infx.R)
            sign = 1 if (infx.kind == PINF) == (fin.lo > 0) else -1
            return RenderNum.pos_inf(infx.R) if sign > 0 else RenderNum.neg_inf(infx.R)
        products = [self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi]
        return RenderNum(FIN, min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other: NumberLike) -> "RenderNum":
        o = _coerce(other)
        if o.kind == FIN and o.lo <= 0 <= o.hi and o.lo != o.hi:
            return RenderNum.top(round(min(self._grade_int(), o._grade_int())))
        if o.kind == FIN and o.lo == o.hi == 0:
            return RenderNum.top(round(self._grade_int()))
        if o.kind == FIN:
            inv = RenderNum(FIN, min(1 / o.lo, 1 / o.hi), max(1 / o.lo, 1 / o.hi))
            return self * inv
        step = Fraction(1, 2**o.R)
        return RenderNum(FIN, -step / 2, step / 2)

    def __rtruediv__(self, other: NumberLike) -> "RenderNum":
        return _coerce(other) / self

    def cmp(self, other: NumberLike) -> Optional[str]:
        """Return '<', '>', '=', or None if undecidable at the common grade."""
        o = _coerce(other)
        if TOP in (self.kind, o.kind):
            return None
        if self.kind in (PINF, NINF) and o.kind == FIN:
            bound = Fraction(2**self.R)
            if max(abs(o.lo), abs(o.hi)) < bound:
                return ">" if self.kind == PINF else "<"
            return None
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

    def refine_with(self, other: NumberLike) -> "RenderNum":
        o = _coerce(other)
        if self.kind != FIN or o.kind != FIN:
            raise ValueError("only finite intervals can be refined")
        lo, hi = max(self.lo, o.lo), min(self.hi, o.hi)
        if lo > hi:
            raise ValueError("incompatible measurements: the render cannot retract")
        return RenderNum(FIN, lo, hi)


def from_float(value: float, R: int) -> RenderNum:
    return RenderNum.measure(value, R)


def from_fraction(numerator: int, denominator: int = 1) -> RenderNum:
    return RenderNum.exact(Fraction(numerator, denominator))


def exact(value: Union[int, float, Fraction]) -> RenderNum:
    return RenderNum.exact(value)


def interval(lo: Union[int, float, Fraction],
             hi: Union[int, float, Fraction]) -> RenderNum:
    return RenderNum.interval(lo, hi)


def pos_inf(R: int) -> RenderNum:
    return RenderNum.pos_inf(R)


def neg_inf(R: int) -> RenderNum:
    return RenderNum.neg_inf(R)


def top(R: int) -> RenderNum:
    return RenderNum.top(R)


def conway_day(n: int) -> list[Fraction]:
    """Conway day n by adjacent dyadic midpoints."""
    nums = [Fraction(0)]
    for _ in range(n):
        new = [nums[0] - 1]
        for a, b in zip(nums, nums[1:]):
            new.append((a + b) / 2)
        new.append(nums[-1] + 1)
        nums = sorted(set(nums) | set(new))
    return nums

