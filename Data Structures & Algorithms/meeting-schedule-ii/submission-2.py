"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Time: O(nlog(n))
        # Space: O(n)
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda interval: interval.start)
        heap = [intervals[0].end]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            smallest = heap[0]
            if interval.start >= smallest:
                heapq.heappop(heap)
            
            heapq.heappush(heap, interval.end)
            
        return len(heap)

