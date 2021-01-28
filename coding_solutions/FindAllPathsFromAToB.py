"""

You are given a directed acyclic graph (DAG) that contains N nodes.

Write a function that can find all the possible paths from node 0 to node N - 1. You can return the path in any order.

graph[a] is a list of all nodes b for which the edge a -> b exists.

"""

def csFindAllPathsFromAToB(graph):
    
    ans = []
    
    def helper(vert, num, path = [0]):
        if not vert:
            ans.append(path)
        if vert:
            for num in vert:
                helper(graph[num], num, path + [num])
    helper(graph[0], 0)
    
    return ans