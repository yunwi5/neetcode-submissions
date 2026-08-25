# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n + m)
        # Space: O(1)
        #
        # while l1Cur and l2Cur:
        # total = l1Cur.val + l2Cur.val + carryOn
        # digit = total % 2
        # carryOn = total // 10 -> update
        # l1Cur.val = digit
        #
        # go to next ones
        # l1Cur = l1Cur.next
        # l2Cur = l2Cur.next
        # 
        # if only one of them left,
        # continue appending remaining digits as nodes

        resHead = None
        res = None
        l1Cur = l1
        l2Cur = l2

        carryOn = 0
        while l1Cur or l2Cur:
            total = carryOn
            if l1Cur:
                total += l1Cur.val
            if l2Cur:
                total += l2Cur.val
            
            digit = total % 10
            carryOn = total // 10

            if l1Cur: 
                l1Cur = l1Cur.next
            if l2Cur: 
                l2Cur = l2Cur.next

            if not res:
                res = ListNode(digit, None)
                resHead = res
            else:
                res.next = ListNode(digit, None)
                res = res.next

        if carryOn > 0:
            res.next = ListNode(1, None)

        return resHead

        