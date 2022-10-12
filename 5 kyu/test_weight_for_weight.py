from weight_for_weight import order_weight
import pytest

@pytest.fixture()
def input_expected():
    d = [["103 123 4444 99 2000", "2000 103 123 4444 99"],
         ["2000 10003 1234000 44444444 9999 11 11 22 123", "11 11 2000 10003 22 123 1234000 44444444 9999"]]
    return d

def test_order_weight(input_expected):
    for d in input_expected:
        assert order_weight(d[0]) == d[1]






