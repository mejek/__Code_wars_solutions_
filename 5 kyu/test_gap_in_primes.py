from gap_in_primes import gap
import pytest

input_expected = [(2,100,110, [101, 103]),
                (4,100,110, [103, 107]),
                (6,100,110, None),
                (8,300,400, [359, 367]),
                (10,300,400, [337, 347]),
                (2,100,103, [101, 103])
                ]

@pytest.mark.parametrize("g, min, max, expected", input_expected)
def test_gap(g, min, max, expected):
    assert gap(g, min, max) == expected