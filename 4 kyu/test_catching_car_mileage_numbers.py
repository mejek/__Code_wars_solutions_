from catching_car_mileage_numbers import is_interesting
import random

def test_boring_number():
    for n in range(random.randint(1,98)):
        assert is_interesting(n, []) == 0

def test_followed_by_all_zeros():
    numbers = [900, 100, 8000, 30000]
    for number in numbers:
        assert is_interesting(number, []) == 2

def test_return_1_followed_by_all_zeros_after_adding_1_or_2():
    numbers = [899, 7999, 299999]
    for number in numbers:
        assert is_interesting(number, []) == 1

def test_every_digit_is_the_same_number():
    numbers = [22222, 111, 444444, 999]
    for number in numbers:
        assert is_interesting(number, []) == 2

def test_return_1_every_digit_is_the_same_number_after_adding_1_or_2():
    numbers = [22221, 110, 444442, 77775, 99998, 9997]
    for number in numbers:
        assert is_interesting(number, []) == 1

def test_digits_are_sequential_incrementing():
    numbers = [1234, 4567, 7890]
    for number in numbers:
        assert is_interesting(number, []) == 2

def test_return_1_digits_are_sequential_incrementing_after_adding_1_or_2():
    numbers = [1232, 4566, 2344, 3456787, 67888, 67889]
    for number in numbers:
        assert is_interesting(number, []) == 1

def test_digits_are_sequential_decreasing():
    numbers = [4321, 876, 3210]
    for number in numbers:
        assert is_interesting(number, []) == 2

def test_return_1_digits_are_sequential_decreasing_after_adding_1_or_2():
    numbers = [4319, 4320, 875, 3209, 3208]
    for number in numbers:
        assert is_interesting(number, []) == 1

def test_all_digits_are_palindrome():
    numbers = [1221, 73837, 896698, 11233211]
    for number in numbers:
        assert is_interesting(number, []) == 2

def test_return_1_all_digits_are_palindrome_after_adding_1_or_2():
    numbers = [1219, 1220, 73835, 89697, 11233210, 11233209]
    for number in numbers:
        assert is_interesting(number, []) == 1

def test_digits_match_on_of_the_awesome_phrases():
    awesome_phrases = [1337, 266]
    assert is_interesting(1337, awesome_phrases) == 2

def test_return_1_if_close_to_interesting_number():
    numbers = [1336, 1335]
    awesome_phrases = [1337, 256]
    for number in numbers:
        assert is_interesting(number, awesome_phrases) == 1