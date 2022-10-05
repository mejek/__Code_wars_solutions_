import pytest
from categorize_new_member import open_or_senior

@pytest.fixture()
def input_list():
    return [[76, 3], [25, 2], [67, 20]] #except ['Open', 'Open', 'Senior']

def test_open_or_senior(input_list):
    assert open_or_senior(input_list) == ['Open', 'Open', 'Senior']
