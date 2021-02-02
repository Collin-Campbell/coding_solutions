"""

Given an array of strings strs, write a function that can group the anagrams. 

The groups should be ordered such that the larger groups come first, with subsequent 

groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a different word 

or phrase, typically using all the original letters exactly once.

"""

def csGroupAnagrams(strs):

    table = {}
    anagram_check = []
    index_grouped = {}
        
    for index,word in enumerate(strs):
        table[index] = {}
        for letter in word:
            if letter not in table[index]:
                table[index][letter] = 1
            else:
                table[index][letter] += 1
    
    for position in table:
        anagram_check.append(sorted(table[position]))
    
    for i in range(len(anagram_check)):
        if ''.join(anagram_check[i]) not in index_grouped:
            index_grouped[''.join(anagram_check[i])] = [strs[i]]
        else:
            index_grouped[''.join(anagram_check[i])].append(strs[i]) 
       
    return list(index_grouped.values())