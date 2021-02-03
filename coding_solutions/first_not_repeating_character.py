"""

Given a string s consisting of small English letters, find and return the 

first instance of a non-repeating character in it. If there is no such character, 

return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c 

since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.

There are no characters in this string that do not repeat.

"""

def first_not_repeating_character(s):
    
    table = {}
    
    for i in range(len(s)):
        if s[i] not in table:
            table[s[i]] = 1
        else:
            table[s[i]] += 1
    
    for key,value in table.items():
        if value == 1:
            return key
            
    return '_'