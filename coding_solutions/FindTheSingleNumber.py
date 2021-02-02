"""

You are given a non-empty array of integers.

One element appears exactly once, with every other element appearing at least twice, 

perhaps more.

Write a function that can find and return the element that appears exactly once.

"""

def csFindTheSingleNumber(nums):
    table = {}
    for num in nums:
        if num in table:
            table[num] += 1
        else:
            table[num] = 1
    
    for element,appearances in table.items():
        if appearances == 1:
            return element