# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(n)
        if not root:
            return []

        q = deque([(root, 1)])
        orderTraversal = []
        while q:
            node, level = q.popleft()

            if len(orderTraversal) < level:
                orderTraversal.append([node.val])
            else:
                orderTraversal[-1].append(node.val)
            
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        
        return orderTraversal
