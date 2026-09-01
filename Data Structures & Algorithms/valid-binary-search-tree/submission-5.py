# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n)
        # Space: O(n)

        def validateBST(node: Optional[TreeNode], lessThan: int = None, greaterThan: int = None) -> bool:
            if not node:
                return True
            
            if node.val >= lessThan or node.val <= greaterThan:
                return False


            return validateBST(node.left, node.val, greaterThan) and validateBST(node.right, lessThan, node.val)
        

        return validateBST(root, math.inf, -math.inf)


        
        