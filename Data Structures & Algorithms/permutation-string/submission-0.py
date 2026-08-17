from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = Counter(s1)
        
        index = 0
        s1Len, s2Len = len(s1), len(s2)
        while index <= s2Len - s1Len:
            if s1Counter[s2[index]] == 0:
                index += 1
                continue

            s2SubStringCounter = Counter(s2[index:index+s1Len])
            if s1Counter == s2SubStringCounter:
                return True

            index += 1

        return False
        