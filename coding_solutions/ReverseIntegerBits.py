"""

Given an integer, write a function that reverses the bits (in binary) and 

returns the integer result.

"""

def csReverseIntegerBits(n):
    reversed_str = ''
    for i in range(len(bin(n))-1,1,-1):
        reversed_str += str(bin(n))[i] 
    
    return int(reversed_str, 2)