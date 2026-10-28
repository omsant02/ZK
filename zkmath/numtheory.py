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




def extended_gcd(a, b):
    """Return (g, x, y) with g = gcd(a, b) and a*x + b*y == g.

    a and b must be non-negative integers.
    """
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    return old_r, old_x, old_y




def mod_inverse(a, n):
    """Return x in range(n) with (a * x) % n == 1.

    Raises ValueError if a has no inverse modulo n (gcd(a, n) != 1).
    """
    if n < 2:
        raise ValueError("modulus must be at least 2")
    g, x, _ = extended_gcd(a % n, n)
    if g != 1:
        raise ValueError(f"{a} has no inverse modulo {n}")
    return x % n



def mod_pow(a, n, m):
    """Compute (a ** n) % m by square-and-multiply, reducing mod m at every step.

    n must be non-negative and m must be positive.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if m < 1:
        raise ValueError("modulus must be positive")
    result = 1 % m
    base = a % m
    while n > 0:
        if n & 1:
            result = (result * base) % m
        base = (base * base) % m
        n >>= 1
    return result