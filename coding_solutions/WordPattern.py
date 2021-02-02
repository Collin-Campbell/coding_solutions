"""

Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one 

correspondence between a letter in pattern and a non-empty word in s.

"""

def csWordPattern(pattern, a):
    
    if len(pattern) != len(a.split()):
        return False
        
    table_a = {}
    table_pattern = {}
    
    for index,element in enumerate(a.split()):
        if element not in table_a:
            table_a[element] = [index]
        else:
            table_a[element].append(index)
            
    for index,letter in enumerate(pattern):
        if letter not in table_pattern:
            table_pattern[letter] = [index]
        else:
            table_pattern[letter].append(index)
    
    return list(table_a.values()) == list(table_pattern.values())