class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multi-source BFS
        # Time: O(n*m)
        # Space: O(n+m)

        ROWS = len(grid)
        COLS = len(grid[0])
        
        # Multi-source BFS queue
        q = collections.deque()
        unrotten = set()
        for rowIndex, row in enumerate(grid):
            for colIndex, cell in enumerate(row):
                if cell == 1:
                    unrotten.add((rowIndex, colIndex))
                if cell == 2:
                    q.append((rowIndex, colIndex))
        
        if not q:
            return -1 if unrotten else 0

        def addBananaIfExists(row: int, col: int):
            if row < 0 or row >= ROWS:
                return
            if col < 0 or col >= COLS:
                return
            if grid[row][col] != 1:
                return
            if (row, col) not in unrotten:
                return
            
            unrotten.remove((row, col))
            q.append((row, col))
            return True

        time = -1
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                addBananaIfExists(row + 1, col)
                addBananaIfExists(row, col + 1)
                addBananaIfExists(row - 1, col)
                addBananaIfExists(row, col - 1)
            time += 1
        
        if unrotten:
            return -1
        
        return time


        