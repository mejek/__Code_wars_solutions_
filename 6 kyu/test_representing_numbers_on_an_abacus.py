from representing_numbers_on_an_abacus import read_abacus, create_abacus
import pytest

@pytest.fixture()
def c_abacus():
    data = [[3,'*********\n         \n---------\n        *\n*********\n*********\n******** \n*********'],
            [7,'******** \n        *\n---------\n        *\n*********\n******** \n*********\n*********'],
            [11,'*********\n         \n---------\n       **\n*******  \n*********\n*********\n*********'],
            [1703, '****** **\n      *  \n---------\n     ** *\n***** ***\n****** **\n******** \n*********']
            ]
    return data

@pytest.fixture()
def r_abacus():
    data = [['*********\n         \n---------\n        *\n*********\n*********\n******** \n*********', 3],
            ['******** \n        *\n---------\n        *\n*********\n******** \n*********\n*********', 7],
            ['*********\n         \n---------\n       **\n*******  \n*********\n*********\n*********', 11],
            ['****** **\n      *  \n---------\n     ** *\n***** ***\n****** **\n******** \n*********', 1703]
            ]
    return data


def test_create_abacus(c_abacus):
    for i in c_abacus:
        assert create_abacus(i[0]) == i[1]

def test_read_abacus(r_abacus):
    for i in r_abacus:
        assert read_abacus(i[0]) == i[1]

