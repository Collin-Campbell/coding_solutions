"""

Given a start integer and an ending integer (both inclusive), write a 

function that returns the count (not the sum) of all integers in the range 

(except integers that contain the digit 5).

"""

def csAnythingButFive(start, end):
    count = 0
    for i in range (start,end + 1):
        if '5' not in str(i):
            count += 1
            
    return count