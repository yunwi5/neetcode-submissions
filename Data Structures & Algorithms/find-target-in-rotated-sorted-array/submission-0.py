class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time: O(n)
        # Space: O(1)
        l = 0
        r = len(nums) - 1
        minIndex = 0
        while l < r:
            if nums[l] < nums[r]:
                if nums[minIndex] > nums[l]:
                    minIndex = l
                break

            mid = (l + r) // 2
            minimum = min(nums[l], nums[mid], nums[r])
            if minimum == nums[l]:
                minIndex = l
            elif minimum == nums[mid]:
                minIndex = mid
            else:
                minIndex = r
            
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1

        # list 1: 0 ... minIndex-1
        # list 2: minIndex ... len(nums)-1
        if minIndex > 0:
            l = 0
            r = minIndex - 1
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        l = minIndex
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1