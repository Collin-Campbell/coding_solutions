"""

Two words are blanagrams if they are anagrams but exactly one letter 

has been substituted for another.

Given two words, check if they are blanagrams of each other.

"""

def checkBlanagrams(word1, word2):
    checker = list(word2)
    
    for letter in word1:
        if letter in checker:
            checker.remove(letter)
    
    return (len(checker) == 1)