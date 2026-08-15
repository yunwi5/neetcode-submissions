class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = prices[0]
        for i, price in enumerate(prices, start=1):
            maxProfit = max(maxProfit, price - lowest)
            
            lowest = min(lowest, price)

        return maxProfit

        