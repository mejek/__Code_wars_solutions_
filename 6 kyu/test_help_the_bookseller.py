from help_the_bookseller import stock_list

def test_if_return_empty_string_if_no_cats_in_categories():
    arts = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    cat = []
    assert stock_list(arts, cat) == ''

def test_if_return_empty_string_if_no_arts_in_articles():
    arts = []
    cat = ['I']
    assert stock_list(arts, cat) == ''

def test_help_the_bookseller_1():
    arts = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    cat = ["A", "B", "C", "D"]
    assert stock_list(arts, cat) == "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"

def test_help_the_bookseller_2():
    arts = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    cat = ["A", "B"]
    assert stock_list(arts, cat) == "(A : 200) - (B : 1140)"