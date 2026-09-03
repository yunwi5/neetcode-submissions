class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n * 2^n)
        # Space: O(n * 2^n)
        result = []

        def backtrack(index: int, path: List[int]):
            # Base case
            if index == len(nums):
                result.append(path[:])
                return
            
            # Scenario 1: append number at index
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            # Scenario 2: don't append at index
            backtrack(index + 1, path)

        
        backtrack(0, [])

        return result