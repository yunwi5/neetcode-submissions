class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums

        # Min heap in O(nlog(n))
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]
