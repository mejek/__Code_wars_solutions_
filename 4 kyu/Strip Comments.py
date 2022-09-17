# Description:
#
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
#
# Example:
#
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
#
# The output expected would be:
#
# apples, pears
# grapes
# bananas
#
# The code would be called like so:
#
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"
#
# My solution:
def strip_comments(strng, markers):
    res = ''
    for s in strng.split('\n'):
        for m in markers:
            if m in s:
                s = s[:s.index(m)].rstrip()
        res += s + '\n'
    return res[:-1]