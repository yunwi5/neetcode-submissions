class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # chosen [True, False, True]
        # True if the element was chosen
        def backtrack(path: List[int], chosen: List[bool]):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            notChosenIndices = [i for i, val in enumerate(chosen) if val == False]
            for index in notChosenIndices:
                path.append(nums[index])
                chosen[index] = True
                backtrack(path, chosen)
                path.pop()
                chosen[index] = False         
            
        backtrack([], [False] * len(nums))

        return result
        