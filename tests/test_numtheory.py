"""Tests for zkmath.numtheory."""

import math

from zkmath.numtheory import gcd


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