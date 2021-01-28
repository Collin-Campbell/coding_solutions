"""

For a given positive integer n determine if it can be represented 

as a sum of two Fibonacci numbers (possibly equal).

"""

def fibonacciSimpleSum2(n):
    fib_list = [0,1]
    pos = 0
    while fib_list[-1] < n:
        fib_list.append(fib_list[pos] + fib_list[pos + 1])
        pos += 1
    
    for i in range(len(fib_list)):
        for j in range(len(fib_list)):
            if (fib_list[i] + fib_list[j]) == n:
                return True

    return False