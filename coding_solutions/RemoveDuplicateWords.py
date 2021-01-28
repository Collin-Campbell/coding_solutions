"""

Given a string, write a function that removes all duplicate words from the 

input. The string that you return should only contain the first occurrence of 

each word in the string.

"""

def csRemoveDuplicateWords(input_str):
    return ' '.join(sorted(set(input_str.split(' ')),key=input_str.split(' ').index))