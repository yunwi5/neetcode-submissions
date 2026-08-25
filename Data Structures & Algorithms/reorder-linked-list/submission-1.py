# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Time: O(n)
        # Space: O(1)

        pointer = head
        n = 0
        while pointer:
            n += 1
            pointer = pointer.next

        firstHalfSize = math.ceil(n/2)
        secondHalfSize = n - firstHalfSize

        traversalNode = head
        for i in range(firstHalfSize - 1):
            traversalNode = traversalNode.next
        
        firstHalf = head
        secondHalf = traversalNode.next
        traversalNode.next = None

        # Reverse second half
        prev = None
        curr = secondHalf
        while curr:
            nextOne = curr.next
            curr.next = prev

            prev = curr
            curr = nextOne
        reversedSecondHalf = prev

        res = firstHalf
        firstHalf = firstHalf.next
        while firstHalf or reversedSecondHalf:
            if reversedSecondHalf:
                res.next = reversedSecondHalf
                res = res.next
                reversedSecondHalf = reversedSecondHalf.next
            
            if firstHalf:
                res.next = firstHalf
                res = res.next
                firstHalf = firstHalf.next
        









        