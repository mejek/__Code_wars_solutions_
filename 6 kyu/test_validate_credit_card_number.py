from validate_credit_card_number import validate, sum_of_digits
import pytest
a = 1714
b = 12345
c = 891

@pytest.fixture
def input_output():
    in_out = [
        (1714, False),
        (12345, False),
        (891, False),
        (123, False),
        (1, False),
        (2121, True),
        (1230, True)]
    return in_out

# def test_return_list_with_double_every_other_digit_even():
#     assert validate(a) == [2, 7, 2, 4]
#
# def test_return_list_with_double_every_other_digit_odd():
#     assert validate(b) == [1, 4, 3, 8, 5]

def test_sum_of_digits():
    assert sum_of_digits(16) == 7

# def test_return_sibgle_digit_if_double_has_two_digits():
#     assert validate(c) == [8, 9, 1]

def test_validate(input_output):
    for in_out in input_output:
        assert validate(in_out[0]) == in_out[1]