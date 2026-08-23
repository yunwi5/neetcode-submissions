# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n) 
        # Space: O(1)

        if not head:
            return None

        prevNode = None
        node = head
        while node.next:
            # n1 -> n2 -> n3
            # n1 <- n2 <- n3
            nextNode = node.next
            node.next = prevNode
            
            prevNode = node
            node = nextNode

        if prevNode is not None:
            node.next = prevNode

        return node

            


        