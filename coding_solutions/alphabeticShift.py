"""

Given a string, your task is to replace each of its characters by the 

next one in the English alphabet; i.e. replace a with b, replace b with c, 

etc (z would be replaced by a).

"""

def alphabeticShift(inputString):
    #97(a) - 122(z)
    to_list = list(inputString)
    for i in range(len(to_list)):
        if to_list[i] == 'z':
            to_list[i] = 'a'
        else:
            to_list[i] = chr(ord(to_list[i]) + 1)
    
    return ''.join(to_list)