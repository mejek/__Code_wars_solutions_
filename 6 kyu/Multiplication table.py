# Description:
#
# Your task, is to create NxN multiplication table, of size provided in parameter.
#
# for example, when given size is 3:
#
# 1 2 3
# 2 4 6
# 3 6 9
#
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
#
# My solution:

def multiplication_table(size):
    res = []
    print(size)
    for x in range(size):
        a = []
        for y in range(size):
            a.append((x+1)*(y+1))
        res.append(a)
    return res