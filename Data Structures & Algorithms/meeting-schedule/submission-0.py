"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Time: O(nlog(n))
        # Space: O(1)

        # A: [(0, 10), (12, 19), (20, 30)]
        # start = 0, end = 30
        # B: [(0, 10), (8, 21), (22, 24)]
        # start = 0, end = 10, start < end
        #
        # start > prev end

        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start < end:
                return False
            end = interval.end
        
        return True