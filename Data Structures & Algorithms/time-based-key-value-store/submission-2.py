class TimeMap:

    def __init__(self):
        self.map = {}
        

    # Time: O(1)
    # Space: O(n) where n = number of values
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(value, timestamp)]
        else:
            self.map[key].append((value, timestamp))
        

    # Time: O(log(n))
    # Space: O(1)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        values = self.map[key]
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            midString, midTimestamp = values[mid]
            if midTimestamp == timestamp:
                return midString
            elif midTimestamp > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        lastIndex = min(left, right)
        lastValue, lastTimestamp = values[lastIndex]
        if lastTimestamp <= timestamp:
            return lastValue
        
        if lastIndex > 0:
            prevValue, prevTimestamp = values[lastIndex - 1]
            return prevValue

        return ""

        
