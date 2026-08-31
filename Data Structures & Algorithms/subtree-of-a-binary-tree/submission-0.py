# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time: O(n * m)
        # Space: O(n * m)
        # n = # nodes in root, m = # nodes in subroot

        subtree = False


        def dfs(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            nonlocal subtree
            if subtree:
                return
            
            if not root or not subRoot:
                return

            if root.val == subRoot.val:
                sameTree = isSameTree(root, subRoot)
                if sameTree:
                    subtree = True
                    return
            
            dfs(root.left, subRoot)
            dfs(root.right, subRoot)


        def isSameTree(root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
            if not root and not sub:
                return True
            if not root or not sub:
                return False
            
            sameLeft = isSameTree(root.left, sub.left)
            sameRight = isSameTree(root.right, sub.right)

            return root.val == sub.val and sameLeft and sameRight
        
        dfs(root, subRoot)

        return subtree
            
        

            




        