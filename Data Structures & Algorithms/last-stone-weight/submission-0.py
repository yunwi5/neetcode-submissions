class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # O(nlogn)
        # O(n)
        #
        # Constructing heap: O(nlogn)
        # Remove two and insert 1 (if not both destroyed): O(logn), do it for whole stones, it is O(nlogn)
        # Time: O(nlogon)
        #
        
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while heap:
            largest = -heapq.heappop(heap)
            if not heap:
                return largest

            nextLargest = -heapq.heappop(heap)

            remain = largest - nextLargest
            if remain > 0:
                heapq.heappush(heap, -remain)
        
        return 0


        