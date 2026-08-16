class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        for char in s:
            if char not in sDict:
                sDict[char] = 1
            else:
                sDict[char] += 1

        for char in t:
            if char not in sDict:
                return False
            else:
                sDict[char] -= 1
                if sDict[char] < 0:
                    return False
                if sDict[char] == 0:
                    del sDict[char]
        
        return not sDict
        