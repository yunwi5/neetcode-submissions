class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Goal is to get k min distance points to origin
        # Use max heap to keep k min distance points
        # Time: O(nlog(k))
        # Space: O(k)

        maxHeap = []

        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)

            heapq.heappush(maxHeap, (-distance, point))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        
        result = [point for _, point in maxHeap]

        return result