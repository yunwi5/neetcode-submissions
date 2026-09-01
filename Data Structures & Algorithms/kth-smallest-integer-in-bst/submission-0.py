# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Time: O(n)
        # Space: O(n)

        smallestNodes = []
        def inOrderTravel(node: Optional[TreeNode]):
            if not node:
                return

            nonlocal smallestNodes
            if len(smallestNodes) >= k:
                return

            inOrderTravel(node.left)
            smallestNodes.append(node.val)
            inOrderTravel(node.right)
        
        inOrderTravel(root)

        return smallestNodes[k - 1]

        


