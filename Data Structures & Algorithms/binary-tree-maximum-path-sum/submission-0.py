# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Time: O(n)
        # Space: O(n)

        maxSum = -math.inf

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            
            leftMaxSum = dfs(node.left)
            rightMaxSum = dfs(node.right)

            nonlocal maxSum
            maxBranchSum = max(node.val, node.val + leftMaxSum, node.val + rightMaxSum)
            maxSumAtNode = max(maxBranchSum, node.val + leftMaxSum + rightMaxSum)
            maxSum = max(maxSum, maxSumAtNode)

            return maxBranchSum

        dfs(root)

        return maxSum



        