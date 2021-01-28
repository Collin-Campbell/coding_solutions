"""

You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's index. If the target value is not present in the array, return -1.

You may assume no duplicate exists in the array.

"""

def findValueSortedShiftedArray(nums, target):
    for index,number in enumerate(nums):
        if number == target:
            return index
    
    return -1