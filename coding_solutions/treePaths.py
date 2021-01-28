"""

Given a binary tree of integers, return all the paths from the tree's root to 
its leaves as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, 
where root is the value stored in the root and node1,node2,...,noden are the 
values stored in the 1st, 2nd,..., and nth nodes in the path respectively 
(noden representing the leaf).

"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(t):

    def helper(t, res):
        if t is None:
            return
        res.append(str(t.value))
        helper(t.left, res)
        helper(t.right, res)
        res.append('pop')

    result = []
    helper(t, result)
    
    queue = []
    final_result = []
    count = 0
    
    for i in range(len(result)):
        queue.append(result[i])
        
        if result[i] != 'pop':
            count = 0
        
        if result[i] == 'pop':
            count += 1
            
            if count == 1:
                queue.pop()
                final_result.append("->".join(queue))
                queue.pop()
            
            if count > 1:
                queue.pop()
                queue.pop()
    
    return final_result