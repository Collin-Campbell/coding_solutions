"""

Write a function that takes a string as input and returns that string in 

reverse order, with the opposite casing for each character within the string.

"""

def csOppositeReverse(txt):
    reverse_string = ''
    for i in range (len(txt)-1,-1,-1):
        if txt[i].isupper() == True:
            reverse_string += txt[i].lower()
        elif txt[i].islower() == True:
            reverse_string += txt[i].upper()
        else:
            reverse_string += txt[i]
    
    return reverse_string