# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        pPath = []
        current = root
        while True:
            pPath.append(current)
            if current.val == p.val:
                break
            
            if current.val > p.val:
                current = current.left
            else:
                current = current.right

        
        qPath = []
        current = root
        while True:
            qPath.append(current)
            if current.val == q.val:
                break
            
            if current.val > q.val:
                current = current.left
            else:
                current = current.right

        

        ancestor = root
        for pAnc, qAnc in zip(pPath, qPath):
            if pAnc.val == qAnc.val:
                ancestor = pAnc
            else:
                break
        
        return ancestor

        