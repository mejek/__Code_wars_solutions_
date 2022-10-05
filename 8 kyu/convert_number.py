# Description:
# Convert number to reversed array of digits
#
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example(Input => Output):
#
# 35231 => [1,3,2,5,3]
# 0 => [0]
#
# My solution:
def digitize(n):
    l = [int(x) for x in str(n)]
    l.reverse()
    return l