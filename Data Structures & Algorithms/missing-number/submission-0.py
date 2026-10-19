class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = (len(nums) + 1) * len(nums) // 2
        currentSum = sum(nums)

        return expectedSum - currentSum