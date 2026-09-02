class MedianFinder:

    def __init__(self):
        self.firstHalfHeap = [] # max heap
        self.secondHalfHeap = [] # min heap

    def addNum(self, num: int) -> None:
        # Time: O(log(n))
        # Space: O(n)
        # where n = number of numbers added
        if not self.firstHalfHeap:
            self.firstHalfHeap.append(-num)
            return
        
        # Add to correct heap
        if num < -self.firstHalfHeap[0]:
            heapq.heappush(self.firstHalfHeap, -num)
        else:
            heapq.heappush(self.secondHalfHeap, num)
        
        # Calibration
        totalSize = len(self.firstHalfHeap) + len(self.secondHalfHeap)
        maxAllowedSize = math.ceil(totalSize / 2)
        if len(self.firstHalfHeap) > maxAllowedSize:
            poppedNum = -heapq.heappop(self.firstHalfHeap)
            heapq.heappush(self.secondHalfHeap, poppedNum)
        if len(self.secondHalfHeap) > maxAllowedSize:
            poppedNum = -heapq.heappop(self.secondHalfHeap)
            heapq.heappush(self.firstHalfHeap, poppedNum)

    def findMedian(self) -> float:
        # Time: O(1)
        # Space: O(1)
        if len(self.firstHalfHeap) > len(self.secondHalfHeap):
            return -self.firstHalfHeap[0]    
        elif len(self.firstHalfHeap) < len(self.secondHalfHeap):
            return self.secondHalfHeap[0]
        return (-self.firstHalfHeap[0] + self.secondHalfHeap[0]) / 2.0
        