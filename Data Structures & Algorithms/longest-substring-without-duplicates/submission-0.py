class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        start = 0
        maxLen = 1

        dupCheckDict = {}
        for i, char in enumerate(s):
            if char in dupCheckDict:
                currentCharIndex = dupCheckDict[char]
                if currentCharIndex >= start:
                    start = currentCharIndex + 1

            dupCheckDict[char] = i
            maxLen = max(maxLen, i - start + 1)

        return maxLen
