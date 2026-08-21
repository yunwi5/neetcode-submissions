class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time: O(nlong(m))
        # Space: O(1)
        # where n = length of array, m = largest number in array
        largest = piles[0]
        for pile in piles:
            largest = max(largest, pile)

        left = 1
        right = largest
        while left <= right:
            mid = (left + right) // 2
            totalHours = 0
            for pile in piles:
                hours = math.ceil(pile / mid)
                totalHours += hours
            
            if totalHours > h:
                left = mid + 1
            else:
                right = mid - 1

        return left

        