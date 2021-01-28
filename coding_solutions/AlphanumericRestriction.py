"""

Create a function that returns True if the given string has any of the 

following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't 

fit into any category, return False.

"""

def csAlphanumericRestriction(input_str):
    if len(input_str) == 0:
        return False
    else:
        if input_str.isalpha() == True or input_str.isnumeric() == True:
            return True
        else:
            return False