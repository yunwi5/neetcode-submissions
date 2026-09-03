class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n * 2^n)
        # Space: O(n)
        # n = # nums
        result = []

        nums.sort()

        def backtrack(index: int, path: List[int]):
            if index >= len(nums):
                result.append(path[:])
                return
            
            nextNewNumIndex = index + 1
            while nextNewNumIndex < len(nums) and nums[index] == nums[nextNewNumIndex]:
                nextNewNumIndex += 1

            # case 2: try all combination of duplicated nums
            for i in range(index, nextNewNumIndex):
                dupCount = nextNewNumIndex - i
                for j in range(dupCount):
                    path.append(nums[i])
                backtrack(nextNewNumIndex, path)
                for j in range(dupCount):
                    path.pop()

            # case 1: skip num
            backtrack(nextNewNumIndex, path)

        backtrack(0, [])

        return result