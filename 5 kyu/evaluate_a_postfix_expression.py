# Imagine you are in a universe where you can just perform the following arithematic operations. Addition(+),
# Subtraction(-), Multiplication(*), Division(/). You are given given a postfix expression. Postfix expression
# is where operands come after operator. Each operator and operand are seperated by a space. You need to
# evaluate the expression.
#
# For example: 25 45 + is equivalent of 25 + 45, hence the answer would be 70. Instead if you are given 20 40 + 60 *,
# it is equivalent of (20+40) * 60, hence the answer should be 3600. 20 40 60 + * is equivalent of 20 * (40 + 60) = 2000.
#
# Create a method 'evaluate' that takes a string as input and returns a long resulted in the evaluation.
# Just concentrate on happy paths.
#
# Assume that expression is always valid and division is always an integer division.
#
# My solution:
def postfix_evaluator(expr):
    operations = '+-*/'

    while len(expr.split()) != 1:
        e_spli = expr.split()
        expr = ''
        for n in range(len(e_spli)-2):
            if e_spli[n+2] in operations:
                if e_spli[n+2] == '/':
                    expr += f'({e_spli[n]}/{e_spli[n+2]}{e_spli[n+1]}) '
                else:
                    expr += f'({e_spli[n]}{e_spli[n + 2]}{e_spli[n + 1]}) '
                break
            else:
                expr += f'{e_spli[n]} '
        if n+2 != len(e_spli)-1:
            expr += ' '.join(e_spli[n+3:])
    return eval(expr)


