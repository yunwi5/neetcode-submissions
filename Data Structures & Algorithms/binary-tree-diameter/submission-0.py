# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time: O(n)
        # Space: O(n)
        self.maxDiameter = 0
        self.dfs(root)

        return self.maxDiameter

    
    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return 0
        
        leftHeight = self.dfs(node.left)
        rightHeight = self.dfs(node.right)

        self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)

        