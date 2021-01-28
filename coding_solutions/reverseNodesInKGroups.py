"""

Note: Your solution should have O(n) time complexity, where n is the number 

of elements in l, and O(1) additional space complexity, since this is what 

you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified 

list. k is a positive integer that is less than or equal to the length of l. 

If the number of nodes in the linked list is not a multiple of k, then the 

nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be 

changed.

"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    
    if (not l.next) or (k == 1):
        return l
    
    position = l
    new_order = []
    final_order = []

    count = 0
    
    while position:
        new_order.append(position.value)
        position = position.next
        count += 1
        if count == k:
            final_order.append(new_order)
            new_order = []
            count = 0
            
    final_order.append(new_order)
    
    new_node = ListNode(42)
    ans = new_node
    
    for i in range(len(final_order)):
        if len(final_order[i]) == k:
            for n in range(k-1,-1,-1):
                new_node.next = ListNode(final_order[i][n])
                new_node = new_node.next
        else:
            for n in range(len(final_order[i])):
                new_node.next = ListNode(final_order[i][n])
                new_node = new_node.next
    
    return ans.next