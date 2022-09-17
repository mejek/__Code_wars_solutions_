# Description:
# Build Tower
#
# Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
#
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]
# My solution:

def tower_builder(n_floors):
    tower = []
    for n in range(1, n_floors+1):
        tower.append(' '*(n_floors-n) + '*'*((2*n)-1) + ' '*(n_floors-n))
    return tower