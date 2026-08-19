class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(n + m)
        # Space: O(1)
        rowSize = len(matrix[0])
        size = len(matrix) * len(matrix[0])
        left = 0
        right = size - 1

        while left <= right:
            mid = (left + right) // 2
            rowIndex = mid // rowSize
            colIndex = mid % rowSize

            if matrix[rowIndex][colIndex] == target:
                return True

            if matrix[rowIndex][colIndex] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

        