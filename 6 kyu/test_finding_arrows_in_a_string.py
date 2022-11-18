from finding_arrows_in_a_string import arrow_search

def test_01():
    assert arrow_search('>.') == 1

def test_06():
    assert arrow_search('<--..') == -3

def test_02():
    assert arrow_search('><=><--') == -2

def test_03():
    assert arrow_search('>===>->') == 11

def test_04():
    assert arrow_search('......') == 0

def test_05():
    assert arrow_search('>>><.=<=<..=<>') == -3