from next_featured_number_higher_than_a_given_value import next_numb

def test_next_numb_1():
    assert next_numb(12) == 15

def test_next_numb_2():
    assert next_numb(13) == 15

def test_next_numb_3():
    assert next_numb(99) == 105

def test_next_numb_4():
    assert next_numb(999999) == 1023459

def test_next_numb_5():
    assert next_numb(9999999999) == "There is no possible number that fulfills those requirements"