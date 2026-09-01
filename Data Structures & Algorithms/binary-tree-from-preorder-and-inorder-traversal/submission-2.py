# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Time: O(n)
        # Space: O(n)

        inorderIndexByValue = {}
        for i, val in enumerate(inorder):
            inorderIndexByValue[val] = i

        preorderIndex = 0

        def dfs(l: int, r: int):
            if l > r:
                return
            
            nonlocal preorderIndex
            value = preorder[preorderIndex]
            node = TreeNode(value)
            preorderIndex += 1

            inorderIndex = inorderIndexByValue[value]

            node.left = dfs(l, inorderIndex - 1)
            node.right = dfs(inorderIndex + 1, r)

            return node

        return dfs(0, len(inorder) - 1)
        