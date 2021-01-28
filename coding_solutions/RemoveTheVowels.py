"""

Given a string, return a new string with all the vowels removed.

"""

def csRemoveTheVowels(input_str):
    ans = ''
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for letter in input_str:
        if letter not in vowels:
            ans += letter
            
    return ans