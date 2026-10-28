from math import gcd as math_gcd

import pytest

from zkmath.numtheory import mod_inverse, mod_pow


def test_known_values():
    assert mod_pow(3, 13, 7) == 3
    assert mod_pow(2, 10, 11) == 1
    assert mod_pow(2, 10, 1000) == 24
    assert mod_pow(5, 4, 12) == 1  # Euler: phi(12) = 4


def test_matches_python_builtin():
    for m in range(1, 30):
        for a in range(0, 30):
            for n in range(0, 30):
                assert mod_pow(a, n, m) == pow(a, n, m)


def test_huge_exponent_is_fast():
    # an exponent of about 77 digits: only ~256 rounds are needed
    big = 2 ** 256
    p = 10 ** 9 + 7
    assert mod_pow(2, big, p) == pow(2, big, p)


def test_fermat_little_theorem():
    for p in [2, 3, 5, 7, 11, 13, 101]:
        for a in range(1, p):
            assert mod_pow(a, p - 1, p) == 1


def test_inverse_from_fermat_matches_extended_euclid():
    for p in [3, 5, 7, 11, 13, 101]:
        for a in range(1, p):
            assert mod_pow(a, p - 2, p) == mod_inverse(a, p)


def test_euler_theorem_small_cases():
    # phi(10) = 4, phi(15) = 8, phi(21) = 12
    for n, phi in [(10, 4), (15, 8), (21, 12)]:
        for a in range(1, n):
            if math_gcd(a, n) == 1:
                assert mod_pow(a, phi, n) == 1


def test_bad_arguments_rejected():
    with pytest.raises(ValueError):
        mod_pow(2, -1, 7)
    with pytest.raises(ValueError):
        mod_pow(2, 3, 0)