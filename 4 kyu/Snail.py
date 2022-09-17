# Description:
# Snail Sort
#
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
#
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
#
# This image will illustrate things more clearly:
#
# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
# My solution:
def snail(snail_map):
    res = []
    print(snail_map)

    while True:
        if snail_map == []:
            return res
        n = len(snail_map[0])

        if n == 1:
            res.append(snail_map[0][0])
            return res

        res += snail_map[0]
        for x in range(1, n - 1):
            res.append(snail_map[x][n - 1])
        res += snail_map[n - 1][::-1]
        for x in range(1, n - 1):
            res.append(snail_map[n - 1 - x][0])

        new_snail = []
        for s in snail_map[1:n - 1]:
            new_snail.append(s[1:-1])
        snail_map = new_snail