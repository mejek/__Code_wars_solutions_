from duplicates_duplicates_everywhere import remove_duplicate_ids


a = {
    "1": ["A", "B", "C"],
    "2": ["A", "B", "D", "A"],
}
res_a = {
    "1": ["C"],
    "2": ["A", "B", "D"]
}
def test_a():
    assert remove_duplicate_ids(a) == res_a

b = {
    "1": ["C", "F", "G"],
    "2": ["A", "B", "C"],
    "3": ["A", "B", "D"],
}
res_b = {
    "1": ["F", "G"],
    "2": ["C"],
    "3": ["A", "B", "D"]
}
def test_b():
    assert remove_duplicate_ids(b) == res_b

c = {
    "1": ["A"],
    "2": ["A"],
    "3": ["A"],
}
res_c = {
    "1": [],
    "2": [],
    "3": ["A"]
}
def test_c():
    assert remove_duplicate_ids(c) == res_c

d = {
    "432": ["A", "A", "B", "D"],
    "53": ["L", "G", "B", "C"],
    "236": ["L", "A", "X", "G", "H", "X"],
    "11": ["P", "R", "S", "D"],
}
res_d = {
    "11": ["P", "R", "S"],
    "53": ["C"],
    "236": ["L", "X", "G", "H"],
    "432": ["A", "B", "D"]
}
def test_d():
    assert remove_duplicate_ids(d) == res_d