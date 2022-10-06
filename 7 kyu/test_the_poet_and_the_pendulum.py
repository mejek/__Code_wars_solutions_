import pytest
from the_poet_and_the_pendulum import pendulum


input_expected = [([4, 6, 8, 7, 5], [8, 6 , 4, 5, 7]),
                 ([-9, -2, -10, -6], [-6, -10, -9, -2]),
                 ([19,30,16,19,28,26,28,17,21,17], [28,26,19,17,16,17,19,21,28,30])
                 ]

@pytest.mark.parametrize("test_input, expected", input_expected)
def test_pendulum(test_input, expected):
    assert pendulum(test_input) == expected