# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        numGoodNodes = 0

        def dfs(node: Optional[TreeNode], atLeast: int):
            if not node:
                return

            nonlocal numGoodNodes
            if node.val >= atLeast:
                numGoodNodes += 1
            
            dfs(node.left, max(atLeast, node.val))
            dfs(node.right, max(atLeast, node.val))
        

        dfs(root, -math.inf)

        return numGoodNodes

                

            

        