class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time: O(nlog(n))
        # Space: O(n)


        intervals.sort(key=lambda i: i[0])

        result = []
        ongoing = None
        for i, interval in enumerate(intervals):
            if not ongoing:
                ongoing = interval
            elif interval[0] > ongoing[1]:
                result.append(ongoing)
                ongoing = interval
            elif interval[1] < ongoing[1]:
                continue
            else:
                ongoing = [min(interval[0], ongoing[0]), max(interval[1], ongoing[1])]
        
        if ongoing:
            result.append(ongoing)
        
        return result