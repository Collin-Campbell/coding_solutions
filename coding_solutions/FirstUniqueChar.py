"""

Given a string, write a function that returns the index of the first unique 

(non-repeating) character. If there isn't a unique (non-repeating) character, 

return -1.

"""

def csFirstUniqueChar(input_str):
    str_to_list = list(input_str)
    for i in range(len(str_to_list)):
        new_str_list = str_to_list.copy()
        new_str_list.pop(i)
        if str_to_list[i] not in new_str_list:
            return i
        else:
            continue
            
    return -1