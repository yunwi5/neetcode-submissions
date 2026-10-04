class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpPosition = len(nums) - 1

        for i in range(len(nums)-1,-1,-1):
            if nums[i] + i >= jumpPosition:
                jumpPosition = i
        
        return True if jumpPosition == 0 else False
