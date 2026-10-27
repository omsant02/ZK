from math import gcd as math_gcd

from zkmath.numtheory import extended_gcd


def test_known_values():
    assert extended_gcd(252, 105) == (21, -2, 5)
    assert extended_gcd(17, 5) == (1, -2, 7)
    assert extended_gcd(240, 46) == (2, -9, 47)


def test_zero_cases():
    assert extended_gcd(5, 0) == (5, 1, 0)
    assert extended_gcd(0, 5) == (5, 0, 1)


def test_bezout_identity_holds():
    # a*x + b*y == g for every small pair
    for a in range(0, 60):
        for b in range(0, 60):
            g, x, y = extended_gcd(a, b)
            assert a * x + b * y == g


def test_g_is_the_gcd():
    for a in range(0, 60):
        for b in range(0, 60):
            g, _, _ = extended_gcd(a, b)
            assert g == math_gcd(a, b)