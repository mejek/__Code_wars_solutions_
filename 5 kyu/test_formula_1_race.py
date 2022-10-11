from formula_1_race import champion_rank

def test_basic():
    inp_exp = (((3, ""), 3),
               ((12, "4 O 3 O"), 12),
               ((10, "1 I 10 O 2 I"), 7))
    for test in inp_exp:
        assert champion_rank(test[0][0], test[0][1]) == test[1]

def test_out():
    assert champion_rank(17, "2 O 17 I") == -1

def test_winner():
    assert champion_rank(2, """9 O 17 O 9 O 12 O 2 O 12 O 9 O 1 O 5 O 12 O 17 O 20 O 16
                            O 7 O 2 O 8 O 16 O 14 O 3 O 14 O 11 O 16 O 1 O 13 O 8 O 14
                             O 5 O 12 O 4 O""") == 1
