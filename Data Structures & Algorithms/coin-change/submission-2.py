class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time: O(n * t)
        # Space: O(t)
        # n = # coins, t = target amount

        minCoinsByRemaining = {}

        def dfs(remaining: int) -> int:
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0
            if remaining in minCoinsByRemaining:
                return minCoinsByRemaining[remaining]

            # Loop through choices
            minCoin = math.inf
            for coin in coins:
                coinsNeeded = dfs(remaining - coin)
                if coinsNeeded == -1:
                    continue
                minCoin = min(minCoin, coinsNeeded + 1)

            minCoinsByRemaining[remaining] = minCoin

            if minCoin == math.inf:
                return -1

            return minCoin

        
        return dfs(amount)
        