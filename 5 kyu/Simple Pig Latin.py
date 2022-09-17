# Description:
#
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples
#
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
# My solution:

import string
def pig_it(text):
    letters = string.ascii_letters
    res = []
    for x in text.split(' '):
        if len(x) != 1 and x not in letters:
            res.append(x[1:]+x[0]+'ay')
        elif len(x) == 1 and x in letters:
            res.append(x + 'ay')
        else:
            res.append(x)
    return ' '.join(res)