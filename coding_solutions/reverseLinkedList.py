"""

Given a singly linked list, reverse and return it.

"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseLinkedList(l):
    if l == None:
        return l
        
    prev = None
    curr = l
    tail = curr.next
    
    while curr:
        curr.next = prev
        prev = curr
        curr = tail
        if tail:
            tail = tail.next
            
    l = prev
    
    return l