"""

Write a function that searches a list of names (unsorted) for the name "Bob" 

and returns the location in the list. If Bob is not in the array, return -1.

"""

def csWhereIsBob(names):
    for i,name in enumerate(names):
        if name == 'Bob':
            return i
    return -1