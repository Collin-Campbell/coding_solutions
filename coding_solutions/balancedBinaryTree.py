"""

You are given a binary tree and you need to write a function that can 
determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left 
and right subtrees of every node differ in height by a maximum of 1.

"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def balancedBinaryTree(root):
    
    def checker(root):
        if root is None:
            return 0
            
        left = checker(root.left)
        if left == -1:
            return -1
        
        right = checker(root.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
            
        return max(left, right) + 1


    return checker(root) > -1   