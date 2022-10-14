# Description:
# How does an abacus work?
#
# An abacus is a mechanical tool for counting and performing simple mathematical operations.
# It consists of vertical poles with beads, where the position of the beads indicates the
# value stored on the abacus. The abacus in the image below, for example, is storing the number 1703.
#
# Each pole represents a decimal digit of the number, where the rightmost pole indicates
# the ones digit, the second to the right the tens digit, the third to the right the hundreds digit, and so on.
#
# Each pole is split into an upper and a lower portion. Each bead in the lower portion
# represents a single unit for the pole (1 for the ones pole, 10 for the tens pole,
# 100 for the hundreds pole, etc.) The bead in the upper portion represents 5 units
# for the pole (5 for the ones pole, 50 for the tens pole, 500 for the hundreds pole, etc.)
#
# For the upper portion of the pole, the bead is counted if it is in the down position.
# For the lower portion of the pole, a bead is counted if it is in the up position.
# Task
#
# For this kata you will need to write two functions:
#
#     An encoding function which will take an int as input and return a string
#     representing that number stored on an abacus
#     A decoding function which will take as input a string representing an abacus
#     and return the number on the abacus as an int
#
# An abacus will be represented as a string where a '*' character represents a bead,
# a ' ' (space) character represents an empty spot on the pole, and a '-' character
# represents the dividing line between the upper and lower portions.
#
# For example, the abacus in the image above (representing the number 1703) would be represented as:
#
# ****** **
#       *
# ---------
#      ** *
# ***** ***
# ****** **
# ********
# *********
#
# or
#
# '****** **\n      *  \n---------\n     ** *\n***** ***\n****** **\n******** \n*********'
#
# Notes:
#
#     All abacus representations will have 9 poles
#     Input to the encoding function will be constrained to 0 <= n <= 999999999
#     Input to the decoding function will always be a valid abacus representation
#
# My solution:

ab_dict = {'* - ****': '0',
           '* -* ***': '1',
           '* -** **': '2',
           '* -*** *': '3',
           '* -**** ': '4',
           ' *- ****': '5',
           ' *-* ***': '6',
           ' *-** **': '7',
           ' *-*** *': '8',
           ' *-**** ': '9'
           }
def create_abacus(n):
    #fill all numbers:
    number = ''
    for _ in range(9):
        if 9 - len(number) > len(str(n)):
            number += '0'
        else:
            number += str(n)
            break
    res = []

    for n in number:
        if int(n) >= 5:
            line = ' *-' + '*'*(4+int(n)-9) + ' ' + '*'*(9-int(n))

        else:
            line = '* -' + '*'*int(n) + ' ' + '*'*(4-int(n))
        res.append(line)
    print(res)
    rot = list(list(x)[::-1] for x in zip(*res))
    print([''.join(x for x in y[::-1]) for y in rot])
    return '\n'.join([''.join(x for x in y[::-1]) for y in rot])

def read_abacus(abacus):
    res = ''
    for n in range(9):
        line = ''
        for a in abacus.split('\n'):
            line += a[n]
        res += ab_dict[line]
    return int(res)

