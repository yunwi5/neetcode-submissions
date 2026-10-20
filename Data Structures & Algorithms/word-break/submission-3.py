class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)-1,-1,-1):
            # logic
            for word in wordDict:
                if i + len(word) > len(s):
                    continue

                if (i + len(word) == len(s) or dp[i+len(word)])and s[i:i+len(word)] == word:
                    dp[i]=True
                    break

        return dp[0]
        