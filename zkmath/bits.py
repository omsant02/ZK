"""8-bit shift and rotate helpers (Part 0.4)."""

WIDTH = 8
MASK = (1 << WIDTH) - 1  # 0b11111111 = 255


def shl8(x, n):
    """Shift x left by n bits, dropping any bits that overflow past 8."""
    return (x << n) & MASK


def shr8(x, n):
    """Shift x right by n bits."""
    return x >> n


def rotl8(x, n):
    """Rotate x left by n bits: bits that fall off the left reappear on the right."""
    return ((x << n) | (x >> (WIDTH - n))) & MASK


def rotr8(x, n):
    """Rotate x right by n bits: bits that fall off the right reappear on the left."""
    return ((x >> n) | (x << (WIDTH - n))) & MASK