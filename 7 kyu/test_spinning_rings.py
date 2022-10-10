from spinning_rings import spinning_rings
import pytest

@pytest.fixture()
def input_expected():
    data = [{'input': [2,3], 'expected': 5},
            {'input': [3,2], 'expected': 2},
            {'input': [1,1], 'expected': 1},
            {'input': [2,2], 'expected': 3},
            {'input': [3,3], 'expected': 2}
            ]
    return data

def test_spinning_rings(input_expected):
    for case in input_expected:
        assert spinning_rings(case['input'][0], case['input'][1]) == case['expected']
