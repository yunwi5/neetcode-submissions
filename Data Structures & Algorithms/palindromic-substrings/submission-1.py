class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time: O(n^2)
        # Space: O(1)

        count = 0

        # Check odd-length palindrome strings
        for i in range(len(s)):
            count += self.countPali(s, i, i)

        # Check even-length palindrome strings
        for i in range(len(s) - 1):
            count += self.countPali(s, i, i + 1)
        

        return count

    def countPali(self, s, start, end):
        count = 0
        while s[start] == s[end]:
            count += 1
            start -= 1
            end += 1
            if start < 0 or end >= len(s):
                break

        return count