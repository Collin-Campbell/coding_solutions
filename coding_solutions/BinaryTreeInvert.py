"""

Given a binary tree, write a function that inverts the tree.

"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBinaryTreeInvert(root):
    
    if root is None:
        return root
    
    else:
        curr = root
        csBinaryTreeInvert(root.left) 
        csBinaryTreeInvert(root.right)
        
        curr = root.left
        root.left = root.right
        root.right = curr
        
        return root