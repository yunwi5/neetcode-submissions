"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, startNode: Optional['Node']) -> Optional['Node']:
        # Time: O(V + E)
        # Space: O(V + E)
        visitNodeDict = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if not node: return None
            if node.val in visitNodeDict:
                return visitNodeDict[node.val]

            newNode = Node(node.val)
            visitNodeDict[node.val] = newNode

            for neigh in node.neighbors:
                neighCopy = dfs(neigh)
                newNode.neighbors.append(neighCopy)

            return newNode

        return dfs(startNode)
        