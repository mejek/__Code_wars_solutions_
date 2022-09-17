# Description:
#
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
# Examples
#
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
#
# Constraints
#
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

# My solution:
def valid_parentheses(string):
    p_string = ''
    for n in string:
        if n == '(' or n == ')':
            p_string += n

    while '()' in p_string:
        p_string = p_string.replace('()', '')

    if p_string == '':
        return True
    return False
