class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        left = 0
        right = len(nums) - 1

        curMin = nums[0]
        while left < right:
            mid = (left + right) // 2
            curMin = min(nums[left], nums[right], nums[mid])

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return curMin
        