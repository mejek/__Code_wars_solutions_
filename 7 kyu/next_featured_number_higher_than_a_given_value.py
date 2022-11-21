# Make a function that receives a value, val and outputs the smallest higher number than the given value,
# and this number belong to a set of positive integers that have the following properties:
#
#     their digits occur only once
#
#     they are odd
#
#     they are multiple of three
#
# next_numb(12) == 15
#
# next_numb(13) == 15
#
# next_numb(99) == 105
#
# next_numb(999999) == 1023459
#
# next_number(9999999999) == "There is no possible number that
# fulfills those requirements"
#
# Enjoy the kata!!
# My solution:
def next_numb(val):
    while True:
        val += 1
        if multiple_of_3(val):
            break

    while val < 9999999999:
        if odd_(val) and digit_occurs_only_once(val):
            return val
        else:
            val += 3

    return "There is no possible number that fulfills those requirements"

def odd_(number):
    if number % 2 == 1:
        return True
    return False

def multiple_of_3(number):
    if number % 3 == 0:
        return True
    return False

def digit_occurs_only_once(number):
    if len(set(str(number))) == len(str(number)):
        return True
    return False