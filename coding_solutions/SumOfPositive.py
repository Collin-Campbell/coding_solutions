"""

Given an array of integers, return the sum of all the positive integers in 

the array.

"""

def csSumOfPositive(input_arr):
    ans = 0
    for num in input_arr:
        if num > 0:
            ans += num
        else:
            continue
    
    return ans