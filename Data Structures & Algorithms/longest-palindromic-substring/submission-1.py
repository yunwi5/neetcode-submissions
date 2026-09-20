class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(n^2)
        # Space: O(1)

        resultL, resultR = 0, 0
        for i in range(len(s)):
            l, r = i, i
            while True:
                if l == 0 or r == len(s) - 1:
                    break
                if s[l-1] != s[r+1]:
                    break
                l -= 1
                r += 1

            if r - l > resultR - resultL:
                resultL = l
                resultR = r

        for i in range(len(s)-1):
            l, r = i, i+1
            if s[l] != s[r]:
                continue

            while True:
                if l == 0 or r == len(s) - 1:
                    break
                if s[l-1] != s[r+1]:
                    break
                
                l -= 1
                r += 1
            
            if r - l > resultR - resultL:
                resultL = l
                resultR = r
        
        return s[resultL:resultR+1]
        