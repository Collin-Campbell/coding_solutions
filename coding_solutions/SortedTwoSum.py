"""

Given a sorted array (in ascending order) of integers and a target, write a 

function that finds the two integers that add up to the target.

"""

def csSortedTwoSum(numbers, target):
    ans = []
    for index,value in enumerate(numbers):
        for i in range(len(numbers)):
            if numbers[i] + value == target and numbers[i] != value:
                ans.append(index)
                ans.append(i)
                return ans
            else:
                continue