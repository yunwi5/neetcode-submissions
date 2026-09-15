class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)

        n = len(nums)
        if n == 1:
            return nums[0]

        # Fill second last
        nums[n-2] = max(nums[n-2], nums[n-1])

        for i in range(n - 3, -1, -1):
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
        

        return nums[0]


        