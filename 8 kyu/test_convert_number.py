from convert_number import digitize

def test_check_if_result_is_list():
    assert isinstance(digitize('123'), list)

def test_digitalize():
    assert digitize('123') == [3, 2, 1]