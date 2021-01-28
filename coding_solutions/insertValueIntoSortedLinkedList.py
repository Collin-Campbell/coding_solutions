"""

Note: Your solution should have O(n) time complexity, where n is the number 

of elements in l, since this is what you will be asked to accomplish in an 

interview.

You have a singly linked list l, which is sorted in strictly increasing 

order, and an integer value. Add value to the list l, preserving its original 

sorting.

Note: in examples below and tests preview linked lists are presented as 

arrays just for simplicity of visualization: in real data you will be given 

a head node l of the linked list

"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):
    
    if not l:
        l = ListNode(value)
        return l
    
    if value < l.value:
        new_node = ListNode(value)
        new_node.next = l
        l = new_node
        return l
        
    else:
        current = l
        upcoming = l.next
          
        while upcoming is not None:  
            if current.value < value < upcoming.value:
                new_node = ListNode(value)
                current.next = new_node
                new_node.next = upcoming
            
            current = current.next
            upcoming = upcoming.next
        
        if value > current.value:
            new_node = ListNode(value)
            current.next = new_node
    
        return l