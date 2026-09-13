class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time: O(n * m)
        # Space: O(n * m)

        maxArea = 0
        visit = [
            [False] * len(grid[0]) for i in range(len(grid))
        ]
        rowLen = len(grid)
        colLen = len(grid[0])

        def bfs(rowIndex: int, colIndex: int) -> int:
            area = 1
            q = collections.deque([(rowIndex, colIndex)])
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()

                    delta = [
                        (1, 0), # bottom
                        (0, 1), # right
                        (-1, 0), # top
                        (0, -1), # left
                    ]

                    for deltaY, deltaX in delta:
                        r = row + deltaY
                        c = col + deltaX

                        if r < 0 or r >= rowLen:
                            continue
                        if c < 0 or c >= colLen:
                            continue
                        if visit[r][c]:
                            continue

                        visit[r][c] = True
                        if grid[r][c] != 1:
                            continue

                        area += 1
                        q.append((r, c))

            return area

        for rowIndex, row in enumerate(grid):
            for colIndex, cell in enumerate(row):
                if visit[rowIndex][colIndex]:
                    continue

                visit[rowIndex][colIndex] = True
                if cell == 1:
                    area = bfs(rowIndex, colIndex)
                    maxArea = max(area, maxArea)

        return maxArea
