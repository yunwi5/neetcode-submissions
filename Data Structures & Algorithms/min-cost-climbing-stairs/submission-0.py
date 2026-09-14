class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        n = len(cost)
        if n == 1:
            return 0

        last = cost[n - 1]
        secondLast = cost[n-2]

        cur = n - 3
        while cur >= -1:
            curPositionCost = cost[cur] if cur >= 0 else 0
            curCost = curPositionCost + min(last, secondLast)

            last = secondLast
            secondLast = curCost

            if cur == -1:
                return curCost

            cur -= 1


        