"""

Given a string sequence consisting of the characters 

'(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not 

the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.

"""

def validBracketSequence(sequence):
    parenthesis = 0
    square_bracket = 0
    curly_bracket = 0
    checker = []
    
    for bracket in sequence:
        if bracket == '(':
            parenthesis += 1
            checker.append('p')
            
        if bracket == ')':
            parenthesis -= 1
            if parenthesis < 0:
                return False
            check = checker.pop()
            if check != 'p':
                return False
            
        if bracket == '[':
            square_bracket += 1
            checker.append('s')
            
        if bracket == ']':
            square_bracket -= 1
            if square_bracket < 0:
                return False
            check = checker.pop()
            if check != 's':
                return False
            
        if bracket == '{':
            curly_bracket += 1
            checker.append('c')
            
        if bracket == '}':
            curly_bracket -= 1
            if curly_bracket < 0:
                return False
            check = checker.pop()
            if check != 'c':
                return False   
            
    if (parenthesis != 0) or (square_bracket != 0) or (curly_bracket != 0):
        return False
        
    return True  