# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Construct list of all nums Time: O(n), Space: O(n)
        # Heapify the list - Time: O(n)
        # Heappop all from the list - Time: O(nlog(n))
        #
        # Approach 2
        # Heap of size k, val: (value, node)
        # While heap not empty, pop min, popped node goes to next node, then heappush the new node
        # 
        # Every node gets added to heap (log(k)), then removed (1).
        # Time: O(nlog(k))
        # Space: O(k)

        
        minHeap = []
        counter = 0
        for listNode in lists:
            if listNode:
                heapq.heappush(minHeap, (listNode.val, counter, listNode))
                counter += 1
        
        mergedHead = ListNode(0) # Dummy node
        mergedCurrent = mergedHead
        while minHeap:
            _, _, listNode = heapq.heappop(minHeap)
            mergedCurrent.next = listNode
            mergedCurrent = listNode

            if listNode.next:
                heapq.heappush(minHeap, (listNode.next.val, counter, listNode.next))
                counter += 1


        return mergedHead.next

