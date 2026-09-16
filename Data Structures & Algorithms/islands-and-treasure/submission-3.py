class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Use DFS
        # Time: O(m * n)
        # Space: O(m * n)

        ROWS = len(grid)
        COLS = len(grid[0])
        
        def bfs(rowIndex: int, colIndex: int):
            root = (rowIndex, colIndex)
            q = collections.deque([root])
            visited = set([root])

            deltas = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1),
            ]

            dist = 0
            while q:
                qLen = len(q)
                for i in range(qLen):
                    row, col = q.popleft()
                    grid[row][col] = dist

                    for (deltaY, deltaX) in deltas:
                        newRow, newCol = row + deltaY, col + deltaX
                        if newRow < 0 or newRow >= ROWS:
                            continue
                        if newCol < 0 or newCol >= COLS:
                            continue
                        if dist + 1 >= grid[newRow][newCol]:
                            continue
                        if (newRow, newCol) in visited:
                            continue
                        
                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))
                
                dist += 1
        
        for rowIndex, row in enumerate(grid):
            for colIndex, cell in enumerate(row):
                if cell == 0:
                    bfs(rowIndex, colIndex)


        