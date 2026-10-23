"""Number theory helpers (Part 0.5, extended in Part 2)."""


def gcd(a, b):
    """Greatest common divisor of two non-negative integers (Euclid's algorithm)."""
    while b != 0:
        a, b = b, a % b
    return a