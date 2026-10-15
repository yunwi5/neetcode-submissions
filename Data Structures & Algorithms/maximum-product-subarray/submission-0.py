class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane's algorithm
        # Time: O(n)
        # Space: O(1)

        globalMax, maxProduct, minProduct = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            newMaxUpdate = maxProduct * num
            newMinUpdate = minProduct * num

            globalMax = max(globalMax, num, newMaxUpdate, newMinUpdate)

            maxProduct = max(num, newMaxUpdate, newMinUpdate)
            minProduct = min(num, newMaxUpdate, newMinUpdate)

        
        return globalMax

        