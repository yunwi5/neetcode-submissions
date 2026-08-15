class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,1,5,6,7,1]
        # buy at 1, sell at 7
        # 
        # Sliding window, only can move right.
        # compare left or right moving right, then pick the better margin.
        # 
        # Start with 10, 1 => -9
        # Move to 10, 5 => -5
        # Choose between 10 -> 1 and 5 -> 6
        # Move to 1, 5 => 4
        # Move 5 -> 6, 1, 6 => 5
        # choose between 1 -> 5 and 6 -> 7
        # Move to 1, 7 => 6
        # Do this till the end


        maxProfit = 0

        lowest = prices[0]
        for i in range(1,len(prices)):
            currPrice = prices[i]
            # print('currPrice:', currPrice)
            maxProfit = max(maxProfit, currPrice - lowest)
            # print('maxProfit:', maxProfit)
            
            lowest = min(lowest, currPrice)

        return maxProfit

        