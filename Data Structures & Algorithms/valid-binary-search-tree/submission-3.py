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

        def validateBST(node: Optional[TreeNode], greaterThan: int = None, lessThan: int = None) -> bool:
            if not node:
                return True
            
            if greaterThan is not None and node.val >= greaterThan:
                return False
            if lessThan is not None and node.val <= lessThan:
                return False

            newGreaterThan = node.val if greaterThan is None else min(node.val, greaterThan)
            newLessThan = node.val if lessThan is None else max(node.val, lessThan)

            leftValid = validateBST(node.left, newGreaterThan, lessThan)
            rightValid = validateBST(node.right, greaterThan, newLessThan)
            
            return leftValid and rightValid
        

        return validateBST(root)


        
        