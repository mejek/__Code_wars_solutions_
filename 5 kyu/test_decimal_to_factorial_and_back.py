from decimal_to_factorial_and_back import dec_2_fact_string, fact_string_2_dec

def test_dec_2_factt_string_1():
    assert dec_2_fact_string(463) == '341010'

def test_dec_2_factt_string_2():
    assert dec_2_fact_string(2982) == '4041000'

def test_dec_2_factt_string_3():
    assert dec_2_fact_string(36288000) == 'A0000000000'

def test_fact_string_2_dec_1():
    assert fact_string_2_dec('341010') == 463

def test_fact_string_2_dec_2():
    assert fact_string_2_dec('4041000') == 2982

def test_fact_string_2_dec_3():
    assert fact_string_2_dec('A0000000000') == 36288000
