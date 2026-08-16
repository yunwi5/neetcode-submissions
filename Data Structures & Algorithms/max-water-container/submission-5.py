class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heightLen = len(heights)
        maxArea = 0
        left = 0
        right = heightLen - 1


        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            maxArea = max(maxArea, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        
        return maxArea
      
       

        