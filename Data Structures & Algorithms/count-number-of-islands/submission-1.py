class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Use visited(nxm) to track which node visited
        # Use BFS to travel nodes
        # init islandCounts = 0
        #
        # Time: O(n * m)
        # Space: O(n * m)
        # n = # rows, m = # cols

        islandCount = 0

        rowCount = len(grid)
        colCount = len(grid[0])

        visited = [
            [False] * len(grid[0]) for i in range(len(grid))
        ]

        def bfs(rowIndex: int, colIndex: int):
            # Perform bfs
            q = collections.deque([(rowIndex, colIndex)])
            visited[rowIndex][colIndex] = True

            while q:
                for i in range(len(q)):
                    (row, col) = q.popleft()
                    options = [
                        (-1, 0),
                        (0, -1),
                        (1, 0),
                        (0, 1),
                    ]
                    for (rowDelta, colDelta) in options:
                        rowOption = row + rowDelta
                        colOption = col + colDelta
                        if rowOption < 0 or rowOption >= rowCount or colOption < 0 or colOption >= colCount:
                            continue
                        
                        if visited[rowOption][colOption]:
                            continue
                        if grid[rowOption][colOption] != "1":
                            continue
                        
                        q.append((rowOption, colOption))
                        visited[rowOption][colOption] = True

        for rowIndex, row in enumerate(grid):
            for colIndex, cell in enumerate(row):
                if cell == "1" and not visited[rowIndex][colIndex]:
                    islandCount += 1
                    bfs(rowIndex, colIndex)

                visited[rowIndex][colIndex] = True

        return islandCount
                
        
