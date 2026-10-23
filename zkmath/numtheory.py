"""Number theory helpers (Part 0.5, extended in Part 2)."""


def gcd(a, b):
    """Greatest common divisor of two non-negative integers (Euclid's algorithm)."""
    while b != 0:
        a, b = b, a % b
    return a





def power(a, n):
    """Compute a**n by square-and-multiply, for integer n >= 0."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    base = a
    while n > 0:
        if n & 1:          # lowest binary digit of n is 1
            result *= base
        base *= base       # a -> a^2 -> a^4 -> a^8 ...
        n >>= 1            # drop the digit we just used
    return result