class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick select
        # Time: O(n)
        # Space: O(n)


        kIndex = len(nums) - k

        def quickSelect(l: int, r: int):
            p, pivotValue = l, nums[r]
            for i in range(l, r):
                if nums[i] < pivotValue:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]

            if kIndex < p:
                return quickSelect(l, p - 1)
            elif kIndex > p:
                return quickSelect(p + 1, r)
            return nums[p]

        return quickSelect(0, len(nums) - 1)