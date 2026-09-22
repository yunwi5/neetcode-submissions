class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        if len(nums) == 1:
            return nums[0]

        maxSum = nums[0]
        curSumMax = nums[0]

        for i in range(1, len(nums)):
            curSumMax = max(nums[i], curSumMax + nums[i])
            maxSum = max(maxSum, curSumMax)

        return maxSum

        