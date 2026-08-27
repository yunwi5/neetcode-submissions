class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)   
        # Floyd's cycle detection

        slow = 0
        fast = 0

        while fast < len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break

        secondSlow = 0
        while True:
            slow = nums[slow]
            secondSlow = nums[secondSlow]

            if slow == secondSlow:
                return slow
        
