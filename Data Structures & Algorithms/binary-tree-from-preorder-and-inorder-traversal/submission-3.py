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

        preorderIndex = 0

        inorderIndexByValue = {}
        for i, item in enumerate(inorder):
            inorderIndexByValue[item] = i
        

        def dfs(inorderLeft: int, inorderRight: int):
            if inorderLeft > inorderRight:
                return

            nonlocal preorderIndex
            treeNode = TreeNode(preorder[preorderIndex])
            preorderIndex += 1

            inorderIndex = inorderIndexByValue[treeNode.val]
            treeNode.left = dfs(inorderLeft, inorderIndex - 1)
            treeNode.right = dfs(inorderIndex + 1, inorderRight)

            return treeNode
        

        return dfs(0, len(inorder) - 1)

        
        