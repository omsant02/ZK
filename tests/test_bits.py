"""Tests for zkmath.bits (Part 0.4)."""

from zkmath.bits import shl8, shr8, rotl8, rotr8


def test_shl8_drops_overflow_bits():
    assert shl8(0b10010110, 3) == 0b10110000
    assert shl8(0b01101001, 2) == 0b10100100


def test_shr8_drops_low_bits():
    assert shr8(0b01101001, 3) == 0b00001101


def test_rotl8_known_values():
    assert rotl8(0b10010110, 3) == 0b10110100
    assert rotl8(0b01101001, 2) == 0b10100101


def test_rotr8_known_values():
    assert rotr8(0b00101101, 2) == 0b01001011


def test_rotation_by_zero_or_full_width_is_identity():
    for x in range(256):
        assert rotl8(x, 0) == x
        assert rotl8(x, 8) == x
        assert rotr8(x, 0) == x
        assert rotr8(x, 8) == x


def test_rotr8_undoes_rotl8():
    for x in range(256):
        for n in range(9):
            assert rotr8(rotl8(x, n), n) == x


def test_rotl_equals_rotr_by_complement():
    for x in range(256):
        for n in range(9):
            assert rotl8(x, n) == rotr8(x, 8 - n)


def test_results_stay_within_8_bits():
    for x in range(256):
        for n in range(9):
            assert 0 <= shl8(x, n) <= 255
            assert 0 <= shr8(x, n) <= 255
            assert 0 <= rotl8(x, n) <= 255
            assert 0 <= rotr8(x, n) <= 255

def test_shr8_matches_floor_division():
    for x in range(256):
        for n in range(9):
            assert shr8(x, n) == x // (2 ** n)