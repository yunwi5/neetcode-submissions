# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)

            rightest = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightest = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightest:
                result.append(rightest.val)

        return result


        