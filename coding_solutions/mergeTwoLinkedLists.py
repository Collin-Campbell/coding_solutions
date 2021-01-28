"""

Note: Your solution should have O(l1.length + l2.length) time complexity, 

since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is 

to merge them. In other words, return a singly linked list, also sorted in 

non-decreasing order, that contains the elements from both original lists.

"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    l = ListNode(42)
    ll = l
    
    while l1 or l2:
        if l1 and (not l2 or l1.value <= l2.value):
            l.next = ListNode(l1.value)
            l1 = l1.next
        else:
            l.next = ListNode(l2.value)
            l2 = l2.next
            
        l = l.next
    
    return ll.next