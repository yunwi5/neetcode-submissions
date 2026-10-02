class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time: O(nlog(n))
        # Space: O(1)
        intervals.sort(key=lambda interval: interval[1])

        last = intervals[0]
        nonOverlappingCount = 1
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < last[1]:
                continue
            
            nonOverlappingCount += 1
            last = [start, end]
        
        return len(intervals) - nonOverlappingCount

        