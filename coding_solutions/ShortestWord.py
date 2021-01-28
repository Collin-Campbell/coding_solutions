"""

Given a string of words, return the length of the shortest word(s).

"""

def csShortestWord(input_str):
    length = 100
    for word in input_str.split():
        if len(word) < length:
            length = len(word)
            
    return length