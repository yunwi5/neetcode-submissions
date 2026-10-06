class Solution:
    def jump(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # 1 dimensional BFS

        jumps = 0
        currentEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if currentEnd == i:
                jumps += 1
                currentEnd = farthest
        
        return jumps
        