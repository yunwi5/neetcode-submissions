class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time: O(n^2)
        # Space: O(1)

        count = 0

        # Check odd-length palindrome strings
        for i in range(len(s)):
            start, end = i, i
            while s[start] == s[end]:
                count += 1
                start -= 1
                end += 1
                if start < 0 or end >= len(s):
                    break
        
        # Check even-length palindrome strings
        for i in range(len(s) - 1):
            start, end = i, i + 1
            while s[start] == s[end]:
                count += 1
                start -= 1
                end += 1
                if start < 0 or end >= len(s):
                    break
        

        return count
