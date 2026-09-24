"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldIdToNewNodeDict = {}

        def copyNodeExceptRandom(node: Optional[Node]):
            if not node:
                return
            
            newNode = Node(node.val)
            newNode.next = copyNodeExceptRandom(node.next)
            oldIdToNewNodeDict[id(node)] = newNode

            return newNode

        newHead = copyNodeExceptRandom(head)

        oldCur = head
        newCur = newHead
        while newCur:
            if oldCur.random is not None:
                newRandom = oldIdToNewNodeDict[id(oldCur.random)]
                newCur.random = newRandom
            
            oldCur = oldCur.next
            newCur = newCur.next
        
        return newHead

        