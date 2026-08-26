# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)
        #
        # [1, 2, 3, 4]
        # left = 0, right = n = 2
        #
        # start at 1, 3
        # shift towards 2, 4
        # right.next == None, hence left.next is index n - 2. 
        #
        # left.next = left.next.next
        # return head
        #
        # head = [1, 3], n = 1
        # return [3]
        # left = index 0, right = index 1
        # 
        # left = node 3, right = None
        # 
        # head = [1, 3, 5], n = 1
        # left = node 1, right = node 3
        # while
        # left = node 3, right = 5

        # Handle sz = 1, n = 1 like [1]
        if not head.next:
            return None 
        
        # Two pointers
        left = head
        right = head
        for i in range(n):
            right = right.next
        
        # Handle sz >= 1, n = sz like [1, 2], n = 2
        if not right:
            return left.next

        # push right until no next element left
        while right and right.next:
            left = left.next
            right = right.next

        # Handle sz > 1, n = 1 like [1, 2]
        left.next = left.next.next

        return head

        