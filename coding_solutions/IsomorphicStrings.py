"""

Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another character while 

preserving the order of characters. No two characters may map to the same character 

but a character may map to itself.

"""

def csIsomorphicStrings(a, b):
    
    if len(a) != len(b):
        return False
        
    table_a = {}
    table_b = {}
    
    for index,letter in enumerate(a):
        if letter not in table_a:
            table_a[letter] = [index]
        else:
            table_a[letter].append(index)
    
    for index,letter in enumerate(b):
        if letter not in table_b:
            table_b[letter] = [index]
        else:
            table_b[letter].append(index)
    
    
    return list(table_a.values()) == list(table_b.values())