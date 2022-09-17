# Description:
#
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
#
# Please note that using encode is considered cheating.
# My solution:
import string

def rot13(message):
    res = ''
    print(message)
    for x in message:
        if x.lower() in string.ascii_lowercase:
            ind = string.ascii_lowercase.index(x.lower())
            if ind + 13 >= 26:
                if x.lower() == x:
                    res += string.ascii_lowercase[ind + 13 - 26]
                else:
                    res += string.ascii_lowercase[ind + 13 - 26].upper()
            else:
                if x.lower() == x:
                    res += string.ascii_lowercase[ind + 13]
                else:
                    res += string.ascii_lowercase[ind + 13].upper()
        else:
            res += x
    return res



