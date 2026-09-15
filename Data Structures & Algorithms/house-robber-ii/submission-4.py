class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n
        if len(nums) <= 3:
            return max(nums)
        
        # First half
        n = len(nums) - 1
        firstNums = nums[0:-1]
        firstNums[n-2] = max(firstNums[n-2], firstNums[n-1])

        for i in range(n - 3, -1, -1):
            firstNums[i] = max(firstNums[i] + firstNums[i+2], firstNums[i+1])
        
        # second half
        secondNums = nums[1:]
        secondNums[n-2] = max(secondNums[n-2], secondNums[n-1])
        for i in range(n - 3, -1, -1):
            secondNums[i] = max(secondNums[i] + secondNums[i+2], secondNums[i+1])
        
        return max(firstNums[0], secondNums[0])
       
        