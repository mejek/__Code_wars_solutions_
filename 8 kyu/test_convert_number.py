from convert_number import digitize
import pytest

@pytest.fixture()
def input_string():
    return '123'

def test_check_if_result_is_list(input_string):
    assert isinstance(digitize(input_string), list)

def test_digitalize(input_string):
    assert digitize(input_string) == [3, 2, 1]