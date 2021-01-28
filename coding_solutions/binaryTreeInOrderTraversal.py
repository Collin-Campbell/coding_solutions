"""

You are given a binary tree. Write a function that returns the binary tree's 

node values using an in-order traversal.

"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def binaryTreeInOrderTraversal(root,result=[]):
    
    if root:
        binaryTreeInOrderTraversal(root.left)
        result.append(root.value)
        binaryTreeInOrderTraversal(root.right)
    
    return result