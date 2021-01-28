"""

Given two strings that include only lowercase alpha characters, 

str_1 and str_2, write a function that returns a new sorted string that 

contains any character (only once) that appeared in str_1 or str_2.

"""

def csLongestPossible(str_1, str_2):
    ans = ''
    for letter in str_1 + str_2:
        if letter not in ans:
            ans += letter
    
    ans2 = ''
    for letter in sorted(ans):
        ans2 += letter
    
    return ans2