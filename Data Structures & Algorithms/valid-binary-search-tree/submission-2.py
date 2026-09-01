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

        def validateBST(node: Optional[TreeNode], minLimit: int, maxLimit: int) -> bool:
            if not node:
                return True
            
            if minLimit is not None and node.val >= minLimit:
                return False
            if maxLimit is not None and node.val <= maxLimit:
                return False

            newMinLimit = node.val if minLimit is None else min(node.val, minLimit)
            newMaxLimit = node.val if maxLimit is None else max(node.val, maxLimit)

            leftValid = validateBST(node.left, newMinLimit, maxLimit)
            rightValid = validateBST(node.right, minLimit, newMaxLimit)
            
            return leftValid and rightValid
        

        return validateBST(root, None, None)


        
        