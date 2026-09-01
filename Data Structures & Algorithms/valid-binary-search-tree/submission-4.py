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
            
            if lessThan is not None and node.val >= lessThan:
                return False
            if greaterThan is not None and node.val <= greaterThan:
                return False

            newLessThan = node.val if lessThan is None else min(node.val, lessThan)
            newGreaterThan = node.val if greaterThan is None else max(node.val, greaterThan)

            leftValid = validateBST(node.left, newLessThan, greaterThan)
            rightValid = validateBST(node.right, lessThan, newGreaterThan)
            
            return leftValid and rightValid
        

        return validateBST(root)


        
        