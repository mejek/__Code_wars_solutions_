# Description:
#
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
#
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
#
# My solution:
def find_uniq(arr):
    numbers = list(set(arr))

    for n in numbers:
        if arr.count(n) == 1:
            return n
        else:
            pass