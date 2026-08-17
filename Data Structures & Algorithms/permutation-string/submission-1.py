class Solution:
    def getCharIndex(self, char: str) -> bool:
        return ord(char) - ord('a')

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len, s2Len = len(s1), len(s2)
        if s1Len > s2Len:
            return False

        s1CharFreq = [0] * 26
        for char in s1:
            s1CharFreq[self.getCharIndex(char)] += 1
        
        s2CurrentFreq = [0] * 26
        for i in range(0, s1Len):
            char = s2[i]
            s2CurrentFreq[self.getCharIndex(char)] += 1
        
        index = s1Len
        while index < s2Len:
            if s1CharFreq == s2CurrentFreq:
                return True

            prevChar = s2[index - s1Len]
            curChar = s2[index]

            s2CurrentFreq[self.getCharIndex(prevChar)] -= 1
            s2CurrentFreq[self.getCharIndex(curChar)] += 1
            index += 1

        if s1CharFreq == s2CurrentFreq:
            return True

        return False

