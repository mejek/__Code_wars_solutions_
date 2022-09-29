# This is a hard version of How many are smaller than me?. If you have troubles solving this one, have a look at the easier kata first.
#
# Write
#
# function smaller(arr)
#
# that given an array arr, you have to return the amount of numbers that are smaller than arr[i] to the right.
#
# For example:
#
# smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
# smaller([1, 2, 0]) === [1, 1, 0]


# My solution:
from collections import Counter
import numpy as np

def smaller(arr):

    # res = []
    # for x in range(len(arr)):

# too slow
#         res.append(sum((1 for c in arr[x:] if c < arr[x])))

# too slow
#         res.append(list(map(lambda a: arr[x] > a, arr[x+1:])).count(True))

# too slow
#         c = Counter(arr[x:])
#         res.append(sum([c[k] for k in c.keys() if k < arr[x]]))

# too slow
#         c = np.array(arr[x:])
#         res.append(sum(c < arr[x]))
    # return res


# too slow
    return [Counter([n for n in arr[x:] if n < arr[x]]).total() for x in range(len(arr))]
    # too slow
    return [sum(np.array(arr[x:]) < arr[x]) for x in range(len(arr))]
