# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # preorder traversal
        # make it a full tree with nulls as child.
        # Time: O(n)
        # Space: O(n)
        result = []
        q = deque([(root, 0)])
        level = 0
        while q:
            qLen = len(q)

            for i in range(qLen):
                node, nodeIndex = q.popleft()
                if not node:
                    continue
                result.append('|'.join([str(node.val), str(nodeIndex)]))

                if node.left:
                    leftIndex = 2 * nodeIndex + 1
                    q.append((node.left, leftIndex))
                if node.right:
                    rightIndex = 2 * nodeIndex + 2
                    q.append((node.right, rightIndex))

        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        bfsList = data.split(',')
        if not bfsList or bfsList[0] == '':
            return None
        
        nodeMapByIndex = {}
        for nodePair in bfsList:
            nodeVal, nodeIndex = nodePair.split('|')
            nodeMapByIndex[int(nodeIndex)] = int(nodeVal)

        rootVal = nodeMapByIndex[0]
        root = TreeNode(int(rootVal))
        q = deque([(root, 0)])

        while q:
            node, bfsIndex = q.popleft()
            leftIndex = bfsIndex * 2 + 1
            rightIndex = bfsIndex * 2 + 2

            if leftIndex in nodeMapByIndex:
                leftVal = nodeMapByIndex[leftIndex]
                leftNode = TreeNode(leftVal)
                node.left = leftNode
                q.append((leftNode, leftIndex))
            if rightIndex in nodeMapByIndex:
                rightVal = nodeMapByIndex[rightIndex]
                rightNode = TreeNode(int(rightVal))
                node.right = rightNode
                q.append((rightNode, rightIndex))
            
        return root

