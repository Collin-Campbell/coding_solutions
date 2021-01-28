"""

Create a function that given an integer, returns an integer where every 

digit in the input integer is squared.

"""

def csSquareAllDigits(n):
    ans = ''
    for num in str(n):
        ans += str(int(num)**2)
    
    return int(ans)