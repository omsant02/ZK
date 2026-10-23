"""Tests for zkmath.numtheory."""

import math
import pytest
from zkmath.numtheory import gcd, power


def test_gcd_known_values():
    assert gcd(12, 18) == 6
    assert gcd(252, 105) == 21
    assert gcd(1071, 462) == 21
    assert gcd(48, 18) == 6
    assert gcd(17, 5) == 1
    assert gcd(100, 75) == 25


def test_gcd_with_zero():
    assert gcd(9, 0) == 9
    assert gcd(0, 9) == 9


def test_gcd_order_does_not_matter():
    assert gcd(18, 48) == gcd(48, 18)


def test_gcd_matches_python_math_gcd():
    for a in range(0, 200):
        for b in range(0, 200):
            assert gcd(a, b) == math.gcd(a, b)




def test_power_known_values():
    assert power(3, 13) == 1594323
    assert power(2, 10) == 1024
    assert power(5, 6) == 15625
    assert power(7, 1) == 7


def test_power_zero_exponent():
    assert power(5, 0) == 1
    assert power(0, 0) == 1  # Python's convention: 0**0 == 1


def test_power_matches_builtin():
    for a in range(0, 20):
        for n in range(0, 40):
            assert power(a, n) == a ** n


def test_power_exponent_addition_rule():
    # a^(m+n) = a^m * a^n
    for m in range(0, 15):
        for n in range(0, 15):
            assert power(3, m + n) == power(3, m) * power(3, n)


def test_power_negative_exponent_rejected():
    with pytest.raises(ValueError):
        power(2, -1)