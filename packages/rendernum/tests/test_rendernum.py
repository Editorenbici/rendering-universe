from fractions import Fraction
from math import inf

from rendernum import FIN, PINF, TOP, NR, conway_day, exact, from_float, from_fraction, interval, neg_inf


def test_conway_day_counts_and_no_third():
    for n in range(9):
        assert len(conway_day(n)) == 2 ** (n + 1) - 1
    assert all(Fraction(1, 3) not in conway_day(n) for n in range(9))
    assert Fraction(3, 8) not in conway_day(3)
    assert Fraction(3, 8) in conway_day(4)


def test_sum_law_of_minimum():
    x = from_float(1.0, 3)
    y = from_float(1.0, 10)
    s = x + y
    assert abs(s.grade() - 3) < 1.2


def test_multiplication_does_not_fabricate_precision():
    x = from_float(1.0, 3)
    p = x * x
    assert abs(p.grade() - 2) < 1.2
    assert float(p.width()) > 2 ** -6


def test_division_by_unresolved_zero_returns_top():
    z = from_float(0.0, 4)
    t = from_float(1.0, 8) / z
    assert t.kind == TOP


def test_from_fraction_is_exact():
    q = from_fraction(1, 3)
    assert q.kind == FIN
    assert q.lo == Fraction(1, 3)
    assert q.hi == Fraction(1, 3)
    assert q.grade() == inf


def test_exact_division_keeps_one_third():
    q = exact(1) / exact(3)
    assert q.lo == Fraction(1, 3)


def test_infinity_relative_to_grade():
    big = from_float(10.0, 3)
    assert big.kind == PINF and big.R == 3
    assert big.cmp(from_float(2.0, 10)) == ">"
    assert big.cmp(from_float(500.0, 10)) is None


def test_infinity_absorbs_and_cancels_to_top():
    big = from_float(10.0, 3)
    assert (big + from_float(2.0, 10)).kind == PINF
    assert (big + neg_inf(5)).kind == TOP


def test_refinement_is_monotone():
    a = from_float(3.14, 4)
    b = from_float(3.141593, 12)
    r = a.refine_with(b)
    assert r.width() <= b.width()
    assert r.lo >= a.lo and r.hi <= a.hi


def test_refinement_rejects_incompatible_measurements():
    a = interval(0, 1)
    b = interval(2, 3)
    try:
        a.refine_with(b)
    except ValueError:
        pass
    else:
        raise AssertionError("expected incompatible measurements to fail")


def test_mantissa_is_simplest_dyadic():
    assert interval(Fraction(3, 10), Fraction(2, 5)).mantissa() == Fraction(3, 8)


def test_top_propagates_through_addition():
    assert (NR.top(4) + from_float(1.0, 8)).kind == TOP


def test_infinity_times_zero_interval_is_top():
    assert (from_float(10.0, 3) * from_float(0.0, 4)).kind == TOP


def test_exact_operator_coercion():
    x = from_fraction(1, 2)
    assert (x + 1).lo == Fraction(3, 2)
    assert (2 * x).lo == 1

