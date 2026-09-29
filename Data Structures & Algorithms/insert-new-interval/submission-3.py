class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(n)
        
        output = []
        newAdded = False
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                output.append(newInterval)
                return output + intervals[i:]
            if newInterval[0] > interval[1]:
                output.append(interval)
            else:
                newInterval = [min(newInterval[0],  interval[0]), max(newInterval[1],  interval[1])]

        output.append(newInterval)
           
        return output

        