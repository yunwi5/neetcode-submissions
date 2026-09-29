class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(n)
        
        output = []
        newAdded = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                # no overlap
                output.append(interval)
            elif interval[1] <= newInterval[1]:
                # combine head
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            elif interval[0] >= newInterval[0] and interval[1] <= newInterval[1]:
                # contains
                continue
            elif newInterval[0] >= interval[0] and newInterval[1] <= interval[1]:
                # contained, no change needed
                return intervals
            elif interval[0] <= newInterval[1]:
                # combine tail
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            else:
                # no overlap
                if not newAdded:
                    output.append(newInterval)
                    newAdded = True
                output.append(interval)

        if not newAdded:
            output.append(newInterval)
            
        return output

        