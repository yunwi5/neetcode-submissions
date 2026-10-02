class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time: O(nlog(n))
        # Space: O(n)
        intervals.sort(key=lambda i: i[0])

        result = []
        ongoing = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] > ongoing[1]:
                result.append(ongoing)
                ongoing = interval
            else:
                ongoing = [min(interval[0], ongoing[0]), max(interval[1], ongoing[1])]
        
        if ongoing:
            result.append(ongoing)
        
        return result