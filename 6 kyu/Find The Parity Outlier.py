# Description:
#
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
# Examples
#
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)
#
# My solution:
def find_outlier(integers):
    odd = 0
    even = 0
    for n in integers[:3]:
        if n%2 == 0:
            even +=1
        else:
            odd +=1
    if odd > even:
        for n in integers:
            if n%2 == 0:
                return n
    else:
        for n in integers:
            if n%2 != 0:
                return n