from math import gcd as math_gcd

import pytest

from zkmath.numtheory import mod_inverse


def test_known_values():
    assert mod_inverse(5, 17) == 7
    assert mod_inverse(3, 11) == 4
    assert mod_inverse(7, 40) == 23


def test_inverse_multiplies_to_one():
    for n in range(2, 60):
        for a in range(1, n):
            if math_gcd(a, n) == 1:
                x = mod_inverse(a, n)
                assert 0 <= x < n
                assert (a * x) % n == 1


def test_matches_python_builtin():
    # Python has its own: pow(a, -1, n)
    for n in range(2, 60):
        for a in range(1, n):
            if math_gcd(a, n) == 1:
                assert mod_inverse(a, n) == pow(a, -1, n)


def test_no_inverse_when_not_coprime():
    with pytest.raises(ValueError):
        mod_inverse(4, 12)
    with pytest.raises(ValueError):
        mod_inverse(6, 9)


def test_every_nonzero_has_inverse_mod_prime():
    for p in [2, 3, 5, 7, 11, 13, 101]:
        for a in range(1, p):
            assert (a * mod_inverse(a, p)) % p == 1