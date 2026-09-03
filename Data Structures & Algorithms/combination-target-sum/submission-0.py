class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index: int, combination: List[int], total: int):
            if total == target:
                result.append(combination[:])
                return
            if total > target:
                return

            # case 1: add same number and continue
            combination.append(nums[index])
            backtrack(index, combination, total + nums[index])
            combination.pop()

            # case 2: go to next index and continue
            if index < len(nums) - 1:
                backtrack(index + 1, combination, total)
            

        backtrack(0, [], 0)

        return result
        