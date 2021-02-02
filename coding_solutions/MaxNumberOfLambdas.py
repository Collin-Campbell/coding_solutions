"""

Given a string text, you need to use the characters of text to form as many 

instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that 

can be formed.

"""

def csMaxNumberOfLambdas(text):

    checker = {'l':0,'a':0,'m':0,'b':0,'d':0}
    
    for letter in text:
        if letter in checker:
            checker[letter] += 1
    
    checker['a'] = checker['a'] // 2
    
    ans = []
    
    for letter,num in checker.items():
        ans.append(num)
    
    return min(ans)