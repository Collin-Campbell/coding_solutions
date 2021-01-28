"""

You are given a parentheses sequence, check if it's regular.

"""

def validParenthesesSequence(s):
    count = 0
    for item in s:
        if item == '(':
            count += 1
        if item == ')':
            count -= 1
        if count < 0:
            return False
            
    return count == 0