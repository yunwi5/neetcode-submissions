class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(index: int, comb: List[int], total: int):
            if total == target:
                result.append(comb[:])
                return
            if total > target or index >= len(candidates): return
            
            nextNumIndex = index + 1
            while nextNumIndex < len(candidates) and candidates[index] == candidates[nextNumIndex]:
                nextNumIndex += 1

            # case 1: skip this num and continue
            if nextNumIndex < len(candidates) and total + candidates[nextNumIndex] <= target:
                backtrack(nextNumIndex, comb, total)

            # case 2: test all scenarios of adding num until new number appears
            for i in range(index, nextNumIndex):
                duplicateCount = nextNumIndex - i
                newTotal = total + candidates[i] * duplicateCount
                if newTotal > target:
                    continue

                backtrack(nextNumIndex, comb + [candidates[i]] * duplicateCount, newTotal) # next num is at index 2, current index is 1, it adds num * 1
            

        backtrack(0, [], 0)

        return result
        