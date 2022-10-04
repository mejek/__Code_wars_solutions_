# Description:
#
# Reverse every other word in a given string, then return the string. Throw away any leading or trailing
# whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated
# as if they are a part of the word in this kata.
#
#
# My solution:

def reverse_alternate(string):
    res = []
    string_split = [x for x in string.split(' ') if x != '']

    for i in range(len(string_split)):
        if i % 2 == 0:
            res.append(string_split[i])
        elif i % 2 != 0:
            res.append(string_split[i][::-1])
    return ' '.join(res)