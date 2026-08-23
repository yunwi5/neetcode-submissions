# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n + m)
        # Space: O(1)

        if not list1:
            return list2
        if not list2:
            return list1

        head = None
        combined = None
        while list1 and list2:
            if list1.val <= list2.val:
                if not combined:
                    head = list1
                    combined = list1
                else:
                    combined.next = list1
                    combined = combined.next
                
                list1 = list1.next
            else:
                if not combined:
                    head = list2
                    combined = list2
                else:
                    combined.next = list2
                    combined = combined.next

                list2 = list2.next
            
        while list1:
            combined.next = list1
            combined = combined.next
            list1 = list1.next
        
        while list2:
            combined.next = list2
            combined = combined.next
            list2 = list2.next

        return head



        