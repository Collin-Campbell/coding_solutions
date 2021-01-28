"""

Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand 

(i.e., [1,2,4,5,6,7] might become [4,5,6,7,1,2]).

You should search for target in nums and if found return its index, 

otherwise return -1.

"""

def csSearchRotatedSortedArray(nums, target):
    for index,num in enumerate(nums):
        if num == target:
            return index
    return -1