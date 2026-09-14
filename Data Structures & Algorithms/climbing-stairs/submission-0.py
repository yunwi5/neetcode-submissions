class Solution:
    def climbStairs(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        if n == 1:
            return 1
        dp = [0] * n

        dp[n-1] = 1
        dp[n-2] = 2

        cur = n - 3
        while cur >= 0:
            ways = dp[cur + 1] + dp[cur + 2]
            dp[cur] = ways
            cur -= 1
        
        return dp[0]

        