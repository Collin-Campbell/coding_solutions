"""

Implement a queue using two stacks.

You are given an array of requests, where requests[i] can be "push <x>" 

or "pop". Return an array composed of the results of each "pop" operation 

that is performed.

"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)
            
    def remove():
        if right.isEmpty() == True:
            while left.isEmpty() == False:
                right.push(left.pop())
        number = right.pop()
        
        while right.isEmpty() == False:
            left.push(right.pop())
            
        return number

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans